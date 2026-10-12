"""Explicit real API experiment: python -m experiments.t07.run --output artifacts/t07/run.json."""
import argparse
import importlib.metadata
import json
import os
import platform
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from experiments.t05 import Ledger
from experiments.t07 import ModelAdapter, Request
from experiments.t07.verify import verify_report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.output.with_suffix('.sqlite').exists():
        parser.error('use a fresh output path; previous evidence must not be overwritten')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    ledger = Ledger(args.output.with_suffix('.sqlite'))
    adapter = ModelAdapter(ledger, 'deepseek-flash', 'https://api.deepseek.com/anthropic',
                           os.environ['ANTHROPIC_AUTH_TOKEN'])
    request = Request('This is an accounting validation. Reply only OK. Do not use tools.',
        'Synthetic count: two registered users, one returning user. No private data.',
        [{'role': 'user', 'content': 'Remember the synthetic count.'},
         {'role': 'assistant', 'content': 'Understood.'},
         {'role': 'user', 'content': 'Reply OK.'}],
        [{'name': 'lookup_metric', 'description': 'Read a synthetic metric definition.',
          'input_schema': {'type': 'object', 'properties': {'name': {'type': 'string'}}, 'required': ['name']}}])
    report: dict[str, Any] = {'created_utc': datetime.now(timezone.utc).isoformat(),
              'python': platform.python_version(), 'sdk': importlib.metadata.version('anthropic'),
              'model': 'deepseek-flash', 'provider_version_mapping': 'DeepSeek-V4.1-Flash',
              'base_url': 'https://api.deepseek.com/anthropic', 'max_retries': 0,
              'request': request.payload('deepseek-flash'), 'count_probe': adapter.count_input(request),
              'strict_token_cap_verified': False, 'cases': []}
    for name, stream, cancel in [('normal', False, None), ('stream_complete', True, None),
                                 ('stream_cancelled', True, 1)]:
        task = ledger.create_task()
        result = adapter.call(task, name, request, attempt_id=task + '-attempt',
                              stream=stream, cancel_after_events=cancel)
        report['cases'].append({'name': name, 'result': result, 'ledger': ledger.inspect(task)})
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    adapter.close()
    report['independent_verification'] = verify_report(report)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'artifact': str(args.output), 'cases': [(c['name'], c['result']['status']) for c in report['cases']]}))


if __name__ == '__main__':
    main()
