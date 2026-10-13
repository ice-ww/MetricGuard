"""Independently recompute system diagnostic results for development acceptance."""
import math
from pathlib import Path
from typing import Any
from experiments.t15.reference import reference


def check(result: dict[str, Any], database: Path) -> dict[str, Any]:
    expected = reference(database, *result['actual_window'])
    diagnosis = result['report']['diagnosis']
    profiles = [e for e in result['evidence'] if e['parameters'].get('kind')=='system_retention']
    assert profiles and profiles[-1]['rows']==expected['rows']
    checks = len(expected['rows'])*len(expected['rows'][0])
    for key in ('standardized_retention','within_effect_pp','composition_effect_pp','total_change_pp'):
        assert math.isclose(diagnosis[key],expected[key],abs_tol=1e-10), key
        checks += 1
    for period, value in expected['actual_retention'].items():
        assert math.isclose(diagnosis['actual_retention'][period],value,abs_tol=1e-10)
        checks += 1
    assert math.isclose(diagnosis['total_change_pp'],diagnosis['within_effect_pp']+diagnosis['composition_effect_pp'],abs_tol=1e-10)
    by_id = {e['evidence_id']: e for e in result['evidence']}
    for ref in diagnosis['source_facts']:
        assert by_id[ref['evidence_id']]['rows'][ref['row']]==ref['values']
        checks += 1
    for fact in result['report']['facts']:
        assert by_id[fact['evidence_id']]['rows'][fact['row']][fact['column']]==fact['value']
        checks += 1
    assert result['report']['validation']['passed']
    assert diagnosis['difference_interval_pp'] is None
    assert all(a['state']=='completed' for a in result['attempts'])
    return dict(passed=True, numeric_and_reference_checks=checks, diagnosis_status=diagnosis['status'],
                tokens=result['tokens'], model_calls=result['model_calls'], tool_calls=result['tool_calls'])
