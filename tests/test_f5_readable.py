"""Human-visible report and terminal behavior at the approved public seams."""
import json
import pytest
from pathlib import Path
import duckdb
import httpx2 as httpx
from metricguard import TaskService
from metricguard.console import interact
from experiments.t01.snapshots import build_snapshot
from tests.test_t09_service import image, response


def test_simple_query_terminal_and_saved_report_show_verified_number(tmp_path, image, capsys):
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal', seed=2701)
    actions = iter([{'action': 'profile', 'table': 'users', 'column': 'user_id', 'kind': 'new_user_counts'},
                    {'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': []}])
    with duckdb.connect(str(snapshot.database), read_only=True) as db:
        expected = db.execute("SELECT COUNT(DISTINCT user_id) FROM users WHERE registered_at >= TIMESTAMPTZ '2026-01-08 00:00:00+08:00' AND registered_at < TIMESTAMPTZ '2026-01-15 00:00:00+08:00'").fetchone()[0]
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(lambda request: response(next(actions)))) as service:
        state = service.run(service.create('查询新增用户数', 'dev', ('2026-01-08', '2026-01-15'), mode='diagnose'))
        before = state['model_calls']
        exported = service.export_report(state['id'])
        interact(service, state)
        after = service.inspect(state['id'])
    body = exported['body']
    assert f'新增用户数：{expected} 人' in body
    assert '[A0]' in body and '2026-01-08' in body and '2026-01-15' in body
    saved = Path(exported['report']).read_text(encoding='utf-8')
    terminal = capsys.readouterr().out
    assert '(#fact-' not in terminal and '# 分析报告' not in terminal
    assert body in saved and exported['terminal_body'] in terminal
    assert '查询事实' in terminal
    assert '完整事实表' in saved and 'evidence.json' in saved
    evidence = json.loads(Path(exported['evidence']).read_text(encoding='utf-8'))
    assert evidence[0]['rows'][0]['users'] == expected
    assert after['model_calls'] == before


def test_system_diagnosis_body_contains_values_controls_and_resolvable_references(tmp_path, image, capsys):
    from datetime import timedelta, timezone
    from tests.test_t15_service import controlled
    snapshot = build_snapshot(tmp_path / 'data', scenario='A4', seed=2702)
    with TaskService(tmp_path / 'state', image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(controlled())) as service:
        state = service.run(service.create('新增用户自然日次日留存变化，请分析系统结构', 'dev', ('2026-01-08', '2026-01-15'),
                            comparison_window=('2026-01-01', '2026-01-08'), mode='diagnose'))
        exported = service.export_report(state['id'])
        interact(service, state)
    body = exported['body']
    assert all(term in body for term in ('支持依据', '反对证据', '未排除因素', '未证明因果', 'Android', 'iOS'))
    assert 'Android' in body.splitlines()[0]
    assert '## 关键比较' in body and '百分点' in body
    assert '基期 → 本期' in body
    with duckdb.connect(str(snapshot.database), read_only=True) as db:
        users = db.execute('SELECT user_id, registered_at, registration_os FROM users').fetchall()
        sessions = db.execute('SELECT user_id, started_at FROM sessions').fetchall()
    local = timezone(timedelta(hours=8))
    active = {(uid, at.astimezone(local).date()) for uid, at in sessions}
    for start,end in [('2026-01-01','2026-01-08'),('2026-01-08','2026-01-15')]:
        for system in ('Android', 'iOS'):
            group = [(uid, at.astimezone(local).date()) for uid,at,os in users if start <= at.astimezone(local).date().isoformat() < end and os == system]
            retained = sum((uid,day+timedelta(days=1)) in active for uid,day in group)
            assert f'{retained/len(group)*100:.3f}%' in body
    directory = Path(exported['report']).parent
    publication = json.loads((directory/'publication.json').read_text(encoding='utf-8'))
    sources = {e['evidence_id']:e for e in json.loads((directory/'evidence.json').read_text(encoding='utf-8'))}
    for assertion in publication['assertions']:
        ref=assertion['reference']
        assert sources[ref['evidence_id']]['rows'][ref['row']][ref['column']] == assertion['value']
    assert exported['terminal_body'] in capsys.readouterr().out


