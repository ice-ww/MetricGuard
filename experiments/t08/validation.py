"""Development-only independent SQL versus Python membership/count experiment."""

from dataclasses import asdict, replace
import importlib.metadata
import json
from pathlib import Path
import platform
import tempfile
from typing import Any

from experiments.t01.references import python_metrics, sql_metrics
from experiments.t01.snapshots import build_snapshot
from .contract import Assertion, ChartSpec, EvidenceResult, EvidenceStore, FactContext, Reference


def run_validation() -> dict[str, Any]:
    checks: dict[str, bool] = {}
    window = ('2026-01-01', '2026-01-08')
    with tempfile.TemporaryDirectory(prefix='metricguard-t08-') as directory:
        snapshot = build_snapshot(Path(directory) / 'snapshot', scenario='normal', seed=809)
        sql = sql_metrics(snapshot.database, *window)['retention']
        oracle = python_metrics(snapshot.database, *window)['retention']
        checks['independent_membership_oracle_matches_relational_counts_and_rates'] = sql == oracle
        columns = {name: ('string' if name in ('os', 'version', 'channel') else 'number') for name in sql[0]}
        contexts = {Reference('retention', index, name).pointer:
                    FactContext(name, window, {k: row[k] for k in ('os', 'version', 'channel')}, None)
                    for index, row in enumerate(sql) for name in columns if columns[name] == 'number'}
        evidence = EvidenceResult('retention', 'reference_query', {'start': window[0], 'end': window[1]},
                                  'experiments/t01/references.py:sql_metrics; cohort.sql', snapshot.logical_hash,
                                  columns, tuple(sql), contexts, window, {}, {'groups': len(sql)},
                                  ('Natural days Asia/Shanghai; registration dimensions; mature cohorts only.',), False)
        store = EvidenceStore()
        store.add(evidence)
        claims = tuple(Assertion(f'fact-{i}', Reference('retention', i, 'retention_rate'),
                                 contexts[f'/rows/{i}/retention_rate'], row['retention_rate'])
                       for i, row in enumerate(oracle))
        checks['all_independently_expected_facts_pass'] = store.validate_report(claims).passed
        claim = claims[0]
        changes: dict[str, dict[str, Any]] = {
            'missing_evidence': {'reference': Reference('absent', 0, 'retention_rate')},
            'missing_row': {'reference': Reference('retention', 999, 'retention_rate')},
            'missing_column': {'reference': Reference('retention', 0, 'absent')},
            'wrong_value': {'value': 99},
            'wrong_metric': {'context': replace(claim.context, metric='completion_rate')},
            'wrong_time': {'context': replace(claim.context, window=('2026-01-02', window[1]))},
            'wrong_group': {'context': replace(claim.context, group={'os': 'unknown'})},
            'wrong_comparison': {'context': replace(claim.context, comparison='prior_week')},
        }
        for name, change in changes.items():
            checks[f'reject_{name}'] = not store.validate(replace(claim, **change)).passed
        for name, altered, altered_claim in (
            ('definition_as_number', replace(evidence, kind='definition'), claim),
            ('truncated_population', replace(evidence, truncated=True), replace(claim, scope='whole_population')),
            ('truncated_ranking', replace(evidence, truncated=True), replace(claim, scope='complete_ranking')),
        ):
            other = EvidenceStore()
            other.add(altered)
            checks[f'reject_{name}'] = not other.validate(altered_claim).passed
        aggregate = EvidenceStore()
        aggregate.add(replace(evidence, truncated=True, whole_population_fields=(claim.reference.pointer,)))
        checks['trusted_query_computed_population_field_allowed'] = aggregate.validate(replace(claim, scope='whole_population')).passed
        # Deliberately wrong denominator: agreement with one's own query is insufficient.
        wrong_rows = tuple({**row, 'retention_rate': row['retained'] / (row['users'] + 1)} for row in sql)
        wrong_store = EvidenceStore()
        wrong_store.add(replace(evidence, rows=wrong_rows, source='controlled wrong denominator: retained / (users + 1)'))
        wrong_claim = replace(claim, value=wrong_rows[0]['retention_rate'])
        checks['wrong_business_denominator_can_match_its_own_cell'] = wrong_store.validate(wrong_claim).passed
        checks['independent_oracle_rejects_wrong_denominator'] = wrong_claim.value != oracle[0]['retention_rate']
        chart_indexes = [i for i, row in enumerate(sql) if row['channel'] == 'organic']
        chart = ChartSpec('chart', 'bar', tuple(Reference('retention', i, 'os') for i in chart_indexes),
                          tuple(Reference('retention', i, 'retention_rate') for i in chart_indexes))
        rendered, = store.render_charts((chart,))
        checks['chart_copies_existing_values_only'] = rendered.points == tuple((oracle[i]['os'], oracle[i]['retention_rate']) for i in chart_indexes)
        for name, charts in (
            ('four_charts', tuple(replace(chart, chart_id=f'c{i}') for i in range(4))),
            ('missing_chart_reference', (replace(chart, y_refs=(Reference('absent', 0, 'retention_rate'),), x_refs=(chart.x_refs[0],)),)),
            ('chart_row_mismatch', (replace(chart, y_refs=(chart.y_refs[1],), x_refs=(chart.x_refs[0],)),)),
        ):
            try:
                store.render_charts(charts)
            except ValueError:
                checks[f'reject_{name}'] = True
            else:
                checks[f'reject_{name}'] = False
        checks['empty_report_rejected'] = not store.validate_report(()).passed
        return {
            'protocol_version': 1, 'passed': all(checks.values()), 'checks': checks,
            'environment': {'python': platform.python_version(), 'platform': platform.platform(),
                            'duckdb': importlib.metadata.version('duckdb')},
            'data': {'purpose': 'development validation, not frozen acceptance', 'seed': 809,
                     'scenario': 'normal', 'snapshot_id': snapshot.logical_hash, 'window': window},
            'evidence': asdict(evidence), 'independent_expected_rows': oracle,
            'report_validation': asdict(store.validate_report(claims)), 'chart': asdict(rendered),
            'boundary': 'Mechanical agreement only; independent oracle checks this fixture business definition; inference not assessed.',
        }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = run_validation()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    print(json.dumps({'passed': report['passed'], 'checks': len(report['checks']), 'output': str(args.output)}))
    if not report['passed']:
        raise SystemExit(1)
