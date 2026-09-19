import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import harness

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.d=Path(self.tmp.name)
    def test_supervisor_template_has_isolated_mode(self):
        spec=json.loads((Path(__file__).parent/"INVOCATION.json").read_text())
        self.assertEqual(spec["argv_template"][1:3],["-I","-B"])
        self.assertIn("--audit-module",spec["argv_template"])
        self.assertFalse(spec["working_directory_required"])
    def test_request_bound_and_trailing_rejected(self):
        p=self.d/"r.json"; p.write_bytes(b"x"*(harness.MAX_REQUEST_BYTES+1))
        with self.assertRaisesRegex(RuntimeError,"REQUEST_SIZE_INVALID"): harness.read_request(p)
        p.write_bytes(b'{"a":1}{}')
        with self.assertRaisesRegex(RuntimeError,"REQUEST_JSON_INVALID"): harness.read_request(p)
    def test_audit_module_identity_mismatch_fails(self):
        p=self.d/"audit_sink.py"; p.write_text("x=1")
        with self.assertRaisesRegex(RuntimeError,"AUDIT_MODULE_IDENTITY_MISMATCH"): harness.load_audit(p)
    def test_adapter_identity_mismatch_fails(self):
        p=self.d/"gateway.py"; p.write_text("x=1")
        with self.assertRaisesRegex(RuntimeError,"ADAPTER_IDENTITY_MISMATCH"): harness.load_adapter(p)
    def test_safe_meta_drops_unknown_payload(self):
        raw=json.dumps({"request_id":"r","synthetic_text":"SECRET","relative_path":"a.txt"}).encode()
        m=harness.safe_request_meta(raw)
        self.assertNotIn("synthetic_text",m)
        self.assertEqual(m["request_id"],"r")
    def test_no_sibling_import(self):
        src=Path(harness.__file__).read_text()
        self.assertNotIn("from audit_sink import",src)
        self.assertNotIn("import audit_sink",src)
    def test_no_network_or_credential_dependency(self):
        src=Path(harness.__file__).read_text()
        for bad in ("socket.","bind(","listen(","urllib","requests.","API_KEY","TOKEN="):
            self.assertNotIn(bad,src)
    def test_exit_codes_stable(self):
        self.assertEqual((harness.EXIT_OK,harness.EXIT_GATEWAY_REJECTED,harness.EXIT_INPUT,harness.EXIT_ADAPTER,harness.EXIT_AUDIT_MODULE,harness.EXIT_AUDIT),(0,20,64,65,66,70))

if __name__=="__main__": unittest.main(verbosity=2)
