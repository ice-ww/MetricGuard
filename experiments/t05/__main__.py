"""Public repeatable acceptance entry: python -m experiments.t05 validate OUTPUT."""
import argparse
import importlib.metadata
import json
import platform
import subprocess
import sys
import time
from pathlib import Path
from .service import TaskService
from .ledger import Ledger

def validate(root: Path) -> dict:
    if root.exists():
        raise ValueError('output must not exist')
    root.mkdir(parents=True)
    checks: list[dict] = []
    def check(name: str, expected: object, actual: object) -> None:
        checks.append({'name': name, 'expected': expected, 'actual': actual, 'passed': expected == actual})
    crash_rows = [('after_reserve', 0, 100, 'unknown'), ('after_send', 1, 100, 'unknown'),
                  ('after_result', 1, 30, 'completed'), ('before_checkpoint', 1, 30, 'completed'),
                  ('after_checkpoint', 1, 30, 'completed')]
    for point, sends, tokens, attempt_state in crash_rows:
        case = root / point
        result = subprocess.run([sys.executable, '-m', 'experiments.t05', 'crash-worker', str(case), point], capture_output=True, timeout=30)
        check(point + ': exit', 73, result.returncode)
        task = (case / 'task.txt').read_text()
        provider = case / 'provider.jsonl'
        before = provider.read_text().splitlines() if provider.exists() else []
        check(point + ': external sends', sends, len(before))
        with TaskService(case) as service:
            data = service.inspect(task)
            check(point + ': task status', 'interrupted', data['status'])
            check(point + ': reserved attempt count', 1, data['model_calls'])
            check(point + ': retained token accounting', tokens, data['tokens'])
            check(point + ': attempt status', attempt_state, data['attempts'][0]['state'])
            try:
                service.run(task)
                rejected = False
            except ValueError:
                rejected = True
            check(point + ': no original resume', True, rejected)
            new_task = service.rerun(task)
            check(point + ': rerun link', task, service.inspect(new_task)['parent'])
            check(point + ': new task counter', 0, service.inspect(new_task)['model_calls'])
            (case / 'observed.json').write_text(json.dumps(data, indent=2), encoding='utf-8')
        after = provider.read_text().splitlines() if provider.exists() else []
        check(point + ': no restart sends', before, after)
    case = root / 'clarification'
    with TaskService(case) as service:
        task = service.create()
        first = service.run(task)
        check('first question round', 1, first['rounds'])
        active = first['active']
        time.sleep(.1)
        check('wait excluded', active, service.inspect(task)['active'])
    with TaskService(case) as service:
        check('persisted waiting', 'waiting', service.inspect(task)['status'])
        second = service.answer(task, first['question'], first['version'], 'controlled answer')
        check('same task', task, second['id'])
        check('second question round', 2, second['rounds'])
        check('resume cumulative calls', 2, second['model_calls'])
        check('resume cumulative usage', 60, second['tokens'])
        check('resume active accumulated', True, second['active'] > active)
        for name, action in [
            ('stale answer rejected', lambda: service.answer(task, first['question'], first['version'], 'stale')),
            ('forged model state rejected', lambda: service.model_reply(task, {'text': 'answer', 'model_calls': 0})),
            ('third question rejected', lambda: service.run(service.create(), questions=3)),
        ]:
            try:
                action(); rejected = False
            except ValueError:
                rejected = True
            check(name, True, rejected)
        final = service.answer(task, second['question'], second['version'], 'answer')
        check('complete after two rounds', 'ended', final['status'])
        check('no duplicate calls', 3, len((case / 'provider.jsonl').read_text().splitlines()))
        (case / 'observed.json').write_text(json.dumps(final, indent=2), encoding='utf-8')
    ledger = Ledger(root / 'retry.sqlite')
    task = ledger.create_task()
    for idx in range(3):
        attempt = ledger.reserve(task, 'sql-op', 'tool', attempt_id=f'attempt-{idx}')
        ledger.mark_sent(attempt['attempt_id'])
        ledger.settle(attempt['attempt_id'], {'ok': idx == 2}, failed=idx < 2)
    ledger.reserve(task, 'sql-op', 'tool', attempt_id='attempt-2')
    data = ledger.inspect(task)
    check('two failures plus success calls', 3, data['tool_calls'])
    check('failed attempts retained', ['failed', 'failed', 'completed'], [r['state'] for r in data['attempts']])
    report = {'environment': {'python': platform.python_version(), 'platform': platform.platform(),
              'langgraph': importlib.metadata.version('langgraph'), 'sqlite_saver': importlib.metadata.version('langgraph-checkpoint-sqlite')},
              'checks': checks, 'passed': sum(c['passed'] for c in checks), 'total': len(checks),
              'scope': 'controlled providers, local sync graph, no diagnosis or remote model'}
    (root / 'report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    return report

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['validate', 'crash-worker'])
    parser.add_argument('output', type=Path)
    parser.add_argument('point', nargs='?')
    args = parser.parse_args()
    if args.command == 'crash-worker':
        with TaskService(args.output, crash_point=args.point) as service:
            task = service.create()
            (args.output / 'task.txt').write_text(task)
            service.run(task)
        raise RuntimeError('crash point not hit')
    result = validate(args.output)
    print(json.dumps({'passed': result['passed'], 'total': result['total']}))
    if result['passed'] != result['total']:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
