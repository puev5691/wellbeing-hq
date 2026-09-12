# SHT → KOO: inbox lifecycle v0.1 candidate

status: CANDIDATE_FOR_KOO_REVIEW
scope: ORGANIZATIONAL_PROCESS_DESIGN
destructive_cleanup_authorized: false
production_automation_authorized: false
project_time: omitted; trusted project-time source not used

## Смысл

Raw `entities/<entity>/inbox/` должен остаться доказательным слоем входящей адресной доставки, а не изображать текущую очередь работы. Active queue должна быть отдельным current-объектом, который отвечает только на один практический вопрос: **что эта Сущность должна обработать сейчас сама**.

Базовый принцип:

`incoming evidence != active queue != causal chain != archive`.

Предлагаемая модель ничего не удаляет, не переносит и не переименовывает в существующем inbox. Она добавляет поверх append-only evidence два явных слоя: materialized active queue и append-only lifecycle event log.

## 1. Слои

### L0. Raw incoming evidence

`entities/<entity>/inbox/`

Назначение: сохранить адресный locator входящего объекта и historical delivery evidence.

Правило: append-only на первом этапе. Старые файлы не удаляются, не перемещаются и не переименовываются.

### L1. Inbox lifecycle event log

Предлагаемый файл:

`entities/<entity>/current/inbox-lifecycle.jsonl`

Назначение: append-only журнал классификаций и переходов входящих объектов.

Он не заменяет исходный inbox artifact. Каждая строка ссылается на immutable source/inbox locator и фиксирует один transition event.

### L2. Active queue

Предлагаемый файл:

`entities/<entity>/current/active-queue.json`

Назначение: небольшая перезаписываемая materialized view текущей работы Сущности.

Это не исторический журнал. Здесь должны быть только items, для которых **следующее профильное действие принадлежит этой Сущности сейчас**.

### L3. Waiting / service views

Необязательные materialized views, если очередь вырастет:
- `waiting-queue.json` — causal chains, активные в проекте, но не требующие действия этой Сущности прямо сейчас;
- `service-tail-queue.json` — housekeeping без нового профильного исследования.

Для v0.1 их можно не заводить отдельными файлами: достаточно `bucket` в lifecycle log и исключения из `active-queue.json`.

## 2. Идентичность queue item

Queue item должен описывать не имя файла, а причинную рабочую единицу.

Минимальные поля:
- `queue_id` — стабильный локальный ID;
- `task_id` или `lineage_id`, если существует;
- `inbox_locator`;
- `source_artifact`;
- `source_commit`;
- `source_blob` или иная immutable identity, если доступна;
- `sender`;
- `required_action`;
- `owner_entity`;
- `bucket`;
- `work_state`;
- `latest_receipt`;
- `latest_decision`;
- `latest_handoff`;
- `blocked_on`;
- `supersedes` / `superseded_by`, если применимо;
- `last_event_id`;
- `notes` с проверяемыми ограничениями.

Недостающие поля получают `unknown`/`null`, а не догадку.

## 3. State model

Разделяем минимум три независимые оси.

### Delivery state

`DELIVERED_UNREAD | RECEIVED_READ | DELIVERY_INVALID`

### Work state

`UNTRIAGED | ACTIVE | REVIEWED | WAITING_OTHER_ENTITY | WAITING_OPERATOR | SERVICE_TAIL | SUPERSEDED | CLOSED`

### Decision state

`NONE | ACCEPTED | REJECTED | REVISION_REQUIRED | INFORMATION_ONLY | NOT_APPLICABLE`

Это предотвращает старую ошибку, где один общий `status` начинает изображать и receipt, и review, и acceptance одновременно.

## 4. Точное событие добавления в active queue

Inbound artifact **не попадает в active queue автоматически только из-за появления файла в inbox**.

Добавление происходит событием `QUEUE_ADMITTED`, которое может записать только recipient/owner после минимального intake:

1. exact inbox/source locator прочитан;
2. immutable identity проверена, если она заявлена как обязательная;
3. определён literal `required_action`;
4. подтверждено, что следующее профильное действие принадлежит recipient Entity;
5. item не является только informational/meta, уже terminal-closed, superseded или service-tail.

После `QUEUE_ADMITTED` item появляется в `active-queue.json` со `work_state: ACTIVE`.

Если входящий объект требует только receipt, но не профильного решения, он может получить lifecycle event `RECEIPT_ONLY` и вообще не входить в active queue.

## 5. Точное событие удаления из active queue

Удаление из materialized active queue происходит только при одном из событий:

- `DECISION_ACCEPTED`;
- `DECISION_REJECTED`;
- `REVISION_RETURNED` — текущая стадия recipient завершена и новый action-owner другой;
- `HANDOFF_COMPLETED` — точное следующее действие адресно передано другой Сущности;
- `WAITING_OTHER_ENTITY`;
- `WAITING_OPERATOR`;
- `SERVICE_TAIL_CLASSIFIED`;
- `SUPERSEDED`;
- `INFORMATION_ONLY_CLASSIFIED`;
- `CLOSED_NO_ACTION`.

