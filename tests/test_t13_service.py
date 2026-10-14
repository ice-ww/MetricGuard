"""Channel diagnosis through TaskService and real SQL worker."""
import duckdb
import httpx2 as httpx
import json
import pytest
from experiments.t01.references import python_metrics
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from tests.test_t09_service import image, response


def controlled(request):
    shared = json.loads(json.loads(request.content)['system'].split('Shared materials:\n')[1])
    if not shared['evidence']:
        return response({'action': 'profile', 'table': 'users', 'column': 'channel', 'kind': 'channel_health'})
    return response({'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': []})


def run(tmp_path, image, snapshot):
    with TaskService(tmp_path / 'service', image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(controlled)) as service:
        return service.run(service.create('新增用户自然日次日留存与渠道成本变化', 'dev', ('2026-01-08', '2026-01-15'), mode='diagnose', comparison_window=('2026-01-01', '2026-01-08')))


def test_channel_counts_costs_and_windows_match_independent_reference(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A2', seed=1313)
    expected = {period: python_metrics(snapshot.database, start, end)['channels'] for period, start, end in
                [('previous', '2026-01-01', '2026-01-08'), ('current', '2026-01-08', '2026-01-15')]}
    result = run(tmp_path, image, snapshot)
    assert result['outcome'] == 'facts_available', result['limitations']
    rows = result['evidence'][0]['rows']
    for period, reference in expected.items():
        for item in reference:
            actual = next(r for r in rows if r['period'] == period and r['channel'] == item['channel'])
            for key, value in item.items():
                assert actual[key] == value
    assert result['evidence'][0]['window'] == ['2026-01-01', '2026-01-15']
    assert result['report']['validation']['passed']
    assert result['report']['diagnosis']['rule_version'] == 'channel-growth-v1'


def test_low_retention_growth_preserves_actual_costs_and_controls(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A2', seed=1313, campaign_unit_cost=100)
    result = run(tmp_path, image, snapshot)
    diagnosis = result['report']['diagnosis']
    assert diagnosis['status'] == 'association_candidate'
    candidate = diagnosis['candidates'][0]
    assert candidate['group'] == {'channel': 'paid'}
    assert candidate['causality'] == 'not_established'
    assert candidate['supporting_facts'] and candidate['counterevidence']
    assert candidate['cost_per_new_change_cents'] == 0
    assert candidate['cost_per_retained_change_cents'] > 0
    assert diagnosis['statistical_limitations'] and diagnosis['unexcluded_factors']


def test_incomplete_spend_cannot_publish_costs_for_complete_user_window(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A2', seed=1313)
    with duckdb.connect(str(snapshot.database)) as con:
        con.execute("UPDATE source_watermarks SET complete_before='2026-01-10T00:00:00+08:00' WHERE source='channel_daily'")
    result = run(tmp_path, image, snapshot)
    assert result['outcome'] == 'insufficient_evidence'
    assert 'channel_daily_incomplete_for_channel_health' in result['limitations']
    assert not result['evidence']


@pytest.mark.parametrize('case', ['zero_growth', 'zero_retained', 'single_channel', 'missing_cost'])
def test_channel_edge_cases_do_not_invent_comparisons_or_costs(tmp_path, image, case):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A2', seed=1313, campaign_growth=1 if case == 'zero_growth' else 3)
    with duckdb.connect(str(snapshot.database)) as con:
        if case == 'zero_growth':
            con.execute("DELETE FROM users WHERE registered_at>='2026-01-08T00:00:00+08:00'")
            con.execute("INSERT INTO users SELECT user_id || '-current',registered_at + INTERVAL 7 DAY,registration_os,registration_version,channel FROM users WHERE registered_at<'2026-01-08T00:00:00+08:00'")
        if case == 'zero_retained':
            con.execute("DELETE FROM sessions WHERE user_id IN (SELECT user_id FROM users WHERE channel='paid') AND CAST(started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>=(SELECT CAST(registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)+1 FROM users WHERE users.user_id=sessions.user_id)")
        if case == 'single_channel':
            con.execute("DELETE FROM users WHERE channel!='paid'")
        if case == 'missing_cost':
            con.execute("DELETE FROM channel_daily WHERE channel='paid'")
    result = run(tmp_path, image, snapshot)
    diagnosis = result['report']['diagnosis']
    rows = result['evidence'][0]['rows']
    idle = next(r for r in rows if r['channel'] == 'idle')
    assert idle['cost_per_new_cents'] is None and idle['cost_per_retained_cents'] is None
    if case == 'zero_growth':
        assert all(m['growth_contribution'] is None for m in diagnosis['channel_metrics'])
        assert not diagnosis['candidates']
    if case == 'zero_retained':
        assert all(r['retained'] == 0 and r['cost_per_retained_cents'] is None for r in rows if r['channel'] == 'paid')
    if case == 'single_channel':
        assert diagnosis['status'] == 'insufficient_evidence'
        assert 'comparison_channels' in diagnosis['missing_evidence']
    if case == 'missing_cost':
        assert 'channel_spend:paid' in diagnosis['missing_evidence']
        assert all(r['cost_per_new_cents'] is None for r in rows if r['channel'] == 'paid')


def test_normal_channels_do_not_create_low_retention_growth_candidate(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal', seed=1313)
    result = run(tmp_path, image, snapshot)
    assert result['report']['diagnosis']['status'] == 'no_supported_candidate'
    assert not result['report']['diagnosis']['candidates']
