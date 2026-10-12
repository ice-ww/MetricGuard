from pathlib import Path

import duckdb
import pytest

from experiments.t01 import build_snapshot


def test_normal_snapshot_is_reproducible_and_answers_are_separate(tmp_path: Path) -> None:
    first = build_snapshot(tmp_path / "one", scenario="normal", seed=7)
    second = build_snapshot(tmp_path / "two", scenario="normal", seed=7)
    assert first.logical_hash == second.logical_hash
    from experiments.t01.validation import database_hash, integrity_checks
    assert database_hash(first.database) == database_hash(second.database)
    assert all(integrity_checks(first.database).values())
    assert first.database.parent.name == "public"
    assert first.private_manifest.parent.name == "private"
    assert set(first.tables) == {
        "users", "sessions", "content_events", "playback_telemetry",
        "channel_daily", "release_calendar", "source_watermarks",
    }


def test_reference_queries_match_hand_worked_boundaries(tmp_path: Path) -> None:
    from experiments.t01.references import sql_metrics, python_metrics

    database = tmp_path / "hand.duckdb"
    with duckdb.connect(str(database)) as con:
        con.execute(Path("experiments/t01/schema.sql").read_text())
        con.execute("""
            INSERT INTO users VALUES
            ('u1','2026-01-01 23:55:00+08','Android','1.0','paid'),
            ('u2','2026-01-02 08:00:00+08','Android','1.0','paid'),
            ('u3','2026-01-02 08:00:00+08','Android','1.0','paid'),
            ('u4','2026-01-02 08:00:00+08','Android','1.0','paid'),
            ('immature','2026-01-03 08:00:00+08','Android','1.0','paid');
            INSERT INTO sessions VALUES
            ('s1','u1','2026-01-01 23:56:00+08','Android','1.0',true),
            ('s2','u1','2026-01-02 00:05:00+08','Android','2.0',false),
            ('s3','u1','2026-01-02 01:00:00+08','Android','2.0',false);
            INSERT INTO channel_daily VALUES
            ('2026-01-01','paid',100),('2026-01-02','paid',300),
            ('2026-01-03','paid',999),('2026-01-01','idle',100);
            INSERT INTO content_events VALUES
            ('e1','p1','s1','start','2026-01-01 23:57:00+08'),
            ('e2','p1','s1','start','2026-01-01 23:57:00+08'),
            ('e3','p1','s1','complete','2026-01-01 23:58:00+08'),
            ('e4','p1','s1','complete','2026-01-01 23:58:00+08'),
            ('e5','p2','s1','start','2026-01-01 23:58:00+08');
            INSERT INTO playback_telemetry VALUES
            ('r1','p1','s1','2026-01-01 23:58:00+08',30,30),
            ('r2','p1','s1','2026-01-01 23:58:30+08',30,30),
            ('r3','p2','s1','2026-01-01 23:59:00+08',30,30);
        """)
        con.executemany("INSERT INTO source_watermarks VALUES (?, ?)", [
            (name, "2026-01-04 00:00:00+08") for name in
            ("users", "sessions", "channel_daily", "content_events", "playback_telemetry")
        ])
    sql = sql_metrics(database, "2026-01-01", "2026-01-04")
    assert sql == python_metrics(database, "2026-01-01", "2026-01-04")
    assert sql["retention"] == [{"os": "Android", "version": "1.0", "channel": "paid",
        "users": 4, "retained": 1, "crashed_users": 1, "retention_rate": .25}]
    paid = next(row for row in sql["channels"] if row["channel"] == "paid")
    assert paid == {"channel": "paid", "spend_cents": 400, "users": 4, "retained": 1,
                    "cost_per_new_cents": 100.0, "cost_per_retained_cents": 400.0}
    assert sql["channels"][0]["cost_per_new_cents"] is None
    assert sql["playback"][0] == {"os": "Android", "version": "1.0", "starts": 2,
        "completions": 1, "telemetry_complete": 2, "missing_complete": 1,
        "unmatched": 0, "effective": 2, "watched_seconds": 60}
    assert sql["coverage"]["retention_complete"] is False


