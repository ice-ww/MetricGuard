"""Explicit image update uses a second real, compatible isolated worker."""
import json
import os
import socket
import subprocess
import sys
import uuid

from experiments.t01.snapshots import build_snapshot
from tests.test_daily_config import ROOT, project, run
from tests.test_t09_service import image


def test_confirmed_image_update_and_later_tag_change(tmp_path, image):
    config = project(tmp_path,image)
    snapshot = build_snapshot(tmp_path/'data',scenario='normal',seed=501001)
    config['snapshots'] = {'dev':str(snapshot.database)}
    with socket.socket() as sock:
        sock.bind(('127.0.0.1',0))
        config['port'] = sock.getsockname()[1]
    path = tmp_path/'.metricguard-local.json'
    path.write_text(json.dumps(config),encoding='utf-8')
    before, data = path.read_bytes(), snapshot.database.read_bytes()
    suffix = uuid.uuid4().hex
    updated = 'metricguard-update:'+suffix
    second = None
    def docker(*args):
        return subprocess.run(['docker',*args],capture_output=True,text=True,encoding='utf-8',timeout=90,check=True).stdout.strip()
    try:
        container = docker('create',image)
        try:
            second = docker('commit','--change','LABEL metricguard.startup.validation='+suffix,container)
        finally:
            docker('rm',container)
        docker('tag',second,updated)
        assert second != image
        answers = ['','','existing','',updated,'','']
        cancelled = run(tmp_path,'\n'.join([*answers,'no'])+'\n','--configure')
        assert cancelled.returncode == 0 and path.read_bytes() == before
        for arguments, text in ((['--configure'],'\n'.join([*answers,'yes','stop'])+'\n'),([], 'stop\n')):
            result = subprocess.run([sys.executable,str(ROOT/'tests/daily_start_worker.py'),
                                     str(tmp_path/'start.py'),*arguments],input=text,
                env={**os.environ,'PYTHONUTF8':'1','PYTHONPATH':str(ROOT),'ANTHROPIC_AUTH_TOKEN':'image-update-sentinel'},
                capture_output=True,text=True,encoding='utf-8',timeout=90)
            assert result.returncode == 0 and 'BROWSER_READY' in result.stdout, result.stdout+result.stderr
            assert json.loads(path.read_text(encoding='utf-8'))['image'] == second
            assert snapshot.database.read_bytes() == data
            docker('tag',image,updated)  # A mutable label now points back to the old image.
    finally:
        if second:
            # The alias may currently name the shared image. Move it back to
            # our owned image before deleting, without pruning its parent.
            docker('tag',second,updated)
            docker('image','rm','--no-prune',updated)
        docker('image','inspect',image)
