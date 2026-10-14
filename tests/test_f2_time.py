"""Date interpretation is observed through public tasks, with a fixed external clock."""
from datetime import datetime, timezone
import pytest
from metricguard import TaskService
import json
import os
import httpx2 as httpx
from experiments.t01.snapshots import build_snapshot


def test_yesterday_conflict_waits_and_anchor_survives_midnight(tmp_path):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'no query until dates chosen')
    root = tmp_path / 'state'
    with TaskService(root, 'unused', {'dev': snapshot}, token='controlled',
                     clock=lambda: datetime(2026, 10, 14, 15, 59, tzinfo=timezone.utc)) as service:
        task = service.create('昨天的用户表现怎么样？', 'dev', ('2026-06-08', '2026-06-15'))
        state = service.run(task)
        assert state['status'] == 'waiting' and state['model_calls'] == 0
        assert state['pending_question']['reason'] == 'time_window_conflict'
        assert '2026-10-13' in state['pending_question']['prompt']
    with TaskService(root, 'unused', {'dev': snapshot}, token='controlled',
                     clock=lambda: datetime(2026, 10, 15, tzinfo=timezone.utc)) as service:
        pending = service.inspect(task)['pending_question']
        state = service.answer(task, pending['question_id'], pending['version'], '1')
        assert state['requested_window'] == ['2026-10-13', '2026-10-14']
        assert state['pending_question']['reason'] == 'metric_required'
        assert state['time_anchor'] == '2026-10-14T23:59:00+08:00'


@pytest.mark.parametrize('text,anchor,expected', [
    ('昨天', '2026-01-01T00:01:00+08:00', ['2025-12-31', '2026-01-01']),
    ('前天', '2026-03-01T08:00:00+08:00', ['2026-02-27', '2026-02-28']),
    ('最近 7 天', '2026-10-15T08:00:00+08:00', ['2026-10-08', '2026-10-15']),
    ('本周', '2026-10-15T08:00:00+08:00', ['2026-10-12', '2026-10-19']),
    ('上周', '2026-10-12T08:00:00+08:00', ['2026-10-05', '2026-10-12']),
    ('2026年6月8日至2026年6月14日', '2026-10-15T08:00:00+08:00', ['2026-06-08', '2026-06-15']),
    ('[2026-06-08,2026-06-15)', '2026-10-15T08:00:00+08:00', ['2026-06-08', '2026-06-15']),
    ('2026/06/08至2026/06/14', '2026-10-15T08:00:00+08:00', ['2026-06-08', '2026-06-15']),
])
def test_supported_dates_are_resolved_before_metric_clarification(tmp_path, text, anchor, expected):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path / 'state', 'unused', {'dev': snapshot}, token='controlled',
                     clock=lambda: datetime.fromisoformat(anchor)) as service:
        state = service.run(service.create(text + '用户表现怎么样？', 'dev', tuple(expected)))
        assert state['pending_question']['reason'] == 'metric_required'
        assert state['requested_window'] == expected


@pytest.mark.parametrize('text', ['最近', '前段时间', '2026-02-30', '6月8日', '最近0天', '昨天之前', '截至昨天', '近七天',
                                  '2026-06-08至6月14日', '2026-06-08或者2026-06-14',
                                  '2026-06-08至14日', '上周一', '昨天上午', '从2026-06-08起', '从昨天'])
def test_unclear_dates_do_not_silently_adopt_preset(tmp_path, text):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path / 'state', 'unused', {'dev': snapshot}, token='controlled') as service:
        state = service.run(service.create(text + '用户表现怎么样？', 'dev', ('2026-06-08', '2026-06-15')))
        assert state['pending_question']['reason'] == 'time_window_required'
        assert state['tool_calls'] == state['model_calls'] == 0


