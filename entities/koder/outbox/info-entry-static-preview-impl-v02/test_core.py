import copy,tempfile,unittest
from pathlib import Path
from static_preview import *
BASE=Path(__file__).resolve().parent
class Core(unittest.TestCase):
 @classmethod
 def setUpClass(c):c.fx=[parse_fixture(p,False) for p in sorted((BASE/'fixtures').glob('*.md'))];c.by={x['name']:x for x in c.fx}
 def test_01_fields(self):self.assertEqual(len(REQ),60);[self.assertEqual(set(x['metadata']),set(REQ)) for x in self.fx]
 def test_02_classify(self):
  for x in self.fx:self.assertEqual(classify(x['metadata'])[:2],(x['metadata']['expected_navigation_bucket'],x['metadata']['expected_primary_badge']))
 def test_03_fail_closed(self):
  m=self.by['POSITIVE-PUBLIC-READY.md']['metadata']
  for k,v in [('public_legal_outcome','blocked'),('public_legal_outcome','unknown'),('security_state','unknown'),('security_state','blocked_secret'),('secret_dependency',True),('rights_basis','unknown'),('representation_state','representation_blocked'),('release_state','release_blocked')]:
   n=copy.deepcopy(m);n[k]=v;self.assertEqual(classify(n)[2],'blocked')
 def test_04_secret(self):
  m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['title']='token=FAKEVALUE123456';self.assertIn('unresolved_secret_like',validate(m))
 def test_05_promotion(self):
  with self.assertRaises(ContractError):validate_config({'mode':'local-static-v01','include_internal_quarantine':True,'force_public_ready':True})
 def test_06_synthetic_identity(self):
  m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['immutable_identity']['id']='wrong';self.assertIn('synthetic_immutable_mismatch',validate(m))
 def test_07_git_identity(self):
  m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m.update(source_repository='repo',source_path='x',source_commit='a'*40,source_blob='b'*40,synthetic=False);m['immutable_identity']={'scheme':'git-blob','id':'b'*40};self.assertEqual(validate(m),[]);m['immutable_identity']['id']='c'*40;self.assertIn('git_immutable_mismatch',validate(m))
 def test_08_supersede(self):
  m=copy.deepcopy(self.by['SUPERSEDED.md']['metadata']);m['editorial_superseded_by']='synthetic-fixture://bad';self.assertIn('supersede_lineage',validate(m))
 def test_09_current_successor(self):
  m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['superseded_by']=['synthetic-fixture://next'];self.assertIn('successor_conflict',validate(m))
 def test_10_derivative_withdrawal(self):
  m=copy.deepcopy(self.by['POSITIVE-PUBLIC-READY.md']['metadata']);m['derivative_of']='bad';self.assertIn('derivative_parent_identity',validate(m));w=copy.deepcopy(self.by['WITHDRAWN.md']['metadata']);w['withdrawal_state']='none';self.assertIn('withdrawal_lineage',validate(w))
