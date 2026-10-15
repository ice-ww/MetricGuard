"""Metric maturity and explicit authorization of incomplete requested ranges."""
from datetime import date, datetime, timedelta, timezone
from typing import Any
import re
from .time_windows import display


SOURCES = {
    'retention': ('users', 'sessions'), 'retained_cost': ('users', 'sessions', 'channel_daily'),
    'new_cost': ('users', 'channel_daily'), 'crash': ('users', 'sessions'),
    'completion': ('sessions', 'content_events'), 'effective': ('sessions', 'content_events', 'playback_telemetry'),
    'new_users': ('users',), 'play_starts': ('sessions', 'content_events'), 'spend': ('channel_daily',),
}
NAMES = {'users': '注册数据', 'sessions': '会话数据', 'channel_daily': '渠道支出数据',
         'content_events': '播放事件数据', 'playback_telemetry': '独立观看进度数据'}


def assess(metric: str, rows: list, requested: list[str] | None) -> dict[str, Any]:
    dates = {source: datetime.fromisoformat(value).astimezone(timezone(timedelta(hours=8))).date()
             for source, value in rows}
    offsets = {source: int(source == 'sessions' and metric in ('retention', 'retained_cost'))
               for source in SOURCES[metric]}
    cutoff = min(dates[source] - timedelta(days=offset) for source, offset in offsets.items())
    window = requested or [(cutoff - timedelta(days=7)).isoformat(), cutoff.isoformat()]
    start, end = map(date.fromisoformat, window)
    available_end = min(end, cutoff)
    missing = [max(start, cutoff).isoformat(), end.isoformat()] if end > cutoff else None
    gaps = [{'source': source, 'complete_before': dates[source].isoformat(),
             'required_complete_before': (end + timedelta(days=offset)).isoformat(),
             'maturity_days': offset}
            for source, offset in offsets.items() if dates[source] < end + timedelta(days=offset)]
    return {'requested_window': list(window), 'available_window': [start.isoformat(), available_end.isoformat()] if start < available_end else None,
            'missing_window': missing, 'gaps': gaps, 'cutoff': cutoff.isoformat()}


def explain(coverage: dict[str, Any]) -> str:
    text = '请求范围：' + display(coverage['requested_window']) + '。'
    available = coverage['available_window']
    text += '按数据齐备水位可用范围：' + (display(available) if available else '无可用日期') + '。'
    if coverage['missing_window']:
        text += '未齐备的指标日期：' + display(coverage['missing_window']) + '。'
    for gap in coverage['gaps']:
        text += NAMES[gap['source']] + '仅保证 ' + gap['complete_before'] + ' 之前齐备；'
        if gap['maturity_days']:
            text += '自然日次日留存还要求 D+1 会话齐备；'
        text += '补齐原请求需该数据源至少覆盖到 ' + gap['required_complete_before'] + '（不含该日）。'
    if coverage['gaps']:
        if available:
            text += '也可自由输入上述可用范围内的具体日期。'
        text += '下一步：补齐所列数据源后使用更新快照重跑，或另行指定可用日期。水位是完整性边界，不是预计更新时间。'
    return text


def options(coverage: dict[str, Any]) -> list[str]:
    return ['使用可用范围：' + display(coverage['available_window']), '保留原范围，返回不足说明']


def apply_answer(data: dict[str, Any], answer: str) -> None:
    coverage = data['coverage']
    if any(term in answer for term in ('拒绝', '不缩小', '不接受', '不同意', '不要', '保留原范围')):
        coverage['decision'] = 'keep_original'
        coverage['authorization'] = dict(data['answers'][-1])

    elif answer in (options(coverage)[0], '接受', '同意', '使用可用范围'):
        coverage['decision'] = 'use_available'
        coverage['confirmed_window'] = list(coverage['available_window'])
        coverage['authorization'] = dict(data['answers'][-1])
    else:
        from .time_windows import parse_time, DATE, RELATIVE
        window, _ = parse_time(answer, data.get('time_anchor'))
        available = coverage['available_window']
        questioning = any(term in answer for term in ('?', '？', '吗', '是否', '能否', '能不能', '假如', '如果'))
        # A date mention is not consent: accept a bare range or a bounded affirmative command.
        selection = re.sub(r'^(?:仅使用|使用|改为|选择|确认|只看|就看)\s*', '', answer.strip())
        selection = re.sub(DATE + '|' + RELATIVE, '', selection)
        explicit_choice = bool(re.fullmatch(r'[\s至到—~～,，\-]*', selection))
        if explicit_choice and not questioning and window and available and available[0] <= window[0] < window[1] <= available[1]:
            coverage['decision'] = 'use_available'
            coverage['confirmed_window'] = window
            coverage['authorization'] = dict(data['answers'][-1])