@pytest.mark.parametrize('scenario', ['A1','A2','A3'])
def test_other_diagnoses_show_named_evidence_and_keep_technical_fields_in_archive(tmp_path, image, scenario):
    from tests.test_t12_service import controlled as version_transport
    from tests.test_t13_service import controlled as channel_provider
    from tests.test_t14_service import controlled as playback_provider
    snapshot = build_snapshot(tmp_path / 'data', scenario=scenario, seed=2703)
    transport = version_transport(['cohort_health','crash_versions','releases']) if scenario == 'A1' else httpx.MockTransport(channel_provider if scenario == 'A2' else playback_provider)
    question = {'A1':'新增用户自然日次日留存变化，请检验版本崩溃解释', 'A2':'新增用户自然日次日留存与渠道成本变化', 'A3':'观测完播率变化，请检验采集解释'}[scenario]
    with TaskService(tmp_path / 'state', image, {'dev':snapshot.database}, token='controlled', transport=transport) as service:
        state = service.run(service.create(question,'dev',('2026-01-08','2026-01-15'),comparison_window=('2026-01-01','2026-01-08'),mode='diagnose'))
        before = state['model_calls']
        exported = service.export_report(state['id'])
        assert service.inspect(state['id'])['model_calls'] == before
    body = exported['body']
    assert '支持依据' in body and '反对证据' in body and '未排除因素' in body
    assert '[A' in body and '未证明因果关系' in body
    if scenario == 'A3':
        from experiments.t14.reference import reference
        expected = reference(snapshot.database, '2026-01-08','2026-01-15')
        assert 'invalid_alignment' not in body
        assert '同分群采集对照' in body
        assert body.index('支持完成事件采集缺失候选') < body.index('## 同期与口径对照') < body.index('## 关键比较')
        for row in expected['rows']:
            assert row['os'] in body and row['version'] in body
            assert f"观测完播率：{row['observed_completed']/row['starts']*100:.3f}%" in body
            assert f"独立进度完整播放比例：{row['independent_complete']/row['starts']*100:.3f}%" in body
    else:
        from experiments.t01.references import python_metrics
        expected = python_metrics(snapshot.database,'2026-01-08','2026-01-15')
        if scenario == 'A2':
            archived = json.loads(Path(exported['evidence']).read_text(encoding='utf-8'))
            idle = next(r for e in archived if e['parameters'].get('kind')=='channel_health' for r in e['rows'] if r['channel']=='idle')
            assert idle['users']==0 and idle['retention_rate'] is None
            published = json.loads((Path(exported['report']).parent/'publication.json').read_text(encoding='utf-8'))
            assert not any(a['context']['group'].get('channel')=='idle' and a['context']['metric']=='retention_rate' for a in published['assertions'])
            for row in expected['channels']:
                if not row['users']:
                    continue  # Main comparison concerns active acquisition; zero-population rows remain in the appendix.
                assert any(row['channel'] in line and '新增用户数' in line and f"{row['users']} 人" in line for line in body.splitlines())
        else:
            rows = [r for r in expected['retention'] if r['os']=='Android' and r['version']=='2.0']
            users=sum(r['users'] for r in rows); retained=sum(r['retained'] for r in rows)
            assert 'Android' in body and '版本 2.0' in body
            assert '同期对照' in body and '版本 2.0' in body.splitlines()[0]
            assert body.index('支持版本崩溃与留存下降相关的候选解释') < body.index('## 同期与口径对照') < body.index('## 关键比较')
            assert f'新增用户数：{users} 人' in body and f'次日留存率：{retained/users*100:.3f}%' in body


def test_narrowed_channel_report_explains_noncomparable_lengths(tmp_path, image):
    from tests.test_t13_service import controlled
    snapshot = build_snapshot(tmp_path / 'data', scenario='insufficient', seed=2704)
    with TaskService(tmp_path / 'state', image, {'dev':snapshot.database}, token='controlled', transport=httpx.MockTransport(controlled)) as service:
        state=service.run(service.create('新增用户自然日次日留存与渠道成本变化','dev',('2026-01-08','2026-01-15'),comparison_window=('2026-01-01','2026-01-08'),mode='diagnose'))
        pending=state['pending_question']
        state=service.answer(state['id'],pending['question_id'],pending['version'],'1')
        exported=service.export_report(state['id'])
    body=exported['body']
    assert '原请求范围' in body and '用户确认范围' in body and '不能推广' in body
    assert '基期 7 天、本期 3 天' in body and '不能直接比较新增人数的增长' in body
    assert 'equal_duration_windows_required_for_count_growth' not in body
    assert body.startswith('# 证据不足，暂无法判断')
    assert '## 候选解释' not in body
    assert '比率仍需核对人群构成和观测条件' in body
    assert body.count('基期 7 天、本期 3 天') == 1
    assert state['report']['facts'] and not state['report']['diagnosis']['candidates']


def test_rejected_model_number_never_enters_readable_report(tmp_path, image):
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=2705)
    calls=[]
    def provider(request):
        calls.append(request)
        return response({'sql':'SELECT COUNT(*) AS users FROM users'} if len(calls)==1 else {'facts':[{'row':0,'column':'users','value':-987654321}]})
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='controlled',transport=httpx.MockTransport(provider)) as service:
        state=service.run(service.create('查询新增用户数','dev',('2026-01-08','2026-01-15')))
        exported=service.export_report(state['id'])
    assert '-987654321' not in exported['body']
    assert '暂无通过引用校验的事实' in exported['body']
    assert not state['report']['facts']


def test_unverified_stop_question_stays_in_audit_only(tmp_path, image):
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=2706)
    unverified='Android 2.0 于 2099-12-31 发布，因此留存下降是否由发布造成？'
    actions=iter([{'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'},
                  {'action':'stop','unsupported_hypotheses':[], 'unresolved_questions':[unverified]}])
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='controlled',
                     transport=httpx.MockTransport(lambda request:response(next(actions)))) as service:
        state=service.run(service.create('查询新增用户数','dev',('2026-01-08','2026-01-15'),mode='diagnose'))
        exported=service.export_report(state['id'])
    assert unverified in state['unresolved_questions']
    assert unverified not in exported['body']
    assert unverified not in Path(exported['report']).read_text(encoding='utf-8')
    assert unverified in (Path(exported['report']).parent/'task.json').read_text(encoding='utf-8')


@pytest.mark.parametrize('budget_stop', [False, True])
def test_user_claim_is_not_repeated_as_stop_explanation(tmp_path, image, budget_stop):
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=2707)
    question='查询新增用户数，已知Android有987654321人'
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='controlled',
                     limits={'model':1} if budget_stop else None,
                     transport=httpx.MockTransport(lambda request:response({'action':'query','sql':'SELECT 7 AS observed'}))) as service:
        state=service.run(service.create(question,'dev',('2026-01-08','2026-01-15'),mode='diagnose'))
        exported=service.export_report(state['id'])
    assert '987654321' not in exported['body']
    assert any(question in line for line in state['report']['unresolved_questions'])
