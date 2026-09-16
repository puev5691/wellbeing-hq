# KOO → SIS: OpenAI D0 runtime/secret gate r0.1

status: `READY_FOR_SIS_EXECUTION`
EXECUTION_MODE: `FAST_PATH`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
live_provider_calls: `no`
api_key_value: `must_not_be_present`
billing_change: `no`
privileged_mutation: `no`

## Purpose

Prepare the exact host/runtime/secret-injection boundary needed for one future separately authorized OpenAI D0 synthetic live call, without using or requesting the key and without making the live call.

## Accepted basis

OpenAI D0 adapter:
`entities/koder/outbox/KOD__openai-responses-d0-adapter-r01-result__KOO.md`
commit `e053746c55f7c8317069ac0bc60f7dcbc5fe66ac`.

OpenAI host preflight:
`entities/sisadmin/outbox/SIS__openai-d0-host-preflight-r01__KOO.md`
verdict `PASS_SIS_OPENAI_D0_HOST_PREFLIGHT_R01`.

Preferred host: `ruvds-xnqc6`.

## Scope

Prepare and verify only:
- user-owned runtime directory/path for D0 runner;
- exact immutable adapter/package readback;
- runtime launch command/template with live execution disabled by default;
- secret-injection mechanism for `OPENAI_API_KEY` that leaves no secret in repo, command history, logs, telemetry or result artifacts;
- explicit `OPENAI_LIVE_D0=EXPLICIT_D0_LIVE`-style gate or equivalent fail-closed switch;
- cleanup contract for any synthetic temp/runtime files created by this preparation;
- one dry-run/fake-transport or no-network validation proving the gate refuses live execution when key/live switch are absent;
- exact smallest operator actions still required before one live D0 call.

## FAST_PATH

- one fresh preflight;
- one current-writer admission check;
- target <=12 tool calls / <=8 GitHub reads unless concrete reason;
- no repeated host inventory already proven by prior preflight;
- no unrelated repair;
- stop when runtime/secret gate is demonstrably ready or exact blocker is known.

## Hard boundaries

DO NOT request/read/create/publish API key.
DO NOT perform authenticated OpenAI request.
DO NOT change billing/account.
DO NOT use sudo/root.
DO NOT deploy production service.
DO NOT send project/private data externally.

## Expected result

`PASS_SIS_OPENAI_D0_RUNTIME_SECRET_GATE_R01`

or exact `BLOCKED_* / FAIL_*`.

Return terminal result to KOO through Exchange Gate with compact telemetry and exact remaining operator dependencies.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: довести OpenAI D0 до безопасного live-ready gate без ключа и без live call
СТАТУС: `ready_for_sis_openai_d0_runtime_secret_gate_r01`
