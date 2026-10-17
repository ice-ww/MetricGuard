"""Loopback-only task transport. Execution stays in the existing TaskService."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import secrets
import sqlite3
import threading
import time
from typing import Any, Iterator
from urllib.parse import urlsplit

from metricguard import TaskService


class WebError(Exception):
    def __init__(self, status: int, message: str):
        self.status, self.message = status, message


class LocalWeb:
    """One owner and one execution slot; browser disconnects cannot cancel work."""
    def __init__(self, service: TaskService, port: int = 0, *, example: dict[str, Any] | None = None):
        self.service = service
        self.example = example
        self.token = secrets.token_urlsafe(32)
        self.lock = threading.RLock()
        self.active: str | None = None
        self.closing = False
        self.database = service.root / 'web-operations.sqlite'
        with self.connect() as db:
            db.execute('CREATE TABLE IF NOT EXISTS operations (key TEXT PRIMARY KEY, payload TEXT NOT NULL, task TEXT, started REAL NOT NULL, finished REAL, body TEXT)')
        self.executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix='metricguard-task')
        app = self
        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args: Any) -> None:
                pass  # Request paths and user content are not server log messages.

            def do_GET(self) -> None:
                self.respond()

            def do_POST(self) -> None:
                self.respond()

            def respond(self) -> None:
                try:
                    app.check_request(self)
                    status, content, mime = app.dispatch(self)
                except WebError as error:
                    status, content, mime = error.status, {'error': error.message}, 'application/json'
                except Exception:
                    status, content, mime = 500, {'error': '本地服务处理失败；任务记录已保留，请检查服务后重新打开任务。'}, 'application/json'
                encoded = json.dumps(content, ensure_ascii=False).encode() if mime=='application/json' else content
                self.send_response(status)
                self.send_header('Content-Type', mime + '; charset=utf-8')
                self.send_header('Content-Length', str(len(encoded)))
                self.send_header('Cache-Control', 'no-store')
                self.send_header('X-Content-Type-Options', 'nosniff')
                self.send_header('Referrer-Policy', 'no-referrer')
                self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'")
                self.end_headers()
                try:
                    self.wfile.write(encoded)
                except (BrokenPipeError, ConnectionResetError):
                    pass
        self.server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
        self.origin = 'http://127.0.0.1:' + str(self.server.server_port)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        db = sqlite3.connect(self.database, timeout=10)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def __enter__(self) -> LocalWeb:
        self.thread.start()
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def close(self) -> None:
        with self.lock:
            self.closing = True
        if self.thread.is_alive():
            self.server.shutdown()
            self.thread.join()
        self.server.server_close()
        self.executor.shutdown(wait=True)

    def check_request(self, handler: BaseHTTPRequestHandler) -> None:
        if handler.headers.get('Host') != self.origin.removeprefix('http://'):
            raise WebError(403, '仅允许使用启动时显示的本机地址。')
        origin = handler.headers.get('Origin')
        if origin and origin != self.origin:
            raise WebError(403, '请求来源不受允许。')
        if handler.headers.get('Sec-Fetch-Site') == 'cross-site':
            raise WebError(403, '请求来源不受允许。')

    def dispatch(self, handler: BaseHTTPRequestHandler) -> tuple[int, Any, str]:
        path = urlsplit(handler.path).path
        if handler.command == 'GET':
            assets = {'/': ('index.html','text/html'), '/app.js': ('app.js','text/javascript'), '/app.css': ('app.css','text/css')}
            if path in assets:
                name, mime = assets[path]
                return 200, (Path(__file__).parent/'web_assets'/name).read_bytes(), mime
            if path == '/api/config':
                return 200, {'token': self.token, 'snapshots': list(self.service.snapshots), 'example': self.example}, 'application/json'
        if not secrets.compare_digest(handler.headers.get('X-MetricGuard-Token',''), self.token):
            raise WebError(403, '页面会话已失效，请刷新页面。')
        if handler.command == 'POST' and path == '/api/tasks':
            try:
                length = int(handler.headers.get('Content-Length', '0'))
                if not 0 < length <= 16384 or handler.headers.get_content_type() != 'application/json':
                    raise ValueError()
                handler.connection.settimeout(5)
                payload = json.loads(handler.rfile.read(length))
            except (ValueError, OSError):
                raise WebError(400, '请输入有效的问题、快照和日期。') from None
            return 202, {'id': self.submit(payload)}, 'application/json'
        if handler.command == 'GET' and re.fullmatch(r'/api/tasks/[a-f0-9]{32}', path):
            return 200, self.inspect(path.rsplit('/',1)[1]), 'application/json'
        raise WebError(404, '找不到此页面或任务。')

    def submit(self, payload: Any) -> str:
        if not isinstance(payload, dict) or set(payload)-{'request_id','question','snapshot_id','window','comparison_window'}:
            raise WebError(400, '请求包含不受支持的设置。')
        key = payload.get('request_id')
        if not isinstance(key,str) or not re.fullmatch(r'[a-zA-Z0-9_-]{8,100}', key):
            raise WebError(400, '操作标识无效，请重新打开页面。')
        question = payload.get('question'); snapshot = payload.get('snapshot_id')
        if not isinstance(question,str) or not question.strip() or len(question)>2000 or not isinstance(snapshot,str) or snapshot not in self.service.snapshots:
            raise WebError(400, '请填写问题并选择已配置的数据快照。')
        from datetime import date
        for name in ('window','comparison_window'):
            value = payload.get(name)
            if value is not None:
                try:
                    if not isinstance(value,list) or len(value)!=2 or not all(isinstance(v,str) for v in value) or date.fromisoformat(value[0])>=date.fromisoformat(value[1]):
                        raise ValueError()
                except ValueError:
                    raise WebError(400, '日期范围无效：结束日期必须晚于开始日期。') from None
        encoded = json.dumps(payload, sort_keys=True, ensure_ascii=False)
        with self.lock:
            with self.connect() as db:
                old = db.execute('SELECT * FROM operations WHERE key=?',(key,)).fetchone()
                if old:
                    if old['payload'] != encoded:
                        raise WebError(409, '同一操作不能提交不同内容，请新建操作。')
                    if old['task']:
                        return str(old['task'])
                    raise WebError(409, '此操作在服务退出前未完成确认；不会自动重放，请创建新操作。')
                if self.closing or self.active is not None:
                    raise WebError(409, '已有任务正在执行，请等待结束或进入等待澄清状态后再提交。')
                db.execute('INSERT INTO operations(key,payload,started) VALUES(?,?,?)',(key,encoded,time.time()))
            try:
                task = self.service.create(question, snapshot, tuple(payload['window']) if payload.get('window') else None,
                    comparison_window=tuple(payload['comparison_window']) if payload.get('comparison_window') else None, mode='diagnose')
            except Exception:
                # Keep the reservation: an unknown failure must not replay a potentially created task.
                raise WebError(400, '无法创建任务；请检查已配置的快照是否仍然可用，再创建新操作。') from None
            with self.connect() as db:
                db.execute('UPDATE operations SET task=? WHERE key=?',(task,key))
            self.active = task
            self.executor.submit(self.execute, task)
            return task

    def execute(self, task: str) -> None:
        body = ''
        try:
            state = self.service.run(task)
            if state['status'] != 'waiting':
                if state['status'] == 'failed':
                    body = '分析未能完成。请检查模型服务和本机查询环境；已获得的记录已保留。'
                else:
                    body = self.service.export_report(task)['terminal_body']
        except Exception:
            body = '任务执行或报告导出失败，记录已保留。请检查本机服务后重新打开任务。'
        finally:
            with self.lock:
                with self.connect() as db:
                    db.execute('UPDATE operations SET finished=?,body=? WHERE task=?',(time.time(),body,task))
                self.active = None

    def inspect(self, task: str) -> dict[str, Any]:
        # Terminal state and its exported body must be observed together.
        with self.lock:
            with self.connect() as db:
                row = db.execute('SELECT * FROM operations WHERE task=?',(task,)).fetchone()
            if row is None:
                raise WebError(404, '此任务不属于当前界面工作目录。')
            state = self.service.inspect(task)
            active = self.active == task
            status = 'running' if active else state['status']
            # A crash between durable creation and worker admission is not an invitation to replay.
            if not active and status in ('created','running'):
                status = 'interrupted'
            end = row['finished'] if row['finished'] is not None else (time.time() if active else None)
            pending = state.get('pending_question') or {}
            return {'id':task,'question':state['question'],'snapshot_id':state['snapshot_id'],
                    'status':status,'elapsed_seconds':max(0,round(end-row['started'],1)) if end is not None else None,
                    'window':state.get('actual_window') or state.get('requested_window'),
                    'window_confirmed': bool(state.get('actual_window')), 'comparison_window': state.get('comparison_window'),
                    'body':row['body'] or '', 'pending': pending.get('prompt') if status=='waiting' else None,
                    'active_task':self.active}
