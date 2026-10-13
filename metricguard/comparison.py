"""Real shared preparation and separately accounted evaluation artifacts."""
from copy import deepcopy
import json
from typing import Any, TYPE_CHECKING

from metricguard.semantic_rubric import digest

if TYPE_CHECKING:
    from metricguard.service import TaskService


SHARED_FIELDS=('question','effective_question','snapshot_id','snapshot_hash','requested_window','actual_window',
               'definition','schema','watermarks','retrieval','limitations','outcome','pending_question')


def measured_usage(attempts: list[dict], seconds: float) -> dict[str, Any]:
    models=[a for a in attempts if a['kind']=='model']
    known=all(a['actual'] is not None for a in models)
    estimates=[json.loads(a['result']).get('fee_usd_range') if a['result'] else None for a in models]
    return {'seconds':seconds,'steps':sum(a['kind']=='tool' for a in attempts),'model_calls':len(models),
            'tokens':sum(a['actual'] for a in models) if known else None,
            # Provider returns estimates, never an invoice. Unknown actual fees are not zero.
            'cost':None if models else 0,
            'cost_estimate_usd':{'minimum':sum(e['minimum'] for e in estimates if e),
                                 'maximum':sum(e['maximum'] for e in estimates if e)} if all(estimates) else None,
            'known_tokens':sum(a['actual'] for a in models if a['actual'] is not None),
            'unknown_usage_calls':sum(a['actual'] is None for a in models),
            'input_tokens':sum(json.loads(a['result'])['usage']['input_total'] for a in models) if known else None}


def protocol_usage(usage: dict) -> dict:
    return {key:usage[key] for key in ('seconds','steps','model_calls','tokens','cost')}


def prepare_shared(service: 'TaskService', question: str, snapshot_id: str, window) -> str:
    task=service.create(question,snapshot_id,window)
    with service.ledger.connect() as db:
        db.execute("UPDATE tasks SET status='running' WHERE id=?",(task,))
    service.ledger.start_activity(task)
    failed=False
    try:
        service._prepare({'task':task})
        data=service._data(task)
        failed=bool(data['outcome'] or data['pending_question'] or not data['actual_window'])
    except Exception as error:
        failed=True; data=service._data(task)
        data['outcome']='insufficient_evidence'
        data['limitations'].append('preflight:'+type(error).__name__)
        service._save(task,data)
    finally:
        service.ledger.accrue_activity(task,stop=True)
        with service.ledger.connect() as db:
            db.execute("UPDATE tasks SET status='ended' WHERE id=?",(task,))
    data=service._data(task); ledger=service.ledger.inspect(task)
    materials={k:deepcopy(data.get(k)) for k in SHARED_FIELDS}
    data['prepared_comparison']={'failed':failed,'materials_hash':digest(materials),
        'usage':measured_usage(ledger['attempts'],ledger['active'])}
    service._save(task,data)
    service._event(task,'shared_preflight_completed',data['prepared_comparison'])
    return task


def create_from_shared(service: 'TaskService', prepared: str, mode: str) -> str:
    if mode not in ('diagnose','baseline'): raise ValueError('comparison mode required')
    source=service.inspect(prepared)
    if source['status']!='ended' or 'prepared_comparison' not in source:
        raise ValueError('completed shared preflight required')
    task=service.create(source['question'],source['snapshot_id'],
                        tuple(source['requested_window']) if source['requested_window'] else None,mode=mode)
    data=service._data(task)
    if data['snapshot_hash']!=source['snapshot_hash']: raise ValueError('shared snapshot changed')
    data.update({k:deepcopy(source.get(k)) for k in SHARED_FIELDS})
    data['shared_preflight']={**deepcopy(source['prepared_comparison']),'source_task':prepared}
    if data['shared_preflight']['failed']:
        data['outcome']='insufficient_evidence'; data['pending_question']=None
    # Charge inherited work to both budgets without dispatching it a second time.
    with service.ledger.connect() as db:
        db.execute('UPDATE tasks SET active=?,limits=?,parent=? WHERE id=?',
                   (source['active'],json.dumps(source['limits']),prepared,task))
        for i,a in enumerate(source['attempts']):
            db.execute('INSERT INTO attempts VALUES(?,?,?,?,?,?,?,?)',
                (task+':shared:'+str(i),task,'shared:'+a['operation'],a['kind'],a['reserved'],a['actual'],a['state'],a['result']))
    service._save(task,data)
    service._event(task,'shared_materials_attached',data['shared_preflight'])
    return task


def comparison_result(service: 'TaskService', task: str) -> dict[str, Any]:
    data=service.inspect(task)
    if data['status'] not in ('ended','failed','interrupted') or 'shared_preflight' not in data:
        raise ValueError('terminal comparison task required')
    preflight=data['shared_preflight']; attempts=[a for a in data['attempts'] if not a['operation'].startswith('shared:')]
    analysis=measured_usage(attempts,max(0,data['active']-preflight['usage']['seconds']))
    report=data.get('report') or {}; assertions=[]
    for i,fact in enumerate(report.get('facts',[])):
        assertions.append({'assertion_id':str(i),'reference':{'evidence_id':fact['evidence_id'],
            'row':fact['row'],'column':fact['column']},'context':fact['context'],'value':fact['value'],'scope':'cell'})
    for rejected in report.get('rejected_facts',[]):
        assertions.append({'assertion_id':'rejected:'+str(rejected['index']),'rejection':rejected})
    return {'task_id':task,'variant':'baseline' if data['mode']=='baseline' else 'agent',
        'shared_materials_hash':preflight['materials_hash'],
        'preflight':{**protocol_usage(preflight['usage']),'status':'failed' if preflight['failed'] else 'ok'},
        'usage':protocol_usage(analysis),'usage_detail':analysis,
        'end_to_end':measured_usage(data['attempts'],data['active']),
        'evidence':data['evidence'],'report':{'assertions':assertions,'inferences':[],
            'explanation':report.get('analysis_result','insufficient_evidence'),'localization':{},
            'conclusions':[],'behaviors':[],'blocked':[]},
        'published_report':report,'query_results':data.get('baseline_results',[]),
        'safety_passed':bool(data['evidence']) and not report.get('rejected_facts') and
            all(r.get('status')=='ok' and r.get('cleanup_verified') is True for r in data.get('baseline_results',[])),
        'semantic_status':'requires_independent_human_review'}
