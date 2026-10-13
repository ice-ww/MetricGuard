"""Mechanical evidence validation. Context must be assigned by trusted tool code.

This boundary does not prove that a SQL query implements a business definition or
that a cited observation supports an inference. Those are separate assessments.
"""

from copy import deepcopy
from dataclasses import dataclass
from datetime import date
import json
import math
from typing import Any


@dataclass(frozen=True)
class FactContext:
    metric: str
    window: tuple[str, str]
    group: dict[str, str]
    comparison: str | None


@dataclass(frozen=True)
class Reference:
    evidence_id: str
    row: int
    column: str

    @property
    def pointer(self) -> str:
        escaped = self.column.replace('~', '~0').replace('/', '~1')
        return f'/rows/{self.row}/{escaped}'


@dataclass(frozen=True)
class EvidenceResult:
    evidence_id: str
    tool: str
    parameters: dict[str, Any]
    source: str
    snapshot_id: str
    columns: dict[str, str]
    rows: tuple[dict[str, Any], ...]
    contexts: dict[str, FactContext]
    window: tuple[str, str]
    group: dict[str, str]
    sample: dict[str, Any]
    limitations: tuple[str, ...]
    truncated: bool
    kind: str = 'query'
    whole_population_fields: tuple[str, ...] = ()


@dataclass(frozen=True)
class Assertion:
    assertion_id: str
    reference: Reference
    context: FactContext
    value: int | float
    scope: str = 'cell'


@dataclass(frozen=True)
class ValidationResult:
    assertion_id: str
    passed: bool
    errors: tuple[str, ...]
    business_definition_status: str = 'requires_independent_reference'
    inference_status: str = 'not_assessed'


@dataclass(frozen=True)
class ChartSpec:
    chart_id: str
    kind: str
    x_refs: tuple[Reference, ...]
    y_refs: tuple[Reference, ...]


@dataclass(frozen=True)
class RenderedChart:
    chart_id: str
    kind: str
    points: tuple[tuple[Any, Any], ...]
    evidence_ids: tuple[str, ...]
    references: tuple[tuple[Reference, Reference], ...]
    limitations: tuple[str, ...]


@dataclass(frozen=True)
class ReportValidation:
    passed: bool
    assertion_count: int
    valid_count: int
    results: tuple[ValidationResult, ...]
    errors: tuple[str, ...]
    protocol_version: int = 1


class EvidenceStore:
    """Write-once result identifiers, copied at ingress and egress."""

    def __init__(self) -> None:
        self._evidence: dict[str, EvidenceResult] = {}

    def add(self, evidence: EvidenceResult) -> None:
        if evidence.evidence_id in self._evidence:
            raise ValueError('duplicate_evidence_id')
        validate_evidence(evidence)
        self._evidence[evidence.evidence_id] = deepcopy(evidence)

    def get(self, evidence_id: str) -> EvidenceResult:
        return deepcopy(self._evidence[evidence_id])

    def validate(self, assertion: Assertion) -> ValidationResult:
        errors: list[str] = []
        ref = assertion.reference
        try:
            # Validation only reads the owned snapshot. Copying the whole result for
            # every cell makes bounded 1,000-row reports quadratic in data size.
            evidence = self._evidence[ref.evidence_id]
            if type(ref.row) is not int or ref.row < 0:
                raise IndexError()
            value = evidence.rows[ref.row][ref.column]
        except (KeyError, IndexError):
            return ValidationResult(assertion.assertion_id, False, ('missing_reference',))
        if not numeric(value) or not numeric(assertion.value) or value != assertion.value:
            errors.append('value_mismatch')
        if evidence.contexts.get(ref.pointer) != assertion.context:
            errors.append('context_mismatch')
        if evidence.kind == 'definition':
            errors.append('definition_is_not_numeric_evidence')
        if assertion.scope not in ('cell', 'whole_population', 'complete_ranking'):
            errors.append('invalid_scope')
        if evidence.truncated and assertion.scope != 'cell':
            if assertion.scope != 'whole_population' or ref.pointer not in evidence.whole_population_fields:
                errors.append('truncated_does_not_support_scope')
        return ValidationResult(assertion.assertion_id, not errors, tuple(errors))

    def render_charts(self, charts: tuple[ChartSpec, ...]) -> tuple[RenderedChart, ...]:
        """Pure postprocessing; no model or diagnostic tool calls, no aggregation."""
        if len(charts) > 3:
            raise ValueError('chart_limit')
        if len({chart.chart_id for chart in charts}) != len(charts):
            raise ValueError('duplicate_chart_id')
        rendered = []
        for chart in charts:
            if chart.kind not in ('bar', 'line') or not chart.chart_id:
                raise ValueError('invalid_chart')
            if not chart.x_refs or len(chart.x_refs) != len(chart.y_refs):
                raise ValueError('chart_length_mismatch')
            points = []
            signature = None
            limitations: set[str] = set()
            for x, y in zip(chart.x_refs, chart.y_refs, strict=True):
                if (x.evidence_id, x.row) != (y.evidence_id, y.row):
                    raise ValueError('chart_row_mismatch')
                try:
                    evidence = self.get(y.evidence_id)
                    if type(y.row) is not int or y.row < 0:
                        raise KeyError()
                    context = evidence.contexts[y.pointer]
                    xv, yv = evidence.rows[x.row][x.column], evidence.rows[y.row][y.column]
                except (KeyError, IndexError):
                    raise ValueError('chart_missing_reference') from None
                if evidence.kind == 'definition' or not numeric(yv) or xv is None or type(xv) is bool:
                    raise ValueError('chart_invalid_data')
                point_signature = (context.metric, context.comparison, evidence.snapshot_id,
                                   context.window,
                                   tuple(sorted((k, v) for k, v in context.group.items() if k != x.column)))
                if signature is not None and signature != point_signature:
                    raise ValueError('chart_incompatible_series')
                signature = point_signature
                limitations.update(evidence.limitations)
                if evidence.truncated:
                    limitations.add('partial_result_not_complete_population_or_ranking')
                points.append((xv, yv))
            rendered.append(RenderedChart(chart.chart_id, chart.kind, tuple(points),
                            tuple(sorted({r.evidence_id for r in chart.y_refs})),
                            tuple(zip(chart.x_refs, chart.y_refs)), tuple(sorted(limitations))))
        return tuple(rendered)

    def validate_report(self, assertions: tuple[Assertion, ...]) -> ReportValidation:
        results = tuple(self.validate(assertion) for assertion in assertions)
        errors = []
        if not assertions:
            errors.append('empty_report')
        if len({a.assertion_id for a in assertions}) != len(assertions):
            errors.append('duplicate_assertion_id')
        if any(not a.assertion_id for a in assertions):
            errors.append('missing_assertion_id')
        valid = sum(result.passed for result in results)
        return ReportValidation(not errors and valid == len(results), len(results), valid, results, tuple(errors))


