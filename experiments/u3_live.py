"""Real model, browser history and graceful service restart; not a human cross-day test."""
import gzip,hashlib,json,os
from pathlib import Path
from uuid import uuid4
import duckdb
from playwright.sync_api import sync_playwright,expect
from metricguard import TaskService
from metricguard.web import LocalWeb
from experiments.t01.snapshots import build_snapshot


def main():
    root=(Path('artifacts/u3-live')/uuid4().hex).resolve();root.mkdir(parents=True)
    snapshot=build_snapshot(root/'data',scenario='normal',seed=321100)
    image=os.environ['METRICGUARD_TEST_IMAGE'];token=os.environ['ANTHROPIC_AUTH_TOKEN']
    with sync_playwright() as pw:
        with TaskService(root/'state',image,{'dev':snapshot.database},token=token) as service:
            with LocalWeb(service,example={'snapshot_id':'dev','question':'用户表现怎么样？','window':['2026-01-08','2026-01-15']}) as app:
                browser=pw.chromium.launch(channel=os.environ.get('METRICGUARD_BROWSER_CHANNEL','msedge'),headless=True)
                try:
                    page=browser.new_page();page.goto(app.origin)
                    page.get_by_role('button',name='填入开发示例').click()
                    page.get_by_role('button',name='开始分析',exact=True).click()
                    expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                    task=page.url.split('task=')[1];before=service.inspect(task)
                finally:browser.close()
        # Both the HTTP owner and TaskService close normally, then reopen the same directory.
        with TaskService(root/'state',image,{'dev':snapshot.database},token=token) as service:
            with LocalWeb(service) as app:
                browser=pw.chromium.launch(channel=os.environ.get('METRICGUARD_BROWSER_CHANNEL','msedge'),headless=True)
                try:
                    page=browser.new_page(viewport={'width':1360,'height':1000});page.goto(app.origin)
                    expect(page.locator('#history-list a')).to_have_count(1)
                    page.screenshot(path=str(root/'history.png'),full_page=True)
                    page.get_by_role('link',name='用户表现怎么样？',exact=True).click()
                    expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                    assert page.url.endswith(task) and service.inspect(task)==before
                    page.get_by_label('你的回答').fill('新增用户数')
                    page.get_by_role('button',name='提交回答',exact=True).click()
                    expect(page.locator('#status')).to_have_text('已结束',timeout=120000)
                    terminal=page.locator('#result').inner_text();after=service.inspect(task)
                    page.get_by_role('button',name='刷新列表',exact=True).click()
                    expect(page.locator('#history-list li')).to_contain_text('已结束')
                    page.get_by_role('link',name='用户表现怎么样？',exact=True).click()
                    expect(page.locator('#result')).to_have_text(terminal)
                    assert service.inspect(task)==after
                    page.screenshot(path=str(root/'result.png'),full_page=True)
                    page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                    page.screenshot(path=str(root/'mobile.png'),full_page=True)
                    exported=service.export_report(task)
                finally:browser.close()
    with duckdb.connect(str(snapshot.database),read_only=True) as db:
        row=db.execute("SELECT COUNT(DISTINCT user_id) FROM users WHERE registered_at>=TIMESTAMPTZ '2026-01-08 00:00:00+08:00' AND registered_at<TIMESTAMPTZ '2026-01-15 00:00:00+08:00'").fetchone()
        assert row is not None;expected=row[0]
    assert after['analysis_result']=='facts_available' and f'新增用户数：{expected} 人' in terminal
    assert after['time_anchor']==before['time_anchor'] and after['limits']==before['limits']
    publication=json.loads((Path(exported['report']).parent/'publication.json').read_text(encoding='utf-8'))
    sources={e['evidence_id']:e for e in after['evidence']}
    for assertion in publication['assertions']:
        ref=assertion['reference'];assert sources[ref['evidence_id']]['rows'][ref['row']][ref['column']]==assertion['value']
    files=[Path('metricguard/web.py'),*Path('metricguard/web_assets').glob('*')]
    receipt={'before_restart':before,'result':after,'publication':publication,'reference':expected,'body':terminal,'artifact':str(root),'passed':True,
             'restart_kind':'graceful HTTP and TaskService lifecycle; same-day real model','source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    raw=json.dumps(receipt,ensure_ascii=False,indent=2);assert token not in raw
    (root/'result.json').write_text(raw,encoding='utf-8');Path('docs/validation/u3-live.json.gz').write_bytes(gzip.compress(raw.encode(),mtime=0))
    print(json.dumps({'task':task,'reference':expected,'model_calls':after['model_calls'],'artifact':str(root),'passed':True},ensure_ascii=False))


if __name__=='__main__':main()
