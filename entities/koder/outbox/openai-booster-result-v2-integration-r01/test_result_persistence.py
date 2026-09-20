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

def provider_body(text="SYNTHETIC_OK",model=MODEL,extra_output=None):
    output=[{"type":"message","role":"assistant","content":[{"type":"output_text","text":text}]}]
    if extra_output is not None: output.append(extra_output)
    return json.dumps({"id":"resp_fixture","object":"response","model":model,"status":"completed",
                       "output":output,"usage":{"input_tokens":10,"output_tokens":4,"total_tokens":14}},
                      separators=(",",":")).encode()

def make_record(**kw):
    args=dict(body=provider_body(),attempt_key="a"*64,request_sha256=REQUEST_SHA,
              task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,
              plan_sha256=PLAN_SHA,authority_sha256=AUTH_SHA,provider="openai",model=MODEL,
              http_status=200,provider_calls=1,retries=0,fallback="none")
    args.update(kw)
    return store.normalize_openai_result(**args)

IDENTITY=dict(attempt_key="a"*64,request_sha256=REQUEST_SHA,task_commit=TASK_COMMIT,
              task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,plan_sha256=PLAN_SHA,
              authority_sha256=AUTH_SHA,provider="openai",model=MODEL)

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

    def persist_tamper(self,mutate):
        p=self.d/"tamper.json"; rec=make_record(); store.persist_atomic(p,rec)
        obj=json.loads(p.read_text()); mutate(obj); p.write_text(json.dumps(obj),encoding="utf-8")
        return p

    def assert_tamper_blocked(self,mutate,pattern="BLOCKED_"):
        p=self.persist_tamper(mutate)
        with self.assertRaisesRegex(store.PersistenceError,pattern):
            store.read_and_validate(p,**IDENTITY)

    def test_valid_readback_and_cross_field_evidence(self):
        p=self.d/"valid.json"; rec=make_record(); store.persist_atomic(p,rec)
        got=store.read_and_validate(p,**IDENTITY)
        eb=store.canonical(got["response_evidence"])
        self.assertEqual(got["response_bytes"],len(eb))
        self.assertEqual(got["response_sha256"],store.sha256_bytes(eb))
        self.assertEqual(got["review_payload"]["text"],"SYNTHETIC_OK")

    def test_integration_persists_reviewable_payload_and_zero_review_calls(self):
        x,r,c=self.runner(); out=x.invoke_once_and_persist(self.plan(),self.ident(),now_tick=1)
        self.assertEqual((r.calls,c.calls),(1,1))
        before=c.calls
        rec=json.loads(Path(out["result_path"]).read_text())
        store.read_and_validate(Path(out["result_path"]),attempt_key=rec["attempt_key"],
            request_sha256=REQUEST_SHA,task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,
            plan_sha256=PLAN_SHA,authority_sha256=AUTH_SHA,provider="openai",model=MODEL)
        self.assertEqual(c.calls,before)
        self.assertEqual(rec["review_payload"]["text"],"SYNTHETIC_OK")

    def test_response_bytes_tamper(self):
        self.assert_tamper_blocked(lambda o:o.__setitem__("response_bytes",o["response_bytes"]+1),"BLOCKED_RESPONSE_BYTES_MISMATCH")
    def test_response_sha256_tamper(self):
        self.assert_tamper_blocked(lambda o:o.__setitem__("response_sha256","0"*64),"BLOCKED_RESPONSE_SHA256_MISMATCH")
    def test_http_status_tamper(self):
        self.assert_tamper_blocked(lambda o:o.__setitem__("http_status",201),"BLOCKED_HTTP_STATUS")
    def test_parser_status_tamper(self):
        self.assert_tamper_blocked(lambda o:o.__setitem__("parser_status","OTHER"),"BLOCKED_PARSER_STATUS")
    def test_plan_sha256_tamper(self):
        self.assert_tamper_blocked(lambda o:o.__setitem__("plan_sha256","8"*64),"BLOCKED_RESULT_IDENTITY_MISMATCH")
    def test_authority_sha256_tamper(self):
        self.assert_tamper_blocked(lambda o:o.__setitem__("authority_sha256","9"*64),"BLOCKED_RESULT_IDENTITY_MISMATCH")

    def test_missing_required_key(self):
        self.assert_tamper_blocked(lambda o:o.pop("response_sha256"),"BLOCKED_RESULT_KEY_SET")
    def test_unexpected_extra_key(self):
        self.assert_tamper_blocked(lambda o:o.__setitem__("mystery","x"),"BLOCKED_RESULT_KEY_SET")
    def test_wrong_type(self):
        self.assert_tamper_blocked(lambda o:o.__setitem__("response_bytes","123"),"BLOCKED_RESPONSE_BYTES_MISMATCH")
    def test_schema_version_mismatch(self):
        self.assert_tamper_blocked(lambda o:o.__setitem__("schema","wb.openai.booster.review_result.v1"),"BLOCKED_RESULT_SCHEMA")

    def test_review_payload_text_tamper(self):
        self.assert_tamper_blocked(lambda o:o["review_payload"].__setitem__("text","CHANGED"),"BLOCKED_REVIEW_PAYLOAD")
    def test_review_payload_bytes_tamper(self):
        self.assert_tamper_blocked(lambda o:o["review_payload"].__setitem__("bytes",999),"BLOCKED_REVIEW_PAYLOAD_IDENTITY")
    def test_review_payload_sha_tamper(self):
        self.assert_tamper_blocked(lambda o:o["review_payload"].__setitem__("sha256","f"*64),"BLOCKED_REVIEW_PAYLOAD_IDENTITY")

    def test_response_evidence_tamper_without_hash_update(self):
        self.assert_tamper_blocked(lambda o:o["response_evidence"]["output"][0]["content"][0].__setitem__("text","CHANGED"),
                                   "BLOCKED_")
    def test_response_evidence_tamper_with_hash_update_still_hits_review_payload(self):
        def mutate(o):
            o["response_evidence"]["output"][0]["content"][0]["text"]="CHANGED"
            eb=store.canonical(o["response_evidence"])
            o["response_bytes"]=len(eb); o["response_sha256"]=store.sha256_bytes(eb)
        self.assert_tamper_blocked(mutate,"BLOCKED_REVIEW_PAYLOAD")

    def test_task_writer_provider_model_correlation_tampers(self):
        cases=[
          ("task_commit","a"*40),("task_blob","b"*40),("writer_blob","c"*40),
          ("provider","anthropic"),("model","gpt-5.6-sol"),("request_sha256","d"*64),("attempt_key","e"*64)
        ]
        for key,value in cases:
            with self.subTest(key=key):
                self.assert_tamper_blocked(lambda o,k=key,v=value:o.__setitem__(k,v),"BLOCKED_RESULT_IDENTITY_MISMATCH")

    def test_authority_flags_tamper(self):
        for key,value in [("requester_review_required",False),("project_acceptance","GRANTED"),
                          ("project_state_mutation",True),("provider_writer_authority",True),
                          ("gateway_writer_authority",True)]:
            with self.subTest(key=key):
                self.assert_tamper_blocked(lambda o,k=key,v=value:o.__setitem__(k,v),"FAIL_RESULT_AUTHORITY")

    def test_retry_fallback_calls_tamper(self):
        for key,value in [("provider_calls",2),("retries",1),("fallback","other")]:
            with self.subTest(key=key):
                self.assert_tamper_blocked(lambda o,k=key,v=value:o.__setitem__(k,v),"BLOCKED_RETRY_FALLBACK_POLICY")

    def test_persistence_write_fsync_rename_fail_closed(self):
        rec=make_record()
        with patch.object(store.os,"write",return_value=0):
            with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_PERSIST_WRITE"):
                store.persist_atomic(self.d/"write.json",rec)
        with patch.object(store.os,"fsync",side_effect=OSError("fail")):
            with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_RESULT_PERSISTENCE"):
                store.persist_atomic(self.d/"fsync.json",rec)
        with patch.object(store.os,"replace",side_effect=OSError("fail")):
            with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_RESULT_PERSISTENCE"):
                store.persist_atomic(self.d/"rename.json",rec)

    def test_malformed_oversized_model_action_fail_closed(self):
        with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_MALFORMED_PROVIDER_RESPONSE"):
            make_record(body=b"{")
        with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_RESPONSE_TOO_LARGE"):
            make_record(body=b"x"*(store.MAX_PROVIDER_BODY_BYTES+1))
        with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_MODEL_MISMATCH"):
            make_record(body=provider_body(model="gpt-5.6-sol"))
        tool={"type":"function_call","name":"x","arguments":"{}"}
        with self.assertRaisesRegex(store.PersistenceError,"BLOCKED_UNEXPECTED_PROVIDER_ACTION"):
            make_record(body=provider_body(extra_output=tool))

    def test_secret_like_material_absent(self):
        x,_,_=self.runner(); out=x.invoke_once_and_persist(self.plan(),self.ident(),now_tick=1)
        raw=Path(out["result_path"]).read_text()
        for forbidden in ("synthetic-not-real","Authorization","OPENAI_API_KEY","secretref:","CREDENTIALS_DIRECTORY"):
            self.assertNotIn(forbidden,raw)

    def test_persistence_failure_after_transport_no_false_pass_and_ledger_consumed(self):
        x,_,c=self.runner()
        with patch.object(store.os,"replace",side_effect=OSError("fail")):
            with self.assertRaisesRegex(integ.IntegrationError,"BLOCKED_REVIEW_RESULT_PERSISTENCE"):
                x.invoke_once_and_persist(self.plan(),self.ident(),now_tick=1)
        self.assertEqual(c.calls,1)
        self.assertEqual(self.w.DurableOneShotLedger(self.ledger).count(),1)
        x2,_,c2=self.runner()
        with self.assertRaisesRegex(integ.IntegrationError,"BLOCKED_DUPLICATE_CALL"):
            x2.invoke_once_and_persist(self.plan(),self.ident(),now_tick=1)
        self.assertEqual(c2.calls,0)

if __name__=="__main__": unittest.main(verbosity=2)
