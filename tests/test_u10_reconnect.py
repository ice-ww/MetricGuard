"""Bounded read recovery at the browser -> HTTP -> durable service seam."""
from playwright.sync_api import sync_playwright, expect
import pytest

from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser
from tests.test_u9_lifecycle import VISIBILITY, visibility


def test_new_draft_cannot_bypass_unconfirmed_initial_task(tmp_path):
    snapshot=tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _,created=request(app,'/api/tasks',{'request_id':'initial-read','question':'用户表现怎么样？','snapshot_id':'dev'})
            task=created['id']; wait_done(app,task); before=service.inspect(task)
            browser=open_browser(pw)
            try:
                page=browser.new_page(); held=[]
                page.route('**/api/tasks/'+task,lambda route:held.append(route))
                page.goto(app.origin+'/?task='+task)
                page.get_by_role('button',name='新建问题',exact=True).click()
                page.get_by_label('分析问题').fill('尚未确认原任务时的新草稿')
                expect(page.get_by_role('button',name='开始分析',exact=True)).to_be_disabled()
                page.locator('#analysis-form').evaluate('form=>form.requestSubmit()')
                assert len(request(app,'/api/tasks')[1]['tasks'])==1
                page.unroute('**/api/tasks/'+task)
                page.get_by_role('button',name='立即重连',exact=True).click()
                expect(page.locator('#connection')).to_contain_text('连接正常')
                expect(page.get_by_label('分析问题')).to_have_value('尚未确认原任务时的新草稿')
                expect(page.get_by_role('button',name='开始分析',exact=True)).to_be_enabled()
                assert service.inspect(task)==before
            finally:
                browser.close()


@pytest.mark.parametrize('status,message,code',[
    (403,'请求来源不受允许。',None),
    (404,'此任务不属于当前界面工作目录。',None),
    (403,'页面会话已失效，请重新连接。','session_expired'),
])
def test_explicit_rejection_stops_recovery_without_refreshing_session(tmp_path,status,message,code):
    snapshot=tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _,created=request(app,'/api/tasks',{'request_id':'denied-recovery','question':'用户表现怎么样？','snapshot_id':'dev'})
            task=created['id']; wait_done(app,task); before=service.inspect(task)
            browser=open_browser(pw)
            try:
                page=browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#status')).to_have_text('等待澄清')
                page.get_by_label('你的回答').fill('明确拒绝后也应保留的旧内容')
                reads=[]
                page.on('request',lambda req:reads.append(req.url) if req.url.endswith(('/api/config','/api/tasks/'+task)) else None)
                page.route('**/api/tasks/'+task,lambda route:route.fulfill(status=status,json={'error':message,'code':code}))
                page.get_by_role('button',name='刷新任务',exact=True).click()
                expect(page.locator('#connection')).to_contain_text(message)
                expect(page.get_by_label('你的回答')).to_be_visible()
                expect(page.get_by_label('你的回答')).to_have_value('明确拒绝后也应保留的旧内容')
                page.clock.run_for(130000)
                assert reads==[app.origin+'/api/tasks/'+task]+([app.origin+'/api/config'] if code else [])
                expect(page.get_by_role('button',name='立即重连',exact=True)).to_be_visible()
                assert service.inspect(task)==before
            finally:
                browser.close()


