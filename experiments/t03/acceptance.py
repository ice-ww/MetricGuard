"""Actual-container resource acceptance with hand-fixed reference answers."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path
from typing import Any, Callable, Protocol

import duckdb

from experiments.t02.acceptance import create_fixture
from experiments.t02.sandbox import Sandbox


class ResourceSandbox(Protocol):
    snapshot: Path

    def query(self, sql: str) -> dict[str, Any]: ...
    def probe(self, sql: str) -> dict[str, Any]: ...
    def fault(self, name: str) -> dict[str, Any]: ...
    def inspect_environment(self) -> dict[str, Any]: ...


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(image: str, output: Path, *, executor_factory: Callable[[Path], ResourceSandbox] | None = None) -> dict[str, Any]:
    output.mkdir(parents=True, exist_ok=False)
    normal_path = create_fixture(output / "normal.duckdb")
    factory = executor_factory or (lambda path: Sandbox(image, path))
    normal = factory(normal_path)
    checks: list[dict[str, Any]] = []

    def record(name: str, passed: bool, expected: Any, actual: Any) -> None:
        checks.append({"name": name, "passed": passed, "expected": expected, "actual": actual})
        print(f"{name}: {'PASS' if passed else 'FAIL'}", flush=True)

    audit = normal.inspect_environment()
    resources = audit["worker"]["resources"]
    record("effective_os_limits", resources["memory_max_bytes"] == "536870912"
           and resources["memory_swap_max_bytes"] == "0" and resources["tmp_total_bytes"] == 16777216,
           {"memory_bytes": 536870912, "swap_bytes": 0, "tmp_bytes": 16777216}, resources)
    original_hash = digest(normal_path)
    first = normal.query("SELECT sum(amount) FROM sales")
    record("independent_reference_10_plus_20_plus_7", first.get("rows") == [[37]], [[37]], first)

    many_path = create_fixture(output / "many.duckdb")
    with duckdb.connect(str(many_path)) as con:
        con.execute("DELETE FROM sales")
        con.execute("INSERT INTO sales SELECT i, 1, 1 FROM range(1,1002) r(i)")
    many = factory(many_path)
    truncated = many.query("SELECT id FROM sales ORDER BY id")
    rows = truncated.pop("rows", [])
    record("1001_rows_keep_first_1000", truncated.get("status") == "ok"
           and truncated.get("truncated") is True and len(rows) == 1000
           and rows == [[i] for i in range(1, 1001)],
           {"rows": 1000, "first": [1], "last": [1000], "truncated": True},
           {**truncated, "row_count": len(rows), "first": rows[:1], "last": rows[-1:]})
    exact = many.query("SELECT id FROM sales ORDER BY id LIMIT 1000")
    exact_rows = exact.pop("rows", [])
    record("exactly_1000_rows_not_truncated", exact.get("status") == "ok"
           and exact.get("truncated") is False and exact_rows == [[i] for i in range(1, 1001)],
           {"rows": 1000, "truncated": False}, {**exact, "row_count": len(exact_rows)})

    giant_path = create_fixture(output / "giant.duckdb")
    with duckdb.connect(str(giant_path)) as con:
        con.execute("UPDATE regions SET name=repeat('x',70000) WHERE id=1")
    total_path = create_fixture(output / "total.duckdb")
    with duckdb.connect(str(total_path)) as con:
        con.execute("DELETE FROM sales")
        con.execute("INSERT INTO sales SELECT i,1,1 FROM range(1000) r(i)")
        con.execute("UPDATE regions SET name=repeat('x',2000) WHERE id=1")
    heavy = "SELECT sum(a.amount+b.amount+c.amount+d.amount) FROM sales a CROSS JOIN sales b CROSS JOIN sales c CROSS JOIN sales d"
    cases = [
        ("giant_cell", factory(giant_path), "query", "SELECT name FROM regions WHERE id=1", {"output_limit"}),
        ("aggregate_bytes", factory(total_path), "query", "SELECT r.name FROM sales s JOIN regions r ON s.region_id=r.id", {"output_limit"}),
        ("column_width", normal, "query", "SELECT " + ",".join(f"1 AS c{i}" for i in range(65)), {"output_limit"}),
        ("parser_pressure", normal, "query", "SELECT " + "(" * 40 + "1" + ")" * 40, {"policy_denied"}),
        ("real_sql_timeout", many, "query", heavy, {"timeout"}),
        ("real_engine_memory_pressure", normal, "probe", "SELECT i FROM range(100000000) r(i) ORDER BY hash(i)", {"engine_memory", "engine_disk"}),
        ("late_result", normal, "fault", "late_result", {"timeout"}),
        ("os_oom", normal, "fault", "oom", {"oom"}),
        ("tmpfs_full", normal, "fault", "disk", {"engine_disk"}),
        ("worker_crash", normal, "fault", "crash", {"crash"}),
        ("descendant_timeout", normal, "fault", "child_timeout", {"timeout"}),
    ]
    for name, sandbox, mode, sql, statuses in cases:
        before = digest(sandbox.snapshot)
        result = getattr(sandbox, mode)(sql)
        record(name, result.get("status") in statuses, sorted(statuses), {"input": sql, "result": result})
        record(name + "_cleanup", result.get("cleanup_verified") is True, True, result.get("cleanup_verified"))
        record(name + "_snapshot_unchanged", digest(sandbox.snapshot) == before, before, digest(sandbox.snapshot))
        if result.get("status") == "timeout":
            record(name + "_deadline_and_cleanup_latency", 4.9 <= result.get("query_seconds", 0) <= 6
                   and 0 <= result.get("termination_delay_seconds", -1) <= 5,
                   "query_seconds in [4.9,6]; termination_delay_seconds in [0,5]",
                   {key: result.get(key) for key in ("query_seconds", "termination_delay_seconds", "cleanup_seconds")})
            record(name + "_rejects_late_evidence", "rows" not in result and result.get("late_result_discarded") is True,
                   "no rows, late_result_discarded=true", result)
        if name == "tmpfs_full":
            record("tmpfs_real_enospc", result.get("errno") == 28, 28, result.get("errno"))
        if name == "descendant_timeout":
            events = result.get("fault_events", [])
            record("descendant_was_alive_with_temp_file", any(event.get("child_alive") is True
                   and event.get("child_tmp_created") is True and event.get("child_pid", 0) > 0 for event in events),
                   "live child with created /tmp/child before container removal", events)
        recovery = normal.query("SELECT sum(amount) FROM sales")
        record(name + "_next_query_recovers", recovery.get("status") == "ok" and recovery.get("rows") == [[37]]
               and recovery.get("cleanup_verified") is True and digest(normal_path) == original_hash,
               {"rows": [[37]], "cleanup_verified": True, "snapshot_unchanged": True}, recovery)
    report = {"suite": "T03 actual-container acceptance v1", "image": image,
              "host_python": platform.python_version(), "host_platform": platform.platform(),
              "automatic_pass": all(check["passed"] for check in checks),
              "checks_passed": sum(check["passed"] for check in checks), "checks_total": len(checks),
              "environment": audit, "checks": checks,
              "limitations": ["SQL admission deadline excludes container bootstrap; cleanup is measured separately.",
                              "OOM and disk fault injection are trusted test-only APIs, not Agent endpoints.",
                              "Container disappearance establishes cgroup removal; this does not claim host-wide absence of unrelated processes."]}
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run(args.image, args.output)
    print(json.dumps({key: report[key] for key in ("automatic_pass", "checks_passed", "checks_total")}))
    if not report["automatic_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
