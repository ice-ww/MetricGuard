"""Real task adapter: public inputs only, with independently audited scoring."""
import argparse
from copy import deepcopy
import json
import os
from pathlib import Path
from uuid import uuid4

from metricguard import TaskService
from metricguard.service import QueryNotDispatched
from metricguard.comparison import protocol_usage
from metricguard.evaluation import EvaluationRunner, file_hash
from metricguard.semantic_rubric import digest


class RealAdapter:
    def __init__(self, root: Path, snapshots: Path, *, transport=None, token=None):
        self.root=Path(root); self.root.mkdir(parents=True,exist_ok=True)
        self.snapshots=Path(snapshots).resolve()
        self.transport=transport
        self.token=token if token is not None else os.environ['ANTHROPIC_AUTH_TOKEN']

    def service(self, public, root, config, hook=None):
        snapshot=(self.snapshots/public['snapshot']).resolve()
        if not snapshot.is_relative_to(self.snapshots): raise ValueError('snapshot escapes root')
        return TaskService(Path(root),config['image'],{public['snapshot_id']:snapshot},token=self.token,
            base_url=config['model']['endpoint'],transport=self.transport,limits=config['budgets'],fault_hook=hook)

    def prepare(self, public, config, controls):
        root=self.root/uuid4().hex
        with self.service(public,root,config) as service:
            prepared=service.prepare_shared(public['question'],public['snapshot_id'],tuple(public['window']))
            state=service.inspect(prepared)
            if state['status']=='waiting' and controls.get('clarification_answer'):
                pending=state['pending_question']
                state=service.answer(prepared,pending['question_id'],pending['version'],controls['clarification_answer'])
            details=state.get('prepared_comparison')
            if details is None:
                from metricguard.comparison import measured_usage
                details={'failed':True,'usage':measured_usage(state['attempts'],state['active'])}
            return {'status':'failed' if details['failed'] else 'ok','usage':protocol_usage(details['usage']),
                'materials':{'prepared':prepared,'service_root':str(root),'controls':deepcopy(controls),
                             'snapshot_file_sha256':state['snapshot_hash']},
                'preflight_task':state}

    def execute(self, public, materials, variant, config):
        fired=False
        def fault(stage):
            nonlocal fired
            if stage=='before_query_dispatch' and not fired and materials['controls'].get('transient_tool_fault_once')=='query_timeout_before_dispatch':
                fired=True
                raise QueryNotDispatched('administrative one-shot timeout before query dispatch')
        with self.service(public,materials['service_root'],config,fault) as service:
            task=service.create_from_shared(materials['prepared'],mode='diagnose' if variant=='agent' else 'baseline')
            service.run(task)
            artifact=service.comparison_result(task)
            state=service.inspect(task)
            artifact['task_trace']=state['trace']
            artifact['task_attempts']=state['attempts']
        # The frozen owner verifies file bytes before prepare. Keep both identities;
        # no query value, context, explanation or scoring answer is rewritten here.
        original_evidence=deepcopy(artifact['evidence'])
        if digest(original_evidence)!=artifact['publication']['evidence_hash']:
            raise ValueError('publication evidence binding mismatch')
        for evidence in artifact['evidence']:
            if evidence['snapshot_id']!=materials['snapshot_file_sha256']:
                raise ValueError('executed evidence snapshot differs from prepared file')
            evidence['snapshot_file_sha256']=evidence['snapshot_id']
            evidence['snapshot_id']=public['snapshot_id']
        artifact['snapshot_identity']={'logical_id':public['snapshot_id'],'file_sha256':materials['snapshot_file_sha256'],
            'binding':'registered public case identity; bytes verified by evaluation owner before preparation'}
        artifact['publication_evidence']=original_evidence
        artifact['evidence_projection']={'original_hash':digest(original_evidence),'projected_hash':digest(artifact['evidence']),
            'publication_id':artifact['publication']['publication_id'],
            'rule':'replace snapshot_id with registered logical identity; retain original as snapshot_file_sha256; all other fields unchanged'}
        return artifact


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--registry',type=Path,required=True)
    parser.add_argument('--snapshots',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--version',required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    owner=EvaluationRunner(args.registry,snapshot_root=args.snapshots)
    adapter=RealAdapter(args.output/'tasks',args.snapshots)
    run=owner.run(args.version,adapter.prepare,adapter.execute,actor='T20 final real model acceptance')
    result=owner.results(run)
    (args.output/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'run_id':run,'complete':result['complete'],'summary':result['summary']},ensure_ascii=False),flush=True)


if __name__=='__main__': main()
