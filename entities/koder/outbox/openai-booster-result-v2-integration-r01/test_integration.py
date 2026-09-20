import json, os, tempfile, unittest
from pathlib import Path
from types import SimpleNamespace
import integrated_live_child_runner as runner

class Resolver:
    def __init__(self): self.calls=0
    def resolve(self,ref):
        self.calls+=1
        return SimpleNamespace(provider="openai",value="synthetic-not-real")

class Client:
    def __init__(self): self.calls=0
    def request(self,**kw):
        self.calls+=1
        body={"id":"resp_fixture","object":"response","model":"gpt-5.6-luna","status":"completed",
              "output":[{"type":"message","role":"assistant","content":[{"type":"output_text","text":"SYNTHETIC_OK"}]}],
              "usage":{"input_tokens":10,"output_tokens":4,"total_tokens":14}}
        return 200,json.dumps(body,separators=(",",":")).encode()

class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.worker=Path(os.environ["LIVE_WORKER"])
        cls.integration=Path(os.environ["INTEGRATION"])
        cls.store=Path(os.environ["RESULT_STORE"])
        cls.invocation_template=json.loads(Path(os.environ["INVOCATION"]).read_text())

    def setUp(self):
        td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup)
        self.d=Path(td.name)
        self.inv=self.d/"invocation.json"
        self.inv.write_text(json.dumps(self.invocation_template),encoding="utf-8")
        self.ledger=self.d/"ledger.sqlite"
        self.results=self.d/"review-results"

    def execute(self,resolver=None,client=None,result_dir=None):
        return runner.execute(invocation_path=self.inv,worker_path=self.worker,
            integration_path=self.integration,store_path=self.store,ledger_path=self.ledger,
            result_dir=result_dir or self.results,resolver=resolver or Resolver(),
            client=client or Client(),now_tick=1)

    def test_success_terminal_only_after_v2_artifact(self):
        r=Resolver(); c=Client()
        out=self.execute(r,c)
        self.assertEqual(out["status"],"PASS_TECHNICAL_RESULT_AFTER_DURABLE_V2_READBACK")
        self.assertEqual((r.calls,c.calls),(1,1))
        p=Path(out["result_path"]); self.assertTrue(p.is_file())
        rec=json.loads(p.read_text())
        self.assertEqual(rec["schema"],"wb.openai.booster.review_result.v2")
        self.assertEqual(rec["review_payload"]["text"],"SYNTHETIC_OK")

    def test_later_requester_review_provider_delta_zero(self):
        c=Client(); out=self.execute(client=c); before=c.calls
        store=runner.load_pinned(self.store,runner.STORE_SHA256,"_test_store_later")
        worker=runner.load_pinned(self.worker,runner.WORKER_SHA256,"_test_worker_later")
        o=runner.read_invocation(self.inv); plan=runner.make_plan(worker,o)
        rec=store.read_and_validate(Path(out["result_path"]),attempt_key=out["attempt_key"],
            request_sha256=plan.request_sha256,task_commit=runner.TASK_COMMIT,task_blob=runner.TASK_BLOB,
            writer_blob=runner.WRITER_BLOB,plan_sha256=plan.plan_sha256,authority_sha256=plan.authority_sha256,
            provider="openai",model=runner.MODEL)
        self.assertEqual(c.calls,before)
        self.assertEqual(rec["review_payload"]["text"],"SYNTHETIC_OK")

    def test_exact_attempt_request_plan_authority_correlation(self):
        out=self.execute()
        store=runner.load_pinned(self.store,runner.STORE_SHA256,"_test_store_corr")
        worker=runner.load_pinned(self.worker,runner.WORKER_SHA256,"_test_worker_corr")
        plan=runner.make_plan(worker,runner.read_invocation(self.inv))
        rec=json.loads(Path(out["result_path"]).read_text())
        expected=worker.sha({"authority":plan.authority_sha256,"request":plan.request_sha256,"plan":plan.plan_sha256})
        self.assertEqual(rec["attempt_key"],expected)
        self.assertEqual(rec["request_sha256"],plan.request_sha256)
        self.assertEqual(rec["plan_sha256"],plan.plan_sha256)
        self.assertEqual(rec["authority_sha256"],plan.authority_sha256)
        store.read_and_validate(Path(out["result_path"]),attempt_key=expected,request_sha256=plan.request_sha256,
            task_commit=runner.TASK_COMMIT,task_blob=runner.TASK_BLOB,writer_blob=runner.WRITER_BLOB,
            plan_sha256=plan.plan_sha256,authority_sha256=plan.authority_sha256,provider="openai",model=runner.MODEL)

    def test_secret_privacy_exclusions_preserved(self):
        out=self.execute()
        raw=Path(out["result_path"]).read_text()
        for x in ("synthetic-not-real","Authorization","OPENAI_API_KEY","secretref:","CREDENTIALS_DIRECTORY"):
            self.assertNotIn(x,raw)

    def test_persistence_failure_after_transport_consumes_one_shot(self):
        worker=runner.load_pinned(self.worker,runner.WORKER_SHA256,"_test_worker_fail")
        plan=runner.make_plan(worker,runner.read_invocation(self.inv))
        attempt=worker.sha({"authority":plan.authority_sha256,"request":plan.request_sha256,"plan":plan.plan_sha256})
        self.results.mkdir()
        (self.results/(attempt+".review.json")).mkdir()
        c=Client()
        with self.assertRaises(Exception):
            self.execute(client=c)
        self.assertEqual(c.calls,1)
        ledger=worker.DurableOneShotLedger(self.ledger)
        self.assertEqual(ledger.count(),1)
        c2=Client()
        with self.assertRaisesRegex(Exception,"BLOCKED_DUPLICATE_CALL"):
            self.execute(client=c2)
        self.assertEqual(c2.calls,0)

    def test_scope_retry_fallback_acceptance_preserved(self):
        out=self.execute()
        self.assertEqual((out["provider"],out["model"]),("openai","gpt-5.6-luna"))
        self.assertEqual((out["provider_calls"],out["retries"],out["fallback"]),(1,0,"none"))
        self.assertTrue(out["requester_review_required"])
        self.assertEqual(out["project_acceptance"],"NOT_GRANTED")
        self.assertFalse(out["project_state_mutation"])
        self.assertFalse(out["provider_writer_authority"])
        self.assertFalse(out["gateway_writer_authority"])

    def test_tamper_protection_remains_active_at_integrated_artifact(self):
        out=self.execute()
        p=Path(out["result_path"])
        obj=json.loads(p.read_text()); obj["response_sha256"]="0"*64; p.write_text(json.dumps(obj))
        store=runner.load_pinned(self.store,runner.STORE_SHA256,"_test_store_tamper")
        worker=runner.load_pinned(self.worker,runner.WORKER_SHA256,"_test_worker_tamper")
        plan=runner.make_plan(worker,runner.read_invocation(self.inv))
        with self.assertRaisesRegex(Exception,"BLOCKED_RESPONSE_SHA256_MISMATCH"):
            store.read_and_validate(p,attempt_key=out["attempt_key"],request_sha256=plan.request_sha256,
                task_commit=runner.TASK_COMMIT,task_blob=runner.TASK_BLOB,writer_blob=runner.WRITER_BLOB,
                plan_sha256=plan.plan_sha256,authority_sha256=plan.authority_sha256,
                provider="openai",model=runner.MODEL)

if __name__=="__main__": unittest.main(verbosity=2)
