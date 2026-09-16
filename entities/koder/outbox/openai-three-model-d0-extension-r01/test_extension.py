from __future__ import annotations
import unittest
import policy
import openai_adapter as oa
import live_transport as lt
import runtime_integration as ri

MODELS=("gpt-5.6-luna","gpt-5.6-terra","gpt-5.6-sol")
def response(model:str,text:str="SYNTHETIC"):
    return {"id":"resp-"+model,"object":"response","model":model,"status":"completed","output":[{"type":"message","id":"msg-1","status":"completed","role":"assistant","content":[{"type":"output_text","text":text,"annotations":[]}]}],"output_text":text,"usage":{"input_tokens":11,"output_tokens":5,"total_tokens":16},"tools":[]}

class ExtensionTests(unittest.TestCase):
    def test_01_allowlist_exact(self):
        self.assertEqual(policy.MODELS,frozenset(MODELS)); self.assertEqual(ri.CAPABILITY_MODELS,frozenset(MODELS))
    def test_02_three_positive_dry_runs(self):
        for model in MODELS:
            with self.subTest(model=model):
                cfg=policy.valid_synthetic_config(model); t=oa.MockTransport(oa.MockHTTPResponse(200,response(model))); r=oa.OpenAIResponsesAdapter().run_mock(cfg,t)
                self.assertEqual(r["request_plan"]["body"]["model"],model); self.assertEqual(r["parsed_response"]["model"],model); self.assertEqual(r["provenance"]["model"],model); self.assertFalse(r["provenance"]["fallback_used"])
    def test_03_unknown_model_rejected_before_transport(self):
        cfg=policy.valid_synthetic_config("gpt-5.6-bogus"); t=oa.MockTransport(oa.MockHTTPResponse(200,response("gpt-5.6-bogus")))
        with self.assertRaisesRegex(policy.PolicyViolation,"unknown_model"): oa.OpenAIResponsesAdapter().run_mock(cfg,t)
        self.assertEqual(t.calls,0)
    def test_04_response_model_mismatch_each_selected_model(self):
        for model in MODELS:
            wrong=next(x for x in MODELS if x!=model); t=oa.MockTransport(oa.MockHTTPResponse(200,response(wrong)))
            with self.subTest(model=model):
                with self.assertRaisesRegex(oa.AdapterError,"RESPONSE_MODEL_MISMATCH"): oa.OpenAIResponsesAdapter().run_mock(policy.valid_synthetic_config(model),t)
                self.assertEqual(t.calls,1)
    def test_05_no_fallback_substitution(self):
        for model in MODELS:
            t=oa.MockTransport(oa.MockHTTPResponse(500,{}))
            with self.subTest(model=model):
                with self.assertRaises(oa.AdapterError): oa.OpenAIResponsesAdapter().run_mock(policy.valid_synthetic_config(model),t)
                self.assertEqual(t.last_plan["body"]["model"],model); self.assertEqual(t.calls,1)
    def test_06_privacy_and_tool_boundaries(self):
        for field in ("tools_allowed","web_search_allowed","file_search_allowed","computer_use_allowed","code_execution_allowed","fallback_allowed","alternate_provider_allowed","network_allowed","project_mutation_allowed","production_allowed"):
            c=policy.valid_synthetic_config("gpt-5.6-luna"); c[field]=True; t=oa.MockTransport(oa.MockHTTPResponse(200,response("gpt-5.6-luna")))
            with self.subTest(field=field):
                with self.assertRaises(policy.PolicyViolation): oa.OpenAIResponsesAdapter().run_mock(c,t)
                self.assertEqual(t.calls,0)
    def test_07_live_switch_secret_gate_preserved(self):
        self.assertEqual(lt.LIVE_SWITCH_ENV,"OPENAI_LIVE_D0"); self.assertEqual(lt.LIVE_SWITCH_VALUE,"EXPLICIT_D0_LIVE")
        for model in MODELS:
            plan=oa.build_request_plan(policy.PolicyGuard().evaluate(policy.valid_synthetic_config(model)).normalized)
            ex=lt.InjectedHTTPExecutor(lambda model=model,**kw: lt.HTTPResult(200,response(model))); sr=lt.InjectedSecretReader(); out=lt.OpenAIResponsesLiveTransport(ex,sr).run_test_injected(plan)
            self.assertEqual(out["parsed_response"]["model"],model); self.assertFalse(out["provenance"]["external_network_used"])
        plan=oa.build_request_plan(policy.PolicyGuard().evaluate(policy.valid_synthetic_config("gpt-5.6-luna")).normalized)
        real=lt.OpenAIResponsesLiveTransport(lt.UrllibExecutor(),lt.EnvironmentSecretReader())
        with self.assertRaisesRegex(lt.LiveTransportError,"LIVE_SWITCH_DENIED"): real.run_live(plan,live_switch=None)
        self.assertEqual(real.executor.calls,0)
    def test_08_runtime_end_to_end_three_models(self):
        r=ri.DryRunRuntime()
        for model in MODELS:
            with self.subTest(model=model):
                out=r.run(ri.RuntimeRequest("run-"+model,model,"synthetic")); self.assertEqual(out.model,model); self.assertEqual(out.telemetry["model"],model); self.assertFalse(out.telemetry["fallback_used"]); self.assertFalse(out.telemetry["external_network_used"]); self.assertEqual(out.routing_state,"not_started")
        self.assertEqual(r.transport_calls,3)
    def test_09_runtime_unknown_model_before_transport(self):
        r=ri.DryRunRuntime()
        with self.assertRaisesRegex(policy.PolicyViolation,"unknown_model"): r.run(ri.RuntimeRequest("bad","gpt-5.6-bogus","synthetic"))
        self.assertEqual(r.transport_calls,0)
    def test_10_runtime_privacy_tools_fail_closed(self):
        for req in (ri.RuntimeRequest("p","gpt-5.6-luna","synthetic",data_class="D1_PROJECT"),ri.RuntimeRequest("t","gpt-5.6-luna","synthetic",tools_allowed=True)):
            r=ri.DryRunRuntime()
            with self.assertRaises(policy.PolicyViolation): r.run(req)
            self.assertEqual(r.transport_calls,0)

if __name__=="__main__": unittest.main(verbosity=2)
