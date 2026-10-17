"""Real model/browser clarification diagnosis with independent source-data checks."""
from datetime import timedelta
import gzip, hashlib, json, os
from pathlib import Path
from uuid import uuid4
import duckdb
from playwright.sync_api import sync_playwright, expect
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from metricguard.web import LocalWeb


def main():
    root=(Path('artifacts/u2-live')/uuid4().hex).resolve();root.mkdir(parents=True)
    snapshot=build_snapshot(root/'data',scenario='A4',seed=311100)
    image=os.environ['METRICGUARD_TEST_IMAGE'];token=os.environ['ANTHROPIC_AUTH_TOKEN']
    question='用户表现有什么变化？'
    with TaskService(root/'state',image,{'dev':snapshot.database},token=token) as service:
        with LocalWeb(service,example={'snapshot_id':'dev','question':question,'window':['2026-01-08','2026-01-15']}) as app:
            with sync_playwright() as pw:
                browser=pw.chromium.launch(channel=os.environ.get('METRICGUARD_BROWSER_CHANNEL','msedge'),headless=True)
                try:
                    page=browser.new_page(viewport={'width':1360,'height':1000});page.goto(app.origin)
                    page.get_by_role('button',name='填入开发示例').click()
                    page.get_by_role('button',name='开始分析',exact=True).click()
                    expect(page.locator('#clarification-prompt')).to_contain_text('哪个指标')
                    task=page.url.split('task=')[1]
                    page.get_by_label('你的回答').fill('新增用户自然日次日留存，重点比较 Android 和 iOS 的变化')
                    page.get_by_role('button',name='提交回答',exact=True).click()
                    expect(page.locator('#clarification-prompt')).to_contain_text('比较基期')
                    page.screenshot(path=str(root/'clarification.png'),full_page=True)
                    page.reload();expect(page.locator('#clarification-prompt')).to_contain_text('比较基期')
                    page.get_by_role('button',name='2026-01-01 至 2026-01-08（结束日不包含）',exact=True).click()
                    page.get_by_role('button',name='提交回答',exact=True).click()
                    expect(page.locator('#status')).to_have_text('已结束',timeout=180000)
                    terminal=page.locator('#result').inner_text();assert terminal
                    page.screenshot(path=str(root/'result.png'),full_page=True)
                    page.set_viewport_size({'width':390,'height':844})
                    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
                    page.screenshot(path=str(root/'mobile.png'),full_page=True)
                    state=service.inspect(task);export=service.export_report(task)
                finally:browser.close()
    assert len(state['answers'])==2 and state['actual_window']==['2026-01-08','2026-01-15']
    assert state['comparison_window']==['2026-01-01','2026-01-08']
    assert state['analysis_result'] in ('supported_descriptive_candidate','no_supported_candidate')
    publication=json.loads((Path(export['report']).parent/'publication.json').read_text(encoding='utf-8'))
    with duckdb.connect(str(snapshot.database),read_only=True) as db:
        users=db.execute("SELECT user_id, CAST(timezone('Asia/Shanghai',registered_at) AS DATE), registration_os FROM users").fetchall()
        active=set(db.execute("SELECT DISTINCT user_id, CAST(timezone('Asia/Shanghai',started_at) AS DATE) FROM sessions").fetchall())
    reference=[]
    for period,start,end in [('previous','2026-01-01','2026-01-08'),('current','2026-01-08','2026-01-15')]:
        for system in ['Android','iOS']:
            group=[(uid,day) for uid,day,os_name in users if start<=str(day)<end and os_name==system]
            retained=sum((uid,day+timedelta(days=1)) in active for uid,day in group)
            reference.append({'period':period,'registration_os':system,'users':len(group),'retained':retained,'retention_rate':retained/len(group)})
    checked=0
    for evidence in state['evidence']:
        if evidence['parameters'].get('kind')=='system_retention':
            for row in evidence['rows']:
                match=next(r for r in reference if r['period']==row['period'] and r['registration_os']==row['registration_os'])
                for field in ('users','retained','retention_rate'):assert abs(row[field]-match[field])<1e-10
                checked+=1
    assert checked>=4,'Expected independent system-retention comparison was not queried'
    sources={e['evidence_id']:e for e in state['evidence']}
    for assertion in publication['assertions']:
        ref=assertion['reference'];assert sources[ref['evidence_id']]['rows'][ref['row']][ref['column']]==assertion['value']
    receipt={'task':state,'publication':publication,'browser_body':terminal,'reference':reference,'checked_rows':checked,
             'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path('metricguard/web.py'),*Path('metricguard/web_assets').glob('*')]},
             'artifact':str(root),'passed':True}
    raw=json.dumps(receipt,ensure_ascii=False,indent=2);assert token not in raw
    (root/'result.json').write_text(raw,encoding='utf-8')
    Path('docs/validation/u2-live.json.gz').write_bytes(gzip.compress(raw.encode(),mtime=0))
    print(json.dumps({'task':task,'analysis_result':state['analysis_result'],'model_calls':state['model_calls'],'checked_rows':checked,'artifact':str(root),'passed':True},ensure_ascii=False))


if __name__=='__main__':main()
