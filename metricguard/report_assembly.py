"""Assemble publications from executed business tools, never evaluation answers."""
from copy import deepcopy
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from typing import Any

from experiments.t08.contract import Reference
from metricguard.metric_profiles import is_business_profile


def canonicalize(evidence: dict, window: list[str]) -> dict:
    """Only reviewed business profiles carry known metric/group semantics."""
    if not is_business_profile(evidence['parameters']):
        return evidence
    kind=evidence['parameters']['kind']
    aliases={'crash_rate':'crash_affected_rate','observed_completed':'completions',
             'independent_complete':'telemetry_complete'}
    contexts={}
    for i,row in enumerate(evidence['rows']):
        period=row.get('period','current')
        interval=[row.get('window_start',evidence['window'][0] if period=='previous' else window[0]),
                  row.get('window_end',window[0] if period=='previous' else window[1])]
        group={}
        if kind in ('cohort_health','system_retention','retained_user_counts'):
            group={k:row[v] for k,v in [('os','registration_os'),('version','registration_version')] if v in row}
        elif kind in ('channel_health','channel_spend'): group={'channel':row['channel']}
        elif kind in ('playback_events','playback_progress','play_start_counts'):
            group={'os':row['actual_os'],'version':row['actual_version'],'population':'play_instances'}
        elif kind=='crash_versions':
            # Raw cross-attribution rows are not yet actual-system totals.
            group={k:row[k] for k in ('registration_os','registration_version','actual_os','actual_version')}
        elif kind=='releases': group={'os':row['os'],'version':row['version']}
        if any(value is None for value in group.values()):
            # Retain opaque raw-profile contexts when attribution is unknown.
            return evidence
        for column in row:
            metric=aliases.get(column,column)
            if kind=='crash_versions': metric='cross_attributed_'+column
            contexts[Reference(evidence['evidence_id'],i,column).pointer]={
                'metric':metric,'window':interval,'group':group,'comparison':period}
    evidence['contexts']=contexts
    return evidence


