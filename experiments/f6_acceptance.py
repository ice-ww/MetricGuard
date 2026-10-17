"""Replay preserved manual failures and new flows against the public service."""
import argparse
from contextlib import redirect_stdout
from datetime import datetime, timedelta, timezone
import gzip
import hashlib
from io import StringIO
import json
import os
from pathlib import Path
import subprocess
from unittest.mock import patch
from uuid import uuid4
import duckdb
from metricguard import TaskService
from metricguard.console import interact
from experiments.t01.snapshots import build_snapshot

ORIGINALS=['20261014-165254-066776','20261014-170326-730523','20261014-171108-970009','20261014-172310-457634','20261014-172339-639002']
LOCAL=timezone(timedelta(hours=8))


def archive_originals() -> list:
    records=[]
    for name in ORIGINALS:
        directory=Path('artifacts/manual-acceptance/runs')/name
        files={p.name:{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'text':p.read_text(encoding='utf-8')} for p in directory.iterdir() if p.is_file() and p.suffix in ('.json','.md')}
        records.append({'directory':str(directory),'files':files})
    Path('docs/validation/f6-original-failures.json.gz').write_bytes(gzip.compress(json.dumps(records,ensure_ascii=False,indent=2).encode(),mtime=0))
    return records


def retention_reference(database: Path, state: dict) -> list:
    with duckdb.connect(str(database),read_only=True) as db:
        users=db.execute('SELECT user_id, registered_at, registration_os FROM users').fetchall()
        sessions=db.execute('SELECT user_id, started_at FROM sessions').fetchall()
    active={(uid,at.astimezone(LOCAL).date()) for uid,at in sessions}; checked=[]
    for evidence in state['evidence']:
        if evidence['parameters'].get('kind')!='system_retention':continue
        for row in evidence['rows']:
            window=state['comparison_window'] if row['period']=='previous' else state['actual_window']
            assert [row['window_start'],row['window_end']]==window
            selected=[(uid,at.astimezone(LOCAL).date()) for uid,at,system in users if window[0]<=at.astimezone(LOCAL).date().isoformat()<window[1] and system==row['registration_os']]
            retained=sum((uid,day+timedelta(days=1)) in active for uid,day in selected)
            assert row['users']==len(selected) and row['retained']==retained
            assert abs(row['retention_rate']-retained/len(selected))<1e-12
            checked.append({'window':window,'system':row['registration_os'],'users':len(selected),'retained':retained})
    assert checked,'Expected independently checkable system_retention profile'
    return checked


def coverage_reference(database: Path, state: dict) -> dict:
    # Enumerate each requested cohort day against raw source completeness timestamps.
    # D1 observes the entire following calendar day, not merely its start.
    with duckdb.connect(str(database),read_only=True) as db:
        source_dates=dict(db.execute('SELECT source, complete_before FROM source_watermarks').fetchall())
    start,end=[datetime.fromisoformat(value).replace(tzinfo=LOCAL) for value in state['requested_window']]
    valid: list[str]=[]
    invalid: list[str]=[]
    day=start
    while day<end:
        enough=(day+timedelta(days=1)<=source_dates['users'] and day+timedelta(days=2)<=source_dates['sessions'])
        (valid if enough else invalid).append(day.date().isoformat());day+=timedelta(days=1)
    expected=[valid[0],(datetime.fromisoformat(valid[-1])+timedelta(days=1)).date().isoformat()] if valid else None
    assert state['coverage']['available_window']==expected
    for gap in state['coverage']['gaps']:
        assert gap['complete_before']==source_dates[gap['source']].astimezone(LOCAL).date().isoformat()
        needed=end+timedelta(days=1 if gap['source']=='sessions' else 0)
        assert gap['required_complete_before']==needed.date().isoformat()
    return {'method':'raw source timestamps + per-cohort-day registration/D1 interval enumeration',
            'source_dates':{key:value.isoformat() for key,value in source_dates.items()},
            'valid_cohort_days':valid,'missing_cohort_days':invalid,'available_window':expected}


