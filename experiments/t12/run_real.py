"""Run an ordinary user question against a registered development snapshot."""
import argparse
import json
import os
from pathlib import Path

from metricguard import TaskService


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path, required=True)
    parser.add_argument('--start', required=True)
    parser.add_argument('--end', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--image', required=True)
    parser.add_argument('--question', default='分析本期新增用户自然日次日留存下降原因，与前一等长窗口比较，并给出支持和反对证据。')
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError('Use a fresh output directory')
    token = os.environ.get('ANTHROPIC_AUTH_TOKEN')
    if not token:
        raise ValueError('ANTHROPIC_AUTH_TOKEN required')
    with TaskService(args.output, args.image, {'development': args.database}, token=token) as service:
        result = service.run(service.create(args.question, 'development', (args.start, args.end), mode='diagnose'))
        (args.output / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('id', 'outcome', 'model_calls', 'tool_calls', 'tokens', 'limitations')}, ensure_ascii=True))


if __name__ == '__main__':
    main()
