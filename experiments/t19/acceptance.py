"""Real sandbox and optional real provider; no formal frozen cases are opened."""
import argparse
from collections import defaultdict
import json
import os
from pathlib import Path
import platform
import subprocess
from typing import Any

import duckdb
import httpx2 as httpx

from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from metricguard.evaluation import file_hash


PROFILE={'action':'profile','table':'users','column':'registration_os','kind':'system_retention'}


def independent_reference(database):
    """Two implementations from raw membership, neither using product metric SQL."""
    with duckdb.connect(str(database),read_only=True) as db:
        users=db.execute('SELECT user_id,registered_at,registration_os FROM users').fetchall()
        sessions=db.execute('SELECT user_id,started_at FROM sessions').fetchall()
        sql=db.execute("""WITH u AS (
          SELECT user_id, registration_os AS os, CAST(registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE) AS d FROM users
        ), s AS (
          SELECT DISTINCT user_id, CAST(started_at AT TIME ZONE 'Asia/Shanghai' AS DATE) AS d FROM sessions
        ) SELECT CASE WHEN u.d < DATE '2026-01-08' THEN 'previous' ELSE 'current' END AS period,
          u.os, COUNT(*) AS users, COUNT(s.user_id) AS retained FROM u LEFT JOIN s ON s.user_id=u.user_id AND s.d=u.d+1
          WHERE u.d>=DATE '2026-01-01' AND u.d<DATE '2026-01-15' GROUP BY period,u.os ORDER BY period,u.os""").fetchall()
    from datetime import timezone,timedelta,date
    zone=timezone(timedelta(hours=8))
    session_days={(uid,ts.astimezone(zone).date()) for uid,ts in sessions}
    expected: dict[tuple[str,str],list[int]]=defaultdict(lambda:[0,0])
    for uid,registered,system in users:
        day=registered.astimezone(zone).date()
        if date(2026,1,1)<=day<date(2026,1,15):
            values=expected[('previous' if day<date(2026,1,8) else 'current',system)]
            values[0]+=1; values[1]+=(uid,day+timedelta(days=1)) in session_days
    assert {tuple(r[:2]):list(r[2:]) for r in sql}==dict(expected)
    return [{'period':p,'os':system,'users':n,'retained':r,'retention_rate':r/n}
            for (p,system),(n,r) in sorted(expected.items())]


def response(value):
    return httpx.Response(200,json={'id':'msg_t19','type':'message','role':'assistant','model':'deepseek-flash',
        'content':[{'type':'text','text':json.dumps(value)}],'stop_reason':'end_turn','stop_sequence':None,
        'usage':{'input_tokens':31,'output_tokens':17}})


def run(output: Path,image: str,real: bool):
    output.mkdir(parents=True,exist_ok=False)
    snapshot=build_snapshot(output/'development-data',scenario='A4',seed=190019)
    reference=independent_reference(snapshot.database)
    def controlled(request):
        shared=json.loads(json.loads(request.content)['system'].split('Shared materials:\n')[1])
        if shared.get('baseline_phase')=='plan': return response({'queries':[PROFILE]})
        if 'last_failure' in shared:
            return response(PROFILE if not shared['evidence'] else {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]})
        return response({'facts':[{'evidence_id':e['evidence_id'],'row':i,'column':k,'value':v}
            for e in shared['evidence'] for i,row in enumerate(e['rows']) for k,v in row.items() if type(v) in (int,float)]})
    token=os.environ['ANTHROPIC_AUTH_TOKEN'] if real else 'controlled'
    with TaskService(output/'service',image,{'development':snapshot.database},token=token,
                     transport=None if real else httpx.MockTransport(controlled)) as service:
        pre=service.prepare_shared('请分析新增用户自然日次日留存的系统结构变化，比较本期与前一期各系统人数和留存表现。',
                                   'development',('2026-01-08','2026-01-15'))
        results: dict[str,Any]={}
        for name,mode in [('baseline','baseline'),('agent','diagnose')]:
            task=service.create_from_shared(pre,mode=mode)
            state=service.run(task)
            artifact=service.comparison_result(task)
            observed=[r for e in state['evidence'] if e['parameters'].get('kind')=='system_retention' for r in e['rows']]
            matches=all(any(r['period']==v['period'] and r['registration_os']==v['os'] and
                           r['users']==v['users'] and r['retained']==v['retained'] and r['retention_rate']==v['retention_rate']
                           for r in observed) for v in reference)
            results[name]={'state':state,'artifact':artifact,'independent_reference_match':matches}
        preflight=service.inspect(pre)
    report={'environment':{'python':platform.python_version(),'platform':platform.platform(),'image':image,
             'uv_lock_sha256':file_hash(Path('uv.lock')),'code_ref':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
             'source_sha256':{str(p).replace('\\','/'):file_hash(p) for p in sorted(Path('metricguard').glob('*.py'))}},
        'model':{'provider':'real' if real else 'controlled','model':'deepseek-flash','endpoint':'https://api.deepseek.com/anthropic',
                 'temperature':0,'sdk_retries':0,'plan_max_output':2048,'report_max_output':1024},
        'limits':preflight['limits'],'development_seed':190019,'snapshot_hash':file_hash(snapshot.database),
        'independent_sql_and_python_agree':True,'reference':reference,'preflight':preflight,'results':results,
        'formal_frozen_accesses':0,'semantic_acceptance':'not_claimed; independent human assessment required for diagnosis'}
    (output/'result.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({name:{'models':r['artifact']['usage']['model_calls'],'queries':r['artifact']['usage']['steps'],
        'outcome':r['state']['outcome'],'reference_match':r['independent_reference_match'],
        'facts_valid':r['state']['report']['validation']['passed']} for name,r in results.items()}))
    if not real:
        assert all(r['independent_reference_match'] and r['state']['report']['validation']['passed'] for r in results.values())
        assert results['baseline']['artifact']['usage']['model_calls']==2
    return report


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--image',required=True); parser.add_argument('--real',action='store_true')
    args=parser.parse_args(); run(args.output,args.image,args.real)


if __name__=='__main__': main()
