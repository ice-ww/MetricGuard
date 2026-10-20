"""Hidden credentials verified in a real Windows console / Linux PTY."""
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import pytest

from experiments.t01.snapshots import build_snapshot
from tests.test_t09_service import image

ROOT = Path(__file__).resolve().parents[1]
SENTINEL = 'terminal-secret-must-not-echo-471'


@pytest.fixture
def provider():
    calls = []
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass
        def do_POST(self):
            calls.append(self.path)
            self.send_response(500)
            self.send_header('Content-Length','0')
            self.end_headers()
        do_GET = do_POST
    server = ThreadingHTTPServer(('127.0.0.1',0),Handler)
    thread = threading.Thread(target=server.serve_forever,daemon=True)
    thread.start()
    try:
        yield f'http://127.0.0.1:{server.server_port}',calls
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def terminal(root, operations, token=''):
    command = [sys.executable,str(ROOT/'tests/daily_start_worker.py'),str(root/'start.py')]
    result = subprocess.run([sys.executable,str(ROOT/'tests/terminal_driver.py')],
        input=json.dumps({'command':command,'operations':operations}),
        env={**os.environ,'PYTHONUTF8':'1','PYTHONPATH':str(ROOT),'ANTHROPIC_AUTH_TOKEN':token},
        capture_output=True, text=True, encoding='utf-8', timeout=140)
    assert result.returncode == 0, result.stdout+result.stderr
    value = json.loads(result.stdout)
    assert SENTINEL not in value['screen']
    return value


def test_hidden_credential_is_single_use_and_environment_has_priority(tmp_path, image, provider):
    shutil.copyfile(ROOT/'start.py',tmp_path/'start.py')
    snapshot = build_snapshot(tmp_path/'data',scenario='normal',seed=471001)
    with socket.socket() as sock:
        sock.bind(('127.0.0.1',0))
        port = sock.getsockname()[1]
    config = tmp_path/'.metricguard-local.json'
    config.write_text(json.dumps({'state_dir':str(tmp_path/'state'),'snapshots':{'dev':str(snapshot.database)},
        'image':image,'port':port,'base_url':provider[0]}),encoding='utf-8')
    before = config.read_bytes()
    for _ in range(2):
        result = terminal(tmp_path,[{'wait':'隐藏输入','write':SENTINEL+'\n'},
                                   {'wait':'BROWSER_READY','write':'stop\n'}])
        assert result['code'] == 0
        assert '未验证提供方' in result['screen']
        assert config.read_bytes() == before
    inherited = terminal(tmp_path,[{'wait':'BROWSER_READY','write':'stop\n'}],token=SENTINEL)
    assert inherited['code'] == 0 and '隐藏输入' not in inherited['screen']
    for value in ('\n','\x03'):
        cancelled = terminal(tmp_path,[{'wait':'隐藏输入','write':value}])
        assert cancelled['code'] != 0 and 'BROWSER_READY' not in cancelled['screen']
    assert config.read_bytes() == before
    assert provider[1] == []
    for path in (tmp_path/'state').rglob('*'):
        if path.is_file():
            assert SENTINEL.encode() not in path.read_bytes()
