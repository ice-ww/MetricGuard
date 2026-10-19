"""Public local HTTP behavior; only the model provider is controlled."""
import json
import threading
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import httpx2 as httpx
from metricguard import TaskService
from metricguard.web import LocalWeb
from experiments.t01.snapshots import build_snapshot
from tests.test_t09_service import image, response


def request(app, path, payload=None, **headers):
    headers = {'X-MetricGuard-Token': app.token, **headers}
    if payload is not None:
        headers['Content-Type'] = 'application/json'
    req = Request(app.origin + path, data=json.dumps(payload).encode() if payload is not None else None, headers=headers)
    try:
        with urlopen(req, timeout=5) as result:
            return result.status, json.load(result)
    except HTTPError as error:
        return error.code, json.load(error)


def wait_done(app, task):
    deadline = time.monotonic() + 60
    while time.monotonic() < deadline:
        code, state = request(app, '/api/tasks/' + task)
        assert code == 200
        if state['status'] not in ('created','running'):
            return state
        time.sleep(.1)
    raise AssertionError('task did not finish')


def test_one_execution_and_durable_duplicate_submission(tmp_path, image):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=301001)
    entered = threading.Event(); release = threading.Event(); calls = []
    def provider(req):
        calls.append(req)
        if len(calls) == 1:
            entered.set()
            assert release.wait(30)
            return response({'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'})
        return response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]})
    body = {'request_id':'operation-0001','question':'查询新增用户数','snapshot_id':'dev','window':['2026-01-08','2026-01-15']}
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='private-token',transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service) as app:
            try:
                from concurrent.futures import ThreadPoolExecutor
                barrier=threading.Barrier(2)
                candidates=[body,{**body,'request_id':'operation-rival'}]
                def compete(candidate):
                    barrier.wait()
                    return candidate,request(app,'/api/tasks',candidate)
                with ThreadPoolExecutor(max_workers=2) as pool:
                    results=list(pool.map(compete,candidates))
                assert sorted(result[1][0] for result in results)==[202,409]
                body,(code,first)=next(result for result in results if result[1][0]==202)
                task = first['id']
                assert entered.wait(20)
                assert request(app,'/api/tasks',body)[1]['id'] == task
                assert request(app,'/api/tasks',{**body,'request_id':'operation-0002'})[0] == 409
                code, state = request(app,'/api/tasks/'+task)
                assert code == 200 and state['status'] == 'running'
                assert 'private-token' not in json.dumps(state)
            finally:
                release.set()
            finished = wait_done(app,task)
            assert '1680 人' in finished['body']
            assert len(calls) == 2
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='unused') as service:
        with LocalWeb(service) as app:
            assert request(app,'/api/tasks',body)[1]['id'] == task
            assert service.inspect(task)['model_calls'] == 2


def test_startup_rejects_missing_credentials_without_leaking_configuration(tmp_path):
    import os
    import subprocess
    import sys
    result = subprocess.run([sys.executable,'-m','metricguard.web_start','--demo','--state-dir',str(tmp_path/'state')],
        env={**os.environ,'ANTHROPIC_AUTH_TOKEN':''},capture_output=True,text=True,encoding='utf-8',timeout=30)
    assert result.returncode != 0
    assert 'ANTHROPIC_AUTH_TOKEN' in result.stderr and '请' in result.stderr
    assert not (tmp_path/'state').exists()


