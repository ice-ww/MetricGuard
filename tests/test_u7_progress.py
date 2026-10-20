"""Execution progress observed through the real local HTTP and browser boundary."""
from datetime import datetime, timezone
import threading
import json
import sqlite3
import subprocess
import sys
import time
from types import SimpleNamespace
from pathlib import Path

import pytest

import httpx2 as httpx
from playwright.sync_api import sync_playwright, expect

from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_t09_service import image, response
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser


def test_real_progress_survives_reads_and_repeated_model_query_stages(tmp_path, image):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=371001)
    instant = [datetime(2026, 10, 19, 1, tzinfo=timezone.utc)]
    entered = [threading.Event(), threading.Event()]
    release = [threading.Event(), threading.Event()]
    querying = threading.Event(); query_release = threading.Event()
    model_returned = threading.Event(); result_release = threading.Event()
    calls = []

    def fault(point):
        if point == 'after_result' and len(calls) == 1:
            model_returned.set()
            assert result_release.wait(60)
        if point == 'before_query_dispatch':
            querying.set()
            assert query_release.wait(60)

    def provider(req):
        index = len(calls)
        calls.append(req)
        entered[index].set()
        assert release[index].wait(60)
        if index == 0:
            return response({'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'})
        return response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]})

    with TaskService(tmp_path/'state', image, {'dev':snapshot.database}, token='controlled',
                     progress_clock=lambda:instant[0], transport=httpx.MockTransport(provider), fault_hook=fault) as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            browser = open_browser(pw)
            try:
                page = browser.new_page(); page.goto(app.origin)
                page.get_by_label('分析问题').fill('查询新增用户数')
                page.locator('#start').fill('2026-01-08'); page.locator('#end').fill('2026-01-15')
                page.get_by_role('button', name='开始分析', exact=True).click()
                assert entered[0].wait(30)
                expect(page.locator('#current-action')).to_have_text('当前动作：请求模型选择下一步分析')
                task = page.url.split('task=')[1]
                before = service.inspect(task)
                assert request(app, '/api/tasks/'+task)[1]['progress']['latest_at'] == '2026-10-19T01:00:00+00:00'
                instant[0] = datetime(2026, 10, 19, 1, 0, 59, tzinfo=timezone.utc)
                page.reload()
                expect(page.locator('#progress-time')).to_contain_text('2026/10/19')
                expect(page.locator('#progress-notice')).to_be_empty()
                instant[0] = datetime(2026, 10, 19, 1, 1, tzinfo=timezone.utc)
                expect(page.locator('#progress-notice')).to_contain_text('60 秒')
                output = Path('artifacts/u7-progress'); output.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(output/'quiet.png'), full_page=True)
                page.set_viewport_size({'width':390,'height':844})
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                page.screenshot(path=str(output/'quiet-mobile.png'), full_page=True)
                page.set_viewport_size({'width':1280,'height':720})
                for _ in range(3):
                    state = request(app, '/api/tasks/'+task)[1]
                    assert state['progress']['latest_at'] == '2026-10-19T01:00:00+00:00'
                after = service.inspect(task)
                assert (after['active'], after['model_calls'], after['tool_calls']) == (before['active'], before['model_calls'], before['tool_calls'])
                assert len(calls) == 1
                page.route('**/api/tasks/'+task, lambda route:route.abort())
                expect(page.locator('#connection')).to_contain_text('最后已知信息')
                expect(page.locator('#progress-notice')).to_be_empty()
                assert len(calls) == 1
                page.unroute('**/api/tasks/'+task)
                page.reload()
                expect(page.locator('#connection')).to_contain_text('连接正常')
                release[0].set()
                assert model_returned.wait(30)
                expect(page.locator('#current-action')).to_have_text('当前动作：正在分析（未记录具体动作）')
                result_release.set()
                assert querying.wait(30)
                expect(page.locator('#current-action')).to_have_text('当前动作：执行数据查询')
                expect(page.locator('#progress-notice')).to_be_empty()
                query_release.set()
                assert entered[1].wait(30)
                expect(page.locator('#progress-notice')).to_be_empty()
                expect(page.locator('#current-action')).to_have_text('当前动作：请求模型选择下一步分析')
                assert request(app, '/api/tasks/'+task)[1]['progress']['latest_at'] == '2026-10-19T01:01:00+00:00'
                release[1].set()
                expect(page.locator('#status')).to_have_text('已结束', timeout=30000)
                expect(page.locator('#current-action')).to_have_text('当前动作：无（已结束）')
                expect(page.locator('#result')).to_contain_text('1680 人')
                assert len(calls) == 2
                terminal = request(app, '/api/tasks/'+task)[1]
                for _ in range(2):
                    page.reload()
                    expect(page.locator('#status')).to_have_text('已结束')
                    assert request(app, '/api/tasks/'+task)[1]['progress'] == terminal['progress']
            finally:
                result_release.set()
                query_release.set()
                for gate in release: gate.set()
                browser.close()
    # Historical reports and evidence remain readable after upgrading an old trace schema.
    with sqlite3.connect(tmp_path/'state'/'ledger.sqlite') as db:
        db.execute('ALTER TABLE trace DROP COLUMN occurred_at')
    with TaskService(tmp_path/'state', image, {'dev':snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            browser = open_browser(pw)
            try:
                page = browser.new_page(); page.goto(app.origin+'/?task='+task)
                expect(page.locator('#status')).to_have_text('已结束')
                expect(page.locator('#progress-time')).to_contain_text('未记录')
                expect(page.locator('#result')).to_contain_text('1680 人')
                assert request(app, '/api/tasks/'+task+'/report')[0] == 200
                assert service.inspect(task)['evidence'][0]['rows']
                assert len(calls) == 2
            finally:
                browser.close()


@pytest.mark.parametrize('legacy', [False, True])
def test_waiting_progress_after_process_restart_and_legacy_migration(tmp_path, legacy):
    (tmp_path/'snapshot').write_bytes(b'not queried')
    child = subprocess.Popen([sys.executable, '-m', 'tests.u7_progress_worker', str(tmp_path)],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        deadline = time.monotonic()+30
        while not (tmp_path/'server.json').exists() and child.poll() is None and time.monotonic()<deadline:
            time.sleep(.05)
        app = SimpleNamespace(**json.loads((tmp_path/'server.json').read_text()))
        code, created = request(app, '/api/tasks', {'request_id':'progress-waiting', 'question':'用户表现怎么样？', 'snapshot_id':'dev'})
        assert code == 202
        task = created['id']
        waiting = wait_done(app, task)
        assert waiting['progress'] == {'action':None, 'latest_at':'2026-10-19T01:00:00+00:00', 'quiet':False}
    finally:
        child.kill(); child.communicate(timeout=10)
    if legacy:
        # Fixture downgrade to the exact old schema, not a production write path.
        with sqlite3.connect(tmp_path/'state'/'ledger.sqlite') as db:
            db.execute('ALTER TABLE trace DROP COLUMN occurred_at')
    with TaskService(tmp_path/'state', 'unused', {'dev':tmp_path/'snapshot'}, token='controlled',
                     progress_clock=lambda:datetime(2026, 10, 20, tzinfo=timezone.utc)) as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            browser = open_browser(pw)
            try:
                page = browser.new_page(); page.goto(app.origin+'/?task='+task)
                expect(page.locator('#status')).to_have_text('等待澄清')
                expect(page.locator('#current-action')).to_have_text('当前动作：等待澄清')
                expect(page.locator('#progress-notice')).to_be_empty()
                expect(page.locator('#progress-time')).to_contain_text('未记录' if legacy else '2026/10/19')
                before = service.inspect(task)
                for _ in range(2):
                    page.reload()
                    expect(page.locator('#status')).to_have_text('等待澄清')
                    assert request(app, '/api/tasks/'+task)[1]['progress'] == {
                        'action':None, 'latest_at':None if legacy else '2026-10-19T01:00:00+00:00', 'quiet':False}
                assert service.inspect(task) == before
                assert before['model_calls'] == 0 and before['tool_calls'] == 1
            finally:
                browser.close()
