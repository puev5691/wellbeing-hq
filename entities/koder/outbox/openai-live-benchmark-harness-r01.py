#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Callable
import argparse, hashlib, json, time

VERDICT = "PASS_OPENAI_LIVE_BENCHMARK_HARNESS_R01_READY_FOR_ACCOUNT_GATE"
TASK_PATH = "entities/koordinator/outbox/KOO__openai-live-benchmark-harness-r01__KOD.md"
TASK_COMMIT = "5afc12021a213723f5bef8d69713018e4016c73a"
TASK_BLOB = "c6f2ba5aea41baf613335be71db8958765b518e1"
WRITER_BLOB = "23f20f04504c65497c154c099d8090cde11fba83"
PROVIDER = "openai"
MODELS = ("gpt-5.6-luna", "gpt-5.6-terra", "gpt-5.6-sol")
LIVE_AUTHORITY_TOKEN = "EXPLICIT_BENCHMARK_LIVE_GATE_R01"

PRICE_SNAPSHOT = {
    "snapshot_id": "openai-gpt56-text-pricing-r01-2026-09-16",
    "currency": "USD",
    "unit": "per_1m_text_tokens",
    "scope": "standard text token pricing; benchmark inputs must remain <=272k tokens; no tool fees or cache-write charges",
    "sources": [
        "https://developers.openai.com/api/docs/models/gpt-5.6-luna",
        "https://developers.openai.com/api/docs/models/gpt-5.6-terra",
        "https://developers.openai.com/api/docs/models/gpt-5.6-sol",
    ],
    "models": {
        "gpt-5.6-luna": {"input": 0.20, "cached_input": 0.02, "output": 1.20},
        "gpt-5.6-terra": {"input": 2.00, "cached_input": 0.20, "output": 12.00},
        "gpt-5.6-sol": {"input": 4.00, "cached_input": 0.40, "output": 20.00},
    },
}
PRICE_SNAPSHOT_ID = PRICE_SNAPSHOT["snapshot_id"]

@dataclass(frozen=True)
class BenchmarkCase:
    case_id: str
    task_class: str
    prompt: str
    fixture_output: str
    evaluator: str

CASES = (
    BenchmarkCase("extract-01", "extraction/classification", "Извлеки status и priority из: status=ready; priority=high. Ответ JSON.", '{"priority":"high","status":"ready"}', "exact_json"),
    BenchmarkCase("summary-ru-01", "concise Russian operator summary", "Сожми в одну строку: сервис работает, сеть не использовалась, ключ не запрашивался.", "Сервис работает; сеть не использовалась; ключ не запрашивался.", "ru_summary_facts"),
    BenchmarkCase("reason-01", "bounded coding/reasoning", "Вычисли результат Python-выражения sum(x*x for x in [1,2,3]). Ответ только числом.", "14", "exact_text"),
    BenchmarkCase("json-01", "structured JSON output", "Верни JSON с полями ok=true, count=3 без иных полей.", '{"count":3,"ok":true}', "exact_json"),
)

DRY_USAGE = {
    "extract-01": (18, 9),
    "summary-ru-01": (24, 16),
    "reason-01": (23, 2),
    "json-01": (17, 9),
}

CURRENT_ACCEPTED_RUNTIME_MODEL = "gpt-5.6-luna"
CURRENT_RUNTIME_GAPS = {
    "gpt-5.6-luna": None,
    "gpt-5.6-terra": "requires_bounded_openai_adapter_model_policy_extension_before_live_run",
    "gpt-5.6-sol": "requires_bounded_openai_adapter_model_policy_extension_before_live_run",
}

@dataclass
class RunRecord:
    provider: str
    model: str
    task_class: str
    case_id: str
    input_tokens: int | None
    output_tokens: int | None
    provider_request_id: str | None
    provider_latency_ms: float | None
    harness_latency_ms: float | None
    retries: int
    result_status: str
    estimated_cost_usd: float | None
    eval: dict[str, Any]
    price_snapshot_id: str
    usage_source: str
    network_used: bool


def canonical(v: Any) -> str:
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def snapshot_sha256() -> str:
    return hashlib.sha256(canonical(PRICE_SNAPSHOT).encode()).hexdigest()


def estimate_cost(model: str, input_tokens: int | None, output_tokens: int | None) -> float | None:
    if input_tokens is None or output_tokens is None:
        return None
    p = PRICE_SNAPSHOT["models"][model]
    return round((input_tokens * p["input"] + output_tokens * p["output"]) / 1_000_000, 10)


def evaluate(case: BenchmarkCase, output: str) -> dict[str, Any]:
    if case.evaluator == "exact_text":
        return {"deterministic": True, "pass": output.strip() == case.fixture_output}
    if case.evaluator == "exact_json":
        try:
            return {"deterministic": True, "pass": json.loads(output) == json.loads(case.fixture_output)}
        except Exception:
            return {"deterministic": True, "pass": False}
    if case.evaluator == "ru_summary_facts":
        low = output.lower()
        facts = ["работает", "сеть не использовалась", "ключ не запрашивался"]
        return {"deterministic": True, "pass": all(x in low for x in facts) and len(output) <= 120, "max_chars": 120}
    return {"deterministic": False, "pass": None}


