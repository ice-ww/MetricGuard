"""Real service remains usable when the operating-system browser launch fails."""
import json
import os
import shutil
import socket
import subprocess
import sys
import queue
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from types import SimpleNamespace
from urllib.request import urlopen

from experiments.t01.snapshots import build_snapshot
from tests.test_daily_config import ROOT, project, run
from tests.test_t09_service import image, response
from metricguard import TaskService
from tests.test_u1_web import request


def test_browser_failure_does_not_stop_service(tmp_path, image):
    config = project(tmp_path,image)
    snapshot = build_snapshot(tmp_path/'data',scenario='normal',seed=491001)
    config['snapshots'] = {'dev':str(snapshot.database)}
    with socket.socket() as sock:
        sock.bind(('127.0.0.1',0))
        config['port'] = sock.getsockname()[1]
    (tmp_path/'.metricguard-local.json').write_text(json.dumps(config),encoding='utf-8')
    script = """import os,runpy,sys,webbrowser
target=sys.argv[1]
runpy.run_path(sys.argv[2],run_name='worker_setup')
real=webbrowser.open
def failure(origin):
    real(origin)
    raise OSError('controlled browser launch failure')
webbrowser.open=failure
sys.argv=[target]
runpy.run_path(target,run_name='__main__')
"""
    # The worker's browser callback probes actual HTTP and arranges graceful stop.
    child = subprocess.Popen([sys.executable,'-c',script,str(tmp_path/'start.py'),
                             str(ROOT/'tests/daily_start_worker.py')],
        env={**os.environ,'PYTHONUTF8':'1','PYTHONPATH':str(ROOT),'ANTHROPIC_AUTH_TOKEN':'lifecycle-sentinel'},
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='utf-8')
    lines = queue.Queue()
    def read():
        for line in child.stdout:
            lines.put(line)
        lines.put(None)
    threading.Thread(target=read,daemon=True).start()
    output = []
    try:
        while True:
            line = lines.get(timeout=90)
            assert line is not None, ''.join(output)
            output.append(line)
            if '浏览器未能打开' in line:
                break
        assert child.poll() is None
        child.stdin.write('stop\n');child.stdin.flush()
        assert child.wait(timeout=15) == 0
        assert '服务仍在运行' in ''.join(output) and 'BROWSER_READY' in ''.join(output)
    finally:
        if child.poll() is None:
            child.kill()
        child.communicate(timeout=10)


def test_port_and_directory_failures_are_distinct(tmp_path, image):
    config = project(tmp_path,image)
    snapshot = build_snapshot(tmp_path/'data',scenario='normal',seed=491002)
    config['snapshots'] = {'dev':str(snapshot.database)}
    path = tmp_path/'.metricguard-local.json'
    with socket.socket() as occupied:
        occupied.bind(('127.0.0.1',0));occupied.listen()
        config['port'] = occupied.getsockname()[1]
        path.write_text(json.dumps(config),encoding='utf-8')
        result = run(tmp_path,'')
        assert result.returncode != 0 and '端口：需要处理' in result.stdout
        assert '不会自动换端口或结束进程' in result.stdout
        assert occupied.getsockname()[1] == config['port']
    with socket.socket() as available:
        available.bind(('127.0.0.1',0))
        config['port'] = available.getsockname()[1]
    path.write_text(json.dumps(config),encoding='utf-8')
    with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='controlled') as owner:
        before = owner.create('用户表现怎么样？','dev')
        result = run(tmp_path,'')
        assert result.returncode != 0 and '任务目录已被其他进程占用' in result.stderr
        assert owner.inspect(before)['id'] == before
    blocked = tmp_path/'not-a-directory'
    blocked.write_text('preserve',encoding='utf-8')
    config['state_dir'] = str(blocked)
    path.write_text(json.dumps(config),encoding='utf-8')
    result = run(tmp_path,'')
    assert result.returncode != 0 and '目录不可写或不是目录' in result.stdout
    assert blocked.read_text(encoding='utf-8') == 'preserve'