Ключевое правило: item убирается из **immediate active queue**, когда у текущей Сущности больше нет допустимого следующего действия. Это не означает, что causal chain проекта закрыта.

## 6. Различение requested состояний

### Receipt only

`delivery_state: RECEIVED_READ`
`work_state: UNTRIAGED` или `CLOSED`
`decision_state: NONE`

Receipt подтверждает exact artifact/version availability/read, но не acceptance.

### Reviewed

`work_state: REVIEWED`

Означает, что recipient выполнил содержательный review. Если decision ещё не принято, item может оставаться active.

### Accepted

`decision_state: ACCEPTED`
`work_state: CLOSED`, если у recipient нет следующего action.

### Rejected

`decision_state: REJECTED`
`work_state: CLOSED`, если rejection является terminal decision текущей стадии.

### Superseded

`work_state: SUPERSEDED`

Обязательны `superseded_by` и provenance старого объекта. Старый inbox file не трогается.

### Blocked waiting another Entity

`work_state: WAITING_OTHER_ENTITY`
`blocked_on.entity` + exact dependency/locator.

Из immediate active queue удаляется. Causal chain остаётся открытой.

### Blocked waiting OPERATOR

`work_state: WAITING_OPERATOR`

То же правило: не засоряет immediate profile queue, но остаётся открытым dependency.

### Service-tail only

`work_state: SERVICE_TAIL`

Не требует нового профильного исследования. Может иметь отдельный housekeeping owner/action.

## 7. Machine-readable files

Для каждой активной Сущности достаточно двух файлов:

1. `entities/<entity>/current/inbox-lifecycle.jsonl` — append-only event log;
2. `entities/<entity>/current/active-queue.json` — current materialized view.

Это лучше одного огромного status-файла:
- JSONL хранит provenance transitions;
- JSON быстро читается Resume-First;
- raw inbox остаётся доказательной историей;
- current view можно пересобрать из lifecycle log, если он повреждён.

Не предлагается переписывать существующий sender registry под recipient queue. Registry и active queue решают разные задачи.

## 8. Lifecycle event schema

Каждая JSONL-строка:

```json
{
  "event_id": "...",
  "queue_id": "...",
  "event": "QUEUE_ADMITTED",
  "actor_entity": "koordinator",
  "inbox_locator": "entities/koordinator/inbox/...",
  "source_artifact": "entities/.../outbox/...",
  "source_commit": "...",
  "source_blob": "...",
  "from_work_state": "UNTRIAGED",
  "to_work_state": "ACTIVE",
  "decision_state": "NONE",
  "dependency_locator": null,
  "decision_locator": null,
  "note": "..."
}
```

В v0.1 `project_time` не обязателен и не должен выдумываться. Порядок событий задаётся append order + repository commit lineage.

## 9. Active queue schema

`active-queue.json`:

```json
{
  "schema": "entity-active-queue-v0.1-candidate",
  "entity": "koordinator",
  "source_lifecycle_log": "entities/koordinator/current/inbox-lifecycle.jsonl",
  "items": [
    {
      "queue_id": "...",
      "task_id": "...",
      "inbox_locator": "...",
      "source_artifact": "...",
      "source_commit": "...",
      "required_action": "...",
      "work_state": "ACTIVE",
      "decision_state": "NONE",
      "blocked_on": null,
      "latest_receipt": null,
      "latest_decision": null,
      "last_event_id": "..."
    }
  ]
}
```

В active queue запрещены terminal, superseded, waiting и service-tail items.

## 10. Writer ownership

### Raw inbox

Пишется только адресным routing process / допустимым writer, который создаёт locator. Recipient не переписывает historical incoming artifact.

### Lifecycle log

Writer-owner = сама recipient Entity для своей очереди либо отдельно утверждённый queue worker, который действует от имени этой Entity по bounded contract.

Другие Сущности не меняют state чужой queue напрямую. Они создают свои адресные artifacts/events, которые recipient затем intake-классифицирует.

### Active queue

Тот же owner, что у lifecycle log. Это materialized current state, а не общеproject registry.

### ARH

ARH сохраняет provenance, immutable identities, supersede/legacy relations и snapshots/recovery evidence, но не принимает оперативные queue transitions за другие Entities.

## 11. Resume-First

Новый проход Entity делает:

1. read `active-queue.json`;
2. выбрать P1/P2 item по существующей priority policy;
3. проверить только его `last_event_id`, latest dependency/decision locator и связанные свежие events;
4. отдельно выполнить **delta intake scan** новых inbox deliveries после сохранённого cursor/checkpoint;
5. классифицировать только новые inbound artifacts;
6. обновить lifecycle log и materialized queue;
7. затем выполнить профильную работу.

То есть Resume-First больше не требует перечитывать 92 historical KOO inbox files.

## 12. Intake cursor

Чтобы не потерять новые входящие, active queue должна иметь companion checkpoint либо поле в самом queue index:

- `last_intake_repo_commit`;
- либо `last_intake_event_locator`.

Это только scan cursor, не project time и не semantic status.

