"""HTTP evidence ownership and unavailable reports are observable, never file selectors."""
import json
from playwright.sync_api import sync_playwright,expect
from tests.test_u2_browser import open_browser
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_u1_web import request,wait_done


def test_report_access_is_owned_and_waiting_task_has_no_report(tmp_path):
    snapshot=tmp_path/'data';snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='secret-u4') as service:
        other=service.create('用户表现怎么样？','dev')
        with LocalWeb(service) as app:
            _,created=request(app,'/api/tasks',{'request_id':'u4-wait-0001','question':'用户表现怎么样？','snapshot_id':'dev'})
            task=created['id'];wait_done(app,task);before=service.inspect(task)
            code,result=request(app,f'/api/tasks/{task}/report')
            assert code==200 and not result['available'] and '尚无' in result['message']
            assert request(app,f'/api/tasks/{other}/report')[0]==404
            assert request(app,f'/api/tasks/{task}/report',**{'X-MetricGuard-Token':'wrong'})[0]==403
            for path in ['/api/tasks/../../AGENTS.md/report',f'/api/tasks/{task}/evidence/../../AGENTS.md',f'/api/tasks/{task}/report/C:/Windows/win.ini']:
                assert request(app,path)[0]==404
            assert request(app,f'/api/tasks/{task}/report?path=C:/Windows/win.ini')[1]==result
            assert 'secret-u4' not in json.dumps(result)
            assert service.inspect(task)==before


def test_failed_resume_does_not_present_a_success_report(tmp_path):
    snapshot=tmp_path/'data';snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='secret-u4') as service:
        with LocalWeb(service) as app:
            _,created=request(app,'/api/tasks',{'request_id':'u4-fail-0001','question':'用户表现怎么样？','snapshot_id':'dev'})
            task=created['id'];waiting=wait_done(app,task);pending=waiting['clarification']
            (tmp_path/'state'/'analysis-checkpoints.sqlite').unlink()
            code,_=request(app,f'/api/tasks/{task}/answers',{'request_id':'u4-fail-answer','question_id':pending['question_id'],'version':pending['version'],'answer':'新增用户数'})
            assert code==202
            state=wait_done(app,task);result=request(app,f'/api/tasks/{task}/report')[1]
            assert state['status']=='failed' and not result['available']
            assert '失败' in result['message']
            assert 'secret-u4' not in json.dumps(result)
            with sync_playwright() as pw:
                browser=open_browser(pw)
                try:
                    page=browser.new_page();page.goto(app.origin+'/?task='+task)
                    expect(page.locator('#status')).to_have_text('执行失败')
                    expect(page.locator('#report-view')).to_contain_text('失败')
                    expect(page.locator('#facts-details')).to_have_count(0)
                finally:browser.close()


import http.client
import time
from urllib.parse import urlsplit
import pytest


@pytest.mark.parametrize('rejection',['origin','token'])
def test_rejected_fragmented_post_returns_error_without_reset(tmp_path,rejection):
    snapshot=tmp_path/'data';snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app:
            address=urlsplit(app.origin)
            for complete in [True,True,True,False]:
                connection=http.client.HTTPConnection(address.hostname,address.port,timeout=3)
                try:
                    connection.putrequest('POST','/api/tasks')
                    connection.putheader('Origin','https://example.com' if rejection=='origin' else app.origin)
                    connection.putheader('X-MetricGuard-Token',app.token if rejection=='origin' else 'wrong')
                    connection.putheader('Content-Length','4000');connection.putheader('Content-Type','application/json')
                    connection.endheaders();connection.send(b'x'*2000)
                    if complete:
                        time.sleep(.01)  # Legal fragmentation: rejection races the final segment.
                        connection.send(b'x'*2000)
                    # Otherwise the peer stalls mid-body; the 3-second client timeout bounds the check.
                    response=connection.getresponse()
                    assert response.status==403 and 'error' in json.loads(response.read())
                finally:connection.close()
            assert request(app,'/api/tasks')[1]['tasks']==[]
