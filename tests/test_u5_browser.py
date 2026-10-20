"""Browser recovery actions use the real service; faults enter at provider boundary."""
import json
import subprocess
import sys
import time
from pathlib import Path
import duckdb
import httpx2 as httpx
from playwright.sync_api import sync_playwright, expect
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser
from tests.test_t09_service import image, response


def test_timeout_copy_and_linked_rerun(tmp_path, image):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=351001)
    calls = []
    def provider(req):
        calls.append(req)
        raise httpx.ReadTimeout('private-u5', request=req)
    with TaskService(tmp_path/'state', image, {'dev': snapshot.database}, token='private-u5', transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service) as app:
            _, result = request(app, '/api/tasks', {'request_id':'u5-timeout', 'question':'查询新增用户数', 'snapshot_id':'dev', 'window':['2026-01-08','2026-01-15']})
            task = result['id']; wait_done(app, task)
            old = service.inspect(task)
            assert len(calls) == 1
            with sync_playwright() as pw:
                browser = open_browser(pw)
                try:
                    page = browser.new_page(); page.goto(app.origin+'/?task='+task)
                    expect(page.locator('#recovery-message')).to_contain_text('超时')
                    assert 'private-u5' not in page.locator('body').inner_text()
                    page.get_by_role('button', name='复制并修改', exact=True).click()
                    expect(page.get_by_label('分析问题')).to_be_enabled()
                    expect(page.get_by_label('开始日期（包含）', exact=True)).to_have_value('2026-01-08')
                    assert len(request(app, '/api/tasks')[1]['tasks']) == 1
                    page.get_by_label('分析问题').fill('用户表现怎么样？')
                    page.get_by_role('button', name='开始分析', exact=True).click()
                    expect(page.locator('#status')).to_have_text('等待澄清')
                    copied = service.inspect(page.url.split('task=')[1])
                    assert copied['parent'] is None and copied['evidence'] == [] and copied['answers'] == []
                    page.goto(app.origin+'/?task='+task)
                    page.get_by_role('button', name='创建关联重跑', exact=True).click()
                    expect(page.locator('#parent-link')).to_have_attribute('href', '/?task='+task)
                    expect(page.locator('#recovery-message')).to_contain_text('超时')
                    rerun = page.url.split('task=')[1]
                    assert rerun != task and service.inspect(rerun)['parent'] == task
                    assert service.inspect(task) == old and len(calls) == 2
                    assert 'private-u5' not in json.dumps(request(app, '/api/tasks/'+rerun)[1])
                    out = Path('artifacts/u5-browser'); out.mkdir(parents=True, exist_ok=True)
                    page.screenshot(path=str(out/'timeout-rerun.png'), full_page=True)
                    (out/'timeout.json').write_text(json.dumps({'original':old,'copied':copied,'rerun':service.inspect(rerun),'provider_calls':len(calls)}, ensure_ascii=False, indent=2), encoding='utf-8')
                finally:
                    browser.close()


