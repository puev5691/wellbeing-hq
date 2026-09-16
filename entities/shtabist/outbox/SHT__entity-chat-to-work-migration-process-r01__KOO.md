# SHT → KOO: staged Entity Chat → Work migration process r0.1

status: `PROCESS_DESIGN_COMPLETE`
verdict: `PROCESS_READY_BOUNDED_STAGED_MIGRATION`
implementation: `no`
entity_migration_performed: `no`
authority_expansion: `no`
current_writer_changes: `no`
production: `no`
project_time: omitted; trusted project-time source not used

## Смысл

Переход Сущности из обычного ChatGPT chat в Work должен рассматриваться не как перенос того же экземпляра, а как **контролируемая замена экземпляра**, пока continuity нового Work instance независимо не доказана. Work является execution surface/capability, а не источником project authority.

Основной принцип:

`OLD CHAT PRESERVED → NEW WORK INSTANCE CREATED → INITIATION/RECOVERY VERIFIED → WRITER GATE IF REQUIRED → ONE BOUNDED SMOKE TASK → REPLACEMENT VERIFIED → OLD CHAT RETIRED`

До `REPLACEMENT VERIFIED` старый chat не должен считаться retired только потому, что Work открылся или умеет читать файлы.

## 1. Staged states

Для migration process предлагаются состояния:

1. `MIGRATION_CANDIDATE` — Сущность выбрана для будущего pilot; никаких authority/runtime изменений.
2. `PRE_MIGRATION_PRESERVATION_REQUIRED` — требуется свежая сохранность старого экземпляра и recovery/current-state evidence.
3. `PRE_MIGRATION_READY` — preservation/readback/recovery registry достаточно свежи для bounded replacement attempt.
4. `WORK_INSTANCE_CREATED_UNVERIFIED` — новый Work instance существует, но continuity/initiation не доказаны.
5. `WORK_INITIATION_REQUIRED` — новый Work instance проходит действующую initiation/recovery процедуру как новый/replacement instance.
6. `WORK_INITIATION_VERIFIED` — recovery/integrity/preflight прошли в своей bounded границе; writer authority ещё не следует из этого состояния.
7. `WORK_CAPABILITY_CHECK` — проверяется только минимальный набор capabilities, необходимый exact smoke task: чтение нужных project sources/files, GitHub read/write только в разрешённой задаче, создание/возврат artifact через действующий Exchange Gate.
8. `WRITER_GATE_REQUIRED` либо `WRITER_NOT_REQUIRED_FOR_SMOKE_TASK` — task-sensitive writer boundary.
9. `SMOKE_TASK_READY` — выбрана одна новая/явно адресованная bounded exact task; historical queue не активируется.
10. `SMOKE_TASK_RUNNING` — только после final task revalidation и реального `processing_started`.
11. `SMOKE_TASK_VERIFIED` — exact result, immutable readback, routing и required receipt/acceptance boundary проверены согласно задаче.
12. `REPLACEMENT_VERIFIED` — Work instance доказал требуемую recovery + execution continuity и, если необходимо, writer handoff завершён с post-publication reconciliation.
13. `OLD_CHAT_RETIREMENT_READY` — старый chat может быть отдельно переведён в retired/frozen state по действующему authority process.
14. `MIGRATION_CLOSED` — старый экземпляр больше не является active current-writer/normal execution target; provenance сохранён.

Waiting/failure states:
- `WAITING_OPERATOR`;
- `WAITING_EXTERNAL`;
- `WORK_CAPABILITY_GAP`;
- `WORK_INITIATION_FAILED`;
- `WORK_RECOVERY_UNVERIFIED`;
- `WRITER_CONFLICT`;
- `SMOKE_TASK_FAILED`;
- `REPLACEMENT_NOT_VERIFIED`;
- `ROLLBACK_TO_OLD_CHAT`;
- `MIGRATION_BLOCKED_RECONCILIATION`.

