"""Coverage authorization through the public service, using actual snapshots."""
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from tests.test_t09_service import image


def test_partial_d1_requires_authorization_and_rejection_keeps_original(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='insufficient', seed=2601)
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled') as service:
        state = service.run(service.create('查询新增用户自然日次日留存', 'dev', ('2026-01-08', '2026-01-15')))
        assert state['status'] == 'waiting'
        pending = state['pending_question']
        assert pending['reason'] == 'coverage_scope_required'
        assert len(pending['options']) == 2
        assert state['actual_window'] is None
        assert state['model_calls'] == 0 and not state['evidence']
        coverage = state['coverage']
        assert coverage['available_window'] == ['2026-01-08', '2026-01-11']
        assert coverage['missing_window'] == ['2026-01-11', '2026-01-15']
        assert 'D+1' in pending['prompt'] and '2026-01-16' in pending['prompt']
        state = service.answer(state['id'], pending['question_id'], pending['version'], '2')
        assert state['status'] == 'ended'
        assert state['analysis_result'] == 'insufficient_evidence'
        assert state['requested_window'] == ['2026-01-08', '2026-01-15']
        assert not state['evidence'] and state['model_calls'] == 0
        assert state['report']['coverage']['decision'] == 'keep_original'


def test_authorized_scope_survives_restart_and_matches_independent_d1(tmp_path, image):
    import duckdb
    import httpx2 as httpx
    from datetime import timedelta
    from tests.test_t09_service import response
    snapshot = build_snapshot(tmp_path / 'data', scenario='insufficient', seed=2602)
    root = tmp_path / 'state'
    with TaskService(root, image, {'dev': snapshot.database}, token='controlled') as service:
        state = service.run(service.create('查询新增用户自然日次日留存', 'dev', ('2026-01-08', '2026-01-15'), mode='diagnose'))
    actions = iter([{'action': 'profile', 'table': 'users', 'column': 'registration_os', 'kind': 'system_retention'},
                    {'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': []}])
    with TaskService(root, image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(lambda request: response(next(actions)))) as service:
        pending = state['pending_question']
        state = service.answer(state['id'], pending['question_id'], pending['version'], '1')
        assert state['status'] == 'ended', state['limitations']
        assert state['actual_window'] == ['2026-01-08', '2026-01-11']
        assert state['requested_window'] == ['2026-01-08', '2026-01-15']
        assert state['report']['coverage']['authorization']['question_id'] == pending['question_id']
        assert '不能推广' in state['report']['scope_statement']
        assert state['report']['facts']
        publication = service.publish_diagnosis(state['id'])
        assert publication['scope_statement'] == state['report']['scope_statement']
        assert publication['coverage'] == state['coverage']
    with duckdb.connect(str(snapshot.database), read_only=True) as db:
        users = db.execute("SELECT user_id, CAST(timezone('Asia/Shanghai', registered_at) AS DATE), registration_os FROM users").fetchall()
        active = set(db.execute("SELECT DISTINCT user_id, CAST(timezone('Asia/Shanghai', started_at) AS DATE) FROM sessions").fetchall())
    for row in state['evidence'][0]['rows']:
        group = [(uid, day) for uid, day, os in users if '2026-01-08' <= str(day) < '2026-01-11' and os == row['registration_os']]
        assert row['users'] == len(group)
        assert row['retained'] == sum((uid, day + timedelta(days=1)) in active for uid, day in group)
        assert (row['window_start'], row['window_end']) == ('2026-01-08', '2026-01-11')


def test_free_date_selection_and_shared_scope_preserve_original(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='insufficient', seed=2603)
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled') as service:
        task = service.prepare_shared('新增用户自然日次日留存变化', 'dev', ('2026-01-08', '2026-01-15'))
        state = service.inspect(task)
        pending = state['pending_question']
        assert pending['reason'] == 'comparison_window_required'
        state = service.answer(task, pending['question_id'], pending['version'], '1')
        pending = state['pending_question']
        assert pending['reason'] == 'coverage_scope_required'
        state = service.answer(task, pending['question_id'], pending['version'], '仅使用2026-01-09至2026-01-10')
        assert state['status'] == 'ended'
        assert state['actual_window'] == ['2026-01-09', '2026-01-11']
        assert state['comparison_window'] == ['2026-01-01', '2026-01-08']
        child = service.inspect(service.create_from_shared(task, mode='diagnose'))
        assert child['coverage'] == state['coverage']
        assert child['coverage']['requested_window'] == ['2026-01-08', '2026-01-15']


