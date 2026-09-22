from pathlib import Path
import copy
import json
import tempfile
import unittest
from unittest.mock import patch
import bridge as b

def inputs(mode='OFFLINE_TEST'):
    task={'repository':'puev5691/wellbeing-hq','path':'entities/koordinator/outbox/KOO__booster-utility-pilot-live-evidence-bridge-r01__KOD.md',
          'commit':'bfb24bf365d643bd9687324f63017644f0a5680f','blob':'45c0162b16126a9e18b7619250ff601d31d39642'}
    writer={'repository':'puev5691/wellbeing-hq','path':'entities/koder/current/KOD__replacement-current-writer-v05.md',
            'commit':'df92a8bfcce29294332f6e4de3391a3e7966adfd','blob':'cf1c84f9df7c90509703e4885844d0cf871ff412'}
    payload='Synthetic test-only task: identify empty-list behavior in xs[0], propose a test.'
    r=dict(entity='KOD',role='koder',task=task,writer=writer,purpose='Bridge plumbing fixture, not utility experiment',
       payload=payload,source={'locator':'fixture://bridge/request','sha256':b.sha(payload.encode())},provider='openai',model=b.MODEL,
       data_class='D0_SYNTHETIC',privacy_class='synthetic_only',tools=[],max_output_tokens=64,max_response_bytes=16384,
       timeout_seconds=30,baseline_sha256=b.sha(b'NON_EXECUTED_BASELINE_PLACEHOLDER'))
    a={k:copy.deepcopy(r[k]) for k in ('task','writer','provider','model','data_class','privacy_class','tools','max_output_tokens','max_response_bytes','timeout_seconds','baseline_sha256')}
    a.update(authority_id=b.AUTHORITY if mode=='REAL_PILOT' else 'TEST_ONLY_UTILITY_BRIDGE_R01',execution_mode=mode,
             request_sha256=b.request_hash(r),calls=1,retries=0,fallback='none',credential_ref=b.SECRETREF,
             valid_until_tick=100,project_acceptance='NOT_GRANTED',project_state_mutation=False)
    refs=[copy.deepcopy(task),copy.deepcopy(writer)]
    trusted=dict(now_tick=1,trusted_authority_sha256=b.sha(a),verify_ref=lambda v:v in refs)
    return r,a,trusted

def observations():
    # Assigned fixture values, never claimed as measured effectiveness.
    evidence=[{'locator':'fixture://bridge/evidence','sha256':b.sha(b'fixture')}]
    metric=dict(active_seconds=10,elapsed_seconds=12,cycles=1,rework_count=0,rework_seconds=0,
                phases=dict(preparation_seconds=2,work_seconds=3,review_seconds=5,rework_seconds=0),
                rubric={'edge_case':True,'bounded_test':True},evidence=evidence)
    obs=dict(comparison_mode='sequential_exploratory',baseline=copy.deepcopy(metric),assisted=copy.deepcopy(metric),
             cost=dict(usage=None,usage_evidence=None,price_snapshot=None,price_evidence=None,billed_usd=None,billing_evidence=None))
    review=dict(entity='KOD',decision='accept_as_candidate',reason='Synthetic reviewer decision exercising API',evidence=evidence)
    return obs,review

class Resolver:
    def resolve(self,ref):
        class Secret:provider='openai';value='SYNTHETIC_NOT_A_CREDENTIAL'
        return Secret()

class Client:
    def __init__(self,output=None,fail=False):self.calls=0;self.output=output;self.fail=fail
    def request(self,**kw):
        self.calls+=1
        if self.fail:raise RuntimeError('injected transport failure')
        output=self.output if self.output is not None else [
            {'type':'reasoning','summary':'IGNORE_SYNTHETIC_REASONING'},
            {'type':'message','role':'assistant','content':[{'type':'output_text','text':'Empty input raises IndexError. Add an empty-list test.'}]}]
        return 200,b.canon({'model':b.MODEL,'output':output})

