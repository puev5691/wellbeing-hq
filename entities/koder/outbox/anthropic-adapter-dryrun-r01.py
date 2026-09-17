#!/usr/bin/env python3
# Запускать в локальном Python 3.10+ без сети и секретов; не в production.
"""Anthropic r0.1: только синтетический адаптер, не реализация HTTP API.

python3 -B anthropic-adapter-dryrun-r01.py --self-test
Зависимость: неизменённый orchestrator-mvp-r01.py с проверяемым Git blob.
Модели synthetic-anthropic-* являются тестовыми идентификаторами проекта.
Реальные model IDs, endpoints, headers и provider-native reasoning не заданы.
Никакой работы с окружением ключей, accounts, billing или живым транспортом.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import sys
from dataclasses import asdict, fields
from pathlib import Path
from types import ModuleType
from typing import Any

MVP_BLOB = "55939b2e4c91f7af1159a60b2f4ee8fa961196f2"
TASK_PATH = "entities/koordinator/outbox/KOO__anthropic-adapter-dryrun-r01__KOD.md"
TASK_COMMIT = "1f95fbb50098bdd238d676988357ea45d074b1f5"
TASK_BLOB = "5064c1103be27fd49022a087944f924b9654c6ea"
WRITER_BLOB = "bfeff738de2759248307dd52433c77139624fb54"
MODELS = frozenset({"synthetic-anthropic-text-a-r01", "synthetic-anthropic-text-b-r01"})
REASONING = frozenset({"LOW", "MEDIUM", "HIGH"})
SECRET_REF = "secretref:anthropic:unresolved-dryrun"
RUN_ID = "run-anthropic-dryrun-r01"
CONTENT = "SYNTHETIC_ANTHROPIC_INPUT"
OUTPUT = "SYNTHETIC_ANTHROPIC_OK"
PASS = "PASS_ANTHROPIC_ADAPTER_DRYRUN_R01_READY_FOR_REVIEW"


def load_mvp(path: Path | None = None) -> ModuleType:
    """Читать только локальный код с точным Git blob, не скачивать зависимости."""
    if path is None:
        here = Path(__file__).resolve().parent
        candidates = [here / "orchestrator-mvp-r01.py"]
        candidates.extend(p / "entities/koder/outbox/orchestrator-mvp-r01.py"
                          for p in [here, *here.parents])
        path = next((p for p in candidates if p.is_file()), None)
    if path is None:
        raise RuntimeError("BLOCKED_MVP_FILE_UNAVAILABLE")
    data = path.read_bytes()
    actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    if actual != MVP_BLOB:
        raise RuntimeError("BLOCKED_MVP_BLOB_MISMATCH")
    name = "_anthropic_dryrun_pinned_mvp"
    module = ModuleType(name)
    module.__file__ = str(path)
    sys.modules[name] = module
    # Исполняются именно проверенные байты, без повторного чтения и TOCTOU.
    exec(compile(data, str(path), "exec"), module.__dict__)
    return module


def build_runtime(mvp: ModuleType):
    """Расширение существующего lifecycle; исходный MVP не изменяется."""
    expected_task = mvp.TaskIdentity(TASK_PATH, TASK_COMMIT, TASK_BLOB)
    expected_fields = {f.name for f in fields(mvp.RequestEnvelope)}

    def deny(code: str) -> None:
        raise mvp.Blocked(code)

    def validate(req: Any) -> None:
        if type(req) is not mvp.RequestEnvelope or set(vars(req)) != expected_fields:
            deny("BLOCKED_REQUEST_SCHEMA")
        string_fields = ("run_id", "entity", "writer_blob", "task_class", "content",
                         "data_class", "provider", "model", "reasoning")
        if any(type(getattr(req, k)) is not str for k in string_fields):
            deny("BLOCKED_REQUEST_SCHEMA")
        if req.entity != "KOD":
            deny("BLOCKED_WRONG_ENTITY")
        if req.writer_blob != WRITER_BLOB:
            deny("BLOCKED_WRONG_WRITER")
        if type(req.task) is not mvp.TaskIdentity or req.task != expected_task:
            deny("BLOCKED_TASK_IDENTITY_MISMATCH")
        if req.run_id != RUN_ID or req.task_class != "coding":
            deny("BLOCKED_SYNTHETIC_METADATA")
        if req.provider != "anthropic":
            deny("BLOCKED_PROVIDER_UNREGISTERED")
        if req.model not in MODELS:
            deny("BLOCKED_MODEL_UNAVAILABLE")
        if req.data_class != "synthetic" or req.content != CONTENT:
            deny("BLOCKED_PRIVACY_BOUNDARY")
        if req.external_send_allowed is not False:
            deny("BLOCKED_EXTERNAL_SEND")
        if type(req.tools_allowed) is not list or req.tools_allowed != []:
            deny("BLOCKED_TOOL_AUTHORITY")
        if (type(req.capabilities_required) is not list or
                req.capabilities_required != ["text"]):
            deny("BLOCKED_UNSUPPORTED_CAPABILITY")
        if req.reasoning not in REASONING or type(req.reasoning_mandatory) is not bool:
            deny("BLOCKED_REASONING_CONTRACT")
        if req.reasoning_mandatory:
            deny("BLOCKED_REASONING_UNSUPPORTED")

    class SentinelTransport:
        """Замкнутый тестовый транспорт: нет сетевых или секретных операций."""
        def __init__(self, case: str = "ok"):
            if type(case) is not str or case not in {
                "ok", "model_mismatch", "provider_mismatch", "tools",
                "unexpected_output", "malformed", "error"
            }:
                deny("BLOCKED_SENTINEL_CASE")
            self.case = case
            self.calls = 0

        def send(self, model: str) -> dict[str, Any]:
            self.calls += 1
            if self.case == "error":
                raise ValueError("UNTRUSTED_TEST_DIAGNOSTIC")
            result = {"provider": "anthropic", "model": model, "output": OUTPUT, "tools": []}
            if self.case == "model_mismatch":
                result["model"] = next(m for m in sorted(MODELS) if m != model)
            if self.case == "provider_mismatch":
                result["provider"] = "unavailable-provider"
            if self.case == "tools":
                result["tools"] = ["UNTRUSTED_TEST_TOOL"]
            if self.case == "unexpected_output":
                result["output"] = "UNTRUSTED_TEST_DIAGNOSTIC"
            if self.case == "malformed":
                result = {"unexpected": "UNTRUSTED_TEST_DIAGNOSTIC"}
            return result

    class AnthropicDryRunAdapter(mvp.ProviderAdapter):
        provider_id = "anthropic"
        caps = mvp.AdapterCapabilities(MODELS, frozenset({"text"}), True, {})

        def __init__(self, transport=None, *, mode: str = "dry_run",
                     secret_ref: str = SECRET_REF):
            if type(mode) is not str or mode != "dry_run":
                deny("BLOCKED_LIVE_AUTHORITY_REQUIRED")
            if type(secret_ref) is not str or secret_ref != SECRET_REF:
                deny("BLOCKED_SECRET_REFERENCE")
            self.transport = SentinelTransport() if transport is None else transport
            if type(self.transport) is not SentinelTransport:
                deny("BLOCKED_EXTERNAL_TRANSPORT")
            self.secret_ref = SECRET_REF

        def fake_invoke(self, req):
            validate(req)  # Повторная защита при прямом вызове без Router.
            try:
                result = self.transport.send(req.model)
            except Exception:
                # Не переносить произвольную диагностику исполнителя в журналы.
                deny("FAIL_SENTINEL_TRANSPORT")
            if type(result) is not dict or set(result) != {"provider", "model", "output", "tools"}:
                deny("FAIL_SENTINEL_RESPONSE_SCHEMA")
            if result["provider"] != "anthropic":
                deny("FAIL_RESPONSE_PROVIDER_MISMATCH")
            if result["model"] != req.model:
                deny("FAIL_RESPONSE_MODEL_MISMATCH")
            if type(result["tools"]) is not list or result["tools"]:
                deny("FAIL_RESPONSE_TOOL_BOUNDARY")
            if result["output"] != OUTPUT:
                deny("FAIL_RESPONSE_SYNTHETIC_BOUNDARY")
            return mvp.ResponseEnvelope(
                req.run_id, "anthropic", req.model, "completed", PASS, output=OUTPUT,
                provider_state={
                    "mode": "synthetic_dry_run", "model_identity_scope": "fixture_only",
                    "network_allowed": False, "private_data_allowed": False,
                    "tools_allowed": False, "secret_reads": 0,
                    "provider_api_compatibility": "not_claimed"
                }
            )

    class Admission:
        def admit(self, req):
            validate(req)

    class AnthropicOrchestrator(mvp.Orchestrator):
        def __init__(self, transport=None, *, mode: str = "dry_run",
                     secret_ref: str = SECRET_REF):
            self.anthropic = AnthropicDryRunAdapter(transport, mode=mode, secret_ref=secret_ref)
            self.registry = mvp.AdapterRegistry([self.anthropic])
            self.router = mvp.Router(self.registry)
            self.admission = Admission()

        def run(self, req):
            # Upstream MVP пишет metadata до admit. Не передавать ему
            # произвольные поля отклонённого запроса, даже без внешней сети.
            try:
                validate(req)
            except mvp.Blocked as exc:
                model = (req.model if type(req) is mvp.RequestEnvelope
                         and type(req.model) is str and req.model in MODELS else None)
                provider = ("anthropic" if type(req) is mvp.RequestEnvelope
                            and type(req.provider) is str and req.provider == "anthropic" else None)
                reasoning = (req.reasoning if type(req) is mvp.RequestEnvelope
                             and type(req.reasoning) is str and req.reasoning in REASONING else None)
                status = str(exc)
                resp = mvp.ResponseEnvelope(RUN_ID, provider, model, "blocked", status)
                state = mvp.RunState(cycle_state="TERMINAL_RESULT", terminal_status=status)
                tel = mvp.Telemetry(RUN_ID, "KOD", provider=provider, model=model,
                                    reasoning_effort=reasoning, result=status)
                return resp, state, mvp.RoutingState(), tel
            return super().run(req)

    def request(model: str, **changes):
        # Обязательный аргумент: OpenAI-default из базового Envelope не наследуется.
        req = mvp.RequestEnvelope(
            RUN_ID, "KOD", WRITER_BLOB, expected_task, "coding", CONTENT,
            provider="anthropic", model=model
        )
        for key, value in changes.items():
            if key not in expected_fields:
                deny("BLOCKED_REQUEST_SCHEMA")
            setattr(req, key, value)
        return req

    return AnthropicOrchestrator, SentinelTransport, request


def compact_telemetry(resp, tel) -> dict[str, Any]:
    """Только проверенные metadata, без content, secret_ref и provider body."""
    return {
        "provider": tel.provider, "model": tel.model,
        "model_identity_scope": "fixture_only",
        "reasoning_requested": tel.reasoning_effort,
        "reasoning_applied": resp.reasoning.get("applied", "not_applied"),
        "provider_native_reasoning": None,
        "tool_boundary": "deny_all", "tool_calls": tel.tool_calls,
        "network_allowed": False, "private_data_allowed": False,
        "secret_access": "none", "retries": tel.retries,
        "latency": tel.latency, "estimated_cost": tel.estimated_cost,
        "result": tel.result
    }


def self_test(mvp: ModuleType) -> dict[str, Any]:
    Orch, Sentinel, request = build_runtime(mvp)
    checks: list[str] = []
    cases = 0

    def check(name, condition):
        nonlocal cases
        if not condition:
            raise AssertionError(name)
        cases += 1

    model_a, model_b = sorted(MODELS)
    for model in sorted(MODELS):
        orch = Orch()
        resp, state, route, tel = orch.run(request(model))
        check("explicit_route", resp.provider == "anthropic" and resp.model == model
              and tel.model == model and resp.terminal_status == PASS
              and orch.anthropic.transport.calls == 1)
        check("same_envelopes", type(resp) is mvp.ResponseEnvelope
              and type(request(model)) is mvp.RequestEnvelope)
        check("same_lifecycle", type(state) is mvp.RunState
              and not state.in_execution_wip and state.cycle_state == "TERMINAL_RESULT"
              and route.status == "not_started" and not route.complete)
        check("reasoning_omitted_not_mapped", resp.reasoning["applied"] == "omitted_unsupported"
              and resp.reasoning["provider_native"] is None)
        check("no_invented_usage", all(v is None for v in resp.usage.values())
              and tel.estimated_cost is None and all(v is None for v in tel.latency.values()))
    checks.append("two_explicit_fixture_models_and_original_lifecycle")

    negatives = [
        ({"provider": "openai"}, "BLOCKED_PROVIDER_UNREGISTERED"),
        ({"provider": "google"}, "BLOCKED_PROVIDER_UNREGISTERED"),
        ({"model": ""}, "BLOCKED_MODEL_UNAVAILABLE"),
        ({"model": "unverified-real-model"}, "BLOCKED_MODEL_UNAVAILABLE"),
        ({"model": []}, "BLOCKED_REQUEST_SCHEMA"),
        ({"capabilities_required": ["vision"]}, "BLOCKED_UNSUPPORTED_CAPABILITY"),
        ({"capabilities_required": ["text", "network"]}, "BLOCKED_UNSUPPORTED_CAPABILITY"),
        ({"capabilities_required": "text"}, "BLOCKED_UNSUPPORTED_CAPABILITY"),
        ({"tools_allowed": ["shell"]}, "BLOCKED_TOOL_AUTHORITY"),
        ({"tools_allowed": None}, "BLOCKED_TOOL_AUTHORITY"),
        ({"external_send_allowed": True}, "BLOCKED_EXTERNAL_SEND"),
        ({"external_send_allowed": 0}, "BLOCKED_EXTERNAL_SEND"),
        ({"data_class": "project_internal"}, "BLOCKED_PRIVACY_BOUNDARY"),
        ({"data_class": "sensitive", "external_send_allowed": True}, "BLOCKED_PRIVACY_BOUNDARY"),
        ({"data_class": "unknown"}, "BLOCKED_PRIVACY_BOUNDARY"),
        ({"content": "UNTRUSTED_TEST_DIAGNOSTIC"}, "BLOCKED_PRIVACY_BOUNDARY"),
        ({"run_id": "UNTRUSTED_TEST_DIAGNOSTIC"}, "BLOCKED_SYNTHETIC_METADATA"),
        ({"reasoning": "UNTRUSTED_TEST_DIAGNOSTIC"}, "BLOCKED_REASONING_CONTRACT"),
        ({"reasoning_mandatory": True}, "BLOCKED_REASONING_UNSUPPORTED"),
        ({"reasoning_mandatory": 0}, "BLOCKED_REASONING_CONTRACT"),
        ({"writer_blob": "old-writer"}, "BLOCKED_WRONG_WRITER"),
        ({"entity": "OTHER"}, "BLOCKED_WRONG_ENTITY"),
        ({"task": None}, "BLOCKED_TASK_IDENTITY_MISMATCH"),
    ]
    for changes, expected in negatives:
        orch = Orch()
        req = request(model_a, **{k:v for k,v in changes.items() if k != "model"})
        if "model" in changes:
            req.model = changes["model"]
        resp, state, route, tel = orch.run(req)
        check(expected, resp.terminal_status == expected and orch.anthropic.transport.calls == 0
              and not state.in_execution_wip and route.status == "not_started")
        exported = json.dumps([asdict(resp), asdict(tel), compact_telemetry(resp, tel)])
        check("rejected_metadata_redacted", "UNTRUSTED_TEST_DIAGNOSTIC" not in exported
              and CONTENT not in exported and SECRET_REF not in exported)
    checks.append("23_negative_requests_rejected_before_transport_and_redacted")

    for bad in [None, {}, "UNTRUSTED_TEST_DIAGNOSTIC"]:
        orch = Orch()
        resp, *_ = orch.run(bad)
        check("malformed_envelope", resp.terminal_status == "BLOCKED_REQUEST_SCHEMA"
              and orch.anthropic.transport.calls == 0)
    req = request(model_a)
    req.untrusted_extra = "UNTRUSTED_TEST_DIAGNOSTIC"
    check("unknown_field", Orch().run(req)[0].terminal_status == "BLOCKED_REQUEST_SCHEMA")
    checks.append("malformed_envelopes_and_unknown_fields_denied")

    try:
        request()
    except TypeError:
        check("model_has_no_default", True)
    else:
        raise AssertionError("model_has_no_default")
    for kwargs, expected in [
        ({"mode": "live"}, "BLOCKED_LIVE_AUTHORITY_REQUIRED"),
        ({"secret_ref": "UNTRUSTED_TEST_DIAGNOSTIC"}, "BLOCKED_SECRET_REFERENCE"),
        ({"transport": object()}, "BLOCKED_EXTERNAL_TRANSPORT"),
    ]:
        try:
            Orch(**kwargs)
        except mvp.Blocked as exc:
            check(expected, str(exc) == expected)
        else:
            raise AssertionError(expected)
    checks.append("explicit_model_closed_live_secret_and_transport_gates")

    for case, status in [
        ("model_mismatch", "FAIL_RESPONSE_MODEL_MISMATCH"),
        ("provider_mismatch", "FAIL_RESPONSE_PROVIDER_MISMATCH"),
        ("tools", "FAIL_RESPONSE_TOOL_BOUNDARY"),
        ("unexpected_output", "FAIL_RESPONSE_SYNTHETIC_BOUNDARY"),
        ("malformed", "FAIL_SENTINEL_RESPONSE_SCHEMA"),
        ("error", "FAIL_SENTINEL_TRANSPORT"),
    ]:
        sentinel = Sentinel(case)
        resp, state, route, tel = Orch(sentinel).run(request(model_a))
        check(case, resp.terminal_status == status and sentinel.calls == 1
              and tel.retries == 0 and not state.in_execution_wip and not route.complete)
        check("response_diagnostics_redacted", "UNTRUSTED_TEST_DIAGNOSTIC" not in
              json.dumps([asdict(resp), compact_telemetry(resp,tel)]))
    checks.append("six_response_failures_one_attempt_no_fallback")

    orch = Orch()
    for provider in ["openai", "google"]:
        try:
            orch.registry.get(provider)
        except mvp.Blocked:
            check("no_fallback_registry", True)
        else:
            raise AssertionError("no_fallback_registry")
    for changes in [{"model":"unknown"}, {"tools_allowed":["shell"]}, {"content":"private-fixture"}]:
        req = request(model_a)
        for k,v in changes.items():
            setattr(req,k,v)
        before = orch.anthropic.transport.calls
        try:
            orch.anthropic.fake_invoke(req)
        except mvp.Blocked:
            check("direct_adapter_guard", orch.anthropic.transport.calls == before)
        else:
            raise AssertionError("direct_adapter_guard")
    checks.append("no_other_providers_and_direct_adapter_guards")
    resp, _, _, tel = Orch().run(request(model_b, reasoning="HIGH"))
    telemetry = compact_telemetry(resp,tel)
    check("telemetry_boundary", telemetry["model"] == model_b
          and telemetry["reasoning_applied"] == "omitted_unsupported"
          and telemetry["tool_boundary"] == "deny_all"
          and telemetry["secret_access"] == "none")
    return {
        "verdict": PASS, "checks": checks, "assertions": cases,
        "fixture_models": sorted(MODELS), "telemetry": telemetry,
        "mvp_blob": MVP_BLOB, "live_provider_calls": 0,
        "real_model_entitlement_verified": False,
        "provider_api_compatibility": "not_claimed",
        "routing": "not_started", "acceptance": "not_claimed"
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mvp", type=Path)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--demo-model", choices=sorted(MODELS))
    args = parser.parse_args()
    if not args.self_test and args.demo_model is None:
        parser.print_help()
        return
    mvp = load_mvp(args.mvp)
    if args.self_test:
        print(json.dumps(self_test(mvp), ensure_ascii=False, indent=2))
    else:
        Orch, _, request = build_runtime(mvp)
        resp, state, route, tel = Orch().run(request(args.demo_model))
        print(json.dumps({"response": asdict(resp), "run": asdict(state),
                          "routing": asdict(route), "telemetry": compact_telemetry(resp,tel)},
                         ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
