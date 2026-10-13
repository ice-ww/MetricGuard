"""Child process: durable provider marker and administrator fault injection."""
import argparse
import json
import os
from pathlib import Path

import httpx2 as httpx

from metricguard import TaskService


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('root', type=Path)
    parser.add_argument('database', type=Path)
    parser.add_argument('image')
    parser.add_argument('point')
    args = parser.parse_args()
    args.root.mkdir(parents=True, exist_ok=True)

    def fault(point: str) -> None:
        if point == args.point:
            os._exit(73)

    def provider(request: httpx.Request) -> httpx.Response:
        with (args.root / 'provider.jsonl').open('a', encoding='utf-8') as out:
            out.write(json.dumps({'request': json.loads(request.content)}) + '\n')
            out.flush()
            os.fsync(out.fileno())
        fault('after_send')
        return httpx.Response(200, json={
            'id': 'msg_recovery', 'type': 'message', 'role': 'assistant', 'model': 'deepseek-flash',
            'content': [{'type': 'text', 'text': json.dumps({'sql': 'SELECT COUNT(*) AS users FROM users'})}],
            'stop_reason': 'end_turn', 'stop_sequence': None,
            'usage': {'input_tokens': 29, 'output_tokens': 13}})

    with TaskService(args.root / 'service', args.image, {'development': args.database},
                     token='controlled', transport=httpx.MockTransport(provider), fault_hook=fault) as service:
        task = service.create('新增用户自然日次日留存', 'development', ('2026-01-01', '2026-01-08'))
        with (args.root / 'task.txt').open('w') as out:
            out.write(task)
            out.flush()
            os.fsync(out.fileno())
        service.run(task)
    raise AssertionError('fault point was not reached')


if __name__ == '__main__':
    main()