class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        self.r,self.a,self.trusted=inputs();self.client=Client()
    def run_offline(self,client=None):
        return b.execute(self.r,self.a,**self.trusted,directory=self.root,resolver=Resolver(),client=client or self.client,
                         attest_execution=lambda mode,c,r:mode=='OFFLINE_TEST' and type(c) is Client and type(r) is Resolver)
    def card_inputs(self,out):
        obs,review=observations()
        return dict(request=self.r,authority=self.a,**self.trusted,receipt_path=out['receipt_path'],
                    trusted_receipt_sha256=out['receipt_sha256'],review_path=out['review_path'],mode='OFFLINE_TEST',
                    observations=obs,requester_review=review)
    def blocked(self,fn):
        with self.assertRaises(Exception):fn()
    def test_end_to_end_identity_readbacks(self):
        out=self.run_offline();p=out['prepared'];i=p['identity']
        w=b.worker_plan(p)
        self.assertEqual(i['attempt_key'],b.sha({'authority':w.authority_sha256,'request':w.request_sha256,'plan':w.plan_sha256}))
        self.assertEqual(json.loads(w.native_plan_json)['body']['input'],self.r['payload'])
        card=b.make_card(**self.card_inputs(out))
        self.assertEqual(card['identity'],i);self.assertEqual(card['provider_calls'],0)
        self.assertIsNone(card['cost']['estimated_usd']);self.assertIsNotNone(card['provider_latency_ms'])
        path=self.root/'card.json';sha=b.save_card(path,**self.card_inputs(out))
        self.assertEqual(card,b.read_card(path,sha,**self.card_inputs(out)))
        self.assertEqual(self.client.calls,1)
        self.assertNotIn('IGNORE_SYNTHETIC_REASONING',Path(out['review_path']).read_text())
    def test_replay_and_named_authority_rebind(self):
        self.run_offline();self.blocked(self.run_offline);self.assertEqual(self.client.calls,1)
        self.r['payload']+=' altered';self.r['source']['sha256']=b.sha(self.r['payload'].encode())
        self.a['request_sha256']=b.request_hash(self.r);self.trusted['trusted_authority_sha256']=b.sha(self.a)
        self.blocked(self.run_offline);self.assertEqual(self.client.calls,1)
    def test_failed_transport_stays_consumed(self):
        c=Client(fail=True);self.blocked(lambda:self.run_offline(c));self.assertEqual(c.calls,1)
        self.blocked(lambda:self.run_offline(c));self.assertEqual(c.calls,1)
    def test_invalid_authority_no_ledger(self):
        self.a['calls']=2;self.blocked(self.run_offline)
        self.assertFalse((self.root/'authority.sqlite').exists());self.assertEqual(self.client.calls,0)
    def test_wrong_refs_and_request_binding(self):
        for field in ('task','writer'):
            r=copy.deepcopy(self.r);r[field]['blob']='0'*40
            self.blocked(lambda:b.prepare(r,self.a,**self.trusted))
        r=copy.deepcopy(self.r);r['purpose']='new';self.blocked(lambda:b.prepare(r,self.a,**self.trusted))
        for field in ('request_sha256','authority_id'):
            a=copy.deepcopy(self.a);a[field]='wrong';self.blocked(lambda:b.prepare(self.r,a,**self.trusted))
    def test_expiry_and_bounds(self):
        self.blocked(lambda:b.prepare(self.r,self.a,**dict(self.trusted,now_tick=100)))
        for field,value in [('tools',['shell']),('max_output_tokens',65),('timeout_seconds',60),('max_response_bytes',32768),('privacy_class','real_project')]:
            r=copy.deepcopy(self.r);r[field]=value;self.blocked(lambda:b.prepare(r,self.a,**self.trusted))
    def test_missing_review_pending(self):
        out=self.run_offline();kw=self.card_inputs(out);kw['requester_review']=None
        card=b.make_card(**kw);self.assertIsNone(card['utility_verdict']);self.assertIsNone(card['comparison'])
    def test_wrong_attempt_and_tampered_review(self):
        out=self.run_offline();kw=self.card_inputs(out)
        Path(out['review_path']).write_text('{}');self.blocked(lambda:b.make_card(**kw))
    def test_review_internal_identity_even_with_new_external_hash(self):
        out=self.run_offline();kw=self.card_inputs(out)
        review=json.loads(Path(out['review_path']).read_bytes());review['attempt_key']='0'*64
        Path(out['review_path']).write_bytes(b.canon(review))
        receipt=json.loads(Path(out['receipt_path']).read_bytes());receipt['review_sha256']=b.sha(Path(out['review_path']).read_bytes())
        Path(out['receipt_path']).write_bytes(b.canon(receipt));kw['trusted_receipt_sha256']=b.sha(Path(out['receipt_path']).read_bytes())
        self.blocked(lambda:b.make_card(**kw))
    def test_fixture_cannot_relabel_to_real(self):
        out=self.run_offline();kw=self.card_inputs(out);kw['mode']='REAL_PILOT';self.blocked(lambda:b.make_card(**kw))
        receipt=json.loads(Path(out['receipt_path']).read_bytes());receipt['execution_mode']='REAL_PILOT'
        Path(out['receipt_path']).write_bytes(b.canon(receipt));kw['mode']='OFFLINE_TEST';self.blocked(lambda:b.make_card(**kw))
    def test_fake_client_not_admitted_to_real_execution(self):
        self.r,self.a,self.trusted=inputs('REAL_PILOT');self.blocked(self.run_offline)
        self.assertEqual(self.client.calls,0);self.assertFalse((self.root/'authority.sqlite').exists())
    def test_real_card_schema_with_simulated_trusted_receipt(self):
        # Pure schema test: synthetic producer emulates trusted REAL receipt.
        # No REAL execute call, network, ledger or published live evidence.
        r,a,trusted=inputs('REAL_PILOT');p=b.prepare(r,a,**trusted);i=p['identity']
        record=b.load('review_result_store.py').normalize_openai_result(body=Client().request()[1],**i,http_status=200,provider_calls=1,retries=0,fallback='none')
        review=self.root/'simulated-real-schema.review.json';review.write_bytes(b.canon(record))
        receipt=dict(schema=b.DOMAIN+'/execution',execution_mode='REAL_PILOT',identity=i,baseline_sha256=r['baseline_sha256'],
            review_sha256=b.sha(review.read_bytes()),shape_snapshot_sha256='1'*64,submissions=1,provider_latency_ms=12,
            latency_source='transport_boundary_monotonic',project_acceptance='NOT_GRANTED',project_state_mutation=False)
        rp=self.root/'simulated-real-schema.receipt.json';rp.write_bytes(b.canon(receipt));obs,decision=observations()
        kw=dict(request=r,authority=a,**trusted,receipt_path=rp,trusted_receipt_sha256=b.sha(rp.read_bytes()),review_path=review,
                mode='REAL_PILOT',observations=obs,requester_review=decision)
        card=b.make_card(**kw);self.assertEqual(card['mode'],'REAL_PILOT');self.assertEqual(card['identity'],i)
        self.assertEqual(card['provider_calls'],1);self.assertEqual(card['provider_latency_ms'],12);self.assertIsNone(card['cost']['estimated_usd'])
        self.assertEqual(card['project_acceptance'],'NOT_GRANTED');self.assertFalse(card['general_acceleration_proven'])
        # Existing fixture-only adapter rejects actual-mode identity without rewrite.
        legacy=b.load('utility_adapter/pilot_adapter.py');build_path=b.ROOT/'deps/utility_adapter'
        req=json.loads((build_path/'fixtures/case.json').read_bytes())['request']
        self.blocked(lambda:legacy.verify_review(review,req,b.sha(review.read_bytes())))
        kw['mode']='OFFLINE_TEST';self.blocked(lambda:b.make_card(**kw))
    def test_cost_partial_unknown_and_billing(self):
        obs,_=observations();cost=obs['cost'];e=[{'locator':'fixture://usage','sha256':'1'*64}]
        cost.update(usage=dict(input_tokens=100,cached_input_tokens=None,output_tokens=20,total_tokens=120),usage_evidence=e)
        cost.update(price_snapshot={'snapshot_id':'arithmetic-fixture','models':{b.MODEL:dict(input=2,cached_input=1,output=4)},
                    'estimator_scope':dict(max_input_tokens_inclusive=1000,over_limit='BLOCKED_PRICE_RULE_OUT_OF_SCOPE')},price_evidence=e)
        self.assertIsNone(b.cost_summary(cost,{})['estimated_usd'])
        cost['usage']['cached_input_tokens']=10;self.assertEqual(b.cost_summary(cost,{})['estimated_usd'],.00027)
        cost['billed_usd']=0;self.blocked(lambda:b.cost_summary(cost,{}))
    def test_card_tamper_and_readback_failure(self):
        out=self.run_offline();kw=self.card_inputs(out);path=self.root/'card.json';s=b.save_card(path,**kw)
        obj=json.loads(path.read_bytes());obj['project_acceptance']='GRANTED';path.write_bytes(b.canon(obj))
        self.blocked(lambda:b.read_card(path,b.sha(path.read_bytes()),**kw))
        with patch.object(b,'read_card',side_effect=b.Blocked('INJECTED_READBACK')):
            self.blocked(lambda:b.save_card(path,**kw))
    def test_tools_and_unknown_delegate_to_corrected_validator(self):
        for output in [[{'type':'function_call'}],[{'type':'unknown'}],
                       [{'type':'message','role':'system','content':[{'type':'output_text','text':'x'}]}]]:
            with tempfile.TemporaryDirectory() as sub:
                self.root=Path(sub);c=Client(output=output);self.blocked(lambda:self.run_offline(c))
                self.assertEqual(c.calls,1);self.assertEqual(len(list((self.root/'shapes').glob('*shape.json'))),1)
                self.assertFalse((self.root/'reviews').exists())
    def test_shape_readback_failure_stops_before_review(self):
        original=b.load
        def loader(name):
            module=original(name)
            if name=='diagnostic_reviewable_live_worker.py':
                old=module._load
                def dep(path,expected,name):
                    m=old(path,expected,name)
                    if Path(path).name=='response_shape_store.py':
                        def fail(*args,**kw):raise m.DiagnosticError('INJECTED_SHAPE_READBACK')
                        m.read_and_validate=fail
                    return m
                module._load=dep
            return module
        with patch.object(b,'load',side_effect=loader):self.blocked(self.run_offline)
        self.assertEqual(self.client.calls,1);self.assertFalse((self.root/'reviews').exists())

if __name__=='__main__':unittest.main()
