from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping, Protocol
from policy import *

class AdapterError(RuntimeError):
    def __init__(self,code:str,*,http_status:int|None=None,retriable:bool=False):
        super().__init__(code); self.code=code; self.http_status=http_status; self.retriable=retriable

def build_request_plan(n:Mapping[str,Any])->dict[str,Any]:
    if n["provider"]!=PROVIDER: raise PolicyViolation("provider_model_mismatch")
    model=n["model"]
    if model not in MODELS: raise PolicyViolation("unknown_model")
    body={"model":model,"input":n["synthetic_text"],"max_output_tokens":n["max_output_tokens"],"store":False,"tools":[],"tool_choice":"none","parallel_tool_calls":False}
    p={"method":"POST","url":ENDPOINT,"headers":{"content-type":"application/json"},"credential_ref":credential_contract(),"body":body,"network_execution_enabled":False,"transport_mode":"mock_only"}
    p["request_hash"]=sha256_json({"method":p["method"],"url":p["url"],"headers":p["headers"],"body":body})
    return p

@dataclass(frozen=True)
class MockHTTPResponse:
    status:int
    body:Mapping[str,Any]
class Transport(Protocol):
    external_network_used:bool
    def send(self,plan:Mapping[str,Any])->MockHTTPResponse: ...
class MockTransport:
    external_network_used=False
    def __init__(self,response:MockHTTPResponse|None=None,error:Exception|None=None):
        self.response=response; self.error=error; self.calls=0; self.last_plan=None
    def send(self,plan:Mapping[str,Any])->MockHTTPResponse:
        if plan.get("network_execution_enabled") is not False or plan.get("transport_mode")!="mock_only": raise AdapterError("MOCK_TRANSPORT_REFUSED_NONMOCK_PLAN")
        if plan.get("url")!=ENDPOINT or plan.get("method")!="POST": raise AdapterError("MOCK_TRANSPORT_ROUTE_MISMATCH")
        self.calls+=1; self.last_plan=plan
        if self.error is not None: raise self.error
        if self.response is None: raise AdapterError("MOCK_RESPONSE_REQUIRED")
        return self.response

def _nonneg_int(v:Any,code:str)->int:
    if not isinstance(v,int) or isinstance(v,bool) or v<0: raise AdapterError(code)
    return v

def _usage(v:Any)->dict[str,int]:
    if not isinstance(v,Mapping): raise AdapterError("MALFORMED_RESPONSE_USAGE")
    out={"input_tokens":_nonneg_int(v.get("input_tokens"),"MALFORMED_RESPONSE_USAGE"),"output_tokens":_nonneg_int(v.get("output_tokens"),"MALFORMED_RESPONSE_USAGE"),"total_tokens":_nonneg_int(v.get("total_tokens"),"MALFORMED_RESPONSE_USAGE")}
    itd=v.get("input_tokens_details")
    if itd is not None:
        if not isinstance(itd,Mapping): raise AdapterError("MALFORMED_RESPONSE_USAGE")
        if "cached_tokens" in itd: out["cached_input_tokens"]=_nonneg_int(itd["cached_tokens"],"MALFORMED_RESPONSE_USAGE")
        if "cache_write_tokens" in itd: out["cache_write_tokens"]=_nonneg_int(itd["cache_write_tokens"],"MALFORMED_RESPONSE_USAGE")
    otd=v.get("output_tokens_details")
    if otd is not None:
        if not isinstance(otd,Mapping): raise AdapterError("MALFORMED_RESPONSE_USAGE")
        if "reasoning_tokens" in otd: out["reasoning_tokens"]=_nonneg_int(otd["reasoning_tokens"],"MALFORMED_RESPONSE_USAGE")
    return out

