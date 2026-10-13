"""Real resource failure inside the final loop, then a successful task in the same service."""
import argparse
import json
from pathlib import Path
from typing import Any

import httpx2 as httpx

from experiments.t01.references import python_metrics
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService

COUNT_SQL = "SELECT COUNT(*) AS users FROM users WHERE registered_at >= '2026-01-01T00:00:00+08:00' AND registered_at < '2026-01-08T00:00:00+08:00'"
HEAVY_SQL = "SELECT COUNT(*) AS combinations FROM sessions a, sessions b, sessions c WHERE a.user_id <> b.user_id AND b.user_id <> c.user_id"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--image', required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError('Use a fresh output directory')
    snapshot = build_snapshot(args.output / 'data', scenario='normal', seed=1112)
    expected = sum(row['users'] for row in python_metrics(snapshot.database, '2026-01-01', '2026-01-08')['retention'])
    sent: list[dict] = []
    phase = 'resource'

    def provider(request):
        value: dict[str, Any]
        sent.append({'phase': phase, 'request': json.loads(request.content)})
        count = sum(item['phase'] == phase for item in sent)
        if phase == 'resource':
            if count > 2:
                raise AssertionError('Resource failure must not cause another model request')
            value = {'action': 'query', 'sql': COUNT_SQL if count == 1 else HEAVY_SQL}
        else:
            value = {'sql': COUNT_SQL} if count == 1 else {'facts': [{'row': 0, 'column': 'users', 'value': expected}]}
        return httpx.Response(200, json={'id': 'resource_fixture', 'type': 'message', 'role': 'assistant',
            'model': 'deepseek-flash', 'content': [{'type': 'text', 'text': json.dumps(value)}],
            'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 31, 'output_tokens': 17}})

    with TaskService(args.output / 'service', args.image, {'dev': snapshot.database}, token='controlled',
                     transport=httpx.MockTransport(provider)) as service:
        first_id = service.create('新增用户自然日次日留存', 'dev', ('2026-01-01', '2026-01-08'), mode='diagnose')
        first = service.run(first_id)
        (args.output / 'first.json').write_text(json.dumps(first, ensure_ascii=False, indent=2), encoding='utf-8')
        failures = [json.loads(a['result']) for a in first['attempts'] if a['kind'] == 'tool' and a['result']]
        failures = [result for result in failures if result.get('status') in ('timeout', 'engine_memory', 'engine_disk', 'query_timeout')]
        assert len(failures) == 1, first
        assert failures[0]['cleanup_verified'], failures[0]
        assert first['model_calls'] == 2 and first['tokens'] == 96
        first_report = service.report(first_id)
        assert first_report is not None
        assert first['evidence'] and first_report['deterministic']
        assert any(fact['value'] == expected for fact in first_report['facts'])
        phase = 'next_task'
        second_id = service.create('新增用户自然日次日留存', 'dev', ('2026-01-01', '2026-01-08'))
        second = service.run(second_id)
        (args.output / 'next.json').write_text(json.dumps(second, ensure_ascii=False, indent=2), encoding='utf-8')
        assert second['outcome'] == 'facts_available', second
        second_report = service.report(second_id)
        assert second_report is not None
        assert second_report['facts'][0]['value'] == expected
        assert second['tokens'] == 96 and second['query_result']['cleanup_verified']
    record = {'passed': True, 'image': args.image, 'independent_users': expected,
              'failure': failures[0], 'first': first, 'next_task': second, 'provider_requests': sent}
    (args.output / 'result.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'passed': True, 'resource_status': failures[0]['status'], 'provider_sends': len(sent)}))


if __name__ == '__main__':
    main()
