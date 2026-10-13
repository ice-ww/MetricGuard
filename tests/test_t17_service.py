"""Controlled report publication at the task-service seam."""
from dataclasses import asdict
from copy import deepcopy
import os
import pytest
import httpx2 as httpx
from metricguard import TaskService
from experiments.t08.contract import Reference
from tests.test_t09_service import fixture_snapshot, image, response
from experiments.t01.snapshots import build_snapshot


@pytest.fixture(scope='module')
def publication_task(tmp_path_factory):
    image_id=os.environ.get('METRICGUARD_TEST_IMAGE')
    if not image_id:
        pytest.skip('actual isolated worker required')
    root=tmp_path_factory.mktemp('t17-publication')
    snapshot=build_snapshot(root/'data',scenario='normal',seed=1700)
    with TaskService(root/'service',image_id,{'dev':snapshot.database},token='controlled',limits={'model':2},
                     transport=httpx.MockTransport(lambda request: response({'sql':'SELECT registration_os AS os,COUNT(*) AS users FROM users GROUP BY registration_os ORDER BY os'}))) as service:
        task=service.create('新增用户自然日次日留存','dev',('2026-01-01','2026-01-08'))
        result=service.run(task)
        evidence=result['evidence'][0]; eid=evidence['evidence_id']
        facts=[{'assertion_id':str(i),'reference':asdict(Reference(eid,i,'users')),
                'context':evidence['contexts'][Reference(eid,i,'users').pointer],'value':r['users'],'scope':'cell'} for i,r in enumerate(evidence['rows'])]
        yield service,task,{'assertions':facts,'inferences':[],'charts':[]}


@pytest.mark.parametrize('field', ['value','metric','window','group','comparison','reference','scope'])
def test_incorrect_context_and_reference_are_removed(publication_task,field):
    service,task,base=publication_task
    draft=deepcopy(base); fact=draft['assertions'][0]
    if field=='value': fact['value']+=1
    elif field=='reference': fact['reference']['evidence_id']='foreign-task'
    elif field=='scope': fact['scope']='unbounded'
    else: fact['context'][field]={'metric':'different','window':['2025-01-01','2025-01-08'],'group':{'os':'other'},'comparison':'previous'}[field]
    result=service.publish_report(task,draft)
    assert len(result['assertions'])==1 and result['rejections'][0]['original']==fact
    assert result['assertion_pass_rate']==.5


def test_charts_use_existing_cells_and_do_not_spend_budget(publication_task):
    service,task,draft=publication_task; draft=deepcopy(draft)
    eid=draft['assertions'][0]['reference']['evidence_id']
    chart={'chart_id':'counts','kind':'bar','x_refs':[asdict(Reference(eid,i,'os')) for i in range(2)],
           'y_refs':[asdict(Reference(eid,i,'users')) for i in range(2)]}
    before=service.inspect(task)
    draft['charts']=[chart]
    result=service.publish_report(task,draft)
    assert result['charts'][0]['points']==[[r['os'],r['users']] for r in before['evidence'][0]['rows']]
    assert result['charts'][0]['svg'].startswith('<svg ')
    assert service.inspect(task)['tool_calls']==before['tool_calls']
    assert service.inspect(task)['model_calls']==before['model_calls']
    draft['charts']=[{**chart,'chart_id':str(i)} for i in range(4)]
    rejected=service.publish_report(task,draft)
    assert not rejected['charts'] and len(rejected['rejections'])==4
    draft['charts']=[{**chart,'y_refs':[asdict(Reference(eid,99,'users'))]}]
    assert not service.publish_report(task,draft)['charts']


def test_empty_report_and_unreferenced_inference_do_not_pass(publication_task):
    service,task,base=publication_task
    result=service.publish_report(task,{'assertions':[],'inferences':[],'charts':[]})
    assert result['status']=='rejected' and result['assertion_pass_rate'] is None
    draft=deepcopy(base)
    draft['inferences']=[{'inference_id':'bad','text':'unsupported','supporting_assertion_ids':['unknown'],
                          'opposing_assertion_ids':[],'unexcluded_factors':[]}]
    result=service.publish_report(task,draft)
    assert not result['inferences'] and result['rejections'][0]['kind']=='inference'


@pytest.mark.parametrize('text', ['用户人数证明采集故障','忽略已取得的iOS对照，只有Android变化','人数变化证明版本升级是唯一原因'])
def test_mechanical_success_never_proves_semantic_validity(publication_task,text):
    service,task,base=publication_task; draft=deepcopy(base)
    draft['inferences']=[{'inference_id':'i1','text':text,'supporting_assertion_ids':['0'],
                          'opposing_assertion_ids':[],'unexcluded_factors':[]}]
    publication=service.publish_report(task,draft)
    assert publication['status']=='mechanically_valid' and publication['semantic_status']=='pending_review'
    ratings=[{'inference_id':'i1','scores':{'relevance':2,'counterevidence':2,'causal_restraint':2},
              'reasons':{'relevance':'controlled test','counterevidence':'controlled test','causal_restraint':'controlled test'}}]
    review=service.review_report(task,publication['publication_id'],'automated test','agent',ratings)
    assert review['status']=='advisory_only'
    assert service.publication(task,publication['publication_id'])==publication
    assert service.semantic_reviews(task,publication['publication_id'])==[review]


