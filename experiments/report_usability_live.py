"""Fresh phrasing against real provider, with existing independent reference checks."""
import gzip
import json
import os
from pathlib import Path
from uuid import uuid4
from experiments.f5_live import QUESTIONS, run


def main():
    QUESTIONS['simple'] = '这个日期窗口内的新增用户数是多少？请给出具体人数和可核查引用。'
    QUESTIONS['A1'] = '请比较新增用户自然日次日留存：指出具体系统版本，检查版本崩溃相关解释与反对证据。'
    root = Path('artifacts/report-usability-live') / uuid4().hex
    root.mkdir(parents=True)
    results = []
    for case in ('simple', 'A1'):
        try:
            result = run(case, root, os.environ['METRICGUARD_TEST_IMAGE'])
        except Exception as error:
            result = {'case': case, 'passed': False, 'error_type': type(error).__name__, 'error': str(error)}
        results.append(result)
        print(json.dumps(result, ensure_ascii=False), flush=True)
        (root / 'summary.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    receipts = {p.parent.name: json.loads(p.read_text(encoding='utf-8')) for p in root.glob('*/result.json')}
    archive = {'questions': {k: QUESTIONS[k] for k in ('simple','A1')}, 'results': results, 'receipts': receipts}
    Path('docs/validation/report-usability-live.json.gz').write_bytes(gzip.compress(json.dumps(archive, ensure_ascii=False, indent=2).encode(), mtime=0))
    if not all(r['passed'] for r in results):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
