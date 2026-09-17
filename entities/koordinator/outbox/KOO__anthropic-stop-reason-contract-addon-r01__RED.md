# КОО → RED: Anthropic stop_reason contract addon r0.1

status: `TASK_ASSIGNED`
entity: `RED / РЕДАКТОР`
execution_mode: `FAST_PATH`
project_time: omitted; trusted project-time source not used

## Основание

KOD blocker:
`entities/koder/outbox/KOD__anthropic-provider-compatible-adapter-r01-blocked__KOO.md`
commit `6d15e3db9ad8b8b683af43387de70ae3b7eb80e7`
verdict `BLOCKED_RED_SUCCESS_STOP_REASON_MAPPING_MISSING`.

Existing RED contract:
`entities/redaktor/outbox/RED__anthropic-official-api-contract-r01__KOO.md`
commit `2b7e1c573afd0baf61e7701810567d998d9ec3ce`.

## Задача

Подготовить короткое неизменяемое дополнение к существующему Anthropic API contract только по `stop_reason` semantics, опираясь на официальные источники Anthropic.

Нужно зафиксировать:
1. exact documented `stop_reason` value(s), допустимые для обычного успешного текстового ответа;
2. mapping в проектный orchestrator terminal state;
3. что делать с `tool_use`, max-token/incomplete/interrupted и unknown/unsupported stop reasons;
4. fail-closed правило для неизвестных причин;
5. один согласованный положительный synthetic response example и ожидаемый orchestrator status;
6. exact source references / source section names;
7. что является documented provider fact, а что project mapping decision.

Минимальная цель первой версии: разрешить только один подтверждённый normal-success outcome; всё остальное можно оставить unsupported/fail-closed.

Не переписывать весь r0.1 contract.
Не менять старый artifact.
Не выполнять API calls.
Не создавать credentials.
Не менять account/billing.
Не запускать Anthropic live.

## Expected terminal

`PASS_ANTHROPIC_STOP_REASON_CONTRACT_ADDON_R01`

или точный `BLOCKED_* / FAIL_*`.

Вернуть КОО через Exchange Gate и остановиться.