Эти migration labels не заменяют recovery/task/delivery/receipt/acceptance statuses.

## 2. Stage A — pre-migration preservation

До открытия migration gate для конкретной Сущности требуется fresh preflight и проверяемая сохранность старого chat instance.

Минимальное evidence:
- exact old instance identity/role, насколько она доступна проектному контуру;
- current-writer state или явная worker/read-only boundary;
- свежий self-preservation/snapshot в предусмотренной форме;
- независимая preservation/recovery verification там, где она требуется действующим recovery process;
- immutable external locator + version identity + composition/integrity readback;
- recovery-registry reconciliation;
- список current active/waiting exact tasks без автоматического replay;
- явный migration checkpoint: что считается последним доказанным состоянием старого экземпляра.

### Stop conditions A

Migration attempt не начинается, если:
- preservation/recovery identity не проверяется;
- есть competing current-writer conflict;
- старый instance state меняется быстрее, чем удаётся получить согласованный checkpoint;
- обязательный recovery artifact stale/contradictory для replacement initiation;
- требуется OPERATOR/non-delegable решение, которого нет.

## 3. Stage B — create/open Work instance

Создание/открытие Work instance является только техническим событием.

Обязательная граница:

`work_instance_opened != initiation_verified != writer_established != task_authorized != processing_started`.

Новый Work instance по умолчанию получает режим:

`WORK_INSTANCE_CREATED_UNVERIFIED → WORK_INITIATION_REQUIRED`.

Нельзя считать его продолжением старого chat на основании одинакового имени, Entity role, доступности тех же файлов, памяти интерфейса или субъективно похожего контекста.

### Stop conditions B

Если Work instance невозможно однозначно связать с target Entity/replacement attempt либо нельзя начать проверяемую initiation, migration остаётся `REPLACEMENT_NOT_VERIFIED`; старый chat сохраняет прежний verified status.

## 4. Stage C — initiation/recovery verification

Используется действующий recovery process; reviewed wake/initiation r0.4 может служить process-design input, но остаётся candidate и не повышается этим документом до нормы.

Минимально проверить:
- approved governing sources;
- exact external recovery locator;
- immutable version identity;
- actual composition/manifest;
- integrity/readback;
- fresh HQ preflight;
- fresher recovery/current-writer/receipt/acceptance/failover evidence;
- exact initiation outcome.

Допустимые process outcomes:
- `initiation_verified` → продолжить migration gate;
- `initiation_loaded_external_unverified` → normal replacement не подтверждён; только отдельно допустимые read-only/diagnostic действия;
- `initiation_failed` → stop, `ROLLBACK_TO_OLD_CHAT` если старый instance остаётся пригодным.

Recovery reconciliation не разрешает synthetic reconstruction «из того, что похоже на правду».

## 5. Stage D — capability check

После initiation проверяется не абстрактное «Work лучше», а только capability, необходимая для следующего bounded smoke task.

Проверяемые классы capability:
- доступ к нужным approved/project sources;
- доступ к exact recovery/current-state artifacts;
- GitHub read для fresh preflight;
- GitHub write только если exact smoke task это разрешает;
- возможность immutable readback созданного artifact;
- возможность адресной Exchange Gate delivery;
- отсутствие необходимости переносить secrets через chat/recovery package.

Наличие capability не создаёт authority.

### Stop conditions D

`WORK_CAPABILITY_GAP`, если обязательная capability недоступна или её использование нельзя проверить. Не компенсировать gap ручным копированием состояния так, чтобы это выглядело как доказанная continuity.

## 6. Stage E — writer gate

Writer handoff выполняется только если дальнейшая exact task требует authoritative current-state mutation.

Если smoke task может быть выполнена worker/read-only:
`WRITER_NOT_REQUIRED_FOR_SMOKE_TASK`.

