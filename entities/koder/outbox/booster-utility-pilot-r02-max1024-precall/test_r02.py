from pathlib import Path
import copy,json,tempfile,unittest
import bridge as b
import prepare_candidate as p

class R02Tests(unittest.TestCase):
    def setUp(self):self.art=p.build();self.r=self.art['request.json'];self.a=self.art['admission.candidate.json']
    def trusted(self,r=None,a=None):
        r=r or self.r;a=a or self.a
        return dict(now_tick=1,trusted_authority_sha256=b.sha(a),verify_ref=lambda ref:ref in (self.r['task'],self.r['writer']))
    def test_exact_single_parameter_delta(self):
        old=p.read('basis/request-r01.json');self.assertEqual({k for k in old if old[k]!=self.r[k]},{'max_output_tokens'})
        self.assertEqual(self.r['max_output_tokens'],1024);self.assertEqual(old['max_output_tokens'],64)
        self.assertEqual(self.r['payload'],p.read('basis/task.json')['specification'])
        self.assertEqual(self.art['comparison.json']['baseline_elapsed_seconds'],40.071600699)
    def test_body_policy_and_identity(self):
        prep=b.prepare(self.r,self.a,**self.trusted());w=b.worker_plan(prep);worker=b.load('live_worker.py')
        native=worker.parse_native(w)[3];body=json.loads(native)
        self.assertEqual(body,self.art['native-body.json']);self.assertEqual(b.sha(native),self.art['identities.json']['native_body_sha256'])
        self.assertEqual(body['model'],'gpt-5.6-luna');self.assertNotIn('reasoning',body)
        self.assertEqual(body['tools'],[]);self.assertEqual(body['tool_choice'],'none');self.assertFalse(body['parallel_tool_calls'])
        for k,v in dict(calls=1,retries=0,fallback='none',max_response_bytes=16384,timeout_seconds=30,project_acceptance='NOT_GRANTED',project_state_mutation=False).items():self.assertEqual(self.a[k],v)
        ids=self.art['identities.json'];self.assertEqual(ids['attempt_key'],b.sha({'authority':ids['authority_sha256'],'request':ids['request_sha256'],'plan':ids['plan_sha256']}))
    def test_fresh_consumed_ledger_evidence(self):
        h=p.read('basis/host-readonly.json');ids=self.art['identities.json']
        self.assertEqual(h['reservation_r02'],ids['named_authority_reservation'])
        self.assertNotEqual(h['reservation_r01'],h['reservation_r02'])
        self.assertEqual(len(h['authority.sqlite']),1);self.assertEqual(h['authority.sqlite'][0][0],h['reservation_r01'])
        self.assertEqual(h['authority.sqlite'][0][-1],'consumed');self.assertEqual(len(h['attempts.sqlite']),1)
        self.assertNotIn(ids['named_authority_reservation'],[r[0] for r in h['authority.sqlite']])
        self.assertNotIn(ids['attempt_key'],[r[0] for r in h['attempts.sqlite']]);self.assertFalse(h['LIVE_GATE_exists'])
    def test_old_authority_and_other_bounds_rejected(self):
        old=p.read('basis/admission-r01.json')
        with self.assertRaises(Exception):b.prepare(self.r,old,**self.trusted(a=old))
        for val in (64,1023,1025):
            r=copy.deepcopy(self.r);r['max_output_tokens']=val
            with self.assertRaises(Exception):b.request_hash(r)
        with self.assertRaises(Exception):b.prepare(self.r,self.a,**dict(self.trusted(),now_tick=2))
    def test_exact_metadata_dependencies(self):
        h=p.read('basis/host-readonly.json')
        for name,sha in h['module_sha256'].items():
            if name!='bridge.py':self.assertEqual(b.sha((b.ROOT/name).read_bytes()),sha)
    def test_offline_reasoning_only_metadata_no_candidate_and_no_replay(self):
        # New r02 REAL authority is only prepared, never executed. Fake attempt uses test identity.
        a=copy.deepcopy(self.a);a['execution_mode']='OFFLINE_TEST';a['authority_id']='TEST_ONLY_UTILITY_BRIDGE_R01'
        class Resolver:
            def resolve(self,ref):
                class Secret:provider='openai';value='SYNTHETIC_NOT_A_CREDENTIAL'
                return Secret()
        class Client:
            calls=0
            def request(self,**kw):
                self.calls+=1
                return 200,b.canon({'model':b.MODEL,'status':'incomplete','incomplete_details':{'reason':'max_output_tokens'},
                  'max_output_tokens':1024,'output':[{'type':'reasoning','content':'SYNTHETIC_PRIVATE_MARKER'}]})
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);c=Client()
            def run():return b.execute(self.r,a,**self.trusted(a=a),directory=root,resolver=Resolver(),client=c,
              attest_execution=lambda mode,client,resolver:mode=='OFFLINE_TEST' and type(client) is Client and type(resolver) is Resolver)
            with self.assertRaisesRegex(Exception,'BLOCKED_PROVIDER_RESPONSE'):run()
            files=list((root/'metadata').glob('*.json'));self.assertEqual(len(files),1)
            raw=files[0].read_text();rec=json.loads(raw);self.assertNotIn('SYNTHETIC_PRIVATE_MARKER',raw)
            self.assertEqual(rec['fields']['max_output_tokens']['value'],1024)
            self.assertFalse((root/'reviews').exists());self.assertEqual(rec['project_acceptance'],'NOT_GRANTED');self.assertFalse(rec['project_state_mutation'])
            with self.assertRaisesRegex(Exception,'BLOCKED_DUPLICATE_CALL'):run()
            self.assertEqual(c.calls,1)
    def test_saved_artifacts_recompute_exactly(self):
        for name,obj in self.art.items():self.assertEqual((p.ROOT/name).read_bytes(),b.canon(obj)+b'\n')

if __name__=='__main__':unittest.main()
