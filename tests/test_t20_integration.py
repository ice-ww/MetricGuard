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
        prepared = service.prepare_shared('新增用户自然日次日留存', 'dev', ('2026-01-08', '2026-01-15'))
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
        prepared=service.prepare_shared('请分析完整请求窗口的新增用户自然日次日留存，说明资料是否充分。','dev',('2026-01-08','2026-01-15'))
        task=service.create_from_shared(prepared,mode='diagnose')
        state=service.run(task)
        rows=state['evidence'][0]['rows']
        previous=[r for r in rows if r['period']=='previous']
        assert all(r['window_start']=='2026-01-01' and r['window_end']=='2026-01-08' for r in previous)
        assert sum(r['users'] for r in previous)==1656
        assert state['analysis_result']=='insufficient_evidence'
        assert not state['report']['diagnosis']['candidates']
        artifact=service.comparison_result(task)
        assert 'incomplete_coverage_disclosed' in artifact['report']['behaviors']
        assert artifact['report']['inferences']
