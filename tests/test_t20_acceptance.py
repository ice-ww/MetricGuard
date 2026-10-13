"""Synthetic receipt fixtures test audit behavior, not actual safety acceptance."""
from copy import deepcopy
from pathlib import Path
import pytest
from metricguard.acceptance import REQUIRED_MODULES, validate_safety
from metricguard.evaluation import file_hash
from metricguard.semantic_rubric import digest
from tests.test_t18_runner import setup_bundle


def receipt_fixture(root, config):
    files={}
    for module in REQUIRED_MODULES:
        name=module.replace('.','/')+'.py'; path=root/name
        path.parent.mkdir(parents=True,exist_ok=True); path.write_text('def test_synthetic():\n    pass\n')
        files[name]=file_hash(path)
    xml='<testsuites><testsuite tests="'+str(len(REQUIRED_MODULES))+'">'+''.join(
        '<testcase classname="'+module+'" name="test_synthetic" />' for module in sorted(REQUIRED_MODULES))+'</testsuite></testsuites>'
    return {'configuration_hash':digest(config),'exit_code':0,'test_hashes':files,'junit_xml':xml,
            'collected_nodeids':sorted(module.replace('.','/')+'.py::test_synthetic' for module in REQUIRED_MODULES)}


@pytest.mark.parametrize('mutation',['configuration','missing_module','failed','skipped','exit','source','invented_test'])
def test_safety_receipt_rejects_incomplete_failed_or_stale_evidence(tmp_path,mutation):
    config={'version':'synthetic'}; receipt=receipt_fixture(tmp_path,config)
    assert validate_safety(receipt,config,tmp_path)['status']=='passed'
    if mutation=='configuration': receipt['configuration_hash']='stale'
    if mutation=='missing_module': receipt['junit_xml']=receipt['junit_xml'].replace('tests.test_t05','absent')
    if mutation=='failed': receipt['junit_xml']=receipt['junit_xml'].replace('name="test_synthetic" />','name="test_synthetic"><failure /></testcase>',1)
    if mutation=='skipped': receipt['junit_xml']=receipt['junit_xml'].replace('name="test_synthetic" />','name="test_synthetic"><skipped /></testcase>',1)
    if mutation=='exit': receipt['exit_code']=1
    if mutation=='source': (tmp_path/'tests/test_t05.py').write_text('changed')
    if mutation=='invented_test': receipt['junit_xml']=receipt['junit_xml'].replace('name="test_synthetic"','name="invented"')
    with pytest.raises(ValueError): validate_safety(receipt,config,tmp_path)


def test_reconfigure_preserves_tasks_and_sticky_regression(tmp_path):
    runner,case,artifact,config=setup_bundle(tmp_path)
    original=runner.access('selftest-v1',actor='controlled fixture',purpose='scorer_selftest')
    runner.access('selftest-v1',actor='controlled repair fixture',purpose='repair')
    revised=deepcopy(config); revised['model']['name']='new controlled provider'
    runner.reconfigure('selftest-v1','selftest-v2',revised,actor='controlled configuration update')
    current=runner.access('selftest-v2',actor='controlled fixture',purpose='scorer_selftest')
    assert current['cases']==original['cases'] and current['family']==original['family']
    assert runner.status('selftest-v2')['purpose']=='regression'


def test_safety_binding_does_not_turn_scorer_fixture_into_formal_acceptance(tmp_path):
    runner,case,artifact,config=setup_bundle(tmp_path)
    # The older scorer fixture's code.py would shadow Python's stdlib code module
    # during actual pytest collection. Use an innocuous fixture filename here.
    (runner.repository/'code.py').rename(runner.repository/'fixture_program.py')
    for key in ('code_hashes','prompt_hashes','rule_hashes','reference_hashes'):
        config[key]={'fixture_program.py':file_hash(runner.repository/'fixture_program.py')}
    runner.reconfigure('selftest-v1','collection-fixture',config,actor='synthetic collection setup')
    run=runner.run('collection-fixture',lambda *args:{'materials':{},'status':'ok','usage':{k:v for k,v in artifact['preflight'].items() if k!='status'}},
                   lambda *args:deepcopy(artifact),actor='controlled receipt test')
    receipt=receipt_fixture(runner.repository,config)
    runner.bind_safety(run,receipt)
    result=runner.results(run)
    assert result['safety']['status']=='passed'
    assert result['summary']['formal_acceptance_passed'] is False
    assert all(not row['formal_acceptance_passed'] for row in result['summary']['rounds'])
    (runner.repository/'tests/test_t05.py').write_text('changed after binding')
    assert runner.results(run)['safety']['status']=='invalid'


def test_safety_collection_preserves_escaped_parameter_identity(tmp_path):
    import subprocess
    import sys
    from metricguard.acceptance import collect_tests
    config={'version':'synthetic escaped ids'}
    receipt=receipt_fixture(tmp_path,config)
    source=tmp_path/'tests/test_t05.py'
    source.write_text('import pytest\n@pytest.mark.parametrize("value", ["中文", r"\\n"])\ndef test_escaped(value):\n    pass\n',encoding='utf-8')
    junit=tmp_path/'actual.xml'
    run=subprocess.run([sys.executable,'-m','pytest','-q','--junitxml='+str(junit)],cwd=tmp_path,capture_output=True)
    assert run.returncode==0
    receipt.update(junit_xml=junit.read_text(encoding='utf-8'),collected_nodeids=collect_tests(tmp_path))
    receipt['test_hashes']['tests/test_t05.py']=file_hash(source)
    assert validate_safety(receipt,config,tmp_path)['tests']==len(REQUIRED_MODULES)+1
