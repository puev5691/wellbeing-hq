#!/usr/bin/env python3
"""Anthropic Messages: ограниченный кандидат без сети и секретов.

Локальный запуск: python3 -B anthropic-provider-compatible-adapter-r01.py --self-test
Рядом требуется точный orchestrator-mvp-r01.py; его Git blob проверяется.
Это преобразование Messages API и тестовый исполнитель, не live-клиент.
Модели/соответствия alias передаются явно; тестовые привязки не доказывают entitlement.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict, fields, field
from pathlib import Path
from types import ModuleType
from typing import Any
import argparse
import hashlib
import json
import re
import sys

MVP_BLOB = "55939b2e4c91f7af1159a60b2f4ee8fa961196f2"
TASK_PATH = "entities/koordinator/outbox/KOO__anthropic-provider-compatible-adapter-r01__KOD.md"
TASK_COMMIT = "03cb2846136eb3a450b832502dbf244cf2330785"
TASK_BLOB = "23beaad41fcc79f2516d2f3894046a971d453d9f"
WRITER_BLOB = "bfeff738de2759248307dd52433c77139624fb54"
PASS = "PASS_ANTHROPIC_PROVIDER_COMPATIBLE_ADAPTER_R01_READY_FOR_INDEPENDENT_VERIFY"
ENDPOINT = "https://api.anthropic.com/v1/messages"
VERSION = "2023-06-01"
D0_TEXT = "Synthetic bounded request."
RUN_ID = "run-anthropic-contract-r01"
# Локальные ограничения кандидата, не лимиты провайдера.
MAX_BODY = 65536
MAX_TEXT = 16384
STOP_KINDS = {
    "end_turn": "normal",
    "tool_use": "unsupported_tool",
    "max_tokens": "incomplete_tokens",
    "model_context_window_exceeded": "incomplete_context",
    "pause_turn": "interrupted",
    "refusal": "refusal",
    "stop_sequence": "unadmitted_sequence",
}
ERRORS = {
    400:"invalid_request_error", 401:"authentication_error", 402:"billing_error",
    403:"permission_error", 404:"not_found_error", 409:"conflict_error",
    413:"request_too_large", 429:"rate_limit_error", 500:"api_error",
    504:"timeout_error", 529:"overloaded_error",
}

def load_mvp(path: Path) -> ModuleType:
    data = path.read_bytes()
    actual = hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    if actual != MVP_BLOB:
        raise RuntimeError("mvp_blob_mismatch")
    mod = ModuleType("_anthropic_provider_pinned_mvp")
    mod.__file__ = str(path)
    sys.modules[mod.__name__] = mod
    exec(compile(data, str(path), "exec"), mod.__dict__)
    return mod

def identifier(value: Any) -> bool:
    return type(value) is str and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}", value) is not None

@dataclass(frozen=True)
class ModelBinding:
    requested: str
    returned: tuple[str, ...]
    # Обязательное происхождение конфигурации, не автоматическое признание её истинной.
    evidence: str
    fixture_only: bool

@dataclass(frozen=True)
class AuthReference:
    kind: str                   # api_key_bearer | api_key_legacy | wif_bearer
    secret_ref: str = field(repr=False)
    multi_workspace: bool = False
    workspace: str | None = None

@dataclass(frozen=True)
class RequestPlan:
    method: str
    url: str
    headers: tuple[tuple[str, str], ...]
    body: bytes = field(repr=False)
    auth_header: str
    auth_prefix: str
    auth_reference: str = field(repr=False)
    credential_resolved: bool = False

@dataclass(frozen=True)
class HTTPReply:
    status: int
    payload: bytes = field(repr=False)
    headers: tuple[tuple[str, str], ...] = ()
    provider: str = "anthropic"
    endpoint: str = ENDPOINT

class Sentinel:
    """Только возвращает заданный ответ. Не содержит сетевого транспорта."""
    def __init__(self, reply: HTTPReply | None):
        self.reply = reply
        self.calls = 0

    def send(self, plan: RequestPlan) -> HTTPReply:
        self.calls += 1
        if self.reply is None:
            raise RuntimeError("untrusted_executor_diagnostic")
        return self.reply

def stop_details(body: dict) -> dict:
    if "stop_reason" not in body:
        return {"stop_kind":"missing", "stop_reason":None}
    value = body["stop_reason"]
    if value is None:
        return {"stop_kind":"null", "stop_reason":None}
    if type(value) is not str:
        return {"stop_kind":"malformed", "stop_reason":None}
    if value in STOP_KINDS:
        return {"stop_kind":STOP_KINDS[value], "stop_reason":value}
    # Не выводить произвольный текст поля в журналы.
    return {"stop_kind":"unknown", "stop_reason":None,
            "stop_value_sha256":hashlib.sha256(value.encode()).hexdigest()}

def strict_json(payload: bytes) -> Any:
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate_json_key")
            result[key] = value
        return result
    def nonfinite(_):
        raise ValueError("nonfinite_json")
    result = json.loads(payload.decode("utf-8"), object_pairs_hook=pairs, parse_constant=nonfinite)
    # JSON escape не должен протащить одиночный Unicode surrogate в диагностику.
    json.dumps(result, ensure_ascii=False, allow_nan=False).encode("utf-8")
    return result

def build_runtime(mvp: ModuleType, bindings: tuple[ModelBinding, ...], auth: AuthReference):
    """Сохраняет исходные конверты, Router, состояния и terminal/routing boundary."""
    def deny(code="BLOCKED_UNSUPPORTED_CAPABILITY"):
        raise mvp.Blocked(code)

    if type(bindings) is not tuple or not bindings:
        deny("BLOCKED_MODEL_UNAVAILABLE")
    for b in bindings:
        if (type(b) is not ModelBinding or not identifier(b.requested) or
            type(b.returned) is not tuple or not b.returned or
            any(not identifier(x) for x in b.returned) or
            len(set(b.returned)) != len(b.returned) or not identifier(b.evidence) or
            type(b.fixture_only) is not bool):
            deny("BLOCKED_MODEL_UNAVAILABLE")
    table = {b.requested:b for b in bindings}
    if len(table) != len(bindings):
        deny("BLOCKED_MODEL_UNAVAILABLE")
    if (type(auth) is not AuthReference or
        auth.kind not in ("api_key_bearer","api_key_legacy","wif_bearer") or
        type(auth.secret_ref) is not str or
        re.fullmatch(r"secretref:anthropic:[A-Za-z0-9_.-]{1,64}", auth.secret_ref) is None or
        type(auth.multi_workspace) is not bool or
        (auth.workspace is not None and not identifier(auth.workspace)) or
        (auth.kind == "wif_bearer" and (auth.workspace is not None or auth.multi_workspace)) or
        (auth.multi_workspace and auth.workspace is None)):
        deny()
    task_identity = mvp.TaskIdentity(TASK_PATH,TASK_COMMIT,TASK_BLOB)
    field_names = {f.name for f in fields(mvp.RequestEnvelope)}

    def validate(req):
        if type(req) is not mvp.RequestEnvelope or set(vars(req)) != field_names:
            deny()
        if req.entity != "KOD": deny("BLOCKED_WRONG_ENTITY")
        if req.writer_blob != WRITER_BLOB: deny("BLOCKED_WRONG_WRITER")
        if type(req.task) is not mvp.TaskIdentity or req.task != task_identity:
            deny("BLOCKED_TASK_IDENTITY_MISMATCH")
        if req.run_id != RUN_ID or req.task_class != "coding": deny()
        if type(req.provider) is not str or req.provider != "anthropic":
            deny("BLOCKED_PROVIDER_UNREGISTERED")
        if type(req.model) is not str or req.model not in table:
            deny("BLOCKED_MODEL_UNAVAILABLE")
        if (req.data_class != "synthetic" or type(req.content) is not str or
            req.content != D0_TEXT or req.external_send_allowed is not False):
            deny("BLOCKED_PRIVACY_BOUNDARY")
        if type(req.tools_allowed) is not list or req.tools_allowed != []:
            deny("BLOCKED_TOOL_AUTHORITY")
        if type(req.capabilities_required) is not list or req.capabilities_required != ["text"]:
            deny()
        if type(req.reasoning) is not str or req.reasoning not in ("LOW","MEDIUM","HIGH"):
            deny("BLOCKED_REASONING_UNSUPPORTED")
        if type(req.reasoning_mandatory) is not bool or req.reasoning_mandatory:
            deny("BLOCKED_REASONING_UNSUPPORTED")

    def request_plan(req, max_tokens=256):
        validate(req)
        if type(max_tokens) is not int or not 1 <= max_tokens <= 1024:
            deny()
        headers = [("anthropic-version",VERSION),("content-type","application/json")]
        if auth.workspace is not None:
            headers.append(("anthropic-workspace-id",auth.workspace))
        payload = json.dumps({"model":req.model,"max_tokens":max_tokens,
                              "messages":[{"role":"user","content":req.content}]},
                             ensure_ascii=False,separators=(",",":")).encode()
        if len(payload) > MAX_BODY: deny()
        legacy = auth.kind == "api_key_legacy"
        return RequestPlan("POST",ENDPOINT,tuple(headers),payload,
                           "x-api-key" if legacy else "Authorization",
                           "" if legacy else "Bearer ",auth.secret_ref)

    def response(req, reply, max_tokens):
        state = {"mode":"injected_no_network", "requested_model":req.model,
                 "returned_model":None, "model_binding_evidence":table[req.model].evidence,
                 "fixture_only":table[req.model].fixture_only,
                 "model_entitlement_verified":False, "credentials_resolved":False,
                 "retry_count":0, "http_status":None}
        def blocked(diagnostic, code="BLOCKED_UNSUPPORTED_CAPABILITY"):
            return mvp.ResponseEnvelope(RUN_ID,"anthropic",req.model,"blocked",code,
                                        provider_state={**state,"diagnostic":diagnostic})
        if (type(reply) is not HTTPReply or type(reply.status) is not int or
            not 100 <= reply.status <= 599 or type(reply.payload) is not bytes or
            len(reply.payload)>MAX_BODY or type(reply.headers) is not tuple):
            return blocked("transport_shape")
        state["http_status"] = reply.status
        if reply.provider != "anthropic" or reply.endpoint != ENDPOINT:
            return blocked("response_origin","BLOCKED_PROVIDER_UNAVAILABLE")
        headers = {}
        for pair in reply.headers:
            if (type(pair) is not tuple or len(pair)!=2 or
                type(pair[0]) is not str or type(pair[1]) is not str or
                len(pair[0])>128 or len(pair[1])>512 or
                pair[0].lower() in headers):
                return blocked("header_shape")
            headers[pair[0].lower()] = pair[1]
        request_id = headers.get("request-id")
        state["request_id"] = request_id if identifier(request_id) else None
        # RED документирует наличие retry-after, но не полный формат rate-limit headers.
        retry = headers.get("retry-after")
        state["retry_after_raw"] = retry if type(retry) is str and re.fullmatch(r"[0-9]{1,8}",retry) else None
        if headers.get("content-type","").split(";",1)[0].strip().lower() == "text/event-stream":
            return blocked("streaming_unsupported")
        try:
            body = strict_json(reply.payload)
        except (ValueError,UnicodeError,RecursionError):
            return blocked("json_schema")
        if type(body) is not dict:
            return blocked("message_schema")
        if reply.status != 200:
            err = body.get("error")
            state["error_type"] = None
            body_request_id = body.get("request_id")
            state["body_request_id"] = body_request_id if identifier(body_request_id) else None
            if (body.get("type")=="error" and type(err) is dict and
                type(err.get("message")) is str and type(err.get("type")) is str and
                reply.status in ERRORS and err["type"]==ERRORS[reply.status]):
                state["error_type"] = err["type"]
                return blocked("provider_error","BLOCKED_PROVIDER_UNAVAILABLE")
            return blocked("provider_error_schema","BLOCKED_PROVIDER_UNAVAILABLE")
        state.update(stop_details(body))
        if (body.get("type")!="message" or body.get("role")!="assistant" or
            not identifier(body.get("id")) or type(body.get("model")) is not str):
            return blocked("message_schema")
        returned = body["model"]
        if returned not in table[req.model].returned:
            state["returned_model_sha256"] = hashlib.sha256(returned.encode()).hexdigest()
            return blocked("response_model_mismatch","BLOCKED_MODEL_UNAVAILABLE")
        state["returned_model"] = returned
        state["message_id"] = body["id"]
        if state["stop_kind"] != "normal":
            return blocked("stop_reason_not_admitted",
                           "BLOCKED_TOOL_AUTHORITY" if state["stop_reason"]=="tool_use"
                           else "BLOCKED_UNSUPPORTED_CAPABILITY")
        if "stop_sequence" not in body or body["stop_sequence"] is not None:
            return blocked("stop_sequence_shape")
        content = body.get("content")
        if type(content) is not list or not 1 <= len(content) <= 16:
            return blocked("content_shape")
        texts = []
        for block in content:
            if type(block) is not dict or type(block.get("type")) is not str:
                return blocked("content_shape")
            if block["type"] != "text":
                state["content_type_sha256"] = hashlib.sha256(block["type"].encode()).hexdigest()
                return blocked("content_type_unsupported",
                               "BLOCKED_TOOL_AUTHORITY" if block["type"]=="tool_use"
                               else "BLOCKED_UNSUPPORTED_CAPABILITY")
            if type(block.get("text")) is not str:
                return blocked("text_shape")
            texts.append(block["text"])
        text = "".join(texts)
        try:
            valid_text = bool(text.strip()) and len(text.encode()) <= MAX_TEXT
        except UnicodeError:
            valid_text = False
        if not valid_text: return blocked("empty_or_oversized_text")
        usage = body.get("usage")
        if (type(usage) is not dict or
            any(type(usage.get(k)) is not int or not 0 <= usage[k] <= 10**9
                for k in ("input_tokens","output_tokens"))):
            return blocked("usage_shape")
        if usage["output_tokens"] > max_tokens:
            return blocked("output_usage_exceeds_request")
        state["usage_total_origin"] = "local_sum_input_output_not_provider_field"
        parsed_usage = {"input_tokens":usage["input_tokens"],"output_tokens":usage["output_tokens"],
                        "total_tokens":usage["input_tokens"]+usage["output_tokens"]}
        return mvp.ResponseEnvelope(RUN_ID,"anthropic",returned,"completed",PASS,
                                    output=text,usage=parsed_usage,provider_state=state)

    class Adapter(mvp.ProviderAdapter):
        provider_id = "anthropic"
        caps = mvp.AdapterCapabilities(frozenset(table),frozenset({"text"}),True,{})
        def __init__(self, sentinel, max_tokens=256, mode="dry_run"):
            if mode != "dry_run": deny("BLOCKED_LIVE_AUTHORITY_REQUIRED")
            if type(sentinel) is not Sentinel: deny()
            if type(max_tokens) is not int or not 1 <= max_tokens <= 1024: deny()
            self.sentinel, self.max_tokens = sentinel,max_tokens
        def fake_invoke(self, req):
            plan = request_plan(req,self.max_tokens)
            try:
                reply = self.sentinel.send(plan)
            except Exception:
                return mvp.ResponseEnvelope(RUN_ID,"anthropic",req.model,"blocked",
                    "BLOCKED_PROVIDER_UNAVAILABLE",provider_state={"diagnostic":"transport_error","retry_count":0})
            return response(req,reply,self.max_tokens)

    class Admission:
        def admit(self, req): validate(req)

    class Orch(mvp.Orchestrator):
        def __init__(self, sentinel, max_tokens=256, mode="dry_run"):
            self.anthropic = Adapter(sentinel,max_tokens,mode)
            self.registry = mvp.AdapterRegistry([self.anthropic])
            self.router, self.admission = mvp.Router(self.registry),Admission()
        def run(self, req):
            # Базовый MVP создаёт телеметрию до admission: сперва отсечь произвольные metadata.
            try:
                validate(req)
            except mvp.Blocked as exc:
                model = req.model if type(req) is mvp.RequestEnvelope and type(req.model) is str and req.model in table else None
                resp = mvp.ResponseEnvelope(RUN_ID,"anthropic",model,"blocked",str(exc))
                run = mvp.RunState(cycle_state="TERMINAL_RESULT",terminal_status=str(exc))
                tel = mvp.Telemetry(RUN_ID,"KOD",provider="anthropic",model=model,result=str(exc))
                return resp,run,mvp.RoutingState(),tel
            return super().run(req)

    def request(model, **changes):
        req = mvp.RequestEnvelope(RUN_ID,"KOD",WRITER_BLOB,task_identity,"coding",D0_TEXT,
                                  provider="anthropic",model=model)
        for key,value in changes.items():
            if key not in field_names: deny()
            setattr(req,key,value)
        return req
    return Orch,request,request_plan

def self_test(mvp):
    import copy
    fixture_model = "synthetic-model-for-contract-test"
    bindings = (ModelBinding(fixture_model,(fixture_model,),"fixture-only-not-entitlement",True),)
    auth = AuthReference("api_key_bearer","secretref:anthropic:unresolved")
    Orch,request,plan = build_runtime(mvp,bindings,auth)
    base = {"id":"msg_synthetic_success_r01","type":"message","role":"assistant",
            "model":fixture_model,"content":[{"type":"text","text":"Synthetic bounded response."}],
            "stop_reason":"end_turn","stop_sequence":None,
            "usage":{"input_tokens":10,"output_tokens":4}}
    checks = []
    def check(name, condition):
        if not condition: raise AssertionError(name)
        checks.append(name)
    def run(body=None,status=200,headers=(),**reply_changes):
        payload = json.dumps(base if body is None else body).encode()
        sent = Sentinel(HTTPReply(status,payload,headers,**reply_changes))
        result = Orch(sent).run(request(fixture_model))
        check("one_attempt",sent.calls==1)
        check("terminal_not_routing",not result[1].in_execution_wip and not result[2].complete)
        return result
    r,_,_,tel=run()
    check("native_envelopes",type(r) is mvp.ResponseEnvelope and type(request(fixture_model)) is mvp.RequestEnvelope)
    check("success_end_turn",r.status=="completed" and r.terminal_status==PASS and r.output=="Synthetic bounded response.")
    check("usage_derived",r.usage=={"input_tokens":10,"output_tokens":4,"total_tokens":14})
    check("reasoning_not_native",r.reasoning["applied"]=="omitted_unsupported" and r.reasoning["provider_native"] is None)
    check("no_invented_metrics",tel.estimated_cost is None and all(v is None for v in tel.latency.values()))
    p=plan(request(fixture_model))
    check("exact_request",p.method=="POST" and p.url==ENDPOINT and json.loads(p.body)=={
        "model":fixture_model,"max_tokens":256,"messages":[{"role":"user","content":D0_TEXT}]})
    check("headers_auth_unresolved",dict(p.headers)=={"anthropic-version":VERSION,"content-type":"application/json"}
          and p.auth_header=="Authorization" and p.auth_prefix=="Bearer " and not p.credential_resolved)
    check("plan_repr_redacted",D0_TEXT not in repr(p) and "secretref:" not in repr(p) and "secretref:" not in repr(auth))
    for kind, header, prefix in [("api_key_legacy","x-api-key",""),("wif_bearer","Authorization","Bearer ")]:
        _,_,make=build_runtime(mvp,bindings,AuthReference(kind,"secretref:anthropic:unresolved"))
        q=make(request(fixture_model));check("auth:"+kind,q.auth_header==header and q.auth_prefix==prefix)
    _,_,make=build_runtime(mvp,bindings,AuthReference("api_key_legacy","secretref:anthropic:unresolved",True,"workspace-fixture"))
    check("workspace_header",dict(make(request(fixture_model)).headers)["anthropic-workspace-id"]=="workspace-fixture")
    for a in [AuthReference("api_key_bearer","secretref:anthropic:unresolved",True),
              AuthReference("wif_bearer","secretref:anthropic:unresolved",False,"workspace-fixture"),
              AuthReference("api_key_bearer","not-a-secret-reference")]:
        try: build_runtime(mvp,bindings,a)
        except mvp.Blocked: check("auth_rejection",True)
        else: raise AssertionError("auth_rejection")
    for reason in [*STOP_KINDS,None,"future_stop",7,[],{}]:
        if reason=="end_turn": continue
        b=copy.deepcopy(base);b["stop_reason"]=reason
        r,*_=run(b)
        check("stop_closed:"+str(reason),r.status=="blocked" and r.output=="")
        check("stop_distinction:"+str(reason),r.provider_state["stop_kind"]==stop_details(b)["stop_kind"])
    b=copy.deepcopy(base);del b["stop_reason"]
    r,*_=run(b);check("missing_stop",r.provider_state["stop_kind"]=="missing" and r.status=="blocked")
    for content in [[],[{"type":"text","text":""}],[{"type":"text","text":"  "}],
                    [{"type":"tool_use","id":"tool_fixture","name":"forbidden","input":{}}],
                    [{"type":"thinking","thinking":"ignored"}],[{"type":"future_block"}],
                    [{"type":"text","text":False}],[{"text":"missing_type"}],
                    [{"type":"text","text":"valid"},{"type":"tool_use"}],
                    [{"type":"text","text":"x"*(MAX_TEXT+1)}]]:
        b=copy.deepcopy(base);b["content"]=content
        r,*_=run(b);check("content_fail_closed",r.status=="blocked" and not r.output)
    for fieldname,value in [("type","error"),("role","user"),("id",None),("model","untrusted_model"),
                            ("usage",{}),("usage",{"input_tokens":True,"output_tokens":4}),
                            ("usage",{"input_tokens":-1,"output_tokens":4}),
                            ("usage",{"input_tokens":1,"output_tokens":257}),
                            ("stop_sequence","unexpected")]:
        b=copy.deepcopy(base);b[fieldname]=value
        r,*_=run(b);check("schema:"+fieldname,r.status=="blocked")
    b=copy.deepcopy(base);b["optional_future_field"]={"ignored":True};b["usage"]["total_tokens"]=999
    r,*_=run(b);check("ignore_optional_not_invented_usage",r.status=="completed" and r.usage["total_tokens"]==14)
    b=copy.deepcopy(base);b["content"]=[{"type":"text","text":"one"},{"type":"text","text":"two"}]
    r,*_=run(b);check("text_blocks_concatenate",r.output=="onetwo")
    alias_bindings=(ModelBinding("request-alias-fixture",(fixture_model,),"explicit-alias-fixture-not-entitlement",True),)
    A,Q,_=build_runtime(mvp,alias_bindings,auth)
    s=Sentinel(HTTPReply(200,json.dumps(base).encode()));r,_,_,t=A(s).run(Q("request-alias-fixture"))
    check("explicit_alias_binding",r.status=="completed" and r.model==fixture_model and t.model=="request-alias-fixture"
          and r.provider_state["requested_model"]=="request-alias-fixture" and not r.provider_state["model_entitlement_verified"])
    for status,err_type in ERRORS.items():
        body={"type":"error","error":{"type":err_type,"message":"UNTRUSTED_PRIVATE_DIAGNOSTIC"},"request_id":"req_fixture"}
        r,_,_,t=run(body,status,(("retry-after","2"),("request-id","req_header")))
        check("error:"+err_type,r.status=="blocked" and r.provider_state["error_type"]==err_type
              and r.provider_state["retry_after_raw"]=="2" and t.retries==0)
        check("error_message_redacted","UNTRUSTED_PRIVATE_DIAGNOSTIC" not in json.dumps(asdict(r)))
    r,*_=run({"type":"error","error":{"type":"rate_limit_error","message":"x"}},429)
    check("429_without_retry_after",r.status=="blocked" and r.provider_state["retry_after_raw"] is None)
    for reply_changes in [{"provider":"openai"},{"endpoint":"https://wrong.invalid/v1/messages"}]:
        r,*_=run(**reply_changes);check("origin_validation",r.status=="blocked")
    r,*_=run(headers=(("content-type","text/event-stream"),))
    check("sse_not_success",r.status=="blocked")
    for raw in [b"not json",b"[]",b'{"type":"message","type":"error"}',b'{"x":NaN}',
                b"\xff",b" "*(MAX_BODY+1)]:
        s=Sentinel(HTTPReply(200,raw));r,*_=Orch(s).run(request(fixture_model))
        check("malformed_json",r.status=="blocked" and s.calls==1)
    negative = [("model","unknown"),("model",[]),("provider","openai"),("provider","google"),
                ("tools_allowed",["shell"]),("capabilities_required",["stream"]),
                ("capabilities_required",["thinking"]),("reasoning_mandatory",True),
                ("data_class","project_internal"),("content","UNTRUSTED_PRIVATE_DIAGNOSTIC"),
                ("external_send_allowed",True),("writer_blob","old"),("task",None),("entity","OTHER")]
    for key,value in negative:
        q=request(fixture_model);setattr(q,key,value);s=Sentinel(HTTPReply(200,json.dumps(base).encode()))
        r,_,_,t=Orch(s).run(q)
        check("pretransport:"+key,r.status=="blocked" and s.calls==0)
        check("redaction:"+key,"UNTRUSTED_PRIVATE_DIAGNOSTIC" not in json.dumps([asdict(r),asdict(t)]))
    for q in [None,{},request(fixture_model)]:
        if type(q) is mvp.RequestEnvelope: q.extra_field=True
        s=Sentinel(None);r,*_=Orch(s).run(q);check("bad_envelope",r.status=="blocked" and s.calls==0)
    for number in [0,-1,True,1025,"256"]:
        try: plan(request(fixture_model),number)
        except mvp.Blocked: check("token_bound",True)
        else: raise AssertionError("token_bound")
    for kwargs in [{"mode":"live"},{"sentinel":object()}]:
        try: Orch(**({"sentinel":Sentinel(None)}|kwargs))
        except mvp.Blocked: check("live_and_transport_closed",True)
        else: raise AssertionError("live_and_transport_closed")
    s=Sentinel(None);r,*_=Orch(s).run(request(fixture_model))
    check("executor_error_redacted",s.calls==1 and r.status=="blocked" and "untrusted_executor_diagnostic" not in json.dumps(asdict(r)))
    try: request()
    except TypeError: check("model_required",True)
    else: raise AssertionError("model_required")
    for provider in ("openai","google"):
        try: Orch(Sentinel(None)).registry.get(provider)
        except mvp.Blocked: check("no_fallback_registry",True)
        else: raise AssertionError("no_fallback_registry")
    return {"verdict":PASS,"assertions":len(checks),"checks":checks,
            "stop_reason_cases":[*STOP_KINDS,"missing","null","malformed","unknown"],
            "provider_api_calls":0,"credential_reads":0,"entitlement_verified":False,
            "tested_model_ids":"RED synthetic fixture plus explicit alias fixture only",
            "public_statuses":"existing completed/blocked + native BLOCKED_*; task-defined PASS",
            "independent_review":"pending"}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test",action="store_true")
    parser.add_argument("--mvp",type=Path,default=Path(__file__).with_name("orchestrator-mvp-r01.py"))
    args=parser.parse_args()
    if not args.self_test:
        parser.print_help()
        return
    print(json.dumps(self_test(load_mvp(args.mvp)),ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
