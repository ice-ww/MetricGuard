"""T09 public service integration; actual SQL worker, provider-only controlled boundary."""
import json
import os
from pathlib import Path

import httpx2 as httpx
import pytest

from experiments.t01.snapshots import build_snapshot
from experiments.t01.references import python_metrics
from metricguard import TaskService

SQL = """SELECT COUNT(*) AS users FROM users WHERE registered_at >= '2026-01-01T00:00:00+08:00' AND registered_at < '2026-01-08T00:00:00+08:00'"""

@pytest.fixture
def fixture_snapshot(tmp_path):
    return build_snapshot(tmp_path / 'data', scenario='normal', seed=903)

@pytest.fixture
def image():
    value = os.environ.get('METRICGUARD_TEST_IMAGE')
    if not value:
        pytest.skip('requires validated business worker image; set METRICGUARD_TEST_IMAGE')
    return value


def response(value, usage=True):
    payload = {'id': 'msg_t09', 'type': 'message', 'role': 'assistant', 'model': 'deepseek-flash',
        'content': [{'type': 'text', 'text': json.dumps(value)}], 'stop_reason': 'end_turn', 'stop_sequence': None}
    if usage:
        payload['usage'] = {'input_tokens': 31, 'output_tokens': 17}
    return httpx.Response(200, json=payload)


