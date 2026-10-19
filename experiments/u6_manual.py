"""One-command local UI acceptance, using the production server and stable snapshots."""
import argparse
from pathlib import Path
from experiments.t01.snapshots import build_snapshot
from metricguard.web_start import main as start_web


def main() -> None:
    parser = argparse.ArgumentParser(description='启动 U6 开发验收界面；复用原目录以保留任务与数据。')
    parser.add_argument('--state-dir', type=Path, default=Path('artifacts/u6-manual/state'))
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    directory = args.state_dir.resolve().parent/'diagnosis-data'
    database = directory/'public'/'snapshot.duckdb'
    if not directory.exists():
        build_snapshot(directory, scenario='A4', seed=361100)
    print('开发验收：demo 用于简单查询；diagnosis 用于分系统留存诊断。', flush=True)
    print('固定本期 2026-01-08 至 2026-01-15，基期 2026-01-01 至 2026-01-08，结束日不包含。', flush=True)
    start_web(['--demo', '--snapshot', 'diagnosis='+str(database), '--state-dir', str(args.state_dir), '--port', str(args.port)])


if __name__ == '__main__':
    main()
