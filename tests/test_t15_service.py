"""System composition through public TaskService and actual isolated SQL."""
import json
import duckdb
import httpx2 as httpx
import pytest
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from tests.test_t09_service import image, response


def controlled():
    actions = iter([{'action': 'profile', 'table': 'users', 'column': 'registration_os', 'kind': 'system_retention'},
                    {'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': []}])
    return lambda request: response(next(actions))


def run(tmp_path, image, snapshot):
    with TaskService(tmp_path / 'service', image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(controlled())) as service:
        return service.run(service.create('新增用户自然日次日留存，分析系统占比变化', 'dev',
                                         ('2026-01-08', '2026-01-15'), mode='diagnose'))


def test_system_composition_decomposition_matches_raw_reference(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A4', seed=1501)
    result = run(tmp_path, image, snapshot)
    assert result['outcome'] == 'facts_available', result['limitations']
    from experiments.t15.reference import reference
    expected = reference(snapshot.database, '2026-01-08', '2026-01-15')
    diagnosis = result['report']['diagnosis']
    assert result['evidence'][0]['rows'] == expected['rows']
    for key in ('actual_retention', 'standardized_retention', 'within_effect_pp', 'composition_effect_pp', 'total_change_pp'):
        assert diagnosis[key] == pytest.approx(expected[key])
    assert diagnosis['status'] == 'association_candidate'
    assert diagnosis['candidates'][0]['supporting_facts']
    assert diagnosis['difference_interval_pp'] is None
    assert result['report']['validation']['passed']


@pytest.mark.parametrize('case', ['missing_system', 'unknown_system', 'empty_previous', 'immature', 'normal'])
def test_composition_limits_preserve_known_facts(tmp_path, image, case):
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal' if case=='normal' else 'A4', seed=1501)
    with duckdb.connect(str(snapshot.database)) as con:
        if case == 'missing_system':
            con.execute("DELETE FROM users WHERE registration_os='Android' AND registered_at>='2026-01-08T00:00:00+08:00'")
        elif case == 'unknown_system':
            con.execute("UPDATE users SET registration_os=NULL WHERE registration_os='Android'")
        elif case == 'empty_previous':
            con.execute("DELETE FROM users WHERE registered_at<'2026-01-08T00:00:00+08:00'")
        elif case == 'immature':
            con.execute("UPDATE source_watermarks SET complete_before='2026-01-12T00:00:00+08:00' WHERE source='sessions'")
    result = run(tmp_path, image, snapshot)
    diagnosis = result['report']['diagnosis']
    assert result['report']['facts']
    if case in ('missing_system', 'unknown_system', 'empty_previous'):
        assert diagnosis['status'] == 'insufficient_evidence'
        assert diagnosis['standardized_retention'] is None
        assert diagnosis['missing_evidence']
    elif case == 'normal':
        assert diagnosis['status'] == 'no_supported_candidate'
        assert not diagnosis['candidates']
    else:
        assert result['actual_window'] == ['2026-01-08', '2026-01-11']
        assert 'requested_window_shortened_to_complete_sources' in result['limitations']
        assert all(row['window_end'] <= '2026-01-11' for row in result['evidence'][0]['rows'])


def test_counts_pool_users_instead_of_averaging_daily_rates(tmp_path, image):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=1510)
    with duckdb.connect(str(snapshot.database)) as con:
        con.execute('DELETE FROM users')
        con.execute('DELETE FROM sessions')
        # Each period: one fully retained user on day 1, nine unretained on day 2.
        for first in (1,8):
            for i in range(10):
                day = first if i==0 else first+1
                uid=f'{first}-{i}'
                con.execute("INSERT INTO users VALUES (?, ?, 'Android','1.0','organic')",[uid,f'2026-01-{day:02d}T08:00:00+08:00'])
                if i==0:
                    for repeat in range(2):
                        con.execute("INSERT INTO sessions VALUES (?, ?, ?, 'Android','9.0',FALSE)",
                                    [uid+str(repeat),uid,f'2026-01-{day+1:02d}T08:00:00+08:00'])
    result=run(tmp_path,image,snapshot)
    diagnosis=result['report']['diagnosis']
    assert diagnosis['actual_retention'] == {'previous': .1, 'current': .1}
    assert diagnosis['standardized_retention'] == .1
    assert diagnosis['sample_sufficiency'] == 'not_established_for_population_inference'
    assert diagnosis['evidence_scope'] == 'observed_snapshot_descriptive_only'
    assert diagnosis['system_metrics'][0]['users']=={'previous':10,'current':10}
    assert all(row['users']==10 and row['retained']==1 for row in result['evidence'][0]['rows'])


def test_truncated_systems_cannot_support_population_shares(tmp_path, image):
    snapshot = build_snapshot(tmp_path/'data', scenario='A4', seed=1511)
    with duckdb.connect(str(snapshot.database)) as con:
        con.execute('UPDATE users SET registration_os=user_id')
    result = run(tmp_path,image,snapshot)
    assert result['evidence'][0]['truncated']
    diagnosis = result['report']['diagnosis']
    assert diagnosis['status']=='insufficient_evidence'
    assert diagnosis['standardized_retention'] is None
    assert not diagnosis['system_metrics'] and not diagnosis['candidates']
    assert 'complete_system_profile' in diagnosis['missing_evidence']
