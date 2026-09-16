# KOO → KOD: orchestrator MVP r0.1

status: `READY_FOR_KOD_EXECUTION`
EXECUTION_MODE: `FAST_PATH`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
live_provider_calls: `no`
credentials: `no`

## Purpose

Materialize a minimal runnable provider-neutral orchestrator MVP from the accepted architecture r0.1, using synthetic/fake transports only.

## Accepted basis

Architecture result:
`entities/koder/outbox/KOD__multimodel-orchestrator-architecture-r01__KOO.md`
commit `3b3f1ab607d3446245497c28de8a4c642ffa7715`
verdict `PASS_MULTIMODEL_ORCHESTRATOR_ARCH_R01_READY_FOR_REVIEW`.

OpenAI adapter basis:
`entities/koder/outbox/KOD__openai-responses-d0-adapter-r01-result__KOO.md`
commit `e053746c55f7c8317069ac0bc60f7dcbc5fe66ac`.

## Scope

Implement the smallest runnable MVP that demonstrates:
- TaskAdmission;
- common request/response envelope;
- provider adapter registry/interface;
- OpenAI adapter wrapper on accepted D0 boundary but fake transport only;
- Anthropic/Google interface stubs, no live transport;
- routing policy with explicit provider/model selection;
- no silent fallback;
- reasoning metadata mapping status;
- tool boundary default deny;
- run state vs routing state;
- terminal detection;
- compact telemetry;
- compact operator result.

## Required synthetic tests

At minimum:
1. PASS synthetic OpenAI route;
2. BLOCKED privacy boundary;
3. BLOCKED unsupported capability;
4. BLOCKED no-silent-fallback case;
5. terminal-result leaves execution WIP while routing remains separate;
6. reasoning mapping supported/omitted/rejected state handling.

## FAST_PATH

- one fresh preflight;
- one current-writer admission check;
- target <=12 tool calls / <=8 GitHub reads unless concrete reason;
- no unrelated refactor;
- no provider pricing research;
- no extra docs beyond what is required to run/test/review;
- stop at first sufficient terminal evidence.

## Hard boundaries

NO live provider calls.
NO API keys.
NO billing changes.
NO production deploy.
NO external project/private data.
NO TERA2/WBN.

## Expected result

`PASS_ORCHESTRATOR_MVP_R01_READY_FOR_RUNTIME_REVIEW`

or exact `BLOCKED_* / FAIL_*`.

Return terminal result to KOO through Exchange Gate with compact telemetry.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: перевести multi-model architecture в runnable synthetic MVP
СТАТУС: `ready_for_kod_orchestrator_mvp_r01`
