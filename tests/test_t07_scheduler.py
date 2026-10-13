"""Accepted scheduling contract, observed at the HTTP and durable ledger boundaries."""
import pytest
import httpx2 as httpx

from experiments.t05 import Ledger
from experiments.t07 import ModelAdapter, Request


REQUEST = Request('system', 'shared', [{'role': 'user', 'content': 'OK'}])


def response(input_tokens=11):
    return httpx.Response(200, json={
        'id': 'msg_budget', 'type': 'message', 'role': 'assistant',
        'model': 'deepseek-flash', 'content': [{'type': 'text', 'text': 'OK'}],
        'stop_reason': 'end_turn', 'stop_sequence': None,
        'usage': {'input_tokens': input_tokens, 'output_tokens': 1},
    })


def test_actual_overrun_is_recorded_and_blocks_further_dispatch(tmp_path):
    ledger = Ledger(tmp_path / 'ledger.sqlite')
    task = ledger.create_task()
    sends = []

    def provider(request):
        # The independent transport sees the reservation before receiving a response.
        snapshot = Ledger(ledger.path).inspect(task)
        assert snapshot['model_calls'] == 1
        assert snapshot['attempts'][0]['state'] == 'sent'
        assert snapshot['attempts'][0]['actual'] is None
        assert snapshot['tokens'] >= REQUEST.max_output
        sends.append(request)
        return response(30000)

    adapter = ModelAdapter(ledger, 'deepseek-flash', 'https://fixture.invalid', 'fixture',
                           transport=httpx.MockTransport(provider))
    try:
        result = adapter.call(task, 'first', REQUEST, attempt_id='first')
        assert result['cap'] == 'scheduler_guard'
        assert ledger.inspect(task)['tokens'] == 30001  # Independent wire fixture: 30000 + 1.
        assert ledger.inspect(task)['attempts'][0]['actual'] == 30001
        for final in (False, True):
            with pytest.raises(ValueError, match='budget'):
                adapter.call(task, 'next', REQUEST, attempt_id='next', final_report=final)
        assert len(sends) == 1
    finally:
        adapter.close()


@pytest.mark.parametrize('limits', [{'tokens': 1024}, {'model': 1}])
def test_report_headroom_is_unavailable_to_normal_calls_but_report_can_use_it(tmp_path, limits):
    ledger = Ledger(tmp_path / 'ledger.sqlite')
    task = ledger.create_task(limits=limits)
    sends = []

    def provider(request):
        sends.append(request)
        return response()

    adapter = ModelAdapter(ledger, 'deepseek-flash', 'https://fixture.invalid', 'fixture',
                           transport=httpx.MockTransport(provider))
    try:
        with pytest.raises(ValueError, match='report budget'):
            adapter.call(task, 'normal', REQUEST, attempt_id='normal')
        assert sends == []
        assert ledger.inspect(task)['model_calls'] == 0
        result = adapter.call(task, 'report', REQUEST, attempt_id='report', final_report=True)
        assert result['status'] == 'completed'
        assert ledger.inspect(task)['tokens'] == 12
        assert len(sends) == 1
        if 'model' in limits:
            with pytest.raises(ValueError, match='budget'):
                adapter.call(task, 'another', REQUEST, attempt_id='another', final_report=True)
            assert len(sends) == 1
    finally:
        adapter.close()


def test_unknown_usage_survives_reopening_and_blocks_even_final_report(tmp_path):
    path = tmp_path / 'ledger.sqlite'
    ledger = Ledger(path)
    task = ledger.create_task()
    sends = []

    def provider(request):
        sends.append(request)
        raise httpx.ReadTimeout('controlled timeout')

    adapter = ModelAdapter(ledger, 'deepseek-flash', 'https://fixture.invalid', 'fixture',
                           transport=httpx.MockTransport(provider))
    try:
        result = adapter.call(task, 'first', REQUEST, attempt_id='first')
    finally:
        adapter.close()

    reopened = Ledger(path)
    adapter = ModelAdapter(reopened, 'deepseek-flash', 'https://fixture.invalid', 'fixture',
                           transport=httpx.MockTransport(provider))
    try:
        assert reopened.inspect(task)['tokens'] == result['reservation'] > 0
        assert reopened.inspect(task)['attempts'][0]['actual'] is None
        assert result['fee_usd_range'] is None
        assert adapter.call(task, 'first', REQUEST, attempt_id='first') == result
        for final in (False, True):
            with pytest.raises(ValueError, match='unknown usage'):
                adapter.call(task, 'retry', REQUEST, attempt_id='retry', final_report=final)
        assert len(sends) == 1
    finally:
        adapter.close()


def test_default_ten_call_limit_preserves_last_call_for_report(tmp_path):
    ledger = Ledger(tmp_path / 'ten.sqlite')
    task = ledger.create_task()
    sends = []

    def provider(request):
        sends.append(request)
        return response()

    adapter = ModelAdapter(ledger, 'deepseek-flash', 'https://fixture.invalid', 'fixture',
                           transport=httpx.MockTransport(provider))
    try:
        for index in range(9):
            adapter.call(task, 'normal', REQUEST, attempt_id=str(index))
        with pytest.raises(ValueError, match='report budget'):
            adapter.call(task, 'normal', REQUEST, attempt_id='tenth-normal')
        adapter.call(task, 'report', REQUEST, attempt_id='report', final_report=True)
        with pytest.raises(ValueError, match='budget'):
            adapter.call(task, 'extra', REQUEST, attempt_id='extra', final_report=True)
        assert len(sends) == ledger.inspect(task)['model_calls'] == 10
        assert ledger.inspect(task)['tokens'] == 120  # Ten independent 11+1 fixtures.
    finally:
        adapter.close()