def _extract_text(body:Mapping[str,Any])->str:
    output=body.get("output")
    if not isinstance(output,list): raise AdapterError("MALFORMED_RESPONSE_OUTPUT")
    texts=[]
    for item in output:
        if not isinstance(item,Mapping): raise AdapterError("MALFORMED_RESPONSE_OUTPUT")
        typ=item.get("type")
        if typ=="reasoning": continue
        if typ!="message" or item.get("role")!="assistant": raise AdapterError("TOOL_OR_UNSUPPORTED_OUTPUT_FORBIDDEN")
        content=item.get("content")
        if not isinstance(content,list) or not content: raise AdapterError("MALFORMED_RESPONSE_CONTENT")
        for block in content:
            if not isinstance(block,Mapping) or block.get("type")!="output_text" or not isinstance(block.get("text"),str): raise AdapterError("NON_TEXT_RESPONSE_FORBIDDEN")
            texts.append(block["text"])
    text="".join(texts)
    if not text: raise AdapterError("EMPTY_RESPONSE_TEXT")
    top=body.get("output_text")
    if top is not None and (not isinstance(top,str) or top!=text): raise AdapterError("OUTPUT_TEXT_MISMATCH")
    return text

def parse_success_response(body:Mapping[str,Any],expected_model:str)->dict[str,Any]:
    if expected_model not in MODELS: raise AdapterError("EXPECTED_MODEL_NOT_ALLOWLISTED")
    if not isinstance(body,Mapping) or body.get("object")!="response": raise AdapterError("MALFORMED_RESPONSE")
    if body.get("model")!=expected_model: raise AdapterError("RESPONSE_MODEL_MISMATCH")
    rid=body.get("id"); status=body.get("status")
    if not isinstance(rid,str) or not rid: raise AdapterError("MALFORMED_RESPONSE_ID")
    if status not in {"completed","failed","in_progress","cancelled","queued","incomplete"}: raise AdapterError("MALFORMED_RESPONSE_STATUS")
    if status!="completed": raise AdapterError("RESPONSE_NOT_COMPLETED")
    if body.get("tools") not in (None,[]): raise AdapterError("TOOLS_RESPONSE_FORBIDDEN")
    return {"response_id":rid,"model":expected_model,"status":status,"text":_extract_text(body),"usage":_usage(body.get("usage"))}

def _http_error(r:MockHTTPResponse)->None:
    if r.status in {401,403}: raise AdapterError("AUTH_ERROR",http_status=r.status)
    if r.status==429: raise AdapterError("RATE_LIMITED",http_status=429,retriable=True)
    if r.status>=500: raise AdapterError("PROVIDER_HTTP_ERROR",http_status=r.status,retriable=True)
    raise AdapterError("PROVIDER_HTTP_ERROR",http_status=r.status)

class OpenAIResponsesAdapter:
    def __init__(self): self.guard=PolicyGuard()
    def run_mock(self,config:Mapping[str,Any],transport:Transport)->dict[str,Any]:
        if not isinstance(transport,MockTransport) or transport.external_network_used is not False: raise PolicyViolation("mock_transport_only")
        g=self.guard.evaluate(config); selected_model=g.normalized["model"]; plan=build_request_plan(g.normalized)
        try: r=transport.send(plan)
        except TimeoutError: raise AdapterError("NETWORK_TIMEOUT",retriable=True) from None
        except OSError: raise AdapterError("NETWORK_ERROR",retriable=True) from None
        if r.status!=200: _http_error(r)
        parsed=parse_success_response(r.body,selected_model); response_hash=sha256_json(r.body)
        prov={"provider":PROVIDER,"model":selected_model,"adapter_version":ADAPTER_VERSION,"endpoint":ENDPOINT,"request_hash":plan["request_hash"],"response_hash":response_hash,"response_id":parsed["response_id"],"response_status":parsed["status"],"normalized_usage":parsed["usage"],"policy_decision":g.decision,"data_class":DATA_CLASS,"input_locator":g.normalized["input_locator"],"synthetic_text_sha256":g.normalized["synthetic_text_sha256"],"credential_source":CREDENTIAL_ENV,"credential_value_recorded":False,"external_network_used":False,"tools_used":False,"web_search_used":False,"file_search_used":False,"computer_use_used":False,"code_execution_used":False,"fallback_used":False,"project_mutation_performed":False,"production":False,"project_acceptance":"NOT_GRANTED"}
        result={"parsed_response":parsed,"provenance":prov,"provenance_hash":sha256_json(prov),"request_plan":plan}
        result["result_identity"]=sha256_json(result)
        return result

[executed on device: ruvds-xnqc6 (dd09a197-f716-4dd6-80bb-7f8e5d8260ff)]