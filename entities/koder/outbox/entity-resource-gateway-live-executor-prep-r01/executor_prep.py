#!/usr/bin/env python3
"""Подготовка границы одного вызова. Локально, Python 3.10+, обычный пользователь.
Нет HTTP-исполнителя, чтения ключей, окружения, часов, БД, запуска wrapper или dispatch.
Проверка: python3 -I -B candidate/test_executor.py --deps deps
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict, replace
from pathlib import Path
from types import ModuleType
from typing import Protocol, Callable, Any
import builtins
import hashlib
import json
import math
import re
import sys
import threading

PASS = "PASS_ENTITY_RESOURCE_GATEWAY_LIVE_EXECUTOR_PREP_R01_READY_FOR_INDEPENDENT_VERIFY"
GATEWAY_BLOB = "e93ac320468dfeed84a7342b4e9dc5c597f48fc2"
LIVE_TRANSPORT_BLOB = "4407a38113b5dd7de8ec30caca29be66a78f0239"
RUNTIME_ROOT = "/home/pev5691/openai-d0-runtime-r01"
WRAPPER_SHA256 = "0e4d85e0eda92b3b63a064a271cfd16c8150fa5ef6850e6a445a5fcbc2356edb"
OPENAI_FINAL_GATE = "787ec5df1878c7ddb0a5f2928c61e265b40959b0"
ANTHROPIC_REVIEW = "d92b3a9ba5abc0c4d1f03169425fb2dcb6e6cd6a"
MAX_LEDGER = 1024

class PreparationError(ValueError):
    """Только фиксированный код. Внешний текст не переносится в исключение."""

def require(value: bool, code: str) -> None:
    if not value:
        raise PreparationError(code)

def canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False)

def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()

def blob(data: bytes) -> str:
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def tick(value: Any) -> bool:
    return type(value) is int and 0 <= value <= 2**53-1

def finite(value: Any, low: float, high: float) -> bool:
    return (type(value) in (float, int) and math.isfinite(value) and low <= value <= high)

@dataclass(frozen=True)
class CredentialReference:
    provider: str
    locator: str = field(repr=False)
    def __post_init__(self):
        require(type(self.provider) is str and self.provider in ("openai","anthropic"),
                "BLOCKED_CREDENTIAL_REFERENCE")
        require(type(self.locator) is str and re.fullmatch(
            r"secretref:"+self.provider+r":[A-Za-z0-9_.-]{1,64}", self.locator) is not None,
            "BLOCKED_CREDENTIAL_REFERENCE")

@dataclass(frozen=True)
class ExecutionPolicy:
    timeout_seconds: float = 30.0
    max_attempts: int = 1
    automatic_retries: int = 0
    max_response_bytes: int = 65536
    def __post_init__(self):
        require(finite(self.timeout_seconds,1.0,60.0), "BLOCKED_TIMEOUT_POLICY")
        require(type(self.max_attempts) is int and self.max_attempts == 1 and
                type(self.automatic_retries) is int and self.automatic_retries == 0,
                "BLOCKED_RETRY_POLICY")
        require(type(self.max_response_bytes) is int and
                1 <= self.max_response_bytes <= 65536, "BLOCKED_RESPONSE_BOUND")

@dataclass(frozen=True)
class PreparedExecution:
    request_sha256: str
    requester: object
    provider: str
    model: str
    credential: CredentialReference = field(repr=False)
    policy: ExecutionPolicy
    native_plan_json: str = field(repr=False)
    binding: tuple[tuple[str,str], ...]
    version: str = field(default="executor-preparation-r01", init=False)
    live_enabled: bool = field(default=False, init=False)
    @property
    def identity(self) -> str:
        return digest(asdict(self))
    def redacted(self) -> dict:
        return {"plan_sha256":self.identity,"request_sha256":self.request_sha256,
                "provider":self.provider,"model":self.model,"policy":asdict(self.policy),
                "binding":dict(self.binding),"live_enabled":False,
                "credential_value_present":False,"credential_reference_exported":False}

@dataclass(frozen=True)
class LIVE_EXECUTION_AUTHORITY:
    """Заявка на точный допуск, не самоподтверждающее полномочие.
    mode SIMULATION не является реальным разрешением на сеть.
    Подлинность source/current writer обязан проверить отдельный доверенный verifier.
    """
    source: object
    requester: object
    request_sha256: str
    plan_sha256: str
    provider: str
    model: str
    credential: CredentialReference = field(repr=False)
    policy: ExecutionPolicy
    not_before_tick: int
    valid_until_tick: int
    mode: str
    kind: str = "LIVE_EXECUTION_AUTHORITY"
    max_calls: int = 1
    data_class: str = "D0_SYNTHETIC"

@dataclass(frozen=True)
class VerifiedAdmission:
    """Внешний результат проверки. Объект не принимается из provider response."""
    authority_sha256: str
    request_sha256: str
    plan_sha256: str
    requester_sha256: str
    decision_source_sha256: str
    mode: str
    valid_until_tick: int

class LiveExecutorPort(Protocol):
    """Контракт будущего отдельно проверенного исполнителя.
    Worker обязан иметь жёсткий timeout/лимит чтения, durable one-shot CAS,
    локальное разрешение secret reference без возврата значения,
    проверку runtime identity и запрет повторов/redirect/fallback.
    В этом пакете реализации данного интерфейса нет.
    """
    def invoke_once(self, plan: PreparedExecution, admission: VerifiedAdmission) -> object: ...

class ReplayPort:
    """Только точные тестовые байты. Никакого пользовательского callback."""
    def __init__(self, reply: object, *, elapsed_seconds: float = 0.0, failure: bool = False):
        require(finite(elapsed_seconds,0,3600) and type(failure) is bool, "BLOCKED_REPLAY_PORT")
        self.reply, self.elapsed_seconds, self.failure = reply, elapsed_seconds, failure
        self.calls = 0
    def take_once(self):
        self.calls += 1
        if self.failure:
            raise RuntimeError("UNTRUSTED_EXECUTOR_DIAGNOSTIC")
        return self.reply

class OneShotLedger:
    """Только память одного процесса. Не подходит как durable ledger для live."""
    def __init__(self):
        self._lock = threading.Lock()
        self._used: set[str] = set()
    def claim(self, key: str) -> None:
        with self._lock:
            require(key not in self._used, "BLOCKED_AUTHORITY_ALREADY_CONSUMED")
            require(len(self._used) < MAX_LEDGER, "BLOCKED_LEDGER_CAPACITY")
            self._used.add(key)
    @property
    def count(self) -> int:
        with self._lock:
            return len(self._used)

def _module(name: str, path: Path, data: bytes, imports: dict | None = None) -> ModuleType:
    mod = ModuleType(name)
    mod.__file__ = str(path)
    sys.modules[name] = mod
    if imports:
        def importer(name, globals=None, locals=None, fromlist=(), level=0):
            if level==0 and name in imports:
                return imports[name]
            return builtins.__import__(name, globals, locals, fromlist, level)
        mod.__dict__["__builtins__"] = {**vars(builtins),"__import__":importer}
    exec(compile(data,str(path),"exec"),mod.__dict__)
    return mod

class ExecutorPreparation:
    def __init__(self, dependencies: Path, ledger: OneShotLedger | None = None):
        # Все данные читаются только из явно заданного каталога с точными исходниками.
        try:
            raw = (dependencies/"gateway.py").read_bytes()
            live = (dependencies/"live_transport.py").read_bytes()
        except OSError:
            raise PreparationError("BLOCKED_DEPENDENCY_UNAVAILABLE") from None
        require(blob(raw)==GATEWAY_BLOB and blob(live)==LIVE_TRANSPORT_BLOB,
                "BLOCKED_DEPENDENCY_IDENTITY")
        self.g = _module("_executor_prep_gateway",dependencies/"gateway.py",raw)
        self.modules = self.g.load_dependencies(dependencies)
        self.live = _module("_executor_prep_live_transport",dependencies/"live_transport.py",live,
                            {"policy":self.modules["policy.py"],
                             "openai_adapter":self.modules["openai_adapter.py"]})
        require(self.live.LIVE_SWITCH_ENV=="OPENAI_LIVE_D0" and
                self.live.LIVE_SWITCH_VALUE=="EXPLICIT_D0_LIVE" and
                self.live.MIN_TIMEOUT_SECONDS==1.0 and self.live.MAX_TIMEOUT_SECONDS==60.0,
                "BLOCKED_RUNTIME_CONTRACT_CHANGED")
        require(ledger is None or type(ledger) is OneShotLedger, "BLOCKED_LEDGER")
        self.ledger = OneShotLedger() if ledger is None else ledger

    def prepare(self, request: object, credential: CredentialReference,
                policy: ExecutionPolicy | None = None) -> PreparedExecution:
        g=self.g
        try:
            g.validate_request(request)
            g.check_policy(request)
        except (g.GatewayError,ValueError,TypeError,UnicodeError,RecursionError):
            raise PreparationError("BLOCKED_REQUEST_POLICY") from None
        require(type(credential) is CredentialReference and credential.provider==request.provider,
                "BLOCKED_CREDENTIAL_REFERENCE")
        policy=ExecutionPolicy() if policy is None else policy
        require(type(policy) is ExecutionPolicy, "BLOCKED_EXECUTION_POLICY")
        # Повторно проверяется состав policy, даже когда тип создавался другим кодом.
        ExecutionPolicy(**asdict(policy))
        binding={"gateway_blob":GATEWAY_BLOB,"request_payload_sha256":g.D0_SHA256,
                 "result_mode":"synthetic_no_network","live_attachment":"not_installed",
                 "accepted_gateway_external_send":"false"}
        if request.provider=="openai":
            pol=self.modules["policy.py"]; adapter=self.modules["openai_adapter.py"]
            require(request.model in pol.MODELS, "BLOCKED_MODEL_UNAVAILABLE")
            config=pol.valid_synthetic_config(request.model,request.payload)
            config["max_output_tokens"]=request.max_output_tokens
            normalized=pol.PolicyGuard().evaluate(config).normalized
            plan=adapter.build_request_plan(normalized)
            self.live.validate_blueprint(plan)
            binding.update({"provider_contract_blob":LIVE_TRANSPORT_BLOB,
                "runtime_root":RUNTIME_ROOT,"wrapper_sha256":WRAPPER_SHA256,
                "technical_gate_commit":OPENAI_FINAL_GATE,
                "switch_name":"OPENAI_LIVE_D0","switch_value":"EXPLICIT_D0_LIVE",
                "secret_input":"hidden_dev_tty_only_in_verified_wrapper",
                "preset_OPENAI_API_KEY":"reject","runtime_key_resolver":"not_invoked",
                "future_entrypoint":"OpenAIResponsesLiveTransport.run_live",
                "transport_constructor":"UrllibExecutor+EnvironmentSecretReader"})
        elif request.provider=="anthropic":
            ant=self.modules["anthropic-provider-compatible-adapter-r01.py"]
            mvp=self.modules["orchestrator-mvp-r01.py"]
            require(request.model==g.ANTHROPIC_MODEL, "BLOCKED_MODEL_UNAVAILABLE")
            bindings=(ant.ModelBinding(request.model,(request.model,),
                                       "executor-prep-fixture-not-entitlement",True),)
            _,make_req,make_plan=ant.build_runtime(mvp,bindings,
                ant.AuthReference("api_key_bearer",credential.locator))
            inner=make_req(request.model)
            require(inner.content==request.payload,"BLOCKED_PAYLOAD_SUBSTITUTION")
            native=make_plan(inner,request.max_output_tokens)
            plan=asdict(native); plan["body"]=json.loads(native.body)
            binding.update({"provider_contract_blob":g.PINS["anthropic-provider-compatible-adapter-r01.py"],
                "technical_gate_commit":ANTHROPIC_REVIEW,
                "transport_boundary":"RequestPlan->HTTPReply",
                "transport_implementation":"not_installed",
                "model_binding":"explicit_synthetic_fixture_only",
                "inner_task_commit":ant.TASK_COMMIT,
                "inner_task_path":ant.TASK_PATH,"inner_run_id":inner.run_id})
        else:
            raise PreparationError("BLOCKED_PROVIDER_UNREGISTERED")
        return PreparedExecution(request.identity,request.requester,request.provider,request.model,
                                 credential,policy,canonical(plan),tuple(sorted(binding.items())))

    def _admit(self, request, plan, authority, verifier, now_tick, mode):
        require(type(plan) is PreparedExecution and plan.live_enabled is False, "BLOCKED_PLAN")
        require(self.prepare(request,plan.credential,plan.policy)==plan, "BLOCKED_PLAN_BINDING")
        require(tick(now_tick), "BLOCKED_AUTHORITY_TIME")
        require(type(authority) is LIVE_EXECUTION_AUTHORITY and
                authority.kind=="LIVE_EXECUTION_AUTHORITY", "BLOCKED_LIVE_EXECUTION_AUTHORITY")
        require(mode in ("SIMULATION","LIVE") and authority.mode==mode, "BLOCKED_AUTHORITY_MODE")
        try:
            self.g.validate_ref(authority.source)
        except (self.g.GatewayError,AttributeError,TypeError):
            raise PreparationError("BLOCKED_AUTHORITY_SOURCE") from None
        require(type(authority.requester) is self.g.Requester and
                authority.requester==request.requester and
                authority.request_sha256==request.identity and
                authority.plan_sha256==plan.identity and
                authority.provider==request.provider and authority.model==request.model and
                authority.credential==plan.credential and authority.policy==plan.policy and
                authority.data_class==request.data_class=="D0_SYNTHETIC",
                "BLOCKED_AUTHORITY_BINDING")
        require(type(authority.max_calls) is int and authority.max_calls==1,
                "BLOCKED_AUTHORITY_BUDGET")
        require(tick(authority.not_before_tick) and tick(authority.valid_until_tick) and
                authority.not_before_tick <= now_tick < authority.valid_until_tick,
                "BLOCKED_AUTHORITY_EXPIRED")
        require(callable(verifier),"BLOCKED_AUTHORITY_UNVERIFIED")
        a_hash=digest(asdict(authority)); requester_hash=digest(asdict(request.requester))
        source_hash=digest(asdict(authority.source))
        try:
            att=verifier(authority,plan,now_tick)
        except Exception:
            raise PreparationError("BLOCKED_AUTHORITY_UNVERIFIED") from None
        require(type(att) is VerifiedAdmission and
                att.authority_sha256==a_hash and att.request_sha256==request.identity and
                att.plan_sha256==plan.identity and att.requester_sha256==requester_hash and
                att.decision_source_sha256==source_hash and att.mode==mode and
                tick(att.valid_until_tick) and now_tick < att.valid_until_tick <= authority.valid_until_tick,
                "BLOCKED_AUTHORITY_UNVERIFIED")
        # Callback доверенный, но изменение контекста всё равно не допускается.
        require(digest(asdict(authority))==a_hash and
                self.prepare(request,plan.credential,plan.policy)==plan, "BLOCKED_CONTEXT_CHANGED")
        return att,source_hash,a_hash

    def execute_once(self, request, plan, *, mode="NO_LIVE", authority=None,
                     verifier=None, now_tick=0, port=None, live_switch=None):
        """Единственный исполняемый путь r0.1: явно допущенная SIMULATION.
        LIVE проверяет gate, затем закрывается до вызова любого порта.
        """
        require(type(mode) is str and mode in ("NO_LIVE","SIMULATION","LIVE"),
                "BLOCKED_EXECUTION_MODE")
        require(mode!="NO_LIVE","BLOCKED_NO_LIVE_DEFAULT")
        att,key,a_hash=self._admit(request,plan,authority,verifier,now_tick,mode)
        if mode=="LIVE":
            if plan.provider=="openai":
                require(live_switch=="EXPLICIT_D0_LIVE", "BLOCKED_OPENAI_LIVE_SWITCH")
            # Принятый ResourceResult и внешняя отправка остаются синтетическими.
            # Не принимать любой callback с флагом network_capable как полномочие.
            raise PreparationError("BLOCKED_LIVE_ATTACHMENT_REQUIRED")
        require(type(port) is ReplayPort,"BLOCKED_NONNETWORK_PORT_REQUIRED")
        require(type(port.reply) is self.g.ReplayResponse and
                port.reply.request_sha256==request.identity and
                port.reply.provider==request.provider and
                type(port.reply.payload) is bytes and
                len(port.reply.payload)<=plan.policy.max_response_bytes,
                "BLOCKED_REPLAY_BINDING")
        require(finite(port.elapsed_seconds,0,3600) and type(port.failure) is bool,
                "BLOCKED_REPLAY_PORT")
        # Решение расходуется ДО единственной попытки, включая неизвестный исход и timeout.
        self.ledger.claim(key)
        forced=None; reply=None
        try:
            reply=port.take_once()
            if port.elapsed_seconds >= plan.policy.timeout_seconds:
                forced="BLOCKED_EXECUTION_TIMEOUT"
        except Exception:
            forced="BLOCKED_EXECUTOR_FAILURE"
        gateway=self.g.Gateway.__new__(self.g.Gateway)
        gateway.modules=self.modules
        gateway.verifier=lambda req: req.identity==plan.request_sha256
        gateway.unavailable=()
        resource=gateway.run(request,reply if forced is None else None)
        if forced:
            resource=replace(resource,technical_status="blocked",terminal_status=forced,
                             blocker=forced,payload="",usage=(),usage_origin=None)
        provenance=dict(resource.provenance)
        provenance.update({"preparation_plan_sha256":plan.identity,
                           "authority_sha256":a_hash,"authority_mode":"SIMULATION",
                           "executor_attempts":str(port.calls),"automatic_retries":"0",
                           "credential_resolution":"not_performed"})
        resource=replace(resource,provenance=tuple(sorted(provenance.items())))
        require(resource.requester==request.requester and resource.project_acceptance=="NOT_GRANTED"
                and resource.execution_mode=="synthetic_no_network" and
                not any((resource.caller_writer_changed,resource.gateway_writer_authority,
                         resource.provider_writer_authority,resource.project_state_applied,
                         resource.external_dispatch_performed)) and resource.routing_status=="not_started",
                "FAIL_RESOURCE_AUTHORITY_BOUNDARY")
        return resource
