"""Recovery and rerun through the public HTTP boundary and real persistence."""
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_u1_web import request, wait_done
import threading
import httpx2 as httpx
from experiments.t01.snapshots import build_snapshot
from tests.test_t09_service import image, response


def test_failed_answer_can_rerun_once_without_changing_original(tmp_path):
    snapshot = tmp_path / 'data'
    snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state', 'unused', {'dev': snapshot}, token='private-u5') as service:
        with LocalWeb(service) as app:
            _, created = request(app, '/api/tasks', {'request_id': 'u5-original', 'question': '用户表现怎么样？', 'snapshot_id': 'dev'})
            task = created['id']
            pending = wait_done(app, task)['clarification']
            assert request(app, f'/api/tasks/{task}/rerun', {'request_id': 'u5-too-early'})[0] == 409
            (tmp_path/'state'/'analysis-checkpoints.sqlite').unlink()
            request(app, f'/api/tasks/{task}/answers', {'request_id': 'u5-answer', 'question_id': pending['question_id'], 'version': pending['version'], 'answer': '新增用户数'})
            assert wait_done(app, task)['status'] == 'failed'
            old = service.inspect(task)
            payload = {'request_id': 'u5-rerun'}
            code, created = request(app, f'/api/tasks/{task}/rerun', payload)
            assert code == 202
            new = created['id']
            assert new != task
            wait_done(app, new)
            assert request(app, f'/api/tasks/{task}/rerun', payload) == (202, created)
            assert service.inspect(new)['parent'] == task
            assert request(app, f'/api/tasks/{new}')[1]['parent'] == task
            assert service.inspect(task) == old
            assert len(request(app, '/api/tasks')[1]['tasks']) == 2
            assert request(app, '/api/tasks', {'request_id': 'u5-rerun', 'question': '另一个问题', 'snapshot_id': 'dev'})[0] == 409
    with TaskService(tmp_path/'state', 'unused', {'dev': snapshot}, token='private-u5') as service:
        with LocalWeb(service) as app:
            assert request(app, f'/api/tasks/{task}/rerun', payload) == (202, created)
            assert service.inspect(task) == old


def test_rerun_owns_single_slot_and_rejects_foreign_tasks(tmp_path, image):
    snapshot = build_snapshot(tmp_path/'data', scenario='normal', seed=351003)
    entered = threading.Event(); release = threading.Event(); calls = []
    def provider(req):
        calls.append(req)
        if len(calls) == 1:
            raise httpx.ReadTimeout('private-u5', request=req)
        entered.set()
        assert release.wait(30)
        return response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]})
    with TaskService(tmp_path/'state', image, {'dev':snapshot.database}, token='private-u5', transport=httpx.MockTransport(provider)) as service:
        foreign = service.create('用户表现怎么样？', 'dev')
        with LocalWeb(service) as app:
            _, created = request(app, '/api/tasks', {'request_id':'u5-busy-original','question':'查询新增用户数','snapshot_id':'dev','window':['2026-01-08','2026-01-15']})
            task = created['id']; wait_done(app, task)
            payload = {'request_id':'u5-busy-rerun'}
            assert request(app, f'/api/tasks/{foreign}/rerun', payload)[0] == 404
            assert request(app, f'/api/tasks/{task}/rerun', payload, **{'X-MetricGuard-Token':'wrong'})[0] == 403
            assert request(app, f'/api/tasks/{task}/rerun', {**payload,'question':'changed'})[0] == 400
            try:
                code, result = request(app, f'/api/tasks/{task}/rerun', payload)
                assert code == 202 and entered.wait(20)
                assert request(app, f'/api/tasks/{task}/rerun', payload) == (202, result)
                assert request(app, f'/api/tasks/{task}/rerun', {'request_id':'u5-competing'})[0] == 409
                assert request(app, '/api/tasks', {'request_id':'u5-new-busy','question':'用户表现怎么样？','snapshot_id':'dev'})[0] == 409
                assert len(request(app, '/api/tasks')[1]['tasks']) == 2
            finally:
                release.set()
            wait_done(app, result['id'])
            assert len(calls) == 2
