"""Independent development instances; never opens the formal registry or snapshots."""
import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
from experiments.t18.freeze import build_case, configuration
from experiments.t20.runner import RealAdapter
from metricguard.evaluation_scoring import score


def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--image',required=True); parser.add_argument('--categories',default='A1,A2,A3,A4')
    args=parser.parse_args(); args.output.mkdir(parents=True,exist_ok=False)
    config=configuration(args.image); adapter=RealAdapter(args.output/'tasks',args.output/'data')
    records=[]
    for index,category in enumerate(args.categories.split(',')):
        recipe={'id':'development-'+str(index),'category':category,'scenario':category if category in ('A1','A2','A3','A4','insufficient') else 'normal',
            'seed':2026001+index,'base_start':(datetime(2026,3,2,tzinfo=timezone(timedelta(hours=8)))+timedelta(days=index*17)).isoformat(),
            'new_version':'9.4','campaign_channel':'development_partner','simple_metric':('users','retained','retention_rate','crashed_users','starts','spend_cents')[index%6]}
        case,reference=build_case(recipe,args.output/'data')
        prepared=adapter.prepare(case['public'],config,case.get('controls',{}))
        pair=[]
        for variant in ('agent','baseline'):
            artifact=adapter.execute(case['public'],prepared['materials'],variant,config)
            artifact['preflight']={**prepared['usage'],'status':prepared['status']}
            record={'category':category,'variant':variant,'artifact':artifact,'score':score(case,artifact)}
            pair.append(record); records.append(record)
            print(json.dumps({'case':index,'category':category,'variant':variant,'score':record['score']},ensure_ascii=False),flush=True)
        (args.output/(recipe['id']+'.json')).write_text(json.dumps({'purpose':'development_only','case':case,
            'reference_agreement':reference,'configuration':config,'preflight':prepared,'records':pair},ensure_ascii=False,indent=2),encoding='utf-8')
    (args.output/'summary.json').write_text(json.dumps({'purpose':'development_only','formal_accesses':0,'configuration':config,
        'results':[{'category':r['category'],'variant':r['variant'],'score':r['score'],'usage':r['artifact']['usage']} for r in records]},
        ensure_ascii=False,indent=2),encoding='utf-8')


if __name__=='__main__': main()
