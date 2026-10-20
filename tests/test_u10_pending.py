"""Unconfirmed writes retain identity while read-only connection recovery runs."""
import pytest
from playwright.sync_api import sync_playwright, expect
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser


@pytest.mark.parametrize('accepted',[False,True])
@pytest.mark.parametrize('edited',['后来编辑的独立草稿',''])
def test_offline_edits_stay_distinct_from_unknown_answer_and_survive_confirmation(tmp_path,accepted,edited):
    snapshot=tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled') as service:
        with LocalWeb(service) as app,sync_playwright() as pw:
            _,created=request(app,'/api/tasks',{'request_id':'separate-drafts','question':'用户表现怎么样？','snapshot_id':'dev'})
            task=created['id']; wait_done(app,task)
            browser=open_browser(pw)
            try:
                page=browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
                page.goto(app.origin+'/?task='+task)
                expect(page.locator('#status')).to_have_text('等待澄清')
                writes=[]
                def lose(route):
                    writes.append(route.request.post_data_json)
                    if accepted: route.fetch()
                    route.abort()
                page.route('**/answers',lose)
                page.get_by_label('你的回答').fill('留存')
                page.get_by_role('button',name='提交回答',exact=True).click()
                expect(page.locator('#connection')).to_contain_text('提交已暂停')
                page.get_by_label('你的回答').fill(edited)
                wait_done(app,task)
                page.get_by_role('button',name='立即重连',exact=True).click()
                expect(page.locator('#connection')).to_contain_text('连接正常')
                expect(page.locator('#unknown-answer-text')).to_have_value('留存')
                if accepted:
                    if edited: expect(page.locator('#stale-drafts textarea')).to_have_value(edited)
                else:
                    expect(page.get_by_label('你的回答')).to_have_value(edited)
                    expect(page.get_by_label('你的回答')).to_be_enabled()
                page.unroute('**/answers')
                def retry(route):
                    writes.append(route.request.post_data_json); route.continue_()
                page.route('**/answers',retry)
                page.get_by_role('button',name='重试原回答' if accepted else '重试相同回答',exact=True).click()
                expect(page.locator('#unknown-answer')).to_be_hidden()
                wait_done(app,task); page.reload()
                expect(page.locator('#unknown-answer')).to_be_hidden()
                if edited: expect(page.locator('#stale-drafts textarea')).to_have_value(edited)
                assert writes[0]==writes[1]
                assert len(service.inspect(task)['answers'])==1
            finally:
                browser.close()


@pytest.mark.parametrize('kind',['create','answer','rerun'])
def test_unknown_write_then_expired_retry_keeps_original_operation(tmp_path,kind):
    snapshot=tmp_path/'snapshot'; snapshot.write_bytes(b'not queried')
    with TaskService(tmp_path/'state','unused',{'dev':snapshot},token='controlled',
                     limits={'tool':1} if kind=='rerun' else None) as service:
        with LocalWeb(service) as app,sync_playwright() as pw:
            browser=open_browser(pw)
            try:
                page=browser.new_page(); page.clock.install(time=0); page.clock.pause_at(1000)
                task=None
                if kind=='create':
                    page.goto(app.origin)
                    page.get_by_label('分析问题').fill('用户表现怎么样？')
                    target='/api/tasks'; submit='开始分析'; retry='重试相同提交'
                else:
                    _,created=request(app,'/api/tasks',{'request_id':'pending-'+kind,
                        'question':'查询新增用户数' if kind=='rerun' else '用户表现怎么样？','snapshot_id':'dev'})
                    task=created['id']; wait_done(app,task)
                    page.goto(app.origin+'/?task='+task)
                    expect(page.locator('#status')).to_have_text('已结束' if kind=='rerun' else '等待澄清')
                    target='/api/tasks/'+task+('/rerun' if kind=='rerun' else '/answers')
                    submit='创建关联重跑' if kind=='rerun' else '提交回答'
                    retry='重试关联重跑' if kind=='rerun' else '重试原回答'
                    if kind=='answer': page.get_by_label('你的回答').fill('留存')
                writes=[]; accepted=[]
                def fault(route):
                    if route.request.method!='POST':
                        route.continue_(); return
                    writes.append(route.request.post_data_json)
                    if len(writes)==1:
                        result=route.fetch(); accepted.append(result.json()['id']); route.abort()
                    elif len(writes)==2:
                        route.fulfill(status=403,json={'error':'页面会话已失效，请重新连接。','code':'session_expired'})
                    else:
                        route.continue_()
                page.route('**'+target,fault)
                page.get_by_role('button',name=submit,exact=True).click()
                expect(page.locator('#connection')).to_contain_text('提交已暂停')
                wait_done(app,accepted[0])
                if kind=='create':
                    page.get_by_label('分析问题').fill('原提交之外后来编辑的新问题')
                before={row['id']:service.inspect(row['id']) for row in request(app,'/api/tasks')[1]['tasks']}
                page.get_by_role('button',name='立即重连',exact=True).click()
                expect(page.locator('#connection')).to_contain_text('连接正常')
                assert len(writes)==1
                if kind=='create':
                    page.reload()
                    expect(page.get_by_label('分析问题')).to_have_value('原提交之外后来编辑的新问题')
                    page.get_by_label('分析问题').fill('')
                    page.locator('#start').fill('2026-02-01')
                page.get_by_role('button',name=retry,exact=True).click()
                expect(page.locator('#connection')).to_contain_text('提交已暂停')
                page.get_by_role('button',name='立即重连',exact=True).click()
                expect(page.locator('#connection')).to_contain_text('连接正常')
                page.get_by_role('button',name=retry,exact=True).click()
                expect(page).to_have_url(app.origin+'/?task='+accepted[0])
                expect(page.locator('#connection')).to_contain_text('连接正常')
                assert len(writes)==3 and writes[0]==writes[1]==writes[2]
                assert {row['id']:service.inspect(row['id']) for row in request(app,'/api/tasks')[1]['tasks']}==before
                if kind=='create':
                    page.get_by_role('button',name='新建问题',exact=True).click()
                    expect(page.get_by_label('分析问题')).to_have_value('')
                    expect(page.locator('#start')).to_have_value('2026-02-01')
                    page.reload()
                    expect(page.get_by_label('分析问题')).to_have_value('')
                    expect(page.locator('#start')).to_have_value('2026-02-01')
            finally:
                browser.close()
