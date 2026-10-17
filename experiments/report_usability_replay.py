"""Re-render preserved manual tasks through public APIs without touching originals."""
from contextlib import redirect_stdout
from decimal import Decimal
import gzip
import hashlib
from io import StringIO
import json
from pathlib import Path
import re
import sqlite3
from uuid import uuid4
from metricguard import TaskService
from metricguard.console import interact


def main():
    original=json.loads(gzip.decompress(Path('docs/validation/report-usability-before.json.gz').read_bytes()))
    root=Path('artifacts/report-usability')/uuid4().hex;root.mkdir(parents=True)
    records=[]
    for old in original:
        report_path=Path(old['path']); state_root=report_path.parents[3]; session_root=report_path.parents[4]
        config=json.loads((session_root/'session.json').read_text(encoding='utf-8'))
        prior=json.loads(old['files']['task.json']['text']); task=prior['id']
        copy=root/task/'state';copy.mkdir(parents=True)
        for database in state_root.glob('*.sqlite'):
            with sqlite3.connect(database.as_uri()+'?mode=ro',uri=True) if database.is_absolute() else sqlite3.connect(database.resolve().as_uri()+'?mode=ro',uri=True) as source:
                with sqlite3.connect(copy/database.name) as target:source.backup(target)
        with TaskService(copy,config['image'],{'dev':Path(config['database'])},token='not-used') as service:
            before=service.inspect(task);output=StringIO()
            with redirect_stdout(output):interact(service,before)
            exported=service.export_report(task);after=service.inspect(task)
        publication=json.loads((Path(exported['report']).parent/'publication.json').read_text(encoding='utf-8'))
        old_publication=json.loads(old['files']['publication.json']['text'])
        for key in ['assertions','inferences']:assert publication[key]==old_publication[key],(task,key)
        for key in ['model_calls','tool_calls','tokens','actual_window','requested_window','comparison_window','analysis_result']:
            assert before.get(key)==after.get(key),(task,key)
        assert exported['terminal_body'] in output.getvalue()
        assert '(#fact-' not in exported['terminal_body']
        by_id={a['assertion_id']:a for a in publication['assertions']};sources={e['evidence_id']:e for e in after['evidence']}
        for a in publication['assertions']:
            ref=a['reference'];assert sources[ref['evidence_id']]['rows'][ref['row']][ref['column']]==a['value']
        checked=0
        for line in exported['body'].splitlines():
            match=re.search(r'差值 ([+-][0-9.]+) 个百分点',line)
            if match:
                ids=re.findall(r'\[A(\d+)\]',line); assert len(ids)==2
                expected=(Decimal(str(by_id[ids[1]]['value']))-Decimal(str(by_id[ids[0]]['value'])))*100
                assert abs(Decimal(match[1])-expected)<=Decimal('0.0005')
                checked+=1
        for name,record in old['files'].items():
            assert hashlib.sha256((report_path.parent/name).read_bytes()).hexdigest()==record['sha256']
        records.append({'task':task,'original_report':str(report_path),'exported':exported,
            'terminal':output.getvalue(),'markdown':Path(exported['report']).read_text(encoding='utf-8'),
            'publication':publication,'task_record':after,'percentage_point_checks':checked,
            'no_new_model_or_query_calls':True,'original_hashes_unchanged':True})
    result={'source_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('metricguard').glob('*.py')},'records':records}
    (root/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    Path('docs/validation/report-usability-after.json.gz').write_bytes(gzip.compress(json.dumps(result,ensure_ascii=False,indent=2).encode(),mtime=0))
    print('Replayed',len(records),'reports;',sum(r['percentage_point_checks'] for r in records),'independent percentage-point checks;',root)


if __name__=='__main__':main()