@pytest.mark.parametrize("scenario", ["A1", "A2", "A3", "A4", "insufficient"])
def test_development_mechanisms_and_independent_answers(tmp_path: Path, scenario: str) -> None:
    from experiments.t01.references import sql_metrics, python_metrics

    snap = build_snapshot(tmp_path / scenario, scenario=scenario, seed=7)
    current = sql_metrics(snap.database, "2026-01-08", "2026-01-15")
    assert current == python_metrics(snap.database, "2026-01-08", "2026-01-15")
    before = sql_metrics(snap.database, "2026-01-01", "2026-01-08")
    if scenario == "A1":
        affected = [r for r in current["retention"] if r["os"] == "Android" and r["version"] == "2.0"]
        assert all(r["retention_rate"] < .3 and r["crashed_users"]/r["users"] > .5 for r in affected)
    elif scenario == "A2":
        paid = next(r for r in current["channels"] if r["channel"] == "paid")
        base = next(r for r in before["channels"] if r["channel"] == "paid")
        assert paid["users"] > 2 * base["users"]
        assert paid["retained"]/paid["users"] < .2
        assert paid["cost_per_retained_cents"] > 2 * base["cost_per_retained_cents"]
    elif scenario == "A3":
        affected = next(r for r in current["playback"] if r["os"] == "Android" and r["version"] == "2.0")
        assert affected["completions"] == 0 and affected["missing_complete"] > 100
        assert affected["telemetry_complete"] == affected["missing_complete"]
    elif scenario == "A4":
        def rate(rows: list[dict], os: str | None = None) -> float:
            selected = [r for r in rows if os is None or r["os"] == os]
            return sum(r["retained"] for r in selected) / sum(r["users"] for r in selected)
        assert rate(current["retention"], "Android") < rate(before["retention"], "Android") - .15
        assert abs(rate(current["retention"]) - rate(before["retention"])) < .05
    else:
        assert not current["coverage"]["retention_complete"]
        assert not current["coverage"]["playback_complete"]
        assert current["playback"] == []


def test_corrupt_play_identity_is_rejected(tmp_path: Path) -> None:
    from experiments.t01.validation import integrity_checks
    snapshot = build_snapshot(tmp_path / "case", scenario="normal", seed=7)
    with duckdb.connect(str(snapshot.database)) as con:
        con.execute("UPDATE content_events SET play_id='collision' WHERE event_type='start'")
    assert not integrity_checks(snapshot.database)["play_id_has_one_session"]


def test_experiment_persists_pending_human_review(tmp_path: Path) -> None:
    from experiments.t01.validation import run_experiment
    report = run_experiment(tmp_path / "run", seeds=[7])
    assert report["automatic_pass"]
    assert report["human_review"] == "pending"
    assert len(report["cases"]) == 6
    assert all(case["checks"]["reproducible_database"] for case in report["cases"])
    assert (tmp_path / "run" / "private" / "report.json").exists()


def test_standardization_uses_baseline_shares(tmp_path: Path) -> None:
    from experiments.t01.standardization import sql_standardization, python_standardization
    database = tmp_path / "mix.duckdb"
    with duckdb.connect(str(database)) as con:
        con.execute(Path("experiments/t01/schema.sql").read_text())
        for uid, day, os in [("b1", 1, "Android"), ("b2", 1, "Android"),
                             ("b3", 1, "iOS"), ("b4", 1, "iOS"), ("c1", 8, "Android"),
                             ("c2", 8, "iOS"), ("c3", 8, "iOS"), ("c4", 8, "iOS")]:
            con.execute("INSERT INTO users VALUES (?, ?, ?, '1.0', 'paid')",
                        [uid, f"2026-01-{day:02d} 08:00:00+08", os])
        for uid in ("c2", "c3", "c4"):
            con.execute("INSERT INTO sessions VALUES (?, ?, '2026-01-09 08:00:00+08', 'iOS', '1.0', false)", [uid, uid])
        for source in ("users", "sessions", "channel_daily", "content_events", "playback_telemetry"):
            con.execute("INSERT INTO source_watermarks VALUES (?, '2026-01-16 00:00:00+08')", [source])
    result = sql_standardization(database)
    assert result == python_standardization(database)
    assert result["standardized_retention"] == .5
    assert result["actual_retention"] == .75
    assert result["systems"][0]["baseline_share"] == .5
    assert result["systems"][0]["current_share"] == .25
