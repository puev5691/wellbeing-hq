import json, os, tempfile, unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import response_shape_store as shape
import diagnostic_reviewable_live_worker as integ

TASK_COMMIT="1"*40; TASK_BLOB="2"*40; WRITER_BLOB="3"*40
REQUEST_SHA="4"*64; PLAN_SHA="5"*64; AUTH_SHA="6"*64; REQUESTER_SHA="7"*64
MODEL="gpt-5.6-luna"

def response(output):
    return json.dumps({"id":"resp_fixture","object":"response","model":MODEL,"status":"completed",
                       "output":output,"usage":{"input_tokens":10,"output_tokens":4,"total_tokens":14}},
                      separators=(",",":")).encode()

MSG={"type":"message","id":"msg_1","status":"completed","role":"assistant",
     "content":[{"type":"output_text","text":"SYNTHETIC_OK","annotations":[]}]}
REASON={"type":"reasoning","id":"rs_1","summary":[],"status":"completed"}
TOOL={"type":"function_call","id":"fc_1","call_id":"call_1","name":"x","arguments":"{}","status":"completed"}
UNKNOWN={"type":"future_thing","id":"u_1","foo":"bar"}

class Resolver:
    def __init__(self): self.calls=0
    def resolve(self,ref):
        self.calls+=1
        return SimpleNamespace(provider="openai",value="synthetic-not-real")
class Client:
    def __init__(self,body): self.body=body; self.calls=0
    def request(self,**kw): self.calls+=1; return 200,self.body

