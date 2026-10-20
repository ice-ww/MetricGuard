"""Cross-feature acceptance through browser, HTTP and durable task inspection."""
from datetime import datetime, timezone
import json
from pathlib import Path
import threading

import httpx2 as httpx
from playwright.sync_api import expect, sync_playwright

from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_t09_service import image, response
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser
from tests.test_u9_lifecycle import VISIBILITY, visibility


def record(name, page, **evidence):
    output = Path('artifacts/u13-controlled')
    output.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(output/(name+'.png')), full_page=True)
    (output/(name+'.json')).write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2), encoding='utf-8')


def test_running_progress_and_budget_survive_disconnect_without_new_execution(tmp_path, image):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=431001)
    entered = threading.Event(); release = threading.Event(); calls = []
    instant = [datetime(2026, 10, 20, 1, tzinfo=timezone.utc)]
    def provider(req):
        calls.append(req)
        if len(calls) == 1:
            return response({'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'})
        entered.set(); assert release.wait(90)
        return response({'action':'stop','unsupported_hypotheses':[], 'unresolved_questions':[]})
    with TaskService(tmp_path/'state', image, {'dev':snapshot.database}, token='controlled',
                     limits={'tool':5, 'tokens':14000}, progress_clock=lambda:instant[0],
                     transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            browser = open_browser(pw)
            try:
                page = browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
                page.goto(app.origin)
                page.get_by_label('分析问题').fill('查询新增用户数')
                page.locator('#start').fill('2026-01-08'); page.locator('#end').fill('2026-01-15')
                page.get_by_role('button', name='开始分析', exact=True).click()
                assert entered.wait(30)
                page.wait_for_url('**/?task=*')
                task = page.url.split('task=')[1]
                with page.expect_response(app.origin+'/api/tasks/'+task):
                    page.clock.run_for(1000)
                expect(page.locator('#current-action')).to_contain_text('请求模型选择下一步分析')
                expect(page.locator('#budget-summary')).to_have_text('已计入预算：模型 2 / 10 次 · 工具 4 / 5 次')
                expect(page.locator('#budget-notice')).to_contain_text('80%')
                page.get_by_text('预算详情', exact=True).click()
                expect(page.locator('#budget-unknown')).to_contain_text('尚待确认用量：1 次')
                before = service.inspect(task)
                state_before = request(app, '/api/tasks/'+task)[1]
                event_time = page.locator('#progress-time').inner_text()
                instant[0] = datetime(2026, 10, 20, 1, 1, tzinfo=timezone.utc)
                with page.expect_response(app.origin+'/api/tasks/'+task):
                    page.clock.run_for(1000)
                expect(page.locator('#progress-notice')).to_contain_text('60 秒')
                page.route('**/api/tasks/'+task, lambda route:route.abort())
                page.route('**/api/tasks', lambda route:route.abort())
                page.get_by_role('button', name='刷新列表', exact=True).click()
                page.clock.run_for(1000)
                expect(page.locator('#connection')).to_contain_text('最后已知信息')
                expect(page.locator('#history-message')).to_contain_text('历史列表读取失败')
                expect(page.locator('#progress-notice')).to_be_empty()
                assert page.locator('#progress-time').inner_text() == event_time
                record('running-offline', page, before=state_before, task=before, provider_calls=len(calls))
                page.unroute('**/api/tasks/'+task); page.unroute('**/api/tasks')
                with page.expect_response(app.origin+'/api/tasks/'+task):
                    page.clock.run_for(1000)
                expect(page.locator('#connection')).to_contain_text('连接正常')
                expect(page.locator('#history-message')).to_be_empty()
                expect(page.locator('#progress-notice')).to_contain_text('60 秒')
                assert page.locator('#progress-time').inner_text() == event_time
                state_after = request(app, '/api/tasks/'+task)[1]
                assert state_after['progress']['latest_at'] == '2026-10-20T01:00:00+00:00'
                assert state_after['budget'] == state_before['budget']
                assert service.inspect(task) == before and len(calls) == 2
                record('running-recovered', page, before=state_before, after=state_after,
                       task=before, provider_calls=len(calls))
                instant[0] = datetime(2026, 10, 20, 1, 1, 1, tzinfo=timezone.utc)
                release.set(); assert wait_done(app, task)['status'] == 'ended'
                with page.expect_response('**/report'):
                    page.clock.run_for(1000)
                expect(page.locator('#current-action')).to_have_text('当前动作：无（已结束）')
                expect(page.locator('#progress-notice')).to_be_empty()
                expect(page.locator('#report-overview')).to_contain_text('1680 人')
                page.locator('#report-overview a').first.click()
                page.locator('#fact-0 a').click()
                expect(page.locator('.evidence-cell:focus')).to_have_text('1680')
                terminal = service.inspect(task)
                reads = []
                page.on('request', lambda req:reads.append(req) if '/api/' in req.url else None)
                page.clock.run_for(30000)
                assert reads == [] and service.inspect(task) == terminal and len(calls) == 2
                record('running-ended', page, task=terminal, provider_calls=len(calls))
            finally:
                release.set(); browser.close()


def test_offline_tab_keeps_versioned_drafts_after_other_tab_answers_and_deadline(tmp_path):
    snapshot = tmp_path/'snapshot'; snapshot.write_bytes(b'not queried while waiting')
    with TaskService(tmp_path/'state', 'unused', {'dev':snapshot}, token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {'request_id':'combined-draft',
                'question':'用户表现怎么样？', 'snapshot_id':'dev'})
            task = created['id']; assert wait_done(app, task)['status'] == 'waiting'
            browser = open_browser(pw); context = browser.new_context()
            try:
                page = context.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
                page.add_init_script(VISIBILITY)
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                page.get_by_label('你的回答').fill('离线前尚未提交的指标草稿')
                page.route('**/api/tasks/'+task, lambda route:route.abort())
                page.clock.run_for(5000)
                expect(page.locator('#connection')).to_contain_text('提交已暂停')
                page.get_by_label('你的回答').fill('离线编辑后的旧问题草稿')
                expect(page.get_by_role('button', name='提交回答', exact=True)).to_be_disabled()
                other = context.new_page(); other.goto(app.origin+'/?task='+task)
                expect(other.locator('#clarification-prompt')).to_contain_text('哪个指标')
                other.get_by_label('你的回答').fill('留存')
                other.get_by_role('button', name='提交回答', exact=True).click()
                assert wait_done(app, task)['status'] == 'waiting'
                other.reload()
                expect(other.locator('#clarification-prompt')).to_contain_text('留存人群')
                after_answer = service.inspect(task)
                assert len(after_answer['answers']) == 1
                assert after_answer['model_calls'] == 0 and after_answer['tool_calls'] == 2
                reads = []; writes = []
                page.on('request', lambda req:reads.append(req) if req.url.endswith('/'+task) else None)
                page.on('request', lambda req:writes.append(req) if req.method=='POST' else None)
                visibility(page, True); page.clock.run_for(120000)
                visibility(page, False)
                expect(page.locator('#connection')).to_contain_text('两分钟上限')
                assert reads == []
                expect(page.get_by_label('你的回答')).to_have_value('离线编辑后的旧问题草稿')
                page.unroute('**/api/tasks/'+task)
                page.get_by_role('button', name='立即重连', exact=True).click()
                expect(page.locator('#clarification-prompt')).to_contain_text('留存人群')
                expect(page.get_by_label('你的回答')).to_have_value('')
                expect(page.locator('#stale-drafts textarea')).to_have_value('离线编辑后的旧问题草稿')
                assert page.locator('#stale-drafts textarea').get_attribute('readonly') is not None
                page.get_by_label('你的回答').fill('新问题尚未提交的人群草稿')
                page.reload()
                expect(page.get_by_label('你的回答')).to_have_value('新问题尚未提交的人群草稿')
                expect(page.locator('#stale-drafts textarea')).to_have_value('离线编辑后的旧问题草稿')
                expect(page.locator('#progress-notice')).to_be_empty()
                assert writes == [] and service.inspect(task) == after_answer
                record('draft-recovered', page, task=after_answer, offline_page_writes=len(writes),
                       old_draft='离线编辑后的旧问题草稿', new_draft='新问题尚未提交的人群草稿')
            finally:
                browser.close()
