"""Real child-process termination; no replacement of graph, ledger, or executor."""
import json
import os
import subprocess
import sys

import pytest

from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService


@pytest.mark.parametrize('point,sends,state', [
    ('after_reserve', 0, 'unknown'), ('after_send', 1, 'unknown'),
    ('after_result', 1, 'completed'), ('before_checkpoint', 1, 'completed'),
    ('after_checkpoint', 1, 'completed')])
def test_public_service_process_crash_preserves_ledger_and_never_resends(tmp_path, point, sends, state):
    image = os.environ.get('METRICGUARD_TEST_IMAGE')
    if not image:
        pytest.skip('requires final validated Docker image')
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal', seed=1010)
    root = tmp_path / point
    child = subprocess.run([sys.executable, '-m', 'experiments.t10.crash_worker', str(root),
                            str(snapshot.database), image, point], capture_output=True, timeout=90)
    assert child.returncode == 73, child.stderr.decode(errors='replace')
    task = (root / 'task.txt').read_text()
    provider = root / 'provider.jsonl'
    before = provider.read_bytes() if provider.exists() else b''
    assert len(before.splitlines()) == sends
    with TaskService(root / 'service', image, {'development': snapshot.database}, token='controlled') as service:
        old = service.inspect(task)
        assert old['status'] == 'interrupted'
        assert old['model_calls'] == 1
        assert old['active'] >= old['limits']['active_seconds']
        models = [attempt for attempt in old['attempts'] if attempt['kind'] == 'model']
        assert models[0]['state'] == state
        if state == 'unknown':
            assert models[0]['actual'] is None
            assert old['tokens'] == models[0]['reserved'] > 2048
        else:
            assert old['tokens'] == models[0]['actual'] == 42
        if point in ('before_checkpoint', 'after_checkpoint'):
            assert len(old['evidence']) == 1
            assert old['query_result']['cleanup_verified']
        with pytest.raises(ValueError):
            service.run(task)
        new = service.rerun(task)
        fresh = service.inspect(new)
        assert fresh['id'] != task and fresh['parent'] == task
        assert fresh['model_calls'] == fresh['tool_calls'] == fresh['tokens'] == 0
        assert service.inspect(task) == old
        assert any(event['event'] == 'interrupted' for event in service.trace(task))
    assert (provider.read_bytes() if provider.exists() else b'') == before
    record = {'point': point, 'exit_code': child.returncode, 'provider_sends': sends,
              'recovered': old, 'new_task': fresh, 'passed': True}
    (root / 'checked.json').write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')


def test_unknown_usage_survives_final_service_restart_and_explicit_rerun(tmp_path):
    import duckdb
    import httpx2 as httpx
    from experiments.t07 import ModelAdapter, Request

    image = os.environ.get('METRICGUARD_TEST_IMAGE')
    if not image:
        pytest.skip('requires final validated Docker image')
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal', seed=1011)
    with duckdb.connect(str(snapshot.database), read_only=True) as con:
        expected = len(set(row[0] for row in con.execute('SELECT user_id FROM users').fetchall()))
    requests = []

    def provider(request):
        requests.append(json.loads(request.content))
        body = {'id': 'msg_unknown', 'type': 'message', 'role': 'assistant', 'model': 'deepseek-flash',
                'content': [{'type': 'text', 'text': json.dumps(
                    {'facts': [{'row': 0, 'column': 'users', 'value': expected}]} if len(requests) == 3
                    else {'sql': 'SELECT COUNT(*) AS users FROM users'})}],
                'stop_reason': 'end_turn', 'stop_sequence': None}
        if len(requests) > 1:
            body['usage'] = {'input_tokens': 29, 'output_tokens': 13}
        return httpx.Response(200, json=body)

    root = tmp_path / 'service'
    with TaskService(root, image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'dev', ('2026-01-01', '2026-01-08'))
        old = service.run(task)
        assert old['outcome'] == 'budget_exhausted' and old['model_calls'] == 1
        model = next(attempt for attempt in old['attempts'] if attempt['kind'] == 'model')
        assert model['actual'] is None and old['tokens'] == model['reserved'] > 2048
    with TaskService(root, image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        assert service.inspect(task) == old
        wire = requests[0]
        system, shared = wire['system'].split('\n\nShared materials:\n', 1)
        with pytest.raises(ValueError):
            service.run(task)
        adapter = ModelAdapter(service.ledger, 'deepseek-flash', 'https://fixture.invalid', 'controlled',
                               transport=httpx.MockTransport(provider))
        try:
            replay = adapter.call(task, 'sql_plan', Request(system, shared, wire['messages'], wire['tools'], wire['max_tokens']),
                                  attempt_id=model['id'])
            assert replay['status'] == 'unknown_usage' and replay['fee_usd_range'] is None
        finally:
            adapter.close()
        assert len(requests) == 1 and service.inspect(task) == old
        new = service.rerun(task)
        done = service.run(new)
        assert done['parent'] == task and done['model_calls'] == 2 and done['tokens'] == 84
        assert service.report(new)['validation']['passed']
        assert service.report(new)['facts'][0]['value'] == expected
        assert service.inspect(task) == old and len(requests) == 3
