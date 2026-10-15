"""Human report text uses published, cell-validated assertions only."""
import html
import json
from datetime import date
from collections import OrderedDict
from typing import Any
from .time_windows import display


def safe(value: Any) -> str:
    return html.escape(str(value), quote=False).replace('\n', ' ').replace('\r', ' ').replace('|', '&#124;').replace('`', '&#96;')


# Units follow reviewed profile semantics, never inferred from a raw SQL alias.
METRICS = {
    'users': ('新增用户数', ' 人'), 'retained': ('次日留存人数', ' 人'),
    'crashed_users': ('首日崩溃人数', ' 人'), 'actual_first_day_crashed_users': ('实际系统/版本首日崩溃人数', ' 人'),
    'cross_attributed_crashed_users': ('注册与实际归属交叉的首日崩溃人数', ' 人'),
    'retention_rate': ('次日留存率', '%'), 'crash_affected_rate': ('首日崩溃受影响比例', '%'),
    'new_user_share': ('新增用户占比', '%'), 'baseline_standardized_retention_rate': ('基期结构标准化留存率', '%'),
    'observed_completion_rate': ('观测完播率', '%'), 'independent_completion_rate': ('独立进度完整播放比例', '%'),
    'starts': ('开始播放实例数', ' 次'), 'completions': ('观测完成播放实例数', ' 次'),
    'telemetry_complete': ('独立进度完整播放实例数', ' 次'),
    'missing_complete': ('独立进度完整但缺完成事件的实例数', ' 次'),
    'independent_complete_without_event': ('独立进度完整但缺完成事件的实例数', ' 次'),
    'spend_cents': ('渠道支出', ' 分'), 'cost_per_new_cents': ('每新增用户成本', ' 分/人'),
    'cost_per_retained_cents': ('每次日留存用户成本', ' 分/人'),
}
GROUPS = {'os': '系统', 'version': '版本', 'channel': '渠道', 'population': '人群',
          'registration_os': '注册系统', 'registration_version': '注册版本', 'actual_os': '实际系统', 'actual_version': '实际版本'}


def context_text(context: dict) -> str:
    group = '，'.join(GROUPS.get(k, safe(k)) + ' ' + safe('播放实例' if v == 'play_instances' else v)
                     for k,v in context['group'].items()) or '总体'
    period = {'previous': '基期', 'current': '本期'}.get(context['comparison'], safe(context['comparison']))
    return f"{period} {display(context['window'])}，{group}"


def value_text(assertion: dict) -> str:
    metric = assertion['context']['metric']; value = assertion['value']
    label, unit = METRICS.get(metric, ('查询值（' + metric + '；业务口径待独立核验）', ''))
    if unit == '%':
        number = format(value * 100, '.3f')
    else:
        number = str(value) if type(value) is int else format(value, '.3f').rstrip('0').rstrip('.') if type(value) is float else safe(value)
    return f'{safe(label)}：{number}{unit}'


def fact_text(assertion: dict) -> str:
    return context_text(assertion['context']) + '，' + value_text(assertion)


def fact_lines(assertions: list[dict], limit: int = 12) -> list[str]:
    groups: dict[str, list[dict]] = OrderedDict()
    for assertion in assertions:
        if assertion['context']['metric'] not in METRICS and not assertion['context']['metric'].startswith('query_result:'):
            continue  # Quality diagnostics and technical columns remain in the complete fact table.
        context = assertion['context']
        key = json.dumps({k:context[k] for k in ('window','group','comparison')}, sort_keys=True)
        groups.setdefault(key, []).append(assertion)
    lines = []
    for items in list(groups.values())[:limit]:
        pieces = [value_text(a) + f" [A{a['assertion_id']}](#fact-{a['assertion_id']})" for a in items]
        lines.append('- ' + context_text(items[0]['context']) + '：' + '；'.join(pieces))
    if len(groups) > limit:
        lines.append('其余分组见完整事实表；此处未展示的分组不代表不存在。')
    return lines


def notice(data: dict, text: str) -> str:
    if text.startswith('No new evidence proposed; question remains unresolved: '):
        return '未获得新的证据，原问题尚未充分解决；原始提问见任务记录。'
    if text.startswith('Not fully resolved due to '):
        return '任务因运行限制未能充分解决原问题；具体限制及原始提问见任务记录。'
    if 'equal_duration_windows_required_for_count_growth' in text:
        previous = data.get('comparison_window'); current = data.get('actual_window')
        if previous and current:
            days = lambda window: (date.fromisoformat(window[1]) - date.fromisoformat(window[0])).days
            return (f'基期 {days(previous)} 天、本期 {days(current)} 天，不能直接比较新增人数的增长。'
                    '以上仅提供各自窗口的事实；如需判断增长，请重新明确等长且齐备的比较日期。')
    return safe(text)


def render(data: dict, publication: dict) -> tuple[str, str]:
    report = data.get('report') or {}
    lines = ['# 分析报告', '']
    if publication.get('scope_statement'):
        lines += [publication['scope_statement'], '']
    lines += [report.get('summary', '暂无报告。'), '']
    assertions = publication['assertions']
    by_id = {a['assertion_id']: a for a in assertions}
    if publication['inferences']:
        for inference in publication['inferences']:
            lines += ['## 候选解释与比较', '', safe(inference['text']), '', '支持依据：', '']
            lines += fact_lines([by_id[i] for i in inference['supporting_assertion_ids']])
            lines += ['', '反对证据与对照：', '']
            opposing = [by_id[i] for i in inference['opposing_assertion_ids']]
            lines += fact_lines(opposing) if opposing else ['尚无已引用的反对证据；这不证明唯一原因。']
            lines += ['', '未排除因素：' + ('；'.join(map(safe, inference['unexcluded_factors'])) or '其他解释仍待核查。'),
                      '上述比较未证明因果关系。', '']
        extra = [a for a in assertions if a['context']['metric'] in
                 ('new_user_share', 'baseline_standardized_retention_rate', 'observed_completion_rate', 'independent_completion_rate', 'missing_complete')]
        if extra:
            lines += ['## 补充比较指标', ''] + fact_lines(extra)
    else:
        lines += ['## 关键事实', ''] + fact_lines(assertions)
    if not assertions:
        lines.append('暂无通过引用校验的事实；不能据此认定正常或异常。')
    # Stop prose is retained for audit, but can embed unvalidated factual claims.
    model_questions = {question for step in data.get('diagnostic_history', [])
                       if step.get('action', {}).get('action') == 'stop'
                       for question in step['action'].get('unresolved_questions', [])}
    lines += ['', *(notice(data, line) for line in report.get('unresolved_questions', [])
                    if line not in model_questions)]
    if model_questions:
        lines.append('模型另提出未核验的待查问题，保留在任务记录中，未作为结论依据。')
    body = '\n'.join(lines).rstrip()
    full = [body, '', '## 完整事实表', '', '| 引用 | 事实 | 原始位置（行号从0起） |', '| --- | --- | --- |']
    for assertion in assertions:
        identity = assertion['assertion_id']; ref = assertion['reference']
        cell = f"{ref['evidence_id']}/rows/{ref['row']}/{ref['column']}"
        full.append(f'| <a id="fact-{identity}"></a>A{identity} | {fact_text(assertion)} | {safe(cell)} |')
    full += ['', '原始证据与 SQL：[evidence.json](evidence.json)。逐项断言：[publication.json](publication.json)。',
             '展示值可取整；原值、上下文、派生来源和引用校验依据均保留在 JSON 中。']
    return body, '\n'.join(full) + '\n'
