"""Trusted reference SQL and a separately expressed set/loop oracle.

Neither is an Agent query executor. Both read only business tables, never the manifest.
"""

from datetime import date, timedelta, timezone
from pathlib import Path
from typing import Any

import duckdb

Metric = dict[str, Any]


def records(con: duckdb.DuckDBPyConnection, sql: str, parameters: Any = None) -> list[Metric]:
    result = con.execute(sql, parameters)
    columns = [column[0] for column in result.description]
    return [dict(zip(columns, row)) for row in result.fetchall()]


def sql_metrics(database: Path, start: str, end: str) -> Metric:
    """Read all counts through independently inspectable relational reference queries."""
    with duckdb.connect(str(database), read_only=True) as con:
        dates = dict(con.execute("SELECT source, CAST(complete_before AT TIME ZONE 'Asia/Shanghai' AS DATE) FROM source_watermarks").fetchall())
        requested_end = date.fromisoformat(end)
        retention_end = min(requested_end, dates["users"], dates["sessions"] - timedelta(days=1), dates["channel_daily"])
        playback_end = min(requested_end, *(dates[name] for name in ("sessions", "content_events", "playback_telemetry")))
        cohort = Path(__file__).with_name("cohort.sql").read_text()
        parameters = {"start": start, "end": retention_end.isoformat()}
        retention = records(con, f"""WITH cohort AS ({cohort})
            SELECT os,version,channel,count(*) AS users,sum(retained)::BIGINT AS retained,
            sum(crashed)::BIGINT AS crashed_users,avg(retained::INTEGER) AS retention_rate
            FROM cohort GROUP BY os,version,channel ORDER BY os,version,channel""", parameters)
        channels = records(con, f"""WITH cohort AS ({cohort}),
            counts AS (SELECT channel,count(*) AS users,sum(retained)::BIGINT AS retained FROM cohort GROUP BY channel),
            costs AS (SELECT channel,sum(spend_cents)::BIGINT AS spend_cents FROM channel_daily
                WHERE day>=CAST($start AS DATE) AND day<CAST($end AS DATE) GROUP BY channel)
            SELECT coalesce(c.channel,n.channel) AS channel,c.spend_cents,
                coalesce(n.users,0) AS users,coalesce(n.retained,0) AS retained,
                c.spend_cents/nullif(n.users,0) AS cost_per_new_cents,
                c.spend_cents/nullif(n.retained,0) AS cost_per_retained_cents
            FROM costs c FULL JOIN counts n USING(channel) ORDER BY channel""", parameters)
        playback = records(con, Path(__file__).with_name("playback.sql").read_text(),
                           {"start": start, "end": playback_end.isoformat()})
    return {"retention": retention, "channels": channels, "playback": playback,
            "coverage": {"requested_start": start, "requested_end": end,
                         "retention_end": retention_end.isoformat(), "playback_end": playback_end.isoformat(),
                         "retention_complete": retention_end == requested_end,
                         "playback_complete": playback_end == requested_end}}


def python_metrics(database: Path, start: str, end: str) -> Metric:
    """Independent membership/count oracle; no aggregation SQL or generator probabilities."""
    local = timezone(timedelta(hours=8))
    begin, stop = date.fromisoformat(start), date.fromisoformat(end)
    with duckdb.connect(str(database), read_only=True) as con:
        tables = {name: records(con, f"SELECT * FROM {name}") for name in (
            "users", "sessions", "channel_daily", "content_events", "playback_telemetry", "source_watermarks")}
    cutoffs = {row["source"]: row["complete_before"].astimezone(local).date() for row in tables["source_watermarks"]}
    rend = min(stop, cutoffs["users"], cutoffs["sessions"]-timedelta(days=1), cutoffs["channel_daily"])
    pend = min(stop, cutoffs["sessions"], cutoffs["content_events"], cutoffs["playback_telemetry"])
    active = {(s["user_id"], s["started_at"].astimezone(local).date()) for s in tables["sessions"]}
    crashes = {(s["user_id"], s["started_at"].astimezone(local).date()) for s in tables["sessions"] if s["crashed"]}
    grouped: dict[tuple[str, str, str], list[int]] = {}
    channel_counts: dict[str, list[int]] = {}
    for user in tables["users"]:
        registered = user["registered_at"].astimezone(local).date()
        if not begin <= registered < rend:
            continue
        retained = int((user["user_id"], registered+timedelta(days=1)) in active)
        cohort_key = (user["registration_os"], user["registration_version"], user["channel"])
        counts = grouped.setdefault(cohort_key, [0, 0, 0])
        counts[0] += 1
        counts[1] += retained
        counts[2] += int((user["user_id"], registered) in crashes)
        counts = channel_counts.setdefault(user["channel"], [0, 0])
        counts[0] += 1
        counts[1] += retained
    retention = [{"os": key[0], "version": key[1], "channel": key[2], "users": n,
                  "retained": r, "crashed_users": c, "retention_rate": r/n}
                 for key, (n, r, c) in sorted(grouped.items())]
    costs: dict[str, int] = {}
    for row in tables["channel_daily"]:
        if begin <= row["day"] < rend:
            costs[row["channel"]] = costs.get(row["channel"], 0) + row["spend_cents"]
    channels = []
    for channel in sorted(costs.keys() | channel_counts.keys()):
        n, r = channel_counts.get(channel, [0, 0])
        spend = costs.get(channel)
        channels.append({"channel": channel, "spend_cents": spend, "users": n, "retained": r,
                         "cost_per_new_cents": spend/n if n and spend is not None else None,
                         "cost_per_retained_cents": spend/r if r and spend is not None else None})
    starts: dict[tuple[str, str], Any] = {}
    completed = set()
    for row in tables["content_events"]:
        key = (row["play_id"], row["session_id"])
        if row["event_type"] == "start":
            starts[key] = min(starts.get(key, row["occurred_at"]), row["occurred_at"])
        elif row["event_type"] == "complete":
            completed.add(key)
    telemetry: dict[tuple[str, str], tuple[int, int]] = {}
    for row in tables["playback_telemetry"]:
        key = (row["play_id"], row["session_id"])
        old = telemetry.get(key, (0, 0))
        telemetry[key] = (max(old[0], row["watched_seconds"]), max(old[1], row["duration_seconds"]))
    sessions = {row["session_id"]: row for row in tables["sessions"]}
    play_counts: dict[tuple[str, str], list[int]] = {}
    for key, at in starts.items():
        if not begin <= at.astimezone(local).date() < pend or key[1] not in sessions:
            continue
        session = sessions[key[1]]
        values = play_counts.setdefault((session["os"], session["version"]), [0]*7)
        watched, duration = telemetry.get(key, (0, 0))
        observed = key in telemetry
        full = observed and watched >= duration
        increments = [1, int(key in completed), int(full), int(full and key not in completed),
                      int(not observed), int(observed and watched >= min(5, duration)), watched]
        for index, value in enumerate(increments):
            values[index] += value
    names = ("starts", "completions", "telemetry_complete", "missing_complete", "unmatched", "effective", "watched_seconds")
    playback = [{"os": key[0], "version": key[1], **dict(zip(names, values))} for key, values in sorted(play_counts.items())]
    return {"retention": retention, "channels": channels, "playback": playback,
            "coverage": {"requested_start": start, "requested_end": end,
                         "retention_end": rend.isoformat(), "playback_end": pend.isoformat(),
                         "retention_complete": rend == stop, "playback_complete": pend == stop}}
