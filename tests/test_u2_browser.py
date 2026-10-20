"""Browser clarification, actual isolated queries and independent references."""
from datetime import datetime, timezone, timedelta
from pathlib import Path
import os
import json
import pytest
import duckdb
import httpx2 as httpx
from playwright.sync_api import sync_playwright, expect
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_t09_service import image, response


def save_record(name,state,**details):
    out=Path("artifacts/u2-browser");out.mkdir(exist_ok=True)
    (out/(name+".json")).write_text(json.dumps({"task":state,**details},ensure_ascii=False,indent=2),encoding="utf-8")


def open_browser(pw):
    return pw.chromium.launch(channel=os.environ.get('METRICGUARD_BROWSER_CHANNEL','msedge'),headless=True)


def submit_answer(page, text):
    page.get_by_label('你的回答').fill(text)
    page.get_by_role('button',name='提交回答',exact=True).click()


def test_continuous_clarification_keeps_task_and_confirmed_scope(tmp_path,image):
    snapshot=build_snapshot(tmp_path/'data',scenario='insufficient',seed=311001)
    actions=iter([{'action':'profile','table':'users','column':'registration_os','kind':'system_retention'},
                  {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]}])
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='controlled',
                     clock=lambda:datetime(2026,1,15,tzinfo=timezone.utc),transport=httpx.MockTransport(lambda req:response(next(actions)))) as service:
        with LocalWeb(service,example={'snapshot_id':'dev','question':'昨天用户表现有什么变化？','window':['2026-01-08','2026-01-15']}) as app:
            with sync_playwright() as pw:
                browser=open_browser(pw)
                try:
                    page=browser.new_page();page.goto(app.origin)
                    page.get_by_role('button',name='填入开发示例').click()
                    page.get_by_role('button',name='开始分析',exact=True).click()
                    expect(page.locator('#clarification-prompt')).to_contain_text('预设日期')
                    task=page.url.split('task=')[1];initial=service.inspect(task);anchor=initial['time_anchor']
                    assert initial['model_calls']==0 and not initial['evidence']
                    page.get_by_role('button',name='2026-01-08 至 2026-01-15（结束日不包含）',exact=True).click()
                    page.get_by_role('button',name='提交回答',exact=True).click()
                    expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                    submit_answer(page,'留存')
                    expect(page.locator('#clarification-prompt')).to_contain_text('留存人群')
                    waiting=service.inspect(task)
                    page.reload()
                    expect(page.locator('#known-information')).to_contain_text('留存')
                    expect(page.locator('#known-information')).to_contain_text('2026-01-08')
                    reloaded=service.inspect(task)
                    assert (reloaded['active'],reloaded['tool_calls'],reloaded['limits'])==(waiting['active'],waiting['tool_calls'],waiting['limits'])
                    page.get_by_role('button',name='新增用户',exact=True).click()
                    page.get_by_role('button',name='提交回答',exact=True).click()
                    expect(page.locator('#clarification-prompt')).to_contain_text('留存周期')
                    submit_answer(page,'自然日次日')
                    expect(page.locator('#clarification-prompt')).to_contain_text('比较基期')
                    submit_answer(page,'确认')
                    expect(page.locator('#clarification-prompt')).to_contain_text('未齐备')
                    before=service.inspect(task)
                    assert before['actual_window'] is None and before['model_calls']==0 and not before['evidence']
                    assert before['comparison_window']==['2026-01-01','2026-01-08']
                    assert before['time_anchor']==anchor and len(before['answers'])==5
                    assert 'question_id' not in page.locator('body').inner_text()
                    page.get_by_role('button',name='使用可用范围：2026-01-08 至 2026-01-11（结束日不包含）',exact=True).click()
                    page.get_by_role('button',name='提交回答',exact=True).dblclick()
                    expect(page.locator('#status')).to_have_text('已结束',timeout=60000)
                    expect(page.locator('#result')).to_contain_text('2026-01-11')
                    assert page.url.endswith(task)
                    state=service.inspect(task)
                    assert state['time_anchor']==anchor and len(state['answers'])==6
                    assert state['requested_window']==['2026-01-08','2026-01-15']
                    assert state['actual_window']==['2026-01-08','2026-01-11']
                    assert state['tool_calls']>=before['tool_calls']>=initial['tool_calls']
                    assert state['model_calls']==2 and state['limits']==initial['limits']
                    out=Path('artifacts/u2-browser');out.mkdir(exist_ok=True)
                    page.screenshot(path=str(out/'continuous.png'),full_page=True)
                finally:browser.close()
    with duckdb.connect(str(snapshot.database),read_only=True) as db:
        users=db.execute("SELECT user_id, CAST(timezone('Asia/Shanghai', registered_at) AS DATE), registration_os FROM users").fetchall()
        active=set(db.execute("SELECT DISTINCT user_id, CAST(timezone('Asia/Shanghai', started_at) AS DATE) FROM sessions").fetchall())
    reference=[]
    for row in state['evidence'][0]['rows']:
        start,end=('2026-01-01','2026-01-08') if row['period']=='previous' else ('2026-01-08','2026-01-11')
        group=[(uid,day) for uid,day,system in users if start<=str(day)<end and system==row['registration_os']]
        assert row['users']==len(group)
        assert row['retained']==sum((uid,day+timedelta(days=1)) in active for uid,day in group)
        assert (row['window_start'],row['window_end'])==(start,end)
        reference.append({'period':row['period'],'system':row['registration_os'],'window':[start,end],'users':len(group),'retained':sum((uid,day+timedelta(days=1)) in active for uid,day in group)})
    save_record('continuous',state,reference=reference,initial_limits=initial['limits'],before_query_calls=before['tool_calls'])