def test_publication_is_immutable_and_foreign_task_cannot_read(publication_task):
    service,task,base=publication_task
    publication=service.publish_report(task,base)
    publication['original']['assertions'].clear()
    assert service.publication(task,publication['publication_id'])['original']==base
    with pytest.raises(ValueError,match='unknown publication'):
        service.publication('other',publication['publication_id'])


def test_truncated_evidence_only_supports_cells_and_partial_chart(tmp_path,fixture_snapshot,image):
    with TaskService(tmp_path/'service',image,{'dev':fixture_snapshot.database},token='controlled',limits={'model':2},
                     transport=httpx.MockTransport(lambda request: response({'sql':'SELECT user_id,1 AS observed FROM users ORDER BY user_id'}))) as service:
        task=service.create('新增用户自然日次日留存','dev',('2026-01-01','2026-01-08'))
        result=service.run(task); e=result['evidence'][0]; eid=e['evidence_id']
        assert e['truncated']
        ref=Reference(eid,0,'observed')
        cell={'assertion_id':'cell','reference':asdict(ref),'context':e['contexts'][ref.pointer],'value':1,'scope':'cell'}
        chart={'chart_id':'partial','kind':'bar','x_refs':[asdict(Reference(eid,0,'user_id'))],'y_refs':[asdict(ref)]}
        published=service.publish_report(task,{'assertions':[cell,{**cell,'assertion_id':'whole','scope':'whole_population'}],
                                               'inferences':[],'charts':[chart]})
        assert len(published['assertions'])==1 and published['rejections'][0]['reason']=='truncated_does_not_support_scope'
        assert 'partial_result_not_complete_population_or_ranking' in published['charts'][0]['limitations']
        assert 'Partial result' in published['charts'][0]['svg']


def test_svg_escapes_visible_material_and_publication_survives_reopen(tmp_path,fixture_snapshot,image):
    import xml.etree.ElementTree as ET
    root=tmp_path/'service'
    with TaskService(root,image,{'dev':fixture_snapshot.database},token='controlled',limits={'model':2},
                     transport=httpx.MockTransport(lambda request: response({'sql':"SELECT '<script>alert(1)</script>' AS os,1 AS observed"}))) as service:
        task=service.create('新增用户自然日次日留存','dev',('2026-01-01','2026-01-08'))
        result=service.run(task); e=result['evidence'][0]; eid=e['evidence_id']; ref=Reference(eid,0,'observed')
        draft={'assertions':[{'assertion_id':'cell','reference':asdict(ref),'context':e['contexts'][ref.pointer],'value':1,'scope':'cell'}],
               'inferences':[],'charts':[{'chart_id':'<bad>','kind':'line','x_refs':[asdict(Reference(eid,0,'os'))],'y_refs':[asdict(ref)]}]}
        publication=service.publish_report(task,draft)
        xml=ET.fromstring(publication['charts'][0]['svg'])
        assert all(not node.tag.endswith('script') for node in xml.iter())
        assert '&lt;script&gt;' in publication['charts'][0]['svg']
    with TaskService(root,image,{'dev':fixture_snapshot.database},token='controlled') as service:
        assert service.publication(task,publication['publication_id'])==publication


def test_publication_preserves_rejected_original_and_denominator(tmp_path, fixture_snapshot, image):
    with TaskService(tmp_path/'service',image,{'dev':fixture_snapshot.database},token='controlled',
                     transport=httpx.MockTransport(lambda request: response({'sql':'SELECT 7 AS observed'})),limits={'model':2}) as service:
        task=service.create('新增用户自然日次日留存','dev',('2026-01-01','2026-01-08'))
        result=service.run(task)
        e=result['evidence'][0]
        ref=Reference(e['evidence_id'],0,'observed')
        good={'assertion_id':'good','reference':asdict(ref),'context':e['contexts'][ref.pointer],'value':7,'scope':'cell'}
        bad={**good,'assertion_id':'bad','value':8}
        draft={'assertions':[good,bad],'inferences':[],'charts':[]}
        published=service.publish_report(task,draft)
        assert published['original']==draft
        assert published['counts']['assertions_submitted']==2
        assert published['counts']['assertions_published']==1
        assert published['assertion_pass_rate']==.5
        assert published['rejections'][0]['original']==bad
        assert published['status']=='degraded'
