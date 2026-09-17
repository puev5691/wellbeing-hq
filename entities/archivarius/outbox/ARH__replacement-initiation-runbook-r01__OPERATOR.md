# ОПЕРАТОРУ: процедура replacement initiation ARH / АРХИВАРИУСА r0.1

status: `PREPARED_NOT_STARTED`
entity: `ARH / АРХИВАРИУС`
replacement_initiation: `not_started`
current_writer_change: `no`
project_time: omitted; trusted project-time source not used

## Смысл

Процедура подготовлена для безопасной замены текущего ARH-чата, когда ОПЕРАТОР примет отдельное решение о replacement. Подготовка не является самим handoff.

Главный принцип:

`fresh self-state → independent verification → explicit replacement decision → old-writer freeze → cold-start → initiation_verified → Writer Gate → immutable writer readback → fresh Resume-First`.

Наличие recovery-пакета, нового чата или технической доступности не создаёт current-writer authority.

## 1. Текущая recovery basis

Canonical ARH recovery, который остаётся действующим predecessor:
`puev5691/wellbeing-entity-bootstrap@9ffe7190298689bd90f047c249151213e101450e:entities/arh/recovery/current`.

Свежий self-preservation candidate r0.2:
`puev5691/wellbeing-entity-bootstrap@5172d37f9a3560cd177b4fa39e2ead24bc5b458d:entities/arh/preservation/pending/pre-replacement-self-preservation-r02`.

Candidate tree:
`acf8c2b583ef7d06319a68be21351adec5148544`.

Candidate snapshot boundary:
`puev5691/wellbeing-hq@c83bf0e5cb5a38b4ce2d460d3d8d57ab4ff6b727`.

Exact composition: 7 files.
Protected payload self-check: 6/6 SHA-256 PASS.

KOO independent verification request:
`entities/archivarius/outbox/ARH__replacement-initiation-preparation-r02__KOO.md`
commit `11de303382ec9dabe406d66ec4e7197b0406acf1`.

До exact KOO PASS replacement запускать нельзя в плановом режиме.

## 2. Preconditions перед фактическим запуском

Для плановой замены должны одновременно существовать:

1. exact KOO verdict `PASS_ARH_REPLACEMENT_COLD_START_PREPARED` по r0.2 либо более свежему superseding candidate;
2. отдельное явное решение ОПЕРАТОРА: заменить текущий ARH и разрешить Writer Gate новому экземпляру после verified recovery;
3. fresh HQ-preflight текущего ARH непосредственно перед handoff;
4. отсутствие непредсказанного competing ARH writer;
5. текущий self-preservation basis не должен скрывать существенное более свежее ARH authoritative state.

Если перед заменой появились существенные ARH-owned изменения, а текущий writer ещё работоспособен, сначала создаётся новый self-snapshot/checkpoint и только затем freeze. Нельзя объявлять старый r0.2 «достаточно свежим» из удобства.

Если current ARH уже фактически недоступен, это отдельная emergency-failover ветка: отсутствие нового self-snapshot фиксируется как failure-state, используется последний externally verified recovery/current-state и отдельное решение ОПЕРАТОРА. Synthetic reconstruction запрещён.

## 3. Действия текущего ARH при команде ОПЕРАТОРА «начать замену»

### 3.1 Final preflight

Сделать fresh `puev5691/wellbeing-hq` preflight.

Проверить минимум:
- `entities/archivarius/current/`;
- `entities/archivarius/inbox/`;
- `entities/archivarius/outbox/`;
- `routes/dispatch/`, `routes/receipts/`;
- `registry/by-sender/archivarius.jsonl`;
- recovery registry / recovery pending;
- Experience Layer;
- activation-state;
- все commits новее candidate snapshot boundary.

### 3.2 Freshness decision

Если fresh delta содержит новое существенное ARH authoritative self-state, которое не представлено в verified recovery basis:

