"""Development questions exercised through the approved public retrieval seam."""
from experiments.t06 import retrieve
from tests.test_t09_service import image, response
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
import httpx2 as httpx
import json
import pytest


def test_baseline_compact_selection_resolves_actual_cells(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A4', seed=190019)
    calls = []
    def provider(request):
        shared = json.loads(json.loads(request.content)['system'].split('Shared materials:\n')[1])
        calls.append(shared)
        if shared.get('baseline_phase') == 'plan':
            return response({'queries': [{'action': 'profile', 'table': 'users',
                'column': 'registration_os', 'kind': 'system_retention'}]})
        return response({'selections': [{'evidence_id': e['evidence_id'], 'columns': ['users', 'retained', 'retention_rate']}
                                       for e in shared['evidence']]})
    with TaskService(tmp_path / 'service', image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        prepared = service.prepare_shared('新增用户自然日次日留存', 'dev', ('2026-01-08', '2026-01-15'),
                                          comparison_window=('2026-01-01', '2026-01-08'))
        task = service.create_from_shared(prepared, mode='baseline')
        state = service.run(task)
        assert len(calls) == 2
        assert state['outcome'] == 'facts_available'
        assert len(state['report']['facts']) >= 12
        assert state['report']['validation']['passed']
        artifact = service.comparison_result(task)
        assert not artifact['execution_failures']
        assert artifact['report']['inferences']
        assert artifact['report']['localization'] == {'os': 'Android'}
        assert artifact['report']['explanation'] == 'composition_masks_subgroup_decline'
        published = service.publish_diagnosis(task)
        assert published['status'] == 'mechanically_valid'
        assert published['inferences'] and published['semantic_status'] == 'pending_review'
        standard = [f for f in published['assertions'] if f['context']['metric'] == 'baseline_standardized_retention_rate']
        assert len(standard) == 1 and standard[0]['value'] == pytest.approx(.596875)
        assert standard[0]['context']['group'] == {}


def test_component_counts_and_acquisition_questions_have_inspectable_definitions():
    window = ('2026-02-01', '2026-02-08')
    for question, metric in [
        ('请计算本期新增用户数', 'new_users'),
        ('Android 9.4 去重播放开始数是多少？', 'play_starts'),
        ('campaign_test 渠道同期支出（分）', 'spend'),
        ('新增用户增长质量如何？请比较留存与渠道成本并说明限制。', 'retained_cost'),
    ]:
        result = retrieve(question, window)
        assert result['status'] == 'adopt', result
        assert result['definition']['id'] == metric
        assert result['definition']['time']


def test_generic_user_performance_requires_metric_clarification():
    result = retrieve('用户表现怎么样？', ('2026-02-01', '2026-02-08'))
    assert result['status'] == 'clarify'
    assert result['definition'] is None
    assert retrieve('本月营收是多少？', ('2026-02-01', '2026-02-08'))['status'] == 'unsupported'
    clarified = retrieve('用户表现怎么样？ 新增用户自然日次日留存。', ('2026-02-01', '2026-02-08'))
    assert clarified['status'] == 'adopt'


def test_named_metric_inside_full_question_is_not_lost_to_rank_threshold():
    result=retrieve('观测完播率出现变化，请用独立证据检查采集与行为解释。',('2026-02-01','2026-02-08'))
    assert result['status']=='adopt' and result['definition']['id']=='completion'


def test_shared_preflight_clarifies_once_and_inherits_answer_and_cost(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal', seed=202002)
    def no_model(request):
        raise AssertionError('preflight must not dispatch a model')
    with TaskService(tmp_path / 'service', image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(no_model)) as service:
        prepared = service.prepare_shared('用户表现怎么样？', 'dev', ('2026-01-08', '2026-01-15'))
        state = service.inspect(prepared)
        assert state['status'] == 'waiting'
        pending = state['pending_question']
        answered = service.answer(prepared, pending['question_id'], pending['version'], '新增用户自然日次日留存。')
        assert answered['status'] == 'ended'
        assert not answered['prepared_comparison']['failed']
        assert answered['model_calls'] == 0
        with pytest.raises(ValueError):
            service.answer(prepared, pending['question_id'], pending['version'], '重复回答')
        for mode in ('baseline', 'diagnose'):
            child = service.inspect(service.create_from_shared(prepared, mode=mode))
            assert child['answers'] == answered['answers']
            assert child['tool_calls'] == answered['tool_calls'] == 4
            assert child['active'] == answered['active']


@pytest.mark.parametrize('question,kind,expected', [
    ('本期新增用户数','new_user_counts',{'users':1680}),
    ('新增用户自然日次日留存人数和留存率','retained_user_counts',{'users':1680,'retained':1176,'retention_rate':.7}),
])
def test_standalone_counts_publish_current_window_facts(tmp_path,image,question,kind,expected):
    snapshot=build_snapshot(tmp_path/'data',scenario='A4',seed=190019)
    def provider(request):
        shared=json.loads(json.loads(request.content)['system'].split('Shared materials:\n')[1])
        return response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]} if shared['evidence'] else
                        {'action':'profile','table':'users','column':'user_id','kind':kind})
    with TaskService(tmp_path/'service',image,{'dev':snapshot.database},token='controlled',transport=httpx.MockTransport(provider)) as service:
        task=service.create(question,'dev',('2026-01-08','2026-01-15'),mode='diagnose')
        state=service.run(task)
        assert state['analysis_result']=='facts_available'
        publication=service.publish_diagnosis(task)
        assert publication['status']=='mechanically_valid'
        overall=[a for a in publication['assertions'] if a['context']['group']=={}]
        observed={a['context']['metric']:a['value'] for a in overall}
        assert observed==expected
        assert all(a['context']=={'metric':a['context']['metric'],'window':['2026-01-08','2026-01-15'],
                                 'group':{},'comparison':'current'} for a in overall)


