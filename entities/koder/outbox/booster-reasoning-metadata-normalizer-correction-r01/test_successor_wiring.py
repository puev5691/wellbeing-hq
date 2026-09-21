import json,os,tempfile,unittest
from pathlib import Path
from types import SimpleNamespace
import shape_diag_successor_runner as runner

MSG={"type":"message","id":"msg_1","status":"completed","role":"assistant",
     "content":[{"type":"output_text","text":"SYNTHETIC_OK","annotations":[]}]}
REASON={"type":"reasoning","id":"rs_1","summary":[],"status":"completed"}

def body(output):
    return json.dumps({"id":"resp_fixture","object":"response","model":"gpt-5.6-luna","status":"completed",
                       "output":output,"usage":{"input_tokens":10,"output_tokens":4,"total_tokens":14}},
                      separators=(",",":")).encode()

class Resolver:
    def __init__(self): self.calls=0
    def resolve(self,ref):
        self.calls+=1
        return SimpleNamespace(provider="openai",value="synthetic-not-real")

class Client:
    def __init__(self,b): self.body=b; self.calls=0
    def request(self,**kw): self.calls+=1; return 200,self.body

class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.worker=Path(os.environ["LIVE_WORKER"])
        cls.diag=Path(os.environ["DIAG_INTEGRATION"])
        cls.ri=Path(os.environ["RESULT_INTEGRATION"])
        cls.rs=Path(os.environ["RESULT_STORE"])
        cls.ss=Path(os.environ["SHAPE_STORE"])
        cls.inv_template=json.loads(Path(os.environ["INVOCATION"]).read_text())

    def setUp(self):
        td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup)
        self.d=Path(td.name)
        self.inv=self.d/"inv.json"; self.inv.write_text(json.dumps(self.inv_template))
        self.ledger=self.d/"ledger.sqlite"; self.shape=self.d/"response-shapes"; self.review=self.d/"review-results"

    def live_invocation(self):
        o=dict(self.inv_template); o["mode"]="LIVE"; o["authority_id"]="synthetic-live"
        self.inv.write_text(json.dumps(o))

    def execute(self,resolver=None,client=None):
        return runner.execute(invocation_path=self.inv,worker_path=self.worker,
            diag_integration_path=self.diag,result_integration_path=self.ri,result_store_path=self.rs,
            shape_store_path=self.ss,ledger_path=self.ledger,shape_dir=self.shape,result_dir=self.review,
            resolver=resolver,client=client,now_tick=1)

    def test_sentinel_zero_provider_zero_credential_value_read(self):
        cred=self.d/"cred"; cred.mkdir(); (cred/runner.OBJECT).write_text("DO_NOT_READ")
        old=os.environ.get("CREDENTIALS_DIRECTORY"); os.environ["CREDENTIALS_DIRECTORY"]=str(cred)
        try: out=self.execute()
        finally:
            if old is None: os.environ.pop("CREDENTIALS_DIRECTORY",None)
            else: os.environ["CREDENTIALS_DIRECTORY"]=old
        self.assertEqual(out["status"],"READY")
        self.assertEqual(out["provider_calls"],0)
        self.assertFalse(out["credential_value_read"])
        self.assertEqual(out["shape_schema"],"wb.openai.booster.response_shape_diag.v2")
        self.assertEqual(out["review_schema"],"wb.openai.booster.review_result.v2")

    def test_plain_message_full_success(self):
        self.live_invocation(); r=Resolver(); c=Client(body([MSG]))
        out=self.execute(r,c)
        self.assertEqual((r.calls,c.calls),(1,1))
        self.assertEqual(out["status"],"PASS_AFTER_SHAPE_AND_REVIEW_PERSISTENCE")
        self.assertTrue(Path(out["shape_path"]).is_file())
        self.assertTrue(Path(out["result_path"]).is_file())
        self.assertEqual(out["provider_calls"],1)
        self.assertEqual((out["retries"],out["fallback"]),(0,"none"))

    def test_reasoning_shape_saved_and_review_created(self):
        self.live_invocation(); r=Resolver(); c=Client(body([REASON,MSG]))
        result=self.execute(r,c)
        self.assertEqual(c.calls,1)
        shapes=list(self.shape.glob("*.shape.json")); self.assertEqual(len(shapes),1)
        rec=json.loads(shapes[0].read_text())
        self.assertEqual([x["type"] for x in rec["output_items"]],["reasoning","message"])
        review=json.loads(Path(result["result_path"]).read_text())
        self.assertEqual(review["review_payload"]["text"],"SYNTHETIC_OK")
        self.assertEqual([x["type"] for x in review["response_evidence"]["output"]],["message"])

    def test_no_secret_material_in_shape_or_review(self):
        self.live_invocation(); self.execute(Resolver(),Client(body([MSG])))
        raw="\n".join(p.read_text() for p in list(self.shape.glob("*"))+list(self.review.glob("*")))
        for forbidden in ("synthetic-not-real","Authorization","OPENAI_API_KEY","secretref:"):
            self.assertNotIn(forbidden,raw)

    def test_scope_is_exact(self):
        self.live_invocation()
        o=runner.read_invocation(self.inv)
        self.assertEqual((o["provider"],o["model"]),("openai","gpt-5.6-luna"))
        self.assertEqual(o["tools"],[])
        self.assertEqual((o["calls"],o["retries"],o["fallback"]),(1,0,"none"))
        self.assertEqual(o["project_acceptance"],"NOT_GRANTED")
        self.assertFalse(o["project_state_mutation"])

if __name__=="__main__": unittest.main(verbosity=2)
