import json, unittest
from copy import deepcopy
from unittest.mock import patch
import urllib.request

from policy import PolicyGuard, PolicyViolation, valid_synthetic_config
from anthropic_adapter import build_request_plan
from live_transport import *


def good_body(inp=125,out=7):
    return {"id":"msg_synthetic_001","type":"message","role":"assistant","model":"claude-sonnet-5","content":[{"type":"text","text":"SYNTHETIC"}],"stop_reason":"end_turn","usage":{"input_tokens":inp,"output_tokens":out}}

def plan():
    g=PolicyGuard().evaluate(valid_synthetic_config())
    return build_request_plan(g.normalized)

class TestLiveTransport(unittest.TestCase):
    def setUp(self):
        self.urlopen_patch=patch.object(urllib.request,"urlopen",side_effect=AssertionError("network forbidden in tests"))
        self.urlopen_patch.start()
    def tearDown(self): self.urlopen_patch.stop()

    def run_injected(self,result=None,handler=None,secret="TEST_ONLY_CREDENTIAL_PLACEHOLDER"):
        if handler is None:
            result=result or HTTPResult(200,good_body())
            handler=lambda **_: result
        ex=InjectedHTTPExecutor(handler)
        sr=InjectedSecretReader(secret)
        tr=AnthropicLiveTransport(ex,sr)
        out=tr.run_test_injected(plan())
        return out,ex,sr,tr

    def test_blueprint_accepts_exact_route(self): validate_blueprint(plan())
    def test_blueprint_rejects_host_change(self):
        p=plan();p["url"]="https://example.invalid/v1/messages"
        with self.assertRaisesRegex(PolicyViolation,"live_route_forbidden"): validate_blueprint(p)
    def test_blueprint_rejects_path_change(self):
        p=plan();p["url"]="https://api.anthropic.com/v1/other"
        with self.assertRaisesRegex(PolicyViolation,"live_route_forbidden"): validate_blueprint(p)
    def test_blueprint_rejects_auth_header_in_blueprint(self):
        p=plan();p["headers"]["x-api-key"]="x"
        with self.assertRaisesRegex(PolicyViolation,"live_headers_blueprint_mismatch"): validate_blueprint(p)
    def test_blueprint_rejects_body_tools(self):
        p=plan();p["body"]["tools"]=[]
        with self.assertRaisesRegex(PolicyViolation,"live_body_shape_mismatch"): validate_blueprint(p)
    def test_live_switch_default_denied(self):
        with self.assertRaisesRegex(LiveTransportError,"LIVE_SWITCH_DENIED"): require_live_switch(None)
    def test_live_switch_wrong_value_denied(self):
        with self.assertRaisesRegex(LiveTransportError,"LIVE_SWITCH_DENIED"): require_live_switch("yes")
    def test_injected_success_keeps_external_false(self):
        out,ex,sr,tr=self.run_injected()
        self.assertFalse(out["provenance"]["external_network_used"]);self.assertFalse(tr.external_network_used);self.assertEqual(ex.calls,1)
    def test_injected_auth_not_in_result(self):
        secret="TEST_ONLY_CREDENTIAL_PLACEHOLDER"
        out,ex,_,_=self.run_injected(secret=secret)
        self.assertNotIn(secret,json.dumps(out,sort_keys=True));self.assertEqual(ex.last_request["headers"]["x-api-key"],secret)
    def test_cost_estimate(self):
        out,_,_,_=self.run_injected()
        self.assertEqual(out["cost_estimate"]["total_cost_usd"],"0.00032");self.assertTrue(out["cost_estimate"]["estimate_only"])
    def test_401_fail_closed_no_retry(self):
        ex=InjectedHTTPExecutor(lambda **_:HTTPResult(401,{}));tr=AnthropicLiveTransport(ex,InjectedSecretReader())
        with self.assertRaises(LiveTransportError) as cm: tr.run_test_injected(plan())
        self.assertEqual(cm.exception.code,"AUTH_ERROR");self.assertEqual(ex.calls,1);self.assertFalse(cm.exception.external_network_used)
    def test_403_fail_closed_no_retry(self):
        ex=InjectedHTTPExecutor(lambda **_:HTTPResult(403,{}));tr=AnthropicLiveTransport(ex,InjectedSecretReader())
        with self.assertRaises(LiveTransportError) as cm: tr.run_test_injected(plan())
        self.assertEqual(cm.exception.code,"AUTH_ERROR");self.assertEqual(ex.calls,1)
    def test_429_retriable_but_no_auto_retry(self):
        ex=InjectedHTTPExecutor(lambda **_:HTTPResult(429,{}));tr=AnthropicLiveTransport(ex,InjectedSecretReader())
        with self.assertRaises(LiveTransportError) as cm: tr.run_test_injected(plan())
        self.assertEqual(cm.exception.code,"RATE_LIMITED");self.assertTrue(cm.exception.retriable);self.assertEqual(ex.calls,1)
    def test_500_retriable_but_no_auto_retry(self):
        ex=InjectedHTTPExecutor(lambda **_:HTTPResult(500,{}));tr=AnthropicLiveTransport(ex,InjectedSecretReader())
        with self.assertRaises(LiveTransportError) as cm: tr.run_test_injected(plan())
        self.assertEqual(cm.exception.code,"PROVIDER_HTTP_ERROR");self.assertTrue(cm.exception.retriable);self.assertEqual(ex.calls,1)
    def test_timeout_no_auto_retry(self):
        def h(**_): raise TimeoutError()
        ex=InjectedHTTPExecutor(h);tr=AnthropicLiveTransport(ex,InjectedSecretReader())
        with self.assertRaises(LiveTransportError) as cm: tr.run_test_injected(plan())
        self.assertEqual(cm.exception.code,"NETWORK_TIMEOUT");self.assertTrue(cm.exception.retriable);self.assertEqual(ex.calls,1);self.assertFalse(cm.exception.external_network_used)
    def test_generic_network_error_sanitized(self):
        secret="TEST_ONLY_CREDENTIAL_PLACEHOLDER"
        def h(**_): raise RuntimeError("do not expose "+secret)
        ex=InjectedHTTPExecutor(h);tr=AnthropicLiveTransport(ex,InjectedSecretReader(secret))
        with self.assertRaises(LiveTransportError) as cm: tr.run_test_injected(plan())
        self.assertEqual(str(cm.exception),"NETWORK_ERROR");self.assertNotIn(secret,str(cm.exception));self.assertEqual(ex.calls,1)
    def test_tool_response_rejected(self):
        b=good_body();b["content"]=[{"type":"tool_use","id":"x","name":"x","input":{}}]
        ex=InjectedHTTPExecutor(lambda **_:HTTPResult(200,b));tr=AnthropicLiveTransport(ex,InjectedSecretReader())
        with self.assertRaisesRegex(LiveTransportError,"NON_TEXT_OR_TOOL_RESPONSE_FORBIDDEN"): tr.run_test_injected(plan())
    def test_malformed_usage_rejected(self):
        b=good_body();b["usage"]={"input_tokens":"125","output_tokens":7}
        ex=InjectedHTTPExecutor(lambda **_:HTTPResult(200,b));tr=AnthropicLiveTransport(ex,InjectedSecretReader())
        with self.assertRaisesRegex(LiveTransportError,"MALFORMED_RESPONSE_USAGE"): tr.run_test_injected(plan())
    def test_model_mismatch_rejected(self):
        b=good_body();b["model"]="other"
        ex=InjectedHTTPExecutor(lambda **_:HTTPResult(200,b));tr=AnthropicLiveTransport(ex,InjectedSecretReader())
        with self.assertRaisesRegex(LiveTransportError,"RESPONSE_MODEL_MISMATCH"): tr.run_test_injected(plan())
    def test_invalid_timeout_rejected_before_executor(self):
        ex=InjectedHTTPExecutor(lambda **_:HTTPResult(200,good_body()));tr=AnthropicLiveTransport(ex,InjectedSecretReader())
        with self.assertRaisesRegex(LiveTransportError,"INVALID_TIMEOUT"): tr.run_test_injected(plan(),timeout=0)
        self.assertEqual(ex.calls,0)
    def test_non_d0_still_rejected_by_accepted_guard(self):
        c=valid_synthetic_config();c["data_class"]="D1"
        with self.assertRaisesRegex(PolicyViolation,"data_class_must_be_D0_SYNTHETIC"): PolicyGuard().evaluate(c)
    def test_tools_still_off_by_accepted_guard(self):
        c=valid_synthetic_config();c["tools_allowed"]=True
        with self.assertRaisesRegex(PolicyViolation,"tools_allowed_must_be_false"): PolicyGuard().evaluate(c)
    def test_test_path_refuses_network_executor(self):
        tr=AnthropicLiveTransport(UrllibExecutor(),InjectedSecretReader())
        with self.assertRaisesRegex(LiveTransportError,"TEST_PATH_REQUIRES_INJECTED_NONNETWORK_DEPENDENCIES"): tr.run_test_injected(plan())

if __name__=="__main__": unittest.main()
