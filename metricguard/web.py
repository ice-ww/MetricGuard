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
            db.execute('CREATE TABLE IF NOT EXISTS answers (key TEXT PRIMARY KEY, payload TEXT NOT NULL, task TEXT NOT NULL, finished INTEGER NOT NULL DEFAULT 0)')
            # The previous owner is gone. Reconcile durable admissions without replay.
            for row in db.execute('SELECT task FROM operations WHERE task IS NOT NULL AND finished IS NULL UNION SELECT task FROM answers WHERE finished<=0'):
                failed = db.execute('SELECT 1 FROM answers WHERE task=? AND finished=-1', (row['task'],)).fetchone()
                service.record_execution_stop(row['task'], failed=bool(failed))
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
                self.unread_body = 0
                try:
                    length = int(self.headers.get('Content-Length', '0'))
                    if self.command == 'POST' and 0 < length <= 16384:
                        self.unread_body = length
                except ValueError:
                    pass
                try:
                    app.check_request(self)
                    status, content, mime = app.dispatch(self)
                except WebError as error:
                    status, content, mime = error.status, {'error': error.message}, 'application/json'
                except Exception:
                    status, content, mime = 500, {'error': '本地服务处理失败；任务记录已保留，请检查服务后重新打开任务。'}, 'application/json'
                # Closing with an unread POST body can reset the connection on Windows,
                # losing the intended rejection response. Drain only bounded bodies,
                # with a total deadline, and never parse or execute rejected content.
                deadline = time.monotonic() + 1
                try:
                    while self.unread_body and time.monotonic() < deadline:
                        self.connection.settimeout(max(.001, deadline - time.monotonic()))
                        chunk = self.rfile.read1(self.unread_body)
                        if not chunk:
                            break
                        self.unread_body -= len(chunk)
                except OSError:
                    pass
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
                except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
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
            assets = {'/': ('index.html','text/html'), '/app.js': ('app.js','text/javascript'), '/app.css': ('app.css','text/css'), '/report.js': ('report.js','text/javascript'), '/drafts.js': ('drafts.js','text/javascript')}
            if path in assets:
                name, mime = assets[path]
                return 200, (Path(__file__).parent/'web_assets'/name).read_bytes(), mime
            if path == '/api/config':
                return 200, {'token': self.token, 'snapshots': list(self.service.snapshots), 'example': self.example}, 'application/json'
        if not secrets.compare_digest(handler.headers.get('X-MetricGuard-Token',''), self.token):
            raise WebError(403, '页面会话已失效，请刷新页面。')
        if handler.command == 'POST' and (path == '/api/tasks' or re.fullmatch(r'/api/tasks/[a-f0-9]{32}/(answers|rerun)', path)):
            try:
                length = int(handler.headers.get('Content-Length', '0'))
                if not 0 < length <= 16384 or handler.headers.get_content_type() != 'application/json':
                    raise ValueError()
                handler.connection.settimeout(5)
                setattr(handler, 'unread_body', 0)
                payload = json.loads(handler.rfile.read(length))
            except (ValueError, OSError):
                raise WebError(400, '请输入有效的问题、快照和日期。') from None
            if path == '/api/tasks':
                task = self.submit(payload)
            elif path.endswith('/rerun'):
                task = self.submit(payload, parent=path.split('/')[3])
            else:
                task = self.answer(path.split('/')[3], payload)
            return 202, {'id': task}, 'application/json'
        if handler.command == 'GET' and path == '/api/tasks':
            return 200, {'tasks': self.list_tasks()}, 'application/json'
        if handler.command == 'GET' and re.fullmatch(r'/api/tasks/[a-f0-9]{32}/report', path):
            return 200, self.report(path.split('/')[3]), 'application/json'
        if handler.command == 'GET' and re.fullmatch(r'/api/tasks/[a-f0-9]{32}', path):
            return 200, self.inspect(path.rsplit('/',1)[1]), 'application/json'
        raise WebError(404, '找不到此页面或任务。')

    def submit(self, payload: Any, *, parent: str | None = None) -> str:
        if parent:
            if not isinstance(payload, dict) or set(payload) != {'request_id'}:
                raise WebError(400, '重跑只接受操作标识；修改问题请使用复制并修改。')
            previous = self.inspect(parent)
            payload = {**payload, **{key: previous[key] for key in ('question','snapshot_id','window','comparison_window')}}
        if not isinstance(payload, dict) or set(payload)-{'request_id','question','snapshot_id','window','comparison_window'}:
            raise WebError(400, '请求包含不受支持的设置。')
        key = payload.get('request_id')
        if not isinstance(key,str) or not re.fullmatch(r'[a-zA-Z0-9_-]{8,100}', key):
            raise WebError(400, '操作标识无效，请重新打开页面。')
        question = payload.get('question'); snapshot = payload.get('snapshot_id')
        if not isinstance(question,str) or not question.strip() or len(question)>2000 or not isinstance(snapshot,str) or (not parent and snapshot not in self.service.snapshots):
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
        encoded = json.dumps({'request_id': key, 'parent': parent} if parent else payload, sort_keys=True, ensure_ascii=False)
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
                if parent and self.inspect(parent)['status'] not in ('ended','failed','interrupted'):
                    raise WebError(409, '原任务尚未结束；等待澄清时请继续回答原任务。')
                db.execute('INSERT INTO operations(key,payload,started) VALUES(?,?,?)',(key,encoded,time.time()))
            try:
                task = self.service.rerun(parent) if parent else self.service.create(question, snapshot, tuple(payload['window']) if payload.get('window') else None,
                    comparison_window=tuple(payload['comparison_window']) if payload.get('comparison_window') else None, mode='diagnose')
            except Exception:
                # Keep the reservation: an unknown failure must not replay a potentially created task.
                raise WebError(400, '无法创建任务；请检查已配置的快照是否仍然可用，再创建新操作。') from None
            with self.connect() as db:
                db.execute('UPDATE operations SET task=? WHERE key=?',(task,key))
            self.active = task
            self.executor.submit(self.execute, task)
            return task

    def answer(self, task: str, payload: Any) -> str:
        if not isinstance(payload, dict) or set(payload) != {'request_id','question_id','version','answer'}:
            raise WebError(400, '回答格式无效，请刷新后再试。')
        key = payload['request_id']
        if not isinstance(key,str) or not re.fullmatch(r'[a-zA-Z0-9_-]{8,100}',key):
            raise WebError(400, '操作标识无效，请刷新后再试。')
        if not isinstance(payload['question_id'],str) or type(payload['version']) is not int or not isinstance(payload['answer'],str) or not payload['answer'].strip() or len(payload['answer'])>2000:
            raise WebError(400, '请填写不超过 2000 字的回答。')
        encoded = json.dumps(payload,sort_keys=True,ensure_ascii=False)
        with self.lock:
            current = self.inspect(task)
            with self.connect() as db:
                old = db.execute('SELECT * FROM answers WHERE key=?',(key,)).fetchone()
                if old:
                    if old['task'] != task or old['payload'] != encoded:
                        raise WebError(409, '同一回答操作不能更换内容。请重新读取当前问题。')
                    if old['finished'] == -1:
                        raise WebError(409, '上次回答执行失败，记录已保留；不能重放同一操作。')
                    if not old['finished'] and self.active != task:
                        raise WebError(409, '上次回答因服务中断未完成确认，不会自动重放。请保留任务记录。')
                    return task
                if self.closing or self.active is not None:
                    raise WebError(409, '已有任务正在执行；本次回答尚未接受，请稍后重试。')
                pending = current['clarification']
                if current['status'] != 'waiting' or not pending or pending['question_id'] != payload['question_id'] or pending['version'] != payload['version']:
                    raise WebError(409, '待答问题已更新或已处理，请刷新查看最新状态。')
                db.execute('INSERT INTO answers(key,payload,task) VALUES(?,?,?)',(key,encoded,task))
                db.execute('UPDATE operations SET started=?,finished=NULL,body=NULL WHERE task=?',(time.time(),task))
            self.active = task
            self.executor.submit(self.execute,task,payload)
            return task

    def execute(self, task: str, answer: dict[str, Any] | None = None) -> None:
        body = ''
        failed = False
        try:
            state = self.service.answer(task,answer['question_id'],answer['version'],answer['answer']) if answer else self.service.run(task)
            if state['status'] != 'waiting':
                if state['status'] == 'failed':
                    body = '分析未能完成。请检查模型服务和本机查询环境；已获得的记录已保留。'
                else:
                    body = self.service.export_report(task)['terminal_body']
        except Exception:
            failed = True
            self.service.record_execution_stop(task, failed=True)
            body = '任务执行或报告导出失败，记录已保留。请检查本机服务后重新打开任务。'
        finally:
            with self.lock:
                with self.connect() as db:
                    db.execute('UPDATE operations SET finished=?,body=? WHERE task=?',(time.time(),body,task))
                    if answer:
                        db.execute('UPDATE answers SET finished=? WHERE key=?',(-1 if failed else 1,answer['request_id']))
                self.active = None

    def report(self, task: str) -> dict[str, Any]:
        """Read an existing publication through owned task APIs; never publish on GET."""
        from metricguard.web_report import presentation
        with self.lock:
            state = self.inspect(task)  # Enforce Web ownership before reading any evidence.
            data = self.service.inspect(task)
            if state['status'] != 'ended' or not data.get('report'):
                return {'available': False, 'message': state['body'] or '当前任务尚无已发布报告。'}
            revisions = [json.loads(e['detail'])['publication_id'] for e in data['trace'] if e['event']=='report_published']
            if not revisions:
                return {'available': False, 'message': '当前任务尚无已发布报告。'}
            publication = self.service.publication(task, revisions[-1])
            return presentation(data, publication)

    def list_tasks(self) -> list[dict[str, Any]]:
        """Only tasks admitted by this Web owner, newest creation first; never execute."""
        with self.lock:
            with self.connect() as db:
                tasks = [row['task'] for row in db.execute('SELECT task FROM operations WHERE task IS NOT NULL ORDER BY rowid DESC')]
            return [{key: state[key] for key in ('id','question','snapshot_id','status','window')}
                    for state in (self.inspect(task) for task in tasks)]

    def inspect(self, task: str) -> dict[str, Any]:
        # Terminal state and its exported body must be observed together.
        with self.lock:
            with self.connect() as db:
                row = db.execute('SELECT * FROM operations WHERE task=?',(task,)).fetchone()
                unfinished_answer = db.execute('SELECT finished FROM answers WHERE task=? AND finished<=0',(task,)).fetchone()
            if row is None:
                raise WebError(404, '此任务不属于当前界面工作目录。')
            state = self.service.inspect(task)
            active = self.active == task
            status = 'running' if active else state['status']
            # A crash between durable creation and worker admission is not an invitation to replay.
            if not active and (status in ('created','running') or unfinished_answer):
                status = 'failed' if unfinished_answer and unfinished_answer['finished']==-1 else 'interrupted'
            end = row['finished'] if row['finished'] is not None else (time.time() if active else None)
            pending = state.get('pending_question') or {}
            message = ''
            if status == 'interrupted':
                message = '服务意外停止，任务已中断。已有记录和证据保留，未知模型调用不会自动重放。可创建关联新任务重跑；这不是断点续跑。'
            elif status == 'failed':
                message = '任务执行失败，已有记录和证据保留。请检查模型服务和本机环境后创建关联新任务重跑。'
            model_errors = [json.loads(a['result']).get('error_type', '') for a in state['attempts'] if a['kind']=='model' and a.get('result')]
            if not active and any('Timeout' in error for error in model_errors):
                message = '模型请求超时，分析未完成。已有记录和证据保留，未知调用不会自动重放。请检查模型服务后创建关联新任务重跑。'
            elif not active and any(model_errors):
                message = '模型调用失败，分析未完成。已有记录和证据保留。请检查模型服务后创建关联新任务重跑。'
            from metricguard.progress import describe
            from metricguard.budget import describe as describe_budget
            return {'id':task,'parent':state.get('parent'),'question':state['question'],'snapshot_id':state['snapshot_id'],
                    'budget':describe_budget(state),
                    'progress':describe(state, status, self.service.ledger.progress_clock()),
                    'status':status,'elapsed_seconds':max(0,round(end-row['started'],1)) if end is not None else None,
                    'window':state.get('actual_window') or state.get('requested_window'),
                    'window_confirmed': bool(state.get('actual_window')), 'comparison_window': state.get('comparison_window'),
                    'body':row['body'] or '', 'recovery_message':message, 'pending': pending.get('prompt') if status=='waiting' else None,
                    'clarification':{key:pending.get(key) for key in ('question_id','version','known_information','prompt','options')} if status=='waiting' else None,
                    'active_task':self.active}
