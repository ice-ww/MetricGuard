"""Baseline contract through the public task service and actual SQL sandbox."""
import json
from copy import deepcopy

import httpx2 as httpx
import pytest

from experiments.t01.references import python_metrics
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from tests.test_t09_service import image, response


SYSTEM_PROFILE={'action':'profile','table':'users','column':'registration_os','kind':'system_retention'}
COUNT={'action':'query','sql':'SELECT COUNT(*) AS users FROM users'}


@pytest.fixture(scope='module')
def baseline_snapshot(tmp_path_factory):
    return build_snapshot(tmp_path_factory.mktemp('t19-data')/'snapshot',scenario='normal',seed=1919)


def provider_with_plan(plan, calls):
    def provider(request):
        payload=json.loads(request.content)
        shared=json.loads(payload['system'].split('Shared materials:\n')[1])
        calls.append(deepcopy(shared))
        if shared.get('baseline_phase')=='plan':
            return response({'queries':plan})
        if 'last_failure' in shared:
            return response(SYSTEM_PROFILE if not shared['evidence'] else
                            {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]})
        return response({'facts':[{'evidence_id':e['evidence_id'],'row':i,'column':k,'value':v}
            for e in shared['evidence'] for i,row in enumerate(e['rows']) for k,v in row.items()
            if type(v) in (int,float)]})
    return provider


def test_shared_real_preflight_and_two_call_baseline_match_independent_reference(tmp_path,image):
    snapshot=build_snapshot(tmp_path/'data',scenario='A4',seed=1901)
    calls=[]
    with TaskService(tmp_path/'service',image,{'dev':snapshot.database},token='controlled',
                     transport=httpx.MockTransport(provider_with_plan([SYSTEM_PROFILE],calls))) as service:
        prepared=service.prepare_shared('新增用户自然日次日留存的系统结构变化','dev',('2026-01-08','2026-01-15'))
        baseline=service.create_from_shared(prepared,mode='baseline')
        agent=service.create_from_shared(prepared,mode='diagnose')
        result=service.run(baseline)
        other=service.run(agent)
        artifact=service.comparison_result(baseline)
        assert artifact['preflight']['status']=='ok'
        assert artifact['preflight']['steps']==3
        assert artifact['usage']['model_calls']==2
        assert artifact['usage']['steps']==1
        assert result['tool_calls']==4 and result['model_calls']==2
        assert result['repairs_used']==0 and result['report']['validation']['passed']
        assert artifact['shared_materials_hash']==service.comparison_result(agent)['shared_materials_hash']
        assert len([s for s in calls if s.get('baseline_phase')=='plan'])==1
        assert len([s for s in calls if s.get('baseline_phase')=='report'])==1
        assert result['definition']==other['definition'] and result['schema']==other['schema']
        assert result['evidence'][0]['rows']==other['evidence'][0]['rows']
        expected={}
        for period,start,end in [('previous','2026-01-01','2026-01-08'),('current','2026-01-08','2026-01-15')]:
            for row in python_metrics(snapshot.database,start,end)['retention']:
                values=expected.setdefault((period,row['os']),[0,0])
                values[0]+=row['users']; values[1]+=row['retained']
        assert {(r['period'],r['registration_os']):[r['users'],r['retained']]
                for r in result['evidence'][0]['rows']}==expected


def test_query_failure_is_retained_without_repair_and_report_still_called(tmp_path,image,baseline_snapshot):
    calls=[]
    plan=[{'action':'query','sql':'SELECT SUM(user_id) AS users FROM users'},COUNT]
    with TaskService(tmp_path,image,{'dev':baseline_snapshot.database},token='controlled',
                     transport=httpx.MockTransport(provider_with_plan(plan,calls))) as service:
        pre=service.prepare_shared('新增用户自然日次日留存','dev',('2026-01-08','2026-01-15'))
        task=service.create_from_shared(pre,mode='baseline')
        result=service.run(task); artifact=service.comparison_result(task)
        assert result['model_calls']==2 and artifact['usage']['steps']==2
        assert result['repairs_used']==0
        assert [r['status'] for r in artifact['query_results']]==['engine_denied','ok']
        assert len(calls)==2 and calls[1]['query_results'][0]['error_type']=='BinderException'
        assert result['outcome']=='insufficient_evidence' and result['report']['facts']
        assert artifact['usage']['tokens']==96 and artifact['usage_detail']['input_tokens']==62
        assert artifact['end_to_end']['steps']==5
        assert artifact['usage']['cost'] is None and artifact['usage_detail']['cost_estimate_usd']['maximum']>0


@pytest.mark.parametrize('mode',['baseline','diagnose'])
def test_failed_real_preflight_retained_for_both_without_model_dispatch(tmp_path,mode,baseline_snapshot):
    calls=[]
    with TaskService(tmp_path,'sha256:'+'0'*64,{'dev':baseline_snapshot.database},token='controlled',
                     transport=httpx.MockTransport(provider_with_plan([COUNT],calls))) as service:
        pre=service.prepare_shared('新增用户自然日次日留存','dev',('2026-01-08','2026-01-15'))
        task=service.create_from_shared(pre,mode=mode)
        service.run(task); artifact=service.comparison_result(task)
        assert artifact['preflight']['status']=='failed'
        assert artifact['preflight']['steps']==3
        assert artifact['usage']['model_calls']==0 and artifact['usage']['steps']==0 and not calls
        assert artifact['end_to_end']['steps']==3


