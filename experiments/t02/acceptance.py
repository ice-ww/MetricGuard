"""Independent black-box checks for the T02 sandbox, never host SQL probes.

Run against the candidate/final adapter rather than importing its validator or
worker. Expected numbers below are hand calculated from three fixture rows.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path
from typing import Any, Protocol

import duckdb


class QuerySandbox(Protocol):
    def query(self, sql: str) -> dict[str, Any]: ...
    def probe(self, sql: str) -> dict[str, Any]: ...
    def inspect_environment(self) -> dict[str, Any]: ...


def create_fixture(path: Path) -> Path:
    """Create only public analysis tables; private markers never enter DuckDB."""
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with duckdb.connect(str(path)) as connection:
        connection.execute("CREATE TABLE sales(id INTEGER, region_id INTEGER, amount INTEGER)")
        connection.execute("INSERT INTO sales VALUES (1, 1, 10), (2, 1, 20), (3, 2, 7)")
        connection.execute("CREATE TABLE regions(id INTEGER, name VARCHAR)")
        connection.execute("INSERT INTO regions VALUES (1, 'East'), (2, 'West')")
    return path


NORMAL_CASES: tuple[tuple[str, str, list[list[Any]]], ...] = (
    ("select", "SELECT id, amount FROM sales ORDER BY id", [[1, 10], [2, 20], [3, 7]]),
    ("nonrecursive_cte", "WITH selected AS (SELECT amount FROM sales WHERE region_id = 1) SELECT sum(amount) AS total FROM selected", [[30]]),
    ("aggregate", "SELECT count(*) AS n, sum(amount) AS total FROM sales", [[3, 37]]),
    ("join", "SELECT r.name, sum(s.amount) AS total FROM sales s JOIN regions r ON s.region_id = r.id GROUP BY r.name ORDER BY r.name", [["East", 30], ["West", 7]]),
    ("nested_select", "SELECT amount FROM sales WHERE amount > (SELECT avg(amount) FROM sales) ORDER BY amount", [[20]]),
    ("quoted_case", 'SELECT "ID", amount FROM "Sales" WHERE "ID" = 3', [[3, 7]]),
)

# Engine-only probes intentionally bypass AST *inside* the same isolation.
# Metadata and dynamic query are allowed by DuckDB; AST owns their prohibition.
DENIED_CASES: tuple[tuple[str, str, bool], ...] = (
    ("present_file", "SELECT * FROM read_text('/canary.txt')", True),
    ("absolute_file", "SELECT * FROM read_text('/secrets/marker.txt')", True),
    ("relative_file", "SELECT * FROM read_text('../secrets/marker.txt')", True),
    ("file_relation", "SELECT * FROM '/secrets/marker.csv'", True),
    ("network", "SELECT * FROM read_csv('https://127.0.0.1:9/marker.csv')", True),
    ("metadata", "SELECT table_name FROM information_schema.tables", False),
    ("metadata_function", "SELECT name FROM duckdb_settings()", False),
    ("dynamic_query", "SELECT * FROM query('SELECT amount FROM sales')", False),
    ("dynamic_table", "SELECT * FROM query_table('sales')", False),
    ("extension_install", "INSTALL httpfs", True),
    ("extension_load", "LOAD httpfs", True),
    ("macro_external_read", "CREATE TEMP MACRO leak() AS TABLE SELECT * FROM read_text('/secrets/marker.txt'); SELECT * FROM leak()", True),
    ("unregistered_udf", "SELECT private_udf(amount) FROM sales", True),
    ("replacement_scan", "SELECT * FROM replacement_scan_canary", True),
    ("reenable_replacement", "SET python_enable_replacements = true", True),
    ("reenable_external", "SET enable_external_access = true", True),
    ("path_exception", "SET allowed_paths = ['/secrets/marker.txt']", True),
    ("unlock_configuration", "SET lock_configuration = false", True),
    ("write_database", "DELETE FROM sales", True),
    ("attach", "ATTACH '/secrets/task.sqlite' AS private", True),
    ("copy", "COPY sales TO '/tmp/export.csv'", True),
    ("multiple_statements", "SELECT amount FROM sales; SELECT * FROM read_text('/secrets/marker.txt')", True),
    ("comment_hidden_statement", "SELECT amount FROM sales; /* another statement */ SET enable_external_access = true", True),
    ("nested_dynamic", "WITH hidden AS (SELECT * FROM query('SELECT amount FROM sales')) SELECT * FROM hidden", False),
    ("recursive_cte", "WITH RECURSIVE x(n) AS (SELECT 1 UNION ALL SELECT n+1 FROM x WHERE n<3) SELECT n FROM x", False),
)


def run_acceptance(sandbox: QuerySandbox, *, host_marker_value: str = "T02_PRIVATE_MARKER") -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def record(name: str, passed: bool, expected: Any, actual: Any) -> None:
        checks.append({"name": name, "passed": passed, "expected": expected, "actual": actual})

    environment = sandbox.inspect_environment()
    record("isolation_verified", environment.get("verified") is True, True, environment)
    worker = environment.get("worker", {})
    for flag in ("marker_absent", "write_root_denied", "network_connect_denied", "canary_readable"):
        record(f"os_{flag}", worker.get(flag) is True, True, worker.get(flag))
    record("nonroot", isinstance(worker.get("uid"), int) and worker["uid"] != 0, "uid != 0", worker.get("uid"))
    record("no_new_privileges", worker.get("no_new_privs") in (1, "1", True), 1, worker.get("no_new_privs"))

    for name, sql, expected in NORMAL_CASES:
        result = sandbox.query(sql)
        record(name, result.get("status") == "ok" and result.get("rows") == expected,
               {"status": "ok", "rows": expected}, {"sql": sql, "result": result})
    for name, sql, must_engine_deny in DENIED_CASES:
        public = sandbox.query(sql)
        record(f"public_{name}", public.get("status") == "policy_denied", "policy_denied", {"sql": sql, "result": public})
        bypass = sandbox.probe(sql)
        expected_statuses = ("engine_denied",) if must_engine_deny else ("ok", "engine_denied")
        record(f"isolated_bypass_{name}", bypass.get("status") in expected_statuses,
               list(expected_statuses), {"sql": sql, "result": bypass,
                                        "owner": "engine/OS" if must_engine_deny else "AST policy; any engine denial is additional defense"})
        if name in ("present_file", "absolute_file", "relative_file"):
            error = str(bypass.get("error", "")).lower()
            permission_denied = ("permission" in error or "external access" in error) and not (
                "no files found" in error or "no such file" in error
            )
            record(f"external_access_enforced_{name}", permission_denied,
                   "permission/external-access rejection, not missing file", bypass.get("error"))
        # Denial is never counted as demonstrated by a crash or unavailable engine.
        record(f"private_marker_absent_{name}", host_marker_value not in json.dumps(bypass, ensure_ascii=False),
               "no private marker value returned", "absent" if host_marker_value not in json.dumps(bypass) else "LEAK")
        if name == "replacement_scan":
            replacement_leaked = "ISOLATED_REPLACEMENT_CANARY" in json.dumps(bypass)
            record("live_replacement_canary_not_readable", not replacement_leaked,
                   "live worker Python relation cannot be queried", "LEAK" if replacement_leaked else "absent")
    return {"suite": "T02 independent acceptance v1", "automatic_pass": all(c["passed"] for c in checks),
            "checks_passed": sum(c["passed"] for c in checks), "checks_total": len(checks),
            "environment": environment, "checks": checks,
            "limitations": ["Only isolated marker data is tested; not a universal sandbox security proof.",
                            "UDF check uses an unregistered function; replacement scan uses a live worker relation and disabled effective settings.",
                            "Metadata, dynamic SQL and harmless macros require AST policy; engine access denial is not claimed.",
                            "T03 resource/timeout budgets are outside this suite."]}


def run_invalid_snapshot_checks(image: str, output: Path) -> dict[str, Any]:
    """Trusted fixture preparation; all attempted query execution is isolated."""
    from experiments.t02.sandbox import Sandbox, SandboxUnavailable

    output.mkdir(parents=True, exist_ok=False)
    alterations = {
        "wrong_column": "ALTER TABLE sales RENAME amount TO private_amount",
        "stored_macro": "CREATE MACRO private_macro() AS 17",
        "extra_schema": "CREATE SCHEMA hidden; CREATE TABLE hidden.marker AS SELECT 'ISOLATED_TEST_ONLY' AS marker",
    }
    checks = []
    for name, sql in alterations.items():
        fixture = create_fixture(output / f"{name}.duckdb")
        with duckdb.connect(str(fixture)) as connection:
            connection.execute(sql)
        try:
            result = Sandbox(image=image, snapshot=fixture).query("SELECT id FROM sales")
        except SandboxUnavailable as exc:
            # Require bootstrap's specific rejection, not a disconnected daemon.
            reason = str(exc)
            expected = "custom functions or macros" if name == "stored_macro" else "Snapshot"
            checks.append({"name": name, "passed": expected in reason,
                           "expected": "environment_denied by snapshot validation", "actual": reason})
        else:
            checks.append({"name": name, "passed": False, "actual": result})
    report = {"automatic_pass": all(check["passed"] for check in checks), "checks": checks}
    (output / "results.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main() -> None:
    from experiments.t02.sandbox import Sandbox, SandboxUnavailable

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    fixture = create_fixture(args.output / "public" / "snapshot.duckdb")
    private = args.output / "secrets"
    private.mkdir()
    marker = "T02_PRIVATE_MARKER_" + hashlib.sha256(str(args.output.resolve()).encode()).hexdigest()
    (private / "marker.txt").write_text(marker, encoding="utf-8")
    (private / "marker.csv").write_text("secret\n" + marker + "\n", encoding="utf-8")
    for name in ("task.sqlite", "golden.json", "repository.txt", "credentials.txt"):
        (private / name).write_text(marker, encoding="utf-8")
    before = hashlib.sha256(fixture.read_bytes()).hexdigest()
    try:
        report = run_acceptance(Sandbox(image=args.image, snapshot=fixture), host_marker_value=marker)
    except SandboxUnavailable as exc:
        report = {"suite": "T02 independent acceptance v1", "automatic_pass": False,
                  "status": "environment_denied", "reason": str(exc)}
    report["host_python"] = platform.python_version()
    report["snapshot_sha256_before"] = before
    report["snapshot_sha256_after"] = hashlib.sha256(fixture.read_bytes()).hexdigest()
    report["snapshot_unchanged"] = report["snapshot_sha256_after"] == before
    report["automatic_pass"] = bool(report["automatic_pass"] and report["snapshot_unchanged"])
    try:
        unavailable_result = Sandbox(image="sha256:" + "0" * 64, snapshot=fixture).query("SELECT id FROM sales")
    except SandboxUnavailable as exc:
        report["unavailable_image"] = {"passed": True, "status": "environment_denied", "reason": str(exc)}
    else:
        report["unavailable_image"] = {"passed": False, "actual": unavailable_result}
        report["automatic_pass"] = False
    report["invalid_snapshots"] = run_invalid_snapshot_checks(args.image, args.output / "invalid_snapshots")
    report["automatic_pass"] = bool(report["automatic_pass"] and report["invalid_snapshots"]["automatic_pass"])
    output = args.output / "results.json"
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"automatic_pass": report["automatic_pass"], "report": str(output)}, ensure_ascii=False))
    raise SystemExit(0 if report["automatic_pass"] else 1)


if __name__ == "__main__":
    main()
