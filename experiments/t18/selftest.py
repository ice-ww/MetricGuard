"""Executable controlled scorer experiment. Contains no frozen cases."""
import argparse
from copy import deepcopy
from dataclasses import asdict
import json
from pathlib import Path
import duckdb
from experiments.t08.contract import Assertion,EvidenceResult,FactContext,Reference
from experiments.t18.freeze import configuration,ROOT
from metricguard.evaluation import EvaluationRunner
from metricguard.semantic_rubric import RUBRIC_HASH,digest

NAMES=('correct','wrong_numeric','preflight_failed','missing_human','agent_review','semantic_rejected','blocked','forbidden','unknown_cost','empty','wrong_location')


def fixtures() -> tuple[list[dict],dict]:
    with duckdb.connect() as con:
        row=con.execute('SELECT COUNT(*) FROM range(7)').fetchone()
        assert row is not None
        observed=row[0]
    assert observed==len(set(range(7)))
    context=FactContext('new_users',('2026-01-01','2026-01-08'),{'os':'Android'},None)
    reference=Reference('controlled-count',0,'n')
    evidence=EvidenceResult('controlled-count','selftest_sql',{},'SELECT COUNT(*) FROM range(7)','scorer-only',
        {'n':'integer'},({'n':observed},),{reference.pointer:context},context.window,{}, {},(),False)
    cases=[]
    for name in NAMES:
        cases.append({'id':'scorer-'+name,'category':'A1','required':[{'context':asdict(context),'value':7,'abs_tol':0,'rel_tol':0}],
            'explanation':'candidate','localization':{'os':'Android'},'forbidden':['certain_cause'],'behaviors':[],'requires_review':True,
            'public':{'id':'scorer-'+name,'question':'Controlled scorer fixture only','window':list(context.window),
                'snapshot':'public/scorer-only.duckdb','snapshot_id':'scorer-only','definition':'count','schema':{'n':'integer'}}})
    artifact={'evidence':[asdict(evidence)],'report':{'assertions':[asdict(Assertion('a',reference,context,observed))],
        'inferences':[{'inference_id':'i','text':'Descriptive candidate, not certain causation','supporting_assertion_ids':['a'],
            'opposing_assertion_ids':[],'unexcluded_factors':['synthetic fixture']}],
        'explanation':'candidate','localization':{'os':'Android'},'conclusions':[],'behaviors':[],'blocked':[]},
        'usage':{'seconds':2,'steps':2,'model_calls':2,'tokens':20,'cost':.02},'safety_passed':True}
    return cases,artifact


def run(output: Path,image: str) -> dict:
    output.mkdir(parents=True,exist_ok=False)
    runner=EvaluationRunner(output/'registry',repository=ROOT); cases,base=fixtures()
    runner.freeze('scorer-selftest-v1','scorer-selftest',[*cases],configuration(image),purpose='scorer_selftest')
    def prepare(public,config,controls):
        return {'status':'failed' if public['id']=='scorer-preflight_failed' else 'ok','materials':{'same_inputs':True},
            'usage':{'seconds':1,'steps':1,'model_calls':1,'tokens':10,'cost':.01}}
    def execute(public,materials,variant,config):
        artifact=deepcopy(base); report=artifact['report']; name=public['id'].removeprefix('scorer-')
        if name=='wrong_numeric': report['assertions'][0]['value']=8
        if name=='forbidden': report['conclusions']=['certain_cause']
        if name=='empty': report['assertions']=[]; report['inferences']=[]
        if name=='wrong_location': report['localization']={'os':'iOS'}
        if name=='unknown_cost': artifact['usage']['cost']=None
        if name=='blocked':
            wrong=deepcopy(report['assertions'][0]); wrong.update(assertion_id='removed',value=8)
            report['blocked']=[{'kind':'assertion','original':wrong,'reason':'wrong value','action':'removed'}]
        return artifact
    run_id=runner.run('scorer-selftest-v1',prepare,execute,actor='dedicated scorer selftest')
    result=runner.results(run_id)
    for ordinal,record in enumerate(result['records']):
        name=record['case_id'].removeprefix('scorer-'); artifact=record['artifact']
        if name in ('preflight_failed','missing_human','empty'): continue
        score=0 if name=='semantic_rejected' else 2
        review={'case_id':record['case_id'],'report_hash':digest(artifact['report']),'evidence_hash':digest(artifact['evidence']),
            'rubric_hash':RUBRIC_HASH,'reviewer':'SYNTHETIC human receipt for scorer testing; not real acceptance',
            'reviewer_kind':'agent' if name=='agent_review' else 'human',
            'ratings':[{'inference_id':'i','scores':{k:score for k in ('relevance','counterevidence','causal_restraint')},
                        'reasons':{k:'controlled scorer fixture, not actual human assessment' for k in ('relevance','counterevidence','causal_restraint')}}]}
        runner.review(run_id,ordinal,review)
    result=runner.results(run_id)
    assert len(result['records'])==66 and result['complete']
    for record in result['records']:
        assert record['score']['complete_pass']==(record['case_id'] in ('scorer-correct','scorer-unknown_cost'))
        if record['case_id']=='scorer-blocked': assert record['score']['assertion_pass_rate']==.5
    for row in result['summary']['rounds']:
        assert row['tasks']==11 and row['complete_passes']==2 and row['total_cost'] is None
        assert row['unknown_cost_records']==1 and row['known_tokens']==310 and row['known_model_calls']==31
        assert row['failure_types']['preflight_failed']==1
    result['experiment']={'cases':11,'rounds':3,'variants':2,'expected_passes_per_round_variant':2,
        'independent_reference':'DuckDB COUNT(range(7)) == Python set cardinality','frozen_cases_accessed':0,
        'human_receipts':'synthetic fixtures only; T17 actual human rubric acceptance remains separate','audit':runner.audit()}
    (output/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    return result


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',required=True,type=Path); parser.add_argument('--image',required=True)
    args=parser.parse_args(); result=run(args.output,args.image)
    print(json.dumps({'records':len(result['records']),'rounds':3,'variants':2,'passed':True,'frozen_cases_accessed':0}))


if __name__=='__main__': main()
