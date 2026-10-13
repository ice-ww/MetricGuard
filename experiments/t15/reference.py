"""Development oracle: independent raw-row sets, never product profile SQL."""
import argparse
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
import json
from pathlib import Path
from typing import Any
import duckdb

SHANGHAI = timezone(timedelta(hours=8))


def reference(database: Path, start: str, end: str) -> dict[str, Any]:
    left, right = date.fromisoformat(start), date.fromisoformat(end)
    before = left - (right-left)
    with duckdb.connect(str(database), read_only=True) as con:
        users = con.execute('SELECT user_id,registered_at,registration_os FROM users').fetchall()
        sessions = con.execute('SELECT user_id,started_at FROM sessions').fetchall()
    returns: dict[str, set] = defaultdict(set)
    for uid, at in sessions:
        if at:
            returns[uid].add(at.astimezone(SHANGHAI).date())
    groups: dict[tuple, list] = defaultdict(list)
    for uid, at, system in users:
        if at:
            day = at.astimezone(SHANGHAI).date()
            if before <= day < right:
                groups[('previous' if day < left else 'current', system)].append((uid, day))
    rows = []
    for (period, system), members in sorted(groups.items(), key=lambda x: (x[0][0], x[0][1] or '')):
        retained = len({uid for uid, day in members if day + timedelta(days=1) in returns[uid]})
        rows.append(dict(period=period, registration_os=system, users=len(members), retained=retained,
            retention_rate=retained/len(members), window_start=before.isoformat() if period=='previous' else start,
            window_end=start if period=='previous' else end))
    totals = {p: sum(r['users'] for r in rows if r['period']==p) for p in ('previous', 'current')}
    actual = {p: sum(r['retained'] for r in rows if r['period']==p)/n if n else None for p, n in totals.items()}
    previous = {r['registration_os']: r for r in rows if r['period']=='previous'}
    current = {r['registration_os']: r for r in rows if r['period']=='current'}
    standard = None
    if previous and previous.keys()==current.keys() and None not in previous:
        # Reference expands baseline membership, then averages each member's current group rate.
        standard = sum(current[system]['retained']/current[system]['users']
                       for (period, system), members in groups.items() if period=='previous'
                       for _ in members) / totals['previous']
    return dict(rows=rows, actual_retention=actual, standardized_retention=standard,
                within_effect_pp=(standard-actual['previous'])*100 if standard is not None else None,
                composition_effect_pp=(actual['current']-standard)*100 if standard is not None else None,
                total_change_pp=(actual['current']-actual['previous'])*100 if actual['current'] is not None and actual['previous'] is not None else None)


def build(output: Path) -> dict:
    from experiments.t01.snapshots import build_snapshot
    cases = []
    for name, first, share, retention, seed, scenario in (
        ('january','2026-01-01',2/3,.30,1501,'A4'),
        ('may','2026-05-03',.60,.38,1502,'A4'),
        ('september','2026-09-05',.75,.20,1503,'A4'),
        ('normal','2026-01-01',2/3,.30,1504,'normal')):
        base = datetime.combine(date.fromisoformat(first), datetime.min.time(), SHANGHAI)
        snap = build_snapshot(output/name, scenario=scenario, seed=seed, base_start=base,
                              current_ios_share=share, current_android_retention=retention)
        start, end = [(base+timedelta(days=n)).date().isoformat() for n in (7,14)]
        cases.append(dict(case=name, database=str(snap.database.resolve()), current_start=start, end=end,
            logical_hash=snap.logical_hash, private_parameters=dict(seed=seed, current_ios_share=share, current_android_retention=retention),
            reference=reference(snap.database,start,end)))
    manifest = dict(purpose='development only; not frozen acceptance or product input', cases=cases)
    (output/'manifest.json').write_text(json.dumps(manifest, indent=2),encoding='utf-8')
    return manifest


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(build(args.output)))
