"""Fail-closed Docker execution harness for T02. No local SQL fallback."""

import json
import math
import queue
import re
import subprocess
import threading
import time
from pathlib import Path
from typing import Any


class SandboxUnavailable(RuntimeError):
    """Safe categorical diagnosis; raw Docker errors stay out of task artifacts."""
    def __init__(self, message: str, *, code: str = 'unspecified'):
        super().__init__(message)
        self.code = code


def docker(*args: str, timeout: float = 30, input: str | None = None) -> str:
    try:
        result = subprocess.run(["docker", *args], input=input, text=True, capture_output=True,
                                encoding="utf-8", timeout=timeout, check=True)
        return result.stdout
    except subprocess.CalledProcessError as exc:
        raise SandboxUnavailable(f"Docker isolation unavailable: {exc.stderr[-1000:]}", code="docker_command_failed") from exc
    except (OSError, subprocess.SubprocessError) as exc:
        raise SandboxUnavailable(f"Docker isolation unavailable: {exc}", code="docker_timeout" if isinstance(exc, subprocess.TimeoutExpired) else "docker_unavailable") from exc


class Sandbox:
    def __init__(self, image: str, snapshot: Path, *, deadline_seconds: float = 5.0):
        if not math.isfinite(deadline_seconds) or not 0 < deadline_seconds <= 5:
            raise SandboxUnavailable("SQL deadline must be positive and at most 5 seconds", code="invalid_deadline")
        self.deadline_seconds = deadline_seconds
        if not re.fullmatch(r"sha256:[0-9a-f]{64}", image):
            raise SandboxUnavailable("An immutable image ID is required", code="invalid_image")
        self.snapshot = snapshot.resolve()
        if not self.snapshot.is_file() or self.snapshot.suffix != ".duckdb":
            raise SandboxUnavailable("A dedicated snapshot file is required", code="invalid_snapshot")
        if "," in str(self.snapshot):
            raise SandboxUnavailable("Invalid snapshot mount path", code="invalid_mount")
        self.image = image

    def _run(self, mode: str, sql: str = "") -> dict[str, Any]:
        if mode == "query" and len(sql.encode("utf-8")) > 8192:
            return {"status": "policy_denied", "error": "SQL byte limit exceeded"}
        if len(sql.encode("utf-8")) > 32768:
            return {"status": "policy_denied", "error": "Experiment request byte limit exceeded"}
        request = {"mode": mode, "sql": sql, "fault": sql if mode == "fault" else ""}
        request_bytes = (json.dumps(request)+"\n").encode()
        if len(request_bytes) > 65536:
            return {"status": "policy_denied", "error": "Encoded request byte limit exceeded"}
        started = time.monotonic()
        container = docker("create", "--pull=never", "--interactive", "--network=none", "--read-only", "--user=65532:65532",
                           "--cap-drop=ALL", "--security-opt=no-new-privileges", "--pids-limit=64",
                           "--memory=512m", "--memory-swap=512m", "--cpus=1",
                           "--tmpfs=/tmp:rw,noexec,nosuid,nodev,size=16777216",
                           "--mount", f"type=bind,source={self.snapshot},target=/data/snapshot.duckdb,readonly",
                           self.image).strip()
        process = None
        reader = None
        stop_reader = threading.Event()
        response: dict[str, Any] = {}
        admitted: float | None = None
        try:
            inspected = json.loads(docker("inspect", container))[0]
            host, config, mounts = inspected["HostConfig"], inspected["Config"], inspected["Mounts"]
            verified = (inspected["Image"] == self.image and host["NetworkMode"] == "none"
                        and host["ReadonlyRootfs"] and config["User"] == "65532:65532"
                        and host["CapDrop"] == ["ALL"] and not host["CapAdd"] and not host["Privileged"]
                        and "no-new-privileges" in host["SecurityOpt"] and host["PidsLimit"] == 64
                        and host["Memory"] == 536870912 and host["MemorySwap"] == 536870912
                        and host["NanoCpus"] == 1000000000
                        and host["Tmpfs"] == {"/tmp": "rw,noexec,nosuid,nodev,size=16777216"}
                        and len(mounts) == 1 and mounts[0]["Type"] == "bind"
                        and mounts[0]["Destination"] == "/data/snapshot.duckdb" and not mounts[0]["RW"])
            if not verified:
                raise SandboxUnavailable("Docker effective isolation configuration mismatch", code="isolation_mismatch")
            # Bounded line protocol: bootstrap readiness is separate from the
            # SQL budget. Deadline includes send, parse, execute, fetch, encode,
            # transport, host JSON decode and worker exit; late results discarded.
            process = subprocess.Popen(["docker", "start", "--attach", "--interactive", container],
                                       stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                       stderr=subprocess.DEVNULL)
            messages: queue.Queue[bytes] = queue.Queue(maxsize=2)

            def read_messages() -> None:
                assert process is not None and process.stdout is not None
                while not stop_reader.is_set():
                    line = process.stdout.readline(1024 * 1024 + 1)
                    while not stop_reader.is_set():
                        try:
                            messages.put(line, timeout=.1)
                            break
                        except queue.Full:
                            continue
                    if not line or len(line) > 1024 * 1024:
                        break

            reader = threading.Thread(target=read_messages, daemon=True)
            reader.start()
            try:
                ready_line = messages.get(timeout=max(.01, 30-(time.monotonic()-started)))
            except queue.Empty as exc:
                raise SandboxUnavailable("Worker bootstrap deadline exceeded", code="bootstrap_timeout") from exc
            ready = json.loads(ready_line or b'{}')
            if ready.get("ready") is not True:
                raise SandboxUnavailable(ready.get("error", "Worker did not attest readiness"), code="bootstrap_denied")
            admitted = time.monotonic()
            assert process.stdin is not None
            process.stdin.write(request_bytes)
            process.stdin.flush()
            process.stdin.close()
            events: list[dict[str, Any]] = []
            try:
                while True:
                    result_line = messages.get(timeout=max(.001, self.deadline_seconds-(time.monotonic()-admitted)))
                    if len(result_line) > 1024 * 1024:
                        response = {"status": "output_limit", "error": "Worker protocol byte limit"}
                    elif result_line:
                        response = json.loads(result_line)
                    if response.get("status") == "fault_running" and len(events) < 8:
                        events.append(response)
                        response = {}
                        continue
                    break
                process.wait(timeout=max(.001, self.deadline_seconds-(time.monotonic()-admitted)))
                if not response:
                    state = json.loads(docker("inspect", container))[0]["State"]
                    response = {"status": "oom" if state["OOMKilled"] else "crash", "exit_code": state["ExitCode"]}
                if time.monotonic()-admitted >= self.deadline_seconds:
                    response = {"status": "timeout", "late_result_discarded": True}
            except (queue.Empty, subprocess.TimeoutExpired):
                response = {"status": "timeout", "late_result_discarded": True}
            response["fault_events"] = events
            response["query_seconds"] = time.monotonic()-admitted
            response["startup_seconds"] = admitted-started
            if response["status"] == "environment_denied":
                raise SandboxUnavailable(response.get("error", "Worker refused environment"), code="environment_denied")
            if mode == "audit":
                response.update(verified=True, docker={"image": inspected["Image"], "host_config": host,
                                                       "mounts": mounts, "config": config})
        finally:
            cleanup_start = time.monotonic()
            try:
                docker("rm", "--force", container)
            finally:
                stop_reader.set()
                if process is not None:
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=5)
                    if reader is not None:
                        reader.join(timeout=1)
                    if process.stdout is not None:
                        process.stdout.close()
                    if process.stdin is not None and not process.stdin.closed:
                        process.stdin.close()
            remaining = docker("ps", "--all", "--quiet", "--filter", f"id={container}").strip()
            if remaining:
                raise SandboxUnavailable("Container cleanup could not be verified", code="cleanup_unverified")
            response.update(container_id=container, cleanup_verified=True,
                            cleanup_seconds=time.monotonic()-cleanup_start,
                            total_seconds=time.monotonic()-started)
            if admitted is not None:
                response["termination_delay_seconds"] = max(0.0, time.monotonic()-admitted-self.deadline_seconds) if response.get("status") == "timeout" else 0.0
        return response

    def query(self, sql: str) -> dict[str, Any]:
        return self._run("query", sql)

    def probe(self, sql: str) -> dict[str, Any]:
        """Privileged test harness only. Never expose this AST bypass to an Agent."""
        return self._run("probe", sql)

    def inspect_environment(self) -> dict[str, Any]:
        return self._run("audit")

    def fault(self, name: str) -> dict[str, Any]:
        """Controlled development fault injection; never expose to Agent tools."""
        return self._run("fault", name)
