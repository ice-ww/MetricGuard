"""Bind independently executed safety checks to an immutable acceptance run."""
from pathlib import Path
import xml.etree.ElementTree as ET
import subprocess
import sys
from metricguard.semantic_rubric import digest

REQUIRED_MODULES={'tests.test_t02_policy','tests.test_t02_sandbox','tests.test_t02_acceptance',
    'tests.test_t03_limits','tests.test_t03_supervisor','tests.test_t04_statistics','tests.test_t04_reference',
    'tests.test_t05','tests.test_t07_adapter','tests.test_t07_scheduler','tests.test_t08',
    'tests.test_t09_service','tests.test_t10_service','tests.test_t10_recovery','tests.test_t17_service'}


def collect_tests(repository: Path) -> list[str]:
    result=subprocess.run([sys.executable,'-m','pytest','--collect-only','-q','tests'],cwd=repository,
        capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=60)
    if result.returncode: raise ValueError('safety collection failed')
    identities=[]
    for line in result.stdout.splitlines():
        if line.startswith(('tests/', 'tests\\')):
            path, separator, name = line.strip().partition('::')
            # Parameter names contain pytest escapes, not filesystem separators.
            identities.append(path.replace('\\', '/') + separator + name)
    if not identities or any('::' not in value for value in identities) or len(identities)!=len(set(identities)):
        raise ValueError('invalid complete collection manifest')
    return sorted(identities)


def validate_safety(receipt: dict, configuration: dict, repository: Path) -> dict:
    from metricguard.evaluation import file_hash
    if receipt.get('configuration_hash')!=digest(configuration): raise ValueError('safety configuration mismatch')
    if receipt.get('exit_code')!=0: raise ValueError('safety execution failed')
    if not receipt.get('test_hashes'): raise ValueError('safety test sources missing')
    for name,expected in receipt['test_hashes'].items():
        path=(repository/name).resolve()
        if not path.is_relative_to(repository.resolve()) or file_hash(path)!=expected:
            raise ValueError('safety test source drift')
    expected_files={module.replace('.','/')+'.py' for module in REQUIRED_MODULES}
    if not expected_files<=receipt['test_hashes'].keys(): raise ValueError('required safety sources missing')
    root=ET.fromstring(receipt['junit_xml'])
    cases=list(root.iter('testcase'))
    modules={case.get('classname') for case in cases}
    if not REQUIRED_MODULES<=modules or not cases:
        raise ValueError('required safety checks missing')
    if any(case.find(tag) is not None for case in cases for tag in ('failure','error','skipped')):
        raise ValueError('safety checks failed or skipped')
    suites=list(root.iter('testsuite'))
    if not suites or any(int(suite.get(k,'0')) for suite in suites for k in ('failures','errors','skipped')):
        raise ValueError('safety suite failed or skipped')
    expected=collect_tests(repository)
    if receipt.get('collected_nodeids')!=expected:
        raise ValueError('safety collection manifest changed or missing')
    actual=[str(case.get('classname')).replace('.','/')+'.py::'+str(case.get('name')) for case in cases]
    if sorted(actual)!=expected or sum(int(s.get('tests','0')) for s in suites)!=len(expected):
        raise ValueError('safety execution does not cover full collected suite')
    if not {node.split('::',1)[0] for node in expected}<=receipt['test_hashes'].keys():
        raise ValueError('collected test source hashes missing')
    return {'status':'passed','tests':len(cases),'required_modules':sorted(REQUIRED_MODULES),
            'receipt_hash':digest(receipt),'configuration_hash':digest(configuration)}
