"""Unknown writes reconciled through real browser / HTTP / durable task records."""
from playwright.sync_api import sync_playwright, expect
import pytest

from experiments.t01.snapshots import build_snapshot
from tests.test_t09_service import image
from tests.test_u10_restart import start, inspect

from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser


def test_operation_lookup_is_authenticated_read_only_and_separates_kinds(tmp_path):
    snapshot = tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state', 'unused', {'dev':snapshot}, token='controlled') as service:
        with LocalWeb(service) as app:
            path = '/api/operations/create/lookup-operation'
            assert request(app, path)[1] == {'accepted':False}
            assert request(app, '/api/tasks')[1]['tasks'] == []
            _, created = request(app, '/api/tasks', {
                'request_id':'lookup-operation', 'question':'用户表现怎么样？', 'snapshot_id':'dev'})
            task = created['id']; wait_done(app, task); before = service.inspect(task)
            assert request(app, path, **{'X-MetricGuard-Token':'expired'})[0] == 403
            assert request(app, path, Origin='https://untrusted.invalid')[0] == 403
            for _ in range(3):
                assert request(app, path)[1] == {'accepted':True, 'id':task, 'parent':None}
                assert request(app, path.replace('/create/', '/rerun/'))[1] == {'accepted':False}
                assert request(app, path.replace('/create/', '/answer/'))[1] == {'accepted':False}
            assert service.inspect(task) == before


def test_accepted_create_is_reconciled_after_refresh_without_another_post(tmp_path):
    snapshot = tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state', 'unused', {'dev':snapshot}, token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            browser = open_browser(pw)
            try:
                page = browser.new_page(); writes = []
                page.clock.install(time=0); page.clock.pause_at(1000)
                def lose(route):
                    if route.request.method == 'POST':
                        writes.append(route.request.post_data_json)
                        route.fetch(); route.abort()
                    else:
                        route.continue_()
                page.route('**/api/tasks', lose)
                page.goto(app.origin)
                page.get_by_label('分析问题').fill('用户表现怎么样？')
                page.get_by_role('button', name='开始分析', exact=True).click()
                expect(page.locator('#connection')).to_contain_text('尚未确认')
                task = request(app, '/api/tasks')[1]['tasks'][0]['id']
                wait_done(app, task); before = service.inspect(task)
                page.get_by_label('分析问题').fill('断连期间修改的草稿')
                page.reload()
                expect(page).to_have_url(app.origin+'/?task='+task)
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                assert len(writes) == 1 and service.inspect(task) == before
                page.get_by_role('button', name='新建问题', exact=True).click()
                expect(page.get_by_label('分析问题')).to_have_value('断连期间修改的草稿')
            finally:
                browser.close()


def test_unaccepted_answer_remains_reachable_from_compose_and_retries_original(tmp_path):
    snapshot = tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state', 'unused', {'dev':snapshot}, token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {
                'request_id':'navigate-unknown', 'question':'用户表现怎么样？', 'snapshot_id':'dev'})
            task = created['id']; wait_done(app, task)
            browser = open_browser(pw)
            try:
                page = browser.new_page(); writes = []
                page.goto(app.origin+'/?task='+task)
                def lose(route):
                    writes.append(route.request.post_data_json); route.abort()
                page.route('**/answers', lose)
                page.get_by_label('你的回答').fill('留存')
                page.get_by_role('button', name='提交回答', exact=True).click()
                expect(page.locator('#connection')).to_contain_text('尚未确认')
                page.goto(app.origin)
                expect(page.locator('#pending-operations')).to_contain_text('尚未确认')
                page.get_by_label('分析问题').fill('独立的新问题草稿')
                expect(page.locator('#submit')).to_be_disabled()
                page.get_by_role('link', name='查看原回答', exact=True).click()
                expect(page.get_by_label('你的回答')).to_have_value('留存')
                page.get_by_label('你的回答').fill('新草稿不能替换旧提交')
                page.unroute('**/answers')
                def record(route):
                    writes.append(route.request.post_data_json); route.continue_()
                page.route('**/answers', record)
                page.get_by_role('button', name='重试相同回答', exact=True).click()
                expect(page.locator('#clarification-prompt')).to_contain_text('留存人群')
                expect(page.locator('#stale-drafts textarea')).to_have_value('新草稿不能替换旧提交')
                assert len(writes) == 2 and writes[0] == writes[1]
                assert len(service.inspect(task)['answers']) == 1
                page.get_by_role('button', name='新建问题', exact=True).click()
                expect(page.get_by_label('分析问题')).to_have_value('独立的新问题草稿')
            finally:
                browser.close()


