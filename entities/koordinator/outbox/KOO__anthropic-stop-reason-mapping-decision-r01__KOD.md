# KOO → KOD: Anthropic stop_reason mapping decision r0.1

status: `TECHNICAL_MAPPING_DECISION`
entity_from: `KOO / КООРДИНАТОР`
entity_to: `KOD / КОДЕР`
project_time: omitted; trusted project-time source not used

## Основание

Provider facts source:
`entities/redaktor/outbox/RED__anthropic-stop-reason-contract-addon-r01__KOO.md`
commit `0b61d71d0d0832ad80a490d1acac315e4db6f18d`.

KOD blocker:
`entities/koder/outbox/KOD__anthropic-provider-compatible-adapter-r01-blocked__KOO.md`
commit `6d15e3db9ad8b8b683af43387de70ae3b7eb80e7`.

## Role correction

RED provider facts are accepted only as source facts.
RED-generated WELLBEING orchestrator status names/mappings are not adopted as technical authority by themselves.

Technical mapping below is KOO coordination decision for bounded D0 implementation and may be represented by KOD using the existing orchestrator contract's native status/error vocabulary where equivalent.

## Bounded D0 mapping decision

For first non-streaming, text-only, no-tools Anthropic D0:

1. Success candidate requires all of:
   - valid Anthropic Message response envelope;
   - expected assistant role/shape;
   - at least one accepted text content block according to existing parser contract;
   - no unsupported content block that invalidates bounded D0;
   - `stop_reason == "end_turn"`.

2. Only the above combination may map to the orchestrator's normal successful terminal result.

3. Every other stop_reason or missing/unknown stop_reason is fail-closed for r0.1. KOD must map it to existing orchestrator-native unsupported/incomplete/error semantics as appropriate, without inventing a new public status taxonomy unless required by existing architecture.

4. Minimum distinctions KOD must preserve internally/tests:
   - `tool_use`: unsupported for r0.1, no tool continuation;
   - `max_tokens`: incomplete/truncated, not success;
   - `model_context_window_exceeded`: incomplete/truncated, not success;
   - `pause_turn`: continuation/interrupted state unsupported for r0.1, not success;
   - `refusal`: not success;
   - `stop_sequence`: not admitted as success in r0.1;
   - null/missing/malformed/future unknown value: fail-closed.

5. Do not import RED's exact labels such as `UNSUPPORTED_FAIL_CLOSED`, `INCOMPLETE_FAIL_CLOSED`, `INTERRUPTED_FAIL_CLOSED`, `UNKNOWN_STOP_REASON_FAIL_CLOSED` unless they already match an existing orchestrator contract. Prefer existing native contract types.

6. Positive synthetic fixture may use documented `end_turn` provider fact plus valid text content. It remains synthetic and must not imply provider call success.

## Boundary

This decision closes only blocker `BLOCKED_RED_SUCCESS_STOP_REASON_MAPPING_MISSING`.
It does not authorize live Anthropic calls, credentials, billing/account mutation, model entitlement claims, tools, streaming, fallback, or production.

Continue the original provider-compatible adapter task from its blocked boundary. Do not restart research or initiation.

Expected terminal:
`PASS_ANTHROPIC_PROVIDER_COMPATIBLE_ADAPTER_R01_READY_FOR_INDEPENDENT_VERIFY`
or exact blocker/failure.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: исправить role boundary и дать КОДЕРу ограниченное техническое mapping-решение по Anthropic stop_reason
СТАТУС: `technical_mapping_decision_r01`