def run(case: str, root: Path) -> dict:
    directory=root/case;directory.mkdir(parents=True)
    choices={'comparison_window_required':'1','coverage_scope_required':'2','time_window_conflict':'2','metric_required':'我想看新增用户自然日次日留存，使用刚才提供的日期窗口'}
    original=None; clock=datetime(2026,10,14,17,0,tzinfo=LOCAL)
    if case.startswith('old'):
        index=int(case[3:]); original=json.loads((Path('artifacts/manual-acceptance/runs')/ORIGINALS[index]/'task.json').read_text(encoding='utf-8'))
        database=Path('artifacts/manual-acceptance/data')/original['snapshot_id']/'public/snapshot.duckdb'
        assert hashlib.sha256(database.read_bytes()).hexdigest()==original['snapshot_hash']
        question=original['question'];window=tuple(original['requested_window'])
    else:
        database=build_snapshot(directory/'data',scenario='insufficient',seed=280601 if case=='chain' else 280602,
            base_start=datetime(2026,8,3,tzinfo=LOCAL)).database
        clock=datetime(2026,8,18,23,59,tzinfo=LOCAL)
        if case=='chain':
            question='最近7天新增用户自然日次日留存发生变化，请按系统比较并说明证据限制。';window=('2026-08-10','2026-08-17');choices['coverage_scope_required']='1'
        else:
            question='昨天新增用户自然日次日留存是多少？';window=('2026-08-10','2026-08-17');choices['time_window_conflict']='1'
    image=os.environ['METRICGUARD_TEST_IMAGE']; token=os.environ['ANTHROPIC_AUTH_TOKEN']
    with TaskService(directory/'state',image,{'dev':database},token=token,clock=lambda:clock) as service:
        state=service.run(service.create(question,'dev',window,mode='diagnose'))
        task=state['id']; initial=state; anchor=state['time_anchor']
    # Reopen the actual persisted task; cross midnight for the new chained flow.
    resumed_clock=clock+timedelta(minutes=2) if case=='chain' else clock
    confirmations=[]; output=StringIO()
    with TaskService(directory/'state',image,{'dev':database},token=token,clock=lambda:resumed_clock) as service:
        def answer(prompt):
            pending=service.inspect(task)['pending_question']; value=choices[pending['reason']]
            confirmations.append({'question':pending,'answer':value}); print(prompt+value); return value
        with redirect_stdout(output),patch('builtins.input',answer):interact(service,service.inspect(task))
        exported=service.export_report(task); state=service.inspect(task)
    publication=json.loads((Path(exported['report']).parent/'publication.json').read_text(encoding='utf-8'))
    receipt={'case':case,'original_task':original['id'] if original else None,'question':question,'initial':initial,
             'confirmations':confirmations,'task':state,'publication':publication,'terminal':output.getvalue(),
             'markdown':Path(exported['report']).read_text(encoding='utf-8'),'exported':exported,
             'database':str(database),'snapshot_sha256':hashlib.sha256(database.read_bytes()).hexdigest(),
             'commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
             'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('metricguard').glob('*.py')}}
    result_path=directory/'result.json'
    result_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    assert state['status']=='ended' and state['time_anchor']==anchor
    assert exported['terminal_body'] in output.getvalue() and exported['body'] in receipt['markdown']
    assert 'question_id' not in output.getvalue() and 'coverage_scope_required' not in output.getvalue()
    sources={e['evidence_id']:e for e in state['evidence']}
    for fact in publication['assertions']:
        ref=fact['reference'];assert sources[ref['evidence_id']]['rows'][ref['row']][ref['column']]==fact['value']
    reasons=[c['question']['reason'] for c in confirmations]
    if case=='old0':
        from experiments.t12.check_result import check
        receipt['reference']=check(database,state)
        assert reasons==['comparison_window_required']
    elif case in ('old3','old4'):
        from experiments.t14.check_result import check
        receipt['reference']=check(database,state)
        assert state['actual_window']==['2026-06-08','2026-06-15']
        assert reasons==(['time_window_conflict','comparison_window_required'] if case=='old3' else ['comparison_window_required'])
    elif case in ('old1','chain'):
        receipt['reference']=retention_reference(database,state)
        if case=='old1': assert reasons==['metric_required']
        else:
            assert reasons==['time_window_conflict','comparison_window_required','coverage_scope_required']
            assert state['requested_window']==['2026-08-10','2026-08-17'] and state['actual_window']==['2026-08-10','2026-08-13']
            assert state['comparison_window']==['2026-08-03','2026-08-10']
            assert '不能推广' in exported['body']
    else:
        assert state['analysis_result']=='insufficient_evidence' and state['actual_window'] is None
        assert state['model_calls']==0 and not state['evidence']
        if case=='empty':
            assert state['requested_window']==['2026-08-17','2026-08-18'] and state['coverage']['available_window'] is None
            assert '无可用日期' in exported['body'] and reasons==['time_window_conflict']
        else: assert reasons==['comparison_window_required','coverage_scope_required'] and state['coverage']['decision']=='keep_original'
        receipt['reference']={'no_analysis_query':True,'coverage':coverage_reference(database,state)}
    if case not in ('old2','empty'):
        assert state['outcome']=='facts_available',state['limitations']
        assert state['model_calls']>0 and state['evidence']
    if case=='chain': receipt['coverage_reference']=coverage_reference(database,state)
    receipt['passed']=True
    result_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    return {'case':case,'task':task,'passed':True,'result':str(result_path)}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--cases',nargs='+',default=['old0','old1','old2','old3','old4','chain','empty']);args=parser.parse_args()
    originals=archive_originals();root=Path('artifacts/f6-live')/uuid4().hex;root.mkdir(parents=True);results=[]
    for case in args.cases:
        try: result=run(case,root)
        except Exception as error:result={'case':case,'passed':False,'error_type':type(error).__name__,'error':str(error)}
        results.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
        (root/'summary.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    for original in originals:
        for name,content in original['files'].items(): assert hashlib.sha256((Path(original['directory'])/name).read_bytes()).hexdigest()==content['sha256']
    if not all(r['passed'] for r in results): raise SystemExit(1)


if __name__=='__main__': main()
