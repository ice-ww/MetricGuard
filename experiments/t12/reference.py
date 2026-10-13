"""Development-only A1 oracle: raw rows and Python sets, independent of runtime SQL."""

import argparse
import json
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import duckdb

SHANGHAI = timezone(timedelta(hours=8))


def reference(database: Path, current_start: str, end: str) -> dict[str, Any]:
    """Return half-open current/previous cohort metrics without SQL aggregation."""
    start_day, end_day = date.fromisoformat(current_start), date.fromisoformat(end)
    if start_day >= end_day:
        raise ValueError("A positive window is required")
    with duckdb.connect(str(database), read_only=True) as connection:
        users = connection.execute(
            "SELECT user_id, registered_at, registration_os, registration_version FROM users"
        ).fetchall()
        sessions = connection.execute(
            "SELECT user_id, started_at, os, version, crashed FROM sessions"
        ).fetchall()
        releases = connection.execute(
            "SELECT os, version, released_at FROM release_calendar"
        ).fetchall()
    registration = {uid: (at.astimezone(SHANGHAI).date(), os, version)
                    for uid, at, os, version in users}
    retained: set[str] = set()
    crashed: set[str] = set()
    actual_crashes: dict[tuple[str, str], set[str]] = defaultdict(set)
    for uid, at, os, version, did_crash in sessions:
        if uid not in registration:
            continue
        registration_day = registration[uid][0]
        session_day = at.astimezone(SHANGHAI).date()
        if session_day == registration_day + timedelta(days=1):
            retained.add(uid)
        if did_crash and session_day == registration_day:
            crashed.add(uid)
            actual_crashes[(os, version)].add(uid)

    def period(left: date, right: date) -> dict[str, Any]:
        cohorts: dict[tuple[str | None, str | None], set[str]] = defaultdict(set)
        cohorts[(None, None)] = set()
        for uid, (day, os, version) in registration.items():
            if left <= day < right:
                cohorts[(None, None)].add(uid)
                cohorts[(os, None)].add(uid)
                cohorts[(os, version)].add(uid)
        rows: list[dict[str, Any]] = []
        crash_rows: list[dict[str, Any]] = []
        for (os, version), population in sorted(
                cohorts.items(), key=lambda item: (item[0][0] or "", item[0][1] or "")):
            count = len(population)
            returned = len(population & retained)
            affected = len(population & crashed)
            rows.append({"registration_os": os, "registration_version": version,
                         "new_users": count, "d1_retained": returned,
                         "d1_retention_rate": returned / count if count else None,
                         "first_day_crash_users": affected,
                         "first_day_crash_rate": affected / count if count else None})
            for (actual_os, actual_version), affected_ids in sorted(actual_crashes.items()):
                affected_count = len(population & affected_ids)
                if affected_count:
                    crash_rows.append({"registration_os": os, "registration_version": version,
                                       "actual_os": actual_os, "actual_version": actual_version,
                                       "first_day_crash_users": affected_count})
        return {"start": left.isoformat(), "end": right.isoformat(),
                "groups": rows, "actual_crashes": crash_rows}

    return {"timezone": "Asia/Shanghai", "bounds": "start-inclusive,end-exclusive",
            "previous": period(start_day - (end_day - start_day), start_day),
            "current": period(start_day, end_day),
            "releases": [{"os": os, "version": version,
                          "released_at": at.astimezone(SHANGHAI).isoformat(),
                          "release_date": at.astimezone(SHANGHAI).date().isoformat()}
                         for os, version, at in sorted(releases)],
            "limitations": ["Descriptive comparison only; no causal or independence claim.",
                            "Completeness and maturity must be verified separately from these counts."]}


def build_development_cases(output: Path) -> dict[str, Any]:
    """Private experiment coordinator; never called or read by the product."""
    from experiments.t01.snapshots import build_snapshot

    cases = []
    for name, start, version, intensity, seed in (
        ("january", "2026-01-01", "2.0", .65, 1201),
        ("march", "2026-03-03", "4.7", .35, 1202),
        ("july", "2026-07-05", "9.2", .85, 1203),
    ):
        base = datetime.combine(date.fromisoformat(start), datetime.min.time(), SHANGHAI)
        snapshot = build_snapshot(output / name, scenario="A1", seed=seed,
                                  base_start=base, new_version=version,
                                  crash_probability=intensity)
        current_start = (base + timedelta(days=7)).date().isoformat()
        end = (base + timedelta(days=14)).date().isoformat()
        expected = reference(snapshot.database, current_start, end)
        cases.append({"case": name, "database": str(snapshot.database.resolve()),
                      "current_start": current_start, "end": end,
                      "logical_hash": snapshot.logical_hash,
                      "private_parameters": {"seed": seed, "new_version": version,
                                             "crash_probability": intensity},
                      "reference": expected})
    manifest = {"purpose": "development-only independent reference; not product input",
                "cases": cases}
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = build_development_cases(args.output)
    print(json.dumps({"cases": len(manifest["cases"]),
                      "manifest": str((args.output / "manifest.json").resolve())}))
