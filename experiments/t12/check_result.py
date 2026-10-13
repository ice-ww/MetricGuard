"""Compare published profile evidence to independently counted raw records."""
import argparse
import json
from math import isclose
from pathlib import Path
from experiments.t12.reference import reference


def check(database: Path, result: dict) -> dict:
    expected = reference(database, *result['actual_window'])
    profiles = {e['parameters'].get('kind'): e for e in result['evidence'] if e['tool'] == 'profile'}
    health = profiles['cohort_health']
    rows = {(r['period'], r['registration_os'], r['registration_version']): r for r in health['rows']}
    checked = 0
    for period in ('previous', 'current'):
        for oracle in expected[period]['groups']:
            if oracle['registration_version'] is None:
                continue
            actual = rows.pop((period, oracle['registration_os'], oracle['registration_version']))
            for field, source in [('users', 'new_users'), ('retained', 'd1_retained'),
                                  ('crashed_users', 'first_day_crash_users'),
                                  ('retention_rate', 'd1_retention_rate'), ('crash_rate', 'first_day_crash_rate')]:
                assert isclose(actual[field], oracle[source], abs_tol=1e-12), (field, actual, oracle)
                checked += 1
            assert actual['window_start'] == expected[period]['start']
            assert actual['window_end'] == expected[period]['end']
    assert not rows, rows
    crash_checks = 0
    if 'crash_versions' in profiles:
        crashes = {(r['period'], r['registration_os'], r['registration_version'], r['actual_os'], r['actual_version']): r
                   for r in profiles['crash_versions']['rows']}
        for period in ('previous', 'current'):
            for oracle in expected[period]['actual_crashes']:
                if oracle['registration_version'] is None:
                    continue
                actual = crashes.pop((period, oracle['registration_os'], oracle['registration_version'], oracle['actual_os'], oracle['actual_version']))
                assert actual['crashed_users'] == oracle['first_day_crash_users']
                assert [actual['window_start'], actual['window_end']] == [expected[period]['start'], expected[period]['end']]
                crash_checks += 1
        assert not crashes, crashes
    release_checks = 0
    if 'releases' in profiles:
        assert profiles['releases']['rows'] == [{k:r[k] for k in ('os', 'version', 'release_date')}
                                               for r in expected['releases'] if r['release_date'] < result['actual_window'][1]]
        release_checks = len(profiles['releases']['rows'])
    assert all(not e['truncated'] for e in profiles.values())
    assert result['tokens'] == sum(a['actual'] for a in result['attempts'] if a['kind'] == 'model')
    return {'cohort_numeric_checks': checked, 'actual_crash_checks': crash_checks,
            'release_checks': release_checks, 'reference': expected,
            'actual_usage': result['tokens'], 'outcome': result['outcome']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', type=Path, required=True)
    parser.add_argument('--result', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    verification = check(args.database, json.loads(args.result.read_text(encoding='utf-8')))
    args.output.write_text(json.dumps(verification, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in verification.items() if k != 'reference'}))
