import json,tempfile,unittest
from pathlib import Path
from static_preview import *
BASE=Path(__file__).resolve().parent
class Readback(unittest.TestCase):
 @classmethod
 def setUpClass(c):c.fx=[parse_fixture(p,False) for p in sorted((BASE/'fixtures').glob('*.md'))]
 def test_11_forbidden(self):
  h,_=render(self.fx);[self.assertNotIn(f.split('.')[-1],h) for x in self.fx for f in x['metadata']['public_display_forbidden_fields']]
 def test_12_nav(self):
  h,_=render(self.fx);nav=h.split('</ul>',1)[0];self.assertNotIn('synthetic-blocked-001',nav);self.assertNotIn('synthetic-secret-like-001',nav)
 def test_13_prewrite_unverified(self):
  _,r=render(self.fx);self.assertTrue(all(not x['readback_confirmed'] and x['phase']=='build' for x in r))
 def test_14_deterministic(self):self.assertEqual(build(BASE,False)['deterministic_identity'],build(BASE,False)['deterministic_identity'])
 def test_15_blob_guard(self):
  src=BASE/'fixtures/POSITIVE-PUBLIC-READY.md'
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/src.name;p.write_bytes(src.read_bytes()+b'\nmutation')
   with self.assertRaises(ContractError):parse_fixture(p,True)
 def test_16_phase_identity(self):
  r=build(BASE,False);self.assertEqual(r['phase'],'post_build_readback');self.assertTrue(r['observed_preview']['identity_match']);self.assertEqual(r['readback_confirmed_count'],6)
 def test_17_all_assertions(self):
  r=build(BASE,False);expected=sum(len(x['metadata']['expected_readback_assertions']) for x in self.fx);seen=sum(len(x['assertion_results']) for x in r['fixture_results']);self.assertEqual((expected,seen,r['assertion_pass_count'],r['assertion_fail_count']),(31,31,31,0))
 def test_18_observed_failure(self):
  h,_=render(self.fx);raw=h.replace('CANDIDATE / NOT CURRENT','CANDIDATE / CHANGED').encode()
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/'preview.html';p.write_bytes(raw);exp={'git_blob_sha1':git_blob_sha(raw),'sha256':sha256(raw)};r=post_build_readback(p,self.fx,exp);row=next(x for x in r['fixture_results'] if x['fixture']=='CANDIDATE-RESEARCH.md');self.assertIn('candidate_badge_persistent',[x['assertion'] for x in row['failures']])
 def test_19_identity_failure(self):
  h,_=render(self.fx);raw=h.encode();exp={'git_blob_sha1':git_blob_sha(raw),'sha256':sha256(raw)}
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/'preview.html';p.write_bytes(raw+b'X');r=post_build_readback(p,self.fx,exp);self.assertFalse(r['readback_pass']);self.assertEqual(r['readback_confirmed_count'],0)
 def test_20_exact_preview(self):
  r=build(BASE,False);self.assertEqual(r['observed_preview']['observed_git_blob_sha1'],'ed85ce20409237c1738f847e2ee38f0319cdd618');self.assertEqual(r['observed_preview']['observed_sha256'],'6acfc8a2c5ec9698641ba93a8e3ff36085b02be988bdb2050efb8af8df57f25b')
