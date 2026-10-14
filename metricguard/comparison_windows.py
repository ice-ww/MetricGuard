"""User-owned comparison scope and explicit baseline confirmation."""
from datetime import date
import re
from typing import Any
from .time_windows import parse_time, display


def split_question(text: str) -> tuple[str, str | None]:
    match = re.search(r'(?:比较基期|基期)(?:为|是|[:：])?\s*|对比\s*(?=\d{4}|昨天|前天|上周|本周|最近)', text)
    return (text[:match.start()], text[match.end():]) if match else (text, None)


def assessment_requested(text: str) -> bool:
    intent = text.replace('受影响人数', '').replace('受影响比例', '')
    return any(word in intent for word in (
        '异常', '诊断', '变化', '原因', '解释', '增长', '掩盖', '恶化', '资料是否充分', '完整请求窗口',
        '分析', '为什么', '为何', '下降', '上升', '降低', '提高', '波动', '影响', '有关', '关联', '检验', '对比', '比较'))


def resolve_comparison(data: dict[str, Any]) -> dict[str, Any] | None:
    window = data.get('requested_window') or data.get('actual_window')
    existing = data.get('comparison_window')
    if not window or existing and data.get('comparison_resolution') != 'explicit_parameter':
        return None
    _, text = split_question(data['question'])
    if text:
        baseline, _ = parse_time(text, data.get('time_anchor'))
        if baseline:
            if existing and list(existing) != baseline:
                return {'reason': 'comparison_window_conflict',
                        'prompt': f'分析日期：{display(window)}。问题中的基期与参数基期不一致，请选择比较范围。',
                        'options': [display(baseline), display(existing)]}
            data['comparison_window'] = baseline
            data['comparison_resolution'] = 'explicit_text'
            return None
    if existing and text is None:
        return None
    if text is None and not assessment_requested(data['effective_question']):
        return None
    start, end = map(date.fromisoformat, window)
    suggested = [(start - (end - start)).isoformat(), window[0]]
    return {'reason': 'comparison_window_required',
            'prompt': f'分析日期：{display(window)}。'+('基期表达尚不明确。' if text else '')+
                      f'建议比较基期：{display(suggested)}。请确认，或输入其他明确基期。',
            'options': [display(suggested)]}


def apply_comparison_answer(data: dict[str, Any], answer: str) -> None:
    if answer in ('确认', '是', '同意') and len(data['pending_question']['options']) == 1:
        answer = data['pending_question']['options'][0]
    baseline, _ = parse_time(answer, data.get('time_anchor'))
    if baseline:
        data['comparison_window'] = baseline
        data['comparison_resolution'] = 'user_confirmed'
