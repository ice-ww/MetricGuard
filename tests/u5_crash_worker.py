"""Process-level fault fixture: terminate after one real evidence result."""
import json
import os
from pathlib import Path
import sys
import threading
from datetime import datetime, timezone
import httpx2 as httpx
from metricguard import TaskService
from metricguard.web import LocalWeb
from tests.test_t09_service import response


def main():
    root, database, image = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    calls = 0
    def provider(req):
        nonlocal calls
        calls += 1
        with (root/'provider.jsonl').open('a', encoding='utf-8') as out:
            out.write(json.dumps({'call': calls})+'\n'); out.flush(); os.fsync(out.fileno())
        if calls == 2:
            os._exit(73)
        return response({'action':'profile','table':'users','column':'user_id','kind':'new_user_counts'})
    with TaskService(root/'state', image, {'dev': database}, token='private-u5', transport=httpx.MockTransport(provider),
                     progress_clock=lambda:datetime(2026, 10, 19, 1, tzinfo=timezone.utc)) as service:
        with LocalWeb(service) as app:
            (root/'server.json').write_text(json.dumps({'origin':app.origin}), encoding='utf-8')
            threading.Event().wait(120)


if __name__ == '__main__':
    main()
