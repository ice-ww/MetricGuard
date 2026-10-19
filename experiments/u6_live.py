"""Production-command browser acceptance with real model calls and independent checks."""
from contextlib import contextmanager
from datetime import timedelta
import hashlib
import json
import os
from pathlib import Path
import queue
import subprocess
import sys
import threading
from typing import Any, Iterator
from urllib.request import Request, urlopen
from uuid import uuid4

import duckdb
from playwright.sync_api import Page, expect, sync_playwright
from metricguard import TaskService


@contextmanager
def server(root: Path) -> Iterator[str]:
    """Use the documented command; stop only after tasks are waiting or ended."""
    command = [sys.executable, '-m', 'experiments.u6_manual', '--state-dir', str(root/'state'), '--port', '0']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', env={**os.environ, 'PYTHONUTF8':'1'})
    lines: queue.Queue[str | None] = queue.Queue()
    def read() -> None:
        assert process.stdout is not None
        for line in process.stdout:
            lines.put(line)
        lines.put(None)
    reader = threading.Thread(target=read, daemon=True); reader.start()
    try:
        while True:
            line = lines.get(timeout=60)
            if line is None:
                raise RuntimeError('Acceptance server exited before readiness')
            with (root/'startup.log').open('a', encoding='utf-8') as output:
                output.write(line.replace(os.environ['ANTHROPIC_AUTH_TOKEN'], '[redacted]'))
            if line.startswith('本机界面：'):
                yield line.split('：', 1)[1].strip()
                break
    finally:
        process.terminate(); process.wait(timeout=20); reader.join(timeout=5)
        if process.stdout:
            process.stdout.close()


def api(origin: str, path: str, token: str = '') -> dict[str, Any]:
    with urlopen(Request(origin+path, headers={'X-MetricGuard-Token':token}), timeout=10) as response:
        return json.load(response)


def inspect_tasks(root: Path, tasks: dict[str, str]) -> dict[str, Any]:
    snapshots = {'demo': root/'demo-data/public/snapshot.duckdb', 'diagnosis': root/'diagnosis-data/public/snapshot.duckdb'}
    with TaskService(root/'state', os.environ['METRICGUARD_TEST_IMAGE'], snapshots, token='read-only') as service:
        return {name:service.inspect(task) for name,task in tasks.items()}


def inspect_report(page: Page, root: Path, name: str, report: dict[str, Any]) -> int:
    assert report['available'] and report['facts']
    expect(page.locator('#report-kind')).to_be_visible()
    page.screenshot(path=str(root/(name+'.png')), full_page=True)
    page.locator('#report-overview a').first.click()
    expect(page.locator('.fact-row:focus')).to_be_visible()
    for fact in report['facts']:
        page.locator('[id="fact-'+fact['assertion_id']+'"] a').click()
        expect(page.locator('.evidence-cell:focus')).to_have_text(json.dumps(fact['value'], ensure_ascii=False, separators=(',',':')))
    page.screenshot(path=str(root/(name+'-evidence.png')), full_page=True)
    page.reload(); expect(page.locator('#report-kind')).to_be_visible()
    page.set_viewport_size({'width':390, 'height':844})
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    page.screenshot(path=str(root/(name+'-mobile.png')), full_page=True)
    page.set_viewport_size({'width':1360, 'height':1000})
    return len(report['facts'])


