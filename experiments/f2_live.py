"""Real terminal/provider date-conflict development acceptance."""
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
    root = Path('artifacts/f2-live') / uuid4().hex
    root.mkdir(parents=True)
    snapshot = build_snapshot(root / 'data', scenario='normal', seed=2026101502,
                              base_start=datetime(2026, 6, 1, tzinfo=timezone(timedelta(hours=8)))).database
    image = os.environ['METRICGUARD_TEST_IMAGE']
    command = [sys.executable, '-m', 'metricguard', '--state-dir', str(root / 'state'), '--image', image,
               '--snapshot', 'dev=' + str(snapshot), 'chat', '昨天新增用户数是多少？', 'dev',
               '--window', '2026-06-08', '2026-06-15']
    run = subprocess.run(command, input='2\n', text=True, encoding='utf-8', capture_output=True,
                         env={**os.environ, 'PYTHONUTF8': '1'}, timeout=240)
    (root / 'terminal.txt').write_text(run.stdout + run.stderr, encoding='utf-8')
    assert run.returncode == 0, run.stderr
    match = re.search(r'inspect ([a-f0-9]{32})', run.stdout)
    assert match is not None, run.stdout
    with TaskService(root / 'state', image, {'dev': snapshot}, token=os.environ['ANTHROPIC_AUTH_TOKEN']) as service:
        state = service.inspect(match.group(1))
        publication = service.publish_diagnosis(state['id'])
    with duckdb.connect(str(snapshot), read_only=True) as db:
        raw = db.execute('SELECT user_id, registered_at FROM users').fetchall()
    local = timezone(timedelta(hours=8))
    expected = len({uid for uid, registered in raw if '2026-06-08' <= registered.astimezone(local).date().isoformat() < '2026-06-15'})
    receipt = {'task': state, 'publication': publication, 'reference_users': expected, 'terminal': run.stdout}
    (root / 'result.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding='utf-8')
    assert state['status'] == 'ended' and state['analysis_result'] == 'facts_available'
    assert state['answers'][0]['reason'] == 'time_window_conflict'
    assert state['actual_window'] == ['2026-06-08', '2026-06-15']
    assert publication['status'] == 'mechanically_valid'
    rows = state['evidence'][0]['rows']
    counts = [sum(row[column] for row in rows) for column in rows[0] if all(type(row[column]) is int for row in rows)]
    assert expected in counts
    print(json.dumps({'task': state['id'], 'reference_users': expected, 'artifact': str(root / 'result.json')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
