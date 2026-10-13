"""Audited evaluation owner. Adapters receive public inputs, never expected answers."""
from copy import deepcopy
from contextlib import contextmanager
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import time
from uuid import uuid4
from metricguard.evaluation_scoring import score,usage
from metricguard.semantic_rubric import RUBRIC_HASH,digest

COUNTS={'simple':6,'A1':3,'A2':3,'A3':3,'A4':3,'normal':2,'insufficient':2,'clarification':1,'recovery':1}


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_json(value,depth=0,ancestors=None):
    """Preserve invalid adapter material as explicit JSON diagnostics, never silence it."""
    ancestors=set() if ancestors is None else ancestors
    if depth>50 or id(value) in ancestors: return {'invalid_value':'circular_or_too_deep'}
    path=ancestors|{id(value)}
    if isinstance(value,dict): return {str(k):safe_json(v,depth+1,path) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [safe_json(v,depth+1,path) for v in value]
    try:
        json.dumps(value,allow_nan=False)
        return value
    except (TypeError,ValueError):
        return {'invalid_value':repr(value) if isinstance(value,float) else type(value).__name__}


def failure_usage(raw,elapsed: float) -> dict:
    try:
        return deepcopy(usage(raw['usage']))
    except (KeyError,ValueError,TypeError,AttributeError,OverflowError):
        return {'seconds':elapsed,'steps':None,'model_calls':None,'tokens':None,'cost':None}


def summarize(records: list[dict], formal: bool) -> dict:
    summaries=[]
    for variant in sorted({r['variant'] for r in records}):
        for round_no in sorted({r['round'] for r in records}):
            rows=[r for r in records if r['variant']==variant and r['round']==round_no]
            scores=[r['score'] for r in rows]; core=[s for s in scores if s['category'] in ('A1','A2','A3','A4')]
            facts=sum(s['assertion_count'] for s in scores); valid=sum(s['valid_assertion_count'] for s in scores)
            required=sum(s['required_count'] for s in scores); matched=sum(s['matched_count'] for s in scores)
            inference=sum(s['inference_count'] for s in scores); cited=sum(s['citation_count'] for s in scores)
            times=sorted(r['artifact']['usage']['seconds'] for r in rows)
            def percentile(p):
                if not times: return None
                index=(len(times)-1)*p; lo=int(index); hi=min(lo+1,len(times)-1)
                return times[lo]+(times[hi]-times[lo])*(index-lo)
            costs=[r['artifact'][phase]['cost'] for r in rows for phase in ('preflight','usage')]
            tokens=[r['artifact'][phase]['tokens'] for r in rows for phase in ('preflight','usage')]
            gate=(formal and len(rows)==24 and all(sum(s['category']==k for s in scores)==v for k,v in COUNTS.items())
                and all(s['complete_pass'] for s in scores if s['category'] not in ('A1','A2','A3','A4'))
                and sum(s['complete_pass'] for s in core)>=9
                and all(any(s['category']==k and s['complete_pass'] for s in core) for k in ('A1','A2','A3','A4'))
                and facts>0 and facts==valid and inference==cited
                and all(r['artifact']['safety_passed'] is True for r in rows))
            summaries.append({'variant':variant,'round':round_no,'tasks':len(rows),'complete_passes':sum(s['complete_pass'] for s in scores),
                'complete_pass_rate':sum(s['complete_pass'] for s in scores)/len(rows) if rows else None,
                'attribution_hits':sum(s['attribution_hit'] for s in core),'attribution_denominator':len(core),
                'attribution_hit_rate':sum(s['attribution_hit'] for s in core)/len(core) if core else None,
                'assertions':facts,'valid_assertions':valid,'assertion_pass_rate':valid/facts if facts else None,
                'required_assertions':required,'matched_reference_assertions':matched,'reference_match_rate':matched/required if required else None,
                'citation_coverage':cited/inference if inference else None,'blocked_count':sum(s['blocked_count'] for s in scores),
                'failure_types':{k:sum(k in s['failure_types'] for s in scores) for k in sorted({k for s in scores for k in s['failure_types']})},
                'preflight_seconds':sum(r['artifact']['preflight']['seconds'] for r in rows),
                'analysis_seconds':sum(times),'p50_seconds':percentile(.5),'p95_seconds':percentile(.95),
                'known_steps':sum(r['artifact'][p]['steps'] for r in rows for p in ('preflight','usage') if r['artifact'][p]['steps'] is not None),
                'unknown_step_records':sum(r['artifact'][p]['steps'] is None for r in rows for p in ('preflight','usage')),
                'known_model_calls':sum(r['artifact'][p]['model_calls'] for r in rows for p in ('preflight','usage') if r['artifact'][p]['model_calls'] is not None),
                'unknown_model_call_records':sum(r['artifact'][p]['model_calls'] is None for r in rows for p in ('preflight','usage')),
                'known_tokens':sum(v for v in tokens if v is not None),'unknown_token_records':sum(v is None for v in tokens),
                'total_cost':sum(costs) if all(v is not None for v in costs) else None,
                'known_cost_subtotal':sum(v for v in costs if v is not None),'unknown_cost_records':sum(v is None for v in costs),
                'case_gate_passed':gate,'safety_suite_status':'separate_suite_required','formal_acceptance_passed':False})
    return {'rounds':summaries,'timing_boundary':'analysis excludes shared preflight; end-to-end includes preflight per participant',
        'selection':'all rounds and both variants retained; no best-round selection',
        'formal_acceptance':'requires separately bound independent safety suite in T20'}


class EvaluationRunner:
    def __init__(self,root: Path, *, repository: Path | None = None,snapshot_root: Path | None = None):
        self.root=Path(root); self.root.mkdir(parents=True,exist_ok=True)
        self.repository=Path(repository or Path.cwd()).resolve()
        self.snapshot_root=Path(snapshot_root).resolve() if snapshot_root else None
        self.database=self.root/'audit.sqlite'
        with self._db() as db:
            db.executescript('''CREATE TABLE IF NOT EXISTS bundles(version TEXT PRIMARY KEY,family TEXT,payload TEXT,hash TEXT);
                CREATE TABLE IF NOT EXISTS regression(identity TEXT PRIMARY KEY,reason TEXT);
                CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY,payload TEXT,previous TEXT,hash TEXT);
                CREATE TABLE IF NOT EXISTS runs(id TEXT PRIMARY KEY,version TEXT,payload TEXT);
                CREATE TABLE IF NOT EXISTS results(run TEXT,ordinal INTEGER,payload TEXT,PRIMARY KEY(run,ordinal));
                CREATE TABLE IF NOT EXISTS reviews(id INTEGER PRIMARY KEY,run TEXT,ordinal INTEGER,payload TEXT);
                CREATE TABLE IF NOT EXISTS safety_receipts(id INTEGER PRIMARY KEY,run TEXT,payload TEXT);''')

    @contextmanager
    def _db(self):
        connection=sqlite3.connect(self.database)
        try:
            with connection:
                yield connection
        finally:
            connection.close()

    def _event(self,kind: str,detail: dict) -> None:
        with self._db() as db:
            db.execute('BEGIN IMMEDIATE')
            row=db.execute('SELECT hash FROM events ORDER BY id DESC LIMIT 1').fetchone()
            previous=row[0] if row else ''
            payload={'time':datetime.now(timezone.utc).isoformat(),'kind':kind,'detail':detail}
            db.execute('INSERT INTO events(payload,previous,hash) VALUES(?,?,?)',
                (json.dumps(payload,ensure_ascii=False),previous,digest([previous,payload])))

    def audit(self) -> list[dict]:
        with self._db() as db:
            rows=db.execute('SELECT payload,previous,hash FROM events ORDER BY id').fetchall()
        previous=''; result=[]
        for raw,parent,hash_value in rows:
            payload=json.loads(raw)
            if parent!=previous or digest([parent,payload])!=hash_value:
                raise ValueError('audit chain mismatch')
            result.append(payload); previous=hash_value
        return result

    def score(self,case: dict,artifact: dict,review: dict | None = None) -> dict:
        return score(case,artifact,review)

    def verify_configuration(self,config: dict) -> None:
        required={'code_ref','code_hashes','dependency_hash','model','prompt_hashes','rule_hashes','reference_hashes','rubric_hash','budgets','image'}
        if set(config)!=required or config['rubric_hash']!=RUBRIC_HASH or not config['code_ref'] or not config['model'] or not config['budgets'] or not config['image']:
            raise ValueError('complete locked configuration required')
        if file_hash(self.repository/'uv.lock')!=config['dependency_hash']:
            raise ValueError('dependency drift')
        if config['model'].get('host_runtime'):
            import platform
            import importlib.metadata
            actual={'python':platform.python_version(),'platform':platform.platform(),
                    'anthropic':importlib.metadata.version('anthropic')}
            if actual!=config['model']['host_runtime']: raise ValueError('host runtime drift')
        for group in ('code_hashes','prompt_hashes','rule_hashes','reference_hashes'):
            if not config[group]: raise ValueError('empty configuration references')
            for name,expected in config[group].items():
                path=(self.repository/name).resolve()
                if not path.is_relative_to(self.repository) or file_hash(path)!=expected:
                    raise ValueError('configuration drift:'+name)

    def freeze(self,version: str,family: str,cases: list[dict],configuration: dict, *, purpose: str = 'formal') -> dict:
        self.verify_configuration(configuration)
        if purpose not in ('formal','scorer_selftest') or not version or not family or not cases:
            raise ValueError('invalid bundle')
        ids=[c['id'] for c in cases]
        if len(ids)!=len(set(ids)): raise ValueError('duplicate cases')
        counts={k:sum(c['category']==k for c in cases) for k in COUNTS}
        if purpose=='formal' and (len(cases)!=24 or counts!=COUNTS): raise ValueError('frozen distribution')
        for case in cases:
            public=case['public']
            if set(public)!={'id','question','window','snapshot','snapshot_id','definition','schema'} or public['id']!=case['id']:
                raise ValueError('public input boundary')
            if not case['required'] or not case['forbidden'] or not isinstance(case['localization'],dict):
                raise ValueError('case expectations required')
            for expected in case['required']:
                if expected['abs_tol']<0 or expected['rel_tol']<0: raise ValueError('negative tolerance')
        bundle={'version':version,'family':family,'purpose':purpose,'cases':cases,'configuration':configuration,'counts':counts}
        payload=json.dumps(bundle,ensure_ascii=False,allow_nan=False)
        with self._db() as db:
            db.execute('INSERT INTO bundles VALUES(?,?,?,?)',(version,family,payload,digest(bundle)))
        self._event('freeze',{'version':version,'family':family,'content_hash':digest(bundle),'purpose':purpose})
        return {'version':version,'content_hash':digest(bundle),'counts':counts,'purpose':purpose}

    def _bundle(self,version: str) -> dict:
        with self._db() as db:
            row=db.execute('SELECT payload,hash FROM bundles WHERE version=?',(version,)).fetchone()
        if row is None: raise ValueError('unknown version')
        bundle=json.loads(row[0])
        if digest(bundle)!=row[1]: raise ValueError('bundle changed')
        return bundle

    def reconfigure(self, source: str, version: str, configuration: dict, *, actor: str) -> dict:
        """Lock new execution configuration without changing any task or expected answer."""
        previous=self.access(source,actor=actor,purpose='generation_audit')
        result=self.freeze(version,previous['family'],deepcopy(previous['cases']),configuration,purpose=previous['purpose'])
        self._event('configuration_revision',{'source':source,'version':version,
            'unchanged_cases_hash':digest(previous['cases']),'actor':actor})
        return result

    def status(self,version: str) -> dict:
        bundle=self._bundle(version)
        identities=['family:'+bundle['family']]+['snapshot:'+c['public']['snapshot_id'] for c in bundle['cases']]
        with self._db() as db:
            reasons=[row[0] for key in identities if (row:=db.execute('SELECT reason FROM regression WHERE identity=?',(key,)).fetchone())]
        return {'version':version,'purpose':'regression' if reasons else bundle['purpose'],'regression_reasons':sorted(set(reasons))}

    def access(self,version: str, *, actor: str,purpose: str) -> dict:
        if not actor.strip() or purpose not in ('formal_run','generation_audit','repair','scorer_selftest'):
            raise ValueError('identified access purpose required')
        bundle=self._bundle(version)
        if purpose=='scorer_selftest' and bundle['purpose']!='scorer_selftest':
            raise ValueError('formal cases cannot be scorer selftests')
        if purpose=='repair':
            with self._db() as db:
                for key in ['family:'+bundle['family']]+['snapshot:'+c['public']['snapshot_id'] for c in bundle['cases']]:
                    db.execute('INSERT OR IGNORE INTO regression VALUES(?,?)',(key,'targeted repair access by '+actor))
        self._event('private_access',{'version':version,'actor':actor,'purpose':purpose,'status':self.status(version)})
        return bundle

    def run(self,version: str,prepare,execute, *, actor: str) -> str:
        bundle=self._bundle(version); self.verify_configuration(bundle['configuration'])
        purpose='scorer_selftest' if bundle['purpose']=='scorer_selftest' else 'formal_run'
        bundle=self.access(version,actor=actor,purpose=purpose)
        run_id=uuid4().hex
        with self._db() as db:
            db.execute('INSERT INTO runs VALUES(?,?,?)',(run_id,version,json.dumps({'configuration':bundle['configuration'],'bundle_hash':digest(bundle)})))
        self._event('run_started',{'run_id':run_id,'version':version,'status':self.status(version)})
        ordinal=0
        for round_no in (1,2,3):
            for case in bundle['cases']:
                self.verify_configuration(bundle['configuration'])
                public=deepcopy(case['public'])
                preflight_started=time.monotonic()
                raw_prepared=None
                try:
                    if bundle['purpose']=='formal':
                        if self.snapshot_root is None: raise ValueError('frozen snapshot root required')
                        snapshot=(self.snapshot_root/public['snapshot']).resolve()
                        if not snapshot.is_relative_to(self.snapshot_root) or file_hash(snapshot)!=case['snapshot_sha256']:
                            raise ValueError('frozen snapshot drift')
                    raw_prepared=prepare(deepcopy(public),deepcopy(bundle['configuration']),deepcopy(case.get('controls',{})))
                    if not isinstance(raw_prepared,dict) or not isinstance(raw_prepared.get('materials'),dict) or raw_prepared.get('status') not in ('ok','failed'):
                        raise ValueError('invalid preflight shape')
                    usage(raw_prepared['usage'])
                    json.dumps(raw_prepared,allow_nan=False)
                    prepared=deepcopy(raw_prepared)
                except Exception as error:
                    prepared={'status':'failed','materials':{},'usage':failure_usage(raw_prepared,time.monotonic()-preflight_started),
                        'error':{'type':type(error).__name__,'original':safe_json(raw_prepared)}}
                for variant in ('agent','baseline'):
                    execution_started=time.monotonic()
                    raw_artifact=None
                    try:
                        raw_artifact=execute(deepcopy(public),deepcopy(prepared['materials']),variant,deepcopy(bundle['configuration'])) if prepared['status']=='ok' else {'usage':{'seconds':0,'steps':0,'model_calls':0,'tokens':0,'cost':0}}
                        if not isinstance(raw_artifact,dict): raise ValueError('invalid execution shape')
                        usage(raw_artifact['usage'])
                        json.dumps(raw_artifact,allow_nan=False)
                        artifact=deepcopy(raw_artifact)
                    except Exception as error:
                        artifact=safe_json(raw_artifact) if isinstance(raw_artifact,dict) else {'original':safe_json(raw_artifact)}
                        artifact.update(adapter_error=type(error).__name__,usage=failure_usage(raw_artifact,time.monotonic()-execution_started),safety_passed=False)
                    artifact['preflight']={**prepared['usage'],'status':prepared['status']}
                    if 'error' in prepared: artifact['preflight_error']=prepared['error']
                    artifact.setdefault('safety_passed',False)
                    record={'case_id':case['id'],'round':round_no,'variant':variant,'public_input_hash':digest(public),
                        'shared_materials_hash':digest(prepared['materials']),'artifact':artifact,'score':score(case,artifact)}
                    with self._db() as db:
                        db.execute('INSERT INTO results VALUES(?,?,?)',(run_id,ordinal,json.dumps(record,ensure_ascii=False,allow_nan=False)))
                    self._event('case_completed',{'run_id':run_id,'ordinal':ordinal,'case_id':case['id'],'round':round_no,'variant':variant})
                    ordinal+=1
        self.verify_configuration(bundle['configuration'])
        self._event('run_completed',{'run_id':run_id,'records':ordinal})
        return run_id

    def review(self,run_id: str,ordinal: int,review: dict) -> dict:
        with self._db() as db:
            row=db.execute('SELECT version FROM runs WHERE id=?',(run_id,)).fetchone()
            stored=db.execute('SELECT payload FROM results WHERE run=? AND ordinal=?',(run_id,ordinal)).fetchone()
        if row is None or stored is None: raise ValueError('unknown run result')
        record=json.loads(stored[0]); bundle=self._bundle(row[0]); case=next(c for c in bundle['cases'] if c['id']==record['case_id'])
        scored=score(case,record['artifact'],review)
        if any(s.startswith('invalid_artifact:') for s in scored['failure_types']): raise ValueError('invalid bound review')
        with self._db() as db:
            db.execute('INSERT INTO reviews(run,ordinal,payload) VALUES(?,?,?)',(run_id,ordinal,json.dumps(review,ensure_ascii=False)))
        self._event('review_recorded',{'run_id':run_id,'ordinal':ordinal,'review_hash':digest(review)})
        return scored

    def results(self,run_id: str) -> dict:
        with self._db() as db:
            run=db.execute('SELECT version,payload FROM runs WHERE id=?',(run_id,)).fetchone()
            rows=db.execute('SELECT ordinal,payload FROM results WHERE run=? ORDER BY ordinal',(run_id,)).fetchall()
            reviews=db.execute('SELECT ordinal,payload FROM reviews WHERE run=? ORDER BY id',(run_id,)).fetchall()
            safety=db.execute('SELECT payload FROM safety_receipts WHERE run=? ORDER BY id DESC LIMIT 1',(run_id,)).fetchone()
        if run is None: raise ValueError('unknown run')
        bundle=self._bundle(run[0]); cases={c['id']:c for c in bundle['cases']}; latest={i:json.loads(p) for i,p in reviews}
        records=[]
        for ordinal,payload in rows:
            record=json.loads(payload)
            if ordinal in latest: record['score']=score(cases[record['case_id']],record['artifact'],latest[ordinal])
            records.append(record)
        self._event('results_read',{'run_id':run_id})
        summary=summarize(records,bundle['purpose']=='formal')
        safety_status={'status':'not_run'}
        if safety:
            try:
                from metricguard.acceptance import validate_safety
                self.verify_configuration(bundle['configuration'])
                safety_status=validate_safety(json.loads(safety[0]),bundle['configuration'],self.repository)
            except (ValueError,KeyError,OSError) as error:
                safety_status={'status':'invalid','reason':str(error)}
        for row in summary['rounds']:
            row['safety_suite_status']=safety_status['status']
            row['formal_acceptance_passed']=(row['case_gate_passed'] and safety_status['status']=='passed'
                and self.status(run[0])['purpose']=='formal')
        agent_rounds=[r for r in summary['rounds'] if r['variant']=='agent']
        summary['formal_acceptance_passed']=(len(records)==144 and len(agent_rounds)==3
            and all(r['formal_acceptance_passed'] for r in agent_rounds) and self.status(run[0])['purpose']=='formal')
        summary['formal_acceptance']='same-version three agent rounds plus bound independent safety; baseline outcomes retained'
        return {'run_id':run_id,'version':run[0],'provenance':json.loads(run[1]),'status':self.status(run[0]),
            'records':records,'reviews':[json.loads(p) for _,p in reviews],
            'safety':safety_status,'summary':summary,'complete':len(records)==len(cases)*6}

    def bind_safety(self, run_id: str, receipt: dict) -> dict:
        from metricguard.acceptance import validate_safety
        with self._db() as db:
            row=db.execute('SELECT payload FROM runs WHERE id=?',(run_id,)).fetchone()
        if row is None: raise ValueError('unknown run')
        configuration=json.loads(row[0])['configuration']
        self.verify_configuration(configuration)
        assessed=validate_safety(receipt,configuration,self.repository)
        with self._db() as db:
            db.execute('INSERT INTO safety_receipts(run,payload) VALUES(?,?)',(run_id,json.dumps(receipt)))
        self._event('safety_bound',{'run_id':run_id,**assessed})
        return assessed