def test_confirmed_window_reaches_sql_evidence_report_and_rerun(tmp_path):
    image = os.environ['METRICGUARD_TEST_IMAGE']
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal', seed=2401).database
    sent = []
    sql = "SELECT COUNT(*) AS users FROM users WHERE CAST(registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='2026-01-08' AND CAST(registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'2026-01-09'"
    def provider(request):
        sent.append(json.loads(request.content))
        value = {'sql': sql} if len(sent) == 1 else {'facts': [{'row': 0, 'column': 'users', 'value': 240}]}
        return httpx.Response(200, json={'id': 'f2', 'type': 'message', 'role': 'assistant', 'model': 'deepseek-flash',
            'content': [{'type': 'text', 'text': json.dumps(value)}], 'stop_reason': 'end_turn',
            'stop_sequence': None, 'usage': {'input_tokens': 10, 'output_tokens': 5}})
    with TaskService(tmp_path / 'state', image, {'dev': snapshot}, token='controlled',
                     transport=httpx.MockTransport(provider), clock=lambda: datetime(2026, 1, 9, tzinfo=timezone.utc)) as service:
        state = service.run(service.create('昨天新增用户数是多少？', 'dev', ('2026-01-01', '2026-01-08')))
        pending = state['pending_question']
        state = service.answer(state['id'], pending['question_id'], pending['version'], '1')
        assert state['analysis_result'] == 'facts_available', state['limitations']
        assert state['actual_window'] == ['2026-01-08', '2026-01-09']
        assert state['evidence'][0]['source'] == sql and state['evidence'][0]['rows'] == [{'users': 240}]
        assert state['report']['window'] == state['actual_window']
        assert state['report']['original_window'] == ['2026-01-01', '2026-01-08']
        assert '2026-01-09' in sent[0]['system']
        new = service.inspect(service.rerun(state['id']))
        assert new['requested_window'] == state['requested_window']
        assert new['time_resolution'] == 'inherited_explicit_window'


def test_incomplete_request_is_not_silently_shortened(tmp_path):
    image = os.environ['METRICGUARD_TEST_IMAGE']
    snapshot = build_snapshot(tmp_path / 'data', scenario='insufficient', seed=2402).database
    with TaskService(tmp_path / 'state', image, {'dev': snapshot}, token='controlled') as service:
        state = service.run(service.create('新增用户自然日次日留存', 'dev', ('2026-01-08', '2026-01-15')))
        assert state['analysis_result'] == 'insufficient_evidence'
        assert state['actual_window'] is None and state['model_calls'] == 0
        assert state['requested_window'] == ['2026-01-08', '2026-01-15']


def test_legacy_request_without_anchor_requires_explicit_relative_dates(tmp_path):
    import sqlite3
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'not queried')
    root = tmp_path / 'state'
    with TaskService(root, 'unused', {'dev': snapshot}, token='controlled') as service:
        task = service.create('昨天用户表现怎么样？', 'dev', ('2026-06-08', '2026-06-15'))
    with sqlite3.connect(root / 'ledger.sqlite') as db:
        data = json.loads(db.execute('SELECT payload FROM analysis_requests WHERE id=?', (task,)).fetchone()[0])
        del data['time_anchor']
        db.execute('UPDATE analysis_requests SET payload=? WHERE id=?', (json.dumps(data), task))
    with TaskService(root, 'unused', {'dev': snapshot}, token='controlled') as service:
        state = service.run(task)
        assert state['pending_question']['reason'] == 'time_window_required'
        assert 'time_anchor' not in state


def test_shared_preparation_preserves_original_time_context(tmp_path):
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal', seed=2403).database
    clock = [datetime(2026, 1, 9, tzinfo=timezone.utc)]
    with TaskService(tmp_path / 'state', os.environ['METRICGUARD_TEST_IMAGE'], {'dev': snapshot},
                     token='controlled', clock=lambda: clock[0], limits={'model': 1}) as service:
        prepared = service.prepare_shared('昨天新增用户数', 'dev', ('2026-01-08', '2026-01-09'))
        before = service.inspect(prepared)
        clock[0] = datetime(2026, 1, 10, tzinfo=timezone.utc)
        after = service.inspect(service.create_from_shared(prepared, mode='diagnose'))
        for key in ('time_anchor', 'time_resolution', 'original_window', 'requested_window'):
            assert after[key] == before[key]
        finished = service.run(after['id'])
        rerun = service.run(service.rerun(finished['id']))
        assert rerun['outcome'] == 'budget_exhausted'
        assert rerun['actual_window'] == ['2026-01-08', '2026-01-09']
