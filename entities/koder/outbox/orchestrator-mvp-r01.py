#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any, Optional
import argparse, json

WRITER_BLOB = "23f20f04504c65497c154c099d8090cde11fba83"
TASK_PATH = "entities/koordinator/outbox/KOO__orchestrator-mvp-r01__KOD.md"
TASK_COMMIT = "7cfaa8f051bb41eb5bf6d66c1c25df8091c9d370"
TASK_BLOB = "61fb873672c6603e0f97bd7cf49e71f90c03570b"

class Blocked(RuntimeError):
    pass

@dataclass(frozen=True)
class TaskIdentity:
    path: str
    commit: str
    blob: str

@dataclass
class RequestEnvelope:
    run_id: str
    entity: str
    writer_blob: str
    task: TaskIdentity
    task_class: str
    content: str
    data_class: str = "synthetic"
    external_send_allowed: bool = False
    capabilities_required: list[str] = field(default_factory=lambda: ["text"])
    provider: str = "openai"
    model: str = "gpt-5.6-luna"
    tools_allowed: list[str] = field(default_factory=list)
    reasoning: str = "MEDIUM"
    reasoning_mandatory: bool = False

@dataclass
class ResponseEnvelope:
    run_id: str
    provider: Optional[str]
    model: Optional[str]
    status: str
    terminal_status: str
    output: str = ""
    usage: dict[str, Optional[int]] = field(default_factory=lambda: {"input_tokens": None, "output_tokens": None, "total_tokens": None})
    reasoning: dict[str, Any] = field(default_factory=dict)
    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    provider_state: dict[str, Any] = field(default_factory=dict)

@dataclass
class RunState:
    cycle_state: str = "ADMISSION"
    terminal_status: Optional[str] = None
    result_locator: Optional[str] = None
    @property
    def in_execution_wip(self) -> bool:
        return self.cycle_state not in {"TERMINAL_RESULT", "ROUTING", "ROUTING_COMPLETE"}

@dataclass
class RoutingState:
    status: str = "not_started"
    receipt: Optional[str] = None
    @property
    def complete(self) -> bool:
        return self.status == "routing_complete"

@dataclass
class Telemetry:
    run_id: str
    entity: str
    provider: Optional[str] = None
    model: Optional[str] = None
    reasoning_effort: Optional[str] = None
    tool_calls: int = 0
    retries: int = 0
    reconciliations: int = 0
    operator_rewakes: int = 0
    estimated_cost: Optional[float] = None
    latency: dict[str, Optional[float]] = field(default_factory=lambda: {"queue":None,"startup":None,"execution":None,"routing":None,"wall":None})
    result: Optional[str] = None

class TaskAdmission:
    def admit(self, req: RequestEnvelope) -> None:
        if req.entity != "KOD":
            raise Blocked("BLOCKED_WRONG_ENTITY")
        if req.writer_blob != WRITER_BLOB:
            raise Blocked("BLOCKED_WRONG_WRITER")
        if req.task != TaskIdentity(TASK_PATH, TASK_COMMIT, TASK_BLOB):
            raise Blocked("BLOCKED_TASK_IDENTITY_MISMATCH")

@dataclass(frozen=True)
class AdapterCapabilities:
    models: frozenset[str]
    capabilities: frozenset[str]
    available: bool
    reasoning_map: dict[str, str] = field(default_factory=dict)

class ProviderAdapter:
    provider_id = "abstract"
    caps = AdapterCapabilities(frozenset(), frozenset(), False, {})
    def fake_invoke(self, req: RequestEnvelope) -> ResponseEnvelope:
        raise NotImplementedError

class OpenAIFakeAdapter(ProviderAdapter):
    provider_id = "openai"
    caps = AdapterCapabilities(frozenset({"gpt-5.6-luna"}), frozenset({"text"}), True, {})
    def __init__(self): self.invocations = 0
    def fake_invoke(self, req: RequestEnvelope) -> ResponseEnvelope:
        self.invocations += 1
        return ResponseEnvelope(req.run_id, self.provider_id, req.model, "completed", "PASS_SYNTHETIC_OPENAI", output=f"fake:{req.content}")

class AnthropicStub(ProviderAdapter):
    provider_id = "anthropic"
    caps = AdapterCapabilities(frozenset(), frozenset({"text"}), False, {})

class GoogleStub(ProviderAdapter):
    provider_id = "google"
    caps = AdapterCapabilities(frozenset(), frozenset({"text"}), False, {})

class AdapterRegistry:
    def __init__(self, adapters: list[ProviderAdapter]):
        self._adapters = {a.provider_id: a for a in adapters}
    def get(self, provider: str) -> ProviderAdapter:
        if provider not in self._adapters:
            raise Blocked("BLOCKED_PROVIDER_UNREGISTERED")
        return self._adapters[provider]


def map_reasoning(level: str, mandatory: bool, native_map: dict[str, str]) -> dict[str, Any]:
    if level in native_map:
        return {"requested": level, "applied": "supported", "provider_native": native_map[level]}
    if mandatory:
        return {"requested": level, "applied": "rejected", "provider_native": None}
    return {"requested": level, "applied": "omitted_unsupported", "provider_native": None}

