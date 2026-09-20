import json, os, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import review_result_store as store
import reviewable_live_worker as integ

TASK_COMMIT="1"*40
TASK_BLOB="2"*40
WRITER_BLOB="3"*40
REQUEST_SHA="4"*64
PLAN_SHA="5"*64
AUTH_SHA="6"*64
REQUESTER_SHA="7"*64
MODEL="gpt-5.6-luna"
ATTEMPT_EXPECTED=None

def provider_body(text="SYNTHETIC_OK",model=MODEL,extra_output=None):
    output=[{"type":"message","role":"assistant","content":[{"type":"output_text","text":text}]}]
    if extra_output is not None: output.append(extra_output)
    return json.dumps({"id":"resp_fixture","object":"response","model":model,"status":"completed","output":output,
                       "usage":{"input_tokens":10,"output_tokens":4,"total_tokens":14}},
                      separators=(",",":")).encode()

class Resolver:
    def __init__(self,w): self.w=w; self.calls=0
    def resolve(self,ref):
        self.calls+=1
        return self.w.ResolvedSecret("openai","synthetic-not-real")

class Client:
    def __init__(self,body=None,status=200): self.calls=0; self.body=body or provider_body(); self.status=status
    def request(self,**kw): self.calls+=1; return self.status,self.body