def reference_checks(root: Path, states: dict[str, Any]) -> dict[str, Any]:
    count_sql = "SELECT COUNT(DISTINCT user_id) FROM users WHERE registered_at>=TIMESTAMPTZ '2026-01-08 00:00:00+08:00' AND registered_at<TIMESTAMPTZ '2026-01-15 00:00:00+08:00'"
    with duckdb.connect(str(root/'demo-data/public/snapshot.duckdb'), read_only=True) as db:
        count_row = db.execute(count_sql).fetchone()
        assert count_row is not None
        count = count_row[0]
    count_evidence = [e for e in states['query']['evidence'] if e['parameters'].get('kind')=='new_user_counts']
    assert count_evidence and sum(row['users'] for row in count_evidence[0]['rows']) == count == 1680
    users_sql = "SELECT user_id,CAST(timezone('Asia/Shanghai',registered_at) AS DATE),registration_os FROM users"
    sessions_sql = "SELECT DISTINCT user_id,CAST(timezone('Asia/Shanghai',started_at) AS DATE) FROM sessions"
    with duckdb.connect(str(root/'diagnosis-data/public/snapshot.duckdb'), read_only=True) as db:
        users = db.execute(users_sql).fetchall()
        active = set(db.execute(sessions_sql).fetchall())
    reference = []
    for period,start,end in [('previous','2026-01-01','2026-01-08'), ('current','2026-01-08','2026-01-15')]:
        for system in ['Android','iOS']:
            group = [(uid,day) for uid,day,system_name in users if start<=str(day)<end and system_name==system]
            retained = sum((uid,day+timedelta(days=1)) in active for uid,day in group)
            reference.append({'period':period, 'registration_os':system, 'users':len(group), 'retained':retained, 'retention_rate':retained/len(group)})
    checked = 0
    checked_groups: set[tuple[str, str]] = set()
    for evidence in states['diagnosis']['evidence']:
        if evidence['parameters'].get('kind')=='system_retention':
            for row in evidence['rows']:
                match = next(r for r in reference if r['period']==row['period'] and r['registration_os']==row['registration_os'])
                expected_window = ('2026-01-01','2026-01-08') if row['period']=='previous' else ('2026-01-08','2026-01-15')
                assert (row['window_start'], row['window_end']) == expected_window
                for key in ('users','retained','retention_rate'):
                    assert abs(row[key]-match[key])<1e-10
                checked += 1
                checked_groups.add((row['period'], row['registration_os']))
    assert checked_groups == {(row['period'], row['registration_os']) for row in reference}, 'Expected all four independent system-retention groups'
    return {'query_sql':count_sql, 'query_users':count, 'users_sql':users_sql, 'sessions_sql':sessions_sql, 'system_reference':reference, 'checked_rows':checked}


