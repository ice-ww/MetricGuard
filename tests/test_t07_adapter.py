"""Provider-boundary checks with real SDK, SQLite ledger, independent wire fixtures."""
import json
import pytest

import httpx2 as httpx

from experiments.t05 import Ledger
from experiments.t07 import ModelAdapter, Request


def test_real_sdk_settles_wire_usage_and_replay_does_not_send(tmp_path):
    sent = []

    def provider(request):
        sent.append(json.loads(request.content))
        return httpx.Response(200, json={
            'id': 'msg_fixture', 'type': 'message', 'role': 'assistant',
            'model': 'deepseek-flash', 'content': [{'type': 'text', 'text': 'OK'}],
            'stop_reason': 'end_turn', 'stop_sequence': None,
            'usage': {'input_tokens': 11, 'output_tokens': 3,
                      'cache_read_input_tokens': 5, 'cache_creation_input_tokens': 0},
        })

    ledger = Ledger(tmp_path / 'ledger.sqlite')
    task = ledger.create_task()
    adapter = ModelAdapter(ledger, 'deepseek-flash', 'https://fixture.invalid', 'fixture',
                           transport=httpx.MockTransport(provider))
    request = Request(system='system', shared='shared', messages=[{'role': 'user', 'content': 'hello'}],
                      tools=[{'name': 'lookup', 'description': 'lookup', 'input_schema': {'type': 'object'}}])
    first = adapter.call(task, 'op', request, attempt_id='first')
    replay = adapter.call(task, 'op', request, attempt_id='first')
    assert first == replay
    assert len(sent) == 1
    assert sent[0]['system'] == 'system\n\nShared materials:\nshared'
    assert sent[0]['tools'][0]['name'] == 'lookup'
    assert ledger.inspect(task)['tokens'] == 19  # Anthropic input excludes cache: 11 + 5 + 3.
    assert first['usage']['input_total'] == 16
    changed = Request(system='system', shared='shared', messages=[{'role': 'user', 'content': 'world'}], tools=request.tools)
    with pytest.raises(ValueError, match='identity conflict'):
        adapter.call(task, 'op', changed, attempt_id='first')


@pytest.mark.parametrize('fault', ['timeout', 'server_error', 'missing_usage'])
def test_unknown_usage_holds_reservation_and_prevents_more_sends(tmp_path, fault):
    wire = []
    def provider(request):
        wire.append(request)
        if fault == 'timeout':
            raise httpx.ReadTimeout('controlled timeout')
        if fault == 'server_error':
            return httpx.Response(503, json={'error': {'type': 'overloaded_error', 'message': 'controlled'}})
        return httpx.Response(200, json={'id': 'msg_x', 'type': 'message', 'role': 'assistant',
            'model': 'deepseek-flash', 'content': [], 'stop_reason': 'end_turn', 'stop_sequence': None})
    ledger = Ledger(tmp_path / 'ledger.sqlite')
    task = ledger.create_task()
    adapter = ModelAdapter(ledger, 'deepseek-flash', 'https://fixture.invalid', 'fixture',
                           transport=httpx.MockTransport(provider))
    request = Request('system', 'materials', [{'role': 'user', 'content': 'hello'}])
    result = adapter.call(task, 'one', request, attempt_id='one')
    assert result['status'] == 'unknown_usage'
    assert ledger.inspect(task)['tokens'] == result['reservation'] > 128
    assert result['fee_usd_range'] is None
    with pytest.raises(ValueError, match='unknown usage'):
        adapter.call(task, 'two', request, attempt_id='two')
    assert len(wire) == 1  # SDK's default automatic retries must be disabled.


def test_report_headroom_and_call_limit_are_enforced(tmp_path):
    ledger = Ledger(tmp_path / 'ledger.sqlite')
    task = ledger.create_task(limits={'model': 1})
    adapter = ModelAdapter(ledger, 'deepseek-flash', 'https://fixture.invalid', 'fixture')
    with pytest.raises(ValueError, match='report budget'):
        adapter.call(task, 'one', Request('s', 'm', [{'role': 'user', 'content': 'x'}]), attempt_id='one')
    assert ledger.inspect(task)['model_calls'] == 0


def test_stream_cancel_keeps_unknown_and_complete_stream_accounts_reasoning_once(tmp_path):
    events = [
        ('message_start', {'type': 'message_start', 'message': {'id': 'msg_stream', 'type': 'message',
            'role': 'assistant', 'model': 'deepseek-flash', 'content': [], 'stop_reason': None,
            'stop_sequence': None, 'usage': {'input_tokens': 12, 'output_tokens': 0}}}),
        ('content_block_start', {'type': 'content_block_start', 'index': 0, 'content_block': {'type': 'text', 'text': ''}}),
        ('content_block_delta', {'type': 'content_block_delta', 'index': 0, 'delta': {'type': 'text_delta', 'text': 'OK'}}),
        ('content_block_stop', {'type': 'content_block_stop', 'index': 0}),
        ('message_delta', {'type': 'message_delta', 'delta': {'stop_reason': 'end_turn', 'stop_sequence': None},
            'usage': {'output_tokens': 8, 'reasoning_tokens': 5}}),
        ('message_stop', {'type': 'message_stop'}),
    ]
    wire = '\n\n'.join('event: ' + name + '\ndata: ' + json.dumps(value) for name, value in events) + '\n\n'
    ledger = Ledger(tmp_path / 'ledger.sqlite')
    adapter = ModelAdapter(ledger, 'deepseek-flash', 'https://fixture.invalid', 'fixture',
        transport=httpx.MockTransport(lambda r: httpx.Response(200, text=wire, headers={'content-type': 'text/event-stream'})))
    request = Request('s', 'm', [{'role': 'user', 'content': 'hello'}])
    task = ledger.create_task()
    result = adapter.call(task, 'cancel', request, attempt_id='cancel', stream=True, cancel_after_events=1)
    assert result['status'] == 'unknown_usage'
    assert ledger.inspect(task)['tokens'] == result['reservation']
    task = ledger.create_task()
    result = adapter.call(task, 'complete', request, attempt_id='complete', stream=True)
    assert result['status'] == 'completed'
    assert ledger.inspect(task)['tokens'] == 20  # output 8 already contains any reasoning; never add 5 again.