class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.worker_path=Path(os.environ["LIVE_WORKER"])
        cls.store_path=Path(os.environ["RESULT_STORE"])
        # instantiate once just to access exact pinned worker module
        td=tempfile.TemporaryDirectory(); cls._td=td
        x=integ.ReviewableLiveWorker(worker_path=cls.worker_path,store_path=cls.store_path,
            ledger_path=Path(td.name)/"x.sqlite",result_dir=Path(td.name)/"results",resolver=None,client=None)
        cls.w=x.worker

    @classmethod
    def tearDownClass(cls): cls._td.cleanup()

    def setUp(self):
        td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup)
        self.d=Path(td.name); self.ledger=self.d/"ledger.sqlite"; self.results=self.d/"results"

    def plan(self):
        native={"method":"POST","url":"https://api.openai.com/v1/responses",
                "headers":{"content-type":"application/json"},
                "body":{"model":MODEL,"input":"Synthetic bounded request.","max_output_tokens":64,
                        "store":False,"tools":[],"tool_choice":"none","parallel_tool_calls":False}}
        return self.w.WorkerPlan(REQUEST_SHA,PLAN_SHA,AUTH_SHA,REQUESTER_SHA,"openai",MODEL,
            self.w.canon(native),self.w.SecretRef("openai","secretref:openai:synthetic-test-only"),
            self.w.WorkerPolicy(30.0,16384,1,0),100)

    def runner(self,client=None):
        resolver=Resolver(self.w); client=client or Client()
        x=integ.ReviewableLiveWorker(worker_path=self.worker_path,store_path=self.store_path,
            ledger_path=self.ledger,result_dir=self.results,resolver=resolver,client=client)
        return x,resolver,client

    def ident(self): return integ.ResultIdentity(TASK_COMMIT,TASK_BLOB,WRITER_BLOB)

    def test_synthetic_result_persists_reviewable_payload(self):
        x,r,c=self.runner(); out=x.invoke_once_and_persist(self.plan(),self.ident(),now_tick=1)
        self.assertEqual((r.calls,c.calls),(1,1))
        self.assertEqual(out["technical_status"],"PASS_PERSISTED_REVIEWABLE_RESULT")
        rec=json.loads(Path(out["result_path"]).read_text())
        self.assertEqual(rec["review_payload"]["text"],"SYNTHETIC_OK")
        self.assertEqual(rec["parser_status"],"NORMALIZED_ASSISTANT_TEXT_EXACT_FROM_OUTPUT_MESSAGES")

    def test_exact_identity_correlation(self):
        x,_,_=self.runner(); out=x.invoke_once_and_persist(self.plan(),self.ident(),now_tick=1)
        rec=json.loads(Path(out["result_path"]).read_text())
        expected=self.w.sha({"authority":AUTH_SHA,"request":REQUEST_SHA,"plan":PLAN_SHA})
        self.assertEqual(rec["attempt_key"],expected)
        self.assertEqual((rec["request_sha256"],rec["task_commit"],rec["task_blob"],rec["writer_blob"]),
                         (REQUEST_SHA,TASK_COMMIT,TASK_BLOB,WRITER_BLOB))
        self.assertEqual((rec["provider"],rec["model"]),("openai",MODEL))
        self.assertEqual((rec["plan_sha256"],rec["authority_sha256"]),(PLAN_SHA,AUTH_SHA))

    def test_later_review_requires_zero_provider_calls(self):
        x,_,c=self.runner(); out=x.invoke_once_and_persist(self.plan(),self.ident(),now_tick=1)
        before=c.calls
        rec=store.read_and_validate(Path(out["result_path"]),attempt_key=json.loads(Path(out["result_path"]).read_text())["attempt_key"],
            request_sha256=REQUEST_SHA,task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,
            provider="openai",model=MODEL)
        self.assertEqual(c.calls,before)
        self.assertEqual(rec["review_payload"]["text"],"SYNTHETIC_OK")

    def test_no_credential_like_material_persisted(self):
        x,_,_=self.runner(); out=x.invoke_once_and_persist(self.plan(),self.ident(),now_tick=1)
        raw=Path(out["result_path"]).read_text()
        for forbidden in ("synthetic-not-real","Authorization","OPENAI_API_KEY","secretref:","CREDENTIALS_DIRECTORY"):
            self.assertNotIn(forbidden,raw)

    def test_persistence_failure_no_false_pass(self):
        x,_,c=self.runner()
        with patch.object(store.os,"replace",side_effect=OSError("fail")):
            with self.assertRaisesRegex(integ.IntegrationError,"BLOCKED_REVIEW_RESULT_PERSISTENCE"):
                x.invoke_once_and_persist(self.plan(),self.ident(),now_tick=1)
        self.assertEqual(c.calls,1)
        self.assertEqual(self.w.DurableOneShotLedger(self.ledger).count(),1)

    def test_write_failure_no_false_pass(self):
        rec=store.normalize_openai_result(body=provider_body(),attempt_key="a"*64,request_sha256=REQUEST_SHA,
            task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,provider="openai",model=MODEL,
            http_status=200,provider_calls=1,retries=0,fallback="none")
        with patch.object(store.os,"write",return_value=0):
            with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_PERSIST_WRITE"):
                store.persist_atomic(self.d/"r.json",rec)

    def test_oversized_result_fail_closed(self):
        with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_RESPONSE_TOO_LARGE"):
            store.normalize_openai_result(body=b"x"*(store.MAX_PROVIDER_BODY_BYTES+1),attempt_key="a"*64,
                request_sha256=REQUEST_SHA,task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,
                provider="openai",model=MODEL,http_status=200,provider_calls=1,retries=0,fallback="none")

    def test_malformed_response_fail_closed(self):
        with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_MALFORMED_PROVIDER_RESPONSE"):
            store.normalize_openai_result(body=b"{",attempt_key="a"*64,request_sha256=REQUEST_SHA,
                task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,provider="openai",model=MODEL,
                http_status=200,provider_calls=1,retries=0,fallback="none")

    def test_model_mismatch_fail_closed(self):
        with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_MODEL_MISMATCH"):
            store.normalize_openai_result(body=provider_body(model="gpt-5.6-sol"),attempt_key="a"*64,
                request_sha256=REQUEST_SHA,task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,
                provider="openai",model=MODEL,http_status=200,provider_calls=1,retries=0,fallback="none")

    def test_unexpected_tool_action_fail_closed(self):
        tool={"type":"function_call","name":"x","arguments":"{}"}
        with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_UNEXPECTED_PROVIDER_ACTION"):
            store.normalize_openai_result(body=provider_body(extra_output=tool),attempt_key="a"*64,
                request_sha256=REQUEST_SHA,task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,
                provider="openai",model=MODEL,http_status=200,provider_calls=1,retries=0,fallback="none")

    def test_retry_fallback_authority_boundaries(self):
        rec=store.normalize_openai_result(body=provider_body(),attempt_key="a"*64,request_sha256=REQUEST_SHA,
            task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,provider="openai",model=MODEL,
            http_status=200,provider_calls=1,retries=0,fallback="none")
        self.assertEqual((rec["provider_calls"],rec["retries"],rec["fallback"]),(1,0,"none"))
        self.assertEqual(rec["project_acceptance"],"NOT_GRANTED")
        self.assertFalse(rec["project_state_mutation"]); self.assertFalse(rec["provider_writer_authority"])
        self.assertFalse(rec["gateway_writer_authority"])

    def test_consumed_one_shot_cannot_replay_to_recover_content(self):
        x,_,_=self.runner(); x.invoke_once_and_persist(self.plan(),self.ident(),now_tick=1)
        # deleting review content cannot authorize transport replay; ledger still blocks.
        for p in self.results.glob("*.review.json"): p.unlink()
        x2,_,c2=self.runner()
        with self.assertRaisesRegex(integ.IntegrationError,"BLOCKED_DUPLICATE_CALL"):
            x2.invoke_once_and_persist(self.plan(),self.ident(),now_tick=1)
        self.assertEqual(c2.calls,0)

if __name__=="__main__": unittest.main(verbosity=2)
