"""Budget presentation through the real browser, HTTP and task service."""
import threading
from pathlib import Path
import pytest
import httpx2 as httpx
from playwright.sync_api import sync_playwright, expect

from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser
from tests.test_t09_service import image, response


def test_waiting_budget_is_read_only_and_counts_admitted_calls(tmp_path):
    snapshot = tmp_path/'snapshot'
    snapshot.write_bytes(b'not queried while waiting')
    with TaskService(tmp_path/'state', 'unused', {'dev':snapshot}, token='controlled') as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {'request_id':'budget-waiting',
                'question':'用户表现怎么样？', 'snapshot_id':'dev'})
            task = created['id']
            assert wait_done(app, task)['status'] == 'waiting'
            before = service.inspect(task)
            browser = open_browser(pw)
            try:
                page = browser.new_page(); page.goto(app.origin+'/?task='+task)
                expect(page.locator('#budget-summary')).to_have_text('已计入预算：模型 0 / 10 次 · 工具 1 / 12 次')
                expect(page.locator('#budget-notice')).to_be_empty()
                page.get_by_text('预算详情', exact=True).click()
                expect(page.locator('#budget-tokens')).to_have_text('Token 预算占用：0 / 30000；已知用量：0；保留预留量：0')
                expect(page.locator('#budget-unknown')).to_have_text('尚待确认用量：0 次；用量未知：0 次。')
                expect(page.locator('#budget-time')).to_contain_text('累计时间预算（服务已确认）')
                for _ in range(2):
                    page.reload()
                    expect(page.locator('#budget-summary')).to_contain_text('工具 1 / 12 次')
                    budget = request(app, '/api/tasks/'+task)[1]['budget']
                    assert budget['active_seconds'] == before['active']
                    assert budget['stopped_reason'] is None
                assert service.inspect(task) == before
            finally:
                browser.close()


@pytest.mark.parametrize('failure', ['missing_usage', 'timeout'])
def test_pending_and_unknown_usage_retain_budget_without_replaying(tmp_path, image, failure):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=382001)
    entered = threading.Event(); release = threading.Event(); calls = []
    def provider(req):
        calls.append(req)
        if len(calls) == 1:
            return response({'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'})
        entered.set(); assert release.wait(60)
        if failure == 'timeout':
            raise httpx.ReadTimeout('controlled timeout')
        return response({'action':'stop','unsupported_hypotheses':[], 'unresolved_questions':[]}, usage=False)
    with TaskService(tmp_path/'state', image, {'dev':snapshot.database}, token='controlled',
                     limits={'tool':5, 'tokens':14000}, transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {'request_id':'budget-unknown',
                'question':'查询新增用户数', 'snapshot_id':'dev', 'window':['2026-01-08','2026-01-15']})
            task = created['id']
            browser = open_browser(pw)
            try:
                assert entered.wait(30)
                before = service.inspect(task)
                page = browser.new_page(); page.goto(app.origin+'/?task='+task)
                expect(page.locator('#budget-summary')).to_have_text('已计入预算：模型 2 / 10 次 · 工具 4 / 5 次')
                expect(page.locator('#budget-notice')).to_contain_text('工具计入次数已达上限的 80%')
                expect(page.locator('#budget-notice')).to_contain_text('Token 预算占用已达上限的 80%（可能含预留）')
                expect(page.locator('#budget-stop')).to_be_empty()
                page.get_by_text('预算详情', exact=True).click()
                expect(page.locator('#budget-unknown')).to_have_text('尚待确认用量：1 次；用量未知：0 次。')
                expect(page.locator('#budget-tokens')).to_contain_text('已知用量：48')
                budget = request(app, '/api/tasks/'+task)[1]['budget']
                assert budget['reserved_tokens'] > 2048
                assert budget['known_tokens'] == 48
                for _ in range(2):
                    page.reload()
                    expect(page.locator('#budget-summary')).to_contain_text('模型 2 / 10 次')
                    assert request(app, '/api/tasks/'+task)[1]['budget'] == budget
                assert service.inspect(task) == before
                assert len(calls) == 2
                release.set()
                expect(page.locator('#status')).to_have_text('已结束', timeout=30000)
                page.get_by_text('预算详情', exact=True).click()
                expect(page.locator('#budget-unknown')).to_have_text('尚待确认用量：0 次；用量未知：1 次。')
                expect(page.locator('#budget-stop')).to_contain_text('模型用量未知，预算保护已停止继续执行')
                terminal = request(app, '/api/tasks/'+task)[1]['budget']
                assert terminal['reserved_tokens'] == budget['reserved_tokens']
                assert terminal['known_tokens'] == 48
                assert terminal['tokens'] == budget['tokens']
                before = service.inspect(task)
                page.reload()
                expect(page.locator('#budget-stop')).to_contain_text('模型用量未知')
                assert service.inspect(task) == before
                assert len(calls) == 2
            finally:
                release.set(); browser.close()


