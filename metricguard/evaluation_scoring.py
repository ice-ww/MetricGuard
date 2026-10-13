"""Independent outcome scoring over T08, without the T17 publication implementation."""
import math
from experiments.t08.contract import Assertion, EvidenceResult, EvidenceStore, FactContext, Reference
from metricguard.semantic_rubric import RUBRIC_HASH, digest, validate_review


def context(raw: dict) -> FactContext:
    return FactContext(raw['metric'],tuple(raw['window']),raw['group'],raw['comparison'])


def numeric(value) -> bool:
    return type(value) in (int,float) and math.isfinite(value)


def usage(raw: dict) -> dict:
    if set(raw)!={'seconds','steps','model_calls','tokens','cost'}:
        raise ValueError('usage fields required')
    for key,value in raw.items():
        if value is None and key in ('steps','model_calls','tokens','cost'):
            continue
        if not numeric(value) or value<0 or (key in ('steps','model_calls','tokens') and type(value) is not int):
            raise ValueError('invalid usage')
    return raw


def score(case: dict, artifact: dict, review: dict | None = None) -> dict:
    result={'case_id':case['id'],'category':case['category'],'attribution_hit':False,'complete_pass':False,
        'semantic_status':'pending','assertion_count':0,'valid_assertion_count':0,'assertion_pass_rate':None,
        'citation_count':0,'inference_count':0,'citation_coverage':None,'required_count':len(case['required']),
        'matched_count':0,'observation_count':0,'valid_observation_count':0,'blocked_count':0,'failure_types':[],'rubric_hash':RUBRIC_HASH}
    try:
        _score(case,artifact,review,result)
    except (ValueError,TypeError,KeyError,IndexError,OverflowError,AttributeError) as error:
        result['complete_pass']=False
        result['failure_types'].append('invalid_artifact:'+str(error))
    if result['inference_count']:
        result['citation_coverage']=result['citation_count']/result['inference_count']
    return result


