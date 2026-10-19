"""One entry point for repository verification: python -m tools.check."""
import argparse
import os
from pathlib import Path
import subprocess
import sys
import uuid
import xml.etree.ElementTree as ET

from tools import evidence


def tests(root: Path) -> int:
    if not os.environ.get('METRICGUARD_TEST_IMAGE', '').startswith('sha256:'):
        print('tests: set METRICGUARD_TEST_IMAGE to the built Docker image sha256 ID', flush=True)
        return 1
    output = root / 'artifacts/checks' / uuid.uuid4().hex
    output.mkdir(parents=True)
    junit = output / 'pytest.xml'
    result = subprocess.run([sys.executable, '-m', 'pytest', '-q', f'--junitxml={junit}'], cwd=root)
    if result.returncode:
        return result.returncode
    try:
        tree = ET.parse(junit)
        cases = list(tree.iter('testcase'))
        if not cases or any(case.find(tag) is not None for case in cases
                            for tag in ('skipped', 'failure', 'error')):
            print(f'tests: empty, skipped or failed cases in {junit}', flush=True)
            return 1
    except (OSError, ET.ParseError) as exc:
        print(f'tests: unreadable JUnit report: {exc}', flush=True)
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('stage', nargs='?', default='all', choices=['all', 'evidence', 'types', 'tests'])
    args = parser.parse_args()
    root = args.root.resolve()
    for stage in (['evidence', 'types', 'tests'] if args.stage == 'all' else [args.stage]):
        print(f'check: {stage}', flush=True)
        if stage == 'evidence':
            code = evidence.check(root)
        elif stage == 'types':
            code = 0
            for platform in ('win32', 'linux'):
                print(f'types: {platform}', flush=True)
                result = subprocess.run([sys.executable, '-m', 'mypy', '--platform', platform,
                                         '--cache-dir', f'.mypy_cache/{platform}'], cwd=root)
                code = code or result.returncode
        else:
            code = tests(root)
        if code:
            return code
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
