"""Build independent frozen data, without invoking any diagnosis or scoring path."""
import argparse
from datetime import datetime,timedelta,timezone
import json
from pathlib import Path
import subprocess
from typing import Any
from experiments.t01.snapshots import build_snapshot
from experiments.t01.references import sql_metrics,python_metrics
from experiments.t05.ledger import DEFAULT_LIMITS
from metricguard.evaluation import EvaluationRunner,file_hash
from metricguard.semantic_rubric import RUBRIC_HASH,digest

ROOT=Path(__file__).resolve().parents[2]
SCHEMA=(ROOT/'experiments/t01/schema.sql').read_text(encoding='utf-8')
DEFINITIONS=json.loads((ROOT/'experiments/t06/corpus.json').read_text(encoding='utf-8'))


def configuration(image: str) -> dict:
    groups={
        'code_hashes':list((ROOT/'metricguard').glob('*.py'))+list((ROOT/'experiments').rglob('*.py')),
        'prompt_hashes':[ROOT/'metricguard/diagnosis.py',ROOT/'metricguard/service.py',ROOT/'experiments/t06/corpus.json'],
        'rule_hashes':[ROOT/'metricguard/semantic_rubric.py',ROOT/'experiments/t04/statistics.py',ROOT/'experiments/t06/config.json',ROOT/'experiments/t02/policy.py'],
        'reference_hashes':list((ROOT/'experiments/t01').glob('*.sql'))+[ROOT/'experiments/t01/references.py']}
    return {'code_ref':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        **{key:{str(p.relative_to(ROOT)).replace('\\','/'):file_hash(p) for p in sorted(paths)} for key,paths in groups.items()},
        'dependency_hash':file_hash(ROOT/'uv.lock'),'model':{'name':'deepseek-flash','endpoint':'https://api.deepseek.com/anthropic',
            'temperature':0,'max_output_tokens':4096,'usage':'actual_or_unknown'},
        'rubric_hash':RUBRIC_HASH,'budgets':dict(DEFAULT_LIMITS),'image':image}


def recipes() -> list[dict]:
    categories=['simple']*6+[kind for kind in ('A1','A2','A3','A4') for _ in range(3)]+['normal']*2+['insufficient']*2+['clarification','recovery']
    result=[]
    for index,category in enumerate(categories):
        instance=(index-6)%3
        start=datetime(2027,1,1,tzinfo=timezone(timedelta(hours=8)))+timedelta(days=index*19)
        result.append({'id':'case-'+digest(['p0-independent-v1',index])[:12],'category':category,
            'scenario':category if category in ('A1','A2','A3','A4','insufficient') else 'normal','seed':810001+index,
            'base_start':start.isoformat(),'new_version':f'8.{instance+1}',
            'crash_probability':(.57,.69,.81)[instance], 'campaign_channel':f'partner-{instance+1}',
            'campaign_growth':(2.6,3.2,3.8)[instance],'campaign_retention':(.11,.16,.21)[instance],
            'campaign_unit_cost':(170,230,290)[instance], 'completion_drop_probability':(.8,.9,1)[instance],
            'current_ios_share':(.61,.67,.72)[instance],'current_android_retention':(.34,.29,.24)[instance],
            'simple_metric':('users','retained','retention_rate','crashed_users','starts','spend_cents')[index%6]})
    return result


