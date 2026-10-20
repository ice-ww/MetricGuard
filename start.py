"""Daily entry point; paths belong to this checkout, never the caller's cwd."""
from pathlib import Path


if __name__ == '__main__':
    from metricguard.daily import main
    raise SystemExit(main(Path(__file__).resolve().parent))
