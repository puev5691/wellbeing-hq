import json, os, tempfile, threading, unittest
from pathlib import Path
import booster_runtime as br

D0="Synthetic bounded request."
D0_SHA="334d56225f1336cfe802b41a5cd82b1613252a4b74b35aa37bd3191202bd59f7"
TASK_COMMIT="1"*40; TASK_BLOB="2"*40; WRITER_COMMIT="3"*40; WRITER_BLOB="4"*40

def request(provider="openai",model="gpt-5.6-luna",**changes):
    r={
      "request_id":"boost-001","entity_id":"KOD","role":"koder",
      "task_path":"entities/koordinator/outbox/synthetic-task.md","task_commit":TASK_COMMIT,"task_blob":TASK_BLOB,
      "writer_path":"entities/koder/current/synthetic-writer.md","writer_commit":WRITER_COMMIT,"writer_blob":WRITER_BLOB,
      "purpose":"bounded synthetic booster replay","provider":provider,"model":model,
      "privacy_class":"synthetic_only","tools":[],"payload":D0,
      "source_locator":"fixture://booster-r02","source_sha256":D0_SHA,"max_output_tokens":64}
    r.update(changes); return r

def authority(r,**changes):
    a={"authority_id":"auth-r02","mode":"REPLAY_ONLY","entity_id":r["entity_id"],"task_commit":r["task_commit"],
       "writer_blob":r["writer_blob"],"provider":r["provider"],"model":r["model"],
       "privacy_class":r["privacy_class"],"tools":r["tools"],"live_execution_authorized":False}
    a.update(changes); return a

def openai_fixture(model="gpt-5.6-luna"):
    return {"http_status":200,"body":{"id":"resp_fixture","object":"response","model":model,"status":"completed",
      "output":[{"type":"message","id":"msg_fixture","status":"completed","role":"assistant",
                 "content":[{"type":"output_text","text":"SYNTHETIC_OK","annotations":[]}]}],
      "output_text":"SYNTHETIC_OK","usage":{"input_tokens":11,"output_tokens":4,"total_tokens":15},"tools":[]}}

def anthropic_fixture(model="synthetic-model-for-contract-test"):
    return {"http_status":200,"body":{"id":"msg_fixture","type":"message","role":"assistant","model":model,
      "content":[{"type":"text","text":"Synthetic bounded response."}],"stop_reason":"end_turn","stop_sequence":None,
      "usage":{"input_tokens":10,"output_tokens":4}}}

