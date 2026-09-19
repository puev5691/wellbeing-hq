import json, os, unittest
from openai_adapter import build_request_plan
from policy import *
from live_transport import *
from test_adapter import response_fixture

class LiveTransportTests(unittest.TestCase):
    def plan(self): return build_request_plan(PolicyGuard().evaluate(valid_synthetic_config("gpt-5.6-luna")).normalized)

    def injected(self,status=200,body=None):
        def handler(**kw): return HTTPResult(status,body or response_fixture())
        ex=InjectedHTTPExecutor(handler); sr=InjectedSecretReader(); tr=OpenAIResponsesLiveTransport(ex,sr)
        return tr,ex,sr

    def test_injected_success_has_no_external_network(self):
        tr,ex,sr=self.injected(); out=tr.run_test_injected(self.plan())
        self.assertEqual(ex.calls,1); self.assertEqual(sr.reads,1)
        self.assertFalse(out["provenance"]["external_network_used"])
        self.assertEqual(ex.last_request["url"],ENDPOINT)
        self.assertTrue(ex.last_request["headers"]["authorization"].startswith("Bearer "))

    def test_live_default_deny_before_secret_or_network(self):
        ex=UrllibExecutor(); sr=EnvironmentSecretReader(); tr=OpenAIResponsesLiveTransport(ex,sr)
        old=os.environ.pop(CREDENTIAL_ENV,None)
        try:
            with self.assertRaisesRegex(LiveTransportError,"LIVE_SWITCH_DENIED"): tr.run_live(self.plan(),live_switch=None)
            self.assertEqual(ex.calls,0); self.assertFalse(tr.external_network_used)
        finally:
            if old is not None: os.environ[CREDENTIAL_ENV]=old

    def test_injected_http_errors(self):
        for status,code in ((401,"AUTH_ERROR"),(429,"RATE_LIMITED"),(500,"PROVIDER_HTTP_ERROR")):
            tr,_,_=self.injected(status=status)
            with self.subTest(status=status):
                with self.assertRaises(LiveTransportError) as cm: tr.run_test_injected(self.plan())
                self.assertEqual(cm.exception.code,code)

    def test_blueprint_rejects_tools(self):
        p=self.plan(); p["body"]["tools"]=[{"type":"web_search"}]
        with self.assertRaises(PolicyViolation): validate_blueprint(p)

    def test_blueprint_rejects_endpoint_change(self):
        p=self.plan(); p["url"]="https://example.invalid/v1/responses"
        with self.assertRaises(PolicyViolation): validate_blueprint(p)


    def test_exact_four_model_live_blueprint_allowlist(self):
        self.assertEqual(MODELS,frozenset({"gpt-5.6-luna","gpt-5.6-terra","gpt-5.6-sol","gpt-6-astra"}))
        for model in sorted(MODELS):
            with self.subTest(model=model):
                cfg=valid_synthetic_config(model)
                plan=build_request_plan(PolicyGuard().evaluate(cfg).normalized)
                validate_blueprint(plan)
        cfg=valid_synthetic_config("gpt-5.6-luna")
        plan=build_request_plan(PolicyGuard().evaluate(cfg).normalized)
        plan["body"]["model"]="gpt-unknown"
        with self.assertRaisesRegex(PolicyViolation,"live_model_forbidden"):
            validate_blueprint(plan)

if __name__=="__main__": unittest.main(verbosity=2)

[executed on device: ruvds-xnqc6 (dd09a197-f716-4dd6-80bb-7f8e5d8260ff)]