def test_pre_dispatch_timeout_is_audited_and_retried_without_duplicate_query(tmp_path,image):
    from metricguard.service import QueryNotDispatched
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=202003)
    fired=[]
    def fault(stage):
        if stage=='before_query_dispatch' and not fired:
            fired.append(stage)
            raise QueryNotDispatched('development timeout before worker dispatch')
    def provider(request):
        shared=json.loads(json.loads(request.content)['system'].split('Shared materials:\n')[1])
        return response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]} if shared['evidence'] else
                        {'action':'profile','table':'users','column':'registration_os','kind':'system_retention'})
    with TaskService(tmp_path/'service',image,{'dev':snapshot.database},token='controlled',
                     transport=httpx.MockTransport(provider),fault_hook=fault) as service:
        prepared=service.prepare_shared('新增用户自然日次日留存','dev',('2026-01-08','2026-01-15'))
        task=service.create_from_shared(prepared,mode='diagnose')
        state=service.run(task)
        assert state['outcome']=='facts_available'
        attempts=[a for a in state['attempts'] if a['operation'].startswith('diagnostic_sql:')]
        assert len(attempts)==2 and {a['state'] for a in attempts}=={'failed','completed'}
        assert len(state['evidence'])==1 and state['model_calls']==2 and state['tool_calls']==5
        assert len([e for e in state['trace'] if e['event']=='query_completed'])==1
        assert 'recovered_without_duplicate_dispatch' in service.comparison_result(task)['report']['behaviors']


def test_partial_current_window_keeps_requested_comparison_and_discloses_insufficiency(tmp_path,image):
    import duckdb
    from tests.test_t15_service import controlled
    snapshot=build_snapshot(tmp_path/'data',scenario='A4',seed=190019)
    with duckdb.connect(str(snapshot.database)) as db:
        db.execute("UPDATE source_watermarks SET complete_before='2026-01-12T00:00:00+08:00' WHERE source='sessions'")
    with TaskService(tmp_path/'service',image,{'dev':snapshot.database},token='controlled',transport=httpx.MockTransport(controlled())) as service:
        prepared=service.prepare_shared('请分析完整请求窗口的新增用户自然日次日留存，说明资料是否充分。','dev',('2026-01-08','2026-01-15'),comparison_window=('2026-01-01','2026-01-08'))
        pending=service.inspect(prepared)['pending_question']
        service.answer(prepared,pending['question_id'],pending['version'],'2')
        task=service.create_from_shared(prepared,mode='diagnose')
        state=service.run(task)
        assert not state['evidence'] and state['model_calls'] == 0
        assert state['actual_window'] is None
        assert state['analysis_result']=='insufficient_evidence'
        assert 'requested_window_incomplete' in state['limitations']
        artifact=service.comparison_result(task)
        assert 'incomplete_coverage_disclosed' in artifact['report']['behaviors']



def test_unknown_cohort_attribution_does_not_invent_zero_crash_groups(tmp_path, image):
    import duckdb
    from tests.test_t12_service import controlled
    snapshot=build_snapshot(tmp_path/'data',scenario='A1',seed=202004)
    with duckdb.connect(str(snapshot.database)) as db:
        db.execute("UPDATE users SET registration_os=NULL WHERE user_id=(SELECT MIN(user_id) FROM users)")
        db.execute("UPDATE sessions SET crashed=FALSE")
    with TaskService(tmp_path/'service',image,{'dev':snapshot.database},token='controlled',
                     transport=controlled(['cohort_health','crash_versions','releases'])) as service:
        task=service.create('新增用户自然日次日留存下降原因','dev',('2026-01-08','2026-01-15'),mode='diagnose',comparison_window=('2026-01-01','2026-01-08'))
        state=service.run(task)
        assert state['evidence']
        published=service.publish_diagnosis(task)
        assert published['assertions']
        assert not any(a['context']['metric']=='actual_first_day_crashed_users' for a in published['assertions'])


def test_multi_profile_diagnosis_finishes_with_original_token_budget(tmp_path, image):
    from tests.test_t12_service import profile
    snapshot=build_snapshot(tmp_path/'data',scenario='A1',seed=2026001)
    kinds=['system_retention','cohort_health','crash_versions','releases']
    usage=[1815,2366,3171,3837,4000]
    calls=[]
    def provider(request):
        payload=json.loads(request.content)
        shared=json.loads(payload['system'].split('Shared materials:\n')[1])
        index=len(calls); calls.append(payload)
        if index==0:
            action={'action':'profile','table':'users','column':'registration_os','kind':kinds[index]}
        elif index<4:
            action=profile(kinds[index])
        else:
            action={'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]}
        result=response(action).json()
        result['usage']={'input_tokens':usage[index]-100,'output_tokens':100}
        return httpx.Response(200,json=result)
    with TaskService(tmp_path/'service',image,{'dev':snapshot.database},token='controlled',
                     transport=httpx.MockTransport(provider),limits={'tool':12,'model':10,'tokens':30000,'active_seconds':180}) as service:
        task=service.create('新增用户自然日次日留存出现变化，请检验可能解释和反对证据。','dev',('2026-01-08','2026-01-15'),mode='diagnose',comparison_window=('2026-01-01','2026-01-08'))
        state=service.run(task)
        assert state['outcome']=='facts_available', state['limitations']
        assert len(calls)==5
        assert state['report']['validation']['passed']
        assert any(d['candidates'] for d in [state['report']['diagnosis']]+state['report'].get('additional_diagnoses',[]))


def test_clarified_metric_query_returns_facts_without_unsolicited_diagnosis(tmp_path,image):
    from tests.test_t15_service import controlled
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=2026009)
    with TaskService(tmp_path/'service',image,{'dev':snapshot.database},token='controlled',transport=httpx.MockTransport(controlled())) as service:
        prepared=service.prepare_shared('用户表现怎么样？','dev',('2026-01-08','2026-01-15'))
        pending=service.inspect(prepared)['pending_question']
        service.answer(prepared,pending['question_id'],pending['version'],'新增用户自然日次日留存，按已提供窗口。')
        task=service.create_from_shared(prepared,mode='diagnose')
        service.run(task)
        artifact=service.comparison_result(task)
        assert artifact['report']['explanation']=='query_result'
        assert not artifact['report']['inferences']
        assert artifact['report']['assertions']
        assert 'clarified_before_analysis' in artifact['report']['behaviors']


