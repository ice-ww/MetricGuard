"""Re-export archived real tasks after presentation fixes, preserving original receipts."""
from contextlib import redirect_stdout
import gzip
import hashlib
from io import StringIO
import json
import os
from pathlib import Path
import sys
from metricguard import TaskService
from metricguard.console import interact


def main():
    root=Path(sys.argv[1]); results=[]
    for original in sorted(root.glob('*/result.json')):
        previous=json.loads(original.read_text(encoding='utf-8')); directory=original.parent
        with TaskService(directory/'state',os.environ['METRICGUARD_TEST_IMAGE'],{'dev':directory/'data'/'public'/'snapshot.duckdb'},token='unused') as service:
            before=service.inspect(previous['task']['id'])
            output=StringIO()
            with redirect_stdout(output): interact(service,before)
            exported=service.export_report(before['id']); after=service.inspect(before['id'])
        assert before['model_calls']==after['model_calls'] and before['tool_calls']==after['tool_calls']
        model_questions={q for step in after['diagnostic_history'] if step['action']['action']=='stop' for q in step['action']['unresolved_questions']}
        assert all(q not in exported['body'] for q in model_questions)
        assert exported['terminal_body'] in output.getvalue()
        report=Path(exported['report']).read_text(encoding='utf-8')
        assert exported['body'] in report
        updated={**previous,'task':after,'terminal':output.getvalue(),'exported':exported,'markdown':report,
                 'original_receipt_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),
                 'presentation_only_reexport':True,
                 'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('metricguard').glob('*.py')}}
        (directory/'rerendered.json').write_text(json.dumps(updated,ensure_ascii=False,indent=2),encoding='utf-8')
        results.append({'case':previous['case'],'original':previous,'rerendered':updated})
    archive=Path('docs/validation/f5-live.json.gz')
    archive.write_bytes(gzip.compress(json.dumps(results,ensure_ascii=False,indent=2).encode('utf-8'),mtime=0))
    print('Preserved and re-exported',len(results),'cases:',archive)


if __name__=='__main__':main()
