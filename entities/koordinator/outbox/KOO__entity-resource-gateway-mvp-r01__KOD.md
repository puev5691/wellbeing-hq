# KOO → KOD: Entity Resource Gateway MVP r0.1

status: TASK
execution_mode: FAST_PATH
priority: TOP_INFRASTRUCTURE

## Goal

Собрать первый provider-neutral Entity Resource Gateway поверх уже существующих и проверенных компонентов, чтобы Сущность могла отправить bounded подзадачу внешней модели и получить проверяемый результат как ресурс, не передавая provider-у writer-authority.

## Basis

- orchestrator MVP/runtime integration already accepted in HQ;
- OpenAI three-model runtime independently verified and final technical gate PASS;
- Anthropic provider-compatible adapter candidate commit `4186f47f350133495ac21ca4cf758e481850d81c`;
- independent SIS verdict commit `d92b3a9ba5abc0c4d1f03169425fb2dcb6e6cd6a`: `PASS_SIS_ANTHROPIC_PROVIDER_COMPATIBLE_ADAPTER_R01`;
- operator priority commit `9ab3205f99bfb4865a11369b34b92c8d0f8f582e`.

## Required MVP

Create isolated gateway/library with explicit request/response contract:

`EntityRequest → policy/authority gate → provider selection → orchestrator/provider adapter → ResourceResult`

Minimum request fields:
- requesting entity id/role;
- exact task/purpose;
- provider/model selection or provider-neutral policy;
- data class/privacy class;
- allowed capabilities;
- external-send flag;
- provenance/source refs;
- bounded prompt/input payload;
- result acceptance policy.

Minimum result fields:
- provider/model actually used;
- technical run status;
- bounded result payload;
- provenance/run id;
- usage if provider returned documented usage;
- error/blocker;
- no claim of project acceptance;
- no change to caller writer-authority.

Must support synthetic/no-network execution paths for:
- OpenAI adapter;
- Anthropic adapter;
- provider-unavailable / provider-unregistered;
- model mismatch;
- privacy/tool/external-send rejection.

Do not:
- make live provider calls;
- read/create credentials;
- change account/billing;
- deploy production/runtime;
- grant provider or gateway writer authority;
- auto-apply returned result to project state;
- auto-dispatch externally;
- alter Telegram Phase 1B or facilitator core;
- touch TERA2/WBN.

Expected terminal:
`PASS_ENTITY_RESOURCE_GATEWAY_MVP_R01_READY_FOR_INDEPENDENT_VERIFY`
or exact blocker.

Return immutable candidate + tests + exact integration boundary + Exchange Gate route to KOO, then stop.
