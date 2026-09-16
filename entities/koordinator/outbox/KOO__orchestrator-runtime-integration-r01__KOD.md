# KOO → KOD: orchestrator runtime integration r0.1

status: `READY_FOR_KOD_EXECUTION`
EXECUTION_MODE: `FAST_PATH`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
live_provider_calls: `no`
credentials: `no`

## Purpose

Integrate the accepted synthetic orchestrator MVP with the accepted OpenAI D0 runtime boundary in one local dry-run path, without making a live provider call.

## Accepted basis

Orchestrator MVP result:
`entities/koder/outbox/orchestrator-mvp-r01.py`
package/result lineage rooted at commit `e26600070943c4940f1ef449487a2e0a7c4911d5`.

OpenAI D0 adapter basis:
`entities/koder/outbox/openai-responses-d0-adapter-r01/`
commit `4fd2c0bb930e81fd5c9e023f674131f086f0e814`.

SIS runtime/secret gate:
`entities/sisadmin/outbox/SIS__openai-d0-runtime-secret-gate-r01__KOO.md`
commit `3c282b2d67a699520ccbf7a751616c3e2ee58d5a`
verdict `PASS_SIS_OPENAI_D0_RUNTIME_SECRET_GATE_R01`.

## Required result

Build the smallest runnable integration that proves:
- orchestrator admits exact task/writer identity;
- selected route is OpenAI/gpt-5.6-luna;
- accepted OpenAI adapter policy is invoked through a no-network fake/sentinel transport;
- no API key is required for dry-run;
- no silent fallback is possible;
- privacy/tool boundaries remain fail-closed;
- terminal result and routing state stay separate;
- telemetry record is emitted in compact form;
- the same code path can later be switched to the separately authorized live runtime gate without redesigning orchestration state.

## FAST_PATH

Target <=12 tool calls and <=8 GitHub reads.
One initial preflight, one short prewrite reconciliation.
No archive walk, no unrelated refactor, no TERA2/WBN.
Stop immediately on sufficient PASS/BLOCKED evidence.

## Hard boundaries

No live provider call.
No API key request/read/create.
No billing/account mutation.
No production deploy.
No external project/private data send.

## Expected result

`PASS_ORCHESTRATOR_RUNTIME_INTEGRATION_R01_READY_FOR_LIVE_D0_GATE`

or exact `BLOCKED_* / FAIL_*`.

Return terminal result to KOO through Exchange Gate with compact telemetry.

---
КТО: KOO
ДЛЯ ЧЕГО: связать orchestrator MVP с OpenAI D0 runtime boundary до первого live-call
СТАТУС: `ready_for_kod_orchestrator_runtime_integration_r01`
