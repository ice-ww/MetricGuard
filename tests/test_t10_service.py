"""Clarification and recovery through the production task-service public API."""
import json
import os
import time

import httpx2 as httpx
import pytest

from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService

@pytest.fixture
def snapshot(tmp_path):
    return build_snapshot(tmp_path / 'data', scenario='normal', seed=1007).database

@pytest.fixture
def image():
    value = os.environ.get('METRICGUARD_TEST_IMAGE')
    if not value:
        pytest.skip('requires final validated business image')
    return value


def test_ambiguous_question_waits_and_does_not_consume_user_wait_time(tmp_path, snapshot, image):
    with TaskService(tmp_path / 'service', image, {'dev': snapshot}, token='controlled') as service:
        task = service.create('留存', 'dev', ('2026-01-01', '2026-01-08'))
        waiting = service.run(task)
        assert waiting['status'] == 'waiting'
        assert waiting['outcome'] is None and service.report(task) is None
        assert waiting['pending_question']['reason'] == 'retention_population_required'
        assert waiting['tool_calls'] == 1 and waiting['model_calls'] == 0
        time.sleep(.15)
        assert service.inspect(task)['active'] == waiting['active']


def provider_response(content):
    return httpx.Response(200, json={'id': 'msg_t10', 'type': 'message', 'role': 'assistant',
        'model': 'deepseek-flash', 'content': [{'type': 'text', 'text': json.dumps(content)}],
        'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 10, 'output_tokens': 5}})


def test_two_answers_continue_same_task_and_stale_answers_do_not_dispatch(tmp_path, snapshot, image):
    requests = []
    def provider(request):
        requests.append(request)
        return provider_response({'sql': 'SELECT COUNT(*) AS users FROM users'} if len(requests) == 1 else
            {'facts': [{'row': 0, 'column': 'users', 'value': 3816}]})
    with TaskService(tmp_path / 'service', image, {'dev': snapshot}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        task = service.create('留存', 'dev', ('2026-01-01', '2026-01-08'))
        first = service.run(task); question1 = first['pending_question']
        second = service.answer(task, question1['question_id'], question1['version'], '新增用户')
        assert second['status'] == 'waiting' and second['rounds'] == 2
        assert second['tool_calls'] == 2 and second['active'] >= first['active']
        question2 = second['pending_question']
        with pytest.raises(ValueError, match='stale'):
            service.answer(task, question1['question_id'], question1['version'], '次日')
        done = service.answer(task, question2['question_id'], question2['version'], '新增用户自然日次日留存')
        assert done['status'] == 'ended' and done['id'] == task
        assert done['model_calls'] == 2 and done['tokens'] == 30
        assert done['tool_calls'] == 6 and len(done['answers']) == 2
        assert done['attempts'][:2] == second['attempts']
        assert done['evidence']
        with pytest.raises(ValueError, match='stale'):
            service.answer(task, question2['question_id'], question2['version'], '新增用户自然日次日留存')
        assert len(requests) == 2


def test_unresolved_clarification_stops_after_two_rounds(tmp_path, snapshot, image):
    with TaskService(tmp_path / 'service', image, {'dev': snapshot}, token='controlled') as service:
        task = service.create('留存', 'dev')
        state = service.run(task)
        for _ in range(2):
            question = state['pending_question']
            state = service.answer(task, question['question_id'], question['version'], '不知道')
        assert state['status'] == 'ended' and state['rounds'] == 2
        assert state['pending_question'] is None
        assert state['outcome'] == 'insufficient_evidence'
        assert 'clarification_limit' in state['limitations']
        assert state['tool_calls'] == 3 and state['model_calls'] == 0


def test_unsupported_question_never_repeatedly_clarifies(tmp_path, snapshot, image):
    with TaskService(tmp_path / 'service', image, {'dev': snapshot}, token='controlled') as service:
        result = service.run(service.create('活跃老用户七日留存', 'dev'))
        assert result['status'] == 'ended' and result['outcome'] == 'unsupported'
        assert result['rounds'] == 0 and result['pending_question'] is None


def test_waiting_task_survives_restart_and_rerun_has_new_budget(tmp_path, snapshot, image):
    root = tmp_path / 'service'
    with TaskService(root, image, {'dev': snapshot}, token='controlled', limits={'model': 1}) as service:
        task = service.create('留存', 'dev', ('2026-01-01', '2026-01-08'))
        waiting = service.run(task)
    time.sleep(.1)
    with TaskService(root, image, {'dev': snapshot}, token='controlled', limits={'model': 1}) as service:
        assert service.inspect(task) == waiting
        pending = waiting['pending_question']
        finished = service.answer(task, pending['question_id'], pending['version'], '新增用户自然日次日留存')
        assert finished['status'] == 'ended' and finished['outcome'] == 'budget_exhausted'
        fresh = service.rerun(task)
        new = service.inspect(fresh)
        assert fresh != task and new['parent'] == task
        assert new['tool_calls'] == new['model_calls'] == new['tokens'] == 0
        assert new['requested_window'] == finished['requested_window']
        assert service.inspect(task) == finished


def test_completed_provider_attempt_replays_from_final_service_ledger(tmp_path, snapshot, image):
    from experiments.t07 import ModelAdapter, Request
    requests = []
    def provider(request):
        requests.append(json.loads(request.content))
        return provider_response({'sql': 'SELECT COUNT(*) AS users FROM users'} if len(requests) == 1 else
            {'facts': [{'row': 0, 'column': 'users', 'value': 3816}]})
    with TaskService(tmp_path / 'service', image, {'dev': snapshot}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        task = service.create('留存', 'dev', ('2026-01-01', '2026-01-08'))
        waiting = service.run(task)
        question = waiting['pending_question']
        done = service.answer(task, question['question_id'], question['version'], '新增用户自然日次日留存')
        wire = requests[0]
        system, shared = wire['system'].split('\n\nShared materials:\n', 1)
        original_request = Request(system, shared, wire['messages'], wire['tools'], wire['max_tokens'])
        # Final service's durable ledger, SDK public call, and real recorded wire request.
        adapter = ModelAdapter(service.ledger, 'deepseek-flash', 'https://fixture.invalid', 'controlled',
                               transport=httpx.MockTransport(provider))
        try:
            replay = adapter.call(task, 'sql_plan', original_request, attempt_id=task + ':sql_plan')
        finally:
            adapter.close()
        assert replay['status'] == 'completed'
        assert service.inspect(task) == done
        assert len(requests) == 2


def test_valid_long_clarification_context_can_rerun(tmp_path, snapshot, image):
    with TaskService(tmp_path / 'service', image, {'dev': snapshot}, token='controlled', limits={'model': 1}) as service:
        task = service.create('留存' + ' ' * 1998, 'dev')
        waiting = service.run(task)
        pending = waiting['pending_question']
        finished = service.answer(task, pending['question_id'], pending['version'], '新增用户自然日次日留存')
        assert finished['status'] == 'ended'
        new = service.rerun(task)
        assert service.inspect(new)['effective_question'] == finished['effective_question']
        assert service.inspect(new)['parent'] == task


def test_pre_t10_persisted_request_remains_runnable_and_rerunnable(tmp_path, snapshot, image):
    import sqlite3
    root = tmp_path / 'service'
    with TaskService(root, image, {'dev': snapshot}, token='controlled', limits={'model': 1}) as service:
        task = service.create('新增用户自然日次日留存', 'dev', ('2026-01-01', '2026-01-08'))
    # Migration fixture reproduces the persisted 0b68abd JSON format. Only fixture
    # construction touches storage; all compatibility observations use public API.
    with sqlite3.connect(root / 'ledger.sqlite') as db:
        payload = json.loads(db.execute('SELECT payload FROM analysis_requests WHERE id=?', (task,)).fetchone()[0])
        for added_in_t10 in ('answers', 'effective_question', 'pending_question'):
            payload.pop(added_in_t10)
        db.execute('UPDATE analysis_requests SET payload=? WHERE id=?', (json.dumps(payload), task))
    with TaskService(root, image, {'dev': snapshot}, token='controlled', limits={'model': 1}) as service:
        result = service.run(task)
        assert result['status'] == 'ended' and result['outcome'] == 'budget_exhausted'
        new = service.rerun(task)
        assert service.inspect(new)['effective_question'] == payload['question']
        assert service.inspect(new)['parent'] == task


def test_concurrent_duplicate_answers_dispatch_only_one_continuation(tmp_path, snapshot, image):
    from concurrent.futures import ThreadPoolExecutor
    from threading import Barrier
    requests = []
    def provider(request):
        requests.append(request)
        return provider_response({'sql': 'SELECT COUNT(*) AS users FROM users'} if len(requests) == 1 else
            {'facts': [{'row': 0, 'column': 'users', 'value': 3816}]})
    with TaskService(tmp_path / 'service', image, {'dev': snapshot}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        task = service.create('留存', 'dev', ('2026-01-01', '2026-01-08'))
        pending = service.run(task)['pending_question']
        barrier = Barrier(2)
        def submit():
            barrier.wait()
            try:
                return service.answer(task, pending['question_id'], pending['version'], '新增用户自然日次日留存')['status']
            except ValueError:
                return 'rejected'
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: submit(), range(2)))
        assert sorted(results) == ['ended', 'rejected']
        assert len(requests) == 2
        assert service.inspect(task)['model_calls'] == 2
        assert len(service.inspect(task)['answers']) == 1
