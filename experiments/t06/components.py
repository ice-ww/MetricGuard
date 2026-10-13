"""Explicit definitions for queryable component counts, without evaluation data."""
from typing import Any

DEFINITIONS: list[dict[str, Any]] = [
    {'id': 'new_users', 'name': '新增用户数', 'aliases': ['新增注册人数', '新注册用户数', '新增人数'],
     'definition': '注册窗口内首次注册的去重用户数。',
     'numerator': 'COUNT DISTINCT users.user_id', 'denominator': '计数，无分母',
     'dimensions': 'registration_os / registration_version / channel 固定注册归属',
     'joins': '不需要会话关联', 'time': 'Asia/Shanghai 注册日期 [start,end)；users 水位完整',
     'pitfalls': '不混入老用户或活跃用户；计数不要求次日成熟'},
    {'id': 'play_starts', 'name': '去重播放开始数', 'aliases': ['播放开始次数', '播放开始数'],
     'definition': '指定播放开始窗口内的独立播放实例数。',
     'numerator': 'content_events 中 start 的去重 play_id 数', 'denominator': '计数，无分母',
     'dimensions': 'sessions.os / version 实际运行归属',
     'joins': 'content_events.session_id = sessions.session_id',
     'time': 'Asia/Shanghai 播放开始日期 [start,end)；sessions/content_events 水位完整',
     'pitfalls': '重复上报去重；重复观看的新 play_id 分开计数'},
    {'id': 'spend', 'name': '渠道同期支出', 'aliases': ['渠道支出', '支出（分）', '支出(分)'],
     'definition': '指定渠道与日期窗口的支出总分。',
     'numerator': 'SUM channel_daily.spend_cents', 'denominator': '金额，无分母',
     'dimensions': 'channel', 'joins': '不与用户明细直接连接',
     'time': 'Asia/Shanghai day 在 [start,end)；channel_daily 水位完整',
     'pitfalls': '金额单位分；不得多对多关联放大金额；缺失覆盖不可当零'},
]


def component_definition(query: str) -> dict | None:
    if any(term in query for term in ('除', '比例', '成本', '率')):
        return None
    matches = [d for d in DEFINITIONS if any(name in query for name in [d['name'], *d['aliases']])]
    # Mixed metric requests need normal ranking/clarification, never first-match routing.
    return matches[0] if len(matches) == 1 else None