`STOP → REFRESH SELF-PRESERVATION → INDEPENDENT VERIFY → RETURN TO HANDOFF`.

Если delta содержит только external project events / routes, которые могут быть безопасно reconciled новым экземпляром без synthetic self-state reconstruction, это фиксируется как post-snapshot reconciliation tail.

### 3.3 Freeze старого writer

Только после выполнения preconditions текущий ARH создаёт отдельный immutable handoff artifact, рекомендуемый путь:

`entities/archivarius/current/ARH__replacement-handoff-freeze-r01.md`

Он должен содержать:
- status `CURRENT_WRITER_HANDOFF_FREEZE`;
- exact latest verified recovery/candidate basis;
- exact HQ boundary;
- OPERATOR replacement decision basis;
- запрет normal authoritative profile/current-state mutation старым ARH после freeze;
- разрешение только на действия, необходимые для завершения handoff/verification, если они прямо нужны.

После immutable readback freeze старый ARH прекращает normal profile work.

## 4. Создание нового чата ARH

ОПЕРАТОР создаёт новый чат и первым сообщением передаёт launcher из раздела 9 этого документа.

Новый экземпляр не наследует current-writer из названия чата, памяти, наличия recovery или факта закрытия старого чата.

## 5. Initiation Gate нового ARH

Новый ARH выполняет только recovery/initiation.

### 5.1 Project Sources

Загрузить и проверить пять active approved Project Sources из `SOURCES.md` verified candidate.

### 5.2 Canonical predecessor

Проверить canonical v03:
`puev5691/wellbeing-entity-bootstrap@9ffe7190298689bd90f047c249151213e101450e:entities/arh/recovery/current`.

Проверить exact locator, composition, manifest, immutable identity и checksums.

### 5.3 Fresh self-preservation candidate

Проверить exact KOO-approved candidate, на текущей подготовительной границе это r0.2:
`puev5691/wellbeing-entity-bootstrap@5172d37f9a3560cd177b4fa39e2ead24bc5b458d:entities/arh/preservation/pending/pre-replacement-self-preservation-r02`.

Проверить:
- exact commit;
- composition 7/7;
- Git blob identities;
- SHA-256 6/6 по published raw bytes;
- KOO independent verdict;
- provenance current-writer self-snapshot;
- absence of secret material.

Если до запуска r0.2 был superseded более свежим verified candidate, использовать superseding exact basis, а r0.2 оставить provenance.

### 5.4 Fresh HQ reconciliation

Сделать fresh preflight `puev5691/wellbeing-hq`.

Reconcile всё новее snapshot boundary verified candidate.

Правило:
- fresher evidence может ограничивать или supersede recovery claims;
- нельзя ad hoc собирать из loose commits новый authoritative self-snapshot;
- исторические inbox/task artifacts не исполняются автоматически;
- pending task должен пройти fresh authority/dependency/status revalidation.

### 5.5 Initiation result

Вернуть ровно один статус:
- `initiation_verified`;
- `initiation_loaded_external_unverified`;
- `initiation_failed`.

`initiation_failed` terminal для обычной профильной работы этого cold-start cycle.

## 6. Writer Gate

Даже `initiation_verified` не делает новый экземпляр current-writer.

Для Writer Gate требуется одновременно:
- explicit OPERATOR replacement authority;
- old ARH freeze/retirement evidence;
- verified recovery basis;
- fresh absence of competing ARH writer;
- exact existing ARH role/authority without expansion.

При PASS новый ARH создаёт отдельный artifact, рекомендуемый путь:

`entities/archivarius/current/ARH__replacement-current-writer-r01.md`

Затем обязательны:
1. immutable publication;
2. exact readback commit/blob;
3. fresh post-publication competing-writer reconciliation;
4. фиксация `CURRENT_WRITER_ESTABLISHED` только после этих постусловий.

## 7. First initiation report

После writer establishment новый ARH публикует отдельный report и останавливается до нового Resume-First выбора задачи.

