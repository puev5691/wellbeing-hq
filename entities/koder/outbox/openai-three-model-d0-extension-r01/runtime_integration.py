from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any
from policy import MODELS, PolicyViolation, valid_synthetic_config
from openai_adapter import AdapterError, MockHTTPResponse, MockTransport, OpenAIResponsesAdapter

CAPABILITY_MODELS=MODELS
LIVE_GATE={"switch_name":"OPENAI_LIVE_D0","switch_value":"EXPLICIT_D0_LIVE","runtime_path":"/home/pev5691/openai-d0-runtime-r01","authority":"separate_KOO_OPERATOR_gate_required"}

@dataclass(frozen=True)
class RuntimeRequest:
    run_id:str
    model:str
    text:str
    data_class:str="D0_SYNTHETIC"
    tools_allowed:bool=False
@dataclass(frozen=True)
class RuntimeResponse:
    run_id:str
    provider:str
    model:str
    terminal_status:str
    text:str
    telemetry:dict[str,Any]
    routing_state:str="not_started"

def fixture(model:str,text:str="SYNTHETIC_RUNTIME_OK")->dict[str,Any]:
    return {"id":"resp_runtime_"+model,"object":"response","model":model,"status":"completed","output":[{"type":"message","id":"msg_runtime","status":"completed","role":"assistant","content":[{"type":"output_text","text":text,"annotations":[]}]}],"output_text":text,"usage":{"input_tokens":11,"output_tokens":4,"total_tokens":15},"tools":[]}

class DryRunRuntime:
    def __init__(self): self.transport_calls=0
    def run(self,req:RuntimeRequest)->RuntimeResponse:
        cfg=valid_synthetic_config(req.model,req.text)
        cfg["data_class"]=req.data_class
        cfg["tools_allowed"]=req.tools_allowed
        transport=MockTransport(MockHTTPResponse(200,fixture(req.model)))
        out=OpenAIResponsesAdapter().run_mock(cfg,transport)
        self.transport_calls+=transport.calls
        parsed=out["parsed_response"]
        telemetry={"provider":"openai","model":parsed["model"],"tokens":parsed["usage"],"retries":0,"result":"PASS_SYNTHETIC_OPENAI_D0_RUNTIME","fallback_used":out["provenance"]["fallback_used"],"external_network_used":out["provenance"]["external_network_used"]}
        return RuntimeResponse(req.run_id,"openai",parsed["model"],"PASS_SYNTHETIC_OPENAI_D0_RUNTIME",parsed["text"],telemetry)

def live_gate_contract()->dict[str,str]:
    return dict(LIVE_GATE)
