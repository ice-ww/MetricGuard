"""Dedicated scorer fixtures, never frozen diagnosis cases."""
from copy import deepcopy
from dataclasses import asdict
import pytest
from experiments.t08.contract import Assertion, EvidenceResult, FactContext, Reference
from metricguard.semantic_rubric import RUBRIC_HASH, digest
from metricguard.evaluation import EvaluationRunner


def sample():
    context=FactContext('new_users',('2026-01-01','2026-01-08'),{'os':'Android'},None)
    ref=Reference('selftest-e',0,'n')
    evidence=EvidenceResult('selftest-e','controlled','SELECT count(*)','selftest','selftest-snapshot',
        {'n':'integer'},({'n':7},),{ref.pointer:context},context.window,{}, {},(),False)
    evidence=asdict(evidence); evidence['parameters']={}
    assertion=asdict(Assertion('a',ref,context,7))
    case={'id':'selftest-1','category':'A1','required':[{'context':asdict(context),'value':7,'abs_tol':0,'rel_tol':0}],
          'explanation':'candidate','localization':{'os':'Android'},'forbidden':['certain_cause'],
          'behaviors':[],'requires_review':True}
    report={'assertions':[assertion],'inferences':[{'inference_id':'i','text':'Candidate only',
        'supporting_assertion_ids':['a'],'opposing_assertion_ids':[],'unexcluded_factors':['confounding']}],
        'explanation':'candidate','localization':{'os':'Android'},'conclusions':[],
        'behaviors':[],'blocked':[]}
    artifact={'evidence':[evidence],'report':report,'preflight':{'status':'ok','seconds':1,'steps':1,'model_calls':1,'tokens':10,'cost':None},
        'usage':{'seconds':2,'steps':2,'model_calls':2,'tokens':20,'cost':None},'safety_passed':True}
    return case,artifact


def human(case,artifact):
    return {'case_id':case['id'],'report_hash':digest(artifact['report']),'evidence_hash':digest(artifact['evidence']),'rubric_hash':RUBRIC_HASH,
        'reviewer':'synthetic human fixture','reviewer_kind':'human','ratings':[{
            'inference_id':'i','scores':{'relevance':2,'counterevidence':2,'causal_restraint':2},
            'reasons':{'relevance':'fixture only','counterevidence':'fixture only','causal_restraint':'fixture only'}}]}


def test_scorer_separates_attribution_from_complete_and_requires_human(tmp_path):
    runner=EvaluationRunner(tmp_path); case,artifact=sample()
    pending=runner.score(case,artifact)
    assert pending['attribution_hit'] and not pending['complete_pass'] and pending['semantic_status']=='pending'
    good=runner.score(case,artifact,human(case,artifact))
    assert good['complete_pass'] and good['assertion_pass_rate']==1
    artifact['report']['assertions'][0]['value']=8
    bad=runner.score(case,artifact,human(case,artifact))
    assert bad['attribution_hit'] and not bad['complete_pass'] and bad['assertion_pass_rate']==0


@pytest.mark.parametrize('change', ['empty','forbidden','wrong_context','bad_review','agent','preflight','blocked','unsafe'])
def test_controlled_failure_cases_never_pass(tmp_path,change):
    runner=EvaluationRunner(tmp_path); case,artifact=sample(); review=human(case,artifact)
    if change=='empty': artifact['report']['assertions']=[]
    if change=='forbidden': artifact['report']['conclusions']=['certain_cause']
    if change=='wrong_context': artifact['report']['assertions'][0]['context']['group']={'os':'iOS'}
    if change=='bad_review': review['report_hash']='stale'
    if change=='agent': review['reviewer_kind']='agent'
    if change=='preflight': artifact['preflight']['status']='failed'
    if change=='blocked': artifact['report']['blocked']=[{'kind':'conclusion','original':{'text':'bad causal claim'},'reason':'unsupported','action':'removed'}]
    if change=='unsafe': artifact['safety_passed']=False
    assert not runner.score(case,artifact,review)['complete_pass']


def setup_bundle(tmp_path):
    from metricguard.evaluation import file_hash
    repo=tmp_path/'repo'; repo.mkdir(); (repo/'uv.lock').write_text('selftest'); (repo/'code.py').write_text('selftest code')
    hashes={'code.py':file_hash(repo/'code.py')}
    config={'code_ref':'selftest-only','code_hashes':hashes,'dependency_hash':file_hash(repo/'uv.lock'),
        'model':{'name':'controlled-provider'},'prompt_hashes':hashes,'rule_hashes':hashes,'reference_hashes':hashes,
        'rubric_hash':RUBRIC_HASH,'budgets':{'model':2},'image':'selftest-no-execution'}
    case,artifact=sample()
    case['public']={'id':case['id'],'question':'Count users','window':['2026-01-01','2026-01-08'],
        'snapshot':'public/sample.duckdb','snapshot_id':'selftest-snapshot','definition':'count unique users','schema':{'users':['id']}}
    runner=EvaluationRunner(tmp_path/'registry',repository=repo)
    runner.freeze('selftest-v1','selftest-family',[case],config,purpose='scorer_selftest')
    return runner,case,artifact,config


