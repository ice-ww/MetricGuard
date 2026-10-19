"""Answer operations at the approved public HTTP seam."""
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_u1_web import request, wait_done
from tests.test_t09_service import image


def answer_payload(state, answer, key='answer-0001'):
    pending=state['clarification']
    return {'request_id':key,'question_id':pending['question_id'],'version':pending['version'],'answer':answer}


def test_answer_is_persistent_deduplicated_and_versioned(tmp_path):
    snapshot=tmp_path/'snapshot';snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app:
            _,created=request(app,'/api/tasks',{'request_id':'create-0001','question':'用户表现怎么样？','snapshot_id':'dev','window':['2026-01-08','2026-01-15']})
            task=created['id'];state=wait_done(app,task)
            assert '2026-01-08' in state['clarification']['known_information']
            payload=answer_payload(state,'留存')
            path='/api/tasks/'+task+'/answers'
            assert request(app,path,{**payload,'image':'untrusted'})[0]==400
            assert request(app,path,{**payload,'answer':' '})[0]==400
            assert request(app,path,{**payload,'version':'1'})[0]==400
            assert request(app,path,payload,Origin='https://example.com')[0]==403
            assert request(app,'/api/tasks/'+'a'*32+'/answers',payload)[0]==404
            assert request(app,path,payload)==(202,{'id':task})
            after=wait_done(app,task)
            assert '人群' in after['clarification']['prompt']
            assert request(app,path,payload)==(202,{'id':task})
            assert request(app,path,{**payload,'request_id':'answer-0002'})[0]==409
            assert request(app,path,{**payload,'answer':'观测完播率'})[0]==409
            assert len(service.inspect(task)['answers'])==1
            assert after['clarification']['version']>payload['version']
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app:
            assert request(app,path,payload)==(202,{'id':task})
            assert len(service.inspect(task)['answers'])==1


def test_busy_answer_is_not_consumed_and_racing_answers_run_once(tmp_path,image):
    import threading
    from concurrent.futures import ThreadPoolExecutor
    import httpx2 as httpx
    from experiments.t01.snapshots import build_snapshot
    from tests.test_t09_service import response
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=311002)
    entered=threading.Event();release=threading.Event();calls=[]
    def provider(req):
        calls.append(req)
        if len(calls)==1:
            entered.set();assert release.wait(30)
            return response({'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'})
        return response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]})
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='controlled',transport=httpx.MockTransport(provider)) as service:
        with LocalWeb(service) as app:
            states=[]
            for key in ['waiting-first','waiting-second']:
                _,created=request(app,'/api/tasks',{'request_id':key,'question':'用户表现怎么样？','snapshot_id':'dev','window':['2026-01-08','2026-01-15']})
                states.append(wait_done(app,created['id']))
            first,second=states;path='/api/tasks/'+first['id']+'/answers'
            barrier=threading.Barrier(2)
            def compete(key):
                payload=answer_payload(first,'新增用户数',key);barrier.wait()
                return payload,request(app,path,payload)
            try:
                with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(compete,['answer-first','answer-rival']))
                assert sorted(result[1][0] for result in results)==[202,409]
                accepted=next(p for p,r in results if r[0]==202)
                assert entered.wait(20)
                assert request(app,path,accepted)[0]==202
                other=answer_payload(second,'留存','answer-second')
                assert request(app,'/api/tasks/'+second['id']+'/answers',other)[0]==409
                untouched=service.inspect(second['id'])
                assert untouched['status']=='waiting' and untouched['answers']==[]
                assert untouched['pending_question']['question_id']==other['question_id']
            finally:release.set()
            assert '1680 人' in wait_done(app,first['id'])['body']
            assert len(calls)==2 and len(service.inspect(first['id'])['answers'])==1
            assert request(app,'/api/tasks/'+second['id']+'/answers',other)[0]==202
            assert '人群' in wait_done(app,second['id'])['clarification']['prompt']


def test_lost_checkpoint_reports_answer_failure_instead_of_waiting(tmp_path):
    snapshot=tmp_path/'snapshot';snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app:
            _,created=request(app,'/api/tasks',{'request_id':'checkpoint-0001','question':'用户表现怎么样？','snapshot_id':'dev'})
            task=created['id'];state=wait_done(app,task);payload=answer_payload(state,'留存')
            # Real storage loss at the filesystem boundary; no mocked service methods.
            (tmp_path/'state'/'analysis-checkpoints.sqlite').unlink()
            path='/api/tasks/'+task+'/answers'
            assert request(app,path,payload)[0]==202
            failed=wait_done(app,task)
            assert failed['status']=='failed' and failed['clarification'] is None
            assert '失败' in failed['body']
            assert request(app,path,payload)[0]==409


def test_interrupted_answer_is_not_replayed_after_restart(tmp_path,image):
    import json, subprocess, sys, time
    from types import SimpleNamespace
    from experiments.t01.snapshots import build_snapshot
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=311004).database
    ready=tmp_path/'ready.json';entered=tmp_path/'entered'
    script="""
import json,sys,threading
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
        _,created=request(app,'/api/tasks',{'request_id':'interrupted-0001','question':'用户表现怎么样？','snapshot_id':'dev','window':['2026-01-08','2026-01-15']})
        task=created['id'];state=wait_done(app,task);payload=answer_payload(state,'新增用户数')
        path='/api/tasks/'+task+'/answers';assert request(app,path,payload)[0]==202
        while not entered.exists() and time.monotonic()<deadline:time.sleep(.05)
        assert entered.exists()
    finally:process.terminate();process.wait(timeout=15)
    with TaskService(tmp_path/'state',image,{'dev':snapshot},token='unused') as service:
        with LocalWeb(service) as app:
            status=request(app,'/api/tasks/'+task)[1]
            assert status['status']=='interrupted' and status['clarification'] is None and status['elapsed_seconds'] is None
            before=service.inspect(task)
            assert request(app,path,payload)[0]==409
            assert request(app,path,{**payload,'request_id':'different-operation'})[0]==409
            assert service.inspect(task)==before
