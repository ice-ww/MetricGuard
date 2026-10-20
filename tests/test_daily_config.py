"""Configuration decisions through the user-facing terminal entry."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import uuid
import pytest

from tests.test_t09_service import image

ROOT = Path(__file__).resolve().parents[1]


def project(tmp_path, image):
    shutil.copyfile(ROOT/'start.py', tmp_path/'start.py')
    (tmp_path/'state').mkdir()
    config = {'state_dir':str(tmp_path/'state'), 'snapshots':{'dev':str(tmp_path/'data.duckdb')},
              'image':image, 'port':8765, 'base_url':'http://127.0.0.1:1'}
    (tmp_path/'.metricguard-local.json').write_text(json.dumps(config), encoding='utf-8')
    return config


def run(root, answers, *args):
    return subprocess.run([sys.executable,str(root/'start.py'),*args], input=answers,
        cwd=root.parent, env={**os.environ,'PYTHONUTF8':'1','PYTHONPATH':str(ROOT),
                              'ANTHROPIC_AUTH_TOKEN':'configuration-sentinel'},
        capture_output=True, text=True, encoding='utf-8', timeout=60)


def test_cancel_edit_displays_difference_without_replacing_configuration(tmp_path, image):
    original = project(tmp_path, image)
    before = (tmp_path/'.metricguard-local.json').read_bytes()
    result = run(tmp_path, '\n'.join(['','','existing','','','8766','','no'])+'\n', '--configure')
    assert result.returncode == 0, result.stdout+result.stderr
    assert '修改前' in result.stdout and '修改后' in result.stdout
    assert '8766' in result.stdout and '旧页面' in result.stdout
    assert '已取消' in result.stdout
    assert (tmp_path/'.metricguard-local.json').read_bytes() == before
    assert json.loads(before) == original


@pytest.mark.parametrize('broken', ['{', '[]', '{"port":8765}'])
def test_corrupt_configuration_never_falls_back(tmp_path, broken):
    shutil.copyfile(ROOT/'start.py', tmp_path/'start.py')
    config = tmp_path/'.metricguard-local.json'
    config.write_text(broken, encoding='utf-8')
    result = run(tmp_path, '')
    assert result.returncode != 0
    assert '首次配置' not in result.stdout
    assert config.read_text(encoding='utf-8') == broken
    assert not (tmp_path/'state').exists()


def test_failed_atomic_save_keeps_previous_file(tmp_path, image):
    project(tmp_path, image)
    path = tmp_path/'.metricguard-local.json'
    before = path.read_bytes()
    script = """import os,runpy,sys
def fail(*args, **kwargs): raise PermissionError('controlled write denial')
os.replace=fail
target=sys.argv[1]; sys.argv=[target,'--configure']; runpy.run_path(target,run_name='__main__')
"""
    result = subprocess.run([sys.executable,'-c',script,str(tmp_path/'start.py')],
        input='\n'.join(['','','existing','','','8766','','yes'])+'\n',
        env={**os.environ,'PYTHONUTF8':'1','PYTHONPATH':str(ROOT)}, capture_output=True,
        text=True, encoding='utf-8', timeout=60)
    assert result.returncode != 0
    assert path.read_bytes() == before
    assert not list(tmp_path.glob('.metricguard-local.json.*.tmp'))


def test_example_requires_confirmation_and_does_not_overwrite(tmp_path, image):
    shutil.copyfile(ROOT/'start.py', tmp_path/'start.py')
    answers = ['new','state','example',image,'8765','http://127.0.0.1:1']
    cancelled = run(tmp_path, '\n'.join([*answers,'no'])+'\n')
    assert cancelled.returncode == 0, cancelled.stdout+cancelled.stderr
    assert not (tmp_path/'demo-data').exists()
    # Existing unrelated data must not be overwritten even on confirmation.
    (tmp_path/'demo-data').mkdir()
    sentinel = tmp_path/'demo-data/original.txt'
    sentinel.write_text('preserve', encoding='utf-8')
    rejected = run(tmp_path, '\n'.join([*answers,'yes'])+'\n')
    assert rejected.returncode != 0 and '不会覆盖' in rejected.stdout
    assert sentinel.read_text(encoding='utf-8') == 'preserve'
    assert not (tmp_path/'.metricguard-local.json').exists()


def test_confirmed_example_starts_real_service_and_is_reused(tmp_path, image):
    shutil.copyfile(ROOT/'start.py', tmp_path/'start.py')
    import socket
    with socket.socket() as sock:
        sock.bind(('127.0.0.1',0))
        port = sock.getsockname()[1]
    tag = 'metricguard-startup-test:'+uuid.uuid4().hex
    subprocess.run(['docker','tag',image,tag], check=True, capture_output=True, timeout=30)
    first = '\n'.join(['new','state','example',tag,str(port),'http://127.0.0.1:1','yes','stop'])+'\n'
    snapshot = tmp_path/'demo-data/public/snapshot.duckdb'
    before = None
    try:
        for answers in (first, 'stop\n'):
            result = subprocess.run([sys.executable,str(ROOT/'tests/daily_start_worker.py'),str(tmp_path/'start.py')],
                input=answers, env={**os.environ,'PYTHONUTF8':'1','PYTHONPATH':str(ROOT),
                                   'ANTHROPIC_AUTH_TOKEN':'example-sentinel'},
                capture_output=True, text=True, encoding='utf-8', timeout=90)
            assert result.returncode == 0 and 'BROWSER_READY' in result.stdout, result.stdout+result.stderr
            assert 'example-sentinel' not in result.stdout+result.stderr
            assert json.loads((tmp_path/'.metricguard-local.json').read_text(encoding='utf-8'))['image'] == image
            if before is not None:
                assert snapshot.read_bytes() == before
            else:
                # Removing the mutable tag must not affect the saved fixed ID.
                subprocess.run(['docker','image','rm',tag], check=True, capture_output=True, timeout=30)
            before = snapshot.read_bytes()
    finally:
        subprocess.run(['docker','image','rm',tag], capture_output=True, timeout=30)

