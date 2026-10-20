"""Actual same-address service restart, without replacing the browser page."""
import json
import os
import subprocess
import sys
import time
from types import SimpleNamespace
import pytest
from playwright.sync_api import sync_playwright, expect
from experiments.t01.snapshots import build_snapshot
from tests.test_t09_service import image
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser


def start(root,database,image,port=0,mode='normal'):
    child=subprocess.Popen([sys.executable,'-m','tests.u10_restart_worker',str(root),str(database),image,str(port),mode],
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8',
        env={**os.environ,'PYTHONUTF8':'1'})
    ready=child.stdout.readline()
    assert ready, child.communicate(timeout=10)
    return child,SimpleNamespace(**json.loads(ready))


def inspect(child,task):
    child.stdin.write(task+'\n'); child.stdin.flush()
    return json.loads(child.stdout.readline())


@pytest.mark.parametrize('kind',['waiting','ended','interrupted'])
def test_same_address_restart_reconciles_original_task_without_replay(tmp_path,image,kind):
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=401001)
    child,app=start(tmp_path,snapshot.database,image,mode='block' if kind=='interrupted' else 'normal')
    with sync_playwright() as pw:
        browser=open_browser(pw)
        try:
            payload={'request_id':'restart-'+kind,'question':'用户表现怎么样？','snapshot_id':'dev'}
            if kind!='waiting':
                payload.update(question='查询新增用户数',window=['2026-01-08','2026-01-15'])
            _,created=request(app,'/api/tasks',payload); task=created['id']
            if kind=='interrupted':
                deadline=time.monotonic()+60
                while not (tmp_path/'blocked').exists() and time.monotonic()<deadline:
                    time.sleep(.05)
                assert (tmp_path/'blocked').exists()
            else:
                assert wait_done(app,task)['status']==kind
            before=inspect(child,task)
            report=request(app,'/api/tasks/'+task+'/report')[1] if kind=='ended' else None
            page=browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
            page.goto(app.origin+'/?task='+task)
            expect(page.locator('#status')).to_have_text({'waiting':'等待澄清','ended':'已结束','interrupted':'正在分析'}[kind])
            if kind=='waiting': page.get_by_label('你的回答').fill('重启后继续编辑的草稿')
            child.kill(); child.communicate(timeout=10)
            page.get_by_role('button',name='刷新任务',exact=True).click()
            expect(page.locator('#connection')).to_contain_text('可能过期')
            marker=(tmp_path/'provider.jsonl').read_bytes() if (tmp_path/'provider.jsonl').exists() else b''
            old_token=app.token
            child,app=start(tmp_path,snapshot.database,image,port=int(app.origin.rsplit(':',1)[1]))
            assert app.token!=old_token
            writes=[]
            page.on('request',lambda req:writes.append(req) if req.method=='POST' else None)
            page.get_by_role('button',name='立即重连',exact=True).click()
            expect(page.locator('#connection')).to_contain_text('连接正常')
            expect(page.locator('#status')).to_have_text({'waiting':'等待澄清','ended':'已结束','interrupted':'已中断'}[kind])
            assert page.url.endswith(task)
            if kind=='waiting': expect(page.get_by_label('你的回答')).to_have_value('重启后继续编辑的草稿')
            after=inspect(child,task)
            for key in ('model_calls','tool_calls','evidence','answers'):
                assert after[key]==before[key]
            if kind=='ended': assert request(app,'/api/tasks/'+task+'/report')[1]==report
            if kind=='interrupted':
                expect(page.locator('#recovery-message')).to_contain_text('不会自动重放')
                assert any(call['state']=='unknown' for call in after['attempts'])
            page.clock.run_for(15000); page.wait_for_timeout(50)
            assert inspect(child,task)==after and writes==[]
            assert ((tmp_path/'provider.jsonl').read_bytes() if (tmp_path/'provider.jsonl').exists() else b'')==marker
        finally:
            browser.close()
            if child.poll() is None: child.kill()
            child.communicate(timeout=10)
