"""Real CLI rendering checks on development snapshots with independent references."""
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from uuid import uuid4
import duckdb
from metricguard import TaskService
from experiments.t01.snapshots import build_snapshot

QUESTIONS = {
    'simple': '查询新增用户数',
    'A1': '新增用户自然日次日留存变化，请检验版本崩溃相关解释与反对证据。',
    'A2': '新增用户自然日次日留存与渠道增长、成本变化，请检验可能解释及反对证据。',
    'A3': '观测完播率出现变化，请用独立证据检验采集与行为解释。',
    'A4': '新增用户自然日次日留存变化，请检验系统结构与分群表现及反对证据。',
}


def run(case: str, root: Path, image: str) -> dict:
    directory = root / case
    directory.mkdir(parents=True)
    database = build_snapshot(directory/'data', scenario='normal' if case=='simple' else case,
        seed=270100 + list(QUESTIONS).index(case), base_start=datetime(2026,7,3,tzinfo=timezone(timedelta(hours=8)))).database
    command = [sys.executable,'-m','metricguard','--state-dir',str(directory/'state'),'--image',image,
        '--snapshot','dev='+str(database),'chat',QUESTIONS[case],'dev','--window','2026-07-10','2026-07-17','--mode','diagnose']
    if case != 'simple': command += ['--comparison-window','2026-07-03','2026-07-10']
    process = subprocess.run(command,input='',text=True,encoding='utf-8',capture_output=True,
        env={**os.environ,'PYTHONUTF8':'1'},timeout=240)
    (directory/'terminal.txt').write_text(process.stdout+process.stderr,encoding='utf-8')
    match = re.search(r'inspect ([a-f0-9]{32})',process.stdout)
    assert process.returncode==0 and match is not None, process.stdout+process.stderr
    with TaskService(directory/'state',image,{'dev':database},token=os.environ['ANTHROPIC_AUTH_TOKEN']) as service:
        task=match.group(1); before=service.inspect(task)
        exported=service.export_report(task); state=service.inspect(task)
        assert before['model_calls']==state['model_calls'] and before['tool_calls']==state['tool_calls']
    publication=json.loads((Path(exported['report']).parent/'publication.json').read_text(encoding='utf-8'))
    receipt={'case':case,'task':state,'publication':publication,'terminal':process.stdout,'exported':exported,
        'commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
        'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('metricguard').glob('*.py')}}
    output=directory/'result.json'
    output.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    assert state['status']=='ended' and state['outcome']=='facts_available',state['limitations']
    assert exported['terminal_body'] in process.stdout
    assert publication['status']=='mechanically_valid'
    sources={e['evidence_id']:e for e in state['evidence']}
    for a in publication['assertions']:
        ref=a['reference']; assert sources[ref['evidence_id']]['rows'][ref['row']][ref['column']]==a['value']
    if case=='simple':
        with duckdb.connect(str(database),read_only=True) as db:
            row=db.execute("SELECT COUNT(DISTINCT user_id) FROM users WHERE registered_at>=TIMESTAMPTZ '2026-07-10 00:00:00+08:00' AND registered_at<TIMESTAMPTZ '2026-07-17 00:00:00+08:00'").fetchone()
            assert row is not None
            count=row[0]
        assert f'新增用户数：{count} 人' in exported['body']
        receipt['reference']={'new_users':count}
    else:
        if case=='A1':
            from experiments.t12.check_result import check
            receipt['reference']=check(database,state)
        elif case=='A2':
            from experiments.t13.check_result import check
            receipt['reference']=check(database,state)
        elif case=='A3':
            from experiments.t14.check_result import check
            receipt['reference']=check(database,state)
        else:
            from experiments.t15.check_result import check as check_system
            receipt['reference']=check_system(state,database)
        assert all(word in exported['body'] for word in ('支持依据','反对证据','未排除因素','未证明因果'))
    receipt['passed']=True
    output.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    return {'case':case,'task':task,'assertions':len(publication['assertions']),'artifact':str(output),'passed':True}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--cases',nargs='+',choices=list(QUESTIONS),default=list(QUESTIONS))
    args=parser.parse_args();root=Path('artifacts/f5-live')/uuid4().hex;root.mkdir(parents=True)
    results=[]
    for case in args.cases:
        try: result=run(case,root,os.environ['METRICGUARD_TEST_IMAGE'])
        except Exception as error: result={'case':case,'passed':False,'error_type':type(error).__name__,'error':str(error)}
        results.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
        (root/'summary.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    if not all(r['passed'] for r in results): raise SystemExit(1)


if __name__=='__main__': main()
