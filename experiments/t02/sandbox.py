"""Fail-closed Docker execution harness for T02. No local SQL fallback."""

import json
import re
import subprocess
from pathlib import Path
from typing import Any


class SandboxUnavailable(RuntimeError):
    pass


def docker(*args: str, timeout: float = 30, input: str | None = None) -> str:
    try:
        result = subprocess.run(["docker", *args], input=input, text=True, capture_output=True,
                                encoding="utf-8", timeout=timeout, check=True)
        return result.stdout
    except subprocess.CalledProcessError as exc:
        raise SandboxUnavailable(f"Docker isolation unavailable: {exc.stderr[-1000:]}") from exc
    except (OSError, subprocess.SubprocessError) as exc:
        raise SandboxUnavailable(f"Docker isolation unavailable: {exc}") from exc


class Sandbox:
    def __init__(self, image: str, snapshot: Path):
        if not re.fullmatch(r"sha256:[0-9a-f]{64}", image):
            raise SandboxUnavailable("An immutable image ID is required")
        self.snapshot = snapshot.resolve()
        if not self.snapshot.is_file() or self.snapshot.suffix != ".duckdb":
            raise SandboxUnavailable("A dedicated snapshot file is required")
        if "," in str(self.snapshot):
            raise SandboxUnavailable("Invalid snapshot mount path")
        self.image = image

    def _run(self, mode: str, sql: str = "") -> dict[str, Any]:
        container = docker("create", "--pull=never", "--interactive", "--network=none", "--read-only", "--user=65532:65532",
                           "--cap-drop=ALL", "--security-opt=no-new-privileges", "--pids-limit=64",
                           "--memory=512m", "--memory-swap=512m", "--cpus=1",
                           "--tmpfs=/tmp:rw,noexec,nosuid,nodev,size=16777216",
                           "--mount", f"type=bind,source={self.snapshot},target=/data/snapshot.duckdb,readonly",
                           self.image).strip()
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
                raise SandboxUnavailable("Docker effective isolation configuration mismatch")
            response = json.loads(docker("start", "--attach", "--interactive", container,
                                         input=json.dumps({"mode": mode, "sql": sql})+"\n"))
            if response["status"] == "environment_denied":
                raise SandboxUnavailable(response.get("error", "Worker refused environment"))
            if mode == "audit":
                response.update(verified=True, docker={"image": inspected["Image"], "host_config": host,
                                                       "mounts": mounts, "config": config})
            return response
        finally:
            docker("rm", "--force", container)

    def query(self, sql: str) -> dict[str, Any]:
        return self._run("query", sql)

    def probe(self, sql: str) -> dict[str, Any]:
        """Privileged test harness only. Never expose this AST bypass to an Agent."""
        return self._run("probe", sql)

    def inspect_environment(self) -> dict[str, Any]:
        return self._run("audit")
