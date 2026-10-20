"""Daily launcher exercised as a real process, with real Docker and HTTP."""
import json
import os
from pathlib import Path
import queue
import shutil
import socket
import subprocess
import sys
import threading
from types import SimpleNamespace

import httpx2 as httpx
from playwright.sync_api import sync_playwright, expect

from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_t09_service import image, response
from tests.test_u1_web import request, wait_done
from tests.test_u2_browser import open_browser


ROOT = Path(__file__).resolve().parents[1]


def test_first_configuration_and_restart_from_other_directory(tmp_path, image):
    project = tmp_path / 'project with spaces'
    project.mkdir()
    shutil.copyfile(ROOT / 'start.py', project / 'start.py')
    snapshot = build_snapshot(project / 'data', scenario='normal', seed=451001)
    with socket.socket() as sock:
        sock.bind(('127.0.0.1', 0))
        port = sock.getsockname()[1]
    original = snapshot.database.read_bytes()
    records = {}
    for restart in range(3):
        if restart == 2:
            with socket.socket() as sock:
                sock.bind(('127.0.0.1', 0))
                port = sock.getsockname()[1]
        child = subprocess.Popen(
            [sys.executable, str(ROOT/'tests/daily_start_worker.py'), str(project/'start.py'),
             *(['--configure'] if restart == 2 else [])],
            cwd=tmp_path if restart else project, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True, encoding='utf-8',
            env={**os.environ, 'PYTHONUTF8':'1', 'PYTHONPATH':str(ROOT),
                 'ANTHROPIC_AUTH_TOKEN':'daily-sentinel-never-send'},
        )
        lines = queue.Queue()
        def read():
            for line in child.stdout:
                lines.put(line)
            lines.put(None)
        reader = threading.Thread(target=read, daemon=True)
        reader.start()
        output = []
        try:
            if not restart:
                child.stdin.write('\n'.join(['new','state','existing','dev=data/public/snapshot.duckdb',
                                            '',image,str(port),'http://127.0.0.1:1','yes'])+'\n')
                child.stdin.flush()
            elif restart == 2:
                child.stdin.write('\n'.join(['','','existing','','',str(port),'','yes'])+'\n')
                child.stdin.flush()
            while True:
                line = lines.get(timeout=90)
                assert line is not None, ''.join(output)
                output.append(line)
                if 'BROWSER_READY ' in line:
                    ready = json.loads(line.split('BROWSER_READY ',1)[1])
                    assert ready['status'] == 200
                    assert {task['id'] for task in ready['tasks']} == set(records)
                    assert ready['origin'] == f'http://127.0.0.1:{port}'
                    break
            app = SimpleNamespace(**ready)
            for task, record in records.items():
                assert request(app, '/api/tasks/'+task)[1] == record
            with sync_playwright() as pw:
                browser = open_browser(pw)
                try:
                    page = browser.new_page()
                    page.goto(app.origin)
                    assert page.locator('#snapshot option').all_text_contents() == ['dev']
                    if not restart:
                        page.get_by_label('分析问题').fill('用户表现怎么样？')
                        page.get_by_role('button', name='开始分析', exact=True).click()
                        expect(page.locator('#status')).to_have_text('等待澄清')
                        task = page.url.split('task=')[1]
                        records[task] = request(app, '/api/tasks/'+task)[1]
                finally:
                    browser.close()
            child.stdin.write('stop\n'); child.stdin.flush()
            assert child.wait(timeout=15) == 0
            reader.join(timeout=5)
            config = json.loads((project/'.metricguard-local.json').read_text(encoding='utf-8'))
            assert config['state_dir'] == str(project/'state')
            assert config['snapshots'] == {'dev':str(snapshot.database)}
            assert config['image'] == image and config['port'] == port
            assert 'daily-sentinel' not in json.dumps(config)
            assert 'daily-sentinel' not in ''.join(output)
            if restart:
                assert '首次配置' not in ''.join(output)
            if restart == 2:
                assert '修改前' in ''.join(output) and '旧页面' in ''.join(output)
            assert snapshot.database.read_bytes() == original
            if not restart:
                # Prepare a completed public record using a controlled provider;
                # neither subsequent startup nor read-only browser may call it.
                calls = []
                def provider(req):
                    calls.append(req)
                    return response({'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'}
                                    if len(calls) == 1 else
                                    {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]})
                with TaskService(project/'state', image, {'dev':snapshot.database},
                                 token='controlled', transport=httpx.MockTransport(provider)) as service:
                    with LocalWeb(service) as app:
                        _, created = request(app, '/api/tasks', {'request_id':'daily-ended',
                            'question':'查询新增用户数','snapshot_id':'dev',
                            'window':['2026-01-08','2026-01-15']})
                        record = wait_done(app, created['id'])
                        assert record['status'] == 'ended'
                        records[created['id']] = record
                        assert len(calls) == 2
        finally:
            if child.poll() is None:
                child.kill()
            child.communicate(timeout=10)
