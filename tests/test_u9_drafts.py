"""Draft and polling behavior at the real browser/HTTP/task boundary."""
from playwright.sync_api import sync_playwright, expect

from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser


def test_refresh_restores_compose_and_same_question_answer_drafts(tmp_path):
    snapshot = tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state', 'unused', {'dev':snapshot}, token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            browser = open_browser(pw)
            try:
                page = browser.new_page(); page.goto(app.origin)
                expect(page.locator('#submit')).to_be_enabled()
                page.get_by_label('分析问题').fill('尚未提交的新问题')
                page.locator('#start').fill('2026-01-08')
                page.reload()
                expect(page.get_by_label('分析问题')).to_have_value('尚未提交的新问题')
                expect(page.locator('#start')).to_have_value('2026-01-08')
                expect(page.locator('#end')).to_have_value('')
                assert request(app, '/api/tasks')[1]['tasks'] == []
                page.get_by_label('分析问题').fill('用户表现怎么样？')
                page.locator('#start').fill('')
                page.get_by_role('button', name='开始分析', exact=True).click()
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                task = page.url.split('task=')[1]
                page.get_by_label('你的回答').fill('还在组织的回答')
                before = service.inspect(task)
                page.get_by_role('button', name='刷新待答问题', exact=True).click()
                expect(page.get_by_label('你的回答')).to_have_value('还在组织的回答')
                page.reload()
                expect(page.get_by_label('你的回答')).to_have_value('还在组织的回答')
                assert service.inspect(task) == before
                page.goto(app.origin)
                expect(page.locator('#submit')).to_be_enabled()
                expect(page.get_by_label('分析问题')).to_have_value('')
                page.get_by_label('分析问题').fill('浏览历史前的新问题草稿')
                page.locator('#start').fill('2026-02-01')
                page.goto(app.origin+'/?task='+task)
                expect(page.get_by_label('你的回答')).to_have_value('还在组织的回答')
                page.get_by_role('button', name='新建问题', exact=True).click()
                expect(page.get_by_label('分析问题')).to_have_value('浏览历史前的新问题草稿')
                expect(page.locator('#start')).to_have_value('2026-02-01')
                page.reload()
                expect(page.get_by_label('分析问题')).to_have_value('浏览历史前的新问题草稿')
            finally:
                browser.close()


def test_unknown_answer_keeps_original_operation_when_question_has_changed(tmp_path):
    snapshot = tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state', 'unused', {'dev':snapshot}, token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {'request_id':'draft-unknown','question':'用户表现怎么样？','snapshot_id':'dev'})
            task = created['id']; wait_done(app, task)
            browser = open_browser(pw)
            try:
                page = browser.new_page(); page.goto(app.origin+'/?task='+task)
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                writes = []
                def lose(route):
                    writes.append(route.request.post_data_json)
                    route.fetch(); route.abort()
                page.route('**/answers', lose)
                page.get_by_label('你的回答').fill('留存')
                page.get_by_role('button', name='提交回答', exact=True).click()
                expect(page.locator('#connection')).to_contain_text('提交已暂停')
                wait_done(app, task); before = service.inspect(task)
                page.reload()
                expect(page.locator('#clarification-prompt')).to_contain_text('留存人群')
                expect(page.locator('#unknown-answer')).to_contain_text('提交结果尚未确认')
                expect(page.locator('#unknown-answer textarea')).to_have_value('留存')
                expect(page.get_by_label('你的回答')).to_have_value('')
                page.get_by_label('你的回答').fill('新问题的草稿，不能替换原提交')
                expect(page.get_by_role('button', name='提交回答', exact=True)).to_be_disabled()
                page.unroute('**/answers')
                def record(route):
                    writes.append(route.request.post_data_json); route.continue_()
                page.route('**/answers', record)
                page.get_by_role('button', name='重试原回答', exact=True).click()
                expect(page.locator('#unknown-answer')).to_be_hidden()
                expect(page.get_by_label('你的回答')).to_have_value('新问题的草稿，不能替换原提交')
                assert len(writes) == 2 and writes[0] == writes[1]
                assert service.inspect(task) == before
                page.reload()
                expect(page.locator('#stale-drafts')).to_be_hidden()
                expect(page.get_by_label('你的回答')).to_have_value('新问题的草稿，不能替换原提交')
            finally:
                browser.close()


