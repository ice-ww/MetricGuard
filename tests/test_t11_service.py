import json
import httpx2 as httpx
from tests.test_t09_service import fixture_snapshot, image, response
from metricguard import TaskService


def test_diagnosis_selects_next_query_from_actual_evidence(tmp_path, fixture_snapshot, image):
    observed = []
    def provider(request):
        payload = json.loads(request.content)
        shared = json.loads(payload['system'].split('Shared materials:\n')[1])
        if 'evidence' not in shared or not shared['evidence']:
            return response({'action': 'query', 'sql': 'SELECT COUNT(*) AS users FROM users'})
        evidence = shared['evidence']
        if len(evidence) == 1:
            count = evidence[0]['rows'][0]['users']
            observed.append(count)
            return response({'action': 'query', 'sql': 'SELECT COUNT(*) AS sessions FROM sessions' if count > 0 else 'SELECT COUNT(*) AS releases FROM release_calendar'})
        if 'last_failure' in shared:
            return response({'action': 'stop', 'unsupported_hypotheses': ['causality untested'], 'unresolved_questions': ['why users returned']})
        return response({'facts': [{'evidence_id': e['evidence_id'], 'row': 0, 'column': k, 'value': v} for e in evidence for k, v in e['rows'][0].items()]})
    with TaskService(tmp_path / 'service', image, {'dev': fixture_snapshot.database}, token='controlled', transport=httpx.MockTransport(provider)) as service:
        task = service.create('新增用户自然日次日留存', 'dev', mode='diagnose')
        result = service.run(task)
        assert result['status'] == 'ended', result['limitations']
        assert observed and observed[0] > 0
        assert len(result['evidence']) == 2
        assert result['report']['validation']['valid_count'] == 2
        assert result['report']['unsupported_hypotheses'] == ['causality untested']
        assert result['tool_calls'] == 5 and result['model_calls'] == 4
        assert service.inspect(service.rerun(task))['mode'] == 'diagnose'


