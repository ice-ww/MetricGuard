"""Descriptive playback collection assessment with explicit source/quality gates."""
from datetime import datetime
from typing import Any
from metricguard.metric_profiles import is_business_profile


def playback_diagnosis(evidence: list[dict[str, Any]], watermarks: list, window: list[str]) -> dict[str, Any] | None:
    profiles = {e['parameters'].get('kind'): e for e in evidence if is_business_profile(e['parameters']) and e['parameters'].get('kind') in ('playback_events', 'playback_progress')}
    if not profiles:
        return None
    report: dict[str, Any] = {'rule_version': 'playback-collection-v1', 'status': 'insufficient_evidence',
        'candidates': [], 'playback_metrics': [], 'missing_evidence': [],
        'unexcluded_factors': ['无法仅凭观测完播率下降认定用户行为恶化；两链路同步偏差及独立遥测本身错误未排除。'],
        'statistical_limitations': ['播放实例不是独立用户样本；仅发布描述性比例，不做用户级独立二项检验或置信区间。', '候选解释需要人工复核，不证明故障因果。']}
    cutoffs = {name: datetime.fromisoformat(value) for name, value in watermarks}
    end = datetime.fromisoformat(window[1] + 'T00:00:00+08:00')
    for name in ('sessions', 'content_events', 'playback_telemetry'):
        if name not in cutoffs or cutoffs[name] < end:
            report['missing_evidence'].append('incomplete_source:' + name)
    for kind in ('playback_events', 'playback_progress'):
        if kind not in profiles or profiles[kind]['truncated']:
            report['missing_evidence'].append('complete_profile:' + kind)
    if any(x.startswith('complete_profile:') for x in report['missing_evidence']):
        return report
    events, progress = profiles['playback_events'], profiles['playback_progress']
    def key(row: dict) -> tuple:
        return row['period'], row['actual_os'], row['actual_version']
    def ref(e: dict, i: int) -> dict:
        return {'evidence_id': e['evidence_id'], 'row': i, 'values': e['rows'][i]}
    progress_rows = {key(r): (i, r) for i, r in enumerate(progress['rows'])}
    for i, row in enumerate(events['rows']):
        match = progress_rows.get(key(row))
        if match is None:
            report['missing_evidence'].append('missing_progress_group'); continue
        j, p = match
        if row['invalid_alignment'] or p.get('invalid_alignment', 0) or p['invalid_telemetry'] or p['unmatched']:
            report['missing_evidence'].append('unaligned_or_missing_or_invalid_progress')
        if p['last_observed'] is not None and ('playback_telemetry' not in cutoffs or 'content_events' not in cutoffs or datetime.fromisoformat(p['last_observed']) >= min(cutoffs['playback_telemetry'], cutoffs['content_events'])):
            report['missing_evidence'].append('progress_beyond_complete_source')
        if row['last_event'] is not None and ('content_events' not in cutoffs or datetime.fromisoformat(row['last_event']) >= cutoffs['content_events']):
            report['missing_evidence'].append('events_beyond_complete_source')
        starts = row['starts']
        report['playback_metrics'].append({**{k: row[k] for k in ('period', 'actual_os', 'actual_version')},
            'starts': starts, 'observed_completed': row['observed_completed'],
            'independent_complete': p['independent_complete'], 'effective': p['effective'],
            'missing_completion': p['independent_complete_without_event'] if not report['missing_evidence'] else None, 'unmatched': p['unmatched'],
            'observed_completion_rate': row['observed_completed'] / starts if starts else None,
            'independent_completion_rate': p['independent_complete'] / starts if starts else None,
            'effective_playback_rate': p['effective'] / starts if starts else None,
            'source_facts': [ref(events, i), ref(progress, j)]})
    if any(not any(m['period']==period and m['starts'] for m in report['playback_metrics']) for period in ('previous', 'current')):
        report['missing_evidence'].append('nonempty_current_and_previous_plays')
    if set(progress_rows) != {key(r) for r in events['rows']}:
        report['missing_evidence'].append('orphan_progress_group')
    if report['missing_evidence']:
        for metric in report['playback_metrics']:
            metric['missing_completion'] = None
        report['missing_evidence'] = sorted(set(report['missing_evidence']))
        report['unexcluded_factors'].append('证据不足，无法区分真实行为变化与完成事件缺失。')
        return report
    for metric in report['playback_metrics']:
        if metric['period'] != 'current' or not metric['missing_completion']:
            continue
        report['candidates'].append({'group': {k: metric[k] for k in ('actual_os', 'actual_version')},
            'window': window, 'causality': 'not_established',
            'explanation': '两条采集链路齐备且实例可对齐，独立观看进度达到完整时长但缺完成事件，支持完成事件采集缺失候选。基期及其他系统/版本的开始数、观测完成数与独立完成数作为对照，限定本候选只覆盖有实例缺失证据的分群；其他分群即使没有同类缺失，也不能排除两条链路共同偏差，更不能据此断言全平台用户行为恶化。',
            'supporting_facts': metric['source_facts'],
            'counterevidence': [f for m in report['playback_metrics'] if m is not metric for f in m['source_facts']]})
    report['status'] = 'association_candidate' if report['candidates'] else 'no_supported_candidate'
    return report
