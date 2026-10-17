"""Real browser + real provider acceptance, independent business reference query."""
import gzip
import hashlib
import json
import os
from pathlib import Path
import queue
import re
import subprocess
import sys
import threading
import time
from uuid import uuid4
import duckdb
from playwright.sync_api import sync_playwright, expect
from metricguard import TaskService


def main():
    root=(Path('artifacts/u1-live')/uuid4().hex).resolve();root.mkdir(parents=True)
    state=root/'state';image=os.environ['METRICGUARD_TEST_IMAGE']
    assert os.environ.get('ANTHROPIC_AUTH_TOKEN'),'Model credentials are required'
    command=[sys.executable,'-m','metricguard.web_start','--demo','--port','0','--state-dir',str(state),'--image',image]
    process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='utf-8',
        env={**os.environ,'PYTHONUTF8':'1'},creationflags=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0)
    messages: queue.Queue[str]=queue.Queue();lines: list[str]=[]
    def read():
        assert process.stdout
        for line in process.stdout:messages.put(line)
    reader=threading.Thread(target=read,daemon=True);reader.start()
    task=None;terminal=None
    try:
        deadline=time.monotonic()+90;origin=None
        while time.monotonic()<deadline:
            try:line=messages.get(timeout=1)
            except queue.Empty:
                if process.poll() is not None:raise RuntimeError('Startup failed: '+''.join(lines))
                continue
            lines.append(line)
            match=re.search(r'http://127.0.0.1:\d+',line)
            if match:origin=match[0];break
        assert origin,'Startup did not become ready'
        with sync_playwright() as pw:
            browser=pw.chromium.launch(channel=os.environ.get('METRICGUARD_BROWSER_CHANNEL','msedge'),headless=True)
            try:
                page=browser.new_page(viewport={'width':1360,'height':900});errors=[]
                page.on('pageerror',lambda error:errors.append(str(error)))
                page.goto(origin);page.get_by_role('button',name='填入开发示例').click()
                page.get_by_label('分析问题').fill('这段时间新增用户数是多少？请给出具体人数。')
                page.get_by_role('button',name='开始分析',exact=True).click()
                page.wait_for_url('**/?task=*');task=page.url.split('task=')[1]
                expect(page.locator('#status')).to_have_text('已结束',timeout=120000)
                expect(page.locator('#result')).to_contain_text('1680 人')
                terminal=page.locator('#result').inner_text()
                page.reload();expect(page.locator('#result')).to_have_text(terminal)
                assert not errors
                page.screenshot(path=str(root/'desktop.png'),full_page=True)
                page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(root/'mobile.png'),full_page=True)
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
            finally:browser.close()
    finally:
        process.terminate();process.wait(timeout=15);reader.join(timeout=5)
        while not messages.empty():lines.append(messages.get())
        (root/'startup.txt').write_text(''.join(lines),encoding='utf-8')
    assert task and terminal
    database=root/'demo-data'/'public'/'snapshot.duckdb'
    with duckdb.connect(str(database),read_only=True) as db:
        row=db.execute("SELECT COUNT(DISTINCT user_id) FROM users WHERE registered_at>=TIMESTAMPTZ '2026-01-08 00:00:00+08:00' AND registered_at<TIMESTAMPTZ '2026-01-15 00:00:00+08:00'").fetchone()
        assert row is not None
        expected=row[0]
    with TaskService(state,image,{'demo':database},token='not-used') as service:
        task_state=service.inspect(task);exported=service.export_report(task)
    assert task_state['status']=='ended' and task_state['analysis_result']=='facts_available'
    assert f'新增用户数：{expected} 人' in terminal and exported['terminal_body']==terminal
    publication=json.loads((Path(exported['report']).parent/'publication.json').read_text(encoding='utf-8'))
    sources={e['evidence_id']:e for e in task_state['evidence']}
    for assertion in publication['assertions']:
        ref=assertion['reference'];assert sources[ref['evidence_id']]['rows'][ref['row']][ref['column']]==assertion['value']
    files=list(Path('metricguard').glob('*.py'))+list(Path('metricguard/web_assets').glob('*'))
    receipt={'task':task_state,'publication':publication,'browser_body':terminal,'reference_new_users':expected,
        'startup_output':''.join(lines),'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
        'screenshots':[str(root/'desktop.png'),str(root/'mobile.png')],'passed':True}
    encoded=json.dumps(receipt,ensure_ascii=False,indent=2)
    assert os.environ['ANTHROPIC_AUTH_TOKEN'] not in encoded
    (root/'result.json').write_text(encoded,encoding='utf-8')
    Path('docs/validation/u1-live.json.gz').write_bytes(gzip.compress(encoded.encode(),mtime=0))
    print(json.dumps({'task':task,'reference':expected,'model_calls':task_state['model_calls'],'tool_calls':task_state['tool_calls'],'artifact':str(root),'passed':True},ensure_ascii=False))


if __name__=='__main__':main()