def select_models(raw: str) -> list[str]:
    wanted = list(MODELS) if raw == "all" else [x.strip() for x in raw.split(",") if x.strip()]
    if not wanted or any(x not in MODELS for x in wanted):
        raise SystemExit("BLOCKED_EXPLICIT_MODEL_SELECTION_REQUIRED")
    return wanted


def dry_run(models: list[str]) -> list[RunRecord]:
    records: list[RunRecord] = []
    for model in models:
        for case in CASES:
            start = time.monotonic_ns()
            inp, out = DRY_USAGE[case.case_id]
            result = case.fixture_output
            elapsed = (time.monotonic_ns() - start) / 1_000_000
            records.append(RunRecord(
                provider=PROVIDER, model=model, task_class=case.task_class, case_id=case.case_id,
                input_tokens=inp, output_tokens=out,
                provider_request_id=f"dryrun:{model}:{case.case_id}",
                provider_latency_ms=None, harness_latency_ms=elapsed, retries=0,
                result_status="PASS_DRY_RUN_FIXTURE", estimated_cost_usd=estimate_cost(model, inp, out),
                eval=evaluate(case, result), price_snapshot_id=PRICE_SNAPSHOT_ID,
                usage_source="synthetic_fixture_not_provider_usage", network_used=False,
            ))
    return records


def live_plan(models: list[str], authority: str | None) -> dict[str, Any]:
    if authority != LIVE_AUTHORITY_TOKEN:
        return {"status": "BLOCKED_LIVE_AUTHORITY_REQUIRED", "network_used": False}
    gaps = {m: CURRENT_RUNTIME_GAPS[m] for m in models if CURRENT_RUNTIME_GAPS[m]}
    if gaps:
        return {"status": "BLOCKED_LIVE_MODEL_POLICY_EXTENSION_REQUIRED", "model_gaps": gaps, "network_used": False}
    return {
        "status": "READY_FOR_SEPARATE_ACCEPTED_LIVE_RUNTIME_BACKEND",
        "model": "gpt-5.6-luna",
        "network_used": False,
        "note": "This harness does not read keys or perform network I/O; a separately authorized runtime backend must execute the live call.",
    }


def summary(records: list[RunRecord]) -> dict[str, Any]:
    return {
        "verdict": VERDICT,
        "provider": PROVIDER,
        "models": sorted({r.model for r in records}),
        "task_classes": [c.task_class for c in CASES],
        "runs": len(records),
        "all_eval_pass": all(r.eval.get("pass") is True for r in records),
        "network_calls": 0,
        "api_keys_read_or_stored": 0,
        "silent_fallback": False,
        "price_snapshot_id": PRICE_SNAPSHOT_ID,
        "price_snapshot_sha256": snapshot_sha256(),
        "current_live_runtime_model": CURRENT_ACCEPTED_RUNTIME_MODEL,
        "live_model_gaps": CURRENT_RUNTIME_GAPS,
        "records": [asdict(r) for r in records],
    }


def self_test() -> dict[str, Any]:
    records = dry_run(list(MODELS))
    s = summary(records)
    assert len(records) == 12 and s["all_eval_pass"]
    assert all(r.network_used is False and r.retries == 0 for r in records)
    assert len({r.model for r in records}) == 3
    assert {r.task_class for r in records} == {c.task_class for c in CASES}
    assert all(r.estimated_cost_usd is not None for r in records)
    assert live_plan(["gpt-5.6-luna"], None)["status"] == "BLOCKED_LIVE_AUTHORITY_REQUIRED"
    assert live_plan(["gpt-5.6-luna", "gpt-5.6-terra"], LIVE_AUTHORITY_TOKEN)["status"] == "BLOCKED_LIVE_MODEL_POLICY_EXTENSION_REQUIRED"
    assert live_plan(["gpt-5.6-luna"], LIVE_AUTHORITY_TOKEN)["status"] == "READY_FOR_SEPARATE_ACCEPTED_LIVE_RUNTIME_BACKEND"
    return {
        "verdict": VERDICT,
        "checks": 8,
        "dry_run_records": len(records),
        "all_eval_pass": s["all_eval_pass"],
        "price_snapshot_id": PRICE_SNAPSHOT_ID,
        "price_snapshot_sha256": s["price_snapshot_sha256"],
        "live_provider_calls": 0,
        "api_keys": 0,
        "live_model_gaps": CURRENT_RUNTIME_GAPS,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=("dry_run", "live_plan"), default="dry_run")
    ap.add_argument("--models", default="all")
    ap.add_argument("--live-authority")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        print(json.dumps(self_test(), indent=2, sort_keys=True, ensure_ascii=False)); return
    models = select_models(args.models)
    if args.mode == "dry_run":
        print(json.dumps(summary(dry_run(models)), indent=2, sort_keys=True, ensure_ascii=False)); return
    print(json.dumps(live_plan(models, args.live_authority), indent=2, sort_keys=True, ensure_ascii=False))

if __name__ == "__main__": main()
