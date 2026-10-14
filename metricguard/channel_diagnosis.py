"""Descriptive channel contribution; no fraud or causal inference."""
from typing import Any
from datetime import date
from metricguard.metric_profiles import is_business_profile


def channel_diagnosis(evidence: list[dict[str, Any]]) -> dict[str, Any] | None:
    profiles = [e for e in evidence if is_business_profile(e['parameters']) and e['parameters']['kind'] == 'channel_health']
    if not profiles:
        return None
    report: dict[str, Any] = {
        'rule_version': 'channel-growth-v1', 'status': 'insufficient_evidence', 'candidates': [], 'channel_metrics': [],
        'business_threshold_pp': 5.0, 'missing_evidence': [],
        'unexcluded_factors': ['低留存不证明用户造假；渠道归属、用户构成和同期产品变化未排除。', '每新增成本是否上升必须由实际支出与人数判断。'],
        'statistical_limitations': ['描述性比较采用 5 个百分点业务差值阈值，不是显著性检验。', '未证明独立同质抽样，不发布置信区间；自适应渠道筛选存在选择偏差，解释仍需人工复核。', '净新增为零时增长贡献不可计算；净增长为负时只报告有符号贡献，不称为拉动增长。']}
    evidence_row = profiles[-1]
    if evidence_row['truncated']:
        report['missing_evidence'] = ['complete_channel_profile']
        return report
    rows = evidence_row['rows']
    durations = {r['period']: (date.fromisoformat(r['window_end']) - date.fromisoformat(r['window_start'])).days for r in rows}
    if len(set(durations.values())) > 1:
        report['missing_evidence'] = ['equal_duration_windows_required_for_count_growth']
        report['unexcluded_factors'].append('两期天数不同；保留各期事实，不用总人数差判断渠道增长或增长贡献。')
        return report
    report['missing_evidence'] += ['channel_spend:' + r['channel'] for r in rows if r['users'] and r['spend_cents'] is None]
    totals = {period: sum(r['users'] for r in rows if r['period'] == period) for period in ('previous', 'current')}
    net = totals['current'] - totals['previous']

    def reference(index: int) -> dict[str, Any]:
        return {'evidence_id': evidence_row['evidence_id'], 'row': index, 'values': rows[index]}

    for channel in sorted({r['channel'] for r in rows}):
        indices = {r['period']: i for i, r in enumerate(rows) if r['channel'] == channel}
        counts = {p: rows[i]['users'] for p, i in indices.items()}
        delta = counts.get('current', 0) - counts.get('previous', 0)
        metric = {'channel': channel, 'new_users_delta': delta, 'total_new_users_delta': net,
                  'growth_contribution': delta / net if net else None,
                  'user_share': {p: counts.get(p, 0) / total if total else None for p, total in totals.items()},
                  'source_facts': [reference(i) for i in indices.values()],
                  'total_source_facts': [reference(i) for i in range(len(rows))],
                  'derivation': 'program_from_complete_channel_profile'}
        report['channel_metrics'].append(metric)
        if 'current' not in indices:
            continue
        index = indices['current']; row = rows[index]
        peers = [(i, r) for i, r in enumerate(rows) if r['period'] == 'current' and r['channel'] != channel and r['users']]
        peer_users = sum(r['users'] for _, r in peers)
        if row['users'] and not peer_users:
            report['missing_evidence'].append('comparison_channels')
        if not row['users'] or not peer_users or net <= 0 or delta <= 0:
            continue
        peer_rate = sum(r['retained'] for _, r in peers) / peer_users
        difference = (row['retention_rate'] - peer_rate) * 100
        if difference > -5.0:
            continue
        previous = rows[indices['previous']] if 'previous' in indices else None
        def cost_change(key: str) -> float | None:
            return row[key] - previous[key] if previous is not None and row[key] is not None and previous[key] is not None else None
        report['candidates'].append({
            'group': {'channel': channel}, 'window': [row['window_start'], row['window_end']],
            'explanation': '该渠道新增人数增加且当前次日留存低于其他渠道，支持低留存渠道贡献新增增长的描述性候选。',
            'causality': 'not_established', 'supporting_facts': metric['source_facts'],
            'counterevidence': [reference(i) for i, _ in peers], 'growth': metric,
            'retention_difference_pp': difference, 'difference_interval_pp': None,
            'cost_per_new_change_cents': cost_change('cost_per_new_cents'),
            'cost_per_retained_change_cents': cost_change('cost_per_retained_cents')})
    if not totals['previous'] or not totals['current']:
        report['missing_evidence'].append('nonempty_current_and_previous_cohorts')
        report['candidates'] = []
    report['missing_evidence'] = sorted(set(report['missing_evidence']))
    report['status'] = ('association_candidate' if report['candidates'] else
                        'insufficient_evidence' if report['missing_evidence'] else 'no_supported_candidate')
    return report
