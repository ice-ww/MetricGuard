"""Local command line entry point; model credentials never enter task metadata."""
import argparse
import json
import os
from pathlib import Path
from .service import TaskService


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--state-dir', type=Path, required=True)
    parser.add_argument('--image', required=True, help='Administrator validated immutable Docker image ID')
    parser.add_argument('--snapshot', action='append', default=[], metavar='ID=PATH')
    parser.add_argument('--base-url', default='https://api.deepseek.com/anthropic')
    sub = parser.add_subparsers(dest='command', required=True)
    create = sub.add_parser('create')
    create.add_argument('question'); create.add_argument('snapshot_id')
    create.add_argument('--window', nargs=2)
    for name in ('run', 'inspect', 'report', 'trace'):
        sub.add_parser(name).add_argument('task')
    args = parser.parse_args()
    snapshots = {}
    for item in args.snapshot:
        key, path = item.split('=', 1)
        snapshots[key] = Path(path)
    with TaskService(args.state_dir, args.image, snapshots,
                     token=os.environ.get('ANTHROPIC_AUTH_TOKEN', ''), base_url=args.base_url) as service:
        if args.command == 'create':
            result = {'task_id': service.create(args.question, args.snapshot_id, tuple(args.window) if args.window else None)}
        else:
            result = getattr(service, args.command)(args.task)
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
