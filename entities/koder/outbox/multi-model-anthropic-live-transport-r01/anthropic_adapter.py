from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Mapping, Protocol
from policy import *

INPUT_USD_PER_MTOK=Decimal("2")
OUTPUT_USD_PER_MTOK=Decimal("10")

class AdapterError(RuntimeError):
    def __init__(self,code:str,*,http_status:int|None=None,retriable:bool=False):
        super().__init__(code); self.code=code; self.http_status=http_status; self.retriable=retriable

def assert_future_live_auth_available(available:bool)->None:
    if available is not True: raise AdapterError("AUTH_MISSING")

def build_request_plan(n:Mapping[str,Any])->dict[str,Any]:
    if n["provider"]!=PROVIDER or n["model"]!=MODEL: raise PolicyViolation("provider_model_mismatch")
    body={"model":MODEL,"max_tokens":n["max_tokens"],"messages":[{"role":"user","content":[{"type":"text","text":n["synthetic_text"]}]}]}
    p={"method":"POST","url":ENDPOINT,"headers":{"anthropic-version":ANTHROPIC_VERSION,"content-type":"application/json"},"credential_ref":credential_contract(),"body":body,"network_execution_enabled":False,"transport_mode":"mock_only"}
    p["request_hash"]=sha256_json({"method":p["method"],"url":p["url"],"headers":p["headers"],"body":body})
    return p

@dataclass(frozen=True)
class MockHTTPResponse:
    status:int
    body:Mapping[str,Any]
class Transport(Protocol):
    external_network_used:bool
    def send(self,plan:Mapping[str,Any])->MockHTTPResponse:...
class MockTransport:
    external_network_used=False
    def __init__(self,response:MockHTTPResponse):self.response=response;self.calls=0;self.last_plan=None
    def send(self,plan:Mapping[str,Any])->MockHTTPResponse:
        if plan.get("network_execution_enabled") is not False or plan.get("transport_mode")!="mock_only": raise AdapterError("MOCK_TRANSPORT_REFUSED_NONMOCK_PLAN")
        if plan.get("url")!=ENDPOINT or plan.get("method")!="POST": raise AdapterError("MOCK_TRANSPORT_ROUTE_MISMATCH")
        self.calls+=1;self.last_plan=plan;return self.response

def _usage(v:Any)->dict[str,int]:
    if not isinstance(v,Mapping):raise AdapterError("MALFORMED_RESPONSE_USAGE")
    if set(v)-{"input_tokens","output_tokens"}:raise AdapterError("UNSUPPORTED_USAGE_FIELDS")
    out={}
    for k in ("input_tokens","output_tokens"):
        x=v.get(k)
        if not isinstance(x,int) or isinstance(x,bool) or x<0:raise AdapterError("MALFORMED_RESPONSE_USAGE")
        out[k]=x
    return out

def parse_success_response(body:Mapping[str,Any])->dict[str,Any]:
    if not isinstance(body,Mapping) or body.get("type")!="message" or body.get("role")!="assistant":raise AdapterError("MALFORMED_RESPONSE")
    if body.get("model")!=MODEL:raise AdapterError("RESPONSE_MODEL_MISMATCH")
    mid=body.get("id"); content=body.get("content")
    if not isinstance(mid,str) or not mid or not isinstance(content,list) or not content:raise AdapterError("MALFORMED_RESPONSE")
    texts=[]
    for b in content:
        if not isinstance(b,Mapping) or b.get("type")!="text" or not isinstance(b.get("text"),str):raise AdapterError("NON_TEXT_OR_TOOL_RESPONSE_FORBIDDEN")
        texts.append(b["text"])
    return {"message_id":mid,"model":MODEL,"text":"".join(texts),"stop_reason":body.get("stop_reason"),"usage":_usage(body.get("usage"))}

def estimate_cost(u:Mapping[str,int])->dict[str,Any]:
    i=Decimal(u["input_tokens"])*INPUT_USD_PER_MTOK/Decimal(1_000_000);o=Decimal(u["output_tokens"])*OUTPUT_USD_PER_MTOK/Decimal(1_000_000)
    return {"currency":"USD","estimate_only":True,"pricing_basis":{"model":MODEL,"input_usd_per_mtok":str(INPUT_USD_PER_MTOK),"output_usd_per_mtok":str(OUTPUT_USD_PER_MTOK),"source":"accepted_KOO_task_and_KAN_readiness_basis"},"input_cost_usd":format(i,"f"),"output_cost_usd":format(o,"f"),"total_cost_usd":format(i+o,"f")}

def _http_error(r:MockHTTPResponse)->None:
    if r.status in {401,403}:raise AdapterError("AUTH_ERROR",http_status=r.status)
    if r.status==429:raise AdapterError("RATE_LIMITED",http_status=429,retriable=True)
    raise AdapterError("PROVIDER_HTTP_ERROR",http_status=r.status,retriable=r.status>=500)

class AnthropicDirectAdapter:
    def __init__(self):self.guard=PolicyGuard()
    def run_mock(self,config:Mapping[str,Any],transport:Transport)->dict[str,Any]:
        if not isinstance(transport,MockTransport) or transport.external_network_used is not False:raise PolicyViolation("mock_transport_only")
        g=self.guard.evaluate(config);plan=build_request_plan(g.normalized);r=transport.send(plan)
        if r.status!=200:_http_error(r)
        parsed=parse_success_response(r.body);response_hash=sha256_json(r.body);cost=estimate_cost(parsed["usage"])
        prov={"provider":PROVIDER,"model":MODEL,"anthropic_version":ANTHROPIC_VERSION,"request_hash":plan["request_hash"],"response_hash":response_hash,"input_tokens":parsed["usage"]["input_tokens"],"output_tokens":parsed["usage"]["output_tokens"],"adapter_version":ADAPTER_VERSION,"policy_decision":g.decision,"data_class":DATA_CLASS,"input_locator":g.normalized["input_locator"],"synthetic_text_sha256":g.normalized["synthetic_text_sha256"],"external_network_used":False,"tools_used":False,"search_used":False,"files_used":False,"caching_used":False,"mcp_used":False,"managed_agents_used":False,"code_execution_used":False,"fallback_used":False,"project_mutation_performed":False,"production":False}
        result={"parsed_response":parsed,"cost_estimate":cost,"provenance":prov,"provenance_hash":sha256_json(prov),"request_plan":plan};result["result_identity"]=sha256_json(result);return result
