"""Public diagnosis seam: real SQL worker, controlled provider, independent oracle."""
from collections import defaultdict
import json
import pytest
import duckdb

import httpx2 as httpx
from experiments.t01.references import python_metrics
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from tests.test_t09_service import image, response


def profile(kind):
    table, column = {'cohort_health': ('users', 'registration_version'),
                     'crash_versions': ('sessions', 'version'),
                     'releases': ('release_calendar', 'version')}[kind]
    return {'action': 'profile', 'table': table, 'column': column, 'kind': kind}


def controlled(kinds):
    def provider(request):
        shared = json.loads(json.loads(request.content)['system'].split('Shared materials:\n')[1])
        evidence = shared['evidence']
        if 'last_failure' in shared:
            if len(evidence) < len(kinds):
                return response(profile(kinds[len(evidence)]))
            return response({'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': []})
        return response({'facts': [{'evidence_id': e['evidence_id'], 'row': i, 'column': k, 'value': v}
                                  for e in evidence for i, row in enumerate(e['rows'])
                                  for k, v in row.items() if type(v) in (int, float)]})
    return httpx.MockTransport(provider)


def test_mature_cohort_health_matches_independent_membership_counts(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A1', seed=1212)
    expected = {}
    for period, start, end in [('previous', '2026-01-01', '2026-01-08'), ('current', '2026-01-08', '2026-01-15')]:
        groups = defaultdict(lambda: [0, 0, 0])
        for row in python_metrics(snapshot.database, start, end)['retention']:
            counts = groups[(row['os'], row['version'])]
            for i, name in enumerate(('users', 'retained', 'crashed_users')):
                counts[i] += row[name]
        expected.update({(period, *key): value for key, value in groups.items()})
    with TaskService(tmp_path / 'service', image, {'dev': snapshot.database}, token='controlled',
                     transport=controlled(['cohort_health'])) as service:
        result = service.run(service.create('新增用户自然日次日留存下降原因', 'dev', ('2026-01-08', '2026-01-15'), mode='diagnose'))
    assert result['outcome'] == 'facts_available', result['limitations']
    rows = result['evidence'][0]['rows']
    assert {(r['period'], r['registration_os'], r['registration_version']):
            [r['users'], r['retained'], r['crashed_users']] for r in rows} == expected
    for row in rows:
        assert row['retention_rate'] == row['retained'] / row['users']
        assert row['crash_rate'] == row['crashed_users'] / row['users']
    assert result['evidence'][0]['window'] == ['2026-01-01', '2026-01-15']
    assert all(f['context']['window'] == ['2026-01-01', '2026-01-08']
               for f in result['report']['facts'] if f['context']['comparison'] == 'previous')


@pytest.mark.parametrize('scenario,expected_status', [('A1', 'association_candidate'), ('normal', 'no_supported_candidate')])
def test_version_association_requires_concordant_evidence_and_retains_controls(tmp_path, image, scenario, expected_status):
    snapshot = build_snapshot(tmp_path / 'data', scenario=scenario, seed=1212)
    with TaskService(tmp_path / 'service', image, {'dev': snapshot.database}, token='controlled',
                     transport=controlled(['releases', 'cohort_health', 'crash_versions'])) as service:
        task = service.create('新增用户自然日次日留存下降原因', 'dev', ('2026-01-08', '2026-01-15'), mode='diagnose')
        result = service.run(task)
        publication = service.publish_diagnosis(task)
    assert publication['status'] == 'mechanically_valid'
    # Numeric publication references cannot support a release-date assertion.
    assert all('发布时间与当前窗口重合' not in inference['text'] for inference in publication['inferences'])
    assert result['outcome'] == 'facts_available', result['limitations']
    diagnosis = result['report']['diagnosis']
    assert diagnosis['status'] == expected_status
    assert diagnosis['unexcluded_factors'] and diagnosis['statistical_limitations']
    if scenario == 'A1':
        candidate = diagnosis['candidates'][0]
        assert candidate['group'] == {'registration_os': 'Android', 'registration_version': '2.0'}
        assert candidate['release_date'] == '2026-01-08'
        assert candidate['supporting_facts'] and candidate['counterevidence']
        assert candidate['causality'] == 'not_established'
        assert {c['group']['registration_os'] for c in candidate['controls']} == {'Android', 'iOS'}
        assert candidate['comparisons'][0]['difference_interval_pp'] is None


def test_mismatching_actual_crash_version_is_not_attributed_to_registration_version(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A1', seed=1212)
    with duckdb.connect(str(snapshot.database)) as con:
        con.execute("UPDATE sessions SET version='different-runtime' WHERE crashed AND version='2.0'")
    with TaskService(tmp_path / 'service', image, {'dev': snapshot.database}, token='controlled',
                     transport=controlled(['crash_versions', 'cohort_health', 'releases'])) as service:
        result = service.run(service.create('新增用户自然日次日留存下降原因', 'dev', ('2026-01-08', '2026-01-15'), mode='diagnose'))
    assert result['report']['diagnosis']['status'] == 'insufficient_evidence'
    assert 'actual_crash_registration_mismatch' in result['report']['diagnosis']['missing_evidence']
    assert not result['report']['diagnosis']['candidates']
    crash_rows = result['evidence'][0]['rows']
    assert any(r['registration_version'] == '2.0' and r['actual_version'] == 'different-runtime' for r in crash_rows)


def test_partial_profiles_publish_facts_without_claiming_explanation(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A1', seed=1212)
    with TaskService(tmp_path / 'service', image, {'dev': snapshot.database}, token='controlled',
                     transport=controlled(['cohort_health'])) as service:
        result = service.run(service.create('新增用户自然日次日留存下降原因', 'dev', ('2026-01-08', '2026-01-15'), mode='diagnose'))
    assert result['report']['validation']['passed']
    assert result['report']['diagnosis']['status'] == 'insufficient_evidence'
    assert result['report']['diagnosis']['missing_evidence'] == ['crash_versions', 'releases']


@pytest.mark.parametrize('missing', ['current_other_version', 'current_other_system', 'unique_matching_release', 'no_same_system_controls'])
def test_missing_required_controls_or_release_remains_unassessed(tmp_path, image, missing):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A1', seed=1212)
    mutations = {
        'current_other_version': "DELETE FROM users WHERE registration_os='Android' AND registration_version='1.0' AND registered_at>='2026-01-08T00:00:00+08:00'",
        'current_other_system': "DELETE FROM users WHERE registration_os='iOS'",
        'unique_matching_release': "DELETE FROM release_calendar WHERE version='2.0'",
        'no_same_system_controls': "DELETE FROM users WHERE registration_os='Android' AND registration_version='1.0'"}
    with duckdb.connect(str(snapshot.database)) as con:
        con.execute(mutations[missing])
    with TaskService(tmp_path / 'service', image, {'dev': snapshot.database}, token='controlled',
                     transport=controlled(['cohort_health', 'releases', 'crash_versions'])) as service:
        result = service.run(service.create('新增用户自然日次日留存下降原因', 'dev', ('2026-01-08', '2026-01-15'), mode='diagnose'))
    assert result['report']['diagnosis']['status'] == 'insufficient_evidence'
    if missing == 'no_same_system_controls':
        assert {'previous_same_system', 'current_other_version'} <= set(result['report']['diagnosis']['missing_evidence'])
    else:
        assert missing in result['report']['diagnosis']['missing_evidence']
    assert not result['report']['diagnosis']['candidates']
