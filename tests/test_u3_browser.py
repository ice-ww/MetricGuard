"""History navigation and controlled next-day restart at the browser boundary."""
from datetime import datetime,timezone,timedelta
from pathlib import Path
import json,threading
import duckdb
import httpx2 as httpx
from playwright.sync_api import sync_playwright,expect
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_t09_service import image,response
from tests.test_u2_browser import open_browser,submit_answer


def test_history_resumes_original_waiting_task_after_next_day_restart(tmp_path,image):
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=321101)
    calls=[];entered=threading.Event();release=threading.Event()
    actions=iter([{'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'},
                  {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]},
                  {'action':'profile','table':'users','column':'registration_os','kind':'system_retention'},
                  {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]}])
    def provider(req):
        calls.append(req)
        if len(calls)==3:entered.set();assert release.wait(30)
        return response(next(actions))
    with sync_playwright() as pw:
        with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='controlled',clock=lambda:datetime(2026,1,15,tzinfo=timezone.utc),transport=httpx.MockTransport(provider)) as service:
            with LocalWeb(service) as app:
                browser=open_browser(pw)
                try:
                    page=browser.new_page();page.goto(app.origin)
                    expect(page.locator('#history-message')).to_have_text('尚无历史任务。')
                    page.get_by_label('分析问题').fill('昨天用户表现怎么样？')
                    page.get_by_role('button',name='开始分析',exact=True).click()
                    expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                    task=page.url.split('task=')[1]
                    submit_answer(page,'留存')
                    expect(page.locator('#clarification-prompt')).to_contain_text('留存人群')
                    waiting=service.inspect(task)
                    assert waiting['requested_window']==['2026-01-14','2026-01-15']
                    page.get_by_role('button',name='新建问题',exact=True).click()
                    page.get_by_label('分析问题').fill('查询新增用户数')
                    page.get_by_label('开始日期（包含）',exact=True).fill('2026-01-08')
                    page.get_by_label('结束日期（不包含）',exact=True).fill('2026-01-15')
                    page.get_by_role('button',name='开始分析',exact=True).click()
                    expect(page.locator('#status')).to_have_text('已结束',timeout=60000)
                    expect(page.locator('#result')).to_contain_text('1680 人')
                    old_task=page.url.split('task=')[1];old_state=service.inspect(old_task)
                    # The text report is collapsed; innerText can be empty despite stored content.
                    old_body=page.locator('#result').text_content()
                    assert old_body
                    assert len(calls)==2
                finally:browser.close()
        with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='controlled',clock=lambda:datetime(2026,1,16,tzinfo=timezone.utc),transport=httpx.MockTransport(provider)) as service:
            with LocalWeb(service) as app:
                browser=open_browser(pw)
                try:
                    page=browser.new_page();page.goto(app.origin)
                    expect(page.locator('#history-list a')).to_have_count(2)
                    page.get_by_role('link',name='查询新增用户数',exact=True).click()
                    expect(page.locator('#result')).to_have_text(old_body)
                    assert service.inspect(old_task)==old_state and len(calls)==2
                    page.get_by_role('link',name='昨天用户表现怎么样？',exact=True).click()
                    expect(page.locator('#clarification-prompt')).to_contain_text('留存人群')
                    assert page.url.endswith(task) and service.inspect(task)==waiting
                    expect(page.locator('#known-information')).to_contain_text('2026-01-14')
                    submit_answer(page,'新增用户')
                    expect(page.locator('#clarification-prompt')).to_contain_text('留存周期')
                    submit_answer(page,'自然日次日')
                    assert entered.wait(20)
                    page.get_by_role('button',name='刷新列表',exact=True).click()
                    expect(page.locator('#history-list li').filter(has_text='昨天用户表现怎么样？')).to_contain_text('正在分析')
                    page.get_by_role('link',name='昨天用户表现怎么样？',exact=True).click()
                    expect(page.locator('#status')).to_have_text('正在分析')
                    release.set()
                    expect(page.locator('#status')).to_have_text('已结束',timeout=60000)
                    result=service.inspect(task)
                    assert result['actual_window']==['2026-01-14','2026-01-15']
                    assert result['time_anchor']==waiting['time_anchor'] and result['limits']==waiting['limits']
                    assert result['tool_calls']>waiting['tool_calls'] and result['answers'][0]==waiting['answers'][0]
                    assert len(calls)==4 and service.inspect(old_task)==old_state
                    page.reload();expect(page.locator('#status')).to_have_text('已结束')
                    assert len(calls)==4
                    out=Path('artifacts/u3-browser');out.mkdir(exist_ok=True)
                    page.screenshot(path=str(out/'history.png'),full_page=True)
                    page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                    page.screenshot(path=str(out/'mobile.png'),full_page=True)
                finally:release.set();browser.close()
    with duckdb.connect(str(snapshot.database),read_only=True) as db:
        users=db.execute("SELECT user_id,CAST(timezone('Asia/Shanghai',registered_at) AS DATE),registration_os FROM users").fetchall()
        active=set(db.execute("SELECT DISTINCT user_id,CAST(timezone('Asia/Shanghai',started_at) AS DATE) FROM sessions").fetchall())
    reference=[]
    for row in result['evidence'][0]['rows']:
        group=[(uid,day) for uid,day,system in users if str(day)=='2026-01-14' and system==row['registration_os']]
        retained=sum((uid,day+timedelta(days=1)) in active for uid,day in group)
        assert row['users']==len(group) and row['retained']==retained
        assert (row['window_start'],row['window_end'])==('2026-01-14','2026-01-15')
        reference.append({'system':row['registration_os'],'users':len(group),'retained':retained})
    (out/'record.json').write_text(json.dumps({'waiting':waiting,'result':result,'old_task':old_state,'reference':reference,'controlled_days':['2026-01-15','2026-01-16']},ensure_ascii=False,indent=2),encoding='utf-8')


def test_invalid_task_link_has_specific_feedback(tmp_path):
    snapshot=tmp_path/'snapshot';snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app:
            with sync_playwright() as pw:
                browser=open_browser(pw)
                try:
                    page=browser.new_page();page.goto(app.origin+'/?task=invalid')
                    expect(page.locator('#connection')).to_contain_text('找不到')
                    expect(page.locator('#status')).to_have_text('无法打开任务')
                    page.get_by_role('button',name='新建问题',exact=True).click()
                    expect(page.get_by_label('分析问题')).to_be_enabled()
                finally:browser.close()
