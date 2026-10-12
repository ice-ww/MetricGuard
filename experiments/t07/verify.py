"""Independent arithmetic over persisted provider evidence, not adapter helpers."""
from decimal import Decimal
from typing import Any


def verify_report(report: dict[str, Any]) -> dict[str, Any]:
    cases = {case['name']: case for case in report['cases']}
    checked = []
    for name in ('normal', 'stream_complete'):
        case = cases[name]
        result, ledger = case['result'], case['ledger']
        assert result['status'] == 'completed', name + ' did not complete'
        raw = result['raw_usage']
        uncached = raw['input_tokens'] + (raw.get('cache_creation_input_tokens') or 0)
        cached = raw.get('cache_read_input_tokens') or 0
        total = uncached + cached + raw['output_tokens']
        assert total == ledger['tokens'] == result['usage']['total']
        assert ledger['model_calls'] == 1 and len(ledger['attempts']) == 1
        assert [entry['event'] for entry in ledger['trace']] == ['reserve', 'sent', 'completed']
        peak = (Decimal(uncached) * Decimal('.3') + Decimal(cached) * Decimal('.006')
                + Decimal(raw['output_tokens']) * Decimal('1.2')) / Decimal(1_000_000)
        assert abs(Decimal(str(result['fee_usd_range']['maximum'])) - peak) < Decimal('1e-15')
        assert abs(Decimal(str(result['fee_usd_range']['minimum'])) - peak / 2) < Decimal('1e-15')
        if report['count_probe']['supported']:
            assert uncached + cached == report['count_probe']['input_tokens'], 'observed count differs from actual input'
        checked.append({'case': name, 'input': uncached + cached, 'cached': cached, 'total': total,
                        'peak_fee_usd': str(peak)})
    case = cases['stream_cancelled']
    assert case['result']['status'] == 'unknown_usage'
    assert case['ledger']['attempts'][0]['actual'] is None
    assert case['ledger']['tokens'] == case['result']['reservation'] > 0
    assert case['result']['fee_usd_range'] is None
    assert report['strict_token_cap_verified'] is False
    return {'provider_arithmetic': checked, 'unknown_preserved': True, 'strict_cap': 'not_verified'}