def test_repair_limit_is_global_across_successful_queries(tmp_path, fixture_snapshot, image):
    actions = iter([
        {'action': 'query', 'sql': 'SELECT registration_os, COUNT(*) AS users FROM users'},
        {'action': 'query', 'sql': 'SELECT COUNT(*) AS users FROM users'},
        {'action': 'query', 'sql': 'SELECT channel, COUNT(*) AS users FROM users'},
        {'action': 'query', 'sql': 'SELECT COUNT(*) AS sessions FROM sessions'},
        {'action': 'query', 'sql': 'SELECT version, COUNT(*) AS sessions FROM sessions'},
    ])
    with TaskService(tmp_path / 'service', image, {'dev': fixture_snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(lambda request: response(next(actions)))) as service:
        result = service.run(service.create('新增用户自然日次日留存', 'dev', mode='diagnose'))
        assert result['outcome'] == 'insufficient_evidence', result['limitations']
        assert result['repairs_used'] == 2
        assert result['model_calls'] == 5 and result['tool_calls'] == 8
        assert result['report']['deterministic'] and result['report']['validation']['valid_count'] == 2
        failures = [e for e in result['trace'] if e['event'] == 'query_failed']
        assert len(failures) == 3
        assert all(a['state'] in ('completed', 'failed') for a in result['attempts'])


def test_profiles_expose_windowed_distribution_missing_and_time_coverage(tmp_path, fixture_snapshot, image):
    actions = iter([
        {'action': 'profile', 'table': 'users', 'column': 'channel', 'kind': 'distribution'},
        {'action': 'profile', 'table': 'users', 'column': 'channel', 'kind': 'missing'},
        {'action': 'profile', 'table': 'users', 'column': 'registered_at', 'kind': 'time_coverage'},
    ])
    def provider(request):
        shared = json.loads(json.loads(request.content)['system'].split('Shared materials:\n')[1])
        if len(shared['evidence']) < 3:
            return response(next(actions))
        # Missing usage stops conservatively with all three actual evidence results.
        return response({'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': []}, usage=False)
    with TaskService(tmp_path / 'service', image, {'dev': fixture_snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        result = service.run(service.create('新增用户自然日次日留存', 'dev', ('2026-01-01', '2026-01-08'), mode='diagnose'))
        assert result['outcome'] == 'budget_exhausted', result['limitations']
        evidence = result['evidence']
        assert len(evidence) == 3
        assert evidence[1]['rows'] == [{'total_rows': 1656, 'missing_rows': 0}]
        assert sum(row['count'] for row in evidence[0]['rows']) == 1656
        assert evidence[2]['rows'][0]['observed_rows'] == 1656
        assert result['report']['validation']['passed']
        assert len({f['evidence_id'] for f in result['report']['facts']}) == 3


def test_security_stop_retains_prior_facts_without_repair(tmp_path, fixture_snapshot, image):
    actions = iter([{'action': 'query', 'sql': 'SELECT COUNT(*) AS users FROM users'},
                    {'action': 'query', 'sql': "SELECT * FROM read_csv('/etc/passwd')"}])
    with TaskService(tmp_path / 'service', image, {'dev': fixture_snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(lambda request: response(next(actions)))) as service:
        result = service.run(service.create('新增用户自然日次日留存', 'dev', mode='diagnose'))
        assert result['outcome'] == 'refused'
        assert result['repairs_used'] == 0 and result['model_calls'] == 2
        assert result['report']['validation']['valid_count'] == 1
        assert result['query_result']['cleanup_verified']


def test_report_rejects_cross_evidence_value_and_unknown_reference(tmp_path, fixture_snapshot, image):
    def provider(request):
        shared = json.loads(json.loads(request.content)['system'].split('Shared materials:\n')[1])
        evidence = shared['evidence']
        if not evidence:
            return response({'action': 'query', 'sql': 'SELECT 7 AS observed'})
        if len(evidence) == 1:
            return response({'action': 'query', 'sql': 'SELECT 9 AS observed'})
        if 'last_failure' in shared:
            return response({'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': []})
        return response({'facts': [
            {'evidence_id': evidence[0]['evidence_id'], 'row': 0, 'column': 'observed', 'value': 9},
            {'evidence_id': 'invented', 'row': 0, 'column': 'observed', 'value': 7},
            {'evidence_id': evidence[1]['evidence_id'], 'row': 0, 'column': 'observed', 'value': 9}]})
    with TaskService(tmp_path / 'service', image, {'dev': fixture_snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        result = service.run(service.create('新增用户自然日次日留存', 'dev', mode='diagnose'))
        report = result['report']
        assert len(report['facts']) == 1 and report['facts'][0]['value'] == 9
        assert len(report['rejected_facts']) == 2
        assert report['rejected_facts'][0]['errors'] == ['value_mismatch']
        assert report['rejected_facts'][1]['error'] == 'unknown_evidence_id'


def test_invalid_profile_parameters_stop_before_query(tmp_path, fixture_snapshot, image):
    with TaskService(tmp_path / 'service', image, {'dev': fixture_snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(lambda request: response({'action': 'profile', 'table': 'users', 'column': 'channel', 'kind': 'distribution', 'limit': 999999}))) as service:
        result = service.run(service.create('新增用户自然日次日留存', 'dev', mode='diagnose'))
        assert result['status'] == 'failed'
        assert result['tool_calls'] == 3 and result['model_calls'] == 1
        assert not result['evidence']
        assert any(e['event'] == 'execution_stopped' for e in result['trace'])


def test_budget_stop_preserves_unresolved_question(tmp_path, fixture_snapshot, image):
    with TaskService(tmp_path / 'service', image, {'dev': fixture_snapshot.database}, token='controlled', limits={'model': 1}) as service:
        result = service.run(service.create('新增用户自然日次日留存', 'dev', mode='diagnose'))
        assert result['outcome'] == 'budget_exhausted'
        assert result['report']['unresolved_questions']
        assert any('新增用户自然日次日留存' in q for q in result['report']['unresolved_questions'])


def test_repeated_successful_query_stops_without_new_tool_attempt(tmp_path, fixture_snapshot, image):
    def provider(request):
        return response({'action': 'query', 'sql': 'SELECT 7 AS observed'})
    with TaskService(tmp_path / 'service', image, {'dev': fixture_snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        result = service.run(service.create('新增用户自然日次日留存', 'dev', mode='diagnose'))
        assert result['tool_calls'] == 4
        assert result['model_calls'] == 2
        assert result['report']['deterministic']
        assert result['report']['facts'][0]['value'] == 7
        assert result['report']['unresolved_questions']
        assert 'no_new_evidence' in result['limitations']
        assert any(e['event'] == 'diagnosis_no_progress' for e in result['trace'])


def test_next_plan_receives_actual_action_and_result_history(tmp_path, fixture_snapshot, image):
    requests = []
    first = {'action': 'query', 'sql': 'SELECT 7 AS observed'}
    def provider(request):
        payload = json.loads(request.content)
        requests.append(payload)
        if len(requests) == 1:
            return response(first)
        return response({'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': ['Explanation untested']}, usage=False)
    with TaskService(tmp_path / 'service', image, {'dev': fixture_snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        result = service.run(service.create('新增用户自然日次日留存', 'dev', mode='diagnose'))
        messages = requests[1]['messages']
        assert len(messages) == 3
        assert messages[1]['role'] == 'assistant' and json.loads(messages[1]['content']) == first
        actual_result = json.loads(messages[2]['content'])
        assert actual_result['status'] == 'ok'
        assert actual_result['evidence_id'] == result['evidence'][0]['evidence_id']
        assert result['diagnostic_history'][0]['action'] == first
        assert result['diagnostic_history'][0]['result'] == actual_result