def test_process_crash_history_rerun_preserves_evidence(tmp_path, image):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=351002)
    child = subprocess.Popen([sys.executable, '-m', 'tests.u5_crash_worker', str(tmp_path), str(snapshot.database), image], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with sync_playwright() as pw:
        browser = open_browser(pw)
        try:
            deadline = time.monotonic()+40
            while not (tmp_path/'server.json').exists() and child.poll() is None and time.monotonic()<deadline:
                time.sleep(.05)
            assert (tmp_path/'server.json').exists()
            origin = json.loads((tmp_path/'server.json').read_text())['origin']
            page = browser.new_page(); page.goto(origin)
            page.get_by_label('分析问题').fill('查询新增用户数')
            page.get_by_label('开始日期（包含）', exact=True).fill('2026-01-08')
            page.get_by_label('结束日期（不包含）', exact=True).fill('2026-01-15')
            page.get_by_role('button', name='开始分析', exact=True).click()
            assert child.wait(timeout=90) == 73
            marker = (tmp_path/'provider.jsonl').read_bytes()
            assert len(marker.splitlines()) == 2
            calls = []
            def provider(req):
                calls.append(req)
                return response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]})
            with TaskService(tmp_path/'state', image, {'dev': snapshot.database}, token='private-u5', transport=httpx.MockTransport(provider)) as service:
                with LocalWeb(service) as app:
                    page.goto(app.origin)
                    expect(page.locator('#history-list li')).to_contain_text('已中断')
                    page.get_by_role('link', name='查询新增用户数', exact=True).click()
                    expect(page.locator('#recovery-message')).to_contain_text('不会自动重放')
                    task = page.url.split('task=')[1]; old = service.inspect(task)
                    assert request(app, '/api/tasks/'+task)[1]['progress'] == {
                        'action':None, 'latest_at':'2026-10-19T01:00:00+00:00', 'quiet':False}
                    expect(page.locator('#current-action')).to_have_text('当前动作：无（已中断）')
                    expect(page.locator('#progress-notice')).to_be_empty()
                    expect(page.locator('#budget-summary')).to_have_text('已计入预算：模型 2 / 10 次 · 工具 4 / 12 次')
                    page.get_by_text('预算详情', exact=True).click()
                    expect(page.locator('#budget-unknown')).to_have_text('尚待确认用量：0 次；用量未知：1 次。')
                    expect(page.locator('#budget-tokens')).to_contain_text('已知用量：48')
                    expect(page.locator('#budget-stop')).to_be_empty()
                    assert request(app, '/api/tasks/'+task)[1]['budget']['active_seconds'] == 180
                    assert old['evidence'] and any(a['state']=='unknown' for a in old['attempts'])
                    with duckdb.connect(str(snapshot.database), read_only=True) as db:
                        expected = db.execute("SELECT COUNT(*) FROM users WHERE registered_at >= TIMESTAMPTZ '2026-01-08T00:00:00+08:00' AND registered_at < TIMESTAMPTZ '2026-01-15T00:00:00+08:00'").fetchone()[0]
                    assert sum(row['users'] for row in old['evidence'][0]['rows']) == expected
                    assert calls == []
                    page.reload(); expect(page.locator('#status')).to_have_text('已中断')
                    assert request(app, '/api/tasks/'+task)[1]['progress']['latest_at'] == '2026-10-19T01:00:00+00:00'
                    assert calls == []
                    page.get_by_role('button', name='创建关联重跑', exact=True).click()
                    expect(page.locator('#status')).to_have_text('已结束', timeout=60000)
                    new = page.url.split('task=')[1]
                    assert new != task and service.inspect(new)['parent'] == task
                    assert service.inspect(new)['evidence'] == []
                    assert service.inspect(task) == old and len(calls) == 1
                    assert (tmp_path/'provider.jsonl').read_bytes() == marker
                    page.get_by_role('link', name='查看原任务', exact=True).click()
                    expect(page.locator('#status')).to_have_text('已中断')
                    out = Path('artifacts/u5-browser'); out.mkdir(parents=True, exist_ok=True)
                    page.screenshot(path=str(out/'interrupted.png'), full_page=True)
                    page.set_viewport_size({'width':390,'height':844})
                    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                    page.screenshot(path=str(out/'interrupted-mobile.png'), full_page=True)
                    (out/'crash.json').write_text(json.dumps({'exit_code':73,'original':old,'rerun':service.inspect(new),'independent_users':expected,'new_provider_calls':len(calls),'old_provider_calls':2}, ensure_ascii=False, indent=2), encoding='utf-8')
        finally:
            browser.close()
            if child.poll() is None:
                child.kill()
            child.communicate(timeout=10)


def test_lost_rerun_response_retries_same_operation_after_reload(tmp_path):
    snapshot = tmp_path/'data'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state', 'unused', {'dev':snapshot}, token='private-u5') as service:
        with LocalWeb(service) as app:
            _, result = request(app, '/api/tasks', {'request_id':'u5-lost-original','question':'用户表现怎么样？','snapshot_id':'dev'})
            task = result['id']; question = wait_done(app, task)['clarification']
            (tmp_path/'state'/'analysis-checkpoints.sqlite').unlink()
            request(app, f'/api/tasks/{task}/answers', {'request_id':'u5-lost-answer','question_id':question['question_id'],'version':question['version'],'answer':'新增用户数'})
            assert wait_done(app, task)['status'] == 'failed'
            old = service.inspect(task)
            with sync_playwright() as pw:
                browser = open_browser(pw)
                try:
                    page = browser.new_page(); page.goto(app.origin+'/?task='+task)
                    def lose_response(route):
                        assert route.fetch().status == 202
                        route.abort()
                    page.route('**/rerun', lose_response, times=1)
                    # Inconclusive lookup exercises the explicit retry path.
                    page.route('**/api/operations/**', lambda route: route.fulfill(json={'accepted':False}))
                    page.get_by_role('button', name='创建关联重跑', exact=True).click()
                    expect(page.get_by_role('button', name='重试关联重跑', exact=True)).to_be_enabled()
                    tasks = request(app, '/api/tasks')[1]['tasks']
                    assert len(tasks) == 2
                    new = tasks[0]['id']; wait_done(app, new)
                    page.reload()
                    page.get_by_role('button', name='重试关联重跑', exact=True).click()
                    expect(page.locator('#status')).to_have_text('等待澄清')
                    assert page.url.endswith(new)
                    assert len(request(app, '/api/tasks')[1]['tasks']) == 2
                    assert service.inspect(task) == old
                finally:
                    browser.close()
