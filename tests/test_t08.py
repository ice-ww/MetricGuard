from dataclasses import replace

import pytest

from experiments.t08.contract import Assertion, ChartSpec, EvidenceResult, EvidenceStore, FactContext, Reference


def example():
    context = FactContext('retention', ('2026-01-01', '2026-01-08'), {'os': 'Android'}, None)
    evidence = EvidenceResult(
        'e1', 'query', {'start': '2026-01-01'}, 'SELECT retained/users AS rate', 'snapshot-1',
        {'os': 'string', 'rate': 'number'}, ({'os': 'Android', 'rate': 0.5},),
        {'/rows/0/rate': context}, context.window, context.group, {'users': 10}, (), False,
    )
    return evidence, Assertion('a1', Reference('e1', 0, 'rate'), context, 0.5)


def test_fact_can_be_retrieved_and_checked_against_specific_result_cell():
    evidence, assertion = example()
    store = EvidenceStore()
    store.add(evidence)
    assert store.get('e1') == evidence
    assert store.validate(assertion).passed
    assert not store.validate(replace(assertion, value=0.6)).passed


@pytest.mark.parametrize('change', [
    {'reference': Reference('absent', 0, 'rate')},
    {'reference': Reference('e1', -1, 'rate')},
    {'reference': Reference('e1', 1, 'rate')},
    {'reference': Reference('e1', 0, 'absent')},
    {'value': True}, {'value': float('nan')},
    {'scope': 'invented_scope'},
    {'context': FactContext('wrong', ('2026-01-01', '2026-01-08'), {'os': 'Android'}, None)},
    {'context': FactContext('retention', ('2026-01-02', '2026-01-08'), {'os': 'Android'}, None)},
    {'context': FactContext('retention', ('2026-01-01', '2026-01-08'), {'os': 'iOS'}, None)},
    {'context': FactContext('retention', ('2026-01-01', '2026-01-08'), {'os': 'Android'}, 'last_week')},
])
def test_incorrect_assertion_rejected(change):
    evidence, assertion = example()
    store = EvidenceStore()
    store.add(evidence)
    assert not store.validate(replace(assertion, **change)).passed


def test_documents_and_truncated_rows_cannot_support_population_claims():
    evidence, assertion = example()
    for evidence_change, claim_change in [
        ({'kind': 'definition'}, {}),
        ({'truncated': True}, {'scope': 'whole_population'}),
        ({'truncated': True}, {'scope': 'complete_ranking'}),
    ]:
        store = EvidenceStore()
        store.add(replace(evidence, **evidence_change))
        assert not store.validate(replace(assertion, **claim_change)).passed
    store = EvidenceStore()
    store.add(replace(evidence, truncated=True, whole_population_fields=('/rows/0/rate',)))
    assert store.validate(replace(assertion, scope='whole_population')).passed
    assert not store.validate(replace(assertion, scope='complete_ranking')).passed


def test_result_is_write_once_and_cannot_be_changed_via_mutable_inputs():
    evidence, assertion = example()
    store = EvidenceStore()
    store.add(evidence)
    evidence.rows[0]['rate'] = 99
    store.get('e1').contexts['/rows/0/rate'].group['os'] = 'iOS'
    assert store.validate(replace(assertion, context=FactContext('retention', ('2026-01-01', '2026-01-08'), {'os': 'Android'}, None))).passed
    with pytest.raises(ValueError, match='duplicate'):
        store.add(evidence)


def test_chart_resolves_existing_cells_without_accepting_supplied_values():
    evidence, _ = example()
    store = EvidenceStore()
    store.add(evidence)
    chart = ChartSpec('c1', 'bar', (Reference('e1', 0, 'os'),), (Reference('e1', 0, 'rate'),))
    rendered, = store.render_charts((chart,))
    assert rendered.points == (('Android', 0.5),)
    assert rendered.evidence_ids == ('e1',)
    with pytest.raises(ValueError, match='chart_limit'):
        store.render_charts(tuple(replace(chart, chart_id=f'c{i}') for i in range(4)))
    for bad in [replace(chart, kind='pie'), replace(chart, x_refs=()),
                replace(chart, y_refs=(Reference('missing', 0, 'rate'),)),
                replace(chart, y_refs=(Reference('e1', 1, 'rate'),)),
                replace(chart, y_refs=(Reference('e1', 0, 'os'),))]:
        with pytest.raises(ValueError):
            store.render_charts((bad,))


def test_chart_rejects_cross_row_and_incompatible_metrics():
    evidence, _ = example()
    context = evidence.contexts['/rows/0/rate']
    evidence = replace(evidence, group={}, rows=evidence.rows + ({'os': 'iOS', 'rate': 0.7},),
                       contexts={**evidence.contexts, '/rows/1/rate': replace(context, metric='completion', group={'os': 'iOS'})})
    store = EvidenceStore()
    store.add(evidence)
    for chart in [ChartSpec('c', 'bar', (Reference('e1', 0, 'os'),), (Reference('e1', 1, 'rate'),)),
                  ChartSpec('c', 'bar', tuple(Reference('e1', i, 'os') for i in range(2)),
                            tuple(Reference('e1', i, 'rate') for i in range(2)))]:
        with pytest.raises(ValueError):
            store.render_charts((chart,))


@pytest.mark.parametrize('change', [
    {'source': ''}, {'snapshot_id': ''}, {'tool': ''},
    {'columns': {'os': 'string', 'rate': 'string'}},
    {'columns': {'os': 'string', 'rate': 'imaginary'}},
    {'rows': ({'os': 'Android'},)},
    {'rows': ({'os': 'Android', 'rate': float('inf')},)},
    {'window': ('2026-01-08', '2026-01-01')},
    {'contexts': {'/rows/99/rate': FactContext('retention', ('2026-01-01', '2026-01-08'), {}, None)}},
    {'whole_population_fields': ('/rows/99/rate',)},
])
def test_invalid_evidence_never_enters_store(change):
    evidence, _ = example()
    with pytest.raises(ValueError):
        EvidenceStore().add(replace(evidence, **change))


def test_report_cannot_pass_with_empty_or_duplicate_assertions():
    evidence, assertion = example()
    store = EvidenceStore()
    store.add(evidence)
    assert store.validate_report((assertion,)).passed
    assert not store.validate_report(()).passed
    assert not store.validate_report((assertion, assertion)).passed
    result = store.validate_report((assertion, replace(assertion, assertion_id='a2', value=0.8)))
    assert not result.passed
    assert result.valid_count == 1 and result.assertion_count == 2


@pytest.mark.parametrize('kind', ['bar', 'line'])
def test_single_series_chart_cannot_hide_other_group_or_window_changes(kind):
    evidence, _ = example()
    context = evidence.contexts['/rows/0/rate']
    for other in (replace(context, group={'os': 'iOS', 'channel': 'paid'}),
                  replace(context, group={'os': 'iOS'}, window=('2026-01-02', '2026-01-08'))):
        store = EvidenceStore()
        store.add(replace(evidence, group={}, rows=evidence.rows + ({'os': 'iOS', 'rate': 0.7},),
                          contexts={**evidence.contexts, '/rows/1/rate': other}))
        chart = ChartSpec('c', kind, tuple(Reference('e1', i, 'os') for i in range(2)),
                          tuple(Reference('e1', i, 'rate') for i in range(2)))
        with pytest.raises(ValueError, match='incompatible'):
            store.render_charts((chart,))
