# KOO → KOD: multi-model orchestrator architecture r0.1

status: `READY_FOR_KOD_EXECUTION`
RECOMMENDED_REASONING: `HIGH`
production: `no`
live_provider_calls: `no`
credentials: `no`

## Priority

This task is part of the current top-priority project lane:
OpenAI-first coordination infrastructure for Project WELLBEING, with later bounded use of other AI providers and project tools.

TERA2/WBN is parked/background and must not be resumed by this task.

## Purpose

Design and materialize a provider-neutral multi-model orchestrator candidate using the existing OpenAI Responses D0 adapter/package as the first implemented provider boundary.

OpenAI is the primary coordination/provider layer. First external provider targets for architecture compatibility:
- Anthropic;
- Google.

No live provider call or credential use is authorized.

## Accepted basis

OpenAI D0 adapter result:
`entities/koder/outbox/KOD__openai-responses-d0-adapter-r01-result__KOO.md`
commit `e053746c55f7c8317069ac0bc60f7dcbc5fe66ac`
verdict `PASS_OPENAI_RESPONSES_D0_ADAPTER_READY_FOR_ACCOUNT_GATE`.

OpenAI host preflight:
`entities/sisadmin/outbox/SIS__openai-d0-host-preflight-r01__KOO.md`
verdict `PASS_SIS_OPENAI_D0_HOST_PREFLIGHT_R01`.

## Required candidate

Prepare a tracked candidate architecture/package that defines:
- common provider-neutral request/response envelope;
- provider adapter interface;
- OpenAI adapter integration using the accepted D0 boundary;
- Anthropic adapter contract candidate;
- Google adapter contract candidate;
- routing policy by task class / model capability / cost / latency / privacy boundary;
- explicit reasoning-effort metadata mapping where supported;
- fallback policy that never silently switches provider/model;
- tool-use capability boundary;
- secret injection contract without storing provider keys in repository;
- telemetry: provider/model, tokens if available, latency, retries, estimated cost, task/entity/run_id, tool calls, result;
- separation of orchestration state from provider state;
- terminal-cycle detection and routing-complete distinction;
- compact operator result format.

## Current-design requirements

Use `entities/koordinator/outbox/KOO__execution-observability-notes-r01__OPERATOR.md` as design input, not canon.

Account for:
- `RECOMMENDED_REASONING` / reasoning-effort policy;
- queue/startup/execution/routing/wall latency separation;
- instance admission guard before profile execution;
- WIP_LIMIT_2 execution-cycle semantics;
- external canonical project state in files/GitHub;
- compact transport instead of chat evidence dumps.

## Provider evidence

For Anthropic and Google integration assumptions, use current official provider documentation only. Record exact source locators and distinguish verified current API facts from project candidate choices.

If current official evidence cannot be obtained, keep those adapters as explicit interface stubs and return the exact evidence gap. Do not guess APIs, models, prices or capabilities.

## Hard boundaries

Do not:
- request/create/read provider API keys;
- make authenticated provider calls;
- change billing;
- deploy production runtime;
- resume TERA2/WBN;
- enable silent fallback;
- send project/private data externally.

## Verification / publication

Before terminal PASS:
1. fresh Resume-First preflight;
2. current KOD writer admission check;
3. exact accepted OpenAI adapter readback;
4. candidate architecture/package generation;
5. deterministic/static tests where applicable;
6. manifest/checksum verification;
7. immutable publication/readback;
8. terminal result to KOO through Exchange Gate.

## Expected result

- `PASS_MULTIMODEL_ORCHESTRATOR_ARCH_R01_READY_FOR_REVIEW`, or
- exact `BLOCKED_* / FAIL_*`.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: вернуть главный приоритет проекта к OpenAI-first multi-model coordination infrastructure
СТАТУС: `ready_for_kod_multimodel_orchestrator_arch_r01`
