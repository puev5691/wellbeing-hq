from __future__ import annotations
from dataclasses import dataclass
import json, os, socket
from typing import Any, Callable, Mapping, Protocol
import urllib.error
import urllib.request

from policy import ANTHROPIC_VERSION, CREDENTIAL_ENV, DATA_CLASS, ENDPOINT, MODEL, PROVIDER, PolicyViolation, canonical_json, credential_contract, sha256_json
from anthropic_adapter import AdapterError, estimate_cost, parse_success_response

TRANSPORT_VERSION="anthropic-live-transport-r01"
LIVE_SWITCH_ENV="ANTHROPIC_LIVE_D0"
LIVE_SWITCH_VALUE="EXPLICIT_D0_LIVE"
DEFAULT_TIMEOUT_SECONDS=30.0
MIN_TIMEOUT_SECONDS=1.0
MAX_TIMEOUT_SECONDS=60.0

class LiveTransportError(RuntimeError):
    def __init__(self,code:str,*,http_status:int|None=None,retriable:bool=False,external_network_used:bool=False):
        super().__init__(code)
        self.code=code
        self.http_status=http_status
        self.retriable=retriable
        self.external_network_used=external_network_used

@dataclass(frozen=True)
class HTTPResult:
    status:int
    body:Mapping[str,Any]

class SecretReader(Protocol):
    def read(self,name:str)->str:...

class EnvironmentSecretReader:
    def read(self,name:str)->str:
        if name!=CREDENTIAL_ENV:
            raise LiveTransportError("AUTH_SOURCE_MISMATCH")
        value=os.environ.get(name)
        if not isinstance(value,str) or not value or len(value)>4096 or "\n" in value or "\r" in value:
            raise LiveTransportError("AUTH_MISSING_OR_INVALID")
        return value

class InjectedSecretReader:
    """Test-only dependency. Never used by run_live()."""
    def __init__(self,value:str="TEST_ONLY_CREDENTIAL_PLACEHOLDER"):
        self._value=value
        self.reads=0
    def read(self,name:str)->str:
        self.reads+=1
        if name!=CREDENTIAL_ENV:
            raise LiveTransportError("AUTH_SOURCE_MISMATCH")
        return self._value

class HTTPExecutor(Protocol):
    external_network_capable:bool
    calls:int
    def request(self,*,method:str,url:str,headers:Mapping[str,str],body:bytes,timeout:float)->HTTPResult:...

class UrllibExecutor:
    external_network_capable=True
    def __init__(self): self.calls=0
    def request(self,*,method:str,url:str,headers:Mapping[str,str],body:bytes,timeout:float)->HTTPResult:
        self.calls+=1
        req=urllib.request.Request(url=url,data=body,headers=dict(headers),method=method)
        try:
            with urllib.request.urlopen(req,timeout=timeout) as r:
                status=int(getattr(r,"status",200))
                raw=r.read()
        except urllib.error.HTTPError as e:
            return HTTPResult(int(e.code),{})
        except (TimeoutError,socket.timeout) as e:
            raise LiveTransportError("NETWORK_TIMEOUT",retriable=True,external_network_used=True) from None
        except urllib.error.URLError as e:
            raise LiveTransportError("NETWORK_ERROR",retriable=True,external_network_used=True) from None
        try:
            body_obj=json.loads(raw.decode("utf-8"))
        except Exception:
            raise LiveTransportError("MALFORMED_PROVIDER_JSON",external_network_used=True) from None
        if not isinstance(body_obj,Mapping):
            raise LiveTransportError("MALFORMED_PROVIDER_JSON",external_network_used=True)
        return HTTPResult(status,body_obj)