class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gateway=Path(os.environ["BOOSTER_GATEWAY"])
        cls.worker=Path(os.environ["BOOSTER_WORKER"])
        cls.deps=Path(os.environ["BOOSTER_DEPS"])

    def setUp(self):
        td=tempfile.TemporaryDirectory(); self.addCleanup(td.cleanup)
        self.d=Path(td.name); self.ledger=self.d/"ledger.sqlite"

    def runtime(self):
        return br.Runtime(gateway_path=self.gateway,live_worker_path=self.worker,deps=self.deps,ledger_path=self.ledger)

    def run_case(self,r,a,rep):
        return self.runtime().run(br.BoosterRequest(**{**r,"tools":tuple(r["tools"])}),
                                  br.Authority(**{**a,"tools":tuple(a["tools"])}),rep)

    def test_openai_replay_e2e(self):
        r=request(); out=self.run_case(r,authority(r),openai_fixture())
        self.assertEqual((out.technical_status,out.terminal_status,out.provider,out.model),
                         ("completed","PASS_RESOURCE_SYNTHETIC","openai","gpt-5.6-luna"))
        self.assertEqual(out.output,"SYNTHETIC_OK")
        self.assertEqual((out.project_acceptance,out.review_required,out.live_provider_calls,out.credential_reads),
                         ("NOT_GRANTED",True,0,0))

    def test_anthropic_replay_e2e(self):
        r=request("anthropic","synthetic-model-for-contract-test")
        out=self.run_case(r,authority(r),anthropic_fixture())
        self.assertEqual((out.technical_status,out.terminal_status,out.provider),
                         ("completed","PASS_RESOURCE_SYNTHETIC","anthropic"))
        self.assertEqual(out.output,"Synthetic bounded response.")
        self.assertEqual(dict(out.usage)["total_tokens"],14)

    def test_authority_binding_fail_closed_before_claim(self):
        r=request(); a=authority(r,writer_blob="5"*40)
        with self.assertRaisesRegex(br.BoosterError,"BLOCKED_AUTHORITY_BINDING"):
            self.run_case(r,a,openai_fixture())
        self.assertFalse(self.ledger.exists())

    def test_privacy_and_tools_fail_closed(self):
        r=request(privacy_class="project_internal"); a=authority(r)
        with self.assertRaisesRegex(br.BoosterError,"BLOCKED_PRIVACY_BOUNDARY"): self.run_case(r,a,openai_fixture())
        r=request(tools=["shell"]); a=authority(r)
        with self.assertRaisesRegex(br.BoosterError,"BLOCKED_TOOL_AUTHORITY"): self.run_case(r,a,openai_fixture())

    def test_no_silent_fallback_on_model_mismatch(self):
        r=request()
        out=self.run_case(r,authority(r),openai_fixture("gpt-5.6-terra"))
        self.assertEqual(out.technical_status,"blocked")
        self.assertEqual(out.terminal_status,"BLOCKED_MODEL_UNAVAILABLE")
        self.assertEqual(out.provider,"openai")

    def test_duplicate_one_shot_rejected(self):
        r=request(); a=authority(r); self.run_case(r,a,openai_fixture())
        with self.assertRaisesRegex(br.BoosterError,"BLOCKED_DUPLICATE_CALL"):
            self.run_case(r,a,openai_fixture())

    def test_exactly_one_concurrent_claimant(self):
        r=request(); a=authority(r); results=[]; lock=threading.Lock()
        rt=self.runtime()
        rr=br.BoosterRequest(**{**r,"tools":tuple(r["tools"])})
        aa=br.Authority(**{**a,"tools":tuple(a["tools"])})
        def go():
            try: x=rt.run(rr,aa,openai_fixture()); v=("ok",x.technical_status)
            except Exception as e: v=("err",str(e))
            with lock: results.append(v)
        ts=[threading.Thread(target=go) for _ in range(6)]
        [x.start() for x in ts]; [x.join() for x in ts]
        self.assertEqual(sum(x[0]=="ok" for x in results),1)
        self.assertEqual(sum("BLOCKED_DUPLICATE_CALL" in x[1] for x in results),5)
        self.assertEqual(rt.ledger.count(),1)

    def test_worker_safety_contract_preserved(self):
        rt=self.runtime(); p=rt.worker.WorkerPolicy()
        self.assertEqual((p.max_calls,p.automatic_retries),(1,0))
        self.assertLessEqual(p.timeout_seconds,60); self.assertLessEqual(p.max_response_bytes,65536)
        self.assertIn("FailClosedRedirect",Path(self.worker).read_text())
        self.assertIn("secretref:",Path(self.worker).read_text())

    def test_result_authority_boundary(self):
        r=request(); out=self.run_case(r,authority(r),openai_fixture())
        self.assertFalse(out.caller_writer_changed); self.assertFalse(out.gateway_writer_authority)
        self.assertFalse(out.provider_writer_authority); self.assertFalse(out.project_state_applied)
        self.assertFalse(out.external_dispatch_performed); self.assertTrue(out.review_required)

    def test_input_schema_rejects_secret_or_live_fields(self):
        r=request(); a=authority(r)
        raw={"request":r,"authority":a,"replay":openai_fixture(),"credential":"secretref:openai:x"}
        with self.assertRaisesRegex(br.BoosterError,"BLOCKED_INPUT_SCHEMA"): br.parse_input(br.canonical(raw))
        a=dict(a); a["live_execution_authorized"]=True
        with self.assertRaisesRegex(br.BoosterError,"BLOCKED_LIVE_EXECUTION_AUTHORITY"):
            self.run_case(r,a,openai_fixture())

    def test_bounded_serialized_result(self):
        r=request(); out=self.run_case(r,authority(r),openai_fixture())
        self.assertLessEqual(len(br.canonical(br.asdict(out))),br.MAX_RESULT_BYTES)

if __name__=="__main__": unittest.main(verbosity=2)