@pytest.mark.parametrize('used,warning', [(79999, False), (80000, True)])
def test_token_threshold_does_not_declare_normal_completion_budget_stopped(tmp_path, image, used, warning):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=381001)
    def provider(req):
        payload = response({'action':'stop','unsupported_hypotheses':[], 'unresolved_questions':[]}).json()
        payload['usage'] = {'input_tokens':used-17, 'output_tokens':17}
        return httpx.Response(200, json=payload)
    with TaskService(tmp_path/'state', image, {'dev':snapshot.database}, token='controlled',
                     limits={'tokens':100000, 'tool':5}, transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {'request_id':'budget-tokens',
                'question':'查询新增用户数', 'snapshot_id':'dev', 'window':['2026-01-08','2026-01-15']})
            task = created['id']; terminal = wait_done(app, task)
            assert terminal['status'] == 'ended'
            browser = open_browser(pw)
            try:
                page = browser.new_page(); page.goto(app.origin+'/?task='+task)
                expect(page.locator('#status')).to_have_text('已结束')
                if warning:
                    expect(page.locator('#budget-notice')).to_contain_text('Token 预算占用已达上限的 80%（可能含预留）')
                else:
                    expect(page.locator('#budget-notice')).to_be_empty()
                expect(page.locator('#budget-stop')).to_be_empty()
                page.get_by_text('预算详情', exact=True).click()
                expect(page.locator('#budget-tokens')).to_have_text(f'Token 预算占用：{used} / 100000；已知用量：{used}；保留预留量：0')
                before = service.inspect(task)
                page.reload()
                expect(page.locator('#budget-summary')).to_contain_text('模型 1 / 10 次 · 工具 3 / 5 次')
                assert service.inspect(task) == before
            finally:
                browser.close()


def test_call_thresholds_follow_admissions_without_implying_stop(tmp_path, image):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=383001)
    gates = [threading.Event() for _ in range(4)]
    entered = [threading.Event() for _ in range(4)]
    actions = [
        {'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'},
        {'action':'profile','table':'users','column':'channel','kind':'distribution'},
        {'action':'profile','table':'users','column':'registration_os','kind':'distribution'},
        {'action':'stop','unsupported_hypotheses':[], 'unresolved_questions':[]}]
    calls = []
    def provider(req):
        index = len(calls); calls.append(req); entered[index].set()
        assert gates[index].wait(60)
        return response(actions[index])
    with TaskService(tmp_path/'state', image, {'dev':snapshot.database}, token='controlled',
                     limits={'model':5, 'tool':10}, transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {'request_id':'budget-counts',
                'question':'查询新增用户数', 'snapshot_id':'dev', 'window':['2026-01-08','2026-01-15']})
            task = created['id']; browser = open_browser(pw)
            try:
                assert entered[0].wait(30)
                page = browser.new_page(); page.goto(app.origin+'/?task='+task)
                expect(page.locator('#budget-summary')).to_contain_text('模型 1 / 5 次')
                expect(page.locator('#budget-notice')).to_be_empty()
                gates[0].set(); assert entered[1].wait(30)
                gates[1].set(); assert entered[2].wait(30)
                expect(page.locator('#budget-summary')).to_contain_text('模型 3 / 5 次')
                expect(page.locator('#budget-notice')).to_be_empty()
                gates[2].set(); assert entered[3].wait(30)
                expect(page.locator('#budget-notice')).to_have_text('模型计入次数已达上限的 80% 或以上。')
                expect(page.locator('#budget-stop')).to_be_empty()
                gates[3].set()
                expect(page.locator('#status')).to_have_text('已结束', timeout=30000)
                expect(page.locator('#budget-summary')).to_have_text('已计入预算：模型 4 / 5 次 · 工具 6 / 10 次')
                expect(page.locator('#budget-stop')).to_be_empty()
                expect(page.locator('#result')).to_contain_text('1680 人')
                page.get_by_text('预算详情', exact=True).click()
                expect(page.locator('#budget-tokens')).to_have_text('Token 预算占用：192 / 30000；已知用量：192；保留预留量：0')
                output = Path('artifacts/u8-budget'); output.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(output/'budget.png'), full_page=True)
                page.set_viewport_size({'width':390,'height':844})
                assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                page.screenshot(path=str(output/'budget-mobile.png'), full_page=True)
                assert len(calls) == 4
            finally:
                for gate in gates: gate.set()
                browser.close()


@pytest.mark.parametrize('limits,valid,expected_status,expected_tools,message', [
    ({'tool':1}, True, 'ended', 1, '预算不足以继续执行'),
    ({'active_seconds':.000001}, True, 'ended', 0, '累计执行时间预算不足'),
    ({'model':1}, True, 'ended', 3, '剩余额度需保留给报告'),
    # Retrieval and schema succeed; the real watermark query fails on the corrupt snapshot.
    ({}, False, 'failed', 3, None),
])
def test_service_stop_reason_is_authoritative_even_below_warning_threshold(tmp_path, image, limits, valid, expected_status, expected_tools, message):
    if valid:
        snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=384001).database
    else:
        snapshot = tmp_path/'broken.duckdb'; snapshot.write_bytes(b'invalid database')
    calls = []
    def provider(req):
        calls.append(req)
        raise AssertionError('No model request expected')
    with TaskService(tmp_path/'state', image, {'dev':snapshot}, token='controlled', limits=limits,
                     transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service) as app, sync_playwright() as pw:
            _, created = request(app, '/api/tasks', {'request_id':'budget-stops',
                'question':'查询新增用户数', 'snapshot_id':'dev', 'window':['2026-01-08','2026-01-15']})
            task = created['id']; assert wait_done(app, task)['status'] == expected_status
            before = service.inspect(task)
            assert before['tool_calls'] == expected_tools and before['model_calls'] == 0
            browser = open_browser(pw)
            try:
                page = browser.new_page(); page.goto(app.origin+'/?task='+task)
                expect(page.locator('#budget-summary')).to_contain_text(f'工具 {expected_tools} / ')
                if message:
                    expect(page.locator('#budget-stop')).to_contain_text(message)
                else:
                    expect(page.locator('#budget-stop')).to_be_empty()
                if 'tool' not in limits:
                    expect(page.locator('#budget-notice')).to_be_empty()
                assert request(app, '/api/tasks/'+task)[1]['budget']['active_seconds'] == before['active']
                page.reload()
                expect(page.locator('#budget-summary')).to_contain_text('模型 0 / ')
                assert service.inspect(task) == before and calls == []
            finally:
                browser.close()