def derived_evidence(evidence: list[dict], window: list[str], task: str, watermarks: list) -> dict | None:
    rows: list[dict]=[]; contexts={}; provenance=[]
    identity=task+':derived:v1'
    from metricguard.playback_diagnosis import playback_diagnosis
    playback=playback_diagnosis(evidence,watermarks,window)
    def add(metric, value, interval, group, period, sources, absence=None):
        if type(value) not in (int,float): return
        index=len(rows); rows.append({'value':value})
        contexts[Reference(identity,index,'value').pointer]={
            'metric':metric,'window':interval,'group':group,'comparison':period}
        provenance.append({'row':index,'source_references':sources,**({'absence_proof':absence} if absence else {})})
    for source in evidence:
        if not is_business_profile(source['parameters']) or source['truncated']: continue
        kind=source['parameters']['kind']
        if any(c['metric'].startswith('profile:') for c in source['contexts'].values()): continue
        if kind=='crash_versions':
            crashes_by_group: dict[tuple,list]=defaultdict(list)
            for i,row in enumerate(source['rows']):
                crashes_by_group[(row['period'],row['actual_os'],row['actual_version'])].append((i,row))
            health=next((e for e in evidence if e['parameters'].get('kind')=='cohort_health' and not e['truncated']
                         and all(not c['metric'].startswith('profile:') for c in e['contexts'].values())),None)
            keys=set(crashes_by_group)
            if health:
                keys.update((r['period'],r['registration_os'],r['registration_version']) for r in health['rows'])
            for period,system,version in sorted(keys):
                values=crashes_by_group.get((period,system,version),[])
                exemplar=next((r for e in ([health] if health else [source]) for r in e['rows'] if r['period']==period),None)
                if exemplar:
                    refs=[{'evidence_id':source['evidence_id'],'row':i,'column':'crashed_users'} for i,_ in values]
                    absence=None
                    if not values and health:
                        refs=[{'evidence_id':health['evidence_id'],'row':i,'column':'users'} for i,r in enumerate(health['rows'])
                              if (r['period'],r['registration_os'],r['registration_version'])==(period,system,version)]
                        absence={'rule':'complete_actual_crash_profile_has_no_matching_group',
                                 'evidence_id':source['evidence_id'],'truncated':False,
                                 'match':{'period':period,'actual_os':system,'actual_version':version},
                                 'window':[exemplar['window_start'],exemplar['window_end']]}
                    add('actual_first_day_crashed_users',sum(r['crashed_users'] for _,r in values),
                        [exemplar['window_start'],exemplar['window_end']],{'os':system,'version':version},period,refs,absence)
            continue
        if kind=='cohort_health':
            for period in ('previous','current'):
                values=[(i,r) for i,r in enumerate(source['rows']) if r['period']==period]
                for system in sorted({r['registration_os'] for _,r in values}):
                    selected=[(i,r) for i,r in values if r['registration_os']==system]
                    users=sum(r['users'] for _,r in selected)
                    if not users: continue
                    interval=[selected[0][1]['window_start'],selected[0][1]['window_end']]
                    refs=[{'evidence_id':source['evidence_id'],'row':i,'column':c} for i,_ in selected for c in ('users','retained')]
                    retained=sum(r['retained'] for _,r in selected)
                    for metric,value in [('users',users),('retained',retained),('retention_rate',retained/users)]:
                        add(metric,value,interval,{'os':system},period,refs)
            continue
        if kind in ('playback_events','playback_progress'):
            if not playback or playback['missing_evidence']: continue
            for i,row in enumerate(source['rows']):
                peer=next((other for other in evidence if other['parameters'].get('kind')=='playback_events' and not other['truncated']),None)
                matched=next(((j,r) for j,r in enumerate(peer['rows']) if all(r[k]==row[k] for k in ('period','actual_os','actual_version'))),None) if peer else None
                if peer and matched and matched[1]['starts']:
                    metric='observed_completion_rate' if kind=='playback_events' else 'independent_completion_rate'
                    numerator='observed_completed' if kind=='playback_events' else 'independent_complete'
                    context=source['contexts'][Reference(source['evidence_id'],i,numerator).pointer]
                    add(metric,row[numerator]/matched[1]['starts'],context['window'],context['group'],row['period'],
                        [{'evidence_id':source['evidence_id'],'row':i,'column':numerator},
                         {'evidence_id':peer['evidence_id'],'row':matched[0],'column':'starts'}])
                    if kind=='playback_progress':
                        add('missing_complete',row['independent_complete_without_event'],context['window'],context['group'],row['period'],
                            [{'evidence_id':source['evidence_id'],'row':i,'column':'independent_complete_without_event'},
                             {'evidence_id':peer['evidence_id'],'row':matched[0],'column':'invalid_alignment'}])
            continue
        if kind not in ('system_retention','channel_health','retained_user_counts'): continue
        by_period={p:[(i,r) for i,r in enumerate(source['rows']) if r.get('period','current')==p] for p in ('previous','current')}
        totals={p:sum(r['users'] for _,r in values) for p,values in by_period.items()}
        refs=[{'evidence_id':source['evidence_id'],'row':i,'column':c}
              for i,r in enumerate(source['rows']) for c in ('users','retained')]
        for period,values in by_period.items():
            if not values or not totals[period]: continue
            interval=[values[0][1].get('window_start',window[0]),values[0][1].get('window_end',window[1])]
            for i,row in values:
                group={'channel':row['channel']} if kind=='channel_health' else {'os':row['registration_os']}
                if kind!='retained_user_counts': add('new_user_share',row['users']/totals[period],interval,group,period,refs)
            if kind in ('system_retention','retained_user_counts'):
                retained=sum(r['retained'] for _,r in values)
                for metric,value in [('users',totals[period]),('retained',retained),('retention_rate',retained/totals[period])]:
                    add(metric,value,interval,{},period,refs)
        if kind=='system_retention' and all(totals.values()):
            previous={r['registration_os']:r for _,r in by_period['previous']}
            current={r['registration_os']:r for _,r in by_period['current']}
            if previous.keys()==current.keys() and all(r['users'] for r in current.values()):
                value=sum(r['users']/totals['previous']*current[system]['retention_rate'] for system,r in previous.items())
                add('baseline_standardized_retention_rate',value,window,{},'current',refs)
    if not rows: return None
    return {'evidence_id':identity,'tool':'deterministic_derivation','parameters':{'version':'publication-derivation-v1',
            'provenance':provenance,'input_evidence_ids':[e['evidence_id'] for e in evidence if is_business_profile(e['parameters'])]},
            'source':'Complete executed profiles; pooled counts, actual crash attribution, shares and descriptive rates.',
            'snapshot_id':evidence[0]['snapshot_id'],'columns':{'value':'number'},'rows':rows,'contexts':contexts,
            'window':[min(c['window'][0] for c in contexts.values()),max(c['window'][1] for c in contexts.values())],
            'group':{},'sample':{'returned_rows':len(rows)},'truncated':False,
            'limitations':['Derived descriptive values; no binomial inference or causal identification.']}


def row_references(value: Any) -> set[tuple[str,int]]:
    found=set()
    if isinstance(value,dict):
        if isinstance(value.get('evidence_id'),str) and type(value.get('row')) is int:
            found.add((value['evidence_id'],value['row']))
        for child in value.values(): found.update(row_references(child))
    elif isinstance(value,list):
        for child in value: found.update(row_references(child))
    return found


