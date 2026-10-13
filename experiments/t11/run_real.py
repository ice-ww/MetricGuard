"""Run a fresh development task on the approved Flash provider; preserve every attempt."""
import argparse
import json
import os
from pathlib import Path
import platform

from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--image', required=True)
    parser.add_argument('--seed', type=int, default=1111)
    parser.add_argument('--question', default='分析新增用户自然日次日留存：先核对注册系统分布，再根据实际结果选择一个系统查询该窗口的新增和次日留存人数，给出有限事实与尚未验证的问题。')
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError('Use a fresh directory; previous attempts must remain available')
    token = os.environ.get('ANTHROPIC_AUTH_TOKEN')
    if not token:
        raise ValueError('ANTHROPIC_AUTH_TOKEN is required; never put the token in arguments')
    snapshot = build_snapshot(args.output / 'data', scenario='normal', seed=args.seed)
    with TaskService(args.output / 'service', args.image, {'development': snapshot.database}, token=token) as service:
        task = service.create(args.question, 'development', ('2026-01-01', '2026-01-08'), mode='diagnose')
        result = service.run(task)
        (args.output / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'task': task, 'status': result['status'], 'outcome': result['outcome'],
                      'model_calls': result['model_calls'], 'tool_calls': result['tool_calls'],
                      'accounted_tokens': result['tokens'], 'python': platform.python_version(),
                      'output': str(args.output)}, ensure_ascii=True))


if __name__ == '__main__':
    main()
