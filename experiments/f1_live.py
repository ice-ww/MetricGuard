"""Development-only real-provider clarification acceptance (not frozen evaluation)."""
import json
import os
from pathlib import Path
import duckdb
from datetime import datetime, timezone, timedelta
from uuid import uuid4
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService


def main():
    root = Path('artifacts/f1-live') / uuid4().hex
    root.mkdir(parents=True, exist_ok=True)
    snapshot = build_snapshot(root / 'data', scenario='normal', seed=2026101501,
                              base_start=datetime(2026, 6, 1, tzinfo=timezone(timedelta(hours=8)))).database
    with duckdb.connect(str(snapshot), read_only=True) as db:
        reference = db.execute("""SELECT COUNT(*), SUM(CASE WHEN EXISTS(
            SELECT 1 FROM sessions s WHERE s.user_id=u.user_id
            AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=
                CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)+1)
            THEN 1 ELSE 0 END) FROM users u
            WHERE CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='2026-06-08'
            AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'2026-06-15'""").fetchone()
    image = os.environ['METRICGUARD_TEST_IMAGE']
    with TaskService(root / 'state', image, {'dev': snapshot}, token=os.environ['ANTHROPIC_AUTH_TOKEN']) as service:
        state = service.run(service.create('用户表现怎么样？', 'dev', ('2026-06-08', '2026-06-15')))
        task = state['id']
        for answer in ('留存', '新增用户'):
            pending = state['pending_question']
            state = service.answer(task, pending['question_id'], pending['version'], answer)
        assert state['status'] == 'waiting' and state['rounds'] == 3
    with TaskService(root / 'state', image, {'dev': snapshot}, token=os.environ['ANTHROPIC_AUTH_TOKEN']) as service:
        state = service.inspect(task)
        pending = state['pending_question']
        state = service.answer(task, pending['question_id'], pending['version'], '1')
        publication = service.publish_diagnosis(task)
        result = {'task': service.inspect(task), 'publication': publication,
                  'independent_reference': {'users': reference[0], 'retained': reference[1],
                                             'retention_rate': reference[1] / reference[0]}}
        (root / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
        assert state['status'] == 'ended' and state['analysis_result'] == 'facts_available'
        assert publication['status'] == 'mechanically_valid'
        rows = state['evidence'][0]['rows']
        assert sum(row['new_users'] for row in rows) == reference[0]
        assert sum(row['retained_users'] for row in rows) == reference[1]
        assert all(abs(row['next_day_retention_rate'] - row['retained_users'] / row['new_users']) < 1e-12 for row in rows)
        print(json.dumps({'task': task, 'result': state['analysis_result'], 'reference': result['independent_reference'],
                          'publication': publication['status'], 'artifact': str(root / 'result.json')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