class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.worker_path=Path(os.environ["LIVE_WORKER"])
        cls.result_integration_path=Path(os.environ["RESULT_INTEGRATION"])
        cls.result_store_path=Path(os.environ["RESULT_STORE"])
        cls.shape_store_path=Path(os.environ["SHAPE_STORE"])
        td=tempfile.TemporaryDirectory(); cls._td=td
        x=integ.DiagnosticReviewableLiveWorker(worker_path=cls.worker_path,
            result_integration_path=cls.result_integration_path,result_store_path=cls.result_store_path,
            shape_store_path=cls.shape_store_path,ledger_path=Path(td.name)/"x.sqlite",
            shape_dir=Path(td.name)/"shape",result_dir=Path(td.name)/"review",
            resolver=Resolver(),client=Client(response([MSG])))
        cls.w=x.worker
    @classmethod
    def tearDownClass(cls): cls._td.cleanup()

    def setUp(self):
        td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup)
        self.d=Path(td.name); self.ledger=self.d/"ledger.sqlite"
        self.shape_dir=self.d/"shape"; self.result_dir=self.d/"review"

    def plan(self):
        native={"method":"POST","url":"https://api.openai.com/v1/responses","headers":{"content-type":"application/json"},
                "body":{"model":MODEL,"input":"Synthetic bounded request.","max_output_tokens":64,
                        "store":False,"tools":[],"tool_choice":"none","parallel_tool_calls":False}}
        return self.w.WorkerPlan(REQUEST_SHA,PLAN_SHA,AUTH_SHA,REQUESTER_SHA,"openai",MODEL,
            self.w.canon(native),self.w.SecretRef("openai","secretref:openai:synthetic-test-only"),
            self.w.WorkerPolicy(30.0,16384,1,0),100)

    def runner(self,body):
        r=Resolver(); c=Client(body)
        x=integ.DiagnosticReviewableLiveWorker(worker_path=self.worker_path,
            result_integration_path=self.result_integration_path,result_store_path=self.result_store_path,
            shape_store_path=self.shape_store_path,ledger_path=self.ledger,shape_dir=self.shape_dir,
            result_dir=self.result_dir,resolver=r,client=c)
        return x,r,c

    def ident(self): return integ.Identity(TASK_COMMIT,TASK_BLOB,WRITER_BLOB)

    def shape_file(self):
        xs=list(self.shape_dir.glob("*.shape.json")); self.assertEqual(len(xs),1); return xs[0]

    def test_plain_message_output_text_passes_and_shape_has_no_content(self):
        x,r,c=self.runner(response([MSG]))
        out=x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        self.assertEqual((r.calls,c.calls),(1,1))
        self.assertTrue(Path(out["result_path"]).is_file())
        diag=json.loads(self.shape_file().read_text())
        self.assertEqual(diag["output_count"],1)
        self.assertEqual(diag["output_items"][0]["type"],"message")
        self.assertEqual(diag["output_items"][0]["classification"],"assistant_text")
        self.assertEqual(diag["output_items"][0]["content_items"][0]["type"],"output_text")
        raw=self.shape_file().read_text()
        self.assertNotIn("SYNTHETIC_OK",raw)

    def test_reasoning_plus_message_shape_saved_but_normalizer_still_blocks(self):
        x,_,c=self.runner(response([REASON,MSG]))
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"BLOCKED_REVIEW_RESULT_PERSISTENCE_AFTER_SHAPE_SAVED:BLOCKED_UNEXPECTED_PROVIDER_ACTION"):
            x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        self.assertEqual(c.calls,1)
        diag=json.loads(self.shape_file().read_text())
        self.assertEqual([i["type"] for i in diag["output_items"]],["reasoning","message"])
        self.assertEqual(diag["output_items"][0]["classification"],"benign_metadata_or_reasoning_container")
        self.assertEqual(list(self.result_dir.glob("*.review.json")),[])

    def test_tool_action_shape_saved_and_normalizer_blocks(self):
        x,_,_=self.runner(response([TOOL,MSG]))
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"BLOCKED_UNEXPECTED_PROVIDER_ACTION"):
            x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        diag=json.loads(self.shape_file().read_text())
        self.assertEqual(diag["output_items"][0]["classification"],"tool_action_request")
        self.assertIn("arguments",diag["output_items"][0]["keys"])
        self.assertNotIn("{}",self.shape_file().read_text())

    def test_unknown_shape_saved_and_normalizer_blocks(self):
        x,_,_=self.runner(response([UNKNOWN,MSG]))
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"BLOCKED_UNEXPECTED_PROVIDER_ACTION"):
            x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        diag=json.loads(self.shape_file().read_text())
        self.assertEqual(diag["output_items"][0]["classification"],"unknown")
        self.assertEqual(diag["output_items"][0]["keys"],["foo","id","type"])

    def test_malformed_json_consumes_transport_but_no_shape_fabricated(self):
        x,_,c=self.runner(b"{")
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"BLOCKED_PROVIDER_RESPONSE"):
            x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        self.assertEqual(c.calls,1)
        self.assertEqual(list(self.shape_dir.glob("*")),[])
        self.assertEqual(self.w.DurableOneShotLedger(self.ledger).count(),1)

    def test_post_transport_diagnostic_persistence_failure_consumed_no_retry(self):
        worker=self.w; plan=self.plan()
        attempt=worker.sha({"authority":plan.authority_sha256,"request":plan.request_sha256,"plan":plan.plan_sha256})
        self.shape_dir.mkdir(); (self.shape_dir/(attempt+".shape.json")).mkdir()
        x,_,c=self.runner(response([MSG]))
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"BLOCKED_SHAPE_DIAGNOSTIC_PERSISTENCE"):
            x.invoke_once_persist_shape_then_normalize(plan,self.ident(),now_tick=1)
        self.assertEqual(c.calls,1); self.assertEqual(worker.DurableOneShotLedger(self.ledger).count(),1)
        x2,_,c2=self.runner(response([MSG]))
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"BLOCKED_DUPLICATE_CALL"):
            x2.invoke_once_persist_shape_then_normalize(plan,self.ident(),now_tick=1)
        self.assertEqual(c2.calls,0)

    def test_diagnostic_tamper_identity_blocks(self):
        body=response([MSG])
        snap=shape.structural_snapshot(body=body,attempt_key="a"*64,request_sha256=REQUEST_SHA,
            task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,
            plan_sha256=PLAN_SHA,authority_sha256=AUTH_SHA,provider="openai",model=MODEL,http_status=200)
        p=self.d/"diag.json"; shape.persist_atomic(p,snap)
        obj=json.loads(p.read_text()); obj["plan_sha256"]="9"*64; p.write_text(json.dumps(obj))
        with self.assertRaisesRegex(shape.DiagnosticError,"BLOCKED_DIAG_IDENTITY_MISMATCH"):
            shape.read_and_validate(p,attempt_key="a"*64,request_sha256=REQUEST_SHA,
                task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,
                plan_sha256=PLAN_SHA,authority_sha256=AUTH_SHA,provider="openai",model=MODEL)

    def test_diagnostic_write_fsync_rename_fail_closed(self):
        snap=shape.structural_snapshot(body=response([MSG]),attempt_key="a"*64,request_sha256=REQUEST_SHA,
            task_commit=TASK_COMMIT,task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,
            plan_sha256=PLAN_SHA,authority_sha256=AUTH_SHA,provider="openai",model=MODEL,http_status=200)
        with patch.object(shape.os,"write",return_value=0):
            with self.assertRaisesRegex(shape.DiagnosticError,"BLOCKED_DIAG_WRITE"): shape.persist_atomic(self.d/"w",snap)
        with patch.object(shape.os,"fsync",side_effect=OSError("x")):
            with self.assertRaisesRegex(shape.DiagnosticError,"BLOCKED_DIAG_PERSISTENCE"): shape.persist_atomic(self.d/"f",snap)
        with patch.object(shape.os,"replace",side_effect=OSError("x")):
            with self.assertRaisesRegex(shape.DiagnosticError,"BLOCKED_DIAG_PERSISTENCE"): shape.persist_atomic(self.d/"r",snap)

    def test_credential_like_material_absent(self):
        x,_,_=self.runner(response([MSG])); x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        raw=self.shape_file().read_text()
        for forbidden in ("synthetic-not-real","Authorization","OPENAI_API_KEY","secretref:","SYNTHETIC_OK"):
            self.assertNotIn(forbidden,raw)

if __name__=="__main__": unittest.main(verbosity=2)
