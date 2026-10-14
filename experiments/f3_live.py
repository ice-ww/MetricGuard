"""Real terminal/provider comparison acceptance with an independent raw-row reference."""
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from uuid import uuid4

import duckdb
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService


def main():
    root = Path('artifacts/f3-live') / uuid4().hex
    root.mkdir(parents=True)
    local = timezone(timedelta(hours=8))
    snapshot = build_snapshot(root / 'data', scenario='A4', seed=2026101503,
                              base_start=datetime(2026, 6, 1, tzinfo=local)).database
    image = os.environ['METRICGUARD_TEST_IMAGE']
    command = [sys.executable, '-m', 'metricguard', '--state-dir', str(root / 'state'), '--image', image,
               '--snapshot', 'dev=' + str(snapshot), 'chat', '昨天新增用户自然日次日留存变化，请分析系统结构。', 'dev',
               '--window', '2026-06-08', '2026-06-15', '--mode', 'diagnose']
    run = subprocess.run(command, input='2\n2026-06-01至2026-06-03\n', text=True, encoding='utf-8', capture_output=True,
                         env={**os.environ, 'PYTHONUTF8': '1'}, timeout=240)
    (root / 'terminal.txt').write_text(run.stdout + run.stderr, encoding='utf-8')
    assert run.returncode == 0, run.stderr
    match = re.search(r'inspect ([a-f0-9]{32})', run.stdout)
    assert match is not None, run.stdout
    with TaskService(root / 'state', image, {'dev': snapshot}, token=os.environ['ANTHROPIC_AUTH_TOKEN']) as service:
        state = service.inspect(match.group(1))
        publication = service.publish_diagnosis(state['id'])
    with duckdb.connect(str(snapshot), read_only=True) as db:
        users = db.execute('SELECT user_id, registered_at, registration_os FROM users').fetchall()
        sessions = db.execute('SELECT user_id, started_at FROM sessions').fetchall()
    active = {(uid, at.astimezone(local).date()) for uid, at in sessions}
    reference = []
    for period, start, end in [('previous', '2026-06-01', '2026-06-04'), ('current', '2026-06-08', '2026-06-15')]:
        for system in ('Android', 'iOS'):
            selected = [(uid, at.astimezone(local).date()) for uid, at, os_name in users
                        if start <= at.astimezone(local).date().isoformat() < end and os_name == system]
            retained = sum((uid, day + timedelta(days=1)) in active for uid, day in selected)
            reference.append({'period': period, 'registration_os': system, 'users': len(selected), 'retained': retained,
                              'retention_rate': retained / len(selected), 'window_start': start, 'window_end': end})
    receipt = {'task': state, 'publication': publication, 'reference': reference, 'terminal': run.stdout}
    (root / 'result.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding='utf-8')
    assert state['status'] == 'ended' and state['outcome'] == 'facts_available', state['limitations']
    assert [a['reason'] for a in state['answers']] == ['time_window_conflict', 'comparison_window_required']
    assert state['actual_window'] == ['2026-06-08', '2026-06-15']
    assert state['comparison_window'] == ['2026-06-01', '2026-06-04']
    assert publication['status'] == 'mechanically_valid'
    evidence = next(e for e in state['evidence'] if e['parameters'].get('kind') == 'system_retention')
    assert sorted(evidence['rows'], key=lambda r: (r['period'], r['registration_os'])) == sorted(reference, key=lambda r: (r['period'], r['registration_os']))
    previous = [a for a in publication['assertions'] if a['context']['comparison'] == 'previous']
    assert previous and all(a['context']['window'] == ['2026-06-01', '2026-06-04'] for a in previous)
    assert '比较基期：2026-06-01 至 2026-06-04' in run.stdout
    print(json.dumps({'task': state['id'], 'reference': reference, 'artifact': str(root / 'result.json')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
