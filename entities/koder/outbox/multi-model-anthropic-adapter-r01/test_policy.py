import unittest
from anthropic_adapter import AnthropicDirectAdapter, MockHTTPResponse, MockTransport, PolicyViolation, valid_synthetic_config, MODEL

def ok():return MockHTTPResponse(200,{"id":"msg_synthetic_001","type":"message","role":"assistant","model":MODEL,"content":[{"type":"text","text":"SYNTHETIC"}],"stop_reason":"end_turn","usage":{"input_tokens":125,"output_tokens":7}})
class PolicyTests(unittest.TestCase):
 def exec_cfg(self,c):return AnthropicDirectAdapter().run_mock(c,MockTransport(ok()))
 def test_non_d0(self):
  c=valid_synthetic_config();c["data_class"]="D2_INTERNAL_LOW"
  with self.assertRaisesRegex(PolicyViolation,"D0_SYNTHETIC"):self.exec_cfg(c)
 def test_unknown_provider_model(self):
  for f,v,m in (("provider","x","unknown_provider"),("model","x","unknown_model")):
   c=valid_synthetic_config();c[f]=v
   with self.assertRaisesRegex(PolicyViolation,m):self.exec_cfg(c)
 def test_forbidden_flags(self):
  for f in ("tools_allowed","search_allowed","files_allowed","caching_allowed","mcp_allowed","managed_agents_allowed","code_execution_allowed","fallback_allowed","alternate_provider_allowed","network_allowed","project_mutation_allowed","production_allowed"):
   c=valid_synthetic_config();c[f]=True
   with self.assertRaisesRegex(PolicyViolation,f+"_must_be_false"):self.exec_cfg(c)
 def test_credential_field_value(self):
  c=valid_synthetic_config();c["api_key"]="placeholder"
  with self.assertRaisesRegex(PolicyViolation,"credential_like_field"):self.exec_cfg(c)
  c=valid_synthetic_config();c["synthetic_text"]="token=SHOULD_NOT_APPEAR_123"
  with self.assertRaisesRegex(PolicyViolation,"credential_like_value"):self.exec_cfg(c)
 def test_private_locator_text(self):
  c=valid_synthetic_config();c["input_locator"]="https://github.com/puev5691/wellbeing-hq/x"
  with self.assertRaisesRegex(PolicyViolation,"project_or_private_locator"):self.exec_cfg(c)
  c=valid_synthetic_config("read entities/koder/private.md")
  with self.assertRaisesRegex(PolicyViolation,"project_or_private_data"):self.exec_cfg(c)
 def test_max_tokens(self):
  for v in (0,1025,-1,True):
   c=valid_synthetic_config();c["max_tokens"]=v
   with self.assertRaisesRegex(PolicyViolation,"max_tokens_out"):self.exec_cfg(c)
