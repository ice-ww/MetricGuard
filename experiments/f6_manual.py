"""Prepare development data and delegate manual checks to the product CLI."""
import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
from uuid import uuid4
from experiments.t01.snapshots import build_snapshot

CASES={
 'A1':('A1','新增用户自然日次日留存出现变化，请检验版本崩溃解释和反对证据。'),
 'A2':('A2','新增用户自然日次日留存与渠道增长、成本变化，请分析。'),
 'A3':('A3','观测完播率变化，请核查采集与行为解释。'),
 'A4':('A4','新增用户自然日次日留存变化，请检验系统结构与分群。'),
 'simple':('normal','查询新增用户数'),
 'clarify':('normal','用户表现怎么样？'),
 'coverage':('insufficient','查询新增用户自然日次日留存'),
 'conflict':('A3','昨天的用户观测完播率发生了很大的变化，请分析一下'),
 'chain':('insufficient','最近7天新增用户自然日次日留存发生变化，请按系统比较。'),
 'empty':('insufficient','昨天新增用户自然日次日留存是多少？'),
}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',choices=list(CASES),default='A1')
    parser.add_argument('--session',type=Path,help='Reuse a session.json path printed by this command')
    parser.add_argument('--task',help='Resume a waiting task in that session')
    parser.add_argument('--question',help='Override the question for a new task')
    parser.add_argument('--prepare-only',action='store_true')
    args=parser.parse_args()
    if args.task and not args.session:parser.error('--task requires --session')
    if args.session:
        session=args.session.resolve();config=json.loads(session.read_text(encoding='utf-8'))
    else:
        image=os.environ.get('METRICGUARD_TEST_IMAGE')
        if not image:parser.error('Set METRICGUARD_TEST_IMAGE to the validated immutable Docker image ID.')
        root=(Path('artifacts/f6-manual')/uuid4().hex).resolve();root.mkdir(parents=True)
        scenario,question=CASES[args.case]
        database=build_snapshot(root/'data',scenario=scenario,seed=280800+list(CASES).index(args.case),
            base_start=datetime(2026,8,3,tzinfo=timezone(timedelta(hours=8)))).database
        config={'state_dir':str(root/'state'),'image':image,'database':str(database.resolve()),'question':question,
                'window':['2026-08-10','2026-08-17'],'case':args.case}
        session=root/'session.json';session.write_text(json.dumps(config,ensure_ascii=False,indent=2),encoding='utf-8')
    print('会话配置（恢复时使用）：'+str(session),flush=True)
    print('日期窗口为起始日包含、结束日不包含；相对日期按实际创建时间解释。',flush=True)
    if args.prepare_only:return
    command=[sys.executable,'-m','metricguard','--state-dir',config['state_dir'],'--image',config['image'],
             '--snapshot','dev='+config['database']]
    if args.task:command+=['resume',args.task]
    else:command+=['chat',args.question or config['question'],'dev','--window',*config['window'],'--mode','diagnose']
    raise SystemExit(subprocess.call(command,env={**os.environ,'PYTHONUTF8':'1'}))


if __name__=='__main__':main()
