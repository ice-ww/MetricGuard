"""Deterministic publication from trusted evidence; semantic judgement stays separate."""
from copy import deepcopy
from dataclasses import asdict
from typing import Any
from experiments.t08.contract import EvidenceStore, EvidenceResult, FactContext, Assertion, Reference, ChartSpec
from metricguard.semantic_rubric import RUBRIC, RUBRIC_HASH, digest


def evidence_store(evidence: list[dict]) -> EvidenceStore:
    store=EvidenceStore()
    for raw in evidence:
        contexts={p:FactContext(v['metric'],tuple(v['window']),v['group'],v['comparison']) for p,v in raw['contexts'].items()}
        store.add(EvidenceResult(raw['evidence_id'],raw['tool'],raw['parameters'],raw['source'],raw['snapshot_id'],
            raw['columns'],tuple(raw['rows']),contexts,tuple(raw['window']),raw['group'],raw['sample'],tuple(raw['limitations']),raw['truncated'],
            raw.get('kind','query'),tuple(raw.get('whole_population_fields',[]))))
    return store


def reference(raw: dict) -> Reference:
    if not isinstance(raw,dict) or set(raw)!={'evidence_id','row','column'} or type(raw['row']) is not int or raw['row']<0:
        raise ValueError('invalid_reference')
    if any(not isinstance(raw[k],str) or not raw[k] for k in ('evidence_id','column')):
        raise ValueError('invalid_reference')
    return Reference(**raw)


def publish(evidence: list[dict], draft: dict) -> dict[str,Any]:
    if not isinstance(draft,dict) or set(draft)!={'assertions','inferences','charts'}:
        raise ValueError('invalid_report_shape')
    if any(not isinstance(draft[k],list) for k in draft) or len(draft['assertions'])>10000 or len(draft['inferences'])>20:
        raise ValueError('invalid_report_size')
    original=deepcopy(draft)
    store=evidence_store(evidence)
    accepted=[]; rejected=[]; inferences=[]; charts=[]; seen=set()
    def reject(kind, item, reason):
        rejected.append({'kind':kind,'original':deepcopy(item),'reason':reason,'action':'removed'})
    for item in draft['assertions']:
        try:
            if not isinstance(item,dict) or set(item)!={'assertion_id','reference','context','value','scope'}:
                raise ValueError('invalid_assertion_shape')
            identity=item['assertion_id']
            if not isinstance(identity,str) or not identity or identity in seen:
                raise ValueError('invalid_or_duplicate_assertion_id')
            seen.add(identity)
            context=item['context']
            if not isinstance(context,dict) or set(context)!={'metric','window','group','comparison'}:
                raise ValueError('invalid_context_shape')
            assertion=Assertion(identity,reference(item['reference']),FactContext(context['metric'],tuple(context['window']),context['group'],context['comparison']),item['value'],item['scope'])
            validation=store.validate(assertion)
            if not validation.passed:
                raise ValueError(','.join(validation.errors))
            accepted.append(deepcopy(item))
        except (ValueError,TypeError,KeyError) as error:
            reject('assertion',item,str(error))
    ids={a['assertion_id'] for a in accepted}
    seen=set()
    for item in draft['inferences']:
        try:
            if not isinstance(item,dict) or set(item)!={'inference_id','text','supporting_assertion_ids','opposing_assertion_ids','unexcluded_factors'}:
                raise ValueError('invalid_inference_shape')
            identity=item['inference_id']
            if not isinstance(identity,str) or not identity or identity in seen:
                raise ValueError('invalid_or_duplicate_inference_id')
            seen.add(identity)
            if not isinstance(item['text'],str) or not item['text'].strip():
                raise ValueError('empty_inference')
            for key in ('supporting_assertion_ids','opposing_assertion_ids','unexcluded_factors'):
                if not isinstance(item[key],list) or any(not isinstance(v,str) or not v.strip() for v in item[key]):
                    raise ValueError('invalid_inference_details')
            if not item['supporting_assertion_ids'] or not set(item['supporting_assertion_ids']+item['opposing_assertion_ids'])<=ids:
                raise ValueError('unsupported_inference_reference')
            inferences.append({**deepcopy(item),'semantic_status':'pending_review'})
        except (ValueError,TypeError,KeyError) as error:
            reject('inference',item,str(error))
    chart_ids=set()
    for item in draft['charts']:
        try:
            if len(draft['charts'])>3:
                raise ValueError('chart_limit')
            if not isinstance(item,dict) or set(item)!={'chart_id','kind','x_refs','y_refs'}:
                raise ValueError('invalid_chart_shape')
            if not isinstance(item['chart_id'],str) or not item['chart_id'] or item['chart_id'] in chart_ids:
                raise ValueError('invalid_or_duplicate_chart_id')
            chart_ids.add(item['chart_id'])
            chart=ChartSpec(item['chart_id'],item['kind'],tuple(reference(r) for r in item['x_refs']),tuple(reference(r) for r in item['y_refs']))
            from metricguard.evidence_charts import render_svg
            for resolved in store.render_charts((chart,)):
                rendered=asdict(resolved)
                charts.append({**rendered,'svg':render_svg(rendered)})
        except (ValueError,TypeError,KeyError) as error:
            reject('chart',item,str(error))
    denominator=len(draft['assertions'])
    return {'protocol_version':'publication-v1','rubric_version':RUBRIC['version'],'rubric_hash':RUBRIC_HASH,
        'original':original,'evidence_hash':digest(evidence),'assertions':accepted,'inferences':inferences,'charts':charts,
        'rejections':rejected,'counts':{'assertions_submitted':denominator,'assertions_published':len(accepted),
            'inferences_submitted':len(draft['inferences']),'inferences_published':len(inferences),'removed':len(rejected)},
        'assertion_pass_rate':len(accepted)/denominator if denominator else None,
        'citation_coverage':sum(bool(i.get('supporting_assertion_ids')) for i in draft['inferences'] if isinstance(i,dict))/len(draft['inferences']) if draft['inferences'] else None,
        'status':'rejected' if not accepted else 'degraded' if rejected else 'mechanically_valid',
        'semantic_status':'pending_review' if inferences else 'not_applicable',
        'limitations':['Mechanical validity does not prove SQL business semantics, relevance, counterevidence handling or causation.']}