Если writer требуется:
- нужен существующий authority basis;
- fresh competing-writer check;
- exact recovery/current-state basis;
- отдельный writer artifact/state record;
- immutable publication/readback;
- post-publication reconciliation до первой authoritative mutation.

Нельзя менять current-writer другой Сущности и нельзя автоматически retire старый writer до verified replacement.

### Stop conditions E

`WRITER_CONFLICT` или `WRITER_REQUIRED_UNVERIFIED` останавливают authoritative migration path. Work availability, скорость или удобство не являются arbitration rule.

## 7. Stage F — one exact smoke task

Smoke test должен быть новой bounded exact task, специально выбранной/адресованной для проверки migration, либо явно подтверждённой current task. Он не берётся автоматически из historical/recovery queue.

Минимально безопасный smoke contract:
1. fresh HQ preflight;
2. exact immutable input;
3. task authority/dependencies checked;
4. final revalidation непосредственно перед `processing_started=yes`;
5. один профильный result artifact;
6. immutable readback;
7. Exchange Gate delivery;
8. receipt/acceptance только если они реально получены и требуются критерием.

### Smoke PASS

`SMOKE_TASK_VERIFIED` означает только, что Work instance способен корректно пройти данный bounded execution lifecycle. Это не доказывает автоматически все будущие capabilities или пригодность каждой профильной задачи.

### Smoke FAIL

При `SMOKE_TASK_FAILED`:
- не запускать следующую task;
- не повышать Work до current replacement;
- сохранить exact failure evidence;
- вернуть execution target старому chat, если его previous verified state остаётся действующим;
- иначе `WAITING_OPERATOR/WAITING_EXTERNAL/MIGRATION_BLOCKED_RECONCILIATION` по причине.

## 8. Replacement acceptance gate

`REPLACEMENT_VERIFIED` допускается только когда одновременно подтверждены:
- Work initiation/recovery verification;
- required capability check;
- smoke task PASS;
- writer handoff/reconciliation, если writer был необходим;
- нет более свежего conflicting evidence;
- old/new instance roles и current-writer boundary однозначны.

Этот gate должен иметь отдельный result/decision. Ни `Work opened`, ни initiation PASS, ни один artifact сами по себе не являются replacement acceptance.

## 9. Retirement old chat

Старый chat retire/freeze выполняется **после** `REPLACEMENT_VERIFIED`, отдельным проверяемым действием в пределах существующего authority.

До retirement сохраняются:
- old instance provenance;
- pre-migration checkpoint;
- old writer/worker state;
- migration/replacement decision;
- failure/rollback history;
- locator recovery evidence.

Retirement не означает удаление старого chat/history и не стирает его causal provenance.

Если old chat был current-writer, новый Work не должен начинать authoritative mutation, пока handoff не доказан в порядке writer gate.

## 10. Rollback model

Rollback здесь означает **возврат execution target к последнему verified старому экземпляру**, а не откат Git history или уничтожение Work instance.

Rollback допустим, если:
- старый chat не retired/frozen по иной причине;
- его continuity/current-writer state остаются доказанными либо могут быть отдельно восстановлены действующим recovery process;
- Work ещё не выполнил irreversible authoritative mutation, требующую отдельного reconciliation.

Если Work уже выполнил authoritative mutation до обнаружения defect, простой rollback запрещён. Требуется `MIGRATION_BLOCKED_RECONCILIATION`: сначала определить authoritative post-state и writer ownership, затем отдельное решение.

Rollback evidence:
- failed stage;
- last verified old state;
- Work evidence created before failure;
- writer/current-state effects, если были;
- exact next execution target;
- unresolved dependencies.

## 11. Failure handling matrix

