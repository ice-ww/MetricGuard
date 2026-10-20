"""Missing tools and timeout diagnostics at the OS process boundary."""
import os
import subprocess
import sys
import pytest
from pathlib import Path
import shutil
import json

from tests.test_daily_config import ROOT, project


def test_missing_tools_are_reported_together_without_cascading_failures(tmp_path):
    project(tmp_path, 'sha256:'+'a'*64)
    result = subprocess.run([sys.executable,str(tmp_path/'start.py')],
        env={**os.environ,'PATH':str(tmp_path),'PYTHONUTF8':'1','PYTHONPATH':str(ROOT),
             'ANTHROPIC_AUTH_TOKEN':'checks-sentinel'},capture_output=True,
        text=True,encoding='utf-8',timeout=30)
    assert result.returncode != 0
    assert 'uv：需要处理' in result.stdout
    assert 'Docker CLI：需要处理' in result.stdout
    assert 'Docker 引擎：暂未检查' in result.stdout
    assert '项目依赖：暂未检查' in result.stdout
    assert 'checks-sentinel' not in result.stdout+result.stderr


def test_other_interpreter_is_rejected_before_business_import(tmp_path):
    shutil.copyfile(ROOT/'start.py',tmp_path/'start.py')
    interpreter = Path(sys.base_prefix)/('python.exe' if os.name=='nt' else 'bin/python3')
    result = subprocess.run([str(interpreter),str(tmp_path/'start.py')],
        env={**os.environ,'PYTHONUTF8':'1','PYTHONPATH':str(ROOT)},
        capture_output=True,text=True,encoding='utf-8',timeout=45)
    assert result.returncode != 0
    assert '项目解释器' in result.stdout
    assert 'Traceback' not in result.stderr


def test_first_configuration_reports_missing_docker_before_image_prompt(tmp_path):
    shutil.copyfile(ROOT/'start.py',tmp_path/'start.py')
    script = """import runpy,shutil,sys
real=shutil.which
shutil.which=lambda name,*args,**kwargs: None if name=='docker' else real(name,*args,**kwargs)
target=sys.argv[1];sys.argv=[target];runpy.run_path(target,run_name='__main__')
"""
    result = subprocess.run([sys.executable,'-c',script,str(tmp_path/'start.py')],input='',
        env={**os.environ,'PYTHONUTF8':'1','PYTHONPATH':str(ROOT)},capture_output=True,
        text=True,encoding='utf-8',timeout=45)
    assert result.returncode != 0
    assert 'Docker CLI：需要处理' in result.stdout
    assert 'Docker 引擎：暂未检查' in result.stdout
    assert '固定镜像与隔离查询：暂未检查' in result.stdout
    assert not (tmp_path/'.metricguard-local.json').exists()


@pytest.mark.parametrize('fault,expected', [
    ('dependencies', ('项目依赖：需要处理','固定镜像与隔离查询：暂未检查','uv sync --locked')),
    ('timeout', ('检查超时（10 秒）','Docker 引擎：需要处理','固定镜像：暂未检查','快照 dev：需要处理')),
    ('windows', ('Linux 容器模式','固定镜像：暂未检查','快照 dev：需要处理')),
    ('image', ('固定镜像：需要处理','--configure','隔离查询 dev：暂未检查')),
])
def test_boundary_failures_are_actionable_and_block_dependent_checks(tmp_path, fault, expected):
    project(tmp_path, 'sha256:'+'a'*64)
    script = """import runpy,subprocess,sys
real = subprocess.run
fault = sys.argv[2]
def run(args, **kwargs):
    if args[0]=='uv' and fault=='dependencies':
        assert kwargs['timeout']==15
        return subprocess.CompletedProcess(args,1,'','controlled missing dependencies')
    if args[:2]==['docker','info']:
        assert kwargs['timeout']==10
        if fault=='timeout': raise subprocess.TimeoutExpired(args,10)
        return subprocess.CompletedProcess(args,0,'windows' if fault=='windows' else 'linux','')
    if args[:3]==['docker','image','inspect'] and fault=='image':
        return subprocess.CompletedProcess(args,1,'','missing')
    return real(args,**kwargs)
subprocess.run=run
target=sys.argv[1];sys.argv=[target]
if fault=='dependencies':sys.modules['metricguard']=None
runpy.run_path(target,run_name='__main__')
"""
    result = subprocess.run([sys.executable,'-c',script,str(tmp_path/'start.py'),fault],
        env={**os.environ,'PYTHONUTF8':'1','PYTHONPATH':str(ROOT),'ANTHROPIC_AUTH_TOKEN':'checks-sentinel'},
        capture_output=True,text=True,encoding='utf-8',timeout=45)
    assert result.returncode != 0
    for text in expected:
        assert text in result.stdout, result.stdout+result.stderr
    assert 'Traceback' not in result.stderr
    assert 'checks-sentinel' not in result.stdout+result.stderr


if os.name == 'nt':
    def test_windows_launcher_explains_missing_python_environment_and_waits(tmp_path):
        shutil.copyfile(ROOT/'start.cmd',tmp_path/'start.cmd')
        payload = {'command':[os.environ['COMSPEC'],'/d','/c',str(tmp_path/'start.cmd')],
                   'operations':[{'wait':'. . .','write':'\n'}]}
        result = subprocess.run([sys.executable,str(ROOT/'tests/terminal_driver.py')],
            input=json.dumps(payload),env={**os.environ,'PYTHONUTF8':'1'},
            capture_output=True,text=True,encoding='utf-8',timeout=45)
        assert result.returncode == 0, result.stdout+result.stderr
        terminal = json.loads(result.stdout)
        assert terminal['code'] == 1
        assert 'Python/project environment missing' in terminal['screen']
        assert 'uv sync --locked --python 3.12' in terminal['screen']
