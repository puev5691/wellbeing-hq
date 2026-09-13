# KOO → KOD: Anthropic live HTTP transport/launcher r0.1 — подготовка без live call

status: TASKED_LIVE_TRANSPORT_PREP_NO_LIVE_CALL
provider: Anthropic
target_model: `claude-sonnet-5`
data_class: `D0_SYNTHETIC` only
live_api_call: no
real_credentials: no
credits_purchase: no
production: no
project_time: omitted; trusted project-time source not used

## Основание

Принятый adapter:
`entities/koder/outbox/KOD__anthropic-direct-adapter-r01__KOO.md`
commit `1fece27e9a35954a55b8225adbcfa7c38d702dfb`
verdict `PASS_ANTHROPIC_DIRECT_ADAPTER_READY_FOR_D0_LIVE_GATE`.

KOO receipt:
`routes/receipts/KOD__anthropic-direct-adapter-r01__KOO.receipt.md`
commit `395b58cc54f606dd5ee521e70c32dfa8bcddf968`.

KAN readiness:
`entities/kancelar/outbox/KAN__anthropic-live-d0-access-cost-capabilities__KOO.md`
commit `c84565bec9f602f1e0da4808107a0abd52e18a4b`
verdict `READY_WITH_EXACT_ACCOUNT_PREREQUISITES`.

## Priority / serialization

Это активная KOD-полоса.
В этот же проход не брать:
- static preview E1 evidence alignment;
- activation-lineage schema F1/F2 structural correction;
- ARH sender-registry sanitation.
Они сохранены в KOO serialized queue.

## Задача

Подготовить отдельно проверяемый live-capable HTTP transport/launcher для exact direct Anthropic Messages route, но НЕ выполнять реальный сетевой вызов.

Будущий route:
`local gateway → POST https://api.anthropic.com/v1/messages → claude-sonnet-5`.

Требуется:
1. интеграция с принятым r0.1 adapter/policy contract без ослабления fail-closed правил;
2. единственный разрешённый host/path: `https://api.anthropic.com/v1/messages`;
3. auth только через reference/injection contract `ANTHROPIC_API_KEY`; secret value не хранить и не читать в tests/artifacts;
4. явный default-deny live switch; обычный запуск не должен уходить в сеть;
5. tools/search/files/caching/MCP/Managed Agents/code execution/fallback OFF;
6. только `D0_SYNTHETIC` payload и exact `claude-sonnet-5`;
7. timeout/error handling для 401/403/429/5xx/network timeout без auto retry/fallback;
8. live provenance contract: `external_network_used` должен становиться true только после фактической попытки provider request; mock/test путь сохраняет false;
9. никакого raw secret/request auth header в logs/provenance/errors;
10. cost/usage parsing использовать accepted pricing basis как estimate, не billing evidence;
11. deterministic unit/integration tests через mocked/injected HTTP transport only;
12. отдельный `LIVE-GATE-CHECKLIST.md` с точными account/billing/key/model-access prerequisites и одной командой будущего запуска, но без реального ключа и без исполнения.

## Запрещено

Не создавать Anthropic account/workspace/API key.
Не покупать credits.
Не читать OPERATOR secrets.
Не делать live API request.
Не передавать project/private data.
Не включать D1/D2+.
Не deploy production.

## Результат

Package:
`entities/koder/outbox/multi-model-anthropic-live-transport-r01/`

Result:
`entities/koder/outbox/KOD__anthropic-live-transport-r01__KOO.md`

Вердикт:
- `PASS_ANTHROPIC_LIVE_TRANSPORT_READY_FOR_ACCOUNT_GATE`
- либо exact blocker.

Вернуть через Exchange Gate с immutable package readback/tests.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: подготовить последний технический слой перед отдельным account/key/billing/live-D0 gate без сетевого вызова
СТАТУС: tasked_live_transport_prep_no_live_call
