import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import harness
import audit_sink

def load_module(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod; spec.loader.exec_module(mod); return mod

class HarnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        adapter_path=os.environ.get("WB_TEST_ADAPTER")
        if not adapter_path: raise RuntimeError("WB_TEST_ADAPTER required")
        cls.adapter_path=Path(adapter_path)
        cls.gateway=load_module(cls.adapter_path,"gateway_test_exact")

    def setUp(self):
        td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup)
        self.dir=Path(td.name)
        self.root=self.dir/"root"; self.root.mkdir()
        (self.root/"a.txt").write_text("alpha")
        self.audit=self.dir/"audit.jsonl"
        self.request=self.dir/"request.json"
        self.request.write_bytes(self.valid_request())
        actual=self.gateway
        outer=self
        class FixtureGateway(actual.Gateway):
            def __init__(self): super().__init__(lambda h,r:outer.root)
        self.proxy=SimpleNamespace(Gateway=FixtureGateway,serialize_result=actual.serialize_result)

    def valid_request(self,**kw):
        o={"schema":"wb.shard_gateway.request.v1","request_id":"req-1","requester_entity":"KOD",
           "authority_ref":"fixture://authority","host_id":"mazhor","mode":"VERIFY","operation":"READ_BOUNDED",
           "root_id":"MAZHOR_REPO_WELLBEING_HQ","relative_path":"a.txt","max_output_bytes":1048576}
        o.update(kw)
        return json.dumps(o,ensure_ascii=False,separators=(",",":")).encode()

    def run_main(self,adapter=None):
        argv=["--adapter",str(self.adapter_path),"--request-file",str(self.request),"--audit",str(self.audit)]
        out=io.BytesIO(); fake_stdout=SimpleNamespace(buffer=out)
        with patch.object(harness,"load_adapter",return_value=adapter or self.proxy), patch.object(harness.sys,"stdout",fake_stdout):
            code=harness.main(argv)
        return code,out.getvalue()

    def audit_lines(self):
        return self.audit.read_bytes().splitlines() if self.audit.exists() else []

    def test_valid_one_shot_canonical_stdout(self):
        code,out=self.run_main()
        self.assertEqual(code,harness.EXIT_OK)
        self.assertEqual(len(out.splitlines()),1)
        parsed=json.loads(out)
        self.assertTrue(parsed["ok"]); self.assertEqual(parsed["payload"]["text"],"alpha")

    def test_invalid_request_and_write_rejected(self):
        self.request.write_bytes(self.valid_request(mode="WRITE"))
        code,out=self.run_main()
        self.assertEqual(code,harness.EXIT_GATEWAY_REJECTED)
        self.assertEqual(json.loads(out)["error_code"],"WRITE_MODE_NOT_AUTHORIZED")
        self.assertEqual(len(self.audit_lines()),1)

    def test_request_size_overflow_and_trailing_input(self):
        self.request.write_bytes(b"x"*(harness.MAX_REQUEST_BYTES+1))
        code,out=self.run_main(); self.assertEqual(code,harness.EXIT_INPUT)
        self.assertEqual(json.loads(out)["error_code"],"REQUEST_SIZE_INVALID")
        self.assertEqual(len(self.audit_lines()),0)
        self.request.write_bytes(self.valid_request()+b"{}")
        code,out=self.run_main(); self.assertEqual(code,harness.EXIT_INPUT)
        self.assertEqual(json.loads(out)["error_code"],"REQUEST_JSON_INVALID")

    def test_no_shell_interpretation(self):
        marker="literal:semicolon|dollar$paren()"
        self.request.write_bytes(self.valid_request(relative_path=marker))
        code,_=self.run_main()
        self.assertEqual(code,harness.EXIT_GATEWAY_REJECTED)
        self.assertFalse((self.root/marker).exists())

    def test_verify_only_exactly_one_execute(self):
        calls={"n":0}; actual=self.proxy.Gateway
        class CountGateway(actual):
            def execute(self,raw): calls["n"]+=1; return super().execute(raw)
        proxy=SimpleNamespace(Gateway=CountGateway,serialize_result=self.gateway.serialize_result)
        code,_=self.run_main(adapter=proxy)
        self.assertEqual(code,0); self.assertEqual(calls["n"],1)

    def test_audit_exactly_once_no_payload_or_env_secret(self):
        os.environ["TEST_PRIVATE_VALUE"]="PRIVATE_MARKER"
        try:
            code,_=self.run_main(); self.assertEqual(code,0)
            lines=self.audit_lines(); self.assertEqual(len(lines),1)
            audit=lines[0]
            self.assertNotIn(b"alpha",audit); self.assertNotIn(b"PRIVATE_MARKER",audit)
            self.assertEqual(json.loads(audit)["schema"],"wb.shard_gateway.audit.v1")
        finally: os.environ.pop("TEST_PRIVATE_VALUE",None)

    def test_audit_failure_fail_closed(self):
        out=io.BytesIO(); fake_stdout=SimpleNamespace(buffer=out)
        with patch.object(harness,"load_adapter",return_value=self.proxy), patch("audit_sink.append_record",side_effect=audit_sink.AuditSinkError("X")), patch.object(harness.sys,"stdout",fake_stdout):
            code=harness.main(["--adapter",str(self.adapter_path),"--request-file",str(self.request),"--audit",str(self.audit)])
        self.assertEqual(code,harness.EXIT_AUDIT)
        self.assertEqual(json.loads(out.getvalue())["error_code"],"AUDIT_APPEND_FAILED")

    def test_audit_partial_write_is_failure(self):
        with patch("audit_sink.os.write",return_value=0):
            with self.assertRaises(audit_sink.AuditSinkError):
                audit_sink.append_record(self.audit,{"schema":"wb.shard_gateway.audit.v1"})

    def test_exit_contract_rejected(self):
        self.request.write_bytes(self.valid_request(operation="NOPE"))
        code,out=self.run_main()
        self.assertEqual(code,20); self.assertFalse(json.loads(out)["ok"])
        self.assertEqual(len(self.audit_lines()),1)

    def test_adapter_identity_and_tamper_rejection(self):
        mod=harness.load_adapter(self.adapter_path); self.assertTrue(hasattr(mod,"Gateway"))
        bad=self.dir/"bad.py"; bad.write_bytes(self.adapter_path.read_bytes()+b"\n#changed\n")
        with self.assertRaisesRegex(RuntimeError,"ADAPTER_IDENTITY_MISMATCH"): harness.load_adapter(bad)

    def test_no_listener_or_credential_dependency(self):
        source=Path(harness.__file__).read_text()+Path(audit_sink.__file__).read_text()
        for bad in ("socket.","bind(","listen(","urllib","requests.","API_KEY"):
            self.assertNotIn(bad,source)

    def test_audit_symlink_denied(self):
        target=self.dir/"real.log"; target.write_text("")
        self.audit.symlink_to(target)
        with self.assertRaises(audit_sink.AuditSinkError): audit_sink.append_record(self.audit,{"x":1})

    def test_stdout_error_canonical_single_line(self):
        bad=self.dir/"bad.py"; bad.write_text("x")
        out=io.BytesIO(); fake_stdout=SimpleNamespace(buffer=out)
        with patch.object(harness.sys,"stdout",fake_stdout):
            code=harness.main(["--adapter",str(bad),"--request-file",str(self.request),"--audit",str(self.audit)])
        self.assertEqual(code,65); self.assertEqual(len(out.getvalue().splitlines()),1)
        self.assertEqual(out.getvalue().strip(),harness.canonical(json.loads(out.getvalue())))

    def test_request_file_read_once_bounded(self):
        with patch("builtins.open",wraps=open) as op: harness.read_request(self.request)
        self.assertEqual(op.call_count,1)

if __name__=="__main__": unittest.main(verbosity=2)
