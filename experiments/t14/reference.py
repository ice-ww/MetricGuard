"""Private development oracle: raw table reads and Python play-id reconciliation."""

import argparse
import json
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import duckdb

SHANGHAI = timezone(timedelta(hours=8))


def earliest_start(observations: list[Any]) -> tuple[Any, datetime] | None:
    known = [(sid, at) for sid, at in observations if at is not None]
    return min(known, key=lambda item: (item[1], str(item[0]))) if known else None


def reference(database: Path, current_start: str, end: str) -> dict[str, Any]:
    start, finish = date.fromisoformat(current_start), date.fromisoformat(end)
    if finish <= start:
        raise ValueError("Positive window required")
    windows = {"previous": (start - (finish - start), start), "current": (start, finish)}
    with duckdb.connect(str(database), read_only=True) as con:
        events = con.execute("SELECT play_id, session_id, event_type, occurred_at FROM content_events").fetchall()
        telemetry = con.execute("SELECT play_id, session_id, observed_at, watched_seconds, duration_seconds FROM playback_telemetry").fetchall()
        sessions = {sid: (os, version) for sid, os, version in con.execute("SELECT session_id, os, version FROM sessions").fetchall()}
        watermarks = dict(con.execute("SELECT source, complete_before FROM source_watermarks").fetchall())
    starts: dict[str, list[Any]] = defaultdict(list)
    completions: dict[str, list[Any]] = defaultdict(list)
    progress: dict[str, list[Any]] = defaultdict(list)
    for pid, sid, kind, at in events:
        if kind == "start":
            starts[pid].append((sid, at))
        elif kind == "complete":
            completions[pid].append((sid, at))
    for pid, sid, at, watched, duration in telemetry:
        progress[pid].append((sid, at, watched, duration))
    groups: dict[tuple[str, str, str], dict[str, Any]] = {}
    for pid, observations in starts.items():
        identities = set(observations)
        first = earliest_start(observations)
        if first is None:
            continue
        sid, at = first
        day = at.astimezone(SHANGHAI).date()
        for period, (left, right) in windows.items():
            if not left <= day < right:
                continue
            os, version = sessions.get(sid, ("unknown", "unknown"))
            key = (period, str(os), str(version))
            cutoff = datetime.combine(right, datetime.min.time(), SHANGHAI)
            complete_sources = all(watermarks.get(source) is not None and watermarks[source] >= cutoff
                                   for source in ("content_events", "playback_telemetry"))
            row = groups.setdefault(key, {"period": period, "os": os, "version": version,
                "window_start": left.isoformat(), "window_end": right.isoformat(),
                "starts": 0, "observed_completed": 0, "independent_complete": 0,
                "effective": 0, "missing_completion": 0 if complete_sources else None,
                "unmatched": 0, "quality_flags": set(), "sources_complete": complete_sources})
            row["starts"] += 1
            flags: set[str] = set()
            if not complete_sources:
                flags.add("incomplete_watermark")
            if len(identities) != 1 or sid not in sessions or os is None or version is None or pid is None:
                flags.add("ambiguous_start_or_session")
            ends = completions.get(pid, [])
            if any(end_sid != sid or end_at is None or end_at < at for end_sid, end_at in ends):
                flags.add("unaligned_completion")
            observed = bool(ends) and not flags.intersection({"ambiguous_start_or_session", "unaligned_completion"})
            readings = progress.get(pid, [])
            if not readings:
                flags.add("missing_independent_telemetry")
            if any(t_sid != sid or t_at is None or t_at < at or watched is None or duration is None
                   or duration <= 0 or watched < 0 or watched > duration
                   for t_sid, t_at, watched, duration in readings):
                flags.add("invalid_or_unaligned_telemetry")
            if len({reading[3] for reading in readings}) > 1:
                flags.add("conflicting_duration")
            usable = bool(readings) and not flags.intersection({"ambiguous_start_or_session", "invalid_or_unaligned_telemetry", "conflicting_duration"})
            independent = usable and max(reading[2] for reading in readings) >= readings[0][3]
            effective = usable and max(reading[2] for reading in readings) >= min(5, readings[0][3])
            row["observed_completed"] += int(observed)
            row["independent_complete"] += int(independent)
            row["effective"] += int(effective)
            if complete_sources and independent and not observed and not flags.intersection({"ambiguous_start_or_session", "unaligned_completion"}):
                row["missing_completion"] += 1
            row["unmatched"] += int(not usable or "unaligned_completion" in flags or "ambiguous_start_or_session" in flags)
            row["quality_flags"].update(flags)
    rows = []
    for key in sorted(groups):
        row = groups[key]
        row["quality_flags"] = sorted(row["quality_flags"])
        for field in ("observed_completed", "independent_complete", "effective", "unmatched"):
            assert 0 <= row[field] <= row["starts"]
        if row["missing_completion"] is not None:
            assert 0 <= row["missing_completion"] <= row["independent_complete"]
        rows.append(row)
    expected_starts = sum(1 for values in starts.values()
                          if (first := earliest_start(values)) is not None
                          and windows["previous"][0] <= first[1].astimezone(SHANGHAI).date() < finish)
    assert sum(row["starts"] for row in rows) == expected_starts
    return {"method": "raw SELECT only; Python play-id sets, actual session OS/version, start natural day",
        "rows": rows, "conservation": {"window_unique_starts": expected_starts,
            "all_unique_starts": len(starts), "raw_start_reports": sum(map(len, starts.values())),
            "orphan_completion_plays": len(set(completions) - set(starts)),
            "orphan_telemetry_plays": len(set(progress) - set(starts))},
        "limitations": ["Development oracle; no causal claim or independent-user binomial test.",
                        "Missing completion is only counted with both source watermarks complete."]}


