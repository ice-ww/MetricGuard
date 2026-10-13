"""Playback collection contract through public TaskService and real SQL."""
import json
import httpx2 as httpx
from experiments.t01.snapshots import build_snapshot
from metricguard import TaskService
from tests.test_t09_service import image, response


def controlled(request):
    shared = json.loads(json.loads(request.content)['system'].split('Shared materials:\n')[1])
    kinds = [e['source']['kind'] for e in shared['evidence']]
    for table, kind in [('content_events', 'playback_events'), ('playback_telemetry', 'playback_progress')]:
        if kind not in kinds:
            return response({'action': 'profile', 'table': table, 'column': 'play_id', 'kind': kind})
    return response({'action': 'stop', 'unsupported_hypotheses': [], 'unresolved_questions': []})


def run(tmp_path, image, snapshot):
    with TaskService(tmp_path / 'service', image, {'dev': snapshot.database}, token='controlled', transport=httpx.MockTransport(controlled)) as service:
        return service.run(service.create('完播率', 'dev', ('2026-01-08', '2026-01-15'), mode='diagnose'))


def test_independent_completion_supports_collection_candidate(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A3', seed=1414)
    result = run(tmp_path, image, snapshot)
    assert result['outcome'] == 'facts_available', result['limitations']
    diagnosis = result['report']['diagnosis']
    assert diagnosis['status'] == 'association_candidate'
    candidate = diagnosis['candidates'][0]
    assert candidate['group'] == {'actual_os': 'Android', 'actual_version': '2.0'}
    assert candidate['causality'] == 'not_established'
    assert candidate['supporting_facts'] and candidate['counterevidence']
    assert diagnosis['statistical_limitations']


def test_invalid_progress_does_not_publish_independent_completion(tmp_path, image):
    import duckdb
    snapshot = build_snapshot(tmp_path / 'data', scenario='A3', seed=1414)
    with duckdb.connect(str(snapshot.database)) as con:
        con.execute("UPDATE playback_telemetry SET session_id='orphan-session'")
    result = run(tmp_path, image, snapshot)
    diagnosis = result['report']['diagnosis']
    assert diagnosis['status'] == 'insufficient_evidence'
    assert not diagnosis['candidates']
    assert all(m['independent_complete'] == 0 and m['missing_completion'] is None for m in diagnosis['playback_metrics'])

import pytest
import duckdb

@pytest.mark.parametrize('case', ['missing', 'incomplete', 'conflicting_start', 'invalid_progress', 'null_version', 'null_os', 'null_started_at', 'empty'])
def test_quality_gates_do_not_confuse_missing_evidence_with_behavior(tmp_path, image, case):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A3', seed=1414)
    with duckdb.connect(str(snapshot.database)) as con:
        if case == 'missing':
            con.execute('DELETE FROM playback_telemetry')
        elif case == 'incomplete':
            con.execute("UPDATE source_watermarks SET complete_before='2026-01-10T00:00:00+08:00' WHERE source='playback_telemetry'")
        elif case == 'conflicting_start':
            con.execute("INSERT INTO content_events SELECT event_id || '-conflict',play_id,session_id,event_type,occurred_at + INTERVAL 1 SECOND FROM content_events WHERE event_type='start' LIMIT 1")
        elif case == 'invalid_progress':
            con.execute('UPDATE playback_telemetry SET watched_seconds=duration_seconds+1')
        elif case.startswith('null_'):
            con.execute('UPDATE sessions SET ' + case.removeprefix('null_') + '=NULL')
        elif case == 'empty':
            con.execute('DELETE FROM content_events'); con.execute('DELETE FROM playback_telemetry')
    result = run(tmp_path, image, snapshot)
    diagnosis = result['report']['diagnosis']
    assert diagnosis['status'] == 'insufficient_evidence'
    assert not diagnosis['candidates']
    assert diagnosis['missing_evidence']
    assert all(m['missing_completion'] is None for m in diagnosis['playback_metrics'])

@pytest.mark.parametrize('source', ['playback_telemetry', 'content_events'])
def test_reports_beyond_source_cutoff_are_not_missing_event_evidence(tmp_path, image, source):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A3', seed=1414)
    with duckdb.connect(str(snapshot.database)) as con:
        if source == 'playback_telemetry':
            con.execute("UPDATE playback_telemetry SET observed_at='2026-01-20T00:00:00+08:00'")
        else:
            con.execute("UPDATE content_events SET occurred_at='2026-01-20T00:00:00+08:00' WHERE event_type='complete'")
    result = run(tmp_path, image, snapshot)
    diagnosis = result['report']['diagnosis']
    assert diagnosis['status'] == 'insufficient_evidence'
    assert not diagnosis['candidates']
    assert all(m['missing_completion'] is None for m in diagnosis['playback_metrics'])


def test_effective_progress_is_not_completion_and_repeat_plays_survive(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='normal', seed=1414)
    with duckdb.connect(str(snapshot.database)) as con:
        con.execute('UPDATE playback_telemetry SET watched_seconds=10')
        expected = con.execute("SELECT COUNT(DISTINCT play_id) FROM content_events WHERE event_type='start' AND occurred_at>='2026-01-01T00:00:00+08:00' AND occurred_at<'2026-01-15T00:00:00+08:00'").fetchone()[0]
    result = run(tmp_path, image, snapshot)
    metrics = result['report']['diagnosis']['playback_metrics']
    assert sum(m['starts'] for m in metrics) == expected
    assert sum(m['effective'] for m in metrics) == expected
    assert all(m['independent_complete'] == 0 for m in metrics)
    assert not result['report']['diagnosis']['candidates']
    for fact in result['report']['facts']:
        assert fact['context']['window'] in [['2026-01-01', '2026-01-08'], ['2026-01-08', '2026-01-15']]


def test_completion_after_event_cutoff_is_not_yet_missing(tmp_path, image):
    snapshot = build_snapshot(tmp_path / 'data', scenario='A3', seed=1414)
    with duckdb.connect(str(snapshot.database)) as con:
        con.execute("INSERT INTO sessions VALUES ('edge-session','edge-user','2026-01-14T23:59:00+08:00','Android','edge',FALSE)")
        con.execute("INSERT INTO content_events VALUES ('edge-start','edge-play','edge-session','start','2026-01-14T23:59:00+08:00')")
        con.execute("INSERT INTO playback_telemetry VALUES ('edge-telemetry','edge-play','edge-session','2026-01-15T00:01:00+08:00',120,120)")
        con.execute("UPDATE source_watermarks SET complete_before='2026-01-15T00:00:00+08:00' WHERE source='content_events'")
    result = run(tmp_path, image, snapshot)
    diagnosis = result['report']['diagnosis']
    assert diagnosis['status'] == 'insufficient_evidence'
    assert 'progress_beyond_complete_source' in diagnosis['missing_evidence']
    assert not diagnosis['candidates']
    assert all(m['missing_completion'] is None for m in diagnosis['playback_metrics'])
