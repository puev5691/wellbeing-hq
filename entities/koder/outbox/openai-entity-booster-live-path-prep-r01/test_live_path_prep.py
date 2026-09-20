import json, os, tempfile, unittest
from pathlib import Path
import live_path_prep as lp

D0="Synthetic bounded request."
TASK_COMMIT="1"*40; TASK_BLOB="2"*40; WRITER_COMMIT="3"*40; WRITER_BLOB="4"*40

def req(mod,**changes):
    d={"request_id":"liveprep-001","entity_id":"KOD","role":"koder",
       "task_path":"entities/koordinator/outbox/synthetic-task.md","task_commit":TASK_COMMIT,"task_blob":TASK_BLOB,
       "writer_path":"entities/koder/current/synthetic-writer.md","writer_commit":WRITER_COMMIT,"writer_blob":WRITER_BLOB,
       "purpose":"future bounded OpenAI D0 booster probe","provider":"openai","model":"gpt-5.6-luna",
       "privacy_class":"synthetic_only","tools":(),"payload":D0,"source_locator":"fixture://openai-liveprep-r01",
       "source_sha256":"334d56225f1336cfe802b41a5cd82b1613252a4b74b35aa37bd3191202bd59f7",
       "max_output_tokens":64}
    d.update(changes); return mod.BoosterRequest(**d)

def auth(**changes):
    d={"authority_id":"auth-liveprep-001","entity_id":"KOD","task_commit":TASK_COMMIT,"writer_blob":WRITER_BLOB,
       "provider":"openai","model":"gpt-5.6-luna","privacy_class":"synthetic_only","data_class":"D0_SYNTHETIC",
       "tools":(),"credential_ref":"secretref:openai:wellbeing-entity-boosters-restricted","max_output_tokens":64,
       "max_response_bytes":16384,"timeout_seconds":30.0,"max_calls":1,"automatic_retries":0,"fallback":"none",
       "use_once":True,"live_execution_authorized":True,"valid_until_tick":100}
    d.update(changes); return lp.LiveAuthority(**d)

class ResolverOK:
    def __init__(self,worker): self.worker=worker; self.calls=0
    def resolve(self,ref): self.calls+=1; return self.worker.ResolvedSecret("openai","synthetic-test-secret")

class ResolverFail:
    def __init__(self): self.calls=0
    def resolve(self,ref): self.calls+=1; raise RuntimeError("NO_SECRET")

class Client:
    def __init__(self,status=200,body=None): self.calls=0; self.status=status; self.body=body
    def request(self,**kw):
        self.calls+=1
        body=self.body
        if body is None: body=json.dumps({"id":"resp_sentinel","model":"gpt-5.6-luna"}).encode()
        return self.status,body

