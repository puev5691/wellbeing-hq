import json, os, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import gateway

def req(**kw):
 x={"schema":gateway.SCHEMA_REQUEST,"request_id":"req-1","requester_entity":"KOD","authority_ref":"fixture://authority","host_id":"mazhor","mode":"VERIFY","operation":"STAT","root_id":"MAZHOR_REPO_WELLBEING_HQ","relative_path":"a.txt","max_output_bytes":gateway.MAX_OUTPUT_BYTES}
 x.update(kw); return gateway.canonical_bytes(x)

class T(unittest.TestCase):
 def setUp(self):
  td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup)
  self.root=Path(td.name); (self.root/"a.txt").write_text("alpha"); (self.root/"dir").mkdir(); (self.root/"dir"/"b.txt").write_text("beta")
  self.gw=gateway.Gateway(lambda h,r:self.root)
 def code(self,raw): return self.gw.execute(raw).error_code
 def test_exact_opcode_enum(self):
  self.assertEqual({x.value for x in gateway.Opcode},{"STAT","LIST_DIR","READ_BOUNDED","SHA256","ARCHIVE_LIST","GIT_STATUS_PORCELAIN","GIT_HEAD","GIT_HEAD_TREE","GIT_LS_TREE","GIT_BLOB_META","GIT_BLOB_READ_BOUNDED"})
 def test_unknown_opcode(self): self.assertEqual(self.code(req(operation="SHELL")),"OP_NOT_ALLOWED")
 def test_unknown_root(self): self.assertEqual(self.code(req(root_id="OTHER")),"ROOT_NOT_ALLOWED")
 def test_absolute_path(self): self.assertEqual(self.code(req(relative_path="/etc/passwd")),"ABSOLUTE_PATH_DENIED")
 def test_traversal(self):
  self.assertEqual(self.code(req(relative_path="../a.txt")),"PATH_TRAVERSAL_DENIED")
  self.assertEqual(self.code(req(relative_path="dir//b.txt")),"PATH_TRAVERSAL_DENIED")
 def test_symlink(self):
  (self.root/"link").symlink_to(self.root/"a.txt"); self.assertEqual(self.code(req(relative_path="link")),"SYMLINK_NOT_ALLOWED")
 def test_denied_target(self):
  (self.root/".env").write_text("X"); self.assertEqual(self.code(req(relative_path=".env")),"DENIED_TARGET")
  (self.root/".ssh").mkdir(); (self.root/".ssh"/"id").write_text("X"); self.assertEqual(self.code(req(relative_path=".ssh/id")),"DENIED_TARGET")
 def test_oversized_output(self):
  (self.root/"big.txt").write_bytes(b"x"*100)
  self.assertEqual(self.code(req(operation="READ_BOUNDED",relative_path="big.txt",max_output_bytes=10)),"LIMIT_EXCEEDED")
 def test_timeout(self):
  with patch("subprocess.run",side_effect=__import__("subprocess").TimeoutExpired(["git"],1)):
   self.assertEqual(self.code(req(operation="GIT_HEAD",relative_path="")),"TIMEOUT")
 def test_target_changed_race(self):
  original=gateway._ident; calls={"n":0}
  def changed(st):
   calls["n"]+=1; x=original(st)
   return x if calls["n"]==1 else (x[0],x[1],x[2]+1,x[3])
  with patch("gateway._ident",side_effect=changed):
   self.assertEqual(self.code(req(operation="READ_BOUNDED")),"TARGET_CHANGED")
 def test_write_attempt(self):
  self.assertEqual(self.code(req(mode="WRITE")),"WRITE_MODE_NOT_AUTHORIZED")
  o=json.loads(req()); o["command"]="rm -rf /"; self.assertEqual(self.code(gateway.canonical_bytes(o)),"OP_NOT_ALLOWED")
 def test_no_automatic_failover(self):
  self.assertEqual(self.code(req(fallback_host_id="burzh",equivalent_object_ref="eq-1")),"HOST_UNAVAILABLE")
 def test_canonical_and_audit(self):
  raw=req(operation="SHA256"); parsed=gateway.parse_request(raw); result=self.gw.execute(raw)
  self.assertEqual(gateway.serialize_result(result),gateway.serialize_result(result))
  a=json.loads(gateway.serialize_audit(parsed,result,7)); self.assertEqual(a["schema"],"wb.shard_gateway.audit.v1"); self.assertEqual(a["mode"],"VERIFY")
 def test_host_mapping_exact(self):
  self.assertEqual(gateway.HOST_ROOTS,{"mazhor":{"MAZHOR_REPO_WELLBEING_HQ":"/data/wellbeing-lab/repos/wellbeing-hq","MAZHOR_ARCHIVE_SHD_PRE_REINIT_V01":"/data/wellbeing-lab/backups/shd-pre-reinit-v01"},"burzh":{"BURZH_REPO_WELLBEING_HQ":"/home/pev5691/wellbeing-hq"}})
 def test_concurrency_one(self):
  self.assertEqual(gateway.CONCURRENCY.locks["mazhor"]._value,1); self.assertEqual(gateway.CONCURRENCY.locks["burzh"]._value,1)

if __name__=="__main__": unittest.main(verbosity=2)
