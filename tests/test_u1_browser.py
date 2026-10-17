"""Real browser -> local HTTP -> TaskService -> isolated query worker."""
from pathlib import Path
import os
import threading
import duckdb
import httpx2 as httpx
from playwright.sync_api import sync_playwright, expect
from metricguard import TaskService
from metricguard.web import LocalWeb
from experiments.t01.snapshots import build_snapshot
from tests.test_t09_service import image, response


def test_browser_query_survives_page_close_and_reopen(tmp_path, image):
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=301101)
    with duckdb.connect(str(snapshot.database),read_only=True) as db:
        expected=db.execute("SELECT count(DISTINCT user_id) FROM users WHERE registered_at>=TIMESTAMPTZ '2026-01-08 00:00:00+08:00' AND registered_at<TIMESTAMPTZ '2026-01-15 00:00:00+08:00'").fetchone()[0]
    entered=threading.Event();release=threading.Event();calls=[]
    def provider(req):
        calls.append(req)
        if len(calls)==1:
            entered.set()
            assert release.wait(30)
            return response({'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'})
        return response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]})
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='browser-private-token',transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service,example={'snapshot_id':'dev','question':'查询新增用户数','window':['2026-01-08','2026-01-15']}) as app:
            with sync_playwright() as pw:
                browser=pw.chromium.launch(channel=os.environ.get('METRICGUARD_BROWSER_CHANNEL','msedge'),headless=True)
                try:
                    page=browser.new_page(viewport={'width':1360,'height':900})
                    errors=[];page.on('pageerror',lambda error:errors.append(str(error)))
                    page.goto(app.origin)
                    page.get_by_role('button',name='填入开发示例').click()
                    expect(page.get_by_label('开始日期（包含）',exact=True)).to_have_value('2026-01-08')
                    question='查询新增用户数 <img src=x onerror="window.injected=1">'
                    page.get_by_label('分析问题').fill(question)
                    page.get_by_role('button',name='开始分析',exact=True).dblclick()
                    page.wait_for_url('**/?task=*')
                    url=page.url;task=url.split('task=')[1]
                    assert entered.wait(20)
                    expect(page.locator('#status')).to_have_text('正在分析')
                    assert page.locator('img').count()==0
                    assert page.evaluate('window.injected') is None
                    page.close()
                    release.set()
                    page=browser.new_page(viewport={'width':1360,'height':900})
                    page.goto(url)
                    expect(page.locator('#result')).to_contain_text(f'新增用户数：{expected} 人',timeout=60000)
                    expect(page.locator('#status')).to_have_text('已结束')
                    page.reload()
                    expect(page.get_by_label('分析问题')).to_have_value(question)
                    expect(page.get_by_label('开始日期（包含）',exact=True)).to_have_value('2026-01-08')
                    expect(page.locator('#result')).to_contain_text(f'{expected} 人')
                    assert len(calls)==2
                    assert service.inspect(task)['model_calls']==2
                    assert 'browser-private-token' not in page.content()
                    assert not errors
                    output=Path('artifacts/u1-browser');output.mkdir(parents=True,exist_ok=True)
                    page.screenshot(path=str(output/'desktop.png'),full_page=True)
                    page.set_viewport_size({'width':390,'height':844})
                    page.screenshot(path=str(output/'mobile.png'),full_page=True)
                    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
                finally:
                    release.set()
                    browser.close()


def test_old_status_response_cannot_overwrite_new_question(tmp_path):
    snapshot=tmp_path/'dummy.duckdb';snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app:
            with sync_playwright() as pw:
                browser=pw.chromium.launch(channel=os.environ.get('METRICGUARD_BROWSER_CHANNEL','msedge'),headless=True)
                page=browser.new_page();held=[]
                def hold(route):
                    held.append((route,route.fetch()))
                page.route('**/api/tasks/*',hold)
                try:
                    page.goto(app.origin)
                    page.get_by_label('分析问题').fill('用户表现怎么样？')
                    page.get_by_role('button',name='开始分析',exact=True).click()
                    page.wait_for_url('**/?task=*')
                    for _ in range(50):
                        if held:break
                        page.wait_for_timeout(100)
                    assert held
                    page.get_by_role('button',name='新建问题',exact=True).click()
                    page.get_by_label('分析问题').fill('这是正在编辑的新问题')
                    route,response=held.pop();route.fulfill(response=response)
                    page.wait_for_timeout(300)
                    expect(page.get_by_label('分析问题')).to_have_value('这是正在编辑的新问题')
                    expect(page.locator('#status')).to_have_text('尚未开始')
                finally:browser.close()