def test_preflight_isolation_failure_preserves_safe_reason_code(tmp_path):
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=2026033)
    with TaskService(tmp_path/'service','mutable-image-tag',{'dev':snapshot.database},token='unused') as service:
        prepared=service.prepare_shared('新增用户自然日次日留存','dev',('2026-01-08','2026-01-15'))
        state=service.inspect(prepared)
        assert state['prepared_comparison']['failed']
        failures=[json.loads(a['result']) for a in state['attempts'] if a['state']=='failed']
        assert failures[0]['error_code']=='invalid_image'
        assert state['model_calls']==0
        assert any(json.loads(e['detail']).get('error_code')=='invalid_image' for e in state['trace'] if e['event']=='execution_stopped')


def test_model_stop_prose_is_not_published_as_verified_limitation(tmp_path,image):
    import duckdb
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=2026035)
    unverified='本期三天与基期七天是等长窗口，因此新增用户下降。'
    def provider(request):
        shared=json.loads(json.loads(request.content)['system'].split('Shared materials:\n')[1])
        return response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[unverified]} if shared['evidence'] else
                        {'action':'profile','table':'users','column':'registration_os','kind':'system_retention'})
    with TaskService(tmp_path/'service',image,{'dev':snapshot.database},token='controlled',transport=httpx.MockTransport(provider)) as service:
        task=service.create('请分析完整请求窗口的新增用户自然日次日留存，说明资料是否充分。','dev',('2026-01-08','2026-01-11'),mode='diagnose',comparison_window=('2026-01-01','2026-01-08'))
        state=service.run(task)
        publication=service.publish_diagnosis(task)
        assert unverified in state['unresolved_questions']
        assert publication['inferences']
        assert all(unverified not in i['unexcluded_factors'] for i in publication['inferences'])
        assert all(i['unexcluded_factors'] for i in publication['inferences'])


@pytest.mark.parametrize('question,answer',[
    ('请查询新增用户自然日次日留存为什么下降',None),
    ('分析用户表现','新增用户自然日次日留存下降是否与版本发布有关？'),
    ('查询新增用户自然日次日留存，并评估版本发布的影响',None),
])
def test_query_word_or_clarification_does_not_suppress_requested_diagnosis(tmp_path,image,question,answer):
    from tests.test_t12_service import controlled
    snapshot=build_snapshot(tmp_path/'data',scenario='A1',seed=1212)
    with TaskService(tmp_path/'service',image,{'dev':snapshot.database},token='controlled',transport=controlled(['releases','cohort_health','crash_versions'])) as service:
        task=service.create(question,'dev',('2026-01-08','2026-01-15'),mode='diagnose',comparison_window=('2026-01-01','2026-01-08'))
        state=service.run(task)
        if answer:
            pending=state['pending_question']
            state=service.answer(task,pending['question_id'],pending['version'],answer)
        assert state['analysis_result']=='supported_descriptive_candidate'
        assert service.publish_diagnosis(task)['inferences']


def test_crash_affected_user_count_is_a_metric_query(tmp_path,image):
    snapshot=build_snapshot(tmp_path/'data',scenario='normal',seed=2026041)
    def provider(request):
        shared=json.loads(json.loads(request.content)['system'].split('Shared materials:\n')[1])
        return response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]} if shared['evidence'] else
                        {'action':'profile','table':'users','column':'user_id','kind':'crash_user_counts'})
    with TaskService(tmp_path/'service',image,{'dev':snapshot.database},token='controlled',transport=httpx.MockTransport(provider)) as service:
        prepared=service.prepare_shared('查询新增用户首日崩溃受影响人数','dev',('2026-01-08','2026-01-15'))
        task=service.create_from_shared(prepared,mode='diagnose')
        service.run(task)
        artifact=service.comparison_result(task)
        assert artifact['report']['explanation']=='query_result'
        assert artifact['report']['assertions']
        assert not artifact['report']['inferences']