def test_three_round_baseline_inputs_accounting_and_persistent_human_review(tmp_path):
    runner,case,artifact,config=setup_bundle(tmp_path); inputs=[]
    def prepare(public,configuration,controls):
        assert set(public)==set(case['public']) and 'required' not in public
        return {'status':'ok','materials':{'schema':'shared'},'usage':{k:v for k,v in artifact['preflight'].items() if k!='status'}}
    def execute(public,materials,variant,configuration):
        inputs.append((deepcopy(public),deepcopy(materials),variant,configuration))
        return deepcopy(artifact)
    run=runner.run('selftest-v1',prepare,execute,actor='controlled selftest')
    result=runner.results(run)
    assert len(result['records'])==6 and result['complete'] and len(inputs)==6
    assert all(inputs[i][0:2]==inputs[i+1][0:2] for i in (0,2,4))
    assert all(s['total_cost'] is None and s['unknown_cost_records']==2 and s['known_tokens']==30 for s in result['summary']['rounds'])
    assert all(s['complete_passes']==0 for s in result['summary']['rounds'])
    runner.review(run,0,human(case,artifact))
    reopened=EvaluationRunner(runner.root,repository=runner.repository)
    assert reopened.results(run)['records'][0]['score']['complete_pass']
    assert not reopened.results(run)['records'][1]['score']['complete_pass']
    assert any(e['kind']=='review_recorded' for e in reopened.audit())


def test_preflight_failure_keeps_all_denominators_and_never_dispatches(tmp_path):
    runner,case,artifact,config=setup_bundle(tmp_path)
    def prepare(*args):
        return {'status':'failed','materials':{},'usage':{k:v for k,v in artifact['preflight'].items() if k!='status'}}
    def execute(*args):
        pytest.fail('must not dispatch after preflight failure')
    result=runner.results(runner.run('selftest-v1',prepare,execute,actor='selftest'))
    assert len(result['records'])==6
    assert all(s['tasks']==1 and s['failure_types']['preflight_failed']==1 and s['complete_passes']==0 for s in result['summary']['rounds'])


def test_repair_contamination_survives_new_version_family_and_restart(tmp_path):
    runner,case,artifact,config=setup_bundle(tmp_path)
    runner.access('selftest-v1',actor='repair fixture',purpose='repair')
    runner.freeze('renamed','different-family',[case],config,purpose='scorer_selftest')
    assert runner.status('renamed')['purpose']=='regression'
    reopened=EvaluationRunner(runner.root,repository=runner.repository)
    changed=deepcopy(case); changed['public']['snapshot_id']='new-snapshot'
    reopened.freeze('regenerated','selftest-family',[changed],config,purpose='scorer_selftest')
    assert reopened.status('regenerated')['purpose']=='regression'
    assert any(e['kind']=='private_access' and e['detail']['purpose']=='repair' for e in reopened.audit())


def test_drift_and_wrong_formal_distribution_fail_before_model_dispatch(tmp_path):
    runner,case,artifact,config=setup_bundle(tmp_path)
    with pytest.raises(ValueError,match='distribution'):
        runner.freeze('bad','family',[case],config)
    (runner.repository/'code.py').write_text('changed')
    with pytest.raises(ValueError,match='configuration drift'):
        runner.run('selftest-v1',lambda *a:None,lambda *a:None,actor='selftest')


def test_path_independence_and_tolerance_are_not_reference_row_matching(tmp_path):
    runner=EvaluationRunner(tmp_path); case,artifact=sample()
    artifact['evidence'][0]['rows']=({'n':99},{'n':7})
    artifact['evidence'][0]['contexts']={'/rows/1/n':deepcopy(artifact['report']['assertions'][0]['context'])}
    artifact['report']['assertions'][0]['reference']['row']=1
    case['required'][0]['value']=7.001; case['required'][0]['abs_tol']=.01
    assert runner.score(case,artifact,human(case,artifact))['complete_pass']


def test_removed_assertion_remains_in_original_error_denominator(tmp_path):
    runner=EvaluationRunner(tmp_path); case,artifact=sample()
    bad=deepcopy(artifact['report']['assertions'][0]); bad.update(assertion_id='wrong',value=8)
    artifact['report']['blocked']=[{'kind':'assertion','original':bad,'action':'removed','reason':'wrong number'}]
    result=runner.score(case,artifact,human(case,artifact))
    assert result['assertion_count']==2 and result['assertion_pass_rate']==.5
    assert result['blocked_count']==1 and not result['complete_pass']


def test_review_cannot_be_transferred_to_different_evidence(tmp_path):
    runner=EvaluationRunner(tmp_path); case,artifact=sample(); review=human(case,artifact)
    artifact['evidence'][0]['source']='different query source'
    assert not runner.score(case,artifact,review)['complete_pass']


