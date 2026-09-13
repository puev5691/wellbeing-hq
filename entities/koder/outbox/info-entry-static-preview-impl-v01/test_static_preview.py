import copy, json, tempfile, unittest
from pathlib import Path
from static_preview import *
BASE=Path(__file__).resolve().parent
class T(unittest.TestCase):
 @classmethod
 def setUpClass(c):
  c.fx=[parse_fixture(p,False) for p in sorted((BASE/'fixtures').glob('*.md'))]; c.by={x['name']:x for x in c.fx}
 def test_01_sixty_fields_preserved(self):
  self.assertEqual(len(REQ),60); [self.assertEqual(set(x['metadata']),set(REQ)) for x in self.fx]
 def test_02_six_fixtures_classify_as_expected(self):
  for x in self.fx:
   b,g,_=classify(x['metadata']); self.assertEqual((b,g),(x['metadata']['expected_navigation_bucket'],x['metadata']['expected_primary_badge']))
 def test_03_blocked_unknown_secret_fail_closed(self):
  m=self.by['POSITIVE-PUBLIC-READY.md']['metadata']
  for k,v in [('public_legal_outcome','blocked'),('public_legal_outcome','unknown'),('security_state','unknown'),('security_state','blocked_secret'),('secret_dependency',True),('rights_basis','unknown'),('representation_state','representation_blocked'),('release_state','release_blocked'),('editorial_status','editorial_blocked')]:
   n=copy.deepcopy(m);n[k]=v;self.assertEqual(classify(n)[2],'blocked')
 def test_04_secret_like_unresolved_fails(self):
  m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['title']='token=FAKEVALUE123456';self.assertIn('unresolved_secret_like',validate(m))
 def test_05_renderer_promotion_fails(self):
  with self.assertRaises(ContractError):validate_config({'mode':'local-static-v01','include_internal_quarantine':True,'force_public_ready':True})
 def test_06_synthetic_identity_mismatch(self):
  m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['immutable_identity']['id']='wrong';self.assertIn('synthetic_immutable_mismatch',validate(m))
 def test_07_git_identity_positive_and_mismatch(self):
  m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m.update(source_repository='repo',source_path='x',source_commit='a'*40,source_blob='b'*40,synthetic=False);m['immutable_identity']={'scheme':'git-blob','id':'b'*40};self.assertEqual(validate(m),[]);m['immutable_identity']['id']='c'*40;self.assertIn('git_immutable_mismatch',validate(m))
 def test_08_supersede_lineage(self):
  m=copy.deepcopy(self.by['SUPERSEDED.md']['metadata']);m['editorial_superseded_by']='synthetic-fixture://bad';self.assertIn('supersede_lineage',validate(m))
 def test_09_current_successor_conflict(self):
  m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['superseded_by']=['synthetic-fixture://next'];self.assertIn('successor_conflict',validate(m))
 def test_10_derivative_lineage(self):
  m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['derivative_of']='bad';self.assertIn('derivative_parent_identity',validate(m));m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['derivative_type']='magic';self.assertIn('derivative_type',validate(m))
 def test_11_withdrawal_lineage(self):
  m=copy.deepcopy(self.by['WITHDRAWN.md']['metadata']);m['withdrawal_state']='none';self.assertIn('withdrawal_lineage',validate(m))
 def test_12_forbidden_fields_suppressed(self):
  h,r=render(self.fx);[self.assertNotIn(f.split('.')[-1],h) for x in self.fx for f in x['metadata']['public_display_forbidden_fields']]
 def test_13_blocked_absent_public_nav(self):
  h,r=render(self.fx);nav=h.split('</ul>',1)[0];self.assertNotIn('synthetic-blocked-001',nav);self.assertNotIn('synthetic-secret-like-001',nav)
 def test_14_states_distinct(self):
  h,r=render(self.fx);d={x['fixture']:x for x in r};self.assertEqual((d['POSITIVE-PUBLIC-READY.md']['preview_ready'],d['POSITIVE-PUBLIC-READY.md']['release_authorized'],d['POSITIVE-PUBLIC-READY.md']['readback_confirmed']),(True,True,True));self.assertEqual((d['CANDIDATE-RESEARCH.md']['preview_ready'],d['CANDIDATE-RESEARCH.md']['release_authorized'],d['CANDIDATE-RESEARCH.md']['readback_confirmed']),(True,False,True))
 def test_15_deterministic_build(self):
  a=build(BASE,False)['deterministic_identity'];b=build(BASE,False)['deterministic_identity'];self.assertEqual(a,b)
 def test_16_blob_identity_mismatch_fails_closed(self):
  src=BASE/'fixtures/POSITIVE-PUBLIC-READY.md'
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/src.name;p.write_bytes(src.read_bytes()+b'\nmutation')
   self.assertNotEqual(git_blob_sha(p.read_bytes()),EXPECTED_BLOBS[p.name])
   with self.assertRaises(ContractError):parse_fixture(p,True)
if __name__=='__main__':unittest.main(verbosity=2)
