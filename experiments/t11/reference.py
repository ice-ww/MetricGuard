"""Raw-record oracle, independent of the Agent's aggregation queries."""
from collections import Counter
from datetime import date, timedelta, timezone
from pathlib import Path

import duckdb


def counts(database: Path, start: str, end: str) -> dict:
    local = timezone(timedelta(hours=8))
    with duckdb.connect(str(database), read_only=True) as con:
        users = con.execute('SELECT user_id,registered_at,registration_os,channel FROM users').fetchall()
        sessions = con.execute('SELECT user_id,started_at FROM sessions').fetchall()
    active = {(uid, stamp.astimezone(local).date()) for uid, stamp in sessions}
    members = {uid: (stamp.astimezone(local).date(), system, channel) for uid, stamp, system, channel in users
               if date.fromisoformat(start) <= stamp.astimezone(local).date() < date.fromisoformat(end)}
    systems = Counter(system for _, system, _ in members.values())
    channel_counts = {system: dict(Counter(channel for _, os_name, channel in members.values() if os_name == system))
                      for system in systems}
    retained = {system: sum((uid, day + timedelta(days=1)) in active
                           for uid, (day, os_name, _) in members.items() if os_name == system) for system in systems}
    return {'window': [start, end], 'users_by_system': dict(systems),
            'channels_by_system': channel_counts, 'retained_by_system': retained}
