"""Controlled browser clock/visibility, real HTTP and durable execution."""
import threading
import httpx2 as httpx
from playwright.sync_api import sync_playwright, expect

from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_t09_service import image, response
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser


VISIBILITY = """
window.testHidden=false;
Object.defineProperty(document,'hidden',{get:()=>window.testHidden});
Object.defineProperty(document,'visibilityState',{get:()=>window.testHidden?'hidden':'visible'});
"""


def visibility(page, hidden):
    page.evaluate("(hidden)=>{window.testHidden=hidden;document.dispatchEvent(new Event('visibilitychange'));}", hidden)


def test_running_reads_pause_in_background_and_reconcile_once_on_return(tmp_path, image):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=391001)
    entered = threading.Event(); release = threading.Event(); calls = []
    def provider(req):
        calls.append(req); entered.set(); assert release.wait(90)
        return response({'action':'stop','unsupported_hypotheses':[], 'unresolved_questions':[]})
    with TaskService(tmp_path/'state', image, {'dev':snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {'request_id':'visibility-running','question':'查询新增用户数',
                'snapshot_id':'dev','window':['2026-01-08','2026-01-15']})
            task = created['id']; browser = open_browser(pw)
            try:
                assert entered.wait(30)
                page = browser.new_page(); page.add_init_script(VISIBILITY)
                page.clock.install(time=0); page.clock.pause_at(1000)
                reads = []
                page.on('request',lambda req:reads.append(req) if req.url==app.origin+'/api/tasks/'+task else None)
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#current-action')).to_contain_text('请求模型')
                before = service.inspect(task)
                page.clock.run_for(999); assert len(reads) == 1
                with page.expect_response(app.origin+'/api/tasks/'+task):
                    page.clock.run_for(1)
                assert len(reads) == 2
                visibility(page, True); page.clock.run_for(15000)
                assert len(reads) == 2
                assert service.inspect(task) == before and len(calls) == 1
                with page.expect_response(app.origin+'/api/tasks/'+task):
                    visibility(page, False)
                assert len(reads) == 3
                # Let the HTTP body render before advancing the next controlled interval.
                page.wait_for_timeout(50)
                page.clock.run_for(999); assert len(reads) == 3
                with page.expect_response(app.origin+'/api/tasks/'+task):
                    page.clock.run_for(1)
                assert len(reads) == 4
                release.set(); assert wait_done(app, task)['status'] == 'ended'
                with page.expect_response(app.origin+'/api/tasks/'+task+'/report'):
                    page.clock.run_for(1000)
                expect(page.locator('#status')).to_have_text('已结束')
                expect(page.locator('#report-view')).to_contain_text('证据不足')
                final = service.inspect(task)
                count = len(reads); page.clock.run_for(30000)
                assert len(reads) == count
                assert service.inspect(task) == final and len(calls) == 1
            finally:
                release.set(); browser.close()


def test_report_failure_keeps_manual_recovery_and_late_report_cannot_replace_draft(tmp_path):
    snapshot = tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state', 'unused', {'dev':snapshot}, token='controlled', limits={'tool':1}) as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {'request_id':'terminal-report','question':'查询新增用户数',
                'snapshot_id':'dev','window':['2026-01-08','2026-01-15']})
            task = created['id']; assert wait_done(app, task)['status'] == 'ended'
            before = service.inspect(task)
            browser = open_browser(pw)
            try:
                page = browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
                page.add_init_script(VISIBILITY)
                reads = []; held = []
                page.on('request',lambda req:reads.append(req.url) if '/api/tasks/'+task in req.url else None)
                page.route('**/report',lambda route:route.abort())
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#report-view')).to_contain_text('报告读取失败')
                expect(page.locator('#connection')).to_contain_text('连接正常')
                assert len(reads) == 2
                page.clock.run_for(30000); assert len(reads) == 2
                visibility(page,True); visibility(page,False)
                page.clock.run_for(30000); assert len(reads) == 2
                page.unroute('**/report')
                page.get_by_role('button',name='刷新任务',exact=True).click()
                expect(page.locator('#report-view')).to_contain_text('预算限制')
                count = len(reads); page.clock.run_for(30000); assert len(reads) == count
                def hold(route):
                    held.append((route,route.fetch()))
                page.route('**/report',hold)
                page.get_by_role('button',name='刷新任务',exact=True).click()
                for _ in range(100):
                    if held: break
                    page.wait_for_timeout(20)
                assert len(held) == 1
                page.get_by_role('button',name='新建问题',exact=True).click()
                page.get_by_label('分析问题').fill('新任务草稿，不能被旧报告覆盖')
                route,result = held.pop(); route.fulfill(response=result)
                page.wait_for_timeout(50)
                expect(page.locator('#task')).to_be_hidden()
                expect(page.get_by_label('分析问题')).to_have_value('新任务草稿，不能被旧报告覆盖')
                page.reload()
                expect(page.get_by_label('分析问题')).to_have_value('新任务草稿，不能被旧报告覆盖')
                assert service.inspect(task) == before
            finally:
                browser.close()


def test_visibility_change_during_submit_does_not_discard_write_result(tmp_path):
    snapshot = tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            browser = open_browser(pw)
            try:
                page = browser.new_page(); page.add_init_script(VISIBILITY); held = []
                def hold(route):
                    if route.request.method == 'POST': held.append((route,route.fetch()))
                    else: route.continue_()
                page.route('**/api/tasks',hold)
                page.goto(app.origin)
                page.get_by_label('分析问题').fill('用户表现怎么样？')
                page.get_by_role('button',name='开始分析',exact=True).click()
                for _ in range(100):
                    if held: break
                    page.wait_for_timeout(20)
                assert len(held) == 1
                visibility(page, True); visibility(page, False)
                route,result=held.pop(); task=result.json()['id']; route.fulfill(response=result)
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                assert page.url.endswith(task)
                assert len(request(app, '/api/tasks')[1]['tasks']) == 1
                assert service.inspect(task)['tool_calls'] == 1
            finally:
                browser.close()
