import argparse
from pathlib import Path

from .validation import run_experiment


def main() -> None:
    parser = argparse.ArgumentParser(description="T04 independent statistics and development calibration")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--seeds", nargs="+", type=int, default=[7, 19, 41])
    parser.add_argument("--simulations", type=int, default=2000)
    args = parser.parse_args()
    report = run_experiment(args.output, seeds=args.seeds, simulations=args.simulations)
    print(f"automatic_pass={report['automatic_pass']}; report={args.output / 'report.json'}")
    raise SystemExit(0 if report["automatic_pass"] else 1)


if __name__ == "__main__":
    main()