@pytest.mark.parametrize('limits', [{'tool':3},{'tokens':1000},{'model':1}])
def test_same_scheduler_limits_prevent_baseline_extra_dispatch(tmp_path,image,baseline_snapshot,limits):
    calls=[]
    with TaskService(tmp_path,image,{'dev':baseline_snapshot.database},token='controlled',limits=limits,
                     transport=httpx.MockTransport(provider_with_plan([COUNT],calls))) as service:
        pre=service.prepare_shared('新增用户自然日次日留存','dev',('2026-01-08','2026-01-15'))
        task=service.create_from_shared(pre,mode='baseline')
        result=service.run(task); artifact=service.comparison_result(task)
        assert artifact['usage']['steps']==0 and result['outcome']=='budget_exhausted'
        assert len(calls)<2 and result['tool_calls']<=result['limits']['tool']


def test_unknown_provider_usage_blocks_report_and_is_not_zero(tmp_path,image,baseline_snapshot):
    calls=[]
    def provider(request):
        calls.append(1)
        return response({'queries':[COUNT]},usage=False)
    with TaskService(tmp_path,image,{'dev':baseline_snapshot.database},token='controlled',transport=httpx.MockTransport(provider)) as service:
        pre=service.prepare_shared('新增用户自然日次日留存','dev',('2026-01-08','2026-01-15'))
        task=service.create_from_shared(pre,mode='baseline')
        result=service.run(task); artifact=service.comparison_result(task)
        assert len(calls)==1 and result['outcome']=='budget_exhausted'
        assert artifact['usage']['tokens'] is None and artifact['usage']['cost'] is None
        assert artifact['usage_detail']['unknown_usage_calls']==1 and artifact['usage']['steps']==0


def test_public_consumption_and_report_protocol_can_be_scored(tmp_path,image,baseline_snapshot):
    from metricguard.evaluation_scoring import score,usage
    import duckdb
    with duckdb.connect(str(baseline_snapshot.database),read_only=True) as db:
        expected=db.execute('SELECT COUNT(DISTINCT user_id) FROM users').fetchone()[0]
    with TaskService(tmp_path,image,{'dev':baseline_snapshot.database},token='controlled',
                     transport=httpx.MockTransport(provider_with_plan([COUNT],[]))) as service:
        pre=service.prepare_shared('新增用户自然日次日留存','dev',('2026-01-08','2026-01-15'))
        task=service.create_from_shared(pre,mode='baseline'); service.run(task)
        artifact=service.comparison_result(task)
    usage(artifact['usage'])
    case={'id':'t19-selftest','category':'simple','required':[{'value':expected,'abs_tol':0,'rel_tol':0,
          'context':{'metric':'query_result:retention','window':['2026-01-08','2026-01-15'],'group':{},'comparison':None}}],
          'explanation':'insufficient_evidence','localization':{},'forbidden':['certain_cause'],'behaviors':[],'requires_review':False}
    assert score(case,artifact)['complete_pass'],score(case,artifact)


def test_completed_pair_persists_and_cannot_replay_dispatch(tmp_path,image,baseline_snapshot):
    calls=[]
    with TaskService(tmp_path,image,{'dev':baseline_snapshot.database},token='controlled',
                     transport=httpx.MockTransport(provider_with_plan([COUNT],calls))) as service:
        pre=service.prepare_shared('新增用户自然日次日留存','dev',('2026-01-08','2026-01-15'))
        task=service.create_from_shared(pre,mode='baseline'); service.run(task)
        saved=service.comparison_result(task)
    with TaskService(tmp_path,image,{'dev':baseline_snapshot.database},token='controlled',
                     transport=httpx.MockTransport(provider_with_plan([COUNT],calls))) as service:
        assert service.comparison_result(task)==saved
        with pytest.raises(ValueError,match='cannot run'): service.run(task)
    assert len(calls)==2


def test_batch_cannot_read_files_and_report_cannot_request_more_queries(tmp_path,image,baseline_snapshot):
    calls=[]
    plan=[{'action':'query','sql':"SELECT * FROM read_csv_auto('/etc/passwd')"},COUNT]
    normal=provider_with_plan(plan,calls)
    def provider(request):
        result=normal(request)
        if len(calls)==2: return response({'facts':[],'queries':[COUNT]})
        return result
    with TaskService(tmp_path,image,{'dev':baseline_snapshot.database},token='controlled',transport=httpx.MockTransport(provider)) as service:
        pre=service.prepare_shared('新增用户自然日次日留存','dev',('2026-01-08','2026-01-15'))
        task=service.create_from_shared(pre,mode='baseline'); result=service.run(task)
        assert len(calls)==2 and result['tool_calls']==5 and result['repairs_used']==0
        assert result['baseline_results'][0]['status']=='policy_denied'
        assert result['outcome']=='refused' and result['report']['deterministic']
        assert result['baseline_report_draft']['queries']==[COUNT]


def test_active_time_budget_and_ambiguous_preflight_do_not_dispatch_models(tmp_path,image,baseline_snapshot):
    for name,question,limits in [('time','新增用户自然日次日留存',{'active_seconds':.000001}),
                                 ('ambiguous','用户表现怎么样',{})]:
        calls=[]
        with TaskService(tmp_path/name,image,{'dev':baseline_snapshot.database},token='controlled',limits=limits,
                         transport=httpx.MockTransport(provider_with_plan([COUNT],calls))) as service:
            pre=service.prepare_shared(question,'dev',('2026-01-08','2026-01-15'))
            task=service.create_from_shared(pre,mode='baseline'); service.run(task)
            assert service.comparison_result(task)['preflight']['status']=='failed' and not calls
