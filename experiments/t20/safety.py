"""Execute the full suite once and retain a configuration-bound safety receipt."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from metricguard.evaluation import EvaluationRunner, file_hash
from metricguard.semantic_rubric import digest
from metricguard.acceptance import validate_safety, collect_tests
from experiments.t18.freeze import configuration


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--image',required=True); args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    config=configuration(args.image)
    hashes={p.as_posix():file_hash(p) for p in Path('tests').rglob('*.py')}
    collected=collect_tests(Path.cwd())
    junit=args.output/'suite.xml'
    environment={**os.environ,'METRICGUARD_TEST_IMAGE':args.image}
    command=[sys.executable,'-m','pytest','-q','--junitxml='+str(junit)]
    with (args.output/'suite.log').open('w',encoding='utf-8') as log:
        result=subprocess.run(command,env=environment,stdout=log,stderr=subprocess.STDOUT)
    receipt={'configuration_hash':digest(config),'configuration':config,'test_hashes':hashes,'collected_nodeids':collected,
        'command':command,'exit_code':result.returncode,'junit_xml':junit.read_text(encoding='utf-8') if junit.exists() else '',
        'log_sha256':file_hash(args.output/'suite.log')}
    (args.output/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    # Fail after retaining all output if source changes occurred during execution.
    EvaluationRunner(args.output/'configuration-audit').verify_configuration(config)
    assessed=validate_safety(receipt,config,Path.cwd())
    print(json.dumps(assessed),flush=True)
    if result.returncode: raise SystemExit(result.returncode)


if __name__=='__main__': main()