class InjectedHTTPExecutor:
    external_network_capable=False
    def __init__(self,handler:Callable[...,HTTPResult]):
        self.handler=handler
        self.calls=0
        self.last_request=None
    def request(self,*,method:str,url:str,headers:Mapping[str,str],body:bytes,timeout:float)->HTTPResult:
        self.calls+=1
        self.last_request={"method":method,"url":url,"headers":dict(headers),"body":body,"timeout":timeout}
        return self.handler(method=method,url=url,headers=headers,body=body,timeout=timeout)

def require_live_switch(value:str|None)->None:
    if value!=LIVE_SWITCH_VALUE:
        raise LiveTransportError("LIVE_SWITCH_DENIED")

def validate_timeout(value:float|int)->float:
    if isinstance(value,bool) or not isinstance(value,(int,float)):
        raise LiveTransportError("INVALID_TIMEOUT")
    value=float(value)
    if value<MIN_TIMEOUT_SECONDS or value>MAX_TIMEOUT_SECONDS:
        raise LiveTransportError("INVALID_TIMEOUT")
    return value

def validate_blueprint(plan:Mapping[str,Any])->None:
    if not isinstance(plan,Mapping): raise PolicyViolation("request_plan_must_be_object")
    required={"method","url","headers","credential_ref","body","network_execution_enabled","transport_mode","request_hash"}
    if set(plan)!=required: raise PolicyViolation("request_plan_shape_mismatch")
    if plan["method"]!="POST": raise PolicyViolation("live_method_forbidden")
    if plan["url"]!=ENDPOINT: raise PolicyViolation("live_route_forbidden")
    if plan["headers"]!={"anthropic-version":ANTHROPIC_VERSION,"content-type":"application/json"}: raise PolicyViolation("live_headers_blueprint_mismatch")
    if plan["credential_ref"]!=credential_contract(): raise PolicyViolation("credential_reference_mismatch")
    if plan["network_execution_enabled"] is not False or plan["transport_mode"]!="mock_only": raise PolicyViolation("accepted_blueprint_boundary_changed")
    b=plan["body"]
    if not isinstance(b,Mapping) or set(b)!={"model","max_tokens","messages"}: raise PolicyViolation("live_body_shape_mismatch")
    if b.get("model")!=MODEL: raise PolicyViolation("live_model_forbidden")
    mt=b.get("max_tokens")
    if not isinstance(mt,int) or isinstance(mt,bool) or not 1<=mt<=1024: raise PolicyViolation("live_max_tokens_out_of_bounds")
    msgs=b.get("messages")
    if not isinstance(msgs,list) or len(msgs)!=1: raise PolicyViolation("live_messages_shape_mismatch")
    m=msgs[0]
    if not isinstance(m,Mapping) or set(m)!={"role","content"} or m.get("role")!="user": raise PolicyViolation("live_message_forbidden")
    content=m.get("content")
    if not isinstance(content,list) or len(content)!=1: raise PolicyViolation("live_content_shape_mismatch")
    block=content[0]
    if not isinstance(block,Mapping) or set(block)!={"type","text"} or block.get("type")!="text" or not isinstance(block.get("text"),str): raise PolicyViolation("live_content_forbidden")
    expected=sha256_json({"method":"POST","url":ENDPOINT,"headers":plan["headers"],"body":b})
    if plan["request_hash"]!=expected: raise PolicyViolation("request_hash_mismatch")

def _authorized_headers(plan:Mapping[str,Any],secret:str)->dict[str,str]:
    if not isinstance(secret,str) or not secret or len(secret)>4096 or "\n" in secret or "\r" in secret:
        raise LiveTransportError("AUTH_MISSING_OR_INVALID")
    h=dict(plan["headers"])
    h["x-api-key"]=secret
    return h

def _map_http_status(r:HTTPResult,external:bool)->None:
    if r.status==200: return
    if r.status in {401,403}: raise LiveTransportError("AUTH_ERROR",http_status=r.status,external_network_used=external)
    if r.status==429: raise LiveTransportError("RATE_LIMITED",http_status=429,retriable=True,external_network_used=external)
    if r.status>=500: raise LiveTransportError("PROVIDER_HTTP_ERROR",http_status=r.status,retriable=True,external_network_used=external)
    raise LiveTransportError("PROVIDER_HTTP_ERROR",http_status=r.status,external_network_used=external)

