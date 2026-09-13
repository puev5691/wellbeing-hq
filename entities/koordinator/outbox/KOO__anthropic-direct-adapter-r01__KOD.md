# KOO → KOD: Anthropic direct adapter r0.1

status: TASKED_CREDENTIAL_FREE_ADAPTER_PREP
provider: Anthropic
target_model: `claude-sonnet-5`
data_class: `D0_SYNTHETIC` only
live_api_call: no
credentials: no
production: no
project_time: omitted; trusted project-time source not used

## Основание

Решение ОПЕРАТОРА: Anthropic выбран первым внешним provider route.

KAN readiness:
`entities/kancelar/outbox/KAN__anthropic-live-d0-access-cost-capabilities__KOO.md`
commit `c84565bec9f602f1e0da4808107a0abd52e18a4b`
verdict `READY_WITH_EXACT_ACCOUNT_PREREQUISITES`.

KOO acceptance:
`routes/receipts/KAN__anthropic-live-d0-access-cost-capabilities__KOO.receipt.md`
commit `b9de93170330c0af564eda99f5ce66225132bd0c`.

Existing local gateway mock:
`entities/koder/outbox/KOD__multi-model-gateway-mock-r01-result__KOO.md`
commit `cb2f21c3ee639fc58a04dfb043826d1ee9581be4`
blob `2bbf4b1562e29eedb665eda383698ff8ca6d0064`.

## Priority / serialization

This task is the active KOD lane.
Do not in the same pass process:
- WEB E1 static-preview evidence alignment;
- ARH sender-registry sanitation finding.
They remain preserved in:
`entities/koordinator/current/KOO__kod-serialized-queue-v01.md`
commit `69bff66d3ab776f91a31ab66d0391a4ba588a695`.

## Task

Prepare a credential-free, network-disabled Anthropic direct adapter/harness that can later be activated for one authorized `D0_SYNTHETIC` live pilot.

Target route after later authorization:
`local gateway → https://api.anthropic.com/v1/messages → claude-sonnet-5`.

Required now:
1. request envelope builder for exact direct Messages route;
2. exact model default `claude-sonnet-5`;
3. D0-only policy guard integration;
4. tools/search/files/caching/MCP/Managed Agents/code execution OFF;
5. no fallback and no alternate provider;
6. auth interface only through environment/secret injection contract, e.g. `ANTHROPIC_API_KEY`; never store a secret value;
7. mocked transport only for tests; real network call forbidden in this task;
8. response parser for minimal text response plus usage/token metadata;
9. provenance fields: provider, model, request hash, response hash, input/output usage, adapter version, external-network-used=false for this task;
10. cost-estimate helper using current accepted Sonnet 5 standard pricing `$2 / MTok input`, `$10 / MTok output`, clearly marked estimate derived from returned usage;
11. fail closed on non-D0, tools, caching, fallback, unknown model, credential value embedded in task/config, project/private locator or production mutation request;
12. deterministic tests for success/error/429/auth-missing/malformed-response paths using mocked responses only.

## Live-pilot boundary

Do NOT:
- create Anthropic account/workspace/API key;
- buy credits;
- read OPERATOR secrets;
- make any request to Anthropic;
- transmit any project data;
- enable D1/D2+;
- enable tools/search/files/MCP/code execution;
- deploy production service.

The later live gate requires separate evidence of OPERATOR account/billing/key readiness and separate KOO authorization.

## Output

Package:
`entities/koder/outbox/multi-model-anthropic-adapter-r01/`

Result:
`entities/koder/outbox/KOD__anthropic-direct-adapter-r01__KOO.md`

Required verdict:
- `PASS_ANTHROPIC_DIRECT_ADAPTER_READY_FOR_D0_LIVE_GATE`
- or exact blocker.

Return through Exchange Gate with immutable package readback and tests.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: подготовить техническую сторону первого Anthropic D0 пилота без ключа, денег и live network call
СТАТУС: tasked_credential_free_adapter_prep
