"""Development-only experiments. All expectations and scenario routing stay private."""

import hashlib
import importlib.metadata
import json
import math
import platform
import tempfile
from pathlib import Path
from typing import Any

import duckdb

from .references import Metric, python_metrics, sql_metrics
from .snapshots import MECHANISMS, TABLES, build_snapshot
from .standardization import python_standardization, sql_standardization


def database_hash(database: Path) -> str:
    """Hash persisted logical rows, independent of DuckDB's physical file layout."""
    with duckdb.connect(str(database), read_only=True) as con:
        rows = {name: con.execute(f"SELECT * FROM {name} ORDER BY ALL").fetchall() for name in TABLES}
    return hashlib.sha256(json.dumps(rows, default=str, sort_keys=True).encode()).hexdigest()


def integrity_checks(database: Path) -> dict[str, bool]:
    violations = {
        "sessions_have_users": "SELECT count(*) FROM sessions s LEFT JOIN users u USING(user_id) WHERE u.user_id IS NULL",
        "events_have_sessions": "SELECT count(*) FROM content_events e LEFT JOIN sessions s USING(session_id) WHERE s.session_id IS NULL",
        "telemetry_has_sessions": "SELECT count(*) FROM playback_telemetry t LEFT JOIN sessions s USING(session_id) WHERE s.session_id IS NULL",
        "play_id_has_one_session": """SELECT count(*) FROM (SELECT play_id FROM
            (SELECT play_id,session_id FROM content_events UNION ALL SELECT play_id,session_id FROM playback_telemetry)
            GROUP BY play_id HAVING count(DISTINCT session_id)<>1)""",
        "every_event_has_start": """SELECT count(*) FROM content_events e WHERE NOT EXISTS
            (SELECT 1 FROM content_events s WHERE s.play_id=e.play_id AND s.event_type='start')""",
        "telemetry_has_start": """SELECT count(*) FROM playback_telemetry t WHERE NOT EXISTS
            (SELECT 1 FROM content_events s WHERE s.play_id=t.play_id AND s.event_type='start')""",
        "telemetry_valid_duration": """SELECT count(*) FROM playback_telemetry
            WHERE duration_seconds<=0 OR watched_seconds<0 OR watched_seconds>duration_seconds""",
        "duration_consistent_per_play": """SELECT count(*) FROM (SELECT play_id FROM playback_telemetry
            GROUP BY play_id HAVING count(DISTINCT duration_seconds)<>1)""",
        "no_observation_window_upgrades": """SELECT count(*) FROM sessions s JOIN users u USING(user_id)
            WHERE s.os<>u.registration_os OR s.version<>u.registration_version""",
        "acquisition_days_have_spend": """SELECT count(*) FROM users u WHERE NOT EXISTS
            (SELECT 1 FROM channel_daily c WHERE c.channel=u.channel AND c.day=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE))""",
        "nonnegative_spend": "SELECT count(*) FROM channel_daily WHERE spend_cents<0",
    }
    with duckdb.connect(str(database), read_only=True) as con:
        checks = {name: con.execute(query).fetchall()[0][0] == 0 for name, query in violations.items()}
        checks["business_tables_only"] = {r[0] for r in con.execute("SHOW TABLES").fetchall()} == set(TABLES)
        checks["all_source_cutoffs_present"] = {r[0] for r in con.execute("SELECT source FROM source_watermarks").fetchall()} == set(TABLES)-{"source_watermarks"}
    return checks


def retention_rate(metrics: Metric, os: str | None = None) -> float:
    rows = [r for r in metrics["retention"] if os is None or r["os"] == os]
    return sum(r["retained"] for r in rows)/sum(r["users"] for r in rows)


