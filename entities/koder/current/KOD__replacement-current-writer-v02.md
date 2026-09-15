# KOD replacement current-writer v0.2

status: `CURRENT_WRITER_ESTABLISHED`
entity: `KOD / КОДЕР`
initiation_status: `initiation_verified`
current_writer_state: `confirmed_replacement_writer`
writer_transfer_performed: `yes`
profile_execution_started: `no`
project_time: omitted; trusted project-time source not used

## Назначение

Эта immutable-запись фиксирует только writer boundary после успешной replacement initiation. Она не запускает никакую профильную KOD-задачу.

## Основание полномочий

KOO decision-gate:
`entities/koordinator/outbox/KOO__KOD-replacement-writer-decision-gate__OPERATOR.md`

KOO gate прямо требовал отдельного явного решения ОПЕРАТОРА и сам authority не создавал.

В текущем взаимодействии ОПЕРАТОР явно решил:
- предыдущий verified KOD current-writer прекращает дальнейшую профильную работу;
- предыдущий writer считается retired для новых KOD mutations;
- новому `initiation_verified` KOD instance разрешено выполнить fresh competing-writer check и, при отсутствии конфликта, установить replacement current-writer;
- после writer establishment требуется остановка и возврат результата KOO;
- профильные задачи автоматически не начинать.

## Initiation provenance

Replacement initiation result:
`entities/koder/outbox/KOD__replacement-initiation-v02-result__KOO.md`
commit `14272b4067069cd044cf10e1affab66858a74b12`
blob `be795983dc744e219db1b408c6d954ca4ff4dbbe`.

Initiation result: `initiation_verified / WAITING_OPERATOR_WRITER_DECISION`.

Canonical recovery:
`puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current`

Independent ARH verification:
`entities/archivarius/outbox/ARH__KOD-emergency-recovery-verification__KOD.md`
commit `78a8f278e3a332bce05e28352e1316ea18f0a13c`
status `PASS_PUBLISHED_CANONICAL_RECOVERY`.

## Fresh competing-writer check

Fresh `puev5691/wellbeing-hq` pre-publication HEAD:
`68aed55a23778cfa7c68a0cdb28ef08a6e3cd308`
message: `KOO: publish replacement initiation v05 result`.

Проверено на этой immutable границе:
- прежний writer marker существует: `entities/koder/current/KOD__initiation-verified-current-writer-v01.md`, blob `92a9e006c37589fee03479a81e4f53608b982ef0`;
- `entities/koder/handoff/` содержит только `.gitkeep`;
- поиск KOD current-writer evidence не обнаружил writer marker новее `b7cdd1cbb28c9f144ca26d23823ba4b42973fd5f`;
- поиск KOD replacement-writer evidence обнаружил только KOO decision-gate preparation `a0c8f70cbe3edd9031ee4881d189639f5a166d98`, а не competing KOD writer;
- отдельного нового KOD retirement evidence до решения ОПЕРАТОРА не было; retirement M365 относится только к экспериментальному контуру, не к KOD writer.

Competing writer verdict:
`NO_NEW_COMPETING_KOD_WRITER_EVIDENCE`.

## Writer transition

Previous writer marker:
`entities/koder/current/KOD__initiation-verified-current-writer-v01.md`
commit создания `b7cdd1cbb28c9f144ca26d23823ba4b42973fd5f`.

С этой записью его operational state для новых KOD mutations:
`RETIRED_BY_EXPLICIT_OPERATOR_DECISION`.

Исторический файл v0.1 не переписывается и сохраняется как provenance. Для новых KOD mutations он superseded этой записью.

Новый instance state:
`CURRENT_WRITER_ESTABLISHED`.

## Жёсткая граница после establishment

Не выполнено и не разрешается автоматически этой записью:
- Telegram Phase1B threading fix;
- TERA2 root-profile;
- любые другие исторические или новые KOD profile tasks;
- deployment, production mutation, credentials handling или live external action.

Следующее профильное действие возможно только по отдельному current task/authority gate после свежего Resume-First preflight.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: установить replacement current-writer после отдельного решения ОПЕРАТОРА и чистого competing-writer check
СТАТУС: `CURRENT_WRITER_ESTABLISHED / PROFILE_WORK_NOT_STARTED`
