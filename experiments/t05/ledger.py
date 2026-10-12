"""Durable application-owned attempt accounting; no graph state is authoritative."""
import json
import math
import sqlite3
import time
import uuid
from pathlib import Path
from typing import Any
from collections.abc import Iterator
from contextlib import contextmanager

DEFAULT_LIMITS = {'tool': 12, 'model': 10, 'tokens': 30000, 'active_seconds': 180}

class Ledger:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.active_segments: dict[str, float] = {}
        with self.connect() as db:
            db.executescript('''
            CREATE TABLE IF NOT EXISTS tasks(id TEXT PRIMARY KEY, status TEXT, rounds INTEGER, version INTEGER,
              question TEXT, active REAL, limits TEXT, parent TEXT);
            CREATE TABLE IF NOT EXISTS attempts(id TEXT PRIMARY KEY, task TEXT, operation TEXT, kind TEXT,
              reserved INTEGER, actual INTEGER, state TEXT, result TEXT);
            CREATE TABLE IF NOT EXISTS trace(seq INTEGER PRIMARY KEY, task TEXT, event TEXT, detail TEXT);
            ''')

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def create_task(self, task_id: str | None = None, limits: dict[str, Any] | None = None,
                    parent: str | None = None) -> str:
        task_id = task_id or uuid.uuid4().hex
        policy = dict(DEFAULT_LIMITS)
        policy.update(limits or {})
        if set(policy) != set(DEFAULT_LIMITS) or any(type(policy[k]) is not int or policy[k] <= 0 for k in ('tool', 'model', 'tokens')):
            raise ValueError('invalid limits')
        active = policy['active_seconds']
        if type(active) not in (int, float) or not math.isfinite(active) or active <= 0:
            raise ValueError('invalid limits')
        with self.connect() as db:
            db.execute('INSERT INTO tasks VALUES(?, ?, 0, 0, NULL, 0, ?, ?)',
                       (task_id, 'created', json.dumps(policy), parent))
        return task_id

    def reserve(self, task_id: str, operation_id: str, kind: str, reserved_tokens: int = 0,
                attempt_id: str | None = None, headroom_tokens: int = 0,
                headroom_calls: int = 0) -> dict[str, Any]:
        if kind not in ('tool', 'model') or any(type(v) is not int or v < 0 for v in (reserved_tokens, headroom_tokens, headroom_calls)):
            raise ValueError('invalid reservation')
        attempt_id = attempt_id or uuid.uuid4().hex
        self.accrue_activity(task_id)
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            old = db.execute('SELECT * FROM attempts WHERE id=?', (attempt_id,)).fetchone()
            if old:
                if (old['task'], old['operation'], old['kind'], old['reserved']) != (task_id, operation_id, kind, reserved_tokens):
                    raise ValueError('attempt identity conflict')
                return dict(old, attempt_id=old['id'])
            task = db.execute('SELECT * FROM tasks WHERE id=?', (task_id,)).fetchone()
            if task is None or task['status'] not in ('created', 'running'):
                raise ValueError('task cannot dispatch')
            limits = json.loads(task['limits'])
            unknown = db.execute("SELECT COUNT(*) FROM attempts WHERE task=? AND kind='model' AND actual IS NULL", (task_id,)).fetchone()[0]
            if unknown:
                raise ValueError('budget blocked by unknown model usage')
            count = db.execute('SELECT COUNT(*) FROM attempts WHERE task=? AND kind=?', (task_id, kind)).fetchone()[0]
            tokens = db.execute('SELECT COALESCE(SUM(COALESCE(actual,reserved)),0) FROM attempts WHERE task=?', (task_id,)).fetchone()[0]
            if count + 1 + headroom_calls > limits[kind] or tokens + reserved_tokens + headroom_tokens > limits['tokens'] or task['active'] >= limits['active_seconds']:
                raise ValueError('budget exhausted')
            db.execute('INSERT INTO attempts VALUES(?,?,?,?,?,NULL,?,NULL)',
                       (attempt_id, task_id, operation_id, kind, reserved_tokens, 'reserved'))
            db.execute('INSERT INTO trace(task,event,detail) VALUES(?,?,?)', (task_id, 'reserve', attempt_id))
            return dict(db.execute('SELECT * FROM attempts WHERE id=?', (attempt_id,)).fetchone(), attempt_id=attempt_id)

    def start_activity(self, task_id: str) -> None:
        if task_id in self.active_segments:
            raise ValueError('activity already running')
        self.active_segments[task_id] = time.monotonic()

    def accrue_activity(self, task_id: str, stop: bool = False) -> None:
        previous = self.active_segments.get(task_id)
        if previous is None:
            return
        current = time.monotonic()
        with self.connect() as db:
            db.execute('UPDATE tasks SET active=active+? WHERE id=?', (current - previous, task_id))
        if stop:
            del self.active_segments[task_id]
        else:
            self.active_segments[task_id] = current

    def mark_sent(self, attempt_id: str) -> None:
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            row = db.execute('SELECT * FROM attempts WHERE id=?', (attempt_id,)).fetchone()
            if row is None or row['state'] != 'reserved':
                raise ValueError('attempt must be fresh reservation')
            db.execute("UPDATE attempts SET state='sent' WHERE id=?", (attempt_id,))
            db.execute('INSERT INTO trace(task,event,detail) VALUES(?,?,?)', (row['task'], 'sent', attempt_id))

    def settle(self, attempt_id: str, result: Any, actual_tokens: int | None = None, failed: bool = False) -> None:
        if actual_tokens is not None and (type(actual_tokens) is not int or actual_tokens < 0):
            raise ValueError('invalid usage')
        encoded = json.dumps(result, sort_keys=True)
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            row = db.execute('SELECT * FROM attempts WHERE id=?', (attempt_id,)).fetchone()
            if row is None or row['state'] != 'sent':
                raise ValueError('only sent attempt can settle')
            state = 'failed' if failed else 'completed'
            db.execute('UPDATE attempts SET actual=?,state=?,result=? WHERE id=?', (actual_tokens, state, encoded, attempt_id))
            db.execute('INSERT INTO trace(task,event,detail) VALUES(?,?,?)', (row['task'], state, attempt_id))

    def inspect(self, task_id: str) -> dict[str, Any]:
        with self.connect() as db:
            task = db.execute('SELECT * FROM tasks WHERE id=?', (task_id,)).fetchone()
            if task is None:
                raise ValueError('unknown task')
            attempts = [dict(r) for r in db.execute('SELECT * FROM attempts WHERE task=? ORDER BY rowid', (task_id,))]
            return dict(task, limits=json.loads(task['limits']), attempts=attempts,
                        tool_calls=sum(r['kind'] == 'tool' for r in attempts),
                        model_calls=sum(r['kind'] == 'model' for r in attempts),
                        tokens=sum(r['reserved'] if r['actual'] is None else r['actual'] for r in attempts),
                        trace=[dict(r) for r in db.execute('SELECT * FROM trace WHERE task=? ORDER BY seq', (task_id,))])
