"""Trusted container bootstrap. Probe mode is test-only, never an Agent endpoint."""

import json
import os
import socket
import sys
from pathlib import Path
from typing import TYPE_CHECKING

import duckdb
import sqlglot

sys.path.insert(0, "/app")
if TYPE_CHECKING:
    from .policy import PolicyError, validate_sql
else:
    from policy import PolicyError, validate_sql

CONFIG = {
    "enable_external_access": "false",
    "allow_community_extensions": "false",
    "allow_unsigned_extensions": "false",
    "autoinstall_known_extensions": "false",
    "autoload_known_extensions": "false",
    "python_enable_replacements": "false",
    "python_scan_all_frames": "false",
    "threads": "1",
    "memory_limit": "128MB",
    "max_temp_directory_size": "0B",
    "temp_directory": "",
}


def audit() -> dict:
    status = dict(line.split(":", 1) for line in Path("/proc/self/status").read_text().splitlines() if ":" in line)
    denied = False
    try:
        Path("/root-write-canary").write_text("ISOLATED_TEST_ONLY")
    except OSError:
        denied = True
    network_denied = False
    try:
        with socket.create_connection(("192.0.2.1", 9), timeout=.2):
            pass
    except OSError:
        network_denied = True
    return {"uid": int(status["Uid"].split()[0]), "cap_eff": status["CapEff"].strip(),
            "no_new_privs": status["NoNewPrivs"].strip(),
            "network_interfaces": sorted(p.name for p in Path("/sys/class/net").iterdir()),
            "env_names": sorted(os.environ), "write_root_denied": denied,
            "network_connect_denied": network_denied,
            "canary_readable": Path("/canary.txt").read_text() == "T02_PUBLIC_CONTROL",
            "marker_absent": all(not Path(p).exists() for p in
                               ("/secrets/marker.txt", "/secrets/task.sqlite", "/secrets/golden.json",
                                "/secrets/credentials.txt", "/task.sqlite", "/golden.json", "/repository")),
            "app_files": sorted(p.name for p in Path("/app").iterdir())}


def main() -> dict:
    runtime = audit()
    if not (runtime["uid"] == 65532 and int(runtime["cap_eff"], 16) == 0
            and runtime["no_new_privs"] == "1" and runtime["network_interfaces"] == ["lo"]
            and runtime["write_root_denied"] and runtime["network_connect_denied"] and runtime["marker_absent"]):
        return {"status": "environment_denied", "error": "Runtime isolation attestation failed"}
    if duckdb.__version__ != "1.5.6" or sqlglot.__version__ != "30.22.0" or sys.version_info[:3] != (3, 12, 10):
        return {"status": "environment_denied", "error": "Unvalidated runtime version"}
    try:
        con = duckdb.connect("/data/snapshot.duckdb", read_only=True, config=dict(CONFIG))
        con.execute("SET allowed_configs=[]")
        con.execute("SET lock_configuration=true")
        settings = dict(con.execute("SELECT name,value FROM duckdb_settings()").fetchall())
        for key, value in CONFIG.items():
            expected = {"memory_limit": "122.0 MiB", "max_temp_directory_size": "0 bytes"}.get(key, value)
            if settings[key] != expected:
                raise ValueError(f"Unexpected effective {key}: {settings[key]!r}")
        # DuckDB 1.5.6 adds these exact DB/WAL exceptions when external
        # access is disabled. Only the DB exists; /data is not writable.
        expected_paths = {"/data/snapshot.duckdb"+suffix for suffix in
                          ("", ".wal", ".wal.checkpoint", ".wal.recovery")}
        if set(con.execute("SELECT current_setting('allowed_paths')").fetchall()[0][0]) != expected_paths:
            raise ValueError("Unapproved path exception")
        directories = con.execute("SELECT current_setting('allowed_directories')").fetchall()[0][0]
        if directories != []:
            raise ValueError(f"Unapproved directory exception: {directories!r}")
        for key, value in {"allowed_configs": "[]", "lock_configuration": "true", "access_mode": "read_only"}.items():
            if settings[key].lower() != value:
                raise ValueError(f"Unexpected {key}")
        tables = con.execute("SELECT table_schema,table_name,table_type FROM information_schema.tables ORDER BY table_schema,table_name").fetchall()
        if tables != [("main", "regions", "BASE TABLE"), ("main", "sales", "BASE TABLE")]:
            raise ValueError("Snapshot must contain only reviewed physical tables")
        columns = con.execute("SELECT table_name,column_name,data_type FROM information_schema.columns ORDER BY table_name,ordinal_position").fetchall()
        if columns != [("regions", "id", "INTEGER"), ("regions", "name", "VARCHAR"),
                       ("sales", "id", "INTEGER"), ("sales", "region_id", "INTEGER"), ("sales", "amount", "INTEGER")]:
            raise ValueError("Snapshot columns do not match the reviewed schema")
        if con.execute("SELECT count(*) FROM duckdb_functions() WHERE NOT internal").fetchall()[0][0]:
            raise ValueError("Snapshot has custom functions or macros")
    except Exception as exc:
        return {"status": "environment_denied", "error": str(exc)}
    request = json.loads(sys.stdin.readline(65537))
    info = {"settings": {k: settings[k] for k in (*CONFIG, "allowed_paths", "allowed_directories", "allowed_configs", "lock_configuration", "access_mode")},
            "versions": {"duckdb": duckdb.__version__, "sqlglot": sqlglot.__version__, "python": sys.version.split()[0]}}
    if request["mode"] == "audit":
        return {"status": "ok", "worker": runtime, **info}
    sql = request["sql"]
    # A real replacement-scan-compatible object, not merely an absent name.
    replacement_scan_canary = con.sql("SELECT 'ISOLATED_REPLACEMENT_CANARY' AS marker")
    if request["mode"] == "query":
        try:
            sql = validate_sql(sql)
        except PolicyError as exc:
            return {"status": "policy_denied", "error": str(exc), **info}
    elif request["mode"] != "probe":
        return {"status": "environment_denied", "error": "Unknown entry mode"}
    try:
        rows = con.execute(sql).fetchmany(1001)
        return {"status": "ok", "rows": rows[:1000], "truncated": len(rows)>1000, **info}
    except Exception as exc:
        return {"status": "engine_denied", "error_type": type(exc).__name__, "error": str(exc), **info}


if __name__ == "__main__":
    try:
        result = main()
    except Exception as exc:
        result = {"status": "environment_denied", "error": str(exc)}
    print(json.dumps(result, default=str))