def test_no_available_dates_explains_missing_source_without_options(tmp_path, image, capsys):
    from metricguard.console import interact
    snapshot = build_snapshot(tmp_path / 'data', scenario='insufficient', seed=2604)
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled') as service:
        state = service.run(service.create('查询新增用户自然日次日留存', 'dev', ('2026-01-12', '2026-01-15')))
        assert state['status'] == 'ended' and state['pending_question'] is None
        assert state['coverage']['available_window'] is None
        assert state['actual_window'] is None and not state['evidence']
        interact(service, state)
    output = capsys.readouterr().out
    assert '无可用日期' in output and '会话数据' in output
    assert '2026-01-16' in output and '不是预计更新时间' in output
    assert '请选择编号' not in output
    assert '自由输入上述可用范围' not in output


def test_console_rejects_scope_without_internal_payload(tmp_path, image, monkeypatch, capsys):
    from metricguard.console import interact
    snapshot = build_snapshot(tmp_path / 'data', scenario='insufficient', seed=2605)
    monkeypatch.setattr('builtins.input', lambda prompt: '保留原范围')
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled') as service:
        state = service.run(service.create('查询新增用户自然日次日留存', 'dev', ('2026-01-08', '2026-01-15')))
        interact(service, state)
        assert service.inspect(state['id'])['coverage']['decision'] == 'keep_original'
    output = capsys.readouterr().out
    assert '使用可用范围' in output and '保留原范围' in output
    assert '未齐备的指标日期' in output and 'D+1' in output
    assert 'question_id' not in output and 'coverage_scope_required' not in output


def test_incomplete_baseline_discloses_its_own_required_dates(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal', seed=2606)
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled') as service:
        state = service.run(service.create('新增用户自然日次日留存变化', 'dev', ('2026-01-08', '2026-01-15'),
                            comparison_window=('2026-01-01', '2026-01-20'), mode='diagnose'))
    assert state['status'] == 'ended' and state['analysis_result'] == 'insufficient_evidence'
    assert state['comparison_window'] == ['2026-01-01', '2026-01-20']
    assert state['report']['comparison_coverage']['missing_window'] == ['2026-01-16', '2026-01-20']
    assert any('2026-01-21' in line and '基期' in line for line in state['report']['unresolved_questions'])
    assert not state['evidence'] and state['model_calls'] == 0


def test_refusal_containing_dates_cannot_authorize_narrowing(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='insufficient', seed=2607)
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled') as service:
        state = service.run(service.create('查询新增用户自然日次日留存', 'dev', ('2026-01-08', '2026-01-15')))
        pending = state['pending_question']
        state = service.answer(state['id'], pending['question_id'], pending['version'], '不要缩小到2026-01-09至2026-01-10，保留原范围')
    assert state['coverage']['decision'] == 'keep_original'
    assert state['actual_window'] is None and not state['evidence']
    assert state['model_calls'] == 0


def test_acceptance_followed_by_budget_exhaustion_still_returns_scoped_report(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='insufficient', seed=2608)
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled', limits={'tool': 3}) as service:
        state = service.run(service.create('查询新增用户自然日次日留存', 'dev', ('2026-01-08', '2026-01-15')))
        pending = state['pending_question']
        state = service.answer(state['id'], pending['question_id'], pending['version'], '1')
    assert state['analysis_result'] == 'budget_exhausted'
    assert state['actual_window'] is None and not state['evidence']
    assert '2026-01-11' in state['report']['scope_statement']


def test_failed_shared_preparation_without_coverage_still_reports(tmp_path):
    snapshot = tmp_path / 'data'
    snapshot.write_bytes(b'no sandbox dispatch')
    with TaskService(tmp_path / 'state', 'mutable-image-tag', {'dev': snapshot}, token='unused') as service:
        task = service.prepare_shared('查询新增用户数', 'dev', ('2026-01-08', '2026-01-15'))
        child = service.run(service.create_from_shared(task, mode='diagnose'))
        assert child['analysis_result'] == 'insufficient_evidence'
        assert child['report']['coverage'] is None
        assert not child['evidence']


def test_mentioned_dates_without_a_choice_remain_pending(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='insufficient', seed=2609)
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled') as service:
        state = service.run(service.create('查询新增用户自然日次日留存', 'dev', ('2026-01-08', '2026-01-15')))
        pending = state['pending_question']
        state = service.answer(state['id'], pending['question_id'], pending['version'], '2026-01-09至2026-01-10只是举例')
        assert state['status'] == 'waiting'
        assert 'decision' not in state['coverage']
        assert state['actual_window'] is None and state['model_calls'] == 0
