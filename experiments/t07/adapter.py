"""Anthropic-compatible candidate; token reservation is a scheduling guard only."""
import json
import hashlib
from dataclasses import dataclass, field
from typing import Any, Callable, cast

import anthropic
import httpx2

from experiments.t05 import Ledger


@dataclass(frozen=True)
class Request:
    system: str
    shared: str
    messages: list[dict[str, Any]]
    tools: list[dict[str, Any]] = field(default_factory=list)
    max_output: int = 128

    def payload(self, model: str) -> dict[str, Any]:
        if type(self.max_output) is not int or not 1 <= self.max_output <= 4096:
            raise ValueError('invalid maximum output')
        return dict(model=model, system=self.system + '\n\nShared materials:\n' + self.shared,
                    messages=self.messages, tools=self.tools, max_tokens=self.max_output,
                    extra_body={'thinking': {'type': 'disabled'}, 'temperature': 0})


class ModelAdapter:
    def __init__(self, ledger: Ledger, model: str, base_url: str, token: str,
                 transport: Any = None, timeout: float = 30, report_reserve: int = 1024,
                 fault_hook: Callable[[str], None] | None = None):
        if report_reserve < 1:
            raise ValueError('report reserve must be positive')
        if model != 'deepseek-flash':
            raise ValueError('only the validated deepseek-flash pricing contract is supported')
        self.ledger, self.model, self.report_reserve = ledger, model, report_reserve
        # Administrator-only process-failure injection; never part of a task payload.
        self.fault_hook = fault_hook
        self.client = anthropic.Anthropic(api_key=token, base_url=base_url,
            max_retries=0, timeout=timeout,
            http_client=httpx2.Client(transport=transport, timeout=timeout))

    def close(self) -> None:
        self.client.close()

    def count_input(self, request: Request) -> dict[str, Any]:
        """A count failure never proves a strict cap; does not generate model output."""
        payload = request.payload(self.model)
        for key in ('max_tokens',):
            payload.pop(key)
        try:
            result = self.client.messages.count_tokens(**payload)
            return {'supported': True, 'input_tokens': result.input_tokens,
                    'strict_bound': False, 'reason': 'count is not a provider-enforced cumulative cap'}
        except Exception as error:
            return {'supported': False, 'error_type': type(error).__name__, 'strict_bound': False}

    def call(self, task: str, operation: str, request: Request, *, attempt_id: str,
             stream: bool = False, cancel_after_events: int | None = None,
             final_report: bool = False) -> dict[str, Any]:
        payload = request.payload(self.model)
        fingerprint = hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        operation = operation + ':' + fingerprint
        # Includes all serialized input fields; bytes are intentionally NOT called a token upper bound.
        estimated_input = len(json.dumps(payload, ensure_ascii=False).encode('utf-8'))
        reserved = estimated_input + request.max_output
        snapshot = self.ledger.inspect(task)
        existing = next((a for a in snapshot['attempts'] if a['id'] == attempt_id), None)
        if existing:
            if existing['operation'] != operation or existing['reserved'] != reserved:
                raise ValueError('attempt identity conflict')
            if existing['state'] in ('completed', 'failed'):
                return json.loads(existing['result'])
            raise ValueError('attempt outcome unresolved; cannot resend')
        if any(a['actual'] is None for a in snapshot['attempts'] if a['kind'] == 'model'):
            raise ValueError('unknown usage blocks further model dispatch')
        if not final_report and (snapshot['tokens'] + reserved + self.report_reserve > snapshot['limits']['tokens']
                                 or snapshot['model_calls'] + 1 >= snapshot['limits']['model']):
            raise ValueError('final report budget reserved')
        self.ledger.reserve(task, operation, 'model', reserved, attempt_id,
                            headroom_tokens=0 if final_report else self.report_reserve,
                            headroom_calls=0 if final_report else 1)
        if self.fault_hook:
            self.fault_hook('after_reserve')
        self.ledger.mark_sent(attempt_id)
        result: dict[str, Any]
        try:
            if stream:
                with self.client.messages.stream(**payload) as events:
                    for index, _ in enumerate(events):
                        if cancel_after_events is not None and index + 1 >= cancel_after_events:
                            raise InterruptedError('caller cancelled stream')
                    message = events.get_final_message()
            else:
                message = self.client.messages.create(**payload)
            raw = message.model_dump(mode='json')
            usage = normalize_usage(raw.get('usage'))
            result = {'status': 'completed' if usage else 'unknown_usage', 'model': raw.get('model'),
                      'content': raw.get('content'), 'raw_usage': raw.get('usage'), 'usage': usage,
                      'reservation': reserved, 'cap': 'scheduler_guard',
                      'fee_usd_range': fee_range(usage) if usage else None}
            self.ledger.settle(attempt_id, result, usage['total'] if usage else None, failed=usage is None)
        except Exception as error:
            result = {'status': 'unknown_usage', 'error_type': type(error).__name__,
                      'usage': None, 'fee_usd_range': None, 'reservation': reserved,
                      'cap': 'scheduler_guard'}
            self.ledger.settle(attempt_id, result, failed=True)
        if self.fault_hook:
            self.fault_hook('after_result')
        return result


def normalize_usage(raw: Any) -> dict[str, int] | None:
    if not isinstance(raw, dict):
        return None
    fields = ('input_tokens', 'output_tokens', 'cache_creation_input_tokens', 'cache_read_input_tokens')
    values = [raw.get(key, 0) if key not in fields[:2] else raw.get(key) for key in fields]
    values = [0 if value is None and index >= 2 else value for index, value in enumerate(values)]
    if any(type(value) is not int or value < 0 for value in values):
        return None
    uncached, output, created, cached = cast(list[int], values)
    return {'input_uncached': uncached + created, 'input_cached': cached,
            'input_total': uncached + created + cached, 'output': output,
            'total': uncached + created + cached + output}


def fee_range(usage: dict[str, int]) -> dict[str, Any]:
    peak = (usage['input_uncached'] * .3 + usage['input_cached'] * .006 + usage['output'] * 1.2) / 1_000_000
    return {'minimum': peak / 2, 'maximum': peak, 'currency': 'USD',
            'kind': 'estimate_not_invoice', 'pricing': 'DeepSeek-V4.1-Flash 2026-10-12'}
