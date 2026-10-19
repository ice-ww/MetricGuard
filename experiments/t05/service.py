"""Minimal real LangGraph experiment, deliberately not a diagnosis workflow."""
import json
import os
import sys
from pathlib import Path
from typing import Any, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.types import Command, interrupt
from .ledger import Ledger

class State(TypedDict):
    step: int
    questions: int
    answer: str

class TaskService:
    def __init__(self, root: Path, crash_point: str | None = None):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.ledger = Ledger(self.root / 'ledger.sqlite')
        self.crash_point = crash_point
        # Single process owner is enforced by OS file lock, not a stale PID file.
        self.lock = (self.root / 'owner.lock').open('a+b')
        if self.lock.tell() == 0:
            self.lock.write(b'0'); self.lock.flush()
        self.lock.seek(0)
        try:
            if sys.platform == 'win32':
                import msvcrt
                msvcrt.locking(self.lock.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            self.lock.close()
            raise ValueError('service already owned') from None
        with self.ledger.connect() as db:
            running = list(db.execute("SELECT id,limits FROM tasks WHERE status='running'"))
            for row in running:
                # Lost active segment cannot be measured with a dead monotonic clock.
                # Conservatively exhaust time; old task can never resume.
                db.execute("UPDATE tasks SET status='interrupted', active=? WHERE id=?", (json.loads(row['limits'])['active_seconds'], row['id']))
                db.execute("UPDATE attempts SET state='unknown' WHERE task=? AND state IN ('reserved','sent')", (row['id'],))
                db.execute('INSERT INTO trace(task,event,detail) VALUES(?,?,?)', (row['id'], 'interrupted', 'restart; active duration upper bound'))

    def close(self) -> None:
        if not self.lock.closed:
            if sys.platform == 'win32':
                import msvcrt
                self.lock.seek(0); msvcrt.locking(self.lock.fileno(), msvcrt.LK_UNLCK, 1)
            self.lock.close()

    def __enter__(self) -> 'TaskService':
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def create(self, parent: str | None = None) -> str:
        return self.ledger.create_task(parent=parent)

    def inspect(self, task: str) -> dict[str, Any]:
        return self.ledger.inspect(task)

    def rerun(self, task: str) -> str:
        self.inspect(task)
        return self.create(parent=task)

    def fault(self, point: str) -> None:
        if self.crash_point == point:
            os._exit(73)

    def _graph(self, saver: SqliteSaver, task: str) -> Any:
        def call(state: State) -> dict[str, Any]:
            attempt_id = task + ':model:' + str(state['step'])
            attempt = self.ledger.reserve(task, 'step:' + str(state['step']), 'model', 100, attempt_id)
            if attempt['state'] == 'reserved':
                self.fault('after_reserve')
                self.ledger.mark_sent(attempt_id)
                # Provider-side durable marker is independent of application SQLite.
                with (self.root / 'provider.jsonl').open('a', encoding='utf-8') as out:
                    out.write(json.dumps({'task': task, 'attempt': attempt_id}) + '\n')
                    out.flush(); os.fsync(out.fileno())
                self.fault('after_send')
                text = self.model_reply(task, {'text': 'controlled reply'})
                self.ledger.settle(attempt_id, {'text': text}, 30)
                self.fault('after_result')
            elif attempt['state'] != 'completed':
                raise ValueError('uncertain attempt cannot replay')
            self.fault('before_checkpoint')
            return {}

        def prepare(state: State) -> dict[str, Any]:
            self.fault('after_checkpoint')
            return {}

        def wait(state: State) -> dict[str, Any]:
            answer = interrupt({'question_id': task + ':question:' + str(state['step'])})
            return {'step': state['step'] + 1, 'answer': answer}

        graph = StateGraph(State)
        graph.add_node('call', call)
        graph.add_node('prepare', prepare)
        graph.add_node('wait', wait)
        graph.add_edge(START, 'call')
        graph.add_edge('call', 'prepare')
        graph.add_conditional_edges('prepare', lambda s: 'wait' if s['step'] < s['questions'] else END)
        graph.add_edge('wait', 'call')
        return graph.compile(checkpointer=saver)

    def _execute(self, task: str, value: Any) -> dict[str, Any]:
        self.ledger.start_activity(task)
        try:
            with SqliteSaver.from_conn_string(str(self.root / 'checkpoints.sqlite')) as saver:
                graph = self._graph(saver, task)
                graph.invoke(value, {'configurable': {'thread_id': task}}, durability='sync')
                snapshot = graph.get_state({'configurable': {'thread_id': task}})
                pending = bool(snapshot.next)
                step = snapshot.values['step']
            with self.ledger.connect() as db:
                if pending:
                    db.execute("UPDATE tasks SET status='waiting', rounds=rounds+1, version=version+1, question=? WHERE id=?", (task + ':question:' + str(step), task))
                else:
                    db.execute("UPDATE tasks SET status='ended', question=NULL WHERE id=?", (task,))
        except Exception:
            with self.ledger.connect() as db:
                db.execute("UPDATE tasks SET status='failed' WHERE id=?", (task,))
            raise
        finally:
            self.ledger.accrue_activity(task, stop=True)
        return self.inspect(task)

    def run(self, task: str, questions: int = 2) -> dict[str, Any]:
        if type(questions) is not int or not 0 <= questions <= 2:
            raise ValueError('at most two questions')
        with self.ledger.connect() as db:
            cursor = db.execute("UPDATE tasks SET status='running' WHERE id=? AND status='created'", (task,))
            if cursor.rowcount != 1:
                raise ValueError('task cannot run')
        return self._execute(task, {'step': 0, 'questions': questions, 'answer': ''})

    def answer(self, task: str, question: str, version: int, answer: str) -> dict[str, Any]:
        if not isinstance(answer, str) or not answer.strip() or len(answer) > 2000:
            raise ValueError('invalid answer')
        with SqliteSaver.from_conn_string(str(self.root / 'checkpoints.sqlite')) as saver:
            graph = self._graph(saver, task)
            snapshot = graph.get_state({'configurable': {'thread_id': task}})
            if not snapshot.next or 'step' not in snapshot.values or question != task + ':question:' + str(snapshot.values['step']):
                raise ValueError('checkpoint missing or question mismatch')
        with self.ledger.connect() as db:
            cursor = db.execute("UPDATE tasks SET status='running' WHERE id=? AND status='waiting' AND question=? AND version=?", (task, question, version))
            if cursor.rowcount != 1:
                raise ValueError('stale or repeated answer')
        return self._execute(task, Command(resume=answer))

    def model_reply(self, task: str, payload: dict[str, Any]) -> str:
        self.inspect(task)
        if set(payload) != {'text'} or not isinstance(payload['text'], str):
            raise ValueError('model reply allows text only')
        return payload['text']
