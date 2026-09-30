# KOO -> SHT: Entity Semantic Bootstrap Profile r0.1 D2-MAP correction-only

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SHT writer:

puev5691/wellbeing-hq@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md

blob:
a019c21cffeb99bb7c387b8fa95a4629137dc6da

Exact current correction successor:

puev5691/wellbeing-hq@1f47de95c6a771e9c67e9599f425b0ffd796a931:
entities/shtabist/outbox/SHT__entity-semantic-bootstrap-profile-r01-D1D3-correction__KOO.md

blob:
e7c5cff2c6bda7673d3bf87c35e25e1126fc3f51

Exact KAN recheck:

puev5691/wellbeing-hq@d952a3c8999d40171d7378f82734a0a921eb018c:
entities/kancelar/outbox/KAN__entity-semantic-bootstrap-profile-r01-D1D3-recheck__KOO.md

blob:
413d1e403032ee87f02213d71cddbbe5205ef16a

terminal:
NEEDS_REWORK_KAN_ENTITY_SEMANTIC_BOOTSTRAP_PROFILE_R01_D1D3_RECHECK

KAN status:
D1 = CLOSED
D2 = PARTIALLY_CLOSED_EXACT_SLOT_MAPPING_RESIDUAL
D3 = CLOSED

Scope:
CORRECTION_ONLY_D2_MAP

Do not reopen D1 or D3.
Do not redesign model.
Do not activate candidate.
Do not start ARH review.

## Exact D2-MAP correction

Modify ONLY the section:

Mandatory normative slot -> exact source basis

Replace broad whole-canon / vague references with the exact source-section bindings below.

Use one exact source-reference index for aliases Core / Roles / Source Loading / Recovery / File Work / Conveyor.

### Source-reference index

Repository:
puev5691/wellbeing-hq

Normative status:
active approved under current source-set.

Core:
entities/koordinator/outbox/project-core-v2_5-approved/project-instructions-core-v2_5-approved.md
blob a42f7dca6a7469a54fa2da24aae0da4e549c9d33

Roles:
entities/koordinator/outbox/source-set-r03-approved/entity-roles-short-v2_4-approved.md
blob 1772339cb74dae8550bfbd2e33401c34a929e911

Recovery:
entities/koordinator/outbox/source-set-r03-approved/entity-state-preservation-and-recovery-canon-v1_6-approved.md
blob 233117e1c9509d730e1f5ec532b1cabe3f786609

File Work:
entities/koordinator/outbox/source-set-r03-approved/file-work-canon-universal-v2_4-approved.md
blob e9c29d62057f34e4f771d6057a36d9b7f72e74c2

Source Loading:
entities/koordinator/outbox/source-set-r03-approved/source-loading-policy-v2_2-approved.md
blob 69eb657f260a019f76e8e707c880ea88c1dfa0bf

Conveyor:
entities/koordinator/outbox/task-conveyor-v1_2-approved/task-conveyor-canon-v1_2-approved.md
blob df7896d867eeeffff506319538fedad938856686

### Exact slot -> semantic basis map

IDENTITY_SEMANTICS:
Core:
- «Границы Сущности, полномочий и прямого взаимодействия»
- «Сохранение состояния и инициация»

ROLE_SEMANTICS:
Roles:
- «Общие понятия и границы»

Note:
specific named role identity remains INSTANCE_BINDING, not general normative invariant.

SOURCE_SEMANTICS:
Core:
- «Источники»

Source Loading:
- §1 «Классы источников»
- §4 «Инициация»
- §5 «Разделение доставки артефактов и task conveyor»

AUTHORITY_SEMANTICS:
Core:
- «Границы Сущности, полномочий и прямого взаимодействия»

Roles:
- «Общие понятия и границы»

RECOVERY_INITIATION_SEMANTICS:
Recovery:
- «Сущность и экземпляр»
- «Обязательная процедура инициации нового чата»
- subsection «Универсальная процедура Wake → Resume / Initiation → Writer Gate → Exact Task»
- «Несколько экземпляров и current-writer»

EVIDENCE_ARTIFACT_SEMANTICS:
Core:
- «Достоверность»
- «Границы Сущности, полномочий и прямого взаимодействия» for UNKNOWN/evidence boundary

File Work:
- §5 «Достоверность важнее скорости»
- §14 «Пакеты»
- §20 «Работа с GitHub и репозиториями»
- §34 «Проверка результата»

Recovery:
- «Artifact reference для значимых зависимостей»
- «Внешнее сохранение»

TASK_ACTIVATION_SEMANTICS:
Conveyor, when applicable:
- §1 «Назначение и граница»
- §2 «Термины»
- §3 «Базовая формула»
- §3 «Инвариант authority конвейера»
- §7 «Resume-First в конвейере»
- §8 «WIP, attempt lineage и дубли»

Core:
- «Доставка артефактов»

DELIVERY_OUTPUT_SEMANTICS:
Core:
- «Доставка артефактов»

File Work:
- §17.1 «Состояния межсущностного артефакта и маршрута»

Conveyor, when applicable:
- §8 «Terminal result и COMPLETED»
- §9 «GitHub и адресная доставка результатов»
- §10 «Manual activation handoff после terminal result»

HUMAN_INTERFACE:
Core:
- «Человекочитаемый интерфейс проекта»

PRECEDENCE_FAIL_CLOSED:
Core:
- «Границы Сущности, полномочий и прямого взаимодействия»
- «Источники»

Source Loading:
- §1.D «Черновики и кандидаты»
- §3 «Специальные правила для текущего корпуса»

Recovery:
- «Универсальная процедура Wake → Resume / Initiation → Writer Gate → Exact Task»

Conveyor, when applicable:
- §7 «Resume-First в конвейере»
- §8 «WIP, attempt lineage и дубли»

## Required invariants

Preserve unchanged:

- NORMATIVE_INVARIANT vs INSTANCE_BINDING separation;
- candidate != active;
- construction order != precedence;
- active source conflict is not resolved by timestamp/order;
- fresh verified current evidence applies only in proven exact scope;
- no synthetic recovery/current-state reconstruction;
- missing mandatory semantic basis -> UNKNOWN -> no PASS.

Do NOT copy canon text into the candidate.
Only exact bindings/index.

Do NOT modify D1.
Do NOT modify D3.
Do NOT change S1-S12 semantics except the exact mapping references necessary for D2-MAP.
Do NOT add loader/runtime behavior.

## Successor requirements

Create one immutable D2-MAP correction successor.

Must include:
- exact predecessor identity;
- exact KAN recheck identity;
- exact D2-MAP diff;
- source-reference index;
- exact slot -> source-section mapping;
- statement D1 and D3 remain closed/unchanged;
- CANDIDATE_NOT_ACTIVE.

Verification:
- no other intentional semantic change;
- mandatory slot mappings resolve unambiguously to exact active source + exact semantic section/basis;
- source identities/blobs match;
- no source activation/effectivity.

Do NOT:
- activate/create Project Source;
- change Recovery Canon;
- change writer/recovery;
- create Entity;
- implement loader/runtime/semantic engine;
- start ARH review;
- touch PKTB D1-D2 lineage;
- replay historical PROMPT.

Expected terminal:

PASS_SHT_ENTITY_SEMANTIC_BOOTSTRAP_PROFILE_R01_D2_MAP_CORRECTION_READY_FOR_KAN_RECHECK

or exact BLOCKED_/FAIL_.

Mandatory RETURN KOO.
Then STOP.