def test_waiting_poll_preserves_input_and_other_tab_changes_archive_old_draft(tmp_path):
    snapshot = tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state', 'unused', {'dev':snapshot}, token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {'request_id':'draft-tabs', 'question':'用户表现怎么样？','snapshot_id':'dev'})
            task = created['id']; wait_done(app, task)
            before = service.inspect(task)
            browser = open_browser(pw); context = browser.new_context()
            try:
                page = context.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
                reads = []
                page.on('request', lambda req: reads.append(req) if req.url==app.origin+'/api/tasks/'+task else None)
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                page.get_by_label('你的回答').fill('这是本页尚未提交的指标想法')
                page.get_by_label('你的回答').focus()
                page.clock.run_for(4999)
                assert len(reads) == 1
                with page.expect_response(app.origin+'/api/tasks/'+task):
                    page.clock.run_for(1)
                assert len(reads) == 2
                expect(page.get_by_label('你的回答')).to_have_value('这是本页尚未提交的指标想法')
                expect(page.get_by_label('你的回答')).to_be_focused()
                assert service.inspect(task) == before
                other = context.new_page(); other.goto(page.url)
                expect(other.get_by_label('你的回答')).to_have_value('')
                other.get_by_label('你的回答').fill('留存')
                with other.expect_response('**/answers'):
                    other.get_by_role('button', name='提交回答', exact=True).click()
                # Playwright's controlled clock is shared by this browser context.
                wait_done(app, task); other.reload()
                expect(other.locator('#clarification-prompt')).to_contain_text('留存人群')
                with page.expect_response(app.origin+'/api/tasks/'+task):
                    page.clock.run_for(5000)
                expect(page.locator('#clarification-prompt')).to_contain_text('留存人群')
                expect(page.get_by_label('你的回答')).to_have_value('')
                expect(page.locator('#stale-drafts')).to_contain_text('问题已更新')
                expect(page.locator('#stale-drafts textarea')).to_have_value('这是本页尚未提交的指标想法')
                assert page.locator('#stale-drafts textarea').get_attribute('readonly') is not None
                page.reload()
                expect(page.locator('#stale-drafts textarea')).to_have_value('这是本页尚未提交的指标想法')
                expect(page.get_by_label('你的回答')).to_have_value('')
                other.reload()
                expect(other.locator('#stale-drafts')).to_be_hidden()
                expect(other.get_by_label('你的回答')).to_have_value('')
                after = service.inspect(task)
                assert len(after['answers']) == 1 and after['model_calls'] == 0 and after['tool_calls'] == 2
                with page.expect_response(app.origin+'/api/tasks/'+task):
                    page.clock.run_for(5000)
                assert service.inspect(task) == after
                _, second = request(app, '/api/tasks', {'request_id':'draft-isolation','question':'用户表现怎么样？','snapshot_id':'dev'})
                wait_done(app, second['id'])
                page.goto(app.origin+'/?task='+second['id'])
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                expect(page.get_by_label('你的回答')).to_have_value('')
                expect(page.locator('#stale-drafts')).to_be_hidden()
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#stale-drafts textarea')).to_have_value('这是本页尚未提交的指标想法')
            finally:
                browser.close()


def test_unknown_new_submission_retries_original_payload_after_refresh(tmp_path):
    snapshot=tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            browser=open_browser(pw)
            try:
                page=browser.new_page(); writes=[]
                def lose(route):
                    if route.request.method=='POST':
                        writes.append(route.request.post_data_json)
                        route.fetch();route.abort()
                    else:route.continue_()
                page.route('**/api/tasks',lose)
                page.goto(app.origin)
                page.get_by_label('分析问题').fill('用户表现怎么样？')
                page.get_by_role('button',name='开始分析',exact=True).click()
                expect(page.get_by_role('button',name='重试相同提交',exact=True)).to_be_enabled()
                page.reload()
                expect(page.get_by_label('分析问题')).to_have_value('用户表现怎么样？')
                page.unroute('**/api/tasks')
                def record(route):
                    if route.request.method=='POST':writes.append(route.request.post_data_json)
                    route.continue_()
                page.route('**/api/tasks',record)
                page.get_by_role('button',name='重试相同提交',exact=True).click()
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                task=page.url.split('task=')[1]
                assert len(writes)==2 and writes[0]==writes[1]
                assert len(request(app,'/api/tasks')[1]['tasks'])==1
                assert service.inspect(task)['tool_calls']==1
                page.goto(app.origin)
                expect(page.get_by_label('分析问题')).to_have_value('')
            finally:browser.close()
