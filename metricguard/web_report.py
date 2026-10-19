"""Read-only presentation of an existing publication, with no new analysis rules."""
import html
import json
from typing import Any
from metricguard.readable import render, fact_text
from metricguard.semantic_rubric import digest


def presentation(data: dict, publication: dict) -> dict[str, Any]:
    if publication['evidence_hash'] != digest(data['evidence']):
        return {'available': False, 'message': '报告与当前证据版本不一致，暂不能展示引用。原任务记录已保留。'}
    body, _ = render(data, publication)
    # Transport exact cell text separately: browser JSON numbers cannot preserve large integers.
    evidence = [{**item,
                 'metadata_text': json.dumps({k:v for k,v in item.items() if k!='rows'}, ensure_ascii=False, indent=2),
                 'row_text': [{k:json.dumps(v, ensure_ascii=False, separators=(',',':')) for k,v in row.items()} for row in item['rows']]}
                for item in data['evidence']]
    trace_text = json.dumps({'publication_id': publication['publication_id'],
                            'analysis_result': data.get('analysis_result'),
                            'scope': {key:data.get(key) for key in ('coverage','comparison_coverage','answers')},
                            'trace': data['trace']}, ensure_ascii=False, indent=2)
    return {'available': True, 'body': html.unescape(body),
            'analysis_result': data.get('analysis_result'), 'publication_id': publication['publication_id'],
            'scope': {key: data.get(key) for key in ('original_window','requested_window','actual_window','comparison_window','coverage','comparison_coverage','answers')},
            'facts': [{**a, 'text': html.unescape(fact_text(a))} for a in publication['assertions']],
            'inferences': publication['inferences'], 'evidence': evidence, 'trace_text': trace_text}