def test_real_console_ctrl_c_waits_for_accepted_execution(tmp_path, image):
    config = project(tmp_path,image)
    snapshot = build_snapshot(tmp_path/'data',scenario='normal',seed=491003)
    config['snapshots'] = {'dev':str(snapshot.database)}
    with socket.socket() as available:
        available.bind(('127.0.0.1',0))
        config['port'] = available.getsockname()[1]
    entered, release = tmp_path/'entered', tmp_path/'release'
    calls = []
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass
        def do_POST(self):
            self.rfile.read(int(self.headers['Content-Length']))
            calls.append(self.path)
            if len(calls) == 1:
                entered.touch()
                deadline = time.monotonic()+45
                while not release.exists() and time.monotonic()<deadline:
                    time.sleep(.05)
                body = response({'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'}).content
            else:
                body = response({'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]}).content
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.send_header('Content-Length',str(len(body)))
            self.end_headers()
            self.wfile.write(body)
    provider = ThreadingHTTPServer(('127.0.0.1',0),Handler)
    threading.Thread(target=provider.serve_forever,daemon=True).start()
    config['base_url'] = f'http://127.0.0.1:{provider.server_port}'
    (tmp_path/'.metricguard-local.json').write_text(json.dumps(config),encoding='utf-8')
    payload = {'command':[sys.executable,str(ROOT/'tests/daily_start_worker.py'),str(tmp_path/'start.py')],
               'operations':[{'wait':'BROWSER_READY'},
                             {'wait_file':str(entered),'interrupt':True},
                             {'wait':'正在停止服务','touch':str(release)}]}
    controller = subprocess.Popen([sys.executable,str(ROOT/'tests/terminal_driver.py')],
        stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8',
        env={**os.environ,'PYTHONUTF8':'1','PYTHONPATH':str(ROOT),'ANTHROPIC_AUTH_TOKEN':'stop-sentinel'})
    controller.stdin.write(json.dumps(payload));controller.stdin.close();controller.stdin=None
    try:
        origin = f"http://127.0.0.1:{config['port']}"
        deadline = time.monotonic()+60
        while True:
            try:
                with urlopen(origin+'/api/config',timeout=1) as result:
                    token = json.load(result)['token']
                break
            except OSError:
                assert time.monotonic()<deadline
                time.sleep(.1)
        assert calls == []
        _, created = request(SimpleNamespace(origin=origin,token=token),'/api/tasks',
            {'request_id':'console-stop','question':'查询新增用户数','snapshot_id':'dev',
             'window':['2026-01-08','2026-01-15']})
        out, err = controller.communicate(timeout=90)
        assert controller.returncode == 0, out+err
        terminal = json.loads(out)
        assert terminal['code'] == 0, terminal['screen']
        assert '正在停止服务' in terminal['screen'] and release.exists()
        assert len(calls) == 2
        with TaskService(tmp_path/'state',image,{'dev':snapshot.database},token='unused') as service:
            task = service.inspect(created['id'])
            assert task['status'] == 'ended' and task['model_calls'] == 2
    finally:
        release.touch()
        if controller.poll() is None:
            controller.kill()
        controller.communicate(timeout=10)
        provider.shutdown()
        provider.server_close()


if os.name == 'nt':
    def test_windows_cmd_preserves_failed_exit_after_keypress(tmp_path):
        shutil.copyfile(ROOT/'start.py',tmp_path/'start.py')
        shutil.copyfile(ROOT/'start.cmd',tmp_path/'start.cmd')
        (tmp_path/'.venv/Scripts').mkdir(parents=True)
        shutil.copyfile(sys.executable,tmp_path/'.venv/Scripts/python.exe')
        shutil.copyfile(ROOT/'.venv/pyvenv.cfg',tmp_path/'.venv/pyvenv.cfg')
        payload = {'command':[os.environ['COMSPEC'],'/d','/c',str(tmp_path/'start.cmd')],
                   'operations':[{'wait':'. . .','hold':.3,'write':'\n'}]}
        result = subprocess.run([sys.executable,str(ROOT/'tests/terminal_driver.py')],
            input=json.dumps(payload),env={**os.environ,'PYTHONUTF8':'1','PYTHONPATH':str(ROOT)},
            capture_output=True,text=True,encoding='utf-8',timeout=60)
        assert result.returncode == 0, result.stdout+result.stderr
        terminal = json.loads(result.stdout)
        assert terminal['code'] == 1
        assert '项目解释器' in terminal['screen']

