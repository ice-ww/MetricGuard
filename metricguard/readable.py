"""Human report text uses published, cell-validated assertions only."""
import html
import json
import re
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
        lines.append('- ' + context_text(items[0]['context']))
        lines.extend('  ' + '；'.join(pieces[i:i+2]) for i in range(0, len(pieces), 2))
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
                    '播放次数、支出等期间总量也不能直接当作增长或下降依据。'
                    '以上仅提供各自窗口的事实；比率仍需核对人群构成和观测条件，不能因分母已归一化就认定可比。'
                    '如需判断增长，请重新明确等长且齐备的比较日期。')
    return safe(text)


def group_text(group: dict) -> str:
    return '，'.join(GROUPS.get(k, safe(k)) + ' ' + safe('播放实例' if v == 'play_instances' else v)
                     for k, v in group.items()) or '总体'


def focus_text(data: dict, publication: dict) -> str:
    report = data.get('report') or {}
    diagnoses = ([report['diagnosis']] if report.get('diagnosis') else []) + report.get('additional_diagnoses', [])
    subjects = []
    aliases = {'registration_os':'os', 'registration_version':'version', 'actual_os':'os', 'actual_version':'version'}
    definitions = [c for d in diagnoses for c in d.get('candidates', [])]
    candidates = [i for i in publication['inferences'] if i['inference_id'].startswith('candidate:')]
    by_id = {a['assertion_id']:a for a in publication['assertions']}
    for candidate, inference in zip(definitions, candidates):
        groups = [{aliases.get(k,k):v for k,v in candidate.get('group', {}).items()}]
        if candidate.get('worsening_systems'):
            groups = [{'os':system} for system in candidate['worsening_systems']]
        for group in groups:
            if group and any(all(by_id[i]['context']['group'].get(k)==v for k,v in group.items())
                             for i in inference['supporting_assertion_ids']):
                subjects.append(group_text(group))
    return '；'.join(dict.fromkeys(subjects))


def comparison_lines(data: dict, assertions: list[dict]) -> list[str]:
    previous = data.get('comparison_window'); current = data.get('actual_window')
    if not previous or not current:
        return []
    pairs: dict[str, dict[str, list[dict]]] = {}
    metrics = ('retention_rate','new_user_share','crash_affected_rate','observed_completion_rate',
               'independent_completion_rate','users','cost_per_new_cents','cost_per_retained_cents')
    for a in assertions:
        c = a['context']; period = c['comparison']
        expected = previous if period == 'previous' else current
        if c['metric'] in metrics and period in ('previous','current') and list(c['window']) == list(expected):
            key = json.dumps([c['metric'], c['group']], sort_keys=True)
            pairs.setdefault(key, {}).setdefault(period, []).append(a)
    lines = []
    for periods in pairs.values():
        if set(periods) != {'previous','current'}:
            continue
        if any(len({a['value'] for a in values}) != 1 for values in periods.values()):
            continue  # Conflicting facts cannot be resolved by presentation.
        before, after = periods['previous'][0], periods['current'][0]
        metric = before['context']['metric']
        label, unit = METRICS[metric]
        left = value_text(before).split('：', 1)[1]; right = value_text(after).split('：', 1)[1]
        refs = f"[A{before['assertion_id']}](#fact-{before['assertion_id']}) → [A{after['assertion_id']}](#fact-{after['assertion_id']})"
        delta = f"；差值 {(after['value']-before['value'])*100:+.3f} 个百分点" if unit == '%' else ''
        lines.append(f"- {group_text(before['context']['group'])}，{label}：{left} → {right}{delta}（{refs}）")
    return ['## 关键比较', '', '基期 → 本期（各自窗口观测值；差值不表示因果效应）：', ''] + lines + [''] if lines else []


