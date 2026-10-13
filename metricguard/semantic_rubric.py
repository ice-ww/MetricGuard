"""Shared T17/T18 review contract; scores must come from an identified reviewer."""
import hashlib
import json

RUBRIC = {
    'version': 'semantic-v1',
    'dimensions': {
        'relevance': {'0': '引用与推断无关或方向矛盾', '1': '部分相关但关键支持不足', '2': '引用对准指标、分群、窗口与推断，独立口径已核验'},
        'counterevidence': {'0': '忽略已取得的关键反证', '1': '提及反证但未解释其影响', '2': '评估关键反证及未排除因素；若无反证说明检索范围'},
        'causal_restraint': {'0': '观察关联宣称确定因果', '1': '有不确定措辞但仍过度归因', '2': '结论强度与证据相称，明确关联及因果识别限制'},
    },
    'pass_rule': '每项推断三个维度均为2且每维有解释；缺评分为pending，不按零计成功。',
    'review_boundary': '字段、引用存在和关键词均不证明语义正确；早期验收人工评分，非每次线上审批。',
}


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,allow_nan=False,separators=(',',':')).encode()).hexdigest()


RUBRIC_HASH = digest(RUBRIC)


def validate_review(inference_ids: set[str], reviewer: str, reviewer_kind: str, ratings: list[dict]) -> dict:
    if not isinstance(reviewer,str) or not reviewer.strip() or reviewer_kind not in ('human','agent'):
        raise ValueError('identified reviewer required')
    if not inference_ids or not isinstance(ratings,list) or len(ratings)!=len(inference_ids):
        raise ValueError('all inferences require review')
    seen=set()
    for rating in ratings:
        if not isinstance(rating,dict) or set(rating)!={'inference_id','scores','reasons'}:
            raise ValueError('invalid semantic rating')
        identity=rating['inference_id']
        if not isinstance(identity,str) or identity not in inference_ids or identity in seen:
            raise ValueError('unknown or duplicate inference rating')
        seen.add(identity)
        for key in ('scores','reasons'):
            if not isinstance(rating[key],dict) or set(rating[key])!=set(RUBRIC['dimensions']):
                raise ValueError('all rubric dimensions required')
        if any(type(v) is not int or v not in (0,1,2) for v in rating['scores'].values()):
            raise ValueError('invalid score')
        if any(not isinstance(v,str) or not v.strip() for v in rating['reasons'].values()):
            raise ValueError('reason required per dimension')
    return {'rubric_version':RUBRIC['version'],'rubric_hash':RUBRIC_HASH,'reviewer':reviewer,
            'reviewer_kind':reviewer_kind,'ratings':ratings,
            'status':('passed' if all(v==2 for r in ratings for v in r['scores'].values()) else 'failed') if reviewer_kind=='human' else 'advisory_only'}
