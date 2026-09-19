# SHT: operator handoff invariant for manual Entity activation

status: `PROCESS_RECOMMENDATION_ACTIVE_FOR_SHT_OUTPUT`
scope: `operator-facing handoff after routed result`
authority_change: `no`
automation_change: `no`
project_time: omitted; trusted project-time source not used

## Problem

Если SHT завершил профильный результат, адресно доставил его следующей Сущности, но дальнейшее processing требует ручной активации ОПЕРАТОРОМ, недостаточно сообщить ОПЕРАТОРУ «активируй адресата».

Такой ответ перекладывает на ОПЕРАТОРА уже известную системе маршрутизационную работу: определить адресата, восстановить exact result locator и сформулировать безопасный Resume-First prompt. Это противоречит цели будущего orchestrator, который должен materialize следующий разрешённый шаг естественно.

## SHT operator-handoff invariant

После terminal result + Exchange Gate, если следующий causal step:
- имеет однозначного recipient;
- exact immutable input/result уже известен;
- не требует нового substantive решения ОПЕРАТОРА;
- но реальное Entity processing не доказано и требуется manual activation,

SHT в том же operator-facing ответе обязан вернуть:

1. **АДРЕСАТ** — точную Сущность/чат;
2. **ГОТОВЫЙ PROMPT** — короткий Resume-First prompt, который ОПЕРАТОР может передать без самостоятельной реконструкции;
3. **EXACT INPUT** — locator результата + commit/blob, если применимо;
4. **BOUNDARY** — что адресат должен сделать и чего не должен считать уже доказанным;
5. **STOP CONDITION** — если processing уже началось/результат superseded, prompt не должен создавать duplicate execution.

## Orchestrator mapping

Будущий orchestrator должен materialize тот же handoff автоматически:

`terminal result → verified routing → recipient resolved → exact input frozen → activation prompt/event materialized → activation attempt → processing evidence`.

Инварианты:

- `dispatch/inbox != processing_started`;
- activation prompt не создаёт task authority;
- prompt не создаёт новую task, если существует exact current task/result lineage;
- stale/superseded input запрещает replay;
- manual OPERATOR transfer и automated activation используют одну и ту же causal/state модель;
- если recipient или exact next action неоднозначны, вернуть blocker вместо догадки.

## Current application

Для результата:
`entities/shtabist/outbox/SHT__source-rebuild-r02-process-review__KOO.md`
commit `021619fd4162cf065054095d21f66fb1cf5fa00b`
blob `ed2ed7bc6bbcd96fbf46d1d1ffc22d3cfecdc75a`

следующий recipient: `KOO / КООРДИНАТОР`.

Следующий causal action: обработать verdict `REQUIRES_EDITS_SHT_SOURCE_REBUILD_R02`, reconcile D1–D3, адресовать bounded correction нужному владельцу и не активировать Project Sources/не закрывать два OPERATOR gates из факта этого review.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: убрать ручную реконструкцию следующего activation step с ОПЕРАТОРА и зафиксировать требование для будущего orchestrator
СТАТУС: process_recommendation_active_for_sht_output
