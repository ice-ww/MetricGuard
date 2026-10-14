"""Comparison choices through public tasks and real isolated queries."""
from datetime import datetime, timezone
import pytest
from metricguard import TaskService
import duckdb
import httpx2 as httpx
from experiments.t01.snapshots import build_snapshot
from tests.test_t09_service import image, response


def test_date_conflict_precedes_baseline_confirmation(tmp_path):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'no queries before confirmation')
    with TaskService(tmp_path / 'state', 'unused', {'dev': snapshot}, token='controlled',
                     clock=lambda: datetime(2026, 1, 15, tzinfo=timezone.utc)) as service:
        state = service.run(service.create('昨天新增用户自然日次日留存下降，请分析', 'dev', ('2026-01-08', '2026-01-15'), mode='diagnose'))
        pending = state['pending_question']
        assert pending['reason'] == 'time_window_conflict'
        state = service.answer(state['id'], pending['question_id'], pending['version'], '2')
        assert state['pending_question']['reason'] == 'comparison_window_required'
        assert '2026-01-01' in state['pending_question']['prompt']
        assert '2026-01-08' in state['pending_question']['prompt']
        assert state['model_calls'] == 0


def test_modified_nonadjacent_baseline_matches_independent_counts(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A4', seed=2026101503)
    actions = iter([
        {'action': 'profile', 'table': 'users', 'column': 'registration_os', 'kind': 'system_retention'},
        {'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': []}])
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(lambda request: response(next(actions)))) as service:
        state = service.run(service.create('新增用户自然日次日留存变化，请分析', 'dev',
                            ('2026-01-08', '2026-01-15'), mode='diagnose'))
        pending = state['pending_question']
        state = service.answer(state['id'], pending['question_id'], pending['version'], '2026-01-01至2026-01-03')
    assert state['status'] == 'ended', state['limitations']
    assert state['report']['comparison_window'] == ['2026-01-01', '2026-01-04']
    with duckdb.connect(str(snapshot.database), read_only=True) as db:
        users = db.execute('SELECT user_id, registered_at, registration_os FROM users').fetchall()
        sessions = db.execute('SELECT user_id, started_at FROM sessions').fetchall()
    from datetime import timedelta
    local = timezone(timedelta(hours=8))
    active = {(uid, at.astimezone(local).date()) for uid, at in sessions}
    for row in state['evidence'][0]['rows']:
        start, end = ('2026-01-01', '2026-01-04') if row['period']=='previous' else ('2026-01-08', '2026-01-15')
        selected = [(uid, at.astimezone(local).date()) for uid, at, os in users
                    if start <= at.astimezone(local).date().isoformat() < end and os == row['registration_os']]
        retained = sum((uid, day + timedelta(days=1)) in active for uid, day in selected)
        assert (row['window_start'], row['window_end']) == (start, end)
        assert row['users'] == len(selected)
        assert row['retained'] == retained
        assert row['retention_rate'] == pytest.approx(retained / len(selected))
    previous_facts = [f for f in state['report']['facts'] if f['context']['comparison']=='previous']
    assert previous_facts and all(list(f['context']['window']) == ['2026-01-01', '2026-01-04'] for f in previous_facts)


@pytest.mark.parametrize('question,explicit,answer', [
    ('新增用户自然日次日留存变化', None, '1'),
    ('新增用户自然日次日留存变化，基期2026-01-01至2026-01-03', None, None),
    ('新增用户自然日次日留存变化', ('2026-01-01', '2026-01-04'), None),
    ('查询新增用户自然日次日留存', None, None),
])
def test_shared_preparation_preserves_default_explicit_and_simple_scope(tmp_path, image, question, explicit, answer):
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal', seed=2502)
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled') as service:
        task = service.prepare_shared(question, 'dev', ('2026-01-08', '2026-01-15'), comparison_window=explicit)
        state = service.inspect(task)
        if answer:
            pending = state['pending_question']
            state = service.answer(task, pending['question_id'], pending['version'], answer)
        assert state['status'] == 'ended', state['pending_question']
        assert state['model_calls'] == 0
        expected = ['2026-01-01', '2026-01-08'] if answer else ['2026-01-01', '2026-01-04'] if ('基期' in question or explicit) else None
        assert state['comparison_window'] == expected
        for mode in ('diagnose', 'baseline'):
            child = service.inspect(service.create_from_shared(task, mode=mode))
            assert child['comparison_window'] == expected