def summarize_reference(raw: dict) -> dict:
    """Normalize independent reference outputs into path-neutral business facts."""
    rows=[]
    cohorts: dict[tuple,list[int]]={}
    for row in raw['retention']:
        for cohort_key in ((row['os'],row['version']),(row['os'],None),(None,None)):
            counts=cohorts.setdefault(cohort_key,[0,0,0])
            for i,key in enumerate(('users','retained','crashed_users')): counts[i]+=row[key]
    for (system,version),(users,retained,crashed) in cohorts.items():
        group={k:v for k,v in {'os':system,'version':version}.items() if v is not None}
        rows.append({'group':group,'metrics':{'users':users,'retained':retained,'crashed_users':crashed,
            'retention_rate':retained/users,'crash_affected_rate':crashed/users},'end':raw['coverage']['retention_end']})
    for row in raw['channels']:
        rows.append({'group':{'channel':row['channel']},'metrics':{k:v for k,v in row.items() if k!='channel' and v is not None},'end':raw['coverage']['retention_end']})
    for row in raw['playback']:
        metrics={k:v for k,v in row.items() if k not in ('os','version')}
        metrics.update(observed_completion_rate=row['completions']/row['starts'],independent_completion_rate=row['telemetry_complete']/row['starts'])
        rows.append({'group':{'os':row['os'],'version':row['version'],'population':'play_instances'},'metrics':metrics,'end':raw['coverage']['playback_end']})
    return {'rows':rows,'coverage':raw['coverage']}


