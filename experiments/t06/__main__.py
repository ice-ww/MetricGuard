import argparse
from pathlib import Path
from .experiment import run
parser = argparse.ArgumentParser()
parser.add_argument("--output", required=True, type=Path)
args = parser.parse_args()
report = run(args.output)
print({"passed": report["passed"], "selected_calibration": report["selected_calibration"], "queries": len(report["results"]), "reference_checks": len(report["reference_checks"])})
raise SystemExit(0 if report["passed"] else 1)