def test_public_transport_rejects_untrusted_requests_and_invalid_inputs(tmp_path):
    snapshot=tmp_path/'dummy.duckdb';snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='secret-not-public') as service:
        with LocalWeb(service) as app:
            body={'request_id':'invalid-0001','question':'查询新增用户数','snapshot_id':'dev'}
            assert request(app,'/api/tasks',body,Origin='https://example.com')[0]==403
            assert request(app,'/api/config',Host='evil.example')[0]==403
            assert request(app,'/api/tasks',body,**{'X-MetricGuard-Token':'wrong'})[0]==403
            assert request(app,'/api/tasks',{**body,'snapshot_id':'C:/secret.duckdb'})[0]==400
            assert request(app,'/api/tasks',{**body,'image':'evil'})[0]==400
            assert request(app,'/api/tasks',{**body,'window':['2026-01-08','2026-01-01']})[0]==400
            assert request(app,'/api/tasks',{**body,'window':[1,2]})[0]==400
            assert request(app,'/api/tasks/'+'a'*32)[0]==404
            assert request(app,'/../../secret')[0]==404
            assert 'secret-not-public' not in json.dumps(request(app,'/api/config')[1])


def test_waiting_releases_execution_slot_and_changed_retry_is_rejected(tmp_path):
    snapshot=tmp_path/'dummy.duckdb';snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app:
            body={'request_id':'waiting-0001','question':'用户表现怎么样？','snapshot_id':'dev','window':['2026-01-08','2026-01-15']}
            code, first=request(app,'/api/tasks',body)
            assert code==202
            state=wait_done(app,first['id'])
            assert state['status']=='waiting' and state['pending']
            assert request(app,'/api/tasks',{**body,'question':'另一问题'})[0]==409
            code,second=request(app,'/api/tasks',{**body,'request_id':'waiting-0002'})
            assert code==202 and second['id']!=first['id']
            assert wait_done(app,second['id'])['status']=='waiting'


def test_startup_validates_admin_model_endpoint_before_running(tmp_path):
    import os, subprocess, sys
    result=subprocess.run([sys.executable,'-m','metricguard.web_start','--demo','--base-url','invalid-address','--state-dir',str(tmp_path/'state')],
        env={**os.environ,'ANTHROPIC_AUTH_TOKEN':'private','METRICGUARD_TEST_IMAGE':'sha256:'+'a'*64},
        capture_output=True,text=True,encoding='utf-8',timeout=30)
    assert result.returncode!=0
    assert '模型服务地址必须' in result.stderr
    assert 'private' not in result.stderr
    assert not (tmp_path/'state').exists()


def test_interrupted_task_does_not_count_server_downtime(tmp_path, image):
    import subprocess, sys
    from types import SimpleNamespace
    snapshot=build_snapshot(tmp_path/'crash-data',scenario='normal',seed=301002).database
    ready=tmp_path/'ready.json';entered=tmp_path/'entered'
    script="""
import json, sys, threading
from pathlib import Path
import httpx2 as httpx
from metricguard import TaskService
from metricguard.web import LocalWeb
root=Path(sys.argv[1])
def provider(request):
    (root/'entered').write_text('entered')
    threading.Event().wait(60)
with TaskService(root/'state',sys.argv[2],{'dev':Path(sys.argv[3])},token='controlled',transport=httpx.MockTransport(provider)) as service:
    with LocalWeb(service) as app:
        (root/'ready.json').write_text(json.dumps({'origin':app.origin,'token':app.token}))
        threading.Event().wait(60)
"""
    process=subprocess.Popen([sys.executable,'-c',script,str(tmp_path),image,str(snapshot)],creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
    try:
        deadline=time.monotonic()+30
        while not ready.exists() and time.monotonic()<deadline:
            assert process.poll() is None
            time.sleep(.05)
        app=SimpleNamespace(**json.loads(ready.read_text()))
        code,result=request(app,'/api/tasks',{'request_id':'crash-0001','question':'查询新增用户数','snapshot_id':'dev','window':['2026-01-08','2026-01-15']})
        assert code==202
        while not entered.exists() and time.monotonic()<deadline:time.sleep(.05)
        assert entered.exists()
    finally:
        process.terminate();process.wait(timeout=15)
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='unused') as service:
        with LocalWeb(service) as app:
            code,state=request(app,'/api/tasks/'+result['id'])
            assert code==200 and state['status']=='interrupted'
            assert state['elapsed_seconds'] is None
