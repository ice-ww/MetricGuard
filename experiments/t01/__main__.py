"""Run with: uv run python -m experiments.t01 --output artifacts/t01-run"""

import argparse
from pathlib import Path

from .validation import run_experiment


def main() -> None:
    parser = argparse.ArgumentParser(description="T01 development data/reference experiment")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seeds", type=int, nargs="+", default=[7, 19, 41])
    args = parser.parse_args()
    report = run_experiment(args.output, seeds=args.seeds)
    print(f"automatic_pass={report['automatic_pass']}; human_review=pending")
    print(args.output / "private" / "report.json")
    raise SystemExit(0 if report["automatic_pass"] else 1)


if __name__ == "__main__":
    main()
