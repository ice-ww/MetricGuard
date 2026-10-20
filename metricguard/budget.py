"""Read-only presentation of existing accounting, never a dispatch decision."""
import json
from typing import Any


def describe(state: dict[str, Any]) -> dict[str, Any]:
    models = [attempt for attempt in state['attempts'] if attempt['kind'] == 'model']
    unsettled = [attempt for attempt in models if attempt['actual'] is None]
    pending = sum(attempt['state'] in ('reserved', 'sent') for attempt in unsettled)
    stopped_reason = None
    if state.get('outcome') == 'budget_exhausted':
        reasons = [json.loads(event['detail']).get('reason') for event in state['trace']
                   if event['event'] == 'execution_stopped']
        reason = reasons[-1] if reasons else None
        stopped_reason = {
            'unknown model usage': '模型用量未知，预算保护已停止继续执行。',
            'unknown usage blocks further model dispatch': '模型用量未知，预算保护已停止继续执行。',
            'budget blocked by unknown model usage': '模型用量未知，预算保护已停止继续执行。',
            'active time budget exhausted': '累计执行时间预算不足，服务已停止继续执行。',
            'final report budget reserved': '剩余额度需保留给报告，预算保护已停止继续执行。',
            'budget exhausted': '预算不足以继续执行，服务已停止（可能是下一次调用所需额度不足）。',
        }.get(reason if isinstance(reason, str) else '', '服务记录因预算保护停止，具体限制未记录。')
    return {
        'model_calls': state['model_calls'], 'tool_calls': state['tool_calls'],
        'limits': state['limits'], 'tokens': state['tokens'],
        'known_tokens': sum(attempt['actual'] for attempt in models if attempt['actual'] is not None),
        'reserved_tokens': sum(attempt['reserved'] for attempt in unsettled),
        'pending_calls': pending, 'unknown_calls': len(unsettled) - pending,
        'active_seconds': state['active'], 'stopped_reason': stopped_reason,
        'near_limits': [key for key, used in (
            ('model', state['model_calls']), ('tool', state['tool_calls']), ('tokens', state['tokens']))
            if used * 5 >= state['limits'][key] * 4],
    }