def test_state_timeout_preserves_draft_and_recovers_without_execution(tmp_path):
    snapshot = tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state', 'unused', {'dev':snapshot}, token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {'request_id':'timeout-recovery','question':'用户表现怎么样？','snapshot_id':'dev'})
            task=created['id']; wait_done(app,task); before=service.inspect(task)
            browser=open_browser(pw)
            try:
                page=browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                page.get_by_label('你的回答').fill('断连时仍然保留的回答')
                held=[]
                page.route('**/api/tasks/'+task, lambda route: held.append(route))
                page.clock.run_for(5000)
                expect(page.locator('#connection')).to_contain_text('连接正常')
                page.clock.run_for(10000)
                expect(page.locator('#connection')).to_contain_text('可能过期')
                expect(page.get_by_role('button',name='提交回答',exact=True)).to_be_disabled()
                expect(page.get_by_label('你的回答')).to_be_enabled()
                page.get_by_label('你的回答').fill('断连期间修改的草稿')
                page.unroute('**/api/tasks/'+task)
                page.clock.run_for(1000)
                expect(page.locator('#connection')).to_contain_text('连接正常')
                expect(page.get_by_label('你的回答')).to_have_value('断连期间修改的草稿')
                expect(page.get_by_role('button',name='提交回答',exact=True)).to_be_enabled()
                assert service.inspect(task)==before
            finally:
                browser.close()


def test_copy_can_be_edited_offline_but_cannot_submit_until_state_is_confirmed(tmp_path):
    snapshot=tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _,created=request(app,'/api/tasks',{'request_id':'offline-edit','question':'用户表现怎么样？','snapshot_id':'dev'})
            task=created['id']; wait_done(app,task); before=service.inspect(task)
            browser=open_browser(pw)
            try:
                page=browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#status')).to_have_text('等待澄清')
                page.route('**/api/tasks/'+task,lambda route:route.abort())
                page.get_by_role('button',name='刷新任务',exact=True).click()
                expect(page.locator('#connection')).to_contain_text('可能过期')
                page.get_by_role('button',name='复制并修改',exact=True).click()
                page.get_by_label('分析问题').fill('断连期间编辑的新草稿')
                expect(page.get_by_role('button',name='开始分析',exact=True)).to_be_disabled()
                page.locator('#analysis-form').evaluate("form=>form.requestSubmit()")
                assert len(request(app,'/api/tasks')[1]['tasks'])==1
                page.unroute('**/api/tasks/'+task)
                page.get_by_role('button',name='立即重连',exact=True).click()
                expect(page.locator('#connection')).to_contain_text('连接正常')
                expect(page.get_by_label('分析问题')).to_have_value('断连期间编辑的新草稿')
                expect(page.get_by_role('button',name='开始分析',exact=True)).to_be_enabled()
                assert service.inspect(task)==before
            finally:
                browser.close()


def test_backoff_deadline_includes_hidden_time_and_manual_reconnect_is_single(tmp_path):
    snapshot=tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _,created=request(app,'/api/tasks',{'request_id':'bounded-recovery','question':'用户表现怎么样？','snapshot_id':'dev'})
            task=created['id']; wait_done(app,task); before=service.inspect(task)
            browser=open_browser(pw)
            try:
                page=browser.new_page(); page.add_init_script(VISIBILITY)
                page.clock.install(time=0); page.clock.pause_at(1000)
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#status')).to_have_text('等待澄清')
                reads=[]
                def fail(route):
                    reads.append(route.request); route.abort()
                page.route('**/api/tasks/'+task,fail)
                page.get_by_role('button',name='刷新任务',exact=True).click()
                expect(page.locator('#connection')).to_contain_text('可能过期')
                for count,delay in enumerate([1000,2000,4000,8000,10000],start=1):
                    page.clock.run_for(delay-1); assert len(reads)==count
                    with page.expect_request(app.origin+'/api/tasks/'+task):
                        page.clock.run_for(1)
                    page.wait_for_timeout(50)
                    assert len(reads)==count+1
                visibility(page,True); page.clock.run_for(96000)
                visibility(page,False)
                expect(page.locator('#connection')).to_contain_text('自动重连已停止')
                page.clock.run_for(30000); assert len(reads)==6
                visibility(page,True); visibility(page,False)
                assert len(reads)==6
                page.unroute('**/api/tasks/'+task); held=[]
                def hold(route):
                    held.append((route,route.fetch()))
                page.route('**/api/tasks/'+task,hold)
                page.get_by_role('button',name='立即重连',exact=True).click()
                page.get_by_role('button',name='立即重连',exact=True).click()
                page.wait_for_timeout(50)
                assert len(held)==1
                route,result=held.pop(); route.fulfill(response=result)
                expect(page.locator('#connection')).to_contain_text('连接正常')
                assert service.inspect(task)==before
            finally:
                browser.close()


