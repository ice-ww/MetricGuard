"""Real model/browser report navigation with independent raw-data references."""
from datetime import timedelta
import gzip,hashlib,json,os
from pathlib import Path
from uuid import uuid4
import duckdb
from playwright.sync_api import sync_playwright,expect
from metricguard import TaskService
from metricguard.web import LocalWeb
from experiments.t01.snapshots import build_snapshot


def main():
    root=(Path('artifacts/u4-live')/uuid4().hex).resolve();root.mkdir(parents=True)
    snapshot=build_snapshot(root/'data',scenario='A4',seed=331100)
    token=os.environ['ANTHROPIC_AUTH_TOKEN'];records=[]
    with duckdb.connect(str(snapshot.database),read_only=True) as db:
        count_row=db.execute("SELECT COUNT(DISTINCT user_id) FROM users WHERE registered_at>=TIMESTAMPTZ '2026-01-08 00:00:00+08:00' AND registered_at<TIMESTAMPTZ '2026-01-15 00:00:00+08:00'").fetchone()
        assert count_row is not None
        count=count_row[0]
        users=db.execute("SELECT user_id,CAST(timezone('Asia/Shanghai',registered_at) AS DATE),registration_os FROM users").fetchall()
        active=set(db.execute("SELECT DISTINCT user_id,CAST(timezone('Asia/Shanghai',started_at) AS DATE) FROM sessions").fetchall())
    with TaskService(root/'state',os.environ['METRICGUARD_TEST_IMAGE'],{'dev':snapshot.database},token=token) as service:
        with LocalWeb(service) as app:
            with sync_playwright() as pw:
                browser=pw.chromium.launch(channel=os.environ.get('METRICGUARD_BROWSER_CHANNEL','msedge'),headless=True)
                try:
                    for case,question in [('query','查询新增用户数'),('diagnosis','分析新增用户自然日次日留存变化，比较 Android 与 iOS 的留存和构成')]:
                        page=browser.new_page(viewport={'width':1360,'height':1000});page.goto(app.origin)
                        page.get_by_label('分析问题').fill(question)
                        page.get_by_label('开始日期（包含）',exact=True).fill('2026-01-08');page.get_by_label('结束日期（不包含）',exact=True).fill('2026-01-15')
                        if case=='diagnosis':
                            page.get_by_text('指定比较基期（可选）',exact=True).click()
                            page.get_by_label('基期开始（包含）').fill('2026-01-01');page.get_by_label('基期结束（不包含）').fill('2026-01-08')
                        page.get_by_role('button',name='开始分析',exact=True).click()
                        expect(page.locator('#status')).to_have_text('已结束',timeout=180000)
                        expect(page.locator('#report-kind')).to_be_visible()
                        task=page.url.split('task=')[1];state=service.inspect(task);report=app.report(task)
                        assert report['available'] and report['facts']
                        page.screenshot(path=str(root/(case+'.png')),full_page=True)
                        if case=='query':
                            assert state['analysis_result']=='facts_available'
                            expect(page.locator('#report-overview')).to_contain_text(f'新增用户数：{count} 人')
                        else:assert state['analysis_result']=='supported_descriptive_candidate'
                        page.locator('#report-overview a').first.click();expect(page.locator('.fact-row:focus')).to_be_visible()
                        page.locator('.fact-row:focus a').click();expect(page.locator('.evidence-cell:focus')).to_be_visible()
                        page.screenshot(path=str(root/(case+'-evidence.png')),full_page=True)
                        checked=0;reference=[]
                        for evidence in state['evidence']:
                            if evidence['parameters'].get('kind')=='system_retention':
                                for row in evidence['rows']:
                                    group=[(uid,day) for uid,day,system in users if row['window_start']<=str(day)<row['window_end'] and system==row['registration_os']]
                                    retained=sum((uid,day+timedelta(days=1)) in active for uid,day in group)
                                    assert (row['users'],row['retained'])==(len(group),retained)
                                    assert abs(row['retention_rate']-retained/len(group))<1e-12
                                    reference.append({'period':row['period'],'system':row['registration_os'],'users':len(group),'retained':retained});checked+=1
                        if case=='diagnosis':assert checked>=4
                        for fact in report['facts']:
                            page.locator('[id="fact-'+fact['assertion_id']+'"] a').click()
                            expect(page.locator('.evidence-cell:focus')).to_have_text(json.dumps(fact['value'],ensure_ascii=False,separators=(',',':')))
                        assert service.inspect(task)==state
                        page.reload();expect(page.locator('#report-kind')).to_be_visible()
                        page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                        page.screenshot(path=str(root/(case+'-mobile.png')),full_page=True)
                        records.append({'case':case,'task':state,'report':report,'reference':reference,'count_reference':count,'checked_cells':len(report['facts'])})
                        page.close()
                finally:browser.close()
    files=[Path('metricguard/web.py'),Path('metricguard/web_report.py'),*Path('metricguard/web_assets').glob('*')]
    receipt={'records':records,'artifact':str(root),'passed':True,'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    raw=json.dumps(receipt,ensure_ascii=False,indent=2);assert token not in raw
    (root/'result.json').write_text(raw,encoding='utf-8');Path('docs/validation/u4-live.json.gz').write_bytes(gzip.compress(raw.encode(),mtime=0))
    print(json.dumps({'tasks':[r['task']['id'] for r in records],'artifact':str(root),'passed':True},ensure_ascii=False))


if __name__=='__main__':main()
