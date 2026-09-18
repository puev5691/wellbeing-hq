#!/usr/bin/env python3
"""Запускать локально под обычным пользователем, Python 3.10+, без сети/секретов.
Entity Resource Gateway r0.1: библиотека, не сервис и не исполнитель решений.
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict, fields
from pathlib import Path
from types import ModuleType
from typing import Callable
import builtins
import hashlib
import json
import re
import sys

VERSION = "entity-resource-gateway-r01"
PASS = "PASS_ENTITY_RESOURCE_GATEWAY_MVP_R01_READY_FOR_INDEPENDENT_VERIFY"
D0_TEXT = "Synthetic bounded request."
D0_SHA256 = hashlib.sha256(D0_TEXT.encode()).hexdigest()
MAX_REQUEST_BYTES = 16384
MAX_REPLY_BYTES = 65536
PINS = {
    "orchestrator-mvp-r01.py": "55939b2e4c91f7af1159a60b2f4ee8fa961196f2",
    "policy.py": "f04676995d63e6e5eadb9474aaf2d15e5153ab43",
    "openai_adapter.py": "47c2c2e8bd361a2dafad3e66457c95de9a11d5e0",
    "anthropic-provider-compatible-adapter-r01.py": "985746909772900d9c72257dc53478aa34861d91",
}
ANTHROPIC_MODEL = "synthetic-model-for-contract-test"
PROVIDERS = frozenset({"openai", "anthropic"})

class GatewayError(ValueError):
    """Исключения содержат только фиксированный код, без входного текста."""

def require(ok, code="BLOCKED_REQUEST_SCHEMA"):
    if not ok:
        raise GatewayError(code)

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def atom(value):
    return type(value) is str and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}", value) is not None

def hexhash(value, length):
    return type(value) is str and re.fullmatch(r"[0-9a-f]{"+str(length)+"}", value) is not None

@dataclass(frozen=True)
class ArtifactRef:
    repository: str
    path: str
    commit: str
    blob: str

@dataclass(frozen=True)
class Requester:
    entity_id: str
    role: str
    task: ArtifactRef
    writer: ArtifactRef

@dataclass(frozen=True)
class SourceRef:
    locator: str
    sha256: str
    data_class: str = "D0_SYNTHETIC"

@dataclass(frozen=True)
class AcceptancePolicy:
    policy_id: str = "bounded_text_then_requester_review"
    max_output_bytes: int = 4096
    expected_output_sha256: str | None = None
    project_acceptance: str = field(default="NOT_GRANTED", init=False)

@dataclass(frozen=True)
class EntityRequest:
    request_id: str
    requester: Requester
    purpose: str = field(repr=False)
    provider: str
    model: str
    data_class: str
    privacy_class: str
    capabilities: tuple[str, ...]
    tools: tuple[str, ...]
    external_send_allowed: bool
    sources: tuple[SourceRef, ...]
    payload: str = field(repr=False)
    acceptance: AcceptancePolicy
    max_output_tokens: int = 64
    @property
    def identity(self):
        return sha(canonical(asdict(self)))

@dataclass(frozen=True)
class ReplayResponse:
    """Входные тестовые байты, связанные с точным запросом; не сетевой callback."""
    request_sha256: str
    provider: str
    http_status: int
    payload: bytes = field(repr=False)

@dataclass(frozen=True)
class ResourceResult:
    request_id: str
    request_sha256: str
    requester: Requester
    run_id: str
    requested_provider: str
    requested_model: str
    provider_used: str | None
    model_used: str | None
    technical_status: str
    terminal_status: str
    blocker: str | None
    payload: str = field(repr=False)
    usage: tuple[tuple[str, int], ...]
    usage_origin: str | None
    provenance: tuple[tuple[str, str], ...]
    sources: tuple[SourceRef, ...]
    transport_calls: int
    data_class: str = field(default="D0_SYNTHETIC", init=False)
    privacy_class: str = field(default="synthetic_only", init=False)
    execution_mode: str = field(default="synthetic_no_network", init=False)
    project_acceptance: str = field(default="NOT_GRANTED", init=False)
    caller_writer_changed: bool = field(default=False, init=False)
    gateway_writer_authority: bool = field(default=False, init=False)
    provider_writer_authority: bool = field(default=False, init=False)
    project_state_applied: bool = field(default=False, init=False)
    external_dispatch_performed: bool = field(default=False, init=False)
    routing_status: str = field(default="not_started", init=False)
    @property
    def identity(self):
        return sha(canonical(asdict(self)))
    def to_bytes(self):
        return canonical({"resource_result": asdict(self), "result_sha256": self.identity})

def validate_ref(value):
    require(type(value) is ArtifactRef)
    require(type(value.repository) is str and
            re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", value.repository) is not None)
    require(type(value.path) is str and 0 < len(value.path) <= 256 and
            re.fullmatch(r"[A-Za-z0-9_./-]+", value.path) is not None and
            all(p not in ("", ".", "..") for p in value.path.split("/")))
    require(hexhash(value.commit,40) and hexhash(value.blob,40))

def validate_request(req):
    """Проверка формы. Некорректную форму нельзя безопасно коррелировать."""
    require(type(req) is EntityRequest and set(vars(req)) == {f.name for f in fields(EntityRequest)})
    require(atom(req.request_id) and type(req.requester) is Requester)
    require(atom(req.requester.entity_id) and atom(req.requester.role))
    validate_ref(req.requester.task)
    validate_ref(req.requester.writer)
    require(type(req.purpose) is str and bool(req.purpose.strip()) and len(req.purpose.encode()) <= 512)
    require(atom(req.provider) and atom(req.model))
    require(type(req.data_class) is str and len(req.data_class)<=64 and
            type(req.privacy_class) is str and len(req.privacy_class)<=64)
    require(type(req.payload) is str and len(req.payload.encode())<=8192,"BLOCKED_REQUEST_SIZE")
    require(type(req.capabilities) is tuple and len(req.capabilities)<=8 and
            all(atom(c) for c in req.capabilities))
    require(type(req.tools) is tuple and len(req.tools)<=8 and all(atom(t) for t in req.tools))
    require(type(req.external_send_allowed) is bool)
    require(type(req.sources) is tuple and 1 <= len(req.sources) <= 8)
    for source in req.sources:
        require(type(source) is SourceRef and type(source.locator) is str and
                re.fullmatch(r"fixture://[A-Za-z0-9_/-]{1,128}",source.locator) is not None)
        require(hexhash(source.sha256,64) and atom(source.data_class))
    require(len(set(req.sources)) == len(req.sources))
    a=req.acceptance
    require(type(a) is AcceptancePolicy and atom(a.policy_id) and a.project_acceptance=="NOT_GRANTED")
    require(type(a.max_output_bytes) is int and 1 <= a.max_output_bytes <= 16384)
    require(a.expected_output_sha256 is None or hexhash(a.expected_output_sha256,64))
    require(type(req.max_output_tokens) is int and 1 <= req.max_output_tokens <= 1024)
    require(len(canonical(asdict(req))) <= MAX_REQUEST_BYTES, "BLOCKED_REQUEST_SIZE")

def check_policy(req):
    require(req.data_class == "D0_SYNTHETIC" and req.privacy_class == "synthetic_only",
            "BLOCKED_PRIVACY_BOUNDARY")
    require(req.payload == D0_TEXT, "BLOCKED_SYNTHETIC_PAYLOAD")
    require(req.capabilities == ("text",), "BLOCKED_UNSUPPORTED_CAPABILITY")
    require(not req.tools, "BLOCKED_TOOL_AUTHORITY")
    require(req.external_send_allowed is False, "BLOCKED_EXTERNAL_SEND")
    require(all(s.sha256==D0_SHA256 and s.data_class=="D0_SYNTHETIC" for s in req.sources),
            "BLOCKED_SOURCE_IDENTITY")
    require(req.acceptance.policy_id=="bounded_text_then_requester_review","BLOCKED_ACCEPTANCE_POLICY")

def load_dependencies(directory: Path):
    """Сначала проверить все байты. Никаких загрузок из сети или sys.path."""
    data={}
    try:
        for filename,expected in PINS.items():
            data[filename]=(directory/filename).read_bytes()
            require(blob(data[filename]) == expected, "BLOCKED_DEPENDENCY_IDENTITY")
    except OSError:
        raise GatewayError("BLOCKED_DEPENDENCY_UNAVAILABLE") from None
    modules={}
    for filename in PINS:
        name="_erg_r01_"+PINS[filename]
        mod=ModuleType(name);mod.__file__=str(directory/filename)
        sys.modules[name]=mod
        if filename == "openai_adapter.py":
            imported_policy=modules["policy.py"]
            def pinned_import(name,globals=None,locals=None,fromlist=(),level=0):
                if name == "policy" and level == 0:
                    return imported_policy
                return builtins.__import__(name,globals,locals,fromlist,level)
            mod.__dict__["__builtins__"]={**vars(builtins),"__import__":pinned_import}
        exec(compile(data[filename],mod.__file__,"exec"),mod.__dict__)
        modules[filename]=mod
    return modules

class Gateway:
    """Управляющий код передаёт verifier; по умолчанию полномочия отсутствуют."""
    def __init__(self, dependencies: Path, verifier: Callable[[EntityRequest],bool] | None = None,
                 *, unavailable: tuple[str,...] = ()):
        require(type(unavailable) is tuple and all(p in PROVIDERS for p in unavailable))
        self.modules=load_dependencies(dependencies)
        self.verifier=verifier
        self.unavailable=unavailable

    def run(self, req: EntityRequest, replay: ReplayResponse | None = None) -> ResourceResult:
        # Неверная схема не сериализуется и не передаётся стороннему verifier.
        try:
            validate_request(req)
        except (UnicodeError, TypeError, RecursionError):
            raise GatewayError("BLOCKED_REQUEST_SCHEMA") from None
        request_hash=req.identity
        run_id="run-"+request_hash[:32]
        mvp=self.modules["orchestrator-mvp-r01.py"]
        oa=self.modules["openai_adapter.py"]
        pol=self.modules["policy.py"]
        ant=self.modules["anthropic-provider-compatible-adapter-r01.py"]
        prov={"gateway_version":VERSION,"request_sha256":request_hash,
              "input_sha256":sha(req.payload.encode()),"execution_scope":"synthetic_fixture_only",
              "dependencies_sha256":sha(canonical(PINS)),
              "model_entitlement":"not_verified","caller_metadata_sent_to_provider":"false"}
        used_provider=None
        used_model=None
        calls=0
        usage_origin=None

        def result(status,terminal,payload="",usage=()):
            return ResourceResult(req.request_id,request_hash,req.requester,run_id,
                req.provider,req.model,used_provider,used_model,status,terminal,
                None if status=="completed" else terminal,payload,usage,usage_origin,
                tuple(sorted(prov.items())),req.sources,calls)

        try:
            check_policy(req)
        except GatewayError as exc:
            return result("blocked",str(exc))
        if not callable(self.verifier):
            return result("blocked","BLOCKED_REQUESTER_AUTHORITY")
        try:
            verified=self.verifier(req)
        except Exception:
            return result("blocked","BLOCKED_REQUESTER_AUTHORITY")
        if verified is not True:
            return result("blocked","BLOCKED_REQUESTER_AUTHORITY")
        # callback является доверенной границей, но контекст запроса всё же сверяется повторно.
        if req.identity != request_hash:
            return result("blocked","BLOCKED_REQUEST_CHANGED")

        original=mvp.RequestEnvelope(run_id,req.requester.entity_id,req.requester.writer.blob,
            mvp.TaskIdentity(req.requester.task.path,req.requester.task.commit,req.requester.task.blob),
            "resource",req.payload,provider=req.provider,model=req.model)

        def check_replay():
            nonlocal used_provider
            if replay is None:
                raise mvp.Blocked("BLOCKED_PROVIDER_UNAVAILABLE")
            if (type(replay) is not ReplayResponse or replay.request_sha256 != request_hash
                or replay.provider != req.provider or type(replay.http_status) is not int
                or not 100 <= replay.http_status <= 599 or type(replay.payload) is not bytes
                or len(replay.payload)>MAX_REPLY_BYTES):
                raise mvp.Blocked("BLOCKED_REPLAY_IDENTITY")
            prov["response_fixture_sha256"]=sha(replay.payload)
            try:
                body=ant.strict_json(replay.payload)
            except (ValueError,UnicodeError,RecursionError):
                raise mvp.Blocked("BLOCKED_RESPONSE_SCHEMA") from None
            if type(body) is not dict:
                raise mvp.Blocked("BLOCKED_RESPONSE_SCHEMA")
            used_provider=req.provider
            return body

        class Bridge(mvp.ProviderAdapter):
            def __init__(bridge,provider,models):
                bridge.provider_id=provider
                bridge.caps=mvp.AdapterCapabilities(frozenset(models),frozenset({"text"}),
                                                   provider not in self.unavailable,{})
            def fake_invoke(bridge,envelope):
                nonlocal calls,used_model,usage_origin
                body=check_replay()
                if bridge.provider_id=="openai":
                    config=pol.valid_synthetic_config(envelope.model,envelope.content)
                    config["max_output_tokens"]=req.max_output_tokens
                    transport=oa.MockTransport(oa.MockHTTPResponse(replay.http_status,body))
                    try:
                        native=oa.OpenAIResponsesAdapter().run_mock(config,transport)
                    except oa.AdapterError as exc:
                        code=("BLOCKED_MODEL_UNAVAILABLE" if exc.code=="RESPONSE_MODEL_MISMATCH"
                              else "BLOCKED_PROVIDER_UNAVAILABLE" if exc.http_status is not None
                              else "BLOCKED_RESPONSE_SCHEMA")
                        raise mvp.Blocked(code) from None
                    except pol.PolicyViolation:
                        raise mvp.Blocked("BLOCKED_PRIVACY_BOUNDARY") from None
                    finally:
                        calls=transport.calls
                    parsed=native["parsed_response"]
                    used_model=parsed["model"]
                    prov["adapter_result_sha256"]=native["result_identity"]
                    prov["adapter_request_sha256"]=native["provenance"]["request_hash"]
                    prov["adapter_input_sha256"]=native["provenance"]["synthetic_text_sha256"]
                    usage_origin="documented_openai_usage_fixture"
                    return mvp.ResponseEnvelope(run_id,"openai",used_model,"completed",
                        "PASS_RESOURCE_SYNTHETIC",output=parsed["text"],usage=parsed["usage"])
                binding=(ant.ModelBinding(ANTHROPIC_MODEL,(ANTHROPIC_MODEL,),
                                           "gateway-fixture-not-entitlement",True),)
                O,Q,make_plan=ant.build_runtime(mvp,binding,
                    ant.AuthReference("api_key_bearer","secretref:anthropic:unresolved"))
                inner_req=Q(envelope.model)
                # Не заменять произвольное содержимое фиксированным запросом молча.
                if inner_req.content != envelope.content:
                    raise mvp.Blocked("BLOCKED_SYNTHETIC_PAYLOAD")
                plan=make_plan(inner_req,req.max_output_tokens)
                prov["adapter_request_sha256"]=sha(plan.body)
                prov["adapter_input_sha256"]=sha(inner_req.content.encode())
                prov["adapter_contract_task"]=ant.TASK_COMMIT+":"+ant.TASK_PATH
                prov["adapter_run_id"]=inner_req.run_id
                transport=ant.Sentinel(ant.HTTPReply(replay.http_status,replay.payload))
                inner,_,_,_=O(transport,max_tokens=req.max_output_tokens).run(inner_req)
                calls=transport.calls
                if inner.status!="completed":
                    raise mvp.Blocked(inner.terminal_status)
                used_model=inner.model
                usage_origin="anthropic_input_output_fixture_total_local_sum"
                return mvp.ResponseEnvelope(run_id,"anthropic",used_model,inner.status,
                    "PASS_RESOURCE_SYNTHETIC",output=inner.output,usage=inner.usage)

        expected=asdict(original)
        class Admission:
            def admit(_,envelope):
                if asdict(envelope)!=expected:
                    raise mvp.Blocked("BLOCKED_REQUEST_CHANGED")
        # Существующий lifecycle используется без исходного фиктивного OpenAI adapter.
        runtime=mvp.Orchestrator.__new__(mvp.Orchestrator)
        runtime.admission=Admission()
        runtime.registry=mvp.AdapterRegistry([Bridge("openai",pol.MODELS),
                                               Bridge("anthropic",{ANTHROPIC_MODEL})])
        runtime.router=mvp.Router(runtime.registry)
        try:
            response,state,routing,_=runtime.run(original)
        except Exception:
            return result("blocked","BLOCKED_ADAPTER_FAILURE")
        if req.identity!=request_hash or asdict(original)!=expected:
            return result("blocked","BLOCKED_REQUEST_CHANGED")
        if state.in_execution_wip or routing.status!="not_started":
            return result("blocked","BLOCKED_LIFECYCLE_BOUNDARY")
        if response.status!="completed":
            return result("blocked",response.terminal_status)
        try:
            text=response.output
            require(response.provider==req.provider and response.model==req.model,
                    "BLOCKED_MODEL_UNAVAILABLE")
            require(type(text) is str and bool(text.strip()) and
                    len(text.encode())<=req.acceptance.max_output_bytes,"BLOCKED_RESULT_BOUND")
            require(req.acceptance.expected_output_sha256 is None or
                    sha(text.encode())==req.acceptance.expected_output_sha256,"BLOCKED_RESULT_CHECK")
            u=response.usage
            require(type(u) is dict and all(type(k) is str and type(v) is int and
                    0<=v<=10**9 for k,v in u.items()),"BLOCKED_USAGE")
            require({"input_tokens","output_tokens","total_tokens"}<=set(u),"BLOCKED_USAGE")
            require(u["output_tokens"]<=req.max_output_tokens,"BLOCKED_USAGE")
            require(prov.get("adapter_input_sha256")==D0_SHA256,"BLOCKED_REQUEST_CHANGED")
        except GatewayError as exc:
            return result("blocked",str(exc))
        except (UnicodeError,TypeError):
            return result("blocked","BLOCKED_RESULT_BOUND")
        prov["output_sha256"]=sha(text.encode())
        prov["technical_acceptance"]="bounded_text_checks_passed_not_project_acceptance"
        return result("completed","PASS_RESOURCE_SYNTHETIC",text,tuple(sorted(u.items())))

def verify_result(result: ResourceResult, request: EntityRequest, identity: str) -> bool:
    """Проверка целостности и корреляции, не подпись, не содержательная приёмка."""
    try:
        return (type(result) is ResourceResult and type(request) is EntityRequest
            and result.identity==identity and result.request_sha256==request.identity
            and result.requester==request.requester and result.request_id==request.request_id
            and result.project_acceptance=="NOT_GRANTED" and not result.caller_writer_changed
            and not result.gateway_writer_authority and not result.provider_writer_authority
            and not result.project_state_applied and not result.external_dispatch_performed)
    except (ValueError,TypeError,UnicodeError):
        return False