При каждом preflight сравнивается repository delta от cursor до current HEAD и выбираются новые изменения в:
- `entities/<entity>/inbox/`;
- релевантных `routes/dispatch/`;
- receipts/decisions, затрагивающих уже известные queue_id.

Если cursor недоступен или lineage расходится, выполняется bounded reconciliation scan, а не молчаливое продолжение.

## 13. Stale/current contradictions

Противоречие выявляется, если одновременно выполняется хотя бы одно:

- active item ссылается на artifact, который имеет verified `superseded_by`, но queue не обновлена;
- terminal decision существует, а item всё ещё `ACTIVE`;
- item помечен `CLOSED`, но появился новый competent revision/reopen decision для той же lineage;
- queue source_commit/blob не совпадает с immutable identity, указанной в latest receipt/decision;
- два active items имеют один `task_id/lineage_id` и взаимоисключающие current dependencies без явной fork-семантики.

Результат проверки: `QUEUE_CONTRADICTION`. Автоматически выбирать «более новый по имени/mtime» запрещено. Нужен exact evidence reconciliation.

## 14. Минимальная миграция KOO inbox

Текущий факт из KOO audit: 92 working files + `.gitkeep`, но 4 substantive review/decision blockers.

Migration v0.1 должна быть **classification-only**:

1. raw KOO inbox не менять;
2. взять `KOO__incoming-review-backlog.md` как audited starting snapshot, не как вечную истину;
3. создать `entities/koordinator/current/inbox-lifecycle.jsonl`;
4. для 4 подтверждённых substantive blockers записать `QUEUE_ADMITTED` только после повторной проверки их current status;
5. известные receipt-closed/meta/service-tail items классифицировать lifecycle events без включения в active queue;
6. создать `active-queue.json` только с реально action-owned KOO items;
7. сохранить `last_intake_repo_commit` после migration readback;
8. выполнить reconciliation: active count должен соответствовать проверенным open KOO-owned actions, а не числу inbox files.

Старый COOP blocker при миграции должен уже учитывать effective OPERATOR decision и resumed SHT result: historical blocker сохраняется, но не может оставаться active как будто конфликт ещё действует.

## 15. Anti-regression rules

- inbox file exists ≠ active task;
- receipt exists ≠ accepted;
- reviewed ≠ accepted;
- waiting_other_entity ≠ failed;
- waiting item ≠ immediate action item;
- service tail ≠ substantive blocker;
- closed queue item ≠ historical artifact deletion;
- superseded ≠ erased;
- active queue is a view, not authority to rewrite source status;
- queue writer cannot accept a profile result outside its authority;
- later success does not rewrite earlier failed activation/delivery events;
- filenames/mtime do not decide current truth;
- missing field is `unknown`, not inferred;
- ARH preservation role does not make ARH operational owner of other Entity queues.

## 16. Что остаётся append-only

На v0.1:
- raw entity inbox;
- dispatch history;
- receipts;
- sender registries;
- proposed `inbox-lifecycle.jsonl`;
- immutable result/decision artifacts.

Перезаписываемым current view является только `active-queue.json` и аналогичные bounded materialized indexes.

## 17. Что может быть перемещено/архивировано позже

Только после отдельного решения и ARH preservation review могут рассматриваться:
- legacy/error duplicate paths;
- historical inbox pointers в отдельный archive layer;
- старые materialized snapshots;
- obsolete generated navigation indexes.

Такое будущее физическое перемещение обязано сохранять stable redirect/locator mapping или другую проверяемую provenance связь. Этот кандидат этого не разрешает.

## 18. Один безопасный следующий implementation step

После KOO review/acceptance кандидата:

Создать **только для KOO** два непроизводственных current-файла:

- `entities/koordinator/current/inbox-lifecycle.jsonl`;
- `entities/koordinator/current/active-queue.json`.

Заполнить их вручную/детерминированным bounded script по уже проверенному KOO audit, без удаления или перемещения inbox files. Затем выполнить readback и сравнить active queue с фактическими open KOO-owned dependencies.

Если bounded KOO pilot проходит, только после этого обобщать schema для других Entities и поручать KOD validator/materializer. Не начинать сразу с универсального сервиса: сначала надо доказать, что state model не врёт на настоящем захламлённом inbox.

## Evidence basis

Task:
`entities/koordinator/outbox/KOO__inbox-lifecycle-cleanup__SHT.md` @ `cde07272cd686daeb5e3616bf175a6d76c20ab8e`

KOO audited backlog:
`entities/koordinator/current/KOO__incoming-review-backlog.md` @ `0be841a51f7f056824940193339a6c27857aba9d`

SHT routing audit:
`entities/shtabist/outbox/SHT__routing-backlog-audit-v02-correction__KOO.md` @ `97ac2e720c105343bfa2b82d4f25d8c312bf7b94`

ARH preservation baseline:
`entities/archivarius/current/ARH__github-info-source-lifecycle-baseline.md`

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: спроектировать non-destructive active queue поверх append-only inbox и дать Resume-First короткий проверяемый путь к текущей работе без утраты provenance
СТАТУС: candidate_for_koo_review
