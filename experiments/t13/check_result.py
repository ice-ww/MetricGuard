"""Independent raw-record checks for public channel diagnosis results."""
import argparse
import json
from math import isclose
from pathlib import Path
from experiments.t13.reference import reference


def check(database: Path, result: dict) -> dict:
    expected = reference(database, *result['actual_window'])
    evidence = next(e for e in result['evidence'] if e['parameters'].get('kind') == 'channel_health')
    actual = {(r['period'], r['channel']): r for r in evidence['rows']}
    metrics = {r['channel']: r for r in result['report']['diagnosis']['channel_metrics']}
    count = 0
    for row in expected['rows']:
        found = dict(actual.pop((row['period'], row['channel'])))
        derived = metrics[row['channel']]
        found.update({k:derived[k] for k in ('new_users_delta', 'total_new_users_delta', 'growth_contribution')})
        found['user_share'] = derived['user_share'][row['period']]
        for field, value in row.items():
            observed = found[field]
            if type(value) in (int, float):
                assert type(observed) in (int, float) and isclose(observed, value, rel_tol=1e-12, abs_tol=1e-12), (field, observed, value)
            else:
                assert observed == value, (field, observed, value)
            count += 1
    assert not actual
    for metric in metrics.values():
        assert metric['derivation'] == 'program_from_complete_channel_profile'
        for ref in metric['source_facts']:
            assert ref['evidence_id'] == evidence['evidence_id']
            assert ref['values'] == evidence['rows'][ref['row']]
    assert not evidence['truncated'] and result['report']['validation']['passed']
    assert result['tokens'] == sum(a['actual'] for a in result['attempts'] if a['kind'] == 'model')
    return {'cell_checks': count, 'reference': expected, 'outcome': result['outcome'], 'actual_usage': result['tokens']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', type=Path, required=True)
    parser.add_argument('--result', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    verified = check(args.database, json.loads(args.result.read_text(encoding='utf-8')))
    args.output.write_text(json.dumps(verified, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in verified.items() if k != 'reference'}))
