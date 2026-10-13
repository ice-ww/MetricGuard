"""Run registered development data through the public service, controlled or real."""
import argparse
import json
import os
from pathlib import Path
import httpx2 as httpx
from metricguard import TaskService
from experiments.t15.check_result import check


def provider():
    actions=iter([{'action':'profile','table':'users','column':'registration_os','kind':'system_retention'},
                  {'action':'stop','unsupported_hypotheses':[],'unresolved_questions':[]}])
    def respond(request):
        return httpx.Response(200,json=dict(id='controlled',type='message',role='assistant',model='deepseek-flash',
            content=[dict(type='text',text=json.dumps(next(actions)))],stop_reason='end_turn',stop_sequence=None,
            usage=dict(input_tokens=31,output_tokens=17)))
    return respond


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--manifest',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--image',required=True)
    parser.add_argument('--real',action='store_true')
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    manifest=json.loads(args.manifest.read_text(encoding='utf-8'))
    records=[]
    for case in manifest['cases']:
        with TaskService(args.output/case['case'],args.image,{'dev':Path(case['database'])},
                         token=os.environ['ANTHROPIC_AUTH_TOKEN'] if args.real else 'controlled',
                         transport=None if args.real else httpx.MockTransport(provider())) as service:
            result=service.run(service.create('新增用户自然日次日留存，分析系统占比变化是否掩盖分群恶化',
                'dev',(case['current_start'],case['end']),mode='diagnose'))
        path=args.output/(case['case']+'.json')
        path.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
        validation=check(result,Path(case['database']))
        assert validation['diagnosis_status']==('no_supported_candidate' if case['case']=='normal' else 'association_candidate')
        records.append(dict(case=case['case'],result=result,validation=validation))
        print(json.dumps(dict(case=case['case'],**validation)),flush=True)
    (args.output/'results.json').write_text(json.dumps(dict(real=args.real,image=args.image,records=records),ensure_ascii=False,indent=2),encoding='utf-8')


if __name__=='__main__':
    main()
