"""Bounded natural-date interpretation; uncertainty is a clarification, never a guess."""
from datetime import date, datetime, timedelta, timezone
import re
from typing import Any

SHANGHAI = timezone(timedelta(hours=8))
DATE = r'(?<!\d)\d{4}(?:[-/]\d{1,2}[-/]\d{1,2}|年\d{1,2}月\d{1,2}日)(?!\d)'
RELATIVE = r'昨天|前天|今天|本周|上周|(?:最近|近)\s*\d+\s*天'
VAGUE = (r'最近|近期|前段时间|过去|未来|上个月|本月|上月|下月|这个月|去年|今年|上星期|这几天|'
         r'上上周|下周|这周|周末|季度|近[一二三四五六七八九十两]+天|近\d+[日周月年]|'
         r'\d{1,2}月|\d{4}年|\d{4}[-/]\d')


def display(window: list[str] | tuple[str, str]) -> str:
    return f'{window[0]} 至 {window[1]}（结束日不包含）'


def parse_time(text: str, anchor: str | None) -> tuple[list[str] | None, str]:
    explicit = list(re.finditer(DATE, text))
    relatives = list(re.finditer(RELATIVE, text))
    remainder = re.sub(RELATIVE, '', re.sub(DATE, '', text))
    if re.search(VAGUE, remainder):
        return None, 'ambiguous'
    if re.search(r'(?:本周|上周)[一二三四五六日天末1-7]|上午|下午|凌晨|晚上|中午|傍晚|\d+点|\d+:\d+', text):
        return None, 'ambiguous'
    if explicit and re.search(r'(?:至|到|[-~～])\s*\d|\d{1,2}(?:日|号|月)', remainder):
        return None, 'ambiguous'
    if (explicit or relatives) and re.search(r'之前|以前|之后|以后|截至|截止|以来', text):
        return None, 'ambiguous'
    matches = explicit + relatives
    if len(matches) == 1:
        matched = matches[0]
        if re.search(r'(?:从|自|到|至)\s*$', text[:matched.start()]) or re.match(r'\s*(?:起|开始|前|后)', text[matched.end():]):
            return None, 'ambiguous'
    try:
        if explicit and relatives or len(relatives) > 1 or len(explicit) > 2:
            return None, 'ambiguous'
        if explicit:
            if len(explicit) == 2 and not re.fullmatch(r'\s*(?:至|到|—|~|～|,|，|-)\s*', text[explicit[0].end():explicit[1].start()]):
                return None, 'ambiguous'
            dates = [date(*map(int, re.findall(r'\d+', m.group()))) for m in explicit]
            if len(dates) == 1:
                start, end = dates[0], dates[0] + timedelta(days=1)
            else:
                start, end = dates
                if not ('结束日不包含' in text or re.search(r'\[[^\]]+\)', text)):
                    end += timedelta(days=1)
            if start >= end:
                return None, 'ambiguous'
            return [start.isoformat(), end.isoformat()], 'explicit'
        if relatives:
            if anchor is None:
                return None, 'ambiguous'
            today = datetime.fromisoformat(anchor).astimezone(SHANGHAI).date()
            term = relatives[0].group()
            if term in ('昨天', '前天', '今天'):
                start = today - timedelta(days={'昨天': 1, '前天': 2, '今天': 0}[term])
                end = start + timedelta(days=1)
            elif term in ('本周', '上周'):
                start = today - timedelta(days=today.weekday() + (7 if term == '上周' else 0))
                end = start + timedelta(days=7)
            else:
                digits = re.search(r'\d+', term)
                assert digits is not None  # matched by RELATIVE
                count = int(digits.group())
                if count <= 0:
                    return None, 'ambiguous'
                start, end = today - timedelta(days=count), today
            return [start.isoformat(), end.isoformat()], 'relative'
        if re.search(VAGUE, text):
            return None, 'ambiguous'
    except (ValueError, OverflowError):
        return None, 'ambiguous'
    return None, 'absent'


def metric_text(text: str) -> str:
    """Date numbers are not retention horizons (e.g. June 8th is not 8-day retention)."""
    return re.sub(RELATIVE, '', re.sub(DATE, '', text))


def resolve(data: dict[str, Any]) -> dict[str, Any] | None:
    if data.get('time_resolved'):
        return None
    window, kind = parse_time(data.get('analysis_question', data['question']), data.get('time_anchor'))
    if kind == 'ambiguous':
        return {'reason': 'time_window_required', 'prompt': '请提供明确的分析日期，例如 2026-06-08 至 2026-06-14（包含首尾日期）。', 'options': []}
    preset = data.get('requested_window')
    if window and preset and list(preset) != window:
        return {'reason': 'time_window_conflict',
                'prompt': f'问题中的日期为 {display(window)}；预设日期为 {display(preset)}。请选择分析范围。',
                'options': [display(window), display(preset)], 'windows': [window, list(preset)]}
    if window:
        data['requested_window'] = window
    data['time_resolved'] = True
    data['time_resolution'] = kind if window else 'preset' if preset else 'snapshot_default'
    return None


def apply_time_answer(data: dict[str, Any], pending: dict[str, Any], answer: str) -> None:
    window = None
    for option, candidate in zip(pending.get('options', []), pending.get('windows', [])):
        if answer == option:
            window = candidate
    if window is None:
        window, _ = parse_time(answer, data.get('time_anchor'))
    if window is not None:
        data['requested_window'] = list(window)
        data['time_resolved'] = True
        data['time_resolution'] = 'user_confirmed'