def numeric(value: Any) -> bool:
    return type(value) is int or (type(value) is float and math.isfinite(value))


def validate_evidence(evidence: EvidenceResult) -> None:
    """Schema/provenance shape checks; authenticity belongs to the tool boundary."""
    if not all(isinstance(v, str) and v.strip() for v in
               (evidence.evidence_id, evidence.tool, evidence.source, evidence.snapshot_id)):
        raise ValueError('missing_provenance')
    if evidence.kind not in ('query', 'statistics', 'definition') or type(evidence.truncated) is not bool:
        raise ValueError('invalid_evidence_kind_or_truncation')
    check_window(evidence.window)
    check_group(evidence.group)
    try:
        json.dumps((evidence.parameters, evidence.sample), allow_nan=False)
    except (TypeError, ValueError):
        raise ValueError('invalid_metadata') from None
    if any(not isinstance(item, str) for item in evidence.limitations):
        raise ValueError('invalid_limitations')
    accepted_types = {'number', 'integer', 'string', 'boolean'}
    if not evidence.columns or any(not isinstance(c, str) or not c or t not in accepted_types
                                   for c, t in evidence.columns.items()):
        raise ValueError('invalid_columns')
    cells: dict[str, Any] = {}
    for index, row in enumerate(evidence.rows):
        if row.keys() != evidence.columns.keys():
            raise ValueError('row_columns_mismatch')
        for column, value in row.items():
            kind = evidence.columns[column]
            matches = value is None or (kind == 'number' and numeric(value)) or (
                kind == 'integer' and type(value) is int) or (kind == 'string' and type(value) is str) or (
                kind == 'boolean' and type(value) is bool)
            if not matches:
                raise ValueError('field_type_mismatch')
            cells[Reference(evidence.evidence_id, index, column).pointer] = value
    for pointer, context in evidence.contexts.items():
        if pointer not in cells or not context.metric.strip():
            raise ValueError('invalid_context_pointer_or_metric')
        check_window(context.window)
        check_group(context.group)
        if context.window[0] < evidence.window[0] or context.window[1] > evidence.window[1]:
            raise ValueError('context_window_outside_result')
        if any(context.group.get(k) != v for k, v in evidence.group.items()):
            raise ValueError('context_group_outside_result')
        if context.comparison is not None and (not isinstance(context.comparison, str) or not context.comparison):
            raise ValueError('invalid_comparison')
    if any(p not in evidence.contexts or not numeric(cells[p]) for p in evidence.whole_population_fields):
        raise ValueError('invalid_whole_population_pointer')


def check_window(window: tuple[str, str]) -> None:
    try:
        if len(window) != 2 or date.fromisoformat(window[0]) >= date.fromisoformat(window[1]):
            raise ValueError()
    except (ValueError, TypeError):
        raise ValueError('invalid_window') from None


def check_group(group: dict[str, str]) -> None:
    if any(not isinstance(k, str) or not k or not isinstance(v, str) or not v for k, v in group.items()):
        raise ValueError('invalid_group')
