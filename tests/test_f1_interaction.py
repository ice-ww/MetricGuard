"""User-visible clarification through the approved task-service seam."""
from metricguard import TaskService
import os
import subprocess
import sys
import re


def test_known_dates_ask_only_for_metric_and_offer_answers(tmp_path):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'not queried while waiting')
    with TaskService(tmp_path / 'state', 'unused', {'dev': snapshot}, token='controlled') as service:
        state = service.run(service.create('用户表现怎么样？', 'dev', ('2026-06-08', '2026-06-15')))
        pending = state['pending_question']
        assert pending['reason'] == 'metric_required'
        assert '时间窗口' not in pending['prompt']
        assert '2026-06-08' in pending['known_information']
        assert pending['options']


def test_progress_across_three_clarification_stages_survives_restart(tmp_path):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'not queried while waiting')
    root = tmp_path / 'state'
    with TaskService(root, 'unused', {'dev': snapshot}, token='controlled') as service:
        state = service.run(service.create('用户表现怎么样？', 'dev', ('2026-06-08', '2026-06-15')))
        task = state['id']
        for answer in ('留存', '新增用户'):
            pending = state['pending_question']
            state = service.answer(task, pending['question_id'], pending['version'], answer)
        assert state['status'] == 'waiting'
        assert state['pending_question']['reason'] == 'retention_horizon_required'
        assert state['rounds'] == 3 and state['tool_calls'] == 3
    with TaskService(root, 'unused', {'dev': snapshot}, token='controlled') as service:
        assert service.inspect(task) == state


def test_console_renders_choices_and_can_resume_without_internal_ids(tmp_path):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'not queried while waiting')
    command = [sys.executable, '-m', 'metricguard', '--state-dir', str(tmp_path / 'state'),
               '--image', 'unused', '--snapshot', 'dev=' + str(snapshot),
               'chat', '用户表现怎么样？', 'dev', '--window', '2026-06-08', '2026-06-15']
    result = subprocess.run(command, input='留存\n\n', capture_output=True, text=True, encoding='utf-8',
                            env={**os.environ, 'PYTHONUTF8': '1'}, timeout=30)
    assert result.returncode == 0, result.stderr
    assert '2026-06-08' in result.stdout and '1. 新增用户' in result.stdout
    assert 'question_id' not in result.stdout and 'metric_required' not in result.stdout
    assert '保留待回答任务' in result.stdout
    task = re.search(r'resume ([a-f0-9]{32})', result.stdout).group(1)
    resumed = subprocess.run(command[:command.index('chat')] + ['resume', task], input='1\n\n',
                             capture_output=True, text=True, encoding='utf-8',
                             env={**os.environ, 'PYTHONUTF8': '1'}, timeout=30)
    assert resumed.returncode == 0, resumed.stderr
    assert '自然日次日' in resumed.stdout and 'question_id' not in resumed.stdout


def test_option_answer_is_resolved_by_service_and_invalid_answers_are_bounded(tmp_path):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'not queried while waiting')
    with TaskService(tmp_path / 'state', 'unused', {'dev': snapshot}, token='controlled') as service:
        state = service.run(service.create('留存', 'dev', ('2026-06-08', '2026-06-15')))
        pending = state['pending_question']
        state = service.answer(state['id'], pending['question_id'], pending['version'], '1')
        assert state['answers'][0]['answer'] == '新增用户'
        assert state['pending_question']['reason'] == 'retention_horizon_required'
        for _ in range(2):
            pending = state['pending_question']
            state = service.answer(state['id'], pending['question_id'], pending['version'], '不知道')
        assert state['status'] == 'ended' and state['model_calls'] == 0
        assert 'clarification_limit' in state['limitations']
        assert any('留存周期' in q for q in state['unresolved_questions'])


def test_selecting_one_of_two_metrics_removes_original_ambiguity(tmp_path):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'not queried while waiting')
    with TaskService(tmp_path / 'state', 'unused', {'dev': snapshot}, token='controlled') as service:
        state = service.run(service.create('观测完播率和新增用户首日崩溃受影响比例', 'dev', ('2026-06-08', '2026-06-15')))
        pending = state['pending_question']
        assert pending['reason'] == 'candidate_ambiguity'
        # Select a partially specified metric to observe subsequent progress without a query.
        state = service.answer(state['id'], pending['question_id'], pending['version'], '留存')
        assert state['pending_question']['reason'] == 'retention_population_required'