def test_request_waits_count_toward_recovery_deadline(tmp_path):
    snapshot=tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _,created=request(app,'/api/tasks',{'request_id':'hung-recovery','question':'用户表现怎么样？','snapshot_id':'dev'})
            task=created['id']; wait_done(app,task); before=service.inspect(task)
            browser=open_browser(pw)
            try:
                page=browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#status')).to_have_text('等待澄清')
                page.route('**/api/tasks/'+task,lambda route:route.abort())
                page.get_by_role('button',name='刷新任务',exact=True).click()
                expect(page.locator('#connection')).to_contain_text('可能过期')
                page.unroute('**/api/tasks/'+task); held=[]
                page.route('**/api/tasks/'+task,lambda route:held.append(route))
                for count,delay in enumerate([1000,2000,4000,8000,10000,10000,10000],start=1):
                    with page.expect_request(app.origin+'/api/tasks/'+task):
                        page.clock.run_for(delay)
                    page.clock.run_for(10000)
                    page.wait_for_timeout(50)
                    assert len(held)==count
                # 115 seconds elapsed: the next ten-second backoff must stop at 120.
                page.clock.run_for(5000)
                expect(page.locator('#connection')).to_contain_text('自动重连已停止')
                page.clock.run_for(30000); assert len(held)==7
                assert service.inspect(task)==before
            finally:
                browser.close()


def test_recovery_never_replays_or_replaces_unknown_answer(tmp_path):
    snapshot=tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _,created=request(app,'/api/tasks',{'request_id':'unknown-recovery','question':'用户表现怎么样？','snapshot_id':'dev'})
            task=created['id']; wait_done(app,task)
            browser=open_browser(pw)
            try:
                page=browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#status')).to_have_text('等待澄清')
                writes=[]
                def lose(route):
                    writes.append(route.request.post_data_json); route.fetch(); route.abort()
                page.route('**/answers',lose)
                # Inconclusive lookup exercises the explicit retry path.
                page.route('**/api/operations/**', lambda route: route.fulfill(json={'accepted':False}))
                page.get_by_label('你的回答').fill('留存')
                page.get_by_role('button',name='提交回答',exact=True).click()
                expect(page.get_by_role('button',name='重试相同回答',exact=True)).to_be_disabled()
                wait_done(app,task); before=service.inspect(task)
                page.route('**/api/tasks/'+task,lambda route:route.abort())
                page.get_by_role('button',name='刷新任务',exact=True).click()
                expect(page.locator('#connection')).to_contain_text('可能过期')
                expect(page.get_by_role('button',name='重试相同回答',exact=True)).to_be_disabled()
                expect(page.get_by_label('你的回答')).to_be_enabled()
                page.get_by_label('你的回答').fill('断连时对旧问题的额外草稿')
                page.unroute('**/api/tasks/'+task)
                page.get_by_role('button',name='立即重连',exact=True).click()
                expect(page.locator('#connection')).to_contain_text('连接正常')
                expect(page.locator('#unknown-answer-text')).to_have_value('留存')
                page.get_by_label('你的回答').fill('不会替换原操作的新草稿')
                expect(page.get_by_role('button',name='提交回答',exact=True)).to_be_disabled()
                assert len(writes)==1 and service.inspect(task)==before
                page.unroute('**/answers')
                def retry(route):
                    writes.append(route.request.post_data_json); route.continue_()
                page.route('**/answers',retry)
                page.get_by_role('button',name='重试原回答',exact=True).click()
                expect(page.locator('#unknown-answer')).to_be_hidden()
                assert writes[0]==writes[1] and service.inspect(task)==before
                expect(page.get_by_label('你的回答')).to_have_value('不会替换原操作的新草稿')
            finally:
                browser.close()