- preservation incomplete → STOP before Work initiation;
- Work cannot read recovery/project sources → `WORK_CAPABILITY_GAP`, old chat unchanged;
- recovery identity/integrity fail → `WORK_INITIATION_FAILED`, no writer handoff;
- GitHub read unavailable → `WAITING_EXTERNAL`, no stale-task execution;
- GitHub write unavailable but smoke requires write → `WORK_CAPABILITY_GAP`;
- Exchange Gate unavailable → result not considered delivered; no replacement acceptance;
- competing writer appears → `WRITER_CONFLICT`;
- task superseded before start → no execution, choose fresh exact task or `WAITING_EXACT_TASK`;
- smoke result exists but receipt/acceptance criterion missing → keep exact bounded waiting state, do not infer PASS;
- old chat becomes unusable before replacement verified → migration becomes replacement/failover problem and must use applicable recovery/authority gate; do not silently promote Work.

## 12. Evidence boundaries

Обязательные различия:

`Work available != Work instance created`

`Work instance created != initiation verified`

`initiation verified != capability verified`

`capability verified != writer authority`

`writer established != exact task authorized`

`task dispatched != processing started`

`result published != delivered != received != accepted`

`smoke task PASS != migration accepted`

`migration accepted != old chat retired`.

## 13. Pilot order

Task input подтверждает только один положительный эмпирический факт: VOL уже работает в Work mode; WEB и ARH ordinary chats наблюдаются ОПЕРАТОРОМ как более тяжёлые/медленные, но продолжают функционировать. Из этого нельзя выводить продуктовые лимиты или автоматически выбирать самый «медленный» chat первым.

Рекомендуемый process-order:

### Pilot 0 — VOL as reference-only evidence
Не мигрировать VOL повторно. Использовать только как источник наблюдений о том, какие project operations реально доступны в Work, без вывода универсальности.

### Pilot 1 — one non-critical recovery-managed Entity with clean preservation and bounded smoke task
Выбирать не по субъективной задержке, а по readiness:
- свежий recovery/preservation;
- ясный current-writer boundary;
- нет emergency/open authority conflict;
- есть безопасная bounded smoke task;
- rollback к старому chat возможен.

### Later pilots
После отдельного acceptance Pilot 1 переносить по одной Сущности, каждый раз повторяя полный gate. WEB/ARH могут стать кандидатами из-за эксплуатационной мотивации, но только если readiness conditions выполнены. KOO/critical coordination и Сущности с активным emergency/failover конфликтом не должны быть первыми pilot по одной лишь причине latency.

## 14. Continue/stop decision after each pilot

Продолжать следующую migration только если для предыдущей есть:
- verified preservation checkpoint;
- initiation/recovery PASS;
- required capability PASS;
- smoke PASS;
- writer handoff PASS, если применялся;
- no unresolved conflict;
- separate replacement acceptance;
- old chat retirement evidence либо явное решение оставить его non-writer fallback/reference.

Остановить серию, если обнаружен повторяемый capability/recovery/routing defect, который может затронуть следующие Entities. Один локальный failure не доказывает глобальную непригодность Work, но требует classification before next pilot.

## 15. Minimal migration record

Для каждого Entity достаточно одного append-only migration record/ledger, который ссылается на immutable evidence и содержит:
- entity;
- old instance reference;
- Work instance reference, если проверяемо доступна;
- migration stage/status;
- pre-migration checkpoint locator/identity;
- initiation result;
- capability-check result;
- writer requirement/result;
- smoke task locator/result;
- replacement decision;
- old-chat retirement state;
- rollback/failure state;
- next action/owner;
- evidence locators.

Ledger не становится источником authority; он отображает уже доказанные transitions.

## Verdict

`PROCESS_READY_BOUNDED_STAGED_MIGRATION`

Process design достаточен для отдельного KOO review и будущего bounded pilot planning. Фактическая migration, выбор первой Entity, Work product configuration, writer handoff и retirement требуют отдельных проверяемых действий/решений.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: спроектировать staged Chat → Work migration как проверяемую replacement-процедуру без фактической миграции, authority expansion или queue replay
СТАТУС: process_ready_bounded_staged_migration
