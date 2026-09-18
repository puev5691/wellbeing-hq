#!/usr/bin/env python3
import json,hashlib,tempfile,unittest,sys,socket,subprocess,os
from pathlib import Path
from types import ModuleType
P=Path(__file__).resolve().parent
m=ModuleType("_fas");m.__file__=str(P/"file_service.py");sys.modules[m.__name__]=m
exec(compile((P/"file_service.py").read_bytes(),m.__file__,"exec"),m.__dict__)
def h(b):return hashlib.sha256(b).hexdigest()
class T(unittest.TestCase):
  def fixture(self):
    td=tempfile.TemporaryDirectory();self.addCleanup(td.cleanup);r=Path(td.name);src=r/"src";out=r/"out";src.mkdir();out.mkdir()
    (src/"a.txt").write_bytes(b"alpha\n");(src/"z.bin").write_bytes(b"\x00\x01\x02")
    req={"schema":"file-artifact-service-request-r01","request_id":"req-1","package_id":"pkg-1","inputs":[
      {"source_id":"A","source_path":"a.txt","target_path":"docs/a.txt","sha256":h(b"alpha\n"),"size":6},
      {"source_id":"Z","source_path":"z.bin","target_path":"bin/z.bin","sha256":h(b"\x00\x01\x02"),"size":3}],
      "prior_manifest_path":None,"create_archive":True,"git_adapter_enabled":False}
    return r,src,out,req
  def execute_service(self,req,src,out):return m.execute((json.dumps(req,sort_keys=True)+"\n").encode(),src,out)
  def test_deterministic_package_and_archive(self):
    r,s,o,q=self.fixture();x=self.execute_service(q,s,o);a=(o/"package.tar.gz").read_bytes();man=(o/"package/MANIFEST.json").read_bytes()
    o2=r/"out2";o2.mkdir();y=self.execute_service(q,s,o2)
    self.assertEqual(a,(o2/"package.tar.gz").read_bytes());self.assertEqual(man,(o2/"package/MANIFEST.json").read_bytes());self.assertEqual(x,y)
  def test_manifest_inventory_exact(self):
    r,s,o,q=self.fixture();self.execute_service(q,s,o);man=json.loads((o/"package/MANIFEST.json").read_text())
    self.assertEqual([x["path"] for x in man["files"]],["bin/z.bin","docs/a.txt"])
    self.assertEqual(man["authority_semantics"],"none");self.assertEqual(man["project_state_semantics"],"none")
  def test_readback(self):
    r,s,o,q=self.fixture();self.execute_service(q,s,o);rb=json.loads((o/"readback.json").read_text())
    for x in rb["files"]:
      d=(o/"package"/x["path"]).read_bytes();self.assertEqual((h(d),len(d)),(x["sha256"],x["size"]))
  def test_hash_mismatch_fail_closed(self):
    r,s,o,q=self.fixture();q["inputs"][0]["sha256"]="0"*64
    with self.assertRaisesRegex(m.ServiceError,"SOURCE_HASH_MISMATCH"):self.execute_service(q,s,o)
  def test_size_mismatch_fail_closed(self):
    r,s,o,q=self.fixture();q["inputs"][0]["size"]=7
    with self.assertRaisesRegex(m.ServiceError,"SOURCE_SIZE_MISMATCH"):self.execute_service(q,s,o)
  def test_missing_source(self):
    r,s,o,q=self.fixture();q["inputs"][0]["source_path"]="missing"
    with self.assertRaisesRegex(m.ServiceError,"SOURCE_MISSING"):self.execute_service(q,s,o)
  def test_request_schema_closed(self):
    r,s,o,q=self.fixture();q["authority"]="writer"
    with self.assertRaisesRegex(m.ServiceError,"BAD_REQUEST_SCHEMA"):self.execute_service(q,s,o)
  def test_git_adapter_disabled(self):
    r,s,o,q=self.fixture();q["git_adapter_enabled"]=True
    with self.assertRaisesRegex(m.ServiceError,"GIT_ADAPTER_DISABLED"):self.execute_service(q,s,o)
    with self.assertRaisesRegex(m.ServiceError,"GIT_ADAPTER_DISABLED"):m.GitAdapter().publish()
  def test_diff(self):
    r,s,o,q=self.fixture();self.execute_service(q,s,o)
    prior={"schema":"file-artifact-manifest-r01","package_id":"old","files":[
      {"path":"docs/a.txt","sha256":h(b"alpha\n"),"size":6,"source_id":"A"},
      {"path":"gone.txt","sha256":h(b"x"),"size":1,"source_id":"X"}]}
    (s/"prior.json").write_text(json.dumps(prior));q["prior_manifest_path"]="prior.json";x=self.execute_service(q,s,o)
    self.assertEqual(x["diff"]["unchanged"],["docs/a.txt"]);self.assertEqual(x["diff"]["added"],["bin/z.bin"]);self.assertEqual(x["diff"]["removed"],["gone.txt"])
  def test_compact_result_no_paths_or_content(self):
    r,s,o,q=self.fixture();x=self.execute_service(q,s,o);raw=json.dumps(x)
    self.assertNotIn(str(s),raw);self.assertNotIn("alpha",raw);self.assertEqual(x["git_adapter"],"disabled")
  def test_zero_network(self):
    r,s,o,q=self.fixture();old=socket.socket
    def deny(*a,**k):raise AssertionError("NETWORK")
    socket.socket=deny
    try:self.execute_service(q,s,o)
    finally:socket.socket=old
  def test_no_subprocess_needed(self):
    r,s,o,q=self.fixture();old=subprocess.Popen
    def deny(*a,**k):raise AssertionError("PROCESS")
    subprocess.Popen=deny
    try:self.execute_service(q,s,o)
    finally:subprocess.Popen=old
if __name__=="__main__":
 r=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(T))
 print(json.dumps({"verdict":m.PASS if r.wasSuccessful() else "FAIL_FILE_ARTIFACT_SERVICE_TESTS","tests":r.testsRun,"failures":len(r.failures),"errors":len(r.errors),"skipped":len(r.skipped),"network_calls":0,"git_publications":0,"credentials":0,"authority_semantics":"none","project_state_semantics":"none"},sort_keys=True))
 raise SystemExit(0 if r.wasSuccessful() else 1)