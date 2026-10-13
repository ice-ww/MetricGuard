"""Private development oracle using raw rows and Python sets, never product SQL."""

import argparse
import json
import math
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import duckdb

SHANGHAI = timezone(timedelta(hours=8))


def reference(database: Path, current_start: str, end: str) -> dict[str, Any]:
    start, finish = date.fromisoformat(current_start), date.fromisoformat(end)
    if start >= finish:
        raise ValueError("A positive window is required")
    previous_start = start - (finish - start)
    with duckdb.connect(str(database), read_only=True) as connection:
        raw_users = connection.execute("SELECT user_id, registered_at, channel FROM users").fetchall()
        raw_sessions = connection.execute("SELECT user_id, started_at FROM sessions").fetchall()
        raw_spend = connection.execute("SELECT day, channel, spend_cents FROM channel_daily").fetchall()
    registrations = {uid: (at.astimezone(SHANGHAI).date(), channel)
                     for uid, at, channel in raw_users}
    retained = {uid for uid, at in raw_sessions if uid in registrations
                and at.astimezone(SHANGHAI).date() == registrations[uid][0] + timedelta(days=1)}
    populations: dict[tuple[str, str], set[str]] = defaultdict(set)
    spending: dict[tuple[str, str], int] = defaultdict(int)
    channels: set[str] = set()
    windows = {"previous": (previous_start, start), "current": (start, finish)}
    for period, (left, right) in windows.items():
        for uid, (day, channel) in registrations.items():
            if left <= day < right:
                channels.add(channel)
                populations[(period, channel)].add(uid)
        for day, channel, cents in raw_spend:
            if left <= day < right:
                channels.add(channel)
                spending[(period, channel)] += cents
    totals = {period: sum(len(populations[(period, channel)]) for channel in channels)
              for period in windows}
    total_delta = totals["current"] - totals["previous"]
    rows: list[dict[str, Any]] = []
    for period, (left, right) in windows.items():
        for channel in sorted(channels):
            population = populations[(period, channel)]
            count, returned = len(population), len(population & retained)
            spend = spending.get((period, channel))
            delta = len(populations[("current", channel)]) - len(populations[("previous", channel)])
            rows.append({"period": period, "channel": channel, "users": count,
                         "retained": returned, "retention_rate": returned / count if count else None,
                         "spend_cents": spend,
                         "cost_per_new_cents": spend / count if spend is not None and count else None,
                         "cost_per_retained_cents": spend / returned if spend is not None and returned else None,
                         "user_share": count / totals[period] if totals[period] else None,
                         "new_users_delta": delta, "total_new_users_delta": total_delta,
                         "growth_contribution": delta / total_delta if total_delta else None,
                         "window_start": left.isoformat(), "window_end": right.isoformat()})
    # Check against raw populations/spending, not just arithmetic on result rows.
    for period, (left, right) in windows.items():
        period_rows = [row for row in rows if row["period"] == period]
        raw_ids = {uid for uid, (day, _) in registrations.items() if left <= day < right}
        assert sum(row["users"] for row in period_rows) == len(raw_ids)
        assert sum(row["retained"] for row in period_rows) == len(raw_ids & retained)
        assert sum(row["spend_cents"] for row in period_rows if row["spend_cents"] is not None) == sum(
            cents for day, _, cents in raw_spend if left <= day < right)
        if raw_ids:
            assert math.isclose(sum(row["user_share"] for row in period_rows), 1)
        assert sum(row["new_users_delta"] for row in period_rows) == total_delta
        if total_delta:
            assert math.isclose(sum(row["growth_contribution"] for row in period_rows), 1)
        for row in period_rows:
            assert 0 <= row["retained"] <= row["users"]
            if row["spend_cents"] is None:
                assert row["cost_per_new_cents"] is None and row["cost_per_retained_cents"] is None
            if not row["users"]:
                assert row["cost_per_new_cents"] is None and row["retention_rate"] is None
            if not row["retained"]:
                assert row["cost_per_retained_cents"] is None
    return {"timezone": "Asia/Shanghai", "bounds": "start-inclusive,end-exclusive",
            "rows": rows, "conservation_checks": "passed",
            "limitations": ["Descriptive only; no fraud, causation or independence conclusion.",
                            "Source completeness and cohort maturity require separate checks."]}


def build_development_cases(output: Path) -> dict[str, Any]:
    from experiments.t01.snapshots import build_snapshot

    cases = []
    for name, first, channel, growth, retention, cost, seed in (
        ("january", "2026-01-01", "paid", 3.0, .12, 200, 1301),
        ("april", "2026-04-03", "partner", 2.0, .2, 100, 1302),
        ("september", "2026-09-05", "search", 4.0, .08, 50, 1303),
    ):
        base = datetime.combine(date.fromisoformat(first), datetime.min.time(), SHANGHAI)
        snapshot = build_snapshot(output / name, scenario="A2", seed=seed, base_start=base,
                                  campaign_channel=channel, campaign_growth=growth,
                                  campaign_retention=retention, campaign_unit_cost=cost)
        start, end = ((base + timedelta(days=days)).date().isoformat() for days in (7, 14))
        expected = reference(snapshot.database, start, end)
        campaign_rows = {row["period"]: row for row in expected["rows"] if row["channel"] == channel}
        assert campaign_rows["previous"]["cost_per_new_cents"] == 100
        assert campaign_rows["current"]["cost_per_new_cents"] == cost
        assert campaign_rows["current"]["retention_rate"] < campaign_rows["previous"]["retention_rate"]
        idle_rows = [row for row in expected["rows"] if row["channel"] == "idle"]
        assert len(idle_rows) == 2
        assert all(row["spend_cents"] == 700 and row["users"] == 0 for row in idle_rows)
        cases.append({"case": name, "database": str(snapshot.database.resolve()),
                      "current_start": start, "end": end, "logical_hash": snapshot.logical_hash,
                      "private_parameters": {"seed": seed, "channel": channel, "growth": growth,
                                             "retention": retention, "unit_cost_cents": cost},
                      "reference": expected})
    manifest = {"purpose": "development-only independent reference; not product input", "cases": cases}
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = build_development_cases(args.output)
    print(json.dumps({"cases": len(manifest["cases"]), "conservation_checks": "passed",
                      "manifest": str((args.output / "manifest.json").resolve())}))
