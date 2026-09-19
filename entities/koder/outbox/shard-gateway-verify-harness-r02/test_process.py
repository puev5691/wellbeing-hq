import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
INV=json.loads((HERE/"INVOCATION.json").read_text())

def argv(values):
    return [values.get(x[1:-1],x) if x.startswith("{") and x.endswith("}") else x for x in INV["argv_template"]]

class ProcessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        required=os.environ.get("WB_TEST_ADAPTER")
        if not required: raise RuntimeError("WB_TEST_ADAPTER required")
        cls.adapter=Path(required).resolve()
        cls.harness=(HERE/"harness.py").resolve()
        cls.audit_module=(HERE/"audit_sink.py").resolve()

    def setUp(self):
        self.t=tempfile.TemporaryDirectory(); self.addCleanup(self.t.cleanup)
        self.d=Path(self.t.name)
        self.req=self.d/"request.json"; self.audit=self.d/"audit.jsonl"
        self.cwd=self.d/"unrelated"; self.cwd.mkdir()
        self.mal=self.d/"ambient"; self.mal.mkdir()
        (self.mal/"audit_sink.py").write_text("raise RuntimeError('AMBIENT_SUBSTITUTION')\n")
        self.base={"python":sys.executable,"harness":str(self.harness),"adapter":str(self.adapter),
                   "audit_module":str(self.audit_module),"request_file":str(self.req),"audit":str(self.audit)}

    def run_proc(self,values=None):
        vals=dict(self.base); vals.update(values or {})
        env={"PATH":"/usr/bin:/bin","LC_ALL":"C","PYTHONPATH":str(self.mal),"PRIVATE_FIXTURE_VALUE":"DO_NOT_LEAK"}
        return subprocess.run(argv(vals),cwd=self.cwd,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=10)

    def request(self,**kw):
        o={"schema":"wb.shard_gateway.request.v1","request_id":"p1","requester_entity":"KOD",
           "authority_ref":"fixture://authority","host_id":"burzh","mode":"VERIFY","operation":"READ_BOUNDED",
           "root_id":"BURZH_REPO_WELLBEING_HQ","relative_path":"fixture.txt","max_output_bytes":1048576}
        o.update(kw); self.req.write_text(json.dumps(o,separators=(",",":")))

    def lines(self): return self.audit.read_bytes().splitlines() if self.audit.exists() else []

    def test_p1_valid_supervisor_invocation(self):
        self.request()
        p=self.run_proc()
        self.assertEqual(p.returncode,0,p.stderr.decode())
        self.assertEqual(len(p.stdout.splitlines()),1)
        self.assertTrue(json.loads(p.stdout)["ok"])
        self.assertEqual(len(self.lines()),1)

    def test_p2_invalid_input_redacted_audit(self):
        self.req.write_bytes(b'{"broken":')
        p=self.run_proc()
        self.assertEqual(p.returncode,64)
        self.assertEqual(json.loads(p.stdout)["error_code"],"REQUEST_JSON_INVALID")
        self.assertEqual(len(self.lines()),1)

    def test_p2_adapter_identity_failure_audited(self):
        self.request()
        bad=self.d/"gateway_bad.py"; bad.write_bytes(self.adapter.read_bytes()+b"\n#tamper\n")
        p=self.run_proc({"adapter":str(bad)})
        self.assertEqual(p.returncode,65)
        self.assertEqual(json.loads(p.stdout)["error_code"],"ADAPTER_IDENTITY_MISMATCH")
        self.assertEqual(len(self.lines()),1)

    def test_p3_audit_failure_exit70(self):
        self.request(); adir=self.d/"audit-dir"; adir.mkdir()
        p=self.run_proc({"audit":str(adir)})
        self.assertEqual(p.returncode,70)
        self.assertEqual(json.loads(p.stdout)["error_code"],"AUDIT_APPEND_FAILED")

    def test_p4_cwd_pythonpath_ambient_independence(self):
        self.request()
        p=self.run_proc()
        self.assertEqual(p.returncode,0,p.stderr.decode())
        self.assertNotIn(b"AMBIENT_SUBSTITUTION",p.stderr+p.stdout)
        self.assertNotEqual(self.cwd,self.harness.parent)

    def test_p5_write_rejected_no_expansion(self):
        self.request(mode="WRITE")
        p=self.run_proc()
        self.assertEqual(p.returncode,20)
        self.assertEqual(json.loads(p.stdout)["error_code"],"WRITE_MODE_NOT_AUTHORIZED")
        self.assertEqual(len(self.lines()),1)
        audit=self.lines()[0]
        self.assertNotIn(b"DO_NOT_LEAK",audit)

    def test_invocation_template_production_and_fixture_same_shape(self):
        prod=argv(INV["production"])
        fixture=argv(self.base)
        self.assertEqual([x if not x.startswith("/") else "<PATH>" for x in prod],
                         [x if not x.startswith("/") else "<PATH>" for x in fixture])

if __name__=="__main__": unittest.main(verbosity=2)