def contrast_lines(publication: dict) -> list[str]:
    assertions = publication['assertions']
    by_id = {a['assertion_id']:a for a in assertions}
    lines = []; seen = set()
    def add(label: str, left: dict, right: dict) -> None:
        key = json.dumps([left['context'], right['context']], sort_keys=True)
        if key in seen:
            return
        seen.add(key)
        lines.append(f"- {label}：{group_text(left['context']['group'])}，{value_text(left)} "
                     f"[A{left['assertion_id']}](#fact-{left['assertion_id']})；"
                     f"{group_text(right['context']['group'])}，{value_text(right)} "
                     f"[A{right['assertion_id']}](#fact-{right['assertion_id']})")
    for inference in publication['inferences']:
        if not inference['inference_id'].startswith('candidate:'):
            continue
        for support_id in inference['supporting_assertion_ids']:
            left = by_id[support_id]; c = left['context']
            if c['comparison'] != 'current' or c['metric'] not in ('retention_rate','crash_affected_rate'):
                continue
            for opposite_id in inference['opposing_assertion_ids']:
                right = by_id[opposite_id]; d = right['context']
                if d['comparison']=='current' and c['window']==d['window'] and c['metric']==d['metric'] and c['group']!=d['group']:
                    add('同期对照', left, right)
    for left in assertions:
        c = left['context']
        if c['comparison']!='current':
            continue
        partner = {'observed_completion_rate':'independent_completion_rate',
                   'retention_rate':'baseline_standardized_retention_rate'}.get(c['metric'])
        if not partner or (c['metric']=='retention_rate' and c['group']):
            continue
        for right in assertions:
            d = right['context']
            if d['metric']==partner and d['window']==c['window'] and d['group']==c['group'] and d['comparison']==c['comparison']:
                add('同分群采集对照' if c['metric']=='observed_completion_rate' else '本期总体与结构标准化对照', left, right)
    return ['## 同期与口径对照', ''] + lines + [''] if lines else []


