import copy,json,os,tempfile,unittest
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

IDENTITY=dict(attempt_key="a"*64,request_sha256=REQUEST_SHA,task_commit=TASK_COMMIT,
              task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,plan_sha256=PLAN_SHA,
              authority_sha256=AUTH_SHA,provider="openai",model=MODEL)

def make_snapshot(body=None):
    return shape.structural_snapshot(body=body or response([MSG]),attempt_key="a"*64,
        request_sha256=REQUEST_SHA,task_commit=TASK_COMMIT,task_blob=TASK_BLOB,
        writer_blob=WRITER_BLOB,plan_sha256=PLAN_SHA,authority_sha256=AUTH_SHA,
        provider="openai",model=MODEL,http_status=200)

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

    # predecessor positive/failure-ordering suite
    def test_positive_plain_message(self):
        x,r,c=self.runner(response([MSG]))
        out=x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        self.assertEqual((r.calls,c.calls),(1,1))
        p=Path(out["shape_path"]); rec=json.loads(p.read_text())
        self.assertEqual(out["shape_snapshot_sha256"],rec["snapshot_sha256"])
        shape.read_and_validate(p,expected_snapshot_sha256=out["shape_snapshot_sha256"],
            attempt_key=rec["attempt_key"],request_sha256=REQUEST_SHA,task_commit=TASK_COMMIT,
            task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,plan_sha256=PLAN_SHA,
            authority_sha256=AUTH_SHA,provider="openai",model=MODEL)
        self.assertNotIn("SYNTHETIC_OK",p.read_text())

    def test_positive_reasoning_shape_saved_normalizer_blocks(self):
        x,_,c=self.runner(response([REASON,MSG]))
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"snapshot_sha256="):
            x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        self.assertEqual(c.calls,1)
        rec=json.loads(self.shape_file().read_text())
        self.assertEqual([i["type"] for i in rec["output_items"]],["reasoning","message"])
        self.assertEqual(rec["output_items"][0]["classification"],"benign_metadata_or_reasoning_container")
        self.assertEqual(list(self.result_dir.glob("*.review.json")),[])

    def test_positive_tool_shape_saved_normalizer_blocks(self):
        x,_,_=self.runner(response([TOOL,MSG]))
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"BLOCKED_UNEXPECTED_PROVIDER_ACTION"):
            x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        rec=json.loads(self.shape_file().read_text())
        self.assertEqual(rec["output_items"][0]["classification"],"tool_action_request")
        self.assertNotIn("{}",self.shape_file().read_text())

    def test_positive_unknown_shape_saved_normalizer_blocks(self):
        x,_,_=self.runner(response([UNKNOWN,MSG]))
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"BLOCKED_UNEXPECTED_PROVIDER_ACTION"):
            x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        self.assertEqual(json.loads(self.shape_file().read_text())["output_items"][0]["classification"],"unknown")

    def test_positive_malformed_json_consumed_no_shape(self):
        x,_,c=self.runner(b"{")
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"BLOCKED_PROVIDER_RESPONSE"):
            x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        self.assertEqual(c.calls,1); self.assertEqual(list(self.shape_dir.glob("*")),[])
        self.assertEqual(self.w.DurableOneShotLedger(self.ledger).count(),1)

    def test_positive_post_transport_diag_persist_failure_consumed_no_retry(self):
        plan=self.plan()
        attempt=self.w.sha({"authority":plan.authority_sha256,"request":plan.request_sha256,"plan":plan.plan_sha256})
        self.shape_dir.mkdir(); (self.shape_dir/(attempt+".shape.json")).mkdir()
        x,_,c=self.runner(response([MSG]))
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"BLOCKED_SHAPE_DIAGNOSTIC_PERSISTENCE"):
            x.invoke_once_persist_shape_then_normalize(plan,self.ident(),now_tick=1)
        self.assertEqual(c.calls,1); self.assertEqual(self.w.DurableOneShotLedger(self.ledger).count(),1)
        x2,_,c2=self.runner(response([MSG]))
        with self.assertRaisesRegex(integ.ShapeIntegrationError,"BLOCKED_DUPLICATE_CALL"):
            x2.invoke_once_persist_shape_then_normalize(plan,self.ident(),now_tick=1)
        self.assertEqual(c2.calls,0)

    def test_positive_write_fsync_rename_fail_closed(self):
        snap=make_snapshot()
        with patch.object(shape.os,"write",return_value=0):
            with self.assertRaisesRegex(shape.DiagnosticError,"BLOCKED_DIAG_WRITE"): shape.persist_atomic(self.d/"w",snap)
        with patch.object(shape.os,"fsync",side_effect=OSError("x")):
            with self.assertRaisesRegex(shape.DiagnosticError,"BLOCKED_DIAG_PERSISTENCE"): shape.persist_atomic(self.d/"f",snap)
        with patch.object(shape.os,"replace",side_effect=OSError("x")):
            with self.assertRaisesRegex(shape.DiagnosticError,"BLOCKED_DIAG_PERSISTENCE"): shape.persist_atomic(self.d/"r",snap)

    def test_positive_privacy_exclusion(self):
        x,_,_=self.runner(response([MSG])); x.invoke_once_persist_shape_then_normalize(self.plan(),self.ident(),now_tick=1)
        raw=self.shape_file().read_text()
        for forbidden in ("synthetic-not-real","Authorization","OPENAI_API_KEY","secretref:","SYNTHETIC_OK"):
            self.assertNotIn(forbidden,raw)

    def test_positive_authority_boundaries(self):
        snap=make_snapshot()
        self.assertTrue(snap["requester_review_required"])
        self.assertEqual(snap["project_acceptance"],"NOT_GRANTED")
        self.assertFalse(snap["project_state_mutation"])
        self.assertFalse(snap["provider_writer_authority"])
        self.assertFalse(snap["gateway_writer_authority"])

    # strict tamper harness
    def assert_tamper(self,mutator,recompute_internal=False):
        p=self.d/"tamper.json"; snap=make_snapshot(body=response([REASON,MSG]))
        expected=snap["snapshot_sha256"]; shape.persist_atomic(p,snap)
        obj=json.loads(p.read_text()); mutator(obj)
        if recompute_internal:
            obj["snapshot_sha256"]=shape.snapshot_identity(obj)
        p.write_text(json.dumps(obj),encoding="utf-8")
        with self.assertRaises(shape.DiagnosticError):
            shape.read_and_validate(p,expected_snapshot_sha256=expected,
                attempt_key="a"*64,request_sha256=REQUEST_SHA,task_commit=TASK_COMMIT,
                task_blob=TASK_BLOB,writer_blob=WRITER_BLOB,plan_sha256=PLAN_SHA,
                authority_sha256=AUTH_SHA,provider="openai",model=MODEL)

    def test_tamper_response_bytes(self): self.assert_tamper(lambda o:o.__setitem__("response_bytes",o["response_bytes"]+1))
    def test_tamper_response_sha256(self): self.assert_tamper(lambda o:o.__setitem__("response_sha256","0"*64))
    def test_tamper_http_status(self): self.assert_tamper(lambda o:o.__setitem__("http_status",201))
    def test_tamper_top_level_keys(self): self.assert_tamper(lambda o:o["top_level_keys"].append("x"))
    def test_tamper_output_count(self): self.assert_tamper(lambda o:o.__setitem__("output_count",99))
    def test_tamper_output_item_type(self): self.assert_tamper(lambda o:o["output_items"][0].__setitem__("type","metadata"))
    def test_tamper_output_item_keys(self): self.assert_tamper(lambda o:o["output_items"][0]["keys"].append("x"))
    def test_tamper_output_item_classification(self): self.assert_tamper(lambda o:o["output_items"][0].__setitem__("classification","unknown"))
    def test_tamper_output_item_role(self): self.assert_tamper(lambda o:o["output_items"][1].__setitem__("role","user"))
    def test_tamper_output_item_content_count(self): self.assert_tamper(lambda o:o["output_items"][1].__setitem__("content_count",2))
    def test_tamper_content_item_type(self): self.assert_tamper(lambda o:o["output_items"][1]["content_items"][0].__setitem__("type","metadata"))
    def test_tamper_content_item_keys(self): self.assert_tamper(lambda o:o["output_items"][1]["content_items"][0]["keys"].append("x"))
    def test_tamper_content_item_classification(self): self.assert_tamper(lambda o:o["output_items"][1]["content_items"][0].__setitem__("classification","unknown"))
    def test_tamper_requester_review_required(self): self.assert_tamper(lambda o:o.__setitem__("requester_review_required",False))
    def test_tamper_project_acceptance(self): self.assert_tamper(lambda o:o.__setitem__("project_acceptance","GRANTED"))
    def test_tamper_project_state_mutation(self): self.assert_tamper(lambda o:o.__setitem__("project_state_mutation",True))
    def test_tamper_provider_writer_authority(self): self.assert_tamper(lambda o:o.__setitem__("provider_writer_authority",True))
    def test_tamper_gateway_writer_authority(self): self.assert_tamper(lambda o:o.__setitem__("gateway_writer_authority",True))
    def test_tamper_attempt_key(self): self.assert_tamper(lambda o:o.__setitem__("attempt_key","b"*64))
    def test_tamper_request_sha256(self): self.assert_tamper(lambda o:o.__setitem__("request_sha256","c"*64))
    def test_tamper_task_commit(self): self.assert_tamper(lambda o:o.__setitem__("task_commit","d"*40))
    def test_tamper_task_blob(self): self.assert_tamper(lambda o:o.__setitem__("task_blob","e"*40))
    def test_tamper_writer_blob(self): self.assert_tamper(lambda o:o.__setitem__("writer_blob","f"*40))
    def test_tamper_plan_sha256(self): self.assert_tamper(lambda o:o.__setitem__("plan_sha256","1"*64))
    def test_tamper_authority_sha256(self): self.assert_tamper(lambda o:o.__setitem__("authority_sha256","2"*64))
    def test_tamper_provider(self): self.assert_tamper(lambda o:o.__setitem__("provider","anthropic"))
    def test_tamper_model(self): self.assert_tamper(lambda o:o.__setitem__("model","gpt-5.6-sol"))
    def test_tamper_snapshot_sha256(self): self.assert_tamper(lambda o:o.__setitem__("snapshot_sha256","3"*64))

    def test_tamper_nested_self_consistent_output_items_and_count(self):
        def mutate(o):
            o["output_items"]=copy.deepcopy(o["output_items"][1:])
            for i,item in enumerate(o["output_items"]): item["index"]=i
            o["output_count"]=len(o["output_items"])
        self.assert_tamper(mutate,recompute_internal=True)

    def test_tamper_self_consistent_response_fields_and_internal_hash(self):
        def mutate(o):
            o["response_bytes"]+=10
            o["response_sha256"]="4"*64
            o["http_status"]=202
        self.assert_tamper(mutate,recompute_internal=True)

if __name__=="__main__": unittest.main(verbosity=2)
