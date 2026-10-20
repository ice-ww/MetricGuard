"""Read-only presentation of reliable execution events, including legacy records."""
from datetime import datetime
import json
from typing import Any


def describe(state: dict[str, Any], status: str, now: datetime) -> dict[str, Any]:
    latest = next((event for event in reversed(state['trace']) if event.get('occurred_at')), None)
    instant = latest['occurred_at'] if latest else None
    action = None
    if status == 'running' and latest:
        if latest['event'] == 'progress_phase':
            action = {'prepare':'核对分析条件', 'report':'整理并校验报告'}.get(json.loads(latest['detail']))
        elif latest['event'] == 'sent':
            attempt = next((a for a in state['attempts'] if a['id'] == latest['detail']), None)
            if attempt:
                operation = attempt['operation'].split(':')[0]
                if attempt['kind'] == 'model':
                    action = {'diagnose':'请求模型选择下一步分析', 'repair':'请求模型修复查询',
                              'sql_plan':'请求模型规划查询', 'baseline_plan':'请求模型规划查询',
                              'report':'请求模型整理报告', 'baseline_report':'请求模型整理报告'}.get(operation, '请求模型')
                else:
                    action = {'retrieval':'检索指标口径', 'schema':'读取数据结构',
                              'watermarks':'查询数据齐备范围', 'sql':'执行数据查询',
                              'diagnostic_sql':'执行数据查询', 'baseline_sql':'执行数据查询'}.get(operation, '执行工具')
    return {'action':action, 'latest_at':instant,
            'quiet':bool(status == 'running' and instant and (now - datetime.fromisoformat(instant)).total_seconds() >= 60)}