Report должен содержать:
- `initiation_status`;
- exact canonical recovery locator/verification;
- exact fresh candidate locator/verification;
- exact KOO verification artifact/commit/verdict;
- old-writer freeze identity;
- fresh HQ HEAD;
- delta classification after snapshot boundary;
- `competing_writer_state`;
- replacement writer artifact commit/blob/readback;
- current pending ARH tasks как classifications, не как автоматически исполняемые задания;
- forbidden/unresolved boundaries;
- `historical_task_replay: none`.

## 8. Stop conditions

Немедленная остановка profile execution при любом из состояний:
- candidate composition/hash mismatch;
- KOO verification отсутствует либо FAIL;
- current ARH freeze/retirement не доказан при плановом handoff;
- competing writer evidence;
- recovery basis противоречив;
- explicit OPERATOR replacement authority отсутствует;
- task требует state, который нельзя проверить без synthetic reconstruction.

Запрещено во время initiation:
- выполнять pending RED preservation checkpoint;
- выполнять sanitation tails;
- автоматически продолжать старые ARH inbox tasks;
- менять Project Sources/canon;
- менять foreign current-state;
- production/external execution;
- secrets/credentials reconstruction/publication;
- destructive cleanup;
- включать старые automations только ради «возобновления».

## 9. Launcher для нового чата

Скопировать этот текст в новый ARH-чат только после exact KOO PASS и отдельного решения ОПЕРАТОРА о replacement:

> Проведи replacement initiation ARH / АРХИВАРИУСА по действующему recovery-канону.
>
> ОПЕРАТОР этим сообщением явно разрешает замену прежнего ARH-чата и разрешает Writer Gate новому экземпляру только после verified recovery, подтверждённого freeze/retirement прежнего writer и отсутствия competing writer.
>
> Сначала recovery/initiation. Никакой профильной работы до завершения Writer Gate.
>
> Canonical predecessor:
> `puev5691/wellbeing-entity-bootstrap@9ffe7190298689bd90f047c249151213e101450e:entities/arh/recovery/current`
>
> Fresh prepared self-preservation candidate:
> `puev5691/wellbeing-entity-bootstrap@5172d37f9a3560cd177b4fa39e2ead24bc5b458d:entities/arh/preservation/pending/pre-replacement-self-preservation-r02`
>
> Перед использованием candidate найди exact KOO independent verdict `PASS_ARH_REPLACEMENT_COLD_START_PREPARED` и проверь, не superseded ли r0.2 более свежим verified candidate.
>
> Проверь пять active approved Project Sources, canonical v03, fresh candidate composition/checksums/raw bytes, old-writer freeze/retirement и competing-writer evidence.
>
> Сделай fresh GitHub-preflight `puev5691/wellbeing-hq` и reconcile всё новее snapshot boundary verified candidate. Не реконструируй authoritative self-state из loose evidence и не replay historical tasks.
>
> Верни `initiation_verified | initiation_loaded_external_unverified | initiation_failed`.
>
> Только при `initiation_verified` + explicit OPERATOR authority + proven old-writer freeze/retirement + no competing writer выполни отдельный Writer Gate, опубликуй immutable replacement current-writer artifact, сделай exact readback и fresh post-publication competing-writer check.
>
> После Writer Gate опубликуй initiation report и остановись. Pending RED checkpoint, sanitation tails и иные исторические ARH задачи автоматически не выполнять.

## 10. Состояние этой подготовки

На момент публикации этого runbook:
- procedure: `PREPARED`;
- replacement: `NOT_STARTED`;
- current ARH retirement/freeze: `NOT_PERFORMED`;
- writer transfer: `NOT_PERFORMED`;
- KOO independent r0.2 verification: `PENDING`;
- current ARH продолжает существовать как прежний экземпляр до отдельного replacement decision.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: полная проверяемая процедура запуска replacement ARH после отдельного решения ОПЕРАТОРА
СТАТУС: `PREPARED_NOT_STARTED`