def run(root: Path) -> dict[str, Any]:
    tasks: dict[str, str] = {}; reports = {}; checked_cells = {}; errors: list[str] = []
    question = '用户表现有什么变化？'
    answers = ['新增用户自然日次日留存，重点比较 Android 和 iOS 的变化', '2026-01-01 至 2026-01-08（结束日不包含）']
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel=os.environ.get('METRICGUARD_BROWSER_CHANNEL','msedge'), headless=True)
        try:
            with server(root) as origin:
                token = api(origin, '/api/config')['token']
                page = browser.new_page(viewport={'width':1360,'height':1000}); page.on('pageerror', lambda error:errors.append(str(error)))
                page.goto(origin)
                page.get_by_label('数据快照').select_option('diagnosis')
                page.get_by_label('分析问题').fill(question)
                page.get_by_label('开始日期（包含）', exact=True).fill('2026-01-08')
                page.get_by_label('结束日期（不包含）', exact=True).fill('2026-01-15')
                page.get_by_role('button', name='开始分析', exact=True).click()
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                tasks['diagnosis'] = page.url.split('task=')[1]
                page.screenshot(path=str(root/'waiting.png'), full_page=True)
                page.get_by_role('button', name='新建问题', exact=True).click()
                page.get_by_role('button', name='填入开发示例', exact=True).click()
                page.get_by_role('button', name='开始分析', exact=True).dblclick()
                page.wait_for_url('**/?task=*'); tasks['query'] = page.url.split('task=')[1]
                query_url = page.url; page.close()
                page = browser.new_page(viewport={'width':1360,'height':1000}); page.on('pageerror', lambda error:errors.append(str(error)))
                page.goto(query_url)
                expect(page.locator('#status')).to_have_text('已结束', timeout=180000)
                expect(page.locator('#report-overview')).to_contain_text('1680 人')
                reports['query'] = api(origin, '/api/tasks/'+tasks['query']+'/report', token)
                checked_cells['query'] = inspect_report(page, root, 'query', reports['query'])
                assert len(api(origin, '/api/tasks', token)['tasks']) == 2
                page.close()
            before = inspect_tasks(root, tasks)
            assert before['diagnosis']['status']=='waiting' and before['diagnosis']['model_calls']==0
            (root/'before-restart.json').write_text(json.dumps(before, ensure_ascii=False, indent=2), encoding='utf-8')
            with server(root) as origin:
                token = api(origin, '/api/config')['token']
                page = browser.new_page(viewport={'width':1360,'height':1000}); page.on('pageerror', lambda error:errors.append(str(error)))
                page.goto(origin)
                expect(page.locator('#history-list a')).to_have_count(2)
                page.get_by_role('link', name=question, exact=True).click()
                expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                assert page.url.endswith(tasks['diagnosis'])
                page.get_by_label('你的回答').fill(answers[0])
                page.get_by_role('button', name='提交回答', exact=True).click()
                expect(page.locator('#clarification-prompt')).to_contain_text('比较基期')
                page.reload(); expect(page.locator('#clarification-prompt')).to_contain_text('比较基期')
                page.screenshot(path=str(root/'clarification.png'), full_page=True)
                page.get_by_role('button', name=answers[1], exact=True).click()
                page.get_by_role('button', name='提交回答', exact=True).click()
                expect(page.locator('#status')).to_have_text('已结束', timeout=180000)
                reports['diagnosis'] = api(origin, '/api/tasks/'+tasks['diagnosis']+'/report', token)
                checked_cells['diagnosis'] = inspect_report(page, root, 'diagnosis', reports['diagnosis'])
                assert api(origin, '/api/tasks/'+tasks['query']+'/report', token)==reports['query']
                assert os.environ['ANTHROPIC_AUTH_TOKEN'] not in page.content()
                page.close()
            states = inspect_tasks(root, tasks)
        finally:
            browser.close()
    assert not errors
    assert states['query']==before['query']
    diagnosis = states['diagnosis']
    assert diagnosis['time_anchor']==before['diagnosis']['time_anchor'] and diagnosis['limits']==before['diagnosis']['limits']
    assert len(diagnosis['answers'])==2 and diagnosis['actual_window']==['2026-01-08','2026-01-15']
    assert diagnosis['comparison_window']==['2026-01-01','2026-01-08']
    assert diagnosis['analysis_result'] in ('supported_descriptive_candidate','no_supported_candidate')
    for name,report in reports.items():
        sources = {e['evidence_id']:e for e in states[name]['evidence']}
        for fact in report['facts']:
            ref = fact['reference']
            assert sources[ref['evidence_id']]['rows'][ref['row']][ref['column']]==fact['value']
    return {'passed':True, 'artifact':str(root), 'tasks':states, 'reports':reports, 'answers':answers, 'before_restart':before,
            'independent_reference':reference_checks(root, states), 'checked_browser_cells':checked_cells,
            'page_errors':errors, 'restart':'external process termination while waiting/ended; no active model call',
            'verification':'real model + actual Docker + automatic Edge browser; user experience not claimed'}


def main() -> None:
    if not os.environ.get('ANTHROPIC_AUTH_TOKEN') or not os.environ.get('METRICGUARD_TEST_IMAGE'):
        raise SystemExit('Configure ANTHROPIC_AUTH_TOKEN and METRICGUARD_TEST_IMAGE before live acceptance.')
    root = (Path('artifacts/u6-live')/uuid4().hex).resolve(); root.mkdir(parents=True)
    print('验收记录目录：'+str(root), flush=True)
    try:
        result = run(root)
    except Exception as error:
        message = str(error).replace(os.environ['ANTHROPIC_AUTH_TOKEN'], '[redacted]')
        (root/'failure.json').write_text(json.dumps({'passed':False, 'error_type':type(error).__name__, 'message':message}, ensure_ascii=False, indent=2), encoding='utf-8')
        raise
    files = [*Path('metricguard').glob('*.py'), *Path('metricguard/web_assets').glob('*'), Path(__file__), Path('experiments/u6_manual.py')]
    result['source_sha256'] = {str(path):hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    raw = json.dumps(result, ensure_ascii=False, indent=2)
    assert os.environ['ANTHROPIC_AUTH_TOKEN'] not in raw
    (root/'result.json').write_text(raw, encoding='utf-8')
    print(json.dumps({'passed':True, 'artifact':str(root), 'tasks':{name:state['id'] for name,state in result['tasks'].items()}}, ensure_ascii=False))


if __name__ == '__main__':
    main()
