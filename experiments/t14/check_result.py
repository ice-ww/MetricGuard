"""Compare playback reports to independently reconciled raw play records."""
import argparse
import json
from math import isclose
from pathlib import Path
from experiments.t14.reference import reference


def check(database: Path, result: dict) -> dict:
    expected = reference(database, *result['actual_window'])
    diagnosis = result['report']['diagnosis']
    metrics = {(m['period'], m['actual_os'], m['actual_version']): m for m in diagnosis['playback_metrics']}
    evidence = {e['evidence_id']:e for e in result['evidence']}
    checked = 0
    sufficient = all(not r['quality_flags'] and r['sources_complete'] for r in expected['rows'])
    if sufficient:
        for row in expected['rows']:
            metric = metrics.pop((row['period'], row['os'], row['version']))
            for field in ('starts', 'observed_completed', 'independent_complete', 'effective', 'missing_completion'):
                assert metric[field] == row[field], (field, metric, row)
                checked += 1
            for field, count in [('observed_completion_rate','observed_completed'),
                                  ('independent_completion_rate','independent_complete'), ('effective_playback_rate','effective')]:
                value = row[count] / row['starts'] if row['starts'] else None
                assert (metric[field] is None if value is None else isclose(metric[field],value,rel_tol=1e-12))
                checked += 1
        assert not metrics
    else:
        assert diagnosis['status'] == 'insufficient_evidence', diagnosis
        assert diagnosis['missing_evidence'] and not diagnosis['candidates']
        assert all(m['missing_completion'] is None for m in metrics.values())
    for metric in diagnosis['playback_metrics']:
        for ref in metric['source_facts']:
            assert ref['values'] == evidence[ref['evidence_id']]['rows'][ref['row']]
            checked += 1
    assert result['tokens'] == sum(a['actual'] for a in result['attempts'] if a['kind'] == 'model')
    assert all(c['causality']=='not_established' for c in diagnosis['candidates'])
    return {'checks': checked, 'sufficient_reference': sufficient, 'reference': expected,
            'diagnosis': diagnosis['status'], 'actual_usage':result['tokens']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', type=Path, required=True)
    parser.add_argument('--result', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = check(args.database, json.loads(args.result.read_text(encoding='utf-8')))
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='reference'}))
