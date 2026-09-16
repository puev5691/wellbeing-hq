# КООРДИНАТОР — рабочая очередь v0.14

Статус: `CURRENT_OPERATOR_QUEUE`
Режим: `WIP_LIMIT_2`
Проектное время не указывается.

## Приоритет

Главный приоритет проекта:
OpenAI-first coordination infrastructure → multi-model orchestration → подключение Anthropic/Google → инструменты и автоматизация Сущностей проекта БЛАГОПОЛУЧИЕ.

TERA2/WBN: `PARKED_BACKGROUND`.
Новые TERA2/WBN execution cycles не запускать без отдельного решения ОПЕРАТОРА.

## ACTIVE SLOT 1 — KOD / multi-model orchestrator architecture r0.1

Exact task:
`entities/koordinator/outbox/KOO__multimodel-orchestrator-architecture-r01__KOD.md`
commit `0e8af1f56e1355d7a04fe7412ed99582b1053bd6`.

`RECOMMENDED_REASONING: HIGH`.

Цель: provider-neutral orchestrator с OpenAI как первым реализованным и основным координационным provider boundary; Anthropic и Google как следующие adapter targets.

No live calls, no credentials, no billing mutation, no production deployment.

## ACTIVE SLOT 2 — RED / provider capabilities and pricing brief r0.1

Exact task:
`entities/koordinator/outbox/KOO__provider-capabilities-pricing-brief-r01__RED.md`
commit `732e29580da8edba837cf67540e0312bf67c7fdb`.

`RECOMMENDED_REASONING: MEDIUM`.

Цель: операторский русскоязычный brief по текущим API-возможностям, ценам, ограничениям и account dependencies OpenAI / Anthropic / Google на основе только официальных актуальных источников.

## WAITING / EXTERNAL GATES

OpenAI live D0 ждёт отдельного внешнего gate:
- account/billing readiness;
- valid API key created by OPERATOR outside project artifacts;
- secret-safe injection path;
- explicit authorization for exactly one bounded synthetic live call.

Telegram Phase1B остаётся `BLOCKED_PRIVILEGE_REQUIRED` до отдельного privilege/provisioning решения.

## PARKED

- TERA2/WBN root-profile/genesis line after KOD r0.3 correction;
- SHD/SIS runtime/genesis follow-ups;
- recovery canon v1.5 operator gate;
- Chat→Work mass migration;
- ARH/WEB replacement;
- retired-instance lifecycle study continues background only and consumes no WIP slot.

## Operating rule

Новая профильная задача должна проходить instance admission guard before execution.
WIP считается по незакрытым execution cycles.
Blocked/waiting освобождает слот.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: вернуть фактическую очередь к приоритету OpenAI-first multi-model coordination infrastructure
СТАТУС: `CURRENT_OPERATOR_QUEUE_V14`
