from experiments.t05 import Ledger

def test_durable_attempts_and_true_retry(tmp_path):
    ledger = Ledger(tmp_path / 'ledger.sqlite')
    task = ledger.create_task()
    first = ledger.reserve(task, 'query', 'tool', attempt_id='first')
    ledger.mark_sent(first['attempt_id'])
    ledger.settle('first', {'error': 'query failed'}, failed=True)
    reopened = Ledger(tmp_path / 'ledger.sqlite')
    assert reopened.reserve(task, 'query', 'tool', attempt_id='first')['state'] == 'failed'
    reopened.reserve(task, 'query', 'tool', attempt_id='retry')
    report = reopened.inspect(task)
    assert report['tool_calls'] == 2
    assert len(report['attempts']) == 2

def test_clarification_survives_restart_without_repeating_call(tmp_path):
    from experiments.t05 import TaskService
    service = TaskService(tmp_path)
    task = service.create()
    waiting = service.run(task)
    assert waiting['status'] == 'waiting'
    assert waiting['model_calls'] == 1
    service.close()
    restarted = TaskService(tmp_path)
    second = restarted.answer(task, waiting['question'], waiting['version'], 'yes')
    assert second['status'] == 'waiting'
    assert second['model_calls'] == 2
    import pytest
    with pytest.raises(ValueError):
        restarted.answer(task, waiting['question'], waiting['version'], 'duplicate')
    done = restarted.answer(task, second['question'], second['version'], 'yes')
    assert done['status'] == 'ended'
    assert done['model_calls'] == 3
    assert done['rounds'] == 2
    restarted.close()


def test_waiting_does_not_consume_active_time_and_model_cannot_edit_state(tmp_path):
    import time
    import pytest
    from experiments.t05 import TaskService
    with TaskService(tmp_path) as service:
        task = service.create()
        waiting = service.run(task)
        before = waiting['active']
        time.sleep(.05)
        assert service.inspect(task)['active'] == before
        with pytest.raises(ValueError):
            service.model_reply(task, {'text': 'hi', 'limits': {'model': 900}})
        assert service.inspect(task)['limits']['model'] == 10
        resumed = service.answer(task, waiting['question'], waiting['version'], 'yes')
        assert resumed['active'] > before
        assert resumed['tokens'] == 60
        with pytest.raises(ValueError):
            service.run(service.create(), questions=3)

import subprocess
import sys
import json
import pytest

@pytest.mark.parametrize('point,expected_sends,expected_tokens,expected_state', [
    ('after_reserve', 0, 100, 'unknown'),
    ('after_send', 1, 100, 'unknown'),
    ('after_result', 1, 30, 'completed'),
    ('before_checkpoint', 1, 30, 'completed'),
    ('after_checkpoint', 1, 30, 'completed'),
])
def test_real_process_crash_never_resumes(tmp_path, point, expected_sends, expected_tokens, expected_state):
    from experiments.t05 import TaskService
    child = subprocess.run([sys.executable, '-m', 'experiments.t05', 'crash-worker', str(tmp_path), point], capture_output=True, timeout=30)
    assert child.returncode == 73, child.stderr.decode()
    task = (tmp_path / 'task.txt').read_text()
    provider = tmp_path / 'provider.jsonl'
    before = provider.read_text().splitlines() if provider.exists() else []
    assert len(before) == expected_sends
    with TaskService(tmp_path) as restarted:
        state = restarted.inspect(task)
        assert state['status'] == 'interrupted'
        assert state['model_calls'] == 1
        assert state['tokens'] == expected_tokens
        assert state['attempts'][0]['state'] == expected_state
        with pytest.raises(ValueError):
            restarted.run(task)
        new_task = restarted.rerun(task)
        assert new_task != task
        assert restarted.inspect(new_task)['parent'] == task
        assert restarted.inspect(new_task)['model_calls'] == 0
    after = provider.read_text().splitlines() if provider.exists() else []
    assert after == before

def test_global_budgets_survive_failed_attempts_and_restart(tmp_path):
    ledger = Ledger(tmp_path / 'budget.sqlite')
    task = ledger.create_task(limits={'tool': 3, 'model': 2, 'tokens': 100})
    for i in range(3):
        a = ledger.reserve(task, 'same-query', 'tool')
        ledger.mark_sent(a['id'])
        ledger.settle(a['id'], {'error': 'failed'}, failed=True)
    reopened = Ledger(tmp_path / 'budget.sqlite')
    with pytest.raises(ValueError, match='budget'):
        reopened.reserve(task, 'new-query-id', 'tool')
    a = reopened.reserve(task, 'model', 'model', 80)
    reopened.mark_sent(a['id'])
    reopened.settle(a['id'], {'unknown_usage': True})
    assert reopened.inspect(task)['tokens'] == 80
    with pytest.raises(ValueError, match='budget'):
        reopened.reserve(task, 'new-model', 'model', 21)


def test_single_service_owner_and_task_closed_cannot_dispatch(tmp_path):
    from experiments.t05 import TaskService
    with TaskService(tmp_path) as service:
        with pytest.raises(ValueError, match='owned'):
            TaskService(tmp_path)
        task = service.create()
        service.run(task, questions=0)
        with pytest.raises(ValueError):
            service.ledger.reserve(task, 'late', 'model', 100)

def test_active_budget_blocks_next_send_inside_same_segment(tmp_path):
    import time
    ledger = Ledger(tmp_path / 'elapsed.sqlite')
    task = ledger.create_task(limits={'active_seconds': .02})
    ledger.start_activity(task)
    time.sleep(.1)
    with pytest.raises(ValueError, match='budget'):
        ledger.reserve(task, 'first', 'tool')
    ledger.accrue_activity(task, stop=True)
    assert ledger.inspect(task)['tool_calls'] == 0
    assert ledger.inspect(task)['active'] >= .02


def test_missing_checkpoint_refuses_waiting_answer(tmp_path):
    from experiments.t05 import TaskService
    with TaskService(tmp_path) as service:
        task = service.create()
        first = service.run(task)
    (tmp_path / 'checkpoints.sqlite').unlink()
    with TaskService(tmp_path) as service:
        with pytest.raises(ValueError, match='checkpoint'):
            service.answer(task, first['question'], first['version'], 'answer')
        assert service.inspect(task)['model_calls'] == 1

@pytest.mark.parametrize('limits', [
    {'tool': True}, {'model': 1.5}, {'tokens': float('inf')},
    {'active_seconds': float('nan')}, {'active_seconds': float('inf')},
])
def test_nonfinite_or_fractional_policy_cannot_expand_budget(tmp_path, limits):
    with pytest.raises(ValueError):
        Ledger(tmp_path / 'bad.sqlite').create_task(limits=limits)
