"""History through public HTTP and actual persistence."""
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_u1_web import request,wait_done


def test_history_only_lists_web_tasks_in_its_directory_without_mutation(tmp_path):
    snapshot=tmp_path/'snapshot';snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        other=service.create('旧终端任务','dev')
        with LocalWeb(service) as app:
            assert request(app,'/api/tasks')==(200,{'tasks':[]})
            assert request(app,'/api/tasks',**{'X-MetricGuard-Token':'wrong'})[0]==403
            ids=[]
            for index in range(2):
                _,result=request(app,'/api/tasks',{'request_id':f'history-{index}','question':'用户表现怎么样？','snapshot_id':'dev'})
                ids.append(result['id']);wait_done(app,result['id'])
            before=[service.inspect(task) for task in ids]
            code,result=request(app,'/api/tasks')
            assert code==200 and [t['id'] for t in result['tasks']]==ids[::-1]
            assert all(t['status']=='waiting' for t in result['tasks'])
            assert all(set(t)=={'id','question','snapshot_id','status','window'} for t in result['tasks'])
            assert other not in str(result)
            assert [service.inspect(task) for task in ids]==before
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app:
            assert request(app,'/api/tasks')[1]==result
    with TaskService(tmp_path/'separate','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app:
            assert request(app,'/api/tasks')==(200,{'tasks':[]})
            assert request(app,'/api/tasks/'+ids[0])[0]==404