def render(data: dict, publication: dict) -> tuple[str, str]:
    report = data.get('report') or {}
    candidates = [i for i in publication['inferences'] if i['inference_id'].startswith('candidate:')]
    diagnoses = ([report['diagnosis']] if report.get('diagnosis') else []) + report.get('additional_diagnoses', [])
    no_candidate = bool(diagnoses) and all(d.get('status')=='no_supported_candidate' and not d.get('missing_evidence') for d in diagnoses)
    if candidates:
        subject = focus_text(data, publication)
        title = '候选解释与比较' + ('：' + subject if subject else '')
    elif data.get('analysis_result') == 'facts_available':
        title = '查询事实'
    elif no_candidate:
        title = '未形成支持充分的候选解释'
    elif data.get('analysis_result') == 'insufficient_evidence':
        title = '证据不足，暂无法判断'
    else:
        title = '未形成支持充分的候选解释'
    lines = ['# ' + title, '']
    seen: set[str] = set()
    def explain(text: str) -> None:
        for sentence in re.split(r'(?<=。)', text):
            sentence = sentence.strip()
            if sentence and sentence not in seen:
                seen.add(sentence)
                lines.extend([sentence, ''])
    coverage = data.get('coverage') or {}
    if coverage and not coverage.get('gaps') and data.get('actual_window') == data.get('requested_window'):
        explain('分析范围：' + display(data['actual_window']) + '。')
    elif publication.get('scope_statement'):
        explain(safe(publication['scope_statement']))
    if not candidates or data.get('analysis_result') == 'insufficient_evidence':
        explain(safe(report.get('summary', '暂无报告。')))
    if data.get('comparison_window'):
        explain('比较基期：' + display(data['comparison_window']) + '。')
    assertions = publication['assertions']
    by_id = {a['assertion_id']: a for a in assertions}
    previous = data.get('comparison_window'); current = data.get('actual_window')
    if previous and current:
        lengths = [(date.fromisoformat(w[1])-date.fromisoformat(w[0])).days for w in (previous,current)]
        if lengths[0] != lengths[1]:
            explain(notice(data, 'equal_duration_windows_required_for_count_growth'))
    for inference in candidates:
        explain(safe(inference['text'].replace('这是描述性候选，未证明因果关系。', '').strip()))
    comparisons = contrast_lines(publication) + comparison_lines(data, assertions)
    lines += comparisons
    shown = set(re.findall(r'\[A(\d+)\]', '\n'.join(comparisons)))
    def evidence_lines(items: list[dict]) -> list[str]:
        fresh = [a for a in items if a['assertion_id'] not in shown]
        repeated = [a for a in items if a['assertion_id'] in shown]
        output = fact_lines(fresh)
        groups: dict[str, list[str]] = {}
        for a in repeated:
            groups.setdefault(context_text(a['context']), []).append(a['assertion_id'])
        for group, ids in groups.items():
            output.append('- ' + group + '（数值见上）：' + ' '.join(f'[A{i}](#fact-{i})' for i in dict.fromkeys(ids)))
        shown.update(a['assertion_id'] for a in items)
        return output
    if candidates:
        for inference in candidates:
            explain(safe(inference['text'].replace('这是描述性候选，未证明因果关系。', '').strip()))
            lines += ['支持依据：', '']
            lines += evidence_lines([by_id[i] for i in inference['supporting_assertion_ids']])
            lines += ['', '反对证据与对照：', '']
            opposing = [by_id[i] for i in inference['opposing_assertion_ids']]
            lines += evidence_lines(opposing) if opposing else ['尚无已引用的反对证据；这不证明唯一原因。']
            lines += ['', '未排除因素：', '']
            for factor in inference['unexcluded_factors']:
                explain(notice(data, factor))
        extra = [a for a in assertions if a['context']['metric'] in
                 ('new_user_share', 'baseline_standardized_retention_rate', 'observed_completion_rate', 'independent_completion_rate', 'missing_complete')]
        if extra:
            remaining = [a for a in extra if a['assertion_id'] not in shown]
            if remaining:
                lines += ['## 补充比较指标', ''] + evidence_lines(remaining)
    else:
        remaining = [a for a in assertions if a['assertion_id'] not in shown]
        lines += ['## 已有事实' if title != '查询事实' else '## 关键事实', ''] + evidence_lines(remaining)
    if not assertions:
        explain('暂无通过引用校验的事实；不能据此认定正常或异常。')
    lines += ['', '## 限制与下一步', '']
    model_questions = {question for step in data.get('diagnostic_history', [])
                       if step.get('action', {}).get('action') == 'stop'
                       for question in step['action'].get('unresolved_questions', [])}
    for line in report.get('unresolved_questions', []):
        if line not in model_questions:
            explain(notice(data, line))
    for inference in publication['inferences']:
        if inference not in candidates:
            for line in inference['unexcluded_factors']:
                explain(notice(data, line))
    if model_questions:
        explain('模型另提出未核验的待查问题，保留在任务记录中，未作为结论依据。')
    if candidates:
        explain('上述比较未证明因果关系。')
    while lines and not lines[-1]:
        lines.pop()
    if lines and lines[-1] == '## 限制与下一步':
        lines.pop()
    body = '\n'.join(lines).rstrip()
    full = [body, '', '## 完整事实表', '', '| 引用 | 事实 | 原始位置（行号从0起） |', '| --- | --- | --- |']
    for assertion in assertions:
        identity = assertion['assertion_id']; ref = assertion['reference']
        cell = f"{ref['evidence_id']}/rows/{ref['row']}/{ref['column']}"
        full.append(f'| <a id="fact-{identity}"></a>A{identity} | {fact_text(assertion)} | {safe(cell)} |')
    full += ['', '原始证据与 SQL：[evidence.json](evidence.json)。逐项断言：[publication.json](publication.json)。',
             '展示值可取整；原值、上下文、派生来源和引用校验依据均保留在 JSON 中。']
    return body, '\n'.join(full) + '\n'


def terminal_text(body: str) -> str:
    """Keep the same facts and reference IDs without Markdown navigation syntax."""
    text = re.sub(r'\[A(\d+)\]\(#fact-\d+\)', r'[A\1]', body)
    return re.sub(r'^#{1,3} ', '', text, flags=re.MULTILINE)