class Router:
    def __init__(self, registry: AdapterRegistry): self.registry = registry
    def select(self, req: RequestEnvelope) -> tuple[ProviderAdapter, dict[str, Any]]:
        if req.data_class in {"project_internal", "sensitive"} and not req.external_send_allowed:
            raise Blocked("BLOCKED_PRIVACY_BOUNDARY")
        if req.tools_allowed:
            raise Blocked("BLOCKED_TOOL_AUTHORITY")
        adapter = self.registry.get(req.provider)
        if not adapter.caps.available:
            raise Blocked("BLOCKED_PROVIDER_UNAVAILABLE")
        if req.model not in adapter.caps.models:
            raise Blocked("BLOCKED_MODEL_UNAVAILABLE")
        missing = set(req.capabilities_required) - set(adapter.caps.capabilities)
        if missing:
            raise Blocked("BLOCKED_UNSUPPORTED_CAPABILITY")
        reasoning = map_reasoning(req.reasoning, req.reasoning_mandatory, adapter.caps.reasoning_map)
        if reasoning["applied"] == "rejected":
            raise Blocked("BLOCKED_REASONING_UNSUPPORTED")
        return adapter, reasoning

class Orchestrator:
    def __init__(self):
        self.openai = OpenAIFakeAdapter()
        self.registry = AdapterRegistry([self.openai, AnthropicStub(), GoogleStub()])
        self.router = Router(self.registry)
        self.admission = TaskAdmission()
    def run(self, req: RequestEnvelope) -> tuple[ResponseEnvelope, RunState, RoutingState, Telemetry]:
        run = RunState()
        routing = RoutingState()
        tel = Telemetry(req.run_id, req.entity, reasoning_effort=req.reasoning)
        try:
            self.admission.admit(req)
            adapter, reasoning = self.router.select(req)
            run.cycle_state = "RUNNING"
            tel.provider, tel.model = adapter.provider_id, req.model
            resp = adapter.fake_invoke(req)
            resp.reasoning = reasoning
            run.cycle_state = "TERMINAL_RESULT"
            run.terminal_status = resp.terminal_status
            tel.result = resp.terminal_status
            return resp, run, routing, tel
        except Blocked as exc:
            status = str(exc)
            run.cycle_state = "TERMINAL_RESULT"
            run.terminal_status = status
            tel.result = status
            return ResponseEnvelope(req.run_id, req.provider, req.model, "blocked", status), run, routing, tel


def base_request(**changes: Any) -> RequestEnvelope:
    req = RequestEnvelope("run-synthetic-001", "KOD", WRITER_BLOB, TaskIdentity(TASK_PATH, TASK_COMMIT, TASK_BLOB), "coding", "hello")
    for k, v in changes.items(): setattr(req, k, v)
    return req

def compact_operator(resp: ResponseEnvelope, routing: RoutingState) -> str:
    return f"STATUS: {resp.terminal_status}\nROUTE: {resp.provider}/{resp.model}\nROUTING: {routing.status}\nRESULT: {resp.output or resp.status}"

def self_test() -> dict[str, Any]:
    o = Orchestrator(); checks = []
    resp, run, routing, tel = o.run(base_request())
    pass_resp, pass_routing = resp, routing
    assert resp.terminal_status == "PASS_SYNTHETIC_OPENAI" and o.openai.invocations == 1; checks.append("pass_openai_fake_route")
    resp, *_ = o.run(base_request(data_class="project_internal", external_send_allowed=False))
    assert resp.terminal_status == "BLOCKED_PRIVACY_BOUNDARY"; checks.append("privacy_boundary")
    resp, *_ = o.run(base_request(capabilities_required=["vision"]))
    assert resp.terminal_status == "BLOCKED_UNSUPPORTED_CAPABILITY"; checks.append("unsupported_capability")
    before = o.openai.invocations
    resp, *_ = o.run(base_request(provider="anthropic", model="any"))
    assert resp.terminal_status == "BLOCKED_PROVIDER_UNAVAILABLE" and o.openai.invocations == before; checks.append("no_silent_fallback")
    resp, run, routing, _ = o.run(base_request(run_id="terminal-separation"))
    assert not run.in_execution_wip and not routing.complete and routing.status == "not_started"; checks.append("terminal_vs_routing_state")
    supported = map_reasoning("HIGH", True, {"HIGH":"native-high"}); omitted = map_reasoning("HIGH", False, {}); rejected = map_reasoning("HIGH", True, {})
    assert supported["applied"] == "supported" and omitted["applied"] == "omitted_unsupported" and rejected["applied"] == "rejected"; checks.append("reasoning_mapping_states")
    resp, *_ = o.run(base_request(tools_allowed=["shell"]))
    assert resp.terminal_status == "BLOCKED_TOOL_AUTHORITY"; checks.append("tool_default_deny")
    return {"verdict":"PASS_ORCHESTRATOR_MVP_R01_READY_FOR_RUNTIME_REVIEW","checks":checks,"count":len(checks),"telemetry":asdict(tel),"operator_result":compact_operator(pass_resp,pass_routing)}

def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--self-test", action="store_true"); ap.add_argument("--demo", action="store_true"); args = ap.parse_args()
    if args.self_test:
        print(json.dumps(self_test(), indent=2, sort_keys=True)); return
    if args.demo:
        resp, run, routing, tel = Orchestrator().run(base_request())
        print(compact_operator(resp, routing)); print(json.dumps({"run":asdict(run),"routing":asdict(routing),"telemetry":asdict(tel)}, indent=2)); return
    ap.print_help()
if __name__ == "__main__": main()
