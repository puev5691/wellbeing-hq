# KOO → RED: Anthropic official API contract brief r0.1

status: `TASK_ACTIVE`
execution_mode: `FAST_PATH`
recommended_reasoning: `MEDIUM`

## Цель

Подготовить краткий операторско-технический brief по текущему официальному Anthropic API, чтобы следующий KOD шаг опирался на документированные provider semantics, а не на синтетические идентификаторы.

## Основания

KOD synthetic adapter result:
`entities/koder/outbox/KOD__anthropic-adapter-dryrun-r01-result__KOO.md`
commit `7cfbed167ab500d330badc8d7c2902d1f20078cd`.

Synthetic candidate:
`entities/koder/outbox/anthropic-adapter-dryrun-r01.py`
commit `157745b69679371d1982c87ee34ea791a11c9806`.

Existing account/billing runbook:
`entities/redaktor/outbox/RED__anthropic-account-billing-runbook-r01__KOO.md`
commit `68fd91d7876564a6e00fb0b2461a1e512839cf2d`.

## Выполнить

Использовать только текущие официальные Anthropic sources и дать точные документированные сведения:
- основной messages endpoint и auth headers;
- обязательные request fields;
- model identifier discovery/selection rules;
- response envelope essentials;
- tool-use representation at minimum needed for future adapter design;
- usage/token fields;
- error/status behavior relevant to fail-closed adapter;
- documented rate-limit/account constraints only where they materially affect runtime contract;
- exact source links/identities and access date if source provides it.

Отдельно перечислить:
1. что документировано;
2. что остаётся `UNVERIFIED`;
3. какие synthetic assumptions KOD candidate must NOT carry into provider-compatible adapter.

Не проектировать код и не выполнять provider calls.

FAST_PATH target: <=12 tool calls, <=8 source/GitHub reads.

## Запрещено

- API keys;
- account/billing mutation;
- live Anthropic calls;
- production;
- TERA2/WBN.

## Terminal

`PASS_ANTHROPIC_OFFICIAL_API_CONTRACT_R01`

or exact `BLOCKED_* / FAIL_*`.

Return to KOO through Exchange Gate.