def verify_conflicting_starts(root: Path) -> dict[str, Any]:
    """Actual raw fixture with deliberately unsorted reports crossing window edges."""
    root.mkdir(parents=True, exist_ok=False)
    database = root / "snapshot.duckdb"
    def at(value: str | None) -> datetime | None:
        return datetime.fromisoformat(value).replace(tzinfo=SHANGHAI) if value else None
    observations: dict[str, list[str | None]] = {"earliest_outside": ["2026-01-09", "2025-12-31"],
                    "earliest_inside": ["2026-01-16", "2026-01-10"],
                    "cross_period": ["2026-01-08", "2026-01-07"],
                    "nullable": [None, "2026-01-11"], "only_null": [None]}
    with duckdb.connect(str(database)) as con:
        con.execute(Path("experiments/t01/schema.sql").read_text(encoding="utf-8"))
        con.execute("INSERT INTO sessions VALUES ('s','u',?,'Android','1.0',false)", [at("2026-01-01")])
        for pid, dates in observations.items():
            for index, value in enumerate(dates):
                con.execute("INSERT INTO content_events VALUES (?,?,'s','start',?)", [f"{pid}-{index}", pid, at(value)])
            con.execute("INSERT INTO content_events VALUES (?,?,'s','complete',?)", [f"{pid}-end", pid, at("2026-01-17")])
            con.execute("INSERT INTO playback_telemetry VALUES (?,?,'s',?,30,30)", [f"{pid}-t", pid, at("2026-01-17")])
        for source in ("content_events", "playback_telemetry"):
            con.execute("INSERT INTO source_watermarks VALUES (?,?)", [source, at("2026-01-20")])
    result = reference(database, "2026-01-08", "2026-01-15")
    assert result["conservation"]["window_unique_starts"] == 3
    assert {row["period"]: row["starts"] for row in result["rows"]} == {"previous": 1, "current": 2}
    assert all(row["observed_completed"] == row["independent_complete"] == row["effective"] == 0
               and row["unmatched"] == row["starts"]
               and "ambiguous_start_or_session" in row["quality_flags"] for row in result["rows"])
    result["fixture_observations"] = observations
    result["checks"] = {"earliest_non_null_window_conservation": True, "ambiguous_counts_excluded": True}
    (root / "result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def build_development(root: Path) -> list[dict[str, Any]]:
    from experiments.t01.snapshots import build_snapshot

    cases = [("january", "A3", 1401, 1, "2.0", 1.0),
             ("may", "A3", 1402, 5, "5.3", .5),
             ("august", "A3", 1403, 8, "8.8", .8),
             ("normal", "normal", 1404, 1, "2.0", 1.0),
             ("no_telemetry", "normal", 1404, 1, "2.0", 1.0),
             ("unaligned", "normal", 1404, 1, "2.0", 1.0),
             ("incomplete_watermark", "normal", 1404, 1, "2.0", 1.0)]
    results = []
    for name, scenario, seed, month, version, strength in cases:
        base = datetime(2026, month, 1, tzinfo=SHANGHAI)
        snapshot = build_snapshot(root / name, scenario=scenario, seed=seed, base_start=base,
                                  new_version=version, completion_drop_probability=strength)
        with duckdb.connect(str(snapshot.database)) as con:
            if name == "no_telemetry":
                con.execute("DELETE FROM playback_telemetry")
            elif name == "unaligned":
                con.execute("UPDATE playback_telemetry SET session_id='nonexistent-session'")
            elif name == "incomplete_watermark":
                con.execute("UPDATE source_watermarks SET complete_before=? WHERE source='playback_telemetry'", [base + timedelta(days=7)])
        current = (base + timedelta(days=7)).date().isoformat()
        end = (base + timedelta(days=14)).date().isoformat()
        result = reference(snapshot.database, current, end)
        result.update({"case": name, "database": str(snapshot.database.resolve()),
                       "current_start": current, "end": end, "development_seed": seed,
                       "mutation": name if name in {"no_telemetry", "unaligned", "incomplete_watermark"} else None})
        (root / name / "reference.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        results.append(result)
    (root / "references.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", type=Path)
    parser.add_argument("--database", type=Path)
    parser.add_argument("--start")
    parser.add_argument("--end")
    args = parser.parse_args()
    if args.build:
        output: Any = build_development(args.build)
    else:
        output = reference(args.database, args.start, args.end)
    print(json.dumps(output, indent=2))
