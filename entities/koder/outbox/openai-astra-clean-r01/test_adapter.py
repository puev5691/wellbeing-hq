import copy, unittest
from openai_adapter import *
from policy import *

def response_fixture():
    return {
        "id":"resp_syn_001","object":"response","model":"gpt-5.6-luna","status":"completed",
        "output":[{"type":"message","id":"msg_syn_001","status":"completed","role":"assistant","content":[{"type":"output_text","text":"SYNTHETIC","annotations":[]}]}],
        "output_text":"SYNTHETIC",
        "usage":{"input_tokens":11,"input_tokens_details":{"cached_tokens":3},"output_tokens":5,"output_tokens_details":{"reasoning_tokens":2},"total_tokens":16},
        "tools":[],
    }

def run(body=None,status=200,error=None,config=None):
    t=MockTransport(MockHTTPResponse(status,body or response_fixture()) if error is None else None,error=error)
    return OpenAIResponsesAdapter().run_mock(config or valid_synthetic_config("gpt-5.6-luna"),t),t

class AdapterTests(unittest.TestCase):
    def test_valid_d0_response(self):
        result,t=run(); self.assertEqual(t.calls,1)
        self.assertEqual(result["parsed_response"]["text"],"SYNTHETIC")
        self.assertEqual(result["parsed_response"]["usage"]["cached_input_tokens"],3)
        self.assertEqual(result["parsed_response"]["usage"]["reasoning_tokens"],2)
        self.assertFalse(result["provenance"]["external_network_used"])
        self.assertEqual(result["provenance"]["project_acceptance"],"NOT_GRANTED")


    def test_exact_four_model_adapter_allowlist(self):
        for model in sorted(MODELS):
            with self.subTest(model=model):
                b=response_fixture(); b["model"]=model
                result,t=run(b,config=valid_synthetic_config(model))
                self.assertEqual(result["parsed_response"]["model"],model)
        with self.assertRaises(PolicyViolation):
            build_request_plan({"provider":PROVIDER,"model":"gpt-unknown","synthetic_text":"x","max_output_tokens":1})

    def test_request_contract(self):
        result,t=run(); p=t.last_plan
        self.assertEqual((p["method"],p["url"]),("POST",ENDPOINT))
        self.assertEqual(p["credential_ref"]["environment_variable"],"OPENAI_API_KEY")
        self.assertEqual(p["body"]["tools"],[]); self.assertEqual(p["body"]["tool_choice"],"none")
        self.assertFalse(p["body"]["store"]); self.assertFalse(p["network_execution_enabled"])

    def test_model_mismatch(self):
        b=response_fixture(); b["model"]="gpt-other"
        with self.assertRaisesRegex(AdapterError,"RESPONSE_MODEL_MISMATCH"): run(b)

    def test_output_text_mismatch(self):
        b=response_fixture(); b["output_text"]="OTHER"
        with self.assertRaisesRegex(AdapterError,"OUTPUT_TEXT_MISMATCH"): run(b)

    def test_tool_output_rejected(self):
        b=response_fixture(); b["output"]=[{"type":"web_search_call"}]; b.pop("output_text",None)
        with self.assertRaisesRegex(AdapterError,"TOOL_OR_UNSUPPORTED_OUTPUT_FORBIDDEN"): run(b)
    def test_malformed_usage(self):
        b=response_fixture(); b["usage"]["input_tokens"]="11"
        with self.assertRaisesRegex(AdapterError,"MALFORMED_RESPONSE_USAGE"): run(b)

    def test_absent_details_not_invented(self):
        b=response_fixture(); b["usage"].pop("input_tokens_details"); b["usage"].pop("output_tokens_details")
        result,_=run(b); u=result["parsed_response"]["usage"]
        self.assertNotIn("cached_input_tokens",u); self.assertNotIn("reasoning_tokens",u)

    def test_non_d0_rejects_before_transport(self):
        c=valid_synthetic_config("gpt-5.6-luna"); c["data_class"]="D1_PROJECT"; t=MockTransport(MockHTTPResponse(200,response_fixture()))
        with self.assertRaises(PolicyViolation): OpenAIResponsesAdapter().run_mock(c,t)
        self.assertEqual(t.calls,0)

    def test_restricted_capability_rejects_before_transport(self):
        for field in ("tools_allowed","web_search_allowed","file_search_allowed","computer_use_allowed","fallback_allowed","project_mutation_allowed"):
            c=valid_synthetic_config("gpt-5.6-luna"); c[field]=True; t=MockTransport(MockHTTPResponse(200,response_fixture()))
            with self.subTest(field=field):
                with self.assertRaises(PolicyViolation): OpenAIResponsesAdapter().run_mock(c,t)
                self.assertEqual(t.calls,0)

    def test_http_errors(self):
        cases=((401,"AUTH_ERROR",False),(403,"AUTH_ERROR",False),(429,"RATE_LIMITED",True),(500,"PROVIDER_HTTP_ERROR",True))
        for status,code,retry in cases:
            with self.subTest(status=status):
                with self.assertRaises(AdapterError) as cm: run(response_fixture(),status=status)
                self.assertEqual(cm.exception.code,code); self.assertEqual(cm.exception.retriable,retry)

    def test_timeout_and_network_errors(self):
        with self.assertRaisesRegex(AdapterError,"NETWORK_TIMEOUT"): run(error=TimeoutError())
        with self.assertRaisesRegex(AdapterError,"NETWORK_ERROR"): run(error=OSError("synthetic"))

    def test_deterministic_identity(self):
        a,_=run(); b,_=run()
        self.assertEqual(a["provenance_hash"],b["provenance_hash"]); self.assertEqual(a["result_identity"],b["result_identity"])

if __name__=="__main__": unittest.main(verbosity=2)
