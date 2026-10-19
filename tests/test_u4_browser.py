"""Published facts are navigable through the real browser/service/query boundary."""
from pathlib import Path
import json
import duckdb
import httpx2 as httpx
from playwright.sync_api import sync_playwright, expect
from metricguard import TaskService
from metricguard.web import LocalWeb
from experiments.t01.snapshots import build_snapshot
from tests.test_t09_service import image, response
from tests.test_u2_browser import open_browser
from tests.test_u1_web import request


def test_query_reference_opens_exact_fact_and_evidence_without_execution(tmp_path,image):
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=331101)
    with duckdb.connect(str(snapshot.database),read_only=True) as db:
        expected=db.execute("SELECT count(DISTINCT user_id) FROM users WHERE registered_at>=TIMESTAMPTZ '2026-01-08 00:00:00+08:00' AND registered_at<TIMESTAMPTZ '2026-01-15 00:00:00+08:00'").fetchone()[0]
    poison='<img src=x onerror="window.injected=1">'
    with duckdb.connect(str(snapshot.database)) as db:
        db.execute('UPDATE users SET channel=?',[poison])
    actions=iter([{'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'}, {'action':'profile','table':'users','column':'channel','kind':'distribution'}, {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]}])
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='private-u4',transport=httpx.MockTransport(lambda req:response(next(actions)))) as service:
        with LocalWeb(service) as app:
            with sync_playwright() as pw:
                browser=open_browser(pw)
                try:
                    page=browser.new_page();page.goto(app.origin)
                    page.get_by_label('分析问题').fill('查询新增用户数 <img src=x onerror="window.injected=1">')
                    page.get_by_label('开始日期（包含）',exact=True).fill('2026-01-08')
                    page.get_by_label('结束日期（不包含）',exact=True).fill('2026-01-15')
                    page.get_by_role('button',name='开始分析',exact=True).click()
                    expect(page.locator('#status')).to_have_text('已结束',timeout=60000)
                    task=page.url.split('task=')[1];before=service.inspect(task)
                    expect(page.locator('#report-view')).to_contain_text(f'新增用户数：{expected} 人')
                    assert not page.locator('#facts-details').evaluate('(e)=>e.open')
                    page.locator('#report-view a').filter(has_text='A0').first.click()
                    expect(page.locator('#fact-0')).to_be_focused()
                    expect(page.locator('#fact-0')).to_contain_text(f'{expected} 人')
                    page.locator('#fact-0 a').click()
                    expect(page.locator('.evidence-cell:focus')).to_contain_text(str(expected))
                    code,report=request(app,f'/api/tasks/{task}/report')
                    assert code==200 and report['available']
                    ref=report['facts'][0]['reference']
                    assert page.locator('.evidence-cell:focus').get_attribute('data-column')==ref['column']
                    assert page.locator('.evidence-cell:focus').get_attribute('data-row')==str(ref['row'])
                    assert service.inspect(task)==before
                    assert 'private-u4' not in page.content() and page.locator('img').count()==0
                    assert page.evaluate('window.injected') is None
                    assert json.dumps(poison) in page.locator('#evidence-details').text_content()
                    page.get_by_text('执行记录',exact=True).click()
                    expect(page.locator('#trace-details')).to_contain_text('report_published')
                    out=Path('artifacts/u4-browser');out.mkdir(exist_ok=True)
                    (out/'query.json').write_text(json.dumps({'task':task,'reference':expected,'report':report},ensure_ascii=False,indent=2),encoding='utf-8')
                finally:browser.close()

from datetime import timedelta
import pytest


