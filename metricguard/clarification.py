"""Human-readable clarification content shared by every task client."""
from typing import Any


def clarification_prompt(reason: str) -> str:
    return {
        'retention_population_required': '请明确留存人群，例如新增注册用户。',
        'retention_horizon_required': '请明确留存周期，例如自然日次日。',
        'candidate_ambiguity': '请明确要查询的指标名称。',
        'metric_required': '你想查看哪个指标？',
    }.get(reason, '请补充明确的指标定义或时间窗口。')


def presentation(data: dict[str, Any], reason: str) -> dict[str, Any]:
    window = data.get('requested_window')
    known = f'已选日期：{window[0]} 至 {window[1]}（结束日不包含）。' if window else '尚未指定日期。'
    if data.get('answers'):
        known += ' 已提供：' + '；'.join(a['answer'] for a in data['answers'])
    options = {
        'metric_required': ['新增用户自然日次日留存', '观测完播率', '新增用户首日崩溃受影响比例'],
        'candidate_ambiguity': ['新增用户自然日次日留存', '观测完播率', '新增用户首日崩溃受影响比例'],
        'retention_population_required': ['新增用户'],
        'retention_horizon_required': ['自然日次日'],
    }.get(reason, [])
    return {'known_information': known, 'prompt': clarification_prompt(reason), 'options': options}