def build_case(recipe: dict,output: Path) -> tuple[dict,dict]:
    params={k:v for k,v in recipe.items() if k not in ('id','category','simple_metric')}
    params['base_start']=datetime.fromisoformat(params['base_start'])
    snapshot=build_snapshot(output/recipe['id'],**params)
    first=params['base_start']; current=first+timedelta(days=7); end=first+timedelta(days=14)
    windows={'previous':(first.date().isoformat(),current.date().isoformat()),'current':(current.date().isoformat(),end.date().isoformat())}
    references={}
    for period,window in windows.items():
        relational=sql_metrics(snapshot.database,*window); independent=python_metrics(snapshot.database,*window)
        if relational!=independent: raise ValueError('independent reference disagreement')
        references[period]=summarize_reference(relational)
    category=recipe['category']; required=[]
    def append_fact(metric,value,group,period,right):
        required.append({'context':{'metric':metric,'window':[windows[period][0],right],'group':group,'comparison':period},
                         'value':value,'abs_tol':0 if type(value) is int else 1e-8,'rel_tol':0})
    for period,reference in references.items():
        for row in reference['rows']:
            group=row['group']; selected=[]
            if category=='simple' and period=='current':
                metric=recipe['simple_metric']
                target=({'population':'play_instances','os':'Android','version':recipe['new_version']} if metric=='starts' else
                        {'channel':recipe['campaign_channel']} if metric=='spend_cents' else {})
                if group==target: selected=[metric]
            elif category=='A1' and set(group)=={'os','version'}:
                selected=['users','retained','crashed_users','retention_rate','crash_affected_rate']
            elif category=='A2' and set(group)=={'channel'} and group['channel']!='idle':
                selected=['users','retained','retention_rate','spend_cents','cost_per_new_cents','cost_per_retained_cents']
                row['metrics']['retention_rate']=row['metrics']['retained']/row['metrics']['users']
            elif category=='A3' and group.get('population')=='play_instances':
                selected=['starts','completions','telemetry_complete','missing_complete','observed_completion_rate','independent_completion_rate']
            elif category in ('A4','normal','clarification','recovery','insufficient') and set(group)=={'os'} and (category not in ('clarification','recovery') or period=='current'):
                selected=['users','retained','retention_rate']
            for metric in selected: append_fact(metric,row['metrics'][metric],group,period,row['end'])
    if category=='A4':
        previous={r['group']['os']:r['metrics'] for r in references['previous']['rows'] if set(r['group'])=={'os'}}
        current_rows={r['group']['os']:r['metrics'] for r in references['current']['rows'] if set(r['group'])=={'os'}}
        denominator=sum(r['users'] for r in previous.values())
        standardized=sum(r['users']/denominator*current_rows[system]['retention_rate'] for system,r in previous.items())
        append_fact('baseline_standardized_retention_rate',standardized,{},'current',windows['current'][1])
    explanations={'A1':'version_crash_association','A2':'low_retention_acquisition_growth','A3':'completion_collection_gap',
        'A4':'composition_masks_subgroup_decline','normal':'no_sufficient_anomaly_evidence','insufficient':'insufficient_evidence',
        'simple':'query_result','clarification':'query_result','recovery':'query_result'}
    questions={'A1':'新增用户自然日次日留存出现变化，请检验可能解释和反对证据。',
        'A2':'新增用户增长质量如何？请比较留存与渠道成本并说明限制。',
        'A3':'观测完播率出现变化，请用独立证据检查采集与行为解释。',
        'A4':'新增用户自然日次日留存总体表现如何？请检查分群及构成变化。',
        'normal':'请检查新增用户自然日次日留存是否有足够异常证据。',
        'insufficient':'请分析完整请求窗口的新增用户自然日次日留存；说明资料是否充分。',
        'clarification':'用户表现怎么样？','recovery':'请查询新增用户自然日次日留存并处理可恢复工具错误。'}
    location=({'os':'Android','version':recipe['new_version']} if category in ('A1','A3') else
              {'channel':recipe['campaign_channel']} if category=='A2' else {'os':'Android'} if category=='A4' else {})
    behaviors={'insufficient':['incomplete_coverage_disclosed'],'clarification':['clarified_before_analysis'],'recovery':['recovered_without_duplicate_dispatch']}.get(category,[])
    question=questions.get(category,'')
    if category=='simple':
        names={'users':'新增用户数','retained':'新增用户自然日次日留存人数','retention_rate':'新增用户自然日次日留存率',
               'crashed_users':'新增用户首日崩溃受影响人数','starts':f'Android {recipe["new_version"]} 去重播放开始数','spend_cents':f'{recipe["campaign_channel"]} 渠道同期支出（分）'}
        question='请查询'+names[recipe['simple_metric']]+'并给出可追踪证据。'
    public={'id':recipe['id'],'question':question,'window':list(windows['current']),
        'snapshot':str(snapshot.database.relative_to(output)).replace('\\','/'),'snapshot_id':snapshot.logical_hash,
        'definition':DEFINITIONS,'schema':SCHEMA}
    controls={'clarification_answer':'新增用户自然日次日留存，按已提供窗口。'} if category=='clarification' else {'transient_tool_fault_once':'query_timeout_before_dispatch'} if category=='recovery' else {}
    case={'id':recipe['id'],'category':category,'public':public,'snapshot_id':snapshot.logical_hash,'snapshot_sha256':file_hash(snapshot.database),
        'required':required,'explanation':explanations[category],'localization':location,
        'forbidden':['certain_cause','fraud_proven']+(['no_anomaly','complete_coverage'] if category=='insufficient' else []),
        'behaviors':behaviors,'requires_review':category not in ('simple','clarification','recovery'), 'controls':controls}
    if not required: raise ValueError('empty expected assertions')
    provenance={'recipe':recipe,'logical_hash':snapshot.logical_hash,'snapshot_sha256':file_hash(snapshot.database),
        'reference_hash':digest(references),'reference_agreement':True,'purpose':'frozen_generation_not_diagnosis'}
    return case,provenance


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,required=True); parser.add_argument('--registry',type=Path,required=True)
    parser.add_argument('--image',required=True); parser.add_argument('--version',default='p0-independent-v1'); args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    cases=[]; provenance=[]
    for recipe in recipes():
        case,source=build_case(recipe,args.output); cases.append(case); provenance.append(source)
    config=configuration(args.image)
    runner=EvaluationRunner(args.registry,repository=ROOT)
    frozen=runner.freeze(args.version,'metricguard-p0-independent',cases,config)
    private=runner.access(args.version,actor='freeze builder',purpose='generation_audit')
    (args.output/'bundle.json').write_text(json.dumps(private,ensure_ascii=False,indent=2),encoding='utf-8')
    (args.output/'provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2),encoding='utf-8')
    (args.output/'public-tasks.json').write_text(json.dumps([c['public'] for c in cases],ensure_ascii=False,indent=2),encoding='utf-8')
    (args.output/'freeze-record.json').write_text(json.dumps({'freeze':frozen,'audit':runner.audit(),'status':runner.status(args.version)},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'freeze':frozen,'reference_agreements':len(provenance),'diagnosis_runs':0}))


if __name__=='__main__': main()
