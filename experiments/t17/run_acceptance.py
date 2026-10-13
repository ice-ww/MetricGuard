"""Actual isolated query + independent reference + controlled report counterexamples."""
import argparse
from dataclasses import asdict
import json
from pathlib import Path
from typing import Any
import httpx2 as httpx
from experiments.t01.snapshots import build_snapshot
from experiments.t08.contract import Reference
from experiments.t15.reference import reference
from metricguard import TaskService
from metricguard.semantic_rubric import RUBRIC,RUBRIC_HASH


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--image',required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    snap=build_snapshot(args.output/'data',scenario='A4',seed=1701)
    actions=iter([{'action':'profile','table':'users','column':'registration_os','kind':'system_retention'},
                  {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]}])
    def provider(request):
        return httpx.Response(200,json={'id':'t17','type':'message','role':'assistant','model':'deepseek-flash',
            'content':[{'type':'text','text':json.dumps(next(actions))}], 'stop_reason':'end_turn','stop_sequence':None,
            'usage':{'input_tokens':31,'output_tokens':17}})
    with TaskService(args.output/'service',args.image,{'dev':snap.database},token='controlled',transport=httpx.MockTransport(provider)) as service:
        task=service.create('新增用户自然日次日留存，分析系统结构变化','dev',('2026-01-08','2026-01-15'),mode='diagnose')
        result=service.run(task)
        expected=reference(snap.database,*result['actual_window'])
        e=result['evidence'][0]
        assert e['rows']==expected['rows']
        facts=[]
        for i,row in enumerate(e['rows']):
            for col in ('users','retained','retention_rate'):
                ref=Reference(e['evidence_id'],i,col)
                facts.append({'assertion_id':f'{i}:{col}','reference':asdict(ref),'context':e['contexts'][ref.pointer],'value':row[col],'scope':'cell'})
        android=[f['assertion_id'] for f in facts if e['rows'][f['reference']['row']]['registration_os']=='Android']
        ios=[f['assertion_id'] for f in facts if e['rows'][f['reference']['row']]['registration_os']=='iOS']
        charts=[]
        for period in ('previous','current'):
            indices=[i for i,r in enumerate(e['rows']) if r['period']==period]
            charts.append({'chart_id':period,'kind':'bar','x_refs':[asdict(Reference(e['evidence_id'],i,'registration_os')) for i in indices],
                           'y_refs':[asdict(Reference(e['evidence_id'],i,'retention_rate')) for i in indices]})
        cases=[('bounded','Android留存下降，iOS的留存及用户结构提供对照；与系统结构掩盖分群恶化的描述性候选相符，尚未排除渠道与版本变化。',android,ios),
               ('irrelevant','基期iOS新增人数证明Android崩溃是留存下降原因。',[next(f['assertion_id'] for f in facts if f['assertion_id'] in ios and f['reference']['column']=='users' and e['rows'][f['reference']['row']]['period']=='previous')],[]),
               ('ignored_counterevidence','Android留存下降，因此本期所有系统留存都下降。',android,[]),
               ('causal_overclaim','这些留存与人数已经证明：系统结构调整是留存变化的唯一确定原因。',android,ios)]
        records: list[dict[str,Any]]=[]
        for name,text,support,opposition in cases:
            draft={'assertions':facts,'inferences':[{'inference_id':name,'text':text,'supporting_assertion_ids':support,
                'opposing_assertion_ids':opposition,'unexcluded_factors':['渠道与版本构成未排除'] if name=='bounded' else []}],'charts':charts}
            publication=service.publish_report(task,draft)
            assert publication['status']=='mechanically_valid' and publication['semantic_status']=='pending_review'
            for chart in publication['charts']:
                (args.output/(chart['chart_id']+'.svg')).write_text(chart['svg'],encoding='utf-8')
                for point,refs in zip(chart['points'],chart['references'],strict=True):
                    assert point==[e['rows'][ref['row']][ref['column']] for ref in refs]
            records.append({'case':name,'publication':publication})
        assert service.inspect(task)['tool_calls']==result['tool_calls']
        payload={'purpose':'development counterexamples, not frozen cases','image':args.image,'task':task,
                 'database':str(snap.database.resolve()),'service_root':str((args.output/'service').resolve()),
                 'result':result,'independent_reference':expected,'rubric':RUBRIC,'rubric_hash':RUBRIC_HASH,'cases':records}
        (args.output/'result.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
        lines=['# T17 人工语义复核材料','',f'Rubric: semantic-v1 / {RUBRIC_HASH}',
            '','以下四份受控报告均通过机械校验；这不代表推断合理。请按相关性、关键反证、因果克制三个维度各评0/1/2，并给理由。',
            '','| 窗口 | 系统 | 新增 | 次日留存人数 | 留存率 |','| --- | --- | ---: | ---: | ---: |']
        for row in e['rows']:
            lines.append(f"| {row['period']} | {row['registration_os']} | {row['users']} | {row['retained']} | {row['retention_rate']:.4%} |")
        lines += ['', '数据来自实际隔离SQL，并以原始用户/会话集合独立核对；没有崩溃数据或因果识别实验。']
        for r in records:
            p=r['publication']; inf=p['inferences'][0]
            lines += ['',f"## {r['case']}",inf['text'],f"支持断言：{inf['supporting_assertion_ids']}",f"反对/对照断言：{inf['opposing_assertion_ids']}",f"发布版本：{p['publication_id']}"]
        lines += ['', '建议评分（待人类核对，不是已完成人工评分）：bounded=2/2/2；irrelevant=0/0/0；ignored_counterevidence=1/0/2；causal_overclaim=1/1/0。',
            '理由：有效例保持描述性关联并保留对照及未排除项；无关例用iOS人数解释未观测的崩溃；遗漏例把Android变化外推到与之不符的iOS；因果例缺少因果识别却断言唯一原因。']
        (args.output/'human-review.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({'passed_mechanical_cases':4,'facts_checked':len(facts),'charts_per_report':2,'human_review':'pending'}))


if __name__=='__main__':
    main()