@pytest.mark.parametrize('case',['reject','unavailable','simple'])
def test_scope_outcomes_and_simple_query_without_baseline(tmp_path,image,case):
    snapshot=build_snapshot(tmp_path/'data',scenario='insufficient',seed=311003)
    actions=iter([{'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'},
                  {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]}])
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='controlled',
                     transport=httpx.MockTransport(lambda req:response(next(actions)))) as service:
        with LocalWeb(service,example={'snapshot_id':'dev','question':'用户表现怎么样？' if case=='simple' else '查询新增用户自然日次日留存',
                    'window':['2026-01-12' if case=='unavailable' else '2026-01-08','2026-01-15']}) as app:
            with sync_playwright() as pw:
                browser=open_browser(pw)
                try:
                    page=browser.new_page();page.goto(app.origin)
                    page.get_by_role('button',name='填入开发示例').click()
                    page.get_by_role('button',name='开始分析',exact=True).click()
                    page.wait_for_url('**/?task=*');task=page.url.split('task=')[1]
                    if case=='reject':
                        expect(page.locator('#clarification-prompt')).to_contain_text('未齐备',timeout=30000)
                        assert not service.inspect(task)['evidence']
                        page.get_by_role('button',name='保留原范围，返回不足说明',exact=True).click()
                        page.get_by_role('button',name='提交回答',exact=True).click()
                    elif case=='simple':
                        expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                        submit_answer(page,'新增用户数')
                    expect(page.locator('#status')).to_have_text('已结束',timeout=60000)
                    state=service.inspect(task)
                    assert state['comparison_window'] is None
                    expect(page.locator('#clarification')).to_be_hidden()
                    if case=='simple':
                        assert len(state['answers'])==1 and state['analysis_result']=='facts_available'
                        with duckdb.connect(str(snapshot.database),read_only=True) as db:
                            expected=db.execute("SELECT count(DISTINCT user_id) FROM users WHERE registered_at>=TIMESTAMPTZ '2026-01-08 00:00:00+08:00' AND registered_at<TIMESTAMPTZ '2026-01-15 00:00:00+08:00'").fetchone()[0]
                        expect(page.locator('#result')).to_contain_text(f'{expected} 人')
                    else:
                        assert state['analysis_result']=='insufficient_evidence' and state['model_calls']==0 and not state['evidence']
                        expect(page.locator('#result')).to_contain_text('会话数据')
                        if case=='unavailable':expect(page.locator('#result')).to_contain_text('无可用日期')
                        else:assert state['coverage']['decision']=='keep_original'
                    save_record(case,state)
                finally:browser.close()


def test_lost_answer_response_refreshes_latest_question_and_stale_tab_is_rejected(tmp_path):
    snapshot=tmp_path/'snapshot';snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app:
            with sync_playwright() as pw:
                browser=open_browser(pw)
                try:
                    page=browser.new_page();page.goto(app.origin)
                    page.get_by_label('分析问题').fill('用户表现怎么样？')
                    page.get_by_role('button',name='开始分析',exact=True).click()
                    expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                    url=page.url;task=url.split('task=')[1]
                    other=browser.new_page();other.clock.install(time=0);other.clock.pause_at(1000);other.goto(url)
                    expect(other.locator('#clarification-prompt')).to_contain_text('哪个指标')
                    def lose_response(route):
                        route.fetch();route.abort()
                    page.route('**/answers',lose_response)
                    submit_answer(page,'留存')
                    expect(page.locator('#clarification-prompt')).to_contain_text('留存人群')
                    expect(page.locator('#unknown-answer-text')).to_have_value('留存')
                    page.reload()
                    expect(page.locator('#clarification-prompt')).to_contain_text('留存人群')
                    submit_answer(other,'观测完播率')
                    expect(other.locator('#answer-error')).to_contain_text('已更新或已处理')
                    other.get_by_role('button',name='刷新待答问题',exact=True).click()
                    expect(other.locator('#clarification-prompt')).to_contain_text('留存人群')
                    assert len(service.inspect(task)['answers'])==1
                    assert service.inspect(task)['model_calls']==0
                finally:browser.close()