def test_query_uses_actual_worker_and_publishes_reference_bound_facts(tmp_path, fixture_snapshot, image):
    reference = python_metrics(fixture_snapshot.database, '2026-01-01', '2026-01-08')
    expected = sum(row['users'] for row in reference['retention'])
    calls = []
    def provider(request):
        calls.append(json.loads(request.content))
        return response({'sql': SQL} if len(calls) == 1 else {'facts': [{'row': 0, 'column': 'users', 'value': expected}]})
    with TaskService(tmp_path / 'service', image, {'development': fixture_snapshot.database},
                     token='controlled', transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        result = service.run(task)
        report = service.report(task)
        assert result['status'] == 'ended', result['limitations']
        assert report['facts'][0]['value'] == expected
        assert report['validation']['passed']
        assert report['business_definition_status'] == 'requires_independent_reference'
        assert result['model_calls'] == 2 and result['tool_calls'] == 4
        assert result['tokens'] == 96
        assert result['definition']['id'] == 'retention'
        assert result['actual_window'] == ['2026-01-01', '2026-01-08']
        assert result['evidence'][0]['rows'] == [{'users': expected}]
        assert result['evidence'][0]['parameters']['sql'] == SQL
        assert any(event['event'] == 'query_completed' for event in service.trace(task))
        assert all('manifest' not in json.dumps(call) and 'scenario' not in json.dumps(call) for call in calls)



RETENTION_SQL = """WITH c AS (SELECT u.user_id, CASE WHEN EXISTS (SELECT 1 FROM sessions s WHERE s.user_id=u.user_id AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)+1) THEN 1 ELSE 0 END AS returned FROM users u WHERE CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='2026-01-01' AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'2026-01-08') SELECT COUNT(*) AS users, SUM(returned) AS retained, SUM(returned)*1.0/NULLIF(COUNT(*),0) AS retention_rate FROM c"""


def test_retention_counts_deduplicated_next_calendar_day_not_24_hours(tmp_path, fixture_snapshot, image):
    reference = python_metrics(fixture_snapshot.database, '2026-01-01', '2026-01-08')
    users = sum(row['users'] for row in reference['retention'])
    retained = sum(row['retained'] for row in reference['retention'])
    expected = {'users': users, 'retained': retained, 'retention_rate': retained / users}
    sent = []
    def provider(request):
        sent.append(request)
        return response({'sql': RETENTION_SQL} if len(sent) == 1 else {'facts': [
            {'row': 0, 'column': key, 'value': value} for key, value in expected.items()]})
    with TaskService(tmp_path / 'service', image, {'development': fixture_snapshot.database},
                     token='controlled', transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        result = service.run(task)
        assert result['evidence'][0]['rows'] == [expected], result['limitations']
        assert service.report(task)['validation']['valid_count'] == 3
        assert result['evidence'][0]['columns'] == {'users': 'integer', 'retained': 'integer', 'retention_rate': 'number'}


def test_unknown_provider_usage_preserves_reservation_and_next_task_works(tmp_path, fixture_snapshot, image):
    sent = []
    def provider(request):
        sent.append(request)
        if len(sent) == 1:
            return response({'sql': SQL}, usage=False)
        return response({'sql': SQL} if len(sent) == 2 else {'facts': [{'row': 0, 'column': 'users', 'value': 1656}]})
    with TaskService(tmp_path / 'service', image, {'development': fixture_snapshot.database},
                     token='controlled', transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        first = service.run(task)
        assert first['outcome'] == 'budget_exhausted'
        assert first['model_calls'] == 1 and first['tokens'] > 2048
        assert service.report(task)['deterministic']
        assert first['attempts'][-1]['actual'] is None
        other = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        second = service.run(other)
        assert second['status'] == 'ended' and second['model_calls'] == 2
        assert len(sent) == 3


def test_model_budget_denial_does_not_send_and_is_queryable(tmp_path, fixture_snapshot, image):
    def provider(request):
        pytest.fail('budget must deny before sending')
    with TaskService(tmp_path / 'service', image, {'development': fixture_snapshot.database}, limits={'model': 1},
                     token='controlled', transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        result = service.run(task)
        assert result['outcome'] == 'budget_exhausted' and result['model_calls'] == 0
        assert service.report(task)['deterministic'] and not service.report(task)['validation']['passed']


def test_denied_sql_is_accounted_without_model_repair(tmp_path, fixture_snapshot, image):
    sent = []
    def provider(request):
        sent.append(request)
        return response({'sql': "SELECT * FROM read_csv('/secrets/task.sqlite')"})
    with TaskService(tmp_path / 'service', image, {'development': fixture_snapshot.database},
                     token='controlled', transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        result = service.run(task)
        assert result['outcome'] == 'refused'
        assert result['tool_calls'] == 4 and result['model_calls'] == 1
        assert result['query_result']['cleanup_verified']
        assert result['query_result']['status'] == 'policy_denied'
        assert result['attempts'][-1]['state'] == 'failed'
        assert len(sent) == 1


def test_wrong_report_number_is_removed_and_never_published(tmp_path, fixture_snapshot, image):
    sent = []
    def provider(request):
        sent.append(request)
        return response({'sql': SQL} if len(sent) == 1 else {'facts': [{'row': 0, 'column': 'users', 'value': -7}]})
    with TaskService(tmp_path / 'service', image, {'development': fixture_snapshot.database},
                     token='controlled', transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        service.run(task)
        report = service.report(task)
        assert report['facts'] == [] and not report['validation']['passed']
        assert report['rejected_facts'][0]['errors'] == ['value_mismatch']


def test_snapshot_default_window_is_mature_and_incomplete_range_is_disclosed(tmp_path, fixture_snapshot, image):
    with TaskService(tmp_path / 'service', image, {'development': fixture_snapshot.database},
                     token='controlled', limits={'model': 1}) as service:
        default = service.run(service.create('新增用户自然日次日留存', 'development'))
        assert default['actual_window'] == ['2026-01-09', '2026-01-16']
        limited = service.run(service.create('新增用户自然日次日留存', 'development', ('2026-01-10', '2026-01-20')))
        # F4 offers an explicit choice; rejecting preserves the F2 no-truncation contract.
        pending = limited['pending_question']
        limited = service.answer(limited['id'], pending['question_id'], pending['version'], '2')
        assert limited['actual_window'] is None
        assert limited['analysis_result'] == 'insufficient_evidence'
        assert 'requested_window_incomplete' in limited['limitations']


def test_nonfinite_query_evidence_is_rejected_without_breaking_service(tmp_path, fixture_snapshot, image):
    def provider(request):
        return response({'sql': 'SELECT 1.0/0 AS invalid_value'})
    with TaskService(tmp_path / 'service', image, {'development': fixture_snapshot.database},
                     token='controlled', transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        result = service.run(task)
        assert result['status'] == 'failed'
        assert result['evidence'] == []
        assert service.report(task)['deterministic']
        assert 'invalid_query_evidence' in result['limitations']


def test_late_provider_result_is_charged_but_cannot_continue(tmp_path, fixture_snapshot, image):
    import time
    sent = []
    def provider(request):
        sent.append(request)
        time.sleep(31)  # Actual external-boundary delay, not a fabricated clock.
        return response({'sql': SQL})
    with TaskService(tmp_path / 'service', image, {'development': fixture_snapshot.database},
                     token='controlled', limits={'active_seconds': 30}, transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        result = service.run(task)
        assert result['active'] >= 30
        assert result['model_calls'] == 1 and result['tokens'] == 48
        assert result['tool_calls'] == 3 and result['evidence'] == []
        assert result['outcome'] == 'budget_exhausted' and service.report(task)['deterministic']
        assert len(sent) == 1


def test_finished_report_survives_service_reopen(tmp_path, fixture_snapshot, image):
    root = tmp_path / 'service'
    with TaskService(root, image, {'development': fixture_snapshot.database}, token='controlled', limits={'model': 1}) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        result = service.run(task)
    with TaskService(root, image, {'development': fixture_snapshot.database}, token='controlled') as service:
        assert service.inspect(task) == result
        assert service.report(task)['outcome'] == 'budget_exhausted'
        with pytest.raises(ValueError, match='cannot run'):
            service.run(task)


def test_tool_budget_exhaustion_blocks_sql_and_model_dispatch(tmp_path, fixture_snapshot, image):
    sent = []
    def provider(request):
        sent.append(request)
        return response({'sql': SQL})
    with TaskService(tmp_path / 'service', image, {'development': fixture_snapshot.database},
                     token='controlled', limits={'tool': 2}, transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        result = service.run(task)
        assert result['tool_calls'] == 2 and result['model_calls'] == 0
        assert result['outcome'] == 'budget_exhausted'
        assert result['evidence'] == [] and service.report(task)['deterministic']
        assert sent == []
        assert len([item for item in result['attempts'] if item['kind'] == 'tool']) == 2


@pytest.mark.parametrize('actual_tokens', [30000, 30021])
def test_known_usage_overshoot_is_not_truncated_and_blocks_followup(tmp_path, fixture_snapshot, image, actual_tokens):
    sent = []
    def provider(request):
        sent.append(request)
        reply = response({'sql': SQL}).json()
        reply['usage'] = {'input_tokens': actual_tokens - 31, 'output_tokens': 31}
        return httpx.Response(200, json=reply)
    with TaskService(tmp_path / 'service', image, {'development': fixture_snapshot.database},
                     token='controlled', transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        result = service.run(task)
        assert result['tokens'] == actual_tokens
        assert result['model_calls'] == 1 and result['tool_calls'] == 3
        assert result['attempts'][-1]['actual'] == actual_tokens
        assert result['attempts'][-1]['reserved'] < 30000
        assert result['outcome'] == 'budget_exhausted'
        assert result['evidence'] == [] and service.report(task)['deterministic']
        assert len(sent) == 1