def test_execution_exception_is_retained_with_unknown_usage(tmp_path):
    runner,case,artifact,config=setup_bundle(tmp_path)
    def prepare(*args):
        return {'status':'ok','materials':{},'usage':{k:v for k,v in artifact['preflight'].items() if k!='status'}}
    def execute(*args): raise RuntimeError('controlled failure')
    result=runner.results(runner.run('selftest-v1',prepare,execute,actor='selftest'))
    assert len(result['records'])==6 and all(not r['score']['complete_pass'] for r in result['records'])
    assert all(s['unknown_model_call_records']==1 and s['total_cost'] is None for s in result['summary']['rounds'])


@pytest.mark.parametrize('category',['A1','A2','A3','A4'])
def test_freeze_builder_uses_independent_references_on_separate_development_data(tmp_path,category):
    from experiments.t18.freeze import build_case
    recipe={'id':'builder-selftest','category':category,'scenario':category,'seed':180018,'base_start':'2026-11-01T00:00:00+08:00',
        'new_version':'9.9','crash_probability':.61,'campaign_channel':'dev-only','campaign_growth':2.9,
        'campaign_retention':.18,'campaign_unit_cost':190,'completion_drop_probability':.85,
        'current_ios_share':.64,'current_android_retention':.32,'simple_metric':'users'}
    case,provenance=build_case(recipe,tmp_path)
    assert provenance['reference_agreement'] and case['required'] and case['snapshot_sha256']
    if category=='A4':
        assert any(r['context']['metric']=='baseline_standardized_retention_rate' for r in case['required'])
        assert any(r['context']['metric']=='retention_rate' and r['context']['group']=={} for r in case['required'])
    if category in ('A2','A4'): assert any(r['context']['metric']=='new_user_share' for r in case['required'])
    if category=='A1':
        assert case['required_observations'][0]['context']['metric']=='release_date'
        assert any(r['context']['metric']=='actual_first_day_crashed_users' for r in case['required'])
    if category=='A3':
        assert len(case['required_observations'])==2
        assert any(r['context']['metric']=='unmatched' for r in case['required'])
    assert 'category' not in case['public'] and 'required' not in case['public']


@pytest.mark.parametrize('invalid', ['nan','object','null','list','missing_materials'])
def test_malformed_adapter_output_preserves_all_rounds_and_failures(tmp_path,invalid):
    runner,case,artifact,config=setup_bundle(tmp_path)
    def prepare(*args):
        prepared={'status':'ok','materials':{},'usage':{k:v for k,v in artifact['preflight'].items() if k!='status'}}
        if invalid=='missing_materials': prepared.pop('materials')
        return prepared
    def execute(*args):
        result=deepcopy(artifact)
        if invalid=='nan': result['report']['assertions'][0]['value']=float('nan')
        if invalid=='object': result['extra']=object()
        if invalid=='null': return None
        if invalid=='list': return []
        return result
    result=runner.results(runner.run('selftest-v1',prepare,execute,actor='invalid adapter selftest'))
    assert result['complete'] and len(result['records'])==6
    assert all(not r['score']['complete_pass'] for r in result['records'])
    if invalid=='nan': assert all(r['score']['assertion_count']==1 and r['score']['assertion_pass_rate']==0 for r in result['records'])


def test_malformed_assertion_keeps_valid_siblings_and_input_denominator(tmp_path):
    runner=EvaluationRunner(tmp_path); case,artifact=sample()
    artifact['report']['assertions'].append({'assertion_id':'malformed'})
    result=runner.score(case,artifact)
    assert result['assertion_count']==2 and result['valid_assertion_count']==1 and result['assertion_pass_rate']==.5
    assert not result['complete_pass']


def test_textual_calendar_observation_requires_exact_evidence_and_context(tmp_path):
    runner=EvaluationRunner(tmp_path); case,artifact=sample()
    ctx={'metric':'release_date','window':['2026-01-01','2026-01-08'],'group':{'os':'Android','version':'2.0'},'comparison':'current'}
    case['required_observations']=[{'context':ctx,'value':'2026-01-01'}]
    assert not runner.score(case,artifact,human(case,artifact))['complete_pass']
    e=artifact['evidence'][0]; e['columns']['released']='string'; e['rows'][0]['released']='2026-01-01'; e['contexts']['/rows/0/released']=ctx
    artifact['report']['observations']=[{'reference':{'evidence_id':e['evidence_id'],'row':0,'column':'released'},'context':ctx,'value':'2026-01-01'}]
    assert runner.score(case,artifact,human(case,artifact))['complete_pass']
    artifact['report']['observations'][0]['value']='2026-01-02'
    assert not runner.score(case,artifact,human(case,artifact))['complete_pass']


def test_registry_releases_file_handles_after_each_operation(tmp_path):
    runner,case,artifact,config=setup_bundle(tmp_path)
    runner.audit(); runner.status('selftest-v1')
    renamed=runner.database.with_suffix('.moved')
    runner.database.rename(renamed)
    renamed.rename(runner.database)