@pytest.mark.parametrize('kind', ['create', 'answer', 'rerun'])
@pytest.mark.parametrize('recovery', ['lookup', 'retry'])
def test_lost_write_survives_denial_refresh_restart_and_never_reexecutes(tmp_path, image, kind, recovery):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=411001)
    child, app = start(tmp_path, snapshot.database, image)
    with sync_playwright() as pw:
        browser = open_browser(pw)
        try:
            task = None; original = None; report = None
            payload = {'request_id':'unknown-original', 'question':'查询新增用户数', 'snapshot_id':'dev'}
            if kind in ('rerun', 'answer'):
                payload['window'] = ['2026-01-08', '2026-01-15']
            if kind == 'answer':
                payload['question'] = '用户表现怎么样？'
            if kind != 'create':
                _, created = request(app, '/api/tasks', payload)
                task = created['id']; wait_done(app, task)
                original = inspect(child, task)
                report = request(app, '/api/tasks/'+task+'/report')[1]
            page = browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
            writes = []
            def lose(route):
                if route.request.method == 'POST':
                    writes.append(route.request.post_data_json)
                    route.fetch(); route.abort()
                else:
                    route.continue_()
            page.route('**/api/**', lose)
            page.goto(app.origin+('/?task='+task if task else ''))
            if kind == 'create':
                page.get_by_label('分析问题').fill('查询新增用户数')
                page.locator('#start').fill('2026-01-08'); page.locator('#end').fill('2026-01-15')
                page.get_by_role('button', name='开始分析', exact=True).click()
            elif kind == 'answer':
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                page.get_by_label('你的回答').fill('新增用户数')
                page.get_by_role('button', name='提交回答', exact=True).click()
            else:
                page.get_by_role('button', name='创建关联重跑', exact=True).click()
            expect(page.locator('#connection')).to_contain_text('尚未确认')
            result_task = request(app, '/api/tasks')[1]['tasks'][0]['id']
            assert wait_done(app, result_task)['status'] == 'ended'
            before = inspect(child, result_task)
            marker = (tmp_path/'provider.jsonl').read_bytes()
            # The worker profiles once, then stops; a rerun adds one stop call.
            assert len(marker.splitlines()) == (3 if kind == 'rerun' else 2)
            if kind == 'answer':
                page.get_by_label('你的回答').fill('修改后的旧回答草稿')
            if kind == 'create':
                page.get_by_label('分析问题').fill('修改后的新问题草稿')
            # A definitive access error cannot erase the immutable pending operation.
            page.route('**/api/operations/**', lambda route: route.fulfill(status=403, json={'error':'测试访问拒绝'}))
            page.reload()
            expect(page.locator('#connection')).to_contain_text('访问被拒绝')
            child.kill(); child.communicate(timeout=10)
            child, app = start(tmp_path, snapshot.database, image, port=int(app.origin.rsplit(':',1)[1]))
            page.unroute('**/api/operations/**')
            if recovery == 'retry':
                # Simulate inconclusive lookup at the HTTP boundary; the write still
                # reaches the real durable deduplicator after a genuine restart.
                page.route('**/api/operations/**', lambda route: route.fulfill(json={'accepted':False}))
            page.get_by_role('button', name='立即重连', exact=True).click()
            expect(page.locator('#connection')).to_contain_text('连接正常')
            if recovery == 'retry':
                retry_name = {'create':'重试相同提交', 'answer':'重试原回答', 'rerun':'重试关联重跑'}[kind]
                page.get_by_role('button', name=retry_name, exact=True).click()
                expect(page.locator('#connection')).to_contain_text('尚未确认')
                page.get_by_role('button', name='立即重连', exact=True).click()
                expect(page.locator('#connection')).to_contain_text('连接正常')
                page.unroute('**/api/**')
                def record(route):
                    if route.request.method == 'POST': writes.append(route.request.post_data_json)
                    route.fallback()
                page.route('**/api/**', record)
                page.get_by_role('button', name=retry_name, exact=True).click()
                assert len(writes) == 3 and writes[0] == writes[1] == writes[2]
            else:
                assert len(writes) == 1
            expect(page).to_have_url(app.origin+'/?task='+result_task)
            expect(page.locator('#status')).to_have_text('已结束')
            assert inspect(child, result_task) == before
            assert (tmp_path/'provider.jsonl').read_bytes() == marker
            assert len(request(app, '/api/tasks')[1]['tasks']) == (2 if kind == 'rerun' else 1)
            if kind == 'rerun':
                assert before['parent'] == task
                assert inspect(child, task) == original
                assert request(app, '/api/tasks/'+task+'/report')[1] == report
            if kind == 'answer':
                expect(page.locator('#stale-drafts textarea')).to_have_value('修改后的旧回答草稿')
            if kind == 'create':
                page.get_by_role('button', name='新建问题', exact=True).click()
                expect(page.get_by_label('分析问题')).to_have_value('修改后的新问题草稿')
        finally:
            browser.close()
            if child.poll() is None: child.kill()
            child.communicate(timeout=10)
