"""Program-owned ending semantics; evidence availability is not analytical success."""
from typing import Any


def conclude(report: dict[str, Any], outcome: str, mode: str) -> dict[str, Any]:
    diagnoses = ([report['diagnosis']] if 'diagnosis' in report else []) + report.get('additional_diagnoses', [])
    if outcome in ('refused', 'budget_exhausted', 'unsupported', 'insufficient_evidence'):
        status = outcome
        for diagnosis in diagnoses:
            diagnosis['candidates'] = []
            diagnosis['status'] = 'insufficient_evidence'
            diagnosis['missing_evidence'] = sorted(set(diagnosis.get('missing_evidence', []) + ['task_ended:' + outcome]))
    elif mode == 'query':
        status = 'facts_available'
    elif not diagnoses or any(d.get('missing_evidence') for d in diagnoses):
        status = 'insufficient_evidence'
    elif any(d.get('candidates') for d in diagnoses):
        status = 'supported_descriptive_candidate'
    elif all(d.get('rule_version') == 'playback-collection-v1' and d['status'] == 'no_supported_candidate' for d in diagnoses):
        # Complete aligned dual-chain census permits a scoped negative finding.
        status = 'no_supported_anomaly'
    else:
        # Binary precision/independence is not established by grouped SQL counts.
        status = 'insufficient_evidence'
    summary = {
        'refused': '请求超出允许的能力边界，已拒绝；已有事实不代表请求已完成。',
        'budget_exhausted': '预算或未知用量保护已停止执行，仅提供现有事实和未决项。',
        'unsupported': '该问题不在当前支持的指标范围内。',
        'insufficient_evidence': '已有观测不足以完成判断；没有候选不等于没有异常。',
        'supported_descriptive_candidate': '证据支持当前快照的描述性候选，尚未证明总体推断或因果关系。',
        'no_supported_anomaly': '在已核验的双链路播放实例和当前窗口内，未发现达到开发规则的采集缺失证据；不排除其他异常。',
        'facts_available': '查询事实可复核，未据此推断异常或原因。',
    }[status]
    if status in ('insufficient_evidence', 'budget_exhausted', 'refused'):
        if not report['unresolved_questions']:
            report['unresolved_questions'].append('仍需核验问题相关的完整性、可比较证据及统计适用性。')
        for diagnosis in diagnoses:
            report['unresolved_questions'].extend('Missing evidence: ' + item for item in diagnosis.get('missing_evidence', []))
    report['unresolved_questions'] = list(dict.fromkeys(report['unresolved_questions']))
    return {'analysis_result': status, 'summary': summary,
            'report_scope': 'partial' if status in ('refused', 'budget_exhausted', 'insufficient_evidence') else 'bounded',
            'anomaly_absence_established': False}
