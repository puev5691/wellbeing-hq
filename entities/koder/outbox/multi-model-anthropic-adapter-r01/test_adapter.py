import ast
from pathlib import Path
import unittest
from anthropic_adapter import *

def body():return {"id":"msg_synthetic_001","type":"message","role":"assistant","model":MODEL,"content":[{"type":"text","text":"SYNTHETIC"}],"stop_reason":"end_turn","usage":{"input_tokens":125,"output_tokens":7}}
class AdapterTests(unittest.TestCase):
 def test_success(self):
  t=MockTransport(MockHTTPResponse(200,body()));r=AnthropicDirectAdapter().run_mock(valid_synthetic_config(),t);self.assertEqual(t.calls,1);self.assertFalse(r["provenance"]["external_network_used"]);self.assertEqual(r["parsed_response"]["text"],"SYNTHETIC")
 def test_request_plan(self):
  p=build_request_plan(AnthropicDirectAdapter().guard.evaluate(valid_synthetic_config()).normalized);self.assertEqual((p["method"],p["url"]),("POST",ENDPOINT));self.assertEqual(p["body"]["model"],MODEL);self.assertEqual(p["headers"]["anthropic-version"],ANTHROPIC_VERSION);self.assertEqual(p["credential_ref"]["environment_variable"],CREDENTIAL_ENV);self.assertNotIn("authorization",{k.lower() for k in p["headers"]});self.assertFalse(p["network_execution_enabled"]);self.assertEqual(set(p["body"]),{"model","max_tokens","messages"})
 def test_cost(self):
  r=AnthropicDirectAdapter().run_mock(valid_synthetic_config(),MockTransport(MockHTTPResponse(200,body())));self.assertEqual(r["cost_estimate"]["total_cost_usd"],"0.00032")
 def test_429(self):
  t=MockTransport(MockHTTPResponse(429,{"type":"error"}))
  with self.assertRaises(AdapterError) as x:AnthropicDirectAdapter().run_mock(valid_synthetic_config(),t)
  self.assertEqual(x.exception.code,"RATE_LIMITED");self.assertEqual(t.calls,1)
 def test_500_401(self):
  for s,c in ((500,"PROVIDER_HTTP_ERROR"),(401,"AUTH_ERROR")):
   with self.assertRaises(AdapterError) as x:AnthropicDirectAdapter().run_mock(valid_synthetic_config(),MockTransport(MockHTTPResponse(s,{})))
   self.assertEqual(x.exception.code,c)
 def test_auth_missing(self):
  with self.assertRaises(AdapterError):assert_future_live_auth_available(False)
  assert_future_live_auth_available(True)
 def test_malformed_and_tool(self):
  b=body();b.pop("usage")
  with self.assertRaisesRegex(AdapterError,"MALFORMED_RESPONSE_USAGE"):AnthropicDirectAdapter().run_mock(valid_synthetic_config(),MockTransport(MockHTTPResponse(200,b)))
  b=body();b["content"]=[{"type":"tool_use","id":"x"}]
  with self.assertRaisesRegex(AdapterError,"NON_TEXT_OR_TOOL"):AnthropicDirectAdapter().run_mock(valid_synthetic_config(),MockTransport(MockHTTPResponse(200,b)))
 def test_nonmock_and_model_mismatch(self):
  class Net:external_network_used=True
  with self.assertRaisesRegex(PolicyViolation,"mock_transport_only"):AnthropicDirectAdapter().run_mock(valid_synthetic_config(),Net())
  b=body();b["model"]="other"
  with self.assertRaisesRegex(AdapterError,"RESPONSE_MODEL_MISMATCH"):AnthropicDirectAdapter().run_mock(valid_synthetic_config(),MockTransport(MockHTTPResponse(200,b)))
 def test_deterministic(self):
  a=AnthropicDirectAdapter().run_mock(valid_synthetic_config(),MockTransport(MockHTTPResponse(200,body())));b=AnthropicDirectAdapter().run_mock(valid_synthetic_config(),MockTransport(MockHTTPResponse(200,body())));self.assertEqual(a,b);self.assertRegex(a["provenance"]["request_hash"],r"^[0-9a-f]{64}$")
 def test_no_network_sdk_imports(self):
  imports=set()
  for f in ("policy.py","anthropic_adapter.py"):
   tree=ast.parse(Path(f).read_text())
   for n in ast.walk(tree):
    if isinstance(n,ast.Import):imports.update(a.name for a in n.names)
    elif isinstance(n,ast.ImportFrom):imports.add(n.module or "")
  forbidden={"socket","requests","urllib","urllib.request","http","http.client","aiohttp","httpx","anthropic","openai","mcp","subprocess"};self.assertTrue(imports.isdisjoint(forbidden),imports&forbidden)