def test_incomplete_baseline_is_not_substituted(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal', seed=2503)
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled') as service:
        state = service.run(service.create('新增用户自然日次日留存变化', 'dev', ('2026-01-08', '2026-01-15'),
                            comparison_window=('2026-01-01', '2026-01-20'), mode='diagnose'))
    assert state['analysis_result'] == 'insufficient_evidence'
    assert state['comparison_window'] == ['2026-01-01', '2026-01-20']
    assert 'comparison_window_incomplete' in state['limitations']
    assert state['model_calls'] == 0 and not state['evidence']


@pytest.mark.parametrize('kind,column,baseline', [
    ('system_retention', 'registration_os', None),
    ('channel_health', 'channel', ('2026-01-01', '2026-01-04')),
])
def test_profile_cannot_invent_comparison_or_count_growth(tmp_path, image, kind, column, baseline):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A2', seed=2504)
    actions = iter([{'action': 'profile', 'table': 'users', 'column': column, 'kind': kind},
                    {'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': []}])
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(lambda request: response(next(actions)))) as service:
        state = service.run(service.create('新增用户自然日次日留存变化' if baseline else '查询新增用户自然日次日留存', 'dev', ('2026-01-08', '2026-01-15'),
                            comparison_window=baseline, mode='diagnose'))
    assert state['status'] == 'ended' and state['report']['facts'], state['limitations']
    if baseline is None:
        assert not state['answers']
        assert {r['period'] for r in state['evidence'][0]['rows']} == {'current'}
    else:
        diagnosis = state['report']['diagnosis']
        assert not diagnosis['candidates'] and not diagnosis['channel_metrics']
        assert diagnosis['missing_evidence'] == ['equal_duration_windows_required_for_count_growth']


def test_analysis_word_requires_confirmation_before_model(tmp_path):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'no query before confirmation')
    with TaskService(tmp_path / 'state', 'unused', {'dev': snapshot}, token='controlled') as service:
        state = service.run(service.create('请分析新增用户自然日次日留存', 'dev', ('2026-01-08', '2026-01-15'), mode='diagnose'))
    assert state['pending_question']['reason'] == 'comparison_window_required'
    assert state['model_calls'] == 0


def test_conflicting_explicit_baselines_require_a_choice(tmp_path):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'no query before confirmation')
    with TaskService(tmp_path / 'state', 'unused', {'dev': snapshot}, token='controlled') as service:
        state = service.run(service.create('新增用户自然日次日留存变化，基期2026-01-01至2026-01-03', 'dev',
                            ('2026-01-08', '2026-01-15'), comparison_window=('2026-01-01', '2026-01-08')))
        pending = state['pending_question']
        state = service.answer(state['id'], pending['question_id'], pending['version'], '确认')
    assert state['pending_question']['reason'] == 'comparison_window_conflict'
    assert len(state['pending_question']['options']) == 2
    assert state['model_calls'] == 0


def test_api_dates_have_one_canonical_representation(tmp_path):
    snapshot = tmp_path / 'snapshot'
    snapshot.write_bytes(b'create only')
    with TaskService(tmp_path / 'state', 'unused', {'dev': snapshot}, token='controlled') as service:
        state = service.inspect(service.create('新增用户数', 'dev', ('20260108', '20260115'),
                                comparison_window=('20260101', '20260104')))
    assert state['requested_window'] == ['2026-01-08', '2026-01-15']
    assert state['comparison_window'] == ['2026-01-01', '2026-01-04']


def test_nonadjacent_playback_baseline_preserves_instance_counts_and_context(tmp_path, image):
    from datetime import timedelta
    snapshot = build_snapshot(tmp_path / 'data', scenario='A3', seed=2505)
    actions = iter([
        {'action': 'profile', 'table': table, 'column': 'play_id', 'kind': kind}
        for table, kind in [('content_events', 'playback_events'), ('playback_telemetry', 'playback_progress')]
    ] + [{'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': []}])
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(lambda request: response(next(actions)))) as service:
        state = service.run(service.create('观测完播率变化', 'dev', ('2026-01-08', '2026-01-15'),
                            comparison_window=('2026-01-01', '2026-01-04'), mode='diagnose'))
        publication = service.publish_diagnosis(state['id'])
    assert state['outcome'] == 'facts_available', state['limitations']
    with duckdb.connect(str(snapshot.database), read_only=True) as db:
        events = db.execute('SELECT play_id, event_type, occurred_at FROM content_events').fetchall()
    first = {}
    for pid, event, at in events:
        if event == 'start':
            first[pid] = min(first.get(pid, at), at)
    days = {pid: at.astimezone(timezone(timedelta(hours=8))).date().isoformat() for pid, at in first.items()}
    for period, start, end in [('previous', '2026-01-01', '2026-01-04'), ('current', '2026-01-08', '2026-01-15')]:
        expected = sum(start <= day < end for day in days.values())
        assert sum(r['starts'] for r in state['evidence'][0]['rows'] if r['period'] == period) == expected
        facts = [a for a in publication['assertions'] if a['context']['comparison'] == period]
        assert facts and all(a['context']['window'] == [start, end] for a in facts)
