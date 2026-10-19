"""Recheck saved real-model results after transport changes, without new model calls."""
import gzip,hashlib,json,os
from pathlib import Path
from playwright.sync_api import sync_playwright,expect
from metricguard import TaskService
from metricguard.web import LocalWeb


def main():
    receipt=json.loads(gzip.decompress(Path('docs/validation/u4-live.json.gz').read_bytes()))
    root=Path(receipt['artifact']);checks=[]
    with TaskService(root/'state',os.environ['METRICGUARD_TEST_IMAGE'],{'dev':root/'data/public/snapshot.duckdb'},token='read-only-no-model') as service:
        with LocalWeb(service) as app:
            with sync_playwright() as pw:
                browser=pw.chromium.launch(channel=os.environ.get('METRICGUARD_BROWSER_CHANNEL','msedge'),headless=True)
                try:
                    for item in receipt['records']:
                        task=item['task']['id'];before=service.inspect(task)
                        assert before==item['task']
                        page=browser.new_page();page.goto(app.origin+'/?task='+task)
                        expect(page.locator('#report-kind')).to_be_visible()
                        report=app.report(task);assert report==item['report']
                        page.locator('#report-overview a').first.click()
                        for fact in report['facts']:
                            page.locator('[id="fact-'+fact['assertion_id']+'"] a').click()
                            expect(page.locator('.evidence-cell:focus')).to_have_text(json.dumps(fact['value'],ensure_ascii=False,separators=(',',':')))
                        assert service.inspect(task)==before
                        checks.append({'task':task,'checked_cells':len(report['facts']),'state_unchanged':True});page.close()
                finally:browser.close()
    files=[Path('metricguard/web.py'),Path('metricguard/web_report.py'),*Path('metricguard/web_assets').glob('*')]
    result={'checks':checks,'new_model_calls':0,'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'passed':True}
    Path('docs/validation/u4/final-display-recheck.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(result['checks']))


if __name__=='__main__':main()
