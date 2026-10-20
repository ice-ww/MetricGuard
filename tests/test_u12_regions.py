"""Local read recovery at browser / real HTTP / published evidence boundaries."""
import pytest
import httpx2 as httpx
import duckdb
from playwright.sync_api import sync_playwright, expect

from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_t09_service import image, response
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser
from tests.test_u9_lifecycle import VISIBILITY, visibility


@pytest.fixture(scope='module')
def region_snapshot(tmp_path_factory):
    return build_snapshot(tmp_path_factory.mktemp('region-data')/'snapshot', scenario='normal', seed=421001)


@pytest.fixture
def published(tmp_path, image, region_snapshot):
    calls = []
    def provider(req):
        calls.append(req)
        return response({'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'}
                        if len(calls) % 2 else
                        {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]})
    with TaskService(tmp_path/'state', image, {'dev':region_snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service) as app:
            _, created = request(app, '/api/tasks', {'request_id':'region-original',
                'question':'查询新增用户数', 'snapshot_id':'dev', 'window':['2026-01-08','2026-01-15']})
            task = created['id']; assert wait_done(app, task)['status'] == 'ended'
            assert len(calls) == 2
            yield app, service, task, calls


def test_report_and_history_recover_independently_then_stop_reading(published):
    app, service, task, calls = published
    before = service.inspect(task); report = request(app, '/api/tasks/'+task+'/report')[1]
    with sync_playwright() as pw:
        browser = open_browser(pw)
        try:
            page = browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
            page.route('**/report', lambda route: route.abort())
            page.route('**/api/tasks', lambda route: route.abort())
            page.goto(app.origin+'/?task='+task)
            expect(page.locator('#report-message')).to_contain_text('报告读取失败')
            expect(page.locator('#history-message')).to_contain_text('历史列表读取失败')
            expect(page.locator('#connection')).to_contain_text('连接正常')
            expect(page.locator('#rerun')).to_be_enabled()
            page.unroute('**/api/tasks')
            with page.expect_response(app.origin+'/api/tasks'):
                page.clock.run_for(1000)
            expect(page.locator('#history-list a')).to_have_count(1)
            expect(page.locator('#history-message')).to_be_empty()
            expect(page.locator('#report-message')).to_contain_text('报告读取失败')
            page.unroute('**/report')
            with page.expect_response('**/report'):
                page.clock.run_for(2000)
            expect(page.locator('#report-kind')).to_have_text('查询事实')
            expect(page.locator('#report-message')).to_be_empty()
            reads = []; page.on('request', lambda req: reads.append(req))
            page.clock.run_for(30000)
            assert reads == [] and len(calls) == 2 and service.inspect(task) == before
            assert request(app, '/api/tasks/'+task+'/report')[1] == report
        finally:
            browser.close()


@pytest.mark.parametrize('region', ['report', 'history'])
def test_region_preserves_content_and_bounds_hanging_reads_and_backoff(published, region):
    app, service, task, calls = published
    before = service.inspect(task)
    path = app.origin+('/api/tasks/'+task+'/report' if region == 'report' else '/api/tasks')
    with sync_playwright() as pw:
        browser = open_browser(pw)
        try:
            page = browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
            page.goto(app.origin+'/?task='+task)
            expect(page.locator('#report-kind')).to_be_visible()
            expect(page.locator('#history-list a')).to_have_count(1)
            old_report = page.locator('#report-view').inner_text()
            held = []; page.route(path, lambda route: held.append(route))
            button = page.locator('#'+region+'-refresh')
            button.click(); button.click()
            assert len(held) == 1
            page.clock.run_for(9999)
            expect(page.locator('#'+region+'-message')).not_to_contain_text('超过 10 秒')
            page.clock.run_for(1)
            expect(page.locator('#'+region+'-message')).to_contain_text('超过 10 秒')
            expect(page.locator('#connection')).to_contain_text('连接正常')
            expect(page.locator('#rerun')).to_be_enabled()
            assert page.locator('#report-view').inner_text() == old_report
            expect(page.locator('#history-list a')).to_have_count(1)
            for count, delay in enumerate([1000,2000,4000,8000,10000,10000,10000], start=2):
                with page.expect_request(path):
                    page.clock.run_for(delay)
                page.clock.run_for(10000)
                expect(page.locator('#'+region+'-message')).to_contain_text('读取失败')
                assert len(held) == count
            page.clock.run_for(5000)
            expect(page.locator('#'+region+'-message')).to_contain_text('两分钟上限')
            page.clock.run_for(30000)
            assert len(held) == 8
            page.unroute(path)
            button.click()
            expect(page.locator('#'+region+'-message')).to_be_empty()
            assert service.inspect(task) == before and len(calls) == 2
        finally:
            browser.close()


@pytest.mark.parametrize('region', ['report', 'history'])
def test_background_time_does_not_renew_region_recovery(published, region):
    app, service, task, calls = published
    path = app.origin+('/api/tasks/'+task+'/report' if region == 'report' else '/api/tasks')
    with sync_playwright() as pw:
        browser = open_browser(pw)
        try:
            page = browser.new_page(); page.add_init_script(VISIBILITY)
            page.clock.install(time=0); page.clock.pause_at(1000)
            page.goto(app.origin+'/?task='+task)
            expect(page.locator('#report-kind')).to_be_visible()
            reads = []
            def fail(route):
                reads.append(route.request); route.abort()
            page.route(path, fail)
            page.locator('#'+region+'-refresh').click()
            expect(page.locator('#'+region+'-message')).to_contain_text('读取失败')
            visibility(page, True); page.clock.run_for(120000); visibility(page, False)
            expect(page.locator('#'+region+'-message')).to_contain_text('两分钟上限')
            count = len(reads)
            visibility(page, True); visibility(page, False); page.clock.run_for(30000)
            assert len(reads) == count == 1
            expect(page.locator('#connection')).to_contain_text('连接正常')
            page.unroute(path); page.locator('#'+region+'-refresh').click()
            expect(page.locator('#'+region+'-message')).to_be_empty()
            assert len(calls) == 2
        finally:
            browser.close()


@pytest.mark.parametrize('region,status', [('report',403),('report',404),('history',403),('history',404)])
def test_definitive_region_errors_stop_without_disabling_task_actions(published, region, status):
    app, service, task, calls = published
    path = app.origin+('/api/tasks/'+task+'/report' if region == 'report' else '/api/tasks')
    with sync_playwright() as pw:
        browser = open_browser(pw)
        try:
            page = browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
            page.goto(app.origin+'/?task='+task)
            expect(page.locator('#report-kind')).to_be_visible()
            reads = []
            def reject(route):
                reads.append(route.request)
                route.fulfill(status=status, json={'error':'明确拒绝' if status==403 else '不存在'})
            page.route(path, reject)
            page.locator('#'+region+'-refresh').click()
            expect(page.locator('#'+region+'-message')).to_contain_text('已停止自动重试')
            page.clock.run_for(120000)
            assert len(reads) == 1 and len(calls) == 2
            expect(page.locator('#connection')).to_contain_text('连接正常')
            expect(page.locator('#rerun')).to_be_enabled()
            expect(page.locator('#report-kind')).to_be_visible()
        finally:
            browser.close()


def test_region_success_cannot_clear_global_failure_and_reconnect_syncs_history(published):
    app, service, task, calls = published
    before = service.inspect(task)
    with sync_playwright() as pw:
        browser = open_browser(pw)
        try:
            page = browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
            page.goto(app.origin+'/?task='+task)
            expect(page.locator('#report-kind')).to_be_visible()
            writes = []; page.on('request', lambda req: writes.append(req) if req.method=='POST' else None)
            state_path = app.origin+'/api/tasks/'+task
            for pattern in ['**/report', '**/api/tasks', state_path]:
                page.route(pattern, lambda route: route.abort())
            page.locator('#report-refresh').click(); page.locator('#history-refresh').click()
            page.locator('#task-refresh').click()
            expect(page.locator('#connection')).to_contain_text('提交已暂停')
            expect(page.locator('#report-message')).to_contain_text('读取失败')
            expect(page.locator('#history-message')).to_contain_text('读取失败')
            expect(page.locator('#rerun')).to_be_disabled()
            page.unroute('**/report'); page.locator('#report-refresh').click()
            expect(page.locator('#report-message')).to_be_empty()
            expect(page.locator('#history-message')).to_contain_text('读取失败')
            expect(page.locator('#rerun')).to_be_disabled()
            page.unroute('**/api/tasks'); page.locator('#history-refresh').click()
            expect(page.locator('#history-message')).to_be_empty()
            expect(page.locator('#connection')).to_contain_text('提交已暂停')
            _, other = request(app, '/api/tasks', {
                'request_id':'region-other', 'question':'用户表现怎么样？', 'snapshot_id':'dev'})
            wait_done(app, other['id'])
            expect(page.locator('#history-list a')).to_have_count(1)
            page.unroute(state_path); page.get_by_role('button', name='立即重连', exact=True).click()
            expect(page.locator('#connection')).to_contain_text('连接正常')
            expect(page.locator('#history-list a')).to_have_count(2)
            expect(page.locator('#rerun')).to_be_enabled()
            assert service.inspect(task) == before and len(calls) == 2 and writes == []
        finally:
            browser.close()


def test_late_report_and_history_cannot_replace_new_task_evidence(published, region_snapshot):
    app, service, task, calls = published
    before = service.inspect(task)
    with sync_playwright() as pw:
        browser = open_browser(pw)
        try:
            page = browser.new_page()
            page.goto(app.origin+'/?task='+task)
            expect(page.locator('#report-kind')).to_be_visible()
            held = []
            intercepted = set()
            def hold(route):
                key = 'report' if route.request.url.endswith('/report') else 'history'
                if key in intercepted:
                    route.continue_()
                else:
                    intercepted.add(key)
                    held.append((route, route.fetch()))
            page.route('**/report', hold)
            page.route('**/api/tasks', hold)
            page.locator('#report-refresh').click(); page.locator('#history-refresh').click()
            for _ in range(100):
                if len(held) == 2:
                    break
                page.wait_for_timeout(50)
            assert len(held) == 2
            page.get_by_role('button', name='新建问题', exact=True).click()
            page.get_by_label('分析问题').fill('查询新增用户数')
            page.locator('#start').fill('2026-01-01'); page.locator('#end').fill('2026-01-02')
            page.get_by_role('button', name='开始分析', exact=True).click()
            expect(page.locator('#report-kind')).to_be_visible(timeout=60000)
            new_task = page.url.split('task=')[1]
            assert new_task != task
            expect(page.locator('#history-list a')).to_have_count(2)
            rendered = page.locator('#report-view').inner_text()
            assert '2026-01-02' in rendered and '2026-01-15' not in rendered
            new_state = service.inspect(new_task)
            for route, response in held:
                route.fulfill(response=response)
            page.wait_for_timeout(100)
            assert page.locator('#report-view').inner_text() == rendered
            expect(page.locator('#history-list a')).to_have_count(2)
            page.locator('#report-view a').filter(has_text='A0').first.click()
            page.locator('#fact-0 a').click()
            with duckdb.connect(str(region_snapshot.database), read_only=True) as db:
                expected = db.execute("SELECT count(*) FROM users WHERE registered_at >= TIMESTAMPTZ '2026-01-01 00:00:00+08:00' AND registered_at < TIMESTAMPTZ '2026-01-02 00:00:00+08:00'").fetchone()[0]
            expect(page.locator('.evidence-cell:focus')).to_contain_text(str(expected))
            assert service.inspect(task) == before and service.inspect(new_task) == new_state and len(calls) == 4
        finally:
            browser.close()


def test_restart_uses_one_session_refresh_for_both_regions(tmp_path, image, region_snapshot):
    from tests.test_u10_restart import start, inspect
    child, app = start(tmp_path, region_snapshot.database, image)
    with sync_playwright() as pw:
        browser = open_browser(pw)
        try:
            _, created = request(app, '/api/tasks', {'request_id':'region-restart',
                'question':'查询新增用户数', 'snapshot_id':'dev', 'window':['2026-01-08','2026-01-15']})
            task = created['id']; wait_done(app, task); before = inspect(child, task)
            page = browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
            page.goto(app.origin+'/?task='+task)
            expect(page.locator('#report-kind')).to_be_visible()
            marker = (tmp_path/'provider.jsonl').read_bytes()
            child.kill(); child.communicate(timeout=10)
            child, app = start(tmp_path, region_snapshot.database, image, port=int(app.origin.rsplit(':',1)[1]))
            configs = []
            def hold_config(route):
                configs.append((route,route.fetch()))
            page.route('**/api/config', hold_config)
            with page.expect_request('**/api/config'):
                page.locator('#report-refresh').click()
            page.locator('#history-refresh').click()
            expect(page.locator('#connection')).to_contain_text('页面会话已失效')
            expect(page.locator('#rerun')).to_be_disabled()
            page.wait_for_timeout(100)
            assert len(configs) == 1
            with page.expect_response('**/report'):
                configs[0][0].fulfill(response=configs[0][1])
            page.clock.run_for(1000)
            expect(page.locator('#connection')).to_contain_text('连接正常')
            expect(page.locator('#report-message')).to_be_empty()
            expect(page.locator('#history-message')).to_be_empty()
            expect(page.locator('#rerun')).to_be_enabled()
            assert len(configs) == 1
            assert inspect(child, task) == before and (tmp_path/'provider.jsonl').read_bytes() == marker
        finally:
            browser.close()
            if child.poll() is None: child.kill()
            child.communicate(timeout=10)
