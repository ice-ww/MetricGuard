"""Real process owner with a fixed external progress clock; never contacts a model."""
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import threading

from metricguard import TaskService
from metricguard.web import LocalWeb


def main():
    root = Path(sys.argv[1])
    with TaskService(root/'state', 'unused', {'dev':root/'snapshot'}, token='controlled',
                     progress_clock=lambda:datetime(2026, 10, 19, 1, tzinfo=timezone.utc)) as service:
        with LocalWeb(service) as app:
            (root/'server.json').write_text(json.dumps({'origin':app.origin, 'token':app.token}), encoding='utf-8')
            threading.Event().wait(120)


if __name__ == '__main__':
    main()