def _success(plan:Mapping[str,Any],r:HTTPResult,external:bool)->dict[str,Any]:
    try:
        parsed=parse_success_response(r.body)
    except AdapterError as e:
        raise LiveTransportError(e.code,http_status=e.http_status,retriable=e.retriable,external_network_used=external) from None
    response_hash=sha256_json(r.body)
    cost=estimate_cost(parsed["usage"])
    prov={
        "provider":PROVIDER,"model":MODEL,"anthropic_version":ANTHROPIC_VERSION,
        "transport_version":TRANSPORT_VERSION,"request_hash":plan["request_hash"],"response_hash":response_hash,
        "input_tokens":parsed["usage"]["input_tokens"],"output_tokens":parsed["usage"]["output_tokens"],
        "data_class":DATA_CLASS,"credential_source":CREDENTIAL_ENV,"credential_value_recorded":False,
        "external_network_used":external,"automatic_retry_used":False,"fallback_used":False,
        "tools_used":False,"search_used":False,"files_used":False,"caching_used":False,
        "mcp_used":False,"managed_agents_used":False,"code_execution_used":False,
        "project_mutation_performed":False,"production":False,
    }
    result={"parsed_response":parsed,"cost_estimate":cost,"provenance":prov,"provenance_hash":sha256_json(prov)}
    result["result_identity"]=sha256_json(result)
    return result

class AnthropicLiveTransport:
    def __init__(self,executor:HTTPExecutor,secret_reader:SecretReader):
        self.executor=executor
        self.secret_reader=secret_reader
        self.external_network_used=False

    def _send_once(self,plan:Mapping[str,Any],*,timeout:float,external:bool)->dict[str,Any]:
        validate_blueprint(plan)
        timeout=validate_timeout(timeout)
        secret=self.secret_reader.read(CREDENTIAL_ENV)
        headers=_authorized_headers(plan,secret)
        body=canonical_json(plan["body"]).encode("utf-8")
        if external:
            self.external_network_used=True
        try:
            r=self.executor.request(method="POST",url=ENDPOINT,headers=headers,body=body,timeout=timeout)
        except LiveTransportError as e:
            if external and not e.external_network_used:
                raise LiveTransportError(e.code,http_status=e.http_status,retriable=e.retriable,external_network_used=True) from None
            raise
        except (TimeoutError,socket.timeout):
            raise LiveTransportError("NETWORK_TIMEOUT",retriable=True,external_network_used=external) from None
        except Exception:
            raise LiveTransportError("NETWORK_ERROR",retriable=True,external_network_used=external) from None
        _map_http_status(r,external)
        return _success(plan,r,external)

    def run_test_injected(self,plan:Mapping[str,Any],*,timeout:float=DEFAULT_TIMEOUT_SECONDS)->dict[str,Any]:
        if getattr(self.executor,"external_network_capable",None) is not False or not isinstance(self.secret_reader,InjectedSecretReader):
            raise LiveTransportError("TEST_PATH_REQUIRES_INJECTED_NONNETWORK_DEPENDENCIES")
        return self._send_once(plan,timeout=timeout,external=False)

    def run_live(self,plan:Mapping[str,Any],*,live_switch:str|None,timeout:float=DEFAULT_TIMEOUT_SECONDS)->dict[str,Any]:
        validate_blueprint(plan)
        require_live_switch(live_switch)
        if type(self.executor) is not UrllibExecutor or type(self.secret_reader) is not EnvironmentSecretReader:
            raise LiveTransportError("LIVE_PATH_REQUIRES_REAL_NETWORK_EXECUTOR_AND_ENV_SECRET_READER")
        return self._send_once(plan,timeout=timeout,external=True)
