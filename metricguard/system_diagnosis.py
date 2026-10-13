"""Base-composition standardization of mature cohorts, descriptive only."""
from typing import Any
from metricguard.metric_profiles import is_business_profile


def system_diagnosis(evidence: list[dict[str, Any]]) -> dict[str, Any] | None:
    profiles = [e for e in evidence if is_business_profile(e['parameters'])
                and e['parameters']['kind'] == 'system_retention']
    if not profiles:
        return None
    result: dict[str, Any] = {
        'rule_version': 'system-composition-v1', 'status': 'insufficient_evidence',
        'business_threshold_pp': 5.0, 'candidates': [], 'system_metrics': [],
        'actual_retention': {}, 'standardized_retention': None, 'within_effect_pp': None,
        'composition_effect_pp': None, 'total_change_pp': None, 'difference_interval_pp': None,
        'missing_evidence': [], 'source_facts': [],
        'derivation': 'S=sum(base_user_share*current_system_retention); within=S-base_actual; composition=current_actual-S',
        'statistical_limitations': ['全窗口成熟注册用户计数加权，不平均每日比例。',
            '标准化为派生比较量，不是二项样本，不发布二项区间。',
            '5 个百分点为开发描述性业务阈值；总体差值未达阈值仅表示观测近似稳定，不证明统计等效。'],
        'unexcluded_factors': ['系统内渠道和版本构成、采集质量及同期产品变化仍未排除；不证明因果，也不泛称辛普森悖论。']}
    source = profiles[-1]
    if source['truncated']:
        result['missing_evidence'] = ['complete_system_profile']
        return result
    rows = source['rows']
    refs = [{'evidence_id': source['evidence_id'], 'row': i, 'values': row} for i, row in enumerate(rows)]
    result['source_facts'] = refs
    grouped = {p: {r['registration_os']: r for r in rows if r['period'] == p} for p in ('previous', 'current')}
    totals = {p: sum(r['users'] for r in group.values()) for p, group in grouped.items()}
    for period, total in totals.items():
        result['actual_retention'][period] = sum(r['retained'] for r in grouped[period].values()) / total if total else None
    if not all(totals.values()):
        result['missing_evidence'].append('nonempty_current_and_previous_cohorts')
    systems = set(grouped['previous']) | set(grouped['current'])
    for system in sorted(systems, key=lambda s: s or ''):
        counts = {p: grouped[p].get(system) for p in grouped}
        shares = {p: (r['users'] if r else 0) / totals[p] if totals[p] else None for p, r in counts.items()}
        rates = {p: r['retention_rate'] if r else None for p, r in counts.items()}
        current_rate, previous_rate = rates['current'], rates['previous']
        delta = (current_rate - previous_rate) * 100 if current_rate is not None and previous_rate is not None else None
        result['system_metrics'].append({'registration_os': system, 'user_share': shares,
            'retention_rate': rates, 'retention_change_pp': delta,
            'source_facts': [ref for ref in refs if ref['values']['registration_os'] == system]})
        if not system:
            result['missing_evidence'].append('known_registration_system')
        if any(r is None for r in counts.values()):
            result['missing_evidence'].append('comparable_system:' + str(system))
    if result['missing_evidence']:
        return result
    standard = sum(m['user_share']['previous'] * m['retention_rate']['current'] for m in result['system_metrics'])
    previous, current = (result['actual_retention'][p] for p in ('previous', 'current'))
    result.update(standardized_retention=standard, within_effect_pp=(standard-previous)*100,
                  composition_effect_pp=(current-standard)*100, total_change_pp=(current-previous)*100)
    worsening = [m for m in result['system_metrics'] if m['retention_change_pp'] <= -5]
    masked = worsening and result['within_effect_pp'] <= -5 and result['composition_effect_pp'] > 0 and abs(result['total_change_pp']) < 5
    result['status'] = 'association_candidate' if masked else 'no_supported_candidate'
    if masked:
        result['candidates'] = [{'explanation': '总体观测留存近似稳定，基期结构标准化显示恶化；系统新增占比变化抵消部分分群恶化。',
            'causality': 'not_established', 'worsening_systems': [m['registration_os'] for m in worsening],
            'supporting_facts': refs, 'counterevidence': [ref for ref in refs if ref['values']['registration_os'] not in {m['registration_os'] for m in worsening}]}]
    return result
