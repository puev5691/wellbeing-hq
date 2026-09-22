import copy,json,tempfile,shutil,unittest
from pathlib import Path
import verifier as v
from seal import seal
ROOT=Path(__file__).parent
class Preparation(unittest.TestCase):
    def blocked(self,code,fn,*args):
        with self.assertRaisesRegex(v.Rejected,'^'+code+'$'): fn(*args)
    def test_01_integrity_reproducible(self):
        self.assertEqual(v.structural(ROOT),'PASS')
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)/'copy';shutil.copytree(ROOT,r)
            seal(r);self.assertEqual((r/'MANIFEST.json').read_bytes(),(ROOT/'MANIFEST.json').read_bytes())
            self.assertEqual((r/'SHA256SUMS.txt').read_bytes(),(ROOT/'SHA256SUMS.txt').read_bytes())
            (r/'recovery/input.json').write_bytes(b'[]\n')
            self.blocked('BLOCKED_INTEGRITY',v.structural,r)
    def test_02_partial_state(self): self.assertEqual(v.frozen_state(ROOT),'PASS')
    def test_03_supersedes(self):
        self.assertEqual(v.specification(ROOT)['id'],'task-v2')
        self.blocked('BLOCKED_UNRESOLVED_CONFLICT',v.specification,ROOT,None,None,[])
    def test_04_raw_done(self):
        report=v.read(ROOT,'verifier-private/restoration-oracle.json');report['status']='DONE'
        self.blocked('FAIL_SEMANTIC',v.semantic,ROOT,report)
        self.assertEqual(v.read(ROOT,'recovery/history-index.json')['entries'][2]['status'],'historical_raw_unpromoted')
    def test_05_unknown(self):
        report=v.read(ROOT,'verifier-private/restoration-oracle.json');report['source_timezone']='UTC'
        self.blocked('FAIL_SEMANTIC',v.semantic,ROOT,report)
    def test_06_projection(self):
        p=v.projection(ROOT)
        self.assertNotIn('recovery/raw-noise.json',p)
        self.assertTrue(all(not k.startswith(('verifier-private/','provenance/','schemas/')) for k in p))
        self.assertNotIn((ROOT/'verifier-private/oracle.json').read_bytes(),p.values())
        self.assertEqual(sum(len(b) for k,b in p.items() if k.startswith('sources/')),192853)
        self.assertEqual(len([k for k in p if k.startswith('sources/')]),6)
    def test_07_missing(self):
        self.blocked('STOP_MISSING_EXACT_EVIDENCE',v.exact,ROOT,{'path':'recovery/absent','bytes':0,'sha256':'0'*64})
    def test_08_escalation(self):
        i=v.read(ROOT,'recovery/identity-authority.json');v.source_policy(i)
        i['project_writer']=True;self.blocked('BLOCKED_AUTHORITY',v.source_policy,i)
    def test_09_input_conflict(self):
        d=v.read(ROOT,'recovery/input.json');d[2]['amount']=5
        self.blocked('BLOCKED_INPUT_CONFLICT',v.unique_records,d)
    def test_10_read_bounds(self):
        for p in ['recovery/raw-noise.json','verifier-private/oracle.json','full-corpus','../oracle']:
            self.blocked('BLOCKED_RETRIEVAL',v.retrieve,ROOT,p)
        self.blocked('BLOCKED_LIMIT',v.retrieve,ROOT,'recovery/input.json',32,0)
        self.blocked('BLOCKED_LIMIT',v.retrieve,ROOT,'recovery/input.json',0,262144)
    def test_11_separate_gates(self):
        for a,b in [('PASS','FAIL'),('FAIL','PASS'),('FAIL','FAIL')]: self.blocked('BLOCKED_GATES',v.continuation_gate,a,b)
        self.assertEqual(v.semantic(ROOT,v.read(ROOT,'verifier-private/restoration-oracle.json')),'PASS')
        self.assertEqual(v.continuation_gate('PASS','PASS'),'GATES_SATISFIED_NOT_EXECUTION_AUTHORITY')
        self.blocked('BLOCKED_MAIN_NOT_AUTHORIZED',v.main_admission)
    def test_12_oracle_and_ledger(self):
        o=v.read(ROOT,'verifier-private/oracle.json')
        ledger={'consumed_indices':[3,4,5],'seen':v.unique_records(v.read(ROOT,'recovery/input.json')),'input_sha256':v.digest((ROOT/'recovery/input.json').read_bytes())}
        claims={'real_chat_continuity':False,'project_acceptance':False}
        self.assertEqual(v.result_check(ROOT,o,ledger,claims),'PASS')
        ledger['consumed_indices']=[0,1,2,3,4,5];self.blocked('FAIL_LEDGER',v.result_check,ROOT,o,ledger,claims)
        claims['real_chat_continuity']=True;self.blocked('FAIL_CLAIM',v.result_check,ROOT,o,ledger,claims)
    def test_13_isolation_contract(self):
        c=v.read(ROOT,'contracts/isolation.json')
        self.assertEqual(c['instances'],['OLD-01','NEW-01']);self.assertEqual(c['environment_allowlist'],[])
        for k in ['inherit_variables','inherit_memory_cache','inherit_transcript','oracle_access','project_writer']:self.assertIs(c[k],False)
        self.assertEqual(c['proof_level'],'PREPARATION_PROJECTION_ONLY_RUNTIME_NOT_TESTED')
    def test_14_authority_not_created(self):
        c=v.read(ROOT,'contracts/admission.json');self.assertIsNone(c['main_authority'])
        self.assertEqual(c['main_attempts_now'],0);self.assertEqual(c['future_main_attempts'],1)
        self.assertEqual(c['deadline_seconds'],5);self.assertEqual(c['automatic_retries'],0)
        self.assertIsNone(v.read(ROOT,'contracts/preservation.json')['independent_receipt'])
if __name__=='__main__': unittest.main()