@pytest.mark.parametrize('case',['candidate','normal','insufficient'])
def test_diagnosis_comparisons_and_scope_remain_visible(tmp_path,image,case):
    snapshot=build_snapshot(tmp_path/'data',scenario={'candidate':'A4','normal':'normal','insufficient':'insufficient'}[case],seed=331102)
    actions=iter(([{'action':'profile','table':'content_events','column':'play_id','kind':'playback_events'},
                   {'action':'profile','table':'playback_telemetry','column':'play_id','kind':'playback_progress'}] if case=='normal' else
                  [{'action':'profile','table':'users','column':'registration_os','kind':'system_retention'}])+
                 [{'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]}])
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='controlled',transport=httpx.MockTransport(lambda req:response(next(actions)))) as service:
        with LocalWeb(service,example={'snapshot_id':'dev','question':'分析观测完播率变化' if case=='normal' else '分析新增用户自然日次日留存变化','window':['2026-01-08','2026-01-15'],'comparison_window':['2026-01-01','2026-01-08']}) as app:
            with sync_playwright() as pw:
                browser=open_browser(pw)
                try:
                    page=browser.new_page(viewport={'width':1360,'height':1000});page.goto(app.origin)
                    page.get_by_role('button',name='填入开发示例').click();page.get_by_role('button',name='开始分析',exact=True).click()
                    if case=='insufficient':
                        expect(page.locator('#clarification-prompt')).to_contain_text('未齐备',timeout=30000)
                        page.get_by_role('button',name='使用可用范围：2026-01-08 至 2026-01-11（结束日不包含）',exact=True).click()
                        page.get_by_role('button',name='提交回答',exact=True).click()
                    expect(page.locator('#status')).to_have_text('已结束',timeout=60000)
                    expect(page.locator('#report-kind')).to_have_text({'candidate':'描述性候选，未证明因果','normal':'未形成支持充分的异常候选','insufficient':'证据不足，暂无法判断'}[case])
                    task=page.url.split('task=')[1];state=service.inspect(task)
                    report=request(app,f'/api/tasks/{task}/report')[1]
                    expect(page.locator('.report-scope')).to_contain_text('2026-01-15')
                    expect(page.locator('#report-overview')).to_contain_text('基期')
                    if case=='insufficient':
                        expect(page.locator('.report-scope')).to_contain_text('2026-01-11')
                        expect(page.locator('#report-overview')).to_contain_text('不能推广至原请求范围')
                        expect(page.locator('#report-overview')).to_contain_text('不能直接比较')
                    if case=='candidate':
                        expect(page.locator('#report-overview')).to_contain_text('个百分点')
                        expect(page.get_by_role('heading',name='未排除因素：')).to_be_visible()
                        for label in ['支持依据','反对证据与对照']:
                            detail=page.locator('#report-overview details').filter(has=page.get_by_text(label,exact=True)).first
                            assert not detail.evaluate('(e)=>e.open')
                            detail.locator('summary').click();detail.locator('a').first.click()
                            expect(page.locator('.fact-row:focus')).to_be_visible()
                    # Every published cell is reached from a real fact link and retains the exact raw value.
                    page.locator('#facts-details summary').click() if not page.locator('#facts-details').evaluate('(e)=>e.open') else None
                    for fact in report['facts']:
                        ref=fact['reference'];page.locator('[id="fact-'+fact['assertion_id']+'"] a').click()
                        cell=page.locator('.evidence-cell:focus')
                        expect(cell).to_have_text(json.dumps(fact['value'],ensure_ascii=False,separators=(',',':')))
                    assert service.inspect(task)==state
                    if case!='normal':
                        with duckdb.connect(str(snapshot.database),read_only=True) as db:
                            users=db.execute("SELECT user_id,CAST(timezone('Asia/Shanghai',registered_at) AS DATE),registration_os FROM users").fetchall()
                            active=set(db.execute("SELECT DISTINCT user_id,CAST(timezone('Asia/Shanghai',started_at) AS DATE) FROM sessions").fetchall())
                        reference=[]
                        for row in state['evidence'][0]['rows']:
                            group=[(uid,day) for uid,day,system in users if row['window_start']<=str(day)<row['window_end'] and system==row['registration_os']]
                            retained=sum((uid,day+timedelta(days=1)) in active for uid,day in group)
                            assert (row['users'],row['retained'])==(len(group),retained)
                            assert abs(row['retention_rate']-retained/len(group))<1e-12
                            reference.append({'period':row['period'],'system':row['registration_os'],'users':len(group),'retained':retained})
                    else:reference=[]
                    page.reload();expect(page.locator('#report-kind')).to_be_visible()
                    out=Path('artifacts/u4-browser');out.mkdir(exist_ok=True)
                    page.screenshot(path=str(out/(case+'.png')),full_page=True)
                    page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                    page.screenshot(path=str(out/(case+'-mobile.png')),full_page=True)
                    (out/(case+'.json')).write_text(json.dumps({'task':state,'report':report,'reference':reference},ensure_ascii=False,indent=2),encoding='utf-8')
                finally:browser.close()


def test_raw_evidence_keeps_integer_beyond_javascript_precision(tmp_path,image):
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=331104)
    actions=iter([{'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'},
                  {'action':'query','sql':'SELECT 9007199254740993 AS exact_integer FROM users LIMIT 1'},
                  {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]}])
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='controlled',transport=httpx.MockTransport(lambda req:response(next(actions)))) as service:
        with LocalWeb(service,example={'snapshot_id':'dev','question':'查询新增用户数','window':['2026-01-08','2026-01-15']}) as app:
            with sync_playwright() as pw:
                browser=open_browser(pw)
                try:
                    page=browser.new_page();page.goto(app.origin)
                    page.get_by_role('button',name='填入开发示例').click();page.get_by_role('button',name='开始分析',exact=True).click()
                    expect(page.locator('#status')).to_have_text('已结束',timeout=60000)
                    expect(page.locator('#report-kind')).to_be_visible()
                    page.locator('#facts-details summary').click()
                    fact=page.locator('.fact-row').filter(has_text='9007199254740993')
                    expect(fact).to_have_count(1);fact.locator('a').click()
                    expect(page.locator('.evidence-cell:focus')).to_have_text('9007199254740993')
                finally:browser.close()