def mechanism_checks(scenario: str, before: Metric, current: Metric, normal: Metric) -> dict[str, bool]:
    if scenario == "insufficient":
        return {"incomplete_is_explicit": not current["coverage"]["retention_complete"] and not current["coverage"]["playback_complete"],
                "unavailable_playback_is_not_zero": current["playback"] == []}
    checks = {"complete_comparison_windows": all(before["coverage"][k] and current["coverage"][k]
                                                  for k in ("retention_complete", "playback_complete"))}
    if scenario == "normal":
        checks["normal_retention_variation_below_5pp"] = abs(retention_rate(current)-retention_rate(before)) < .05
    elif scenario == "A1":
        affected = [r for r in current["retention"] if r["os"] == "Android" and r["version"] == "2.0"]
        checks["crash_association_observed"] = bool(affected) and all(r["retention_rate"] < .3 and r["crashed_users"]/r["users"] > .5 for r in affected)
        control = lambda m: [r for r in m["retention"] if r["os"] != "Android" or r["version"] != "2.0"]
        checks["unaffected_cohorts_match_normal"] = control(current) == control(normal)
    elif scenario == "A2":
        paid = next(r for r in current["channels"] if r["channel"] == "paid")
        old = next(r for r in before["channels"] if r["channel"] == "paid")
        checks["volume_quality_cost_observed"] = paid["users"] > 2*old["users"] and paid["retained"]/paid["users"] < .2 and paid["cost_per_retained_cents"] > 2*old["cost_per_retained_cents"]
        control = lambda m: [r for r in m["retention"] if r["channel"] == "organic"]
        checks["organic_control_matches_normal"] = control(current) == control(normal)
    elif scenario == "A3":
        affected_play = next(r for r in current["playback"] if r["os"] == "Android" and r["version"] == "2.0")
        checks["collector_loss_observed"] = affected_play["completions"] == 0 and affected_play["missing_complete"] > 100
        checks["independent_progress_unchanged"] = all(
            {k: v for k, v in actual.items() if k not in ("completions", "missing_complete")} ==
            {k: v for k, v in expected.items() if k not in ("completions", "missing_complete")}
            for actual, expected in zip(current["playback"], normal["playback"], strict=True))
        checks["retention_control_matches_normal"] = current["retention"] == normal["retention"]
    elif scenario == "A4":
        checks["android_decline_above_15pp"] = retention_rate(current, "Android") < retention_rate(before, "Android")-.15
        checks["overall_change_below_5pp"] = abs(retention_rate(current)-retention_rate(before)) < .05
        checks["ios_control_stable_within_5pp"] = abs(retention_rate(current, "iOS")-retention_rate(before, "iOS")) < .05
    return checks


def run_experiment(output: Path, *, seeds: list[int]) -> dict[str, Any]:
    if output.exists():
        raise FileExistsError(f"Use a fresh output directory: {output}")
    if not seeds or len(set(seeds)) != len(seeds):
        raise ValueError("Provide at least one unique seed; duplicate seeds are not additional trials")
    output.mkdir(parents=True)
    (output / "private").mkdir()
    report: dict[str, Any] = {
        "purpose": "development_only", "human_review": "pending", "automatic_pass": False,
        "environment": {"python": platform.python_version(), "platform": platform.platform(),
                        **{name: importlib.metadata.version(name) for name in ("duckdb", "pytz", "pytest", "mypy")}},
        "configuration": {"seeds": seeds, "timezone": "Asia/Shanghai", "windows": [["2026-01-01", "2026-01-08"], ["2026-01-08", "2026-01-15"]]},
        "source_hashes": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(Path(__file__).parent.glob("*")) if p.suffix in (".py", ".sql")},
        "cases": [],
    }
    for seed in seeds:
        normal: Metric = {}
        baseline: Metric = {}
        for scenario in MECHANISMS:
            case_id = f"case-{len(report['cases'])+1:03d}"
            snapshot = build_snapshot(output / case_id, scenario=scenario, seed=seed)
            checks = integrity_checks(snapshot.database)
            digest = database_hash(snapshot.database)
            with tempfile.TemporaryDirectory() as staging:
                duplicate = build_snapshot(Path(staging) / "repeat", scenario=scenario, seed=seed)
                checks["reproducible_database"] = database_hash(duplicate.database) == digest
            before, current = [sql_metrics(snapshot.database, *window) for window in report["configuration"]["windows"]]
            for name, window, result in zip(("baseline", "current"), report["configuration"]["windows"], (before, current), strict=True):
                checks[f"independent_{name}_agreement"] = result == python_metrics(snapshot.database, *window)
            if scenario == "normal":
                normal, baseline = current, before
            elif scenario != "insufficient":
                checks["baseline_unaffected"] = before == baseline
            checks.update(mechanism_checks(scenario, before, current, normal))
            case = {"case": case_id, "scenario": scenario, "seed": seed, "database_hash": digest,
                    "checks": checks, "baseline": before, "current": current}
            if scenario == "A4":
                derived = sql_standardization(snapshot.database)
                oracle = python_standardization(snapshot.database)
                checks["standardization_independent_agreement"] = derived["systems"] == oracle["systems"] and all(
                    math.isclose(derived[key], oracle[key], rel_tol=0, abs_tol=1e-12)
                    for key in ("standardized_retention", "actual_retention"))
                checks["composition_masks_decline"] = derived["actual_retention"] - derived["standardized_retention"] > .05
                case["standardization"] = derived
            report["cases"].append(case)
            (snapshot.private_manifest.parent / "reference-results.json").write_text(json.dumps(case, indent=2), encoding="utf-8")
    report["automatic_pass"] = all(all(case["checks"].values()) for case in report["cases"])
    (output / "private" / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report
