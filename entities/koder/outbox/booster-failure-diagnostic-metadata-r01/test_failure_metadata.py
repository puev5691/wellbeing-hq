from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import sqlite3
import tempfile
import unittest
from unittest.mock import patch
import bridge as b
from test_bridge import inputs, Resolver

spec=importlib.util.spec_from_file_location('metadata_test',Path(__file__).parent/'deps/failure_metadata_store.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

MARKER='SYNTHETIC_CONTENT_MUST_NOT_LEAK'

def fixture(completed=False):
    output=[dict(type='reasoning',content=MARKER,summary=MARKER,encrypted_content=MARKER)]
    if completed:
        output.append(dict(type='message',role='assistant',content=[dict(type='output_text',text=MARKER)]))
    return dict(model=b.MODEL,output=output,status='completed' if completed else 'incomplete',
                incomplete_details=None if completed else {'reason':'max_output_tokens'},
                error={'code':'server_error','type':'server_error','message':MARKER},
                max_output_tokens=64,usage={'input_tokens':20,'output_tokens':64,'total_tokens':84,
                 'input_tokens_details':{'cached_tokens':0},'output_tokens_details':{'reasoning_tokens':64}},
                reasoning={'effort':'medium','summary':MARKER},metadata={'secret':MARKER},headers={'Authorization':MARKER})

class Client:
    def __init__(self,obj):self.obj=obj;self.calls=0;self.sent=None
    def request(self,**kw):
        self.calls+=1;self.sent=kw['body'];return 200,b.canon(self.obj)

class MetadataTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        self.r,self.a,self.trusted=inputs();self.client=Client(fixture())
    def run_offline(self):
        return b.execute(self.r,self.a,**self.trusted,directory=self.root,resolver=Resolver(),client=self.client,
           attest_execution=lambda mode,c,r:mode=='OFFLINE_TEST' and type(c) is Client and type(r) is Resolver)
    def build(self,obj):
        raw=b.canon(obj)
        ident={k:hashlib.sha256(k.encode()).hexdigest() for k in m.IDENTITY_KEYS}
        ident['response_sha256']=hashlib.sha256(raw).hexdigest()
        return m.build(body=raw,identity=ident,execution_mode='OFFLINE_TEST',http_status=200,transport_latency_ms=12.5)
    def read(self):
        paths=list((self.root/'metadata').glob('*.json'));self.assertEqual(len(paths),1)
        return paths[0],json.loads(paths[0].read_bytes())
    def validate(self,record):
        return m.validate(record,expected_snapshot_sha256=record['snapshot_sha256'],
                          expected_identity=record['identity'],expected_mode=record['execution_mode'])
    def test_reasoning_only_survives_normalization_failure_and_no_leak(self):
        with self.assertRaisesRegex(Exception,'BLOCKED_REVIEW_RESULT_PERSISTENCE_AFTER_SHAPE_SAVED:BLOCKED_PROVIDER_RESPONSE'):
            self.run_offline()
        path,rec=self.read();self.assertNotIn(MARKER,path.read_text())
        self.assertEqual(rec['fields']['incomplete_details.reason'],{'state':'value','value':'max_output_tokens'})
        self.assertEqual(rec['fields']['usage.output_tokens_details.reasoning_tokens']['value'],64)
        self.assertFalse((self.root/'reviews').exists());self.assertFalse((self.root/'execution.json').exists())
        self.assertEqual(self.client.calls,1)
    def test_completed_assistant_still_reviewable(self):
        self.client=Client(fixture(True));out=self.run_offline();path,rec=self.read()
        self.assertEqual(rec['fields']['status']['value'],'completed');self.assertNotIn(MARKER,path.read_text())
        self.assertIn(MARKER,Path(out['review_path']).read_text())
    def test_missing_metadata_is_absent(self):
        rec=self.build({'output':[]})
        self.assertTrue(all(x=={'state':'absent'} for x in rec['fields'].values()))
    def test_null_leaf_and_null_parent_are_distinct(self):
        rec=self.build(dict(status=None,usage=None,error={'code':None},reasoning=None,incomplete_details=None))
        self.assertEqual(rec['fields']['status'],{'state':'null'})
        self.assertEqual(rec['fields']['error.code'],{'state':'null'})
        self.assertEqual(rec['fields']['usage.input_tokens'],{'state':'ancestor_null'})
        self.assertEqual(rec['fields']['reasoning.effort'],{'state':'ancestor_null'})
    def test_wrong_types_and_unknown_strings_never_echo(self):
        obj=fixture();obj.update(status=MARKER,incomplete_details=[],error={'code':MARKER,'type':False},max_output_tokens=True)
        obj['usage']['output_tokens']=-1;obj['usage']['input_tokens_details']='bad'
        rec=self.build(obj);f=rec['fields']
        self.assertEqual(f['status'],{'state':'unsupported'})
        self.assertEqual(f['error.code'],{'state':'unsupported'})
        self.assertEqual(f['error.type'],{'state':'invalid'})
        self.assertEqual(f['max_output_tokens'],{'state':'invalid'})
        self.assertEqual(f['usage.output_tokens'],{'state':'invalid'})
        self.assertEqual(f['usage.input_tokens_details.cached_tokens'],{'state':'ancestor_invalid'})
        self.assertNotIn(MARKER,m.canon(rec).decode())
    def test_numeric_and_enum_boundaries(self):
        for val in (False,-1,1.5,'64',2**53,[],{}):
            rec=self.build({'usage':{'input_tokens':val}})
            self.assertEqual(rec['fields']['usage.input_tokens'],{'state':'invalid'})
        for val in (0,64,2**53-1):
            self.assertEqual(self.build({'max_output_tokens':val})['fields']['max_output_tokens']['value'],val)
        for val in sorted(m.EFFORT):
            self.assertEqual(self.build({'reasoning':{'effort':val}})['fields']['reasoning.effort']['value'],val)
        self.assertEqual(self.build({'reasoning':{'effort':MARKER}})['fields']['reasoning.effort'],{'state':'unsupported'})
    def test_exact_native_response_and_all_identity_bindings(self):
        with self.assertRaises(Exception):self.run_offline()
        _,rec=self.read();p=b.prepare(self.r,self.a,**self.trusted);i=p['identity']
        for key in ('request_sha256','plan_sha256','authority_sha256','attempt_key'):self.assertEqual(rec['identity'][key],i[key])
        self.assertEqual(rec['identity']['native_body_sha256'],b.sha(self.client.sent))
        self.assertEqual(rec['identity']['response_sha256'],b.sha(b.canon(self.client.obj)))
        body=json.loads(self.client.sent)
        self.assertEqual(body['input'],self.r['payload']);self.assertEqual(body['max_output_tokens'],64)
        self.assertNotIn('reasoning',body);self.assertEqual(body['tools'],[])
        for key in m.IDENTITY_KEYS:
            expected=copy.deepcopy(rec['identity']);expected[key]='0'*64
            with self.assertRaises(m.MetadataError):
                m.validate(rec,expected_snapshot_sha256=rec['snapshot_sha256'],expected_identity=expected,expected_mode='OFFLINE_TEST')
    def test_latency_is_measured_transport_not_processing(self):
        with patch.object(b.time,'perf_counter_ns',side_effect=[1000000,4000000]):
            with self.assertRaises(Exception):self.run_offline()
        _,rec=self.read();self.assertEqual(rec['transport_latency_ms'],3.0)
        self.assertEqual(rec['latency_source'],'transport_boundary_monotonic')
    def test_shape_v2_bytes_unchanged_by_metadata(self):
        with self.assertRaises(Exception):self.run_offline()
        _,rec=self.read();shape=b.load('response_shape_store.py');p=b.prepare(self.r,self.a,**self.trusted)
        expected=shape.structural_snapshot(body=b.canon(self.client.obj),**p['identity'],http_status=200)
        path=self.root/'shapes'/(p['identity']['attempt_key']+'.shape.json')
        self.assertEqual(path.read_bytes(),shape.canonical(expected)+b'\n')
        self.assertEqual(rec['identity']['shape_snapshot_sha256'],expected['snapshot_sha256'])
    def test_strict_readback_and_tamper(self):
        rec=self.build(fixture());p=self.root/'meta.json';digest=m.persist_and_readback(p,rec)
        kw=dict(expected_snapshot_sha256=digest,expected_identity=rec['identity'],expected_mode='OFFLINE_TEST')
        self.assertEqual(m.read_and_validate(p,**kw),rec)
        changed=copy.deepcopy(rec);changed['fields']['status']['value']='completed';p.write_bytes(m.canon(changed)+b'\n')
        with self.assertRaises(m.MetadataError):m.read_and_validate(p,**kw)
        with self.assertRaises(m.MetadataError):m.read_and_validate(p,**dict(kw,expected_mode='REAL_PILOT'))
    def test_readback_rejects_extra_keys_and_invalid_rehashed_values(self):
        rec=self.build(fixture())
        for change in ('extra','badcount','payload'):
            x=copy.deepcopy(rec)
            if change=='extra':x['payload']=MARKER
            if change=='badcount':x['fields']['max_output_tokens']['value']=True
            if change=='payload':x['fields']['status']['extra']=MARKER
            x['snapshot_sha256']=m.snapshot_identity(x)
            with self.assertRaises(m.MetadataError):self.validate(x)
    def test_persistence_is_create_only(self):
        rec=self.build(fixture());p=self.root/'meta.json';m.persist_and_readback(p,rec);before=p.read_bytes()
        with self.assertRaises(m.MetadataError):m.persist_and_readback(p,self.build(fixture(True)))
        self.assertEqual(p.read_bytes(),before)
        link=self.root/'link.json';link.symlink_to(p)
        with self.assertRaises(m.MetadataError):m.persist_and_readback(link,rec)
        with self.assertRaises(m.MetadataError):m.read_and_validate(link,expected_snapshot_sha256=rec['snapshot_sha256'],expected_identity=rec['identity'],expected_mode='OFFLINE_TEST')
    def test_readback_failure_stops_review(self):
        original=b.load
        def loader(name):
            mod=original(name)
            if name=='diagnostic_reviewable_live_worker.py':
                old=mod._load
                def inner(path,expected,name):
                    dep=old(path,expected,name)
                    if Path(path).name=='failure_metadata_store.py':
                        dep.read_and_validate=lambda *a,**kw: (_ for _ in ()).throw(dep.MetadataError('INJECTED_READBACK'))
                    return dep
                mod._load=inner
            return mod
        self.client=Client(fixture(True))
        with patch.object(b,'load',side_effect=loader):
            with self.assertRaisesRegex(Exception,'BLOCKED_FAILURE_METADATA:INJECTED_READBACK'):self.run_offline()
        self.assertFalse((self.root/'reviews').exists());self.assertEqual(self.client.calls,1)
    def test_retry_after_failure_cannot_overwrite_evidence(self):
        with self.assertRaises(Exception):self.run_offline()
        path,_=self.read();before=path.read_bytes()
        with self.assertRaisesRegex(Exception,'BLOCKED_DUPLICATE_CALL'):self.run_offline()
        self.assertEqual(path.read_bytes(),before);self.assertEqual(self.client.calls,1)
    def test_consumed_real_named_authority_fixture_blocks_before_transport(self):
        # Synthetic ledger only. No real r01 admission document, host path or credential.
        r,a,kw=inputs('REAL_PILOT');p=b.prepare(r,a,**kw);i=p['identity'];w=b.load('live_worker.py')
        key=b.sha({'domain':b.DOMAIN+'/use-once','authority_id':b.AUTHORITY})
        ledger=w.DurableOneShotLedger(self.root/'authority.sqlite')
        ledger.claim(key,i['request_sha256'],i['plan_sha256'],i['authority_sha256'])
        class NeverResolver:
            def resolve(self,ref):raise AssertionError('resolver must not be reached')
        with self.assertRaisesRegex(Exception,'BLOCKED_DUPLICATE_CALL'):
            b.execute(r,a,**kw,directory=self.root,resolver=NeverResolver(),client=self.client,
                      attest_execution=lambda *args:True)
        self.assertEqual(self.client.calls,0);self.assertEqual(ledger.count(),1)
        self.assertFalse((self.root/'attempts.sqlite').exists())
    def test_original_normalizer_and_worker_exact(self):
        for name,expected in [('review_result_store.py','72a3374bdebd1cd0f37951507dd8cd3cf271b8a7924335a6e61f707fcc33e3ba'),
                              ('live_worker.py','175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3'),
                              ('response_shape_store.py','bc68a15f1dd288ef7092eaf1013e5b825432bb519da4cba4b355c1feb7118e8f')]:
            self.assertEqual(b.sha((b.ROOT/'deps'/name).read_bytes()),expected)
    def test_raw_json_and_bounds_reject_ambiguity(self):
        for raw in (b'{"status":"completed","status":"failed"}',b'{"usage":NaN}',b'[]',b'x',b' '*16385):
            ident={k:'1'*64 for k in m.IDENTITY_KEYS};ident['response_sha256']=b.sha(raw)
            with self.assertRaises(m.MetadataError):m.build(body=raw,identity=ident,execution_mode='OFFLINE_TEST',http_status=200,transport_latency_ms=1)
    def test_latency_absent_and_wrong_types(self):
        raw=b'{}';ident={k:'1'*64 for k in m.IDENTITY_KEYS};ident['response_sha256']=b.sha(raw)
        for value in (True,-1,float('inf'),'10'):
            with self.assertRaises(m.MetadataError):m.build(body=raw,identity=ident,execution_mode='OFFLINE_TEST',http_status=200,transport_latency_ms=value)
        rec=m.build(body=raw,identity=ident,execution_mode='OFFLINE_TEST',http_status=200,transport_latency_ms=None)
        self.assertIsNone(rec['latency_source'])

if __name__=='__main__':unittest.main()
