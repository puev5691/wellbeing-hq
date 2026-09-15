import copy, tempfile, unittest
from pathlib import Path
from static_preview import *
from post_build_readback import verify
BASE=Path(__file__).resolve().parent
class T(unittest.TestCase):
 @classmethod
 def setUpClass(c):c.fx=[parse_fixture(p,False) for p in sorted((BASE/'fixtures').glob('*.md'))];c.by={x['name']:x for x in c.fx}
 def test_01_sixty_fields(self):self.assertEqual(len(REQ),60);[self.assertEqual(set(x['metadata']),set(REQ)) for x in self.fx]
 def test_02_classify(self):
  for x in self.fx:self.assertEqual(classify(x['metadata'])[:2],(x['metadata']['expected_navigation_bucket'],x['metadata']['expected_primary_badge']))
 def test_03_fail_closed(self):
  m=self.by['POSITIVE-PUBLIC-READY.md']['metadata']
  for k,v in [('public_legal_outcome','blocked'),('public_legal_outcome','unknown'),('security_state','unknown'),('security_state','blocked_secret'),('secret_dependency',True),('rights_basis','unknown'),('representation_state','representation_blocked'),('release_state','release_blocked'),('editorial_status','editorial_blocked')]:n=copy.deepcopy(m);n[k]=v;self.assertEqual(classify(n)[2],'blocked')
 def test_04_secret(self):m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['title']='token=FAKEVALUE123456';self.assertIn('unresolved_secret_like',validate(m))
 def test_05_promotion(self):
  with self.assertRaises(ContractError):validate_config({'mode':'local-static-v01','include_internal_quarantine':True,'force_public_ready':True})
 def test_06_synth_identity(self):m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['immutable_identity']['id']='wrong';self.assertIn('synthetic_immutable_mismatch',validate(m))
 def test_07_git_identity(self):m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m.update(source_repository='repo',source_path='x',source_commit='a'*40,source_blob='b'*40,synthetic=False);m['immutable_identity']={'scheme':'git-blob','id':'b'*40};self.assertEqual(validate(m),[]);m['immutable_identity']['id']='c'*40;self.assertIn('git_immutable_mismatch',validate(m))
 def test_08_supersede(self):m=copy.deepcopy(self.by['SUPERSEDED.md']['metadata']);m['editorial_superseded_by']='synthetic-fixture://bad';self.assertIn('supersede_lineage',validate(m))
 def test_09_successor(self):m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['superseded_by']=['synthetic-fixture://next'];self.assertIn('successor_conflict',validate(m))
 def test_10_derivative(self):m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['derivative_of']='bad';self.assertIn('derivative_parent_identity',validate(m));m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['derivative_type']='magic';self.assertIn('derivative_type',validate(m))
 def test_11_withdrawal(self):m=copy.deepcopy(self.by['WITHDRAWN.md']['metadata']);m['withdrawal_state']='none';self.assertIn('withdrawal_lineage',validate(m))
 def test_12_forbidden(self):h,r=render(self.fx);[self.assertNotIn(f.split('.')[-1],h) for x in self.fx for f in x['metadata']['public_display_forbidden_fields']]
 def test_13_nav(self):h,r=render(self.fx);nav=h.split('</ul>',1)[0];self.assertNotIn('synthetic-blocked-001',nav);self.assertNotIn('synthetic-secret-like-001',nav)
 def test_14_build_does_not_self_confirm(self):h,r=render(self.fx);self.assertTrue(all(x['readback_confirmed'] is False for x in r));self.assertTrue(all(x['assertions']==[] for x in r))
 def test_15_deterministic(self):self.assertEqual(build(BASE,False)['deterministic_identity'],build(BASE,False)['deterministic_identity'])
 def test_16_blob_mismatch(self):
  src=BASE/'fixtures/POSITIVE-PUBLIC-READY.md'
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/src.name;p.write_bytes(src.read_bytes()+b'\nmutation')
   with self.assertRaises(ContractError):parse_fixture(p,True)
 def test_17_post_build_phase_and_identity(self):
  s=build(BASE,False);i=s['expected_preview_identity'];r=verify(BASE,i['git_blob'],i['sha256'],False);self.assertEqual(r['phase'],'post_build_readback');self.assertTrue(r['identity_match']);self.assertEqual(r['status'],'PASS')
 def test_18_all_named_assertions_executed(self):
  s=build(BASE,False);i=s['expected_preview_identity'];r=verify(BASE,i['git_blob'],i['sha256'],False);self.assertEqual(sum(len(x['assertion_evidence']) for x in r['fixture_results']),sum(len(x['metadata']['expected_readback_assertions']) for x in self.fx));self.assertTrue(all(e['assertion_result']=='PASS' for x in r['fixture_results'] for e in x['assertion_evidence']))
 def test_19_identity_mismatch_fails(self):s=build(BASE,False);i=s['expected_preview_identity'];r=verify(BASE,'0'*40,i['sha256'],False);self.assertEqual(r['status'],'FAIL');self.assertEqual(r['readback_confirmed_count'],0)
 def test_20_report_failures_observed(self):
  s=build(BASE,False);i=s['expected_preview_identity'];p=BASE/'preview.html';good=p.read_bytes();p.write_bytes(good.replace(b'PUBLIC-READY / SYNTHETIC',b'BROKEN',1));r=verify(BASE,git_blob_sha(p.read_bytes()),__import__('hashlib').sha256(p.read_bytes()).hexdigest(),False);self.assertEqual(r['status'],'FAIL');self.assertTrue(r['failures']);p.write_bytes(good)
if __name__=='__main__':unittest.main(verbosity=2)