def _score(case: dict, artifact: dict, review: dict | None, result: dict) -> None:
    report=artifact.get('report',{})
    submitted=report.get('assertions',[])
    blocked=report.get('blocked',[])
    if not isinstance(submitted,list) or not isinstance(blocked,list): raise ValueError('invalid assertion collection')
    original_items=submitted+[item.get('original',{}) for item in blocked if isinstance(item,dict) and item.get('kind')=='assertion']
    result['assertion_count']=len(original_items)
    result['blocked_count']=len(blocked)
    result['assertion_pass_rate']=0 if original_items else None
    if artifact.get('adapter_error'): result['failure_types'].append('adapter_output_invalid')
    if artifact['preflight']['status']!='ok':
        result['failure_types'].append('preflight_failed')
        return
    store=EvidenceStore()
    for raw in artifact['evidence']:
        if case.get('snapshot_id') and raw['snapshot_id']!=case['snapshot_id']:
            raise ValueError('snapshot mismatch')
        store.add(EvidenceResult(raw['evidence_id'],raw['tool'],raw['parameters'],raw['source'],raw['snapshot_id'],
            raw['columns'],tuple(raw['rows']),{k:context(v) for k,v in raw['contexts'].items()},
            tuple(raw['window']),raw['group'],raw['sample'],tuple(raw['limitations']),raw['truncated'],
            raw.get('kind','query'),tuple(raw.get('whole_population_fields',[]))))
    facts=[]; published=[]
    for index,f in enumerate(original_items):
        try:
            ref=Reference(**f['reference'])
            if not isinstance(f['assertion_id'],str) or not f['assertion_id'] or not isinstance(ref.evidence_id,str) or not isinstance(ref.column,str):
                raise ValueError('invalid assertion identity')
            facts.append(Assertion(f['assertion_id'],ref,context(f['context']),f['value'],f['scope']))
            published.append(index<len(submitted))
        except (ValueError,TypeError,KeyError):
            result['failure_types'].append('malformed_assertion')
    checked=store.validate_report(tuple(facts))
    result['valid_assertion_count']=checked.valid_count
    result['assertion_pass_rate']=checked.valid_count/len(original_items) if original_items else None
    if not checked.passed or not submitted:
        result['failure_types'].append('assertion_validation')
    valid=[f for f,v,is_published in zip(facts,checked.results,published,strict=True) if v.passed and is_published]
    for required in case['required']:
        if any(digest(required['context'])==digest(f.context.__dict__) and
               math.isclose(f.value,required['value'],abs_tol=required['abs_tol'],rel_tol=required['rel_tol']) for f in valid):
            result['matched_count']+=1
    if not case['required'] or result['matched_count']!=len(case['required']):
        result['failure_types'].append('required_assertions_missing_or_wrong')
    observations=report.get('observations',[]); valid_observations=[]
    result['observation_count']=len(observations)
    for observation in observations:
        try:
            ref=Reference(**observation['reference']); source=store.get(ref.evidence_id)
            if type(ref.row) is not int or ref.row<0 or not isinstance(observation['value'],str): raise ValueError('invalid observation')
            if source.rows[ref.row][ref.column]!=observation['value'] or source.contexts[ref.pointer]!=context(observation['context']):
                raise ValueError('observation mismatch')
            valid_observations.append(observation)
        except (ValueError,TypeError,KeyError,IndexError):
            result['failure_types'].append('observation_validation')
    result['valid_observation_count']=len(valid_observations)
    for required in case.get('required_observations',[]):
        if not any(digest(required['context'])==digest(o['context']) and required['value']==o['value'] for o in valid_observations):
            result['failure_types'].append('required_observation_missing_or_wrong')
    ids={f.assertion_id for f in valid}
    inference_ids=set()
    if not isinstance(report['inferences'],list): raise ValueError('invalid inference collection')
    result['inference_count']=len(report['inferences'])
    for inference in report['inferences']:
        identity=inference['inference_id']
        if not isinstance(identity,str) or not identity or identity in inference_ids or not inference['text'].strip():
            raise ValueError('invalid inference')
        inference_ids.add(identity)
        for key in ('supporting_assertion_ids','opposing_assertion_ids','unexcluded_factors'):
            if not isinstance(inference[key],list) or any(not isinstance(v,str) or not v.strip() for v in inference[key]):
                raise ValueError('invalid inference references')
        support=inference['supporting_assertion_ids']; opposition=inference['opposing_assertion_ids']
        result['citation_count']+=bool(support)
        if not support or not set(support+opposition)<=ids:
            result['failure_types'].append('inference_reference')
    result['attribution_hit']=case['category'] in ('A1','A2','A3','A4') and report['explanation']==case['explanation']
    if report['explanation']!=case['explanation']:
        result['failure_types'].append('explanation')
    if any(report['localization'].get(k)!=v for k,v in case['localization'].items()):
        result['failure_types'].append('localization')
    if set(case['forbidden']) & (set(report['conclusions'])|{report['explanation']}):
        result['failure_types'].append('forbidden_conclusion')
    if not set(case['behaviors'])<=set(report['behaviors']):
        result['failure_types'].append('behavior')
    for item in report['blocked']:
        if item.get('kind') not in ('assertion','inference','conclusion') or not item.get('original') or not isinstance(item.get('reason'),str) or not item['reason'].strip() or item.get('action') not in ('removed','downgraded'):
            raise ValueError('blocked original and reason required')
    result['blocked_count']=len(report['blocked'])
    if result['blocked_count']:
        result['failure_types'].append('blocked_or_downgraded')
    if artifact['safety_passed'] is not True:
        result['failure_types'].append('safety_failed_or_unverified')
    if inference_ids:
        if review is not None:
            if review['case_id']!=case['id'] or review['report_hash']!=digest(report) or review['evidence_hash']!=digest(artifact['evidence']) or review['rubric_hash']!=RUBRIC_HASH:
                raise ValueError('review binding mismatch')
            assessed=validate_review(inference_ids,review['reviewer'],review['reviewer_kind'],review['ratings'])
            result['semantic_status']=assessed['status']
        if result['semantic_status']!='passed':
            result['failure_types'].append('semantic_'+result['semantic_status'])
    elif case['requires_review']:
        result['failure_types'].append('missing_inference')
    else:
        result['semantic_status']='not_applicable'
    result['complete_pass']=not result['failure_types']
