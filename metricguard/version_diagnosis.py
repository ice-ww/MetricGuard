"""Bounded descriptive version/crash interpretation from trusted profile evidence.

This is an explicit candidate rule, not a causal or general semantic evaluator.
"""
from dataclasses import asdict
from typing import Any

from experiments.t04.statistics import BinarySample, FrozenRule, compare
from metricguard.metric_profiles import is_business_profile


def version_diagnosis(evidence: list[dict[str, Any]]) -> dict[str, Any] | None:
    profiles = {e['parameters']['kind']: e for e in evidence if is_business_profile(e['parameters']) and not e['truncated']
                and e['parameters']['kind'] in ('cohort_health', 'crash_versions', 'releases')}
    if not profiles:
        return None
    report: dict[str, Any] = {
        'status': 'insufficient_evidence', 'candidates': [],
        'rule_version': 'version-association-v1', 'business_threshold_pp': FrozenRule().threshold_pp,
        'unexcluded_factors': ['渠道与用户构成、同期产品变化、设备差异等混杂因素未排除。', '发布时间相近和分群差异不能识别崩溃对留存的因果效应。'],
        'statistical_limitations': ['用户级去重并限定成熟 cohort；未证明独立同质 Bernoulli 抽样，故只作描述比较，不发布置信区间或显著性结论。',
                                   '使用 t04-v1 的 5 个百分点业务差值阈值筛选探索性候选，不代表统计显著或已证明因果。',
                                   '自适应下钻存在选择偏差；候选解释仍需人工语义复核。'],
        'missing_evidence': sorted({'cohort_health', 'crash_versions', 'releases'} - profiles.keys())}
    if report['missing_evidence']:
        return report
    health, crashes, releases = (profiles[k] for k in ('cohort_health', 'crash_versions', 'releases'))
    current = [(i, r) for i, r in enumerate(health['rows']) if r['period'] == 'current']
    previous = [(i, r) for i, r in enumerate(health['rows']) if r['period'] == 'previous']
    if not current or not previous:
        report['missing_evidence'] = ['nonempty_current_and_previous_cohorts']
        return report

    def refs(e: dict[str, Any], index: int) -> dict[str, Any]:
        return {'evidence_id': e['evidence_id'], 'row': index, 'values': e['rows'][index]}

    def comparison(row: dict[str, Any], peers: list[tuple[int, dict[str, Any]]], metric: str) -> dict[str, Any]:
        value = asdict(compare(BinarySample(row[metric], row['users']),
                               BinarySample(sum(r[metric] for _, r in peers), sum(r['users'] for _, r in peers)), independent=False))
        value['metric'] = metric
        value['reference_facts'] = [refs(health, i) for i, _ in peers]
        return value

    threshold = FrozenRule().threshold_pp
    for index, row in current:
        os, version = row['registration_os'], row['registration_version']
        past = [(i, r) for i, r in previous if r['registration_os'] == os]
        old = [(i, r) for i, r in current if r['registration_os'] == os and r['registration_version'] != version]
        other = [(i, r) for i, r in current if r['registration_os'] != os]
        release = [(i, r) for i, r in enumerate(releases['rows']) if r['os'] == os and r['version'] == version
                   and row['window_start'] <= r['release_date'] < row['window_end']]
        actual = [(i, r) for i, r in enumerate(crashes['rows']) if r['period'] == 'current'
                  and r['registration_os'] == os and r['registration_version'] == version]
        available_controls = [peers for peers in (past, old) if peers]
        if not available_controls:
            report['missing_evidence'].extend(['previous_same_system', 'current_other_version'])
            continue
        relevant = any(comparison(row, peers, 'retained')['difference_pp'] <= -threshold
                       and comparison(row, peers, 'crashed_users')['difference_pp'] >= threshold for peers in available_controls)
        if not relevant:
            continue
        # Without an observed pre-period, old-version and other-system controls the candidate remains unassessed.
        missing = [name for name, present in [('previous_same_system', bool(past)), ('current_other_version', bool(old)),
                   ('current_other_system', bool(other)), ('unique_matching_release', len(release) == 1),
                   ('actual_crash_attribution', bool(actual))] if not present]
        if missing:
            report['missing_evidence'].extend(missing)
            continue
        if any(r['actual_os'] != os or r['actual_version'] != version for _, r in actual):
            report['missing_evidence'].append('actual_crash_registration_mismatch')
            continue
        if sum(r['crashed_users'] for _, r in actual) != row['crashed_users']:
            report['missing_evidence'].append('actual_crash_user_count_mismatch')
            continue
        comparisons = [comparison(row, past, 'retained'), comparison(row, old, 'retained'),
                       comparison(row, old, 'crashed_users')]
        if not (comparisons[0]['difference_pp'] <= -threshold and comparisons[1]['difference_pp'] <= -threshold
                and comparisons[2]['difference_pp'] >= threshold):
            continue
        system = [r for _, r in current if r['registration_os'] == os]
        now_rate = sum(r['retained'] for r in system) / sum(r['users'] for r in system)
        past_rate = sum(r['retained'] for _, r in past) / sum(r['users'] for _, r in past)
        if (now_rate - past_rate) * 100 > -threshold:
            continue
        controls = [{'group': {'registration_os': r['registration_os'], 'registration_version': r['registration_version']},
                     'fact': refs(health, i)} for i, r in old + other]
        system_counts = {'users': sum(r['users'] for r in system), 'retained': sum(r['retained'] for r in system)}
        system_comparison = comparison(system_counts, past, 'retained')
        system_comparison['current_facts'] = [refs(health, i) for i, r in current if r['registration_os'] == os]
        report['candidates'].append({
            'group': {'registration_os': os, 'registration_version': version}, 'window': [row['window_start'], row['window_end']],
            'explanation': '该系统新注册版本的留存更低、首日崩溃受影响比例更高，且发布时间与当前窗口重合；支持版本崩溃与留存下降相关的候选解释。',
            'causality': 'not_established', 'release_date': release[0][1]['release_date'],
            'supporting_facts': [refs(health, index)] + [refs(health, i) for i, _ in past] + [refs(crashes, i) for i, _ in actual] + [refs(releases, release[0][0])],
            'counterevidence': [{'interpretation': '对照的实际表现必须纳入解释；不能忽略其是否也发生同向变化。', 'fact': refs(health, i),
                                'previous_facts': [refs(health, j) for j, p in previous if p['registration_os'] == r['registration_os'] and p['registration_version'] == r['registration_version']]}
                               for i, r in old + other],
            'controls': controls, 'comparisons': comparisons, 'system_comparison': system_comparison,
            'same_version_previous': [refs(health, i) for i, r in past if r['registration_version'] == version],
            'same_version_previous_limitation': '新版本前期可能无样本；未将缺失留存率当作零。'})
    report['missing_evidence'] = sorted(set(report['missing_evidence']))
    report['status'] = ('association_candidate' if report['candidates'] else
                        'insufficient_evidence' if report['missing_evidence'] else 'no_supported_candidate')
    return report