def assemble(data: dict, task: str) -> tuple[list[dict],dict]:
    evidence=deepcopy(data['evidence'])
    derived=derived_evidence(evidence,data['actual_window'],task,(data.get('watermarks') or {}).get('rows',[]))
    if derived and not any(e['evidence_id']==derived['evidence_id'] for e in evidence): evidence.append(derived)
    watermarks=data.get('watermarks') or {}
    watermark_id=task+':source-watermarks'
    if evidence and watermarks.get('status')=='ok' and not any(e['evidence_id']==watermark_id for e in evidence):
        rows=[{'source':r[0],'complete_before':datetime.fromisoformat(r[1]).astimezone(timezone(timedelta(hours=8))).date().isoformat()}
              for r in watermarks['rows']]
        evidence.append({'evidence_id':watermark_id,'tool':'preflight_watermarks','parameters':{'sql':'SELECT source, complete_before FROM source_watermarks'},
            'source':'SELECT source, complete_before FROM source_watermarks; date normalized to Asia/Shanghai',
            'snapshot_id':data['snapshot_hash'],'columns':{'source':'string','complete_before':'string'},'rows':rows,
            'contexts':{Reference(watermark_id,i,'complete_before').pointer:{'metric':'source_complete_before',
                'window':data['actual_window'],'group':{'source':r['source']},'comparison':'current'} for i,r in enumerate(rows)},
            'window':data['actual_window'],'group':{},'sample':{'returned_rows':len(rows)},'truncated':False,'limitations':[]})
    sources={e['evidence_id']:e for e in evidence}
    facts=deepcopy((data.get('report') or {}).get('facts',[]))
    if derived:
        facts.extend({'evidence_id':derived['evidence_id'],'row':i,'column':'value','value':row['value']}
                     for i,row in enumerate(derived['rows']))
    assertions=[]; row_ids: dict[tuple[str,int],list[str]]=defaultdict(list)
    for i,fact in enumerate(facts):
        ref={k:fact[k] for k in ('evidence_id','row','column')}
        source=sources[ref['evidence_id']]
        context=source['contexts'][Reference(**ref).pointer]
        assertion={'assertion_id':str(i),'reference':ref,'context':context,'value':fact['value'],'scope':'cell'}
        assertions.append(assertion); row_ids[(ref['evidence_id'],ref['row'])].append(str(i))
    report=data.get('report') or {}; inferences: list[dict]=[]
    diagnoses=([report['diagnosis']] if report.get('diagnosis') else [])+report.get('additional_diagnoses',[])
    for diagnosis in diagnoses:
        for candidate in diagnosis.get('candidates',[]):
            supports=row_references(candidate.get('supporting_facts',[]))
            opposition=row_references(candidate.get('counterevidence',[]))
            inferences.append({'inference_id':'candidate:'+str(len(inferences)),
                'text':candidate['explanation']+' 这是描述性候选，未证明因果关系。',
                'supporting_assertion_ids':sorted({a for row in supports for a in row_ids.get(row,[])}),
                'opposing_assertion_ids':sorted({a for row in opposition for a in row_ids.get(row,[])}),
                'unexcluded_factors':diagnosis.get('unexcluded_factors',[])})
    if not inferences and assertions and (diagnoses or
            'requested_window_shortened_to_complete_sources' in report.get('limitations',[])):
        inferences.append({'inference_id':'assessment:0','text':report['summary'],
            'supporting_assertion_ids':[a['assertion_id'] for a in assertions],
            'opposing_assertion_ids':[],
            'unexcluded_factors':list(dict.fromkeys(report.get('limitations',[])+report.get('unresolved_questions',[])
                +[f for d in diagnoses for f in d.get('unexcluded_factors',[])]))})
    return evidence,{'assertions':assertions,'inferences':inferences,'charts':[]}


def assessment(report: dict) -> tuple[str,dict]:
    """Outcome labels follow actual bounded rules, independent of task category."""
    codes={'version-association-v1':'version_crash_association',
           'channel-growth-v1':'low_retention_acquisition_growth',
           'playback-collection-v1':'completion_collection_gap',
           'system-composition-v1':'composition_masks_subgroup_decline'}
    diagnoses=([report['diagnosis']] if report.get('diagnosis') else [])+report.get('additional_diagnoses',[])
    for diagnosis in diagnoses:
        candidates=diagnosis.get('candidates',[])
        if candidates:
            candidate=candidates[0]; group=candidate.get('group',{})
            localization={({'registration_os':'os','registration_version':'version','actual_os':'os','actual_version':'version'}.get(k,k)):v
                          for k,v in group.items()}
            if candidate.get('worsening_systems'): localization={'os':candidate['worsening_systems'][0]}
            return codes.get(diagnosis['rule_version'],diagnosis['rule_version']),localization
    if diagnoses and all(d.get('status')=='no_supported_candidate' and not d.get('missing_evidence') for d in diagnoses):
        return 'no_sufficient_anomaly_evidence',{}
    return ('query_result' if report.get('analysis_result')=='facts_available' else 'insufficient_evidence'),{}