class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.booster_path=Path(os.environ["BOOSTER_R02"])
        cls.worker_path=Path(os.environ["LIVE_WORKER"])
        cls.path=lp.LivePath(booster_path=cls.booster_path,worker_path=cls.worker_path)
        cls.mod=cls.path.booster

    def setUp(self):
        td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup)
        self.ledger=Path(td.name)/"ledger.sqlite"

    def test_valid_authority_reaches_sentinel_worker(self):
        p=self.path.prepare(req(self.mod),auth())
        resolver=ResolverOK(self.path.worker); client=Client()
        out=self.path.invoke_sentinel(p,ledger_path=self.ledger,resolver=resolver,client=client,now_tick=1)
        self.assertEqual(out["terminal_status"],"PASS_SENTINEL_LIVE_WORKER_BOUNDARY")
        self.assertEqual((resolver.calls,client.calls),(1,1))
        self.assertEqual(out["project_acceptance"],"NOT_GRANTED"); self.assertTrue(out["review_required"])

    def test_missing_or_wrong_authority_blocks_before_resolution(self):
        for a in [auth(live_execution_authorized=False),auth(entity_id="SIS"),auth(task_commit="9"*40),
                  auth(writer_blob="8"*40),auth(provider="anthropic"),auth(model="gpt-5.6-sol")]:
            with self.subTest(a=a):
                with self.assertRaises(lp.PrepError):
                    self.path.prepare(req(self.mod),a)

    def test_tools_privacy_data_class_block(self):
        with self.assertRaisesRegex(lp.PrepError,"BLOCKED_TOOL_AUTHORITY"):
            self.path.prepare(req(self.mod,tools=("shell",)),auth(tools=("shell",)))
        with self.assertRaisesRegex(lp.PrepError,"BLOCKED_PRIVACY_BOUNDARY"):
            self.path.prepare(req(self.mod,privacy_class="project_internal"),auth(privacy_class="project_internal"))
        with self.assertRaisesRegex(lp.PrepError,"BLOCKED_DATA_CLASS"):
            self.path.prepare(req(self.mod),auth(data_class="PROJECT"))

    def test_policy_bounds_retry_fallback_one_call(self):
        for a in [auth(max_calls=2),auth(automatic_retries=1),auth(fallback="openai-alt")]:
            with self.assertRaisesRegex(lp.PrepError,"BLOCKED_RETRY_FALLBACK_POLICY"):
                self.path.prepare(req(self.mod),a)
        p=self.path.prepare(req(self.mod),auth())
        wp=self.path.worker_plan(p)
        self.assertEqual((wp.policy.max_calls,wp.policy.automatic_retries),(1,0))

    def test_credential_reference_only(self):
        p=self.path.prepare(req(self.mod),auth())
        self.assertNotIn("synthetic-test-secret",repr(p))
        self.assertNotIn("credential_ref",json.dumps({"provider":p.provider,"model":p.model}))
        with self.assertRaisesRegex(lp.PrepError,"BLOCKED_CREDENTIAL_REF"):
            self.path.prepare(req(self.mod),auth(credential_ref="sk-real-looking-value"))

    def test_duplicate_use_once_blocks(self):
        p=self.path.prepare(req(self.mod),auth())
        self.path.invoke_sentinel(p,ledger_path=self.ledger,resolver=ResolverOK(self.path.worker),client=Client(),now_tick=1)
        with self.assertRaisesRegex(lp.PrepError,"BLOCKED_DUPLICATE_CALL"):
            self.path.invoke_sentinel(p,ledger_path=self.ledger,resolver=ResolverOK(self.path.worker),client=Client(),now_tick=1)

    def test_resolver_failure_no_transport(self):
        p=self.path.prepare(req(self.mod),auth()); resolver=ResolverFail(); client=Client()
        with self.assertRaisesRegex(lp.PrepError,"BLOCKED_CREDENTIAL_RESOLUTION"):
            self.path.invoke_sentinel(p,ledger_path=self.ledger,resolver=resolver,client=client,now_tick=1)
        self.assertEqual((resolver.calls,client.calls),(1,0))

    def test_redirect_malformed_oversized_model_mismatch_fail_closed(self):
        cases=[
          (Client(status=302,body=b"{}"),"BLOCKED_REDIRECT"),
          (Client(status=200,body=b"not-json"),"BLOCKED_PROVIDER_RESPONSE"),
          (Client(status=200,body=b"x"*20000),"BLOCKED_RESPONSE_TOO_LARGE"),
          (Client(status=200,body=json.dumps({"model":"gpt-5.6-sol"}).encode()),"BLOCKED_MODEL_MISMATCH")]
        for i,(client,code) in enumerate(cases):
            with self.subTest(code=code):
                p=self.path.prepare(req(self.mod,request_id=f"r-{i}"),auth(authority_id=f"a-{i}"))
                ledger=self.ledger.parent/f"l{i}.sqlite"
                with self.assertRaisesRegex(lp.PrepError,code):
                    self.path.invoke_sentinel(p,ledger_path=ledger,resolver=ResolverOK(self.path.worker),client=client,now_tick=1)

    def test_endpoint_and_native_plan_exact(self):
        p=self.path.prepare(req(self.mod),auth()); obj=json.loads(p.native_plan_json)
        self.assertEqual((obj["method"],obj["url"]),("POST","https://api.openai.com/v1/responses"))
        self.assertEqual(obj["headers"],{"content-type":"application/json"})
        self.assertEqual(obj["body"]["model"],"gpt-5.6-luna")
        self.assertEqual(obj["body"]["tools"],[])
        self.assertFalse(obj["body"]["store"])

    def test_result_has_no_writer_or_project_authority(self):
        p=self.path.prepare(req(self.mod),auth())
        out=self.path.invoke_sentinel(p,ledger_path=self.ledger,resolver=ResolverOK(self.path.worker),client=Client(),now_tick=1)
        self.assertFalse(out["gateway_writer_authority"]); self.assertFalse(out["provider_writer_authority"])
        self.assertFalse(out["project_state_applied"]); self.assertFalse(out["external_dispatch_performed"])

    def test_no_real_credential_or_network_dependency_in_prep(self):
        src=Path(lp.__file__).read_text()
        self.assertNotIn("OPENAI_API_KEY",src)
        self.assertNotIn("os.environ",src)
        self.assertNotIn("urllib.request",src)
        self.assertNotIn("requests.",src)

if __name__=="__main__": unittest.main(verbosity=2)
