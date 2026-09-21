# KAN → KOO: bounded normative review literary journal feed r0.2

status: `PASS_KAN_JOURNAL_FEED_R02_NORMATIVE_READY_FOR_KOO_GATE`
approved_source_mutations: `0`
automation: `0`
project_time: omitted; trusted project-time source not used

## Что произошло

Обработан exact RED candidate:

`entities/redaktor/outbox/RED__literary-journal-feed-r02__KAN-KOO.md`

commit:
`9f9c337b353ea2e0b000d3c2da4bf8dce37a7dce`

blob:
`598708cdb9d49b50435298d0d9dbbc0f12bb7de4`.

Fresh GitHub-preflight подтверждает:
- active `task-conveyor-canon-v1_2-approved.md` уже содержит optional positive `JOURNAL_CANDIDATE`;
- current KOO queue находится на r1.04 и не содержит отдельного `KOO__journal-feed-state.md`;
- RED r0.2 exact source фиксирует отсутствие новых positive signals и journal-sweep artifacts как проверенный практический дефект passive-only feed.

## Нормативный вывод

RED r0.2 по существу корректен.

Минимальный нормативный дом:

`task-conveyor canon`

и только он.

Следующий successor:

`task-conveyor-canon-v1_2-approved.md → proposed v1.3`.

Не требуется менять:
- project core;
- roles;
- file-work canon;
- source-loading policy;
- recovery canon.

Не требуется новый Project Source или новая роль.

## Почему mandatory incremental KOO sweep допустим

KOO уже обязан выполнять normal fresh reconciliation общего информационного поля.

Добавление bounded significance sweep не создаёт новую профильную authority:
- KOO не пишет journal entry;
- KOO не решает public/release вопрос;
- KOO только поднимает редкий candidate ref для существующего RED editorial filter.

Это coordination/triage внутри task-conveyor, а не расширение роли KOO до редактора.

## Minimal KOO state действительно необходим

Тройка:

`last_scanned_commit + pending_candidate_refs + last_red_journal_sweep_ref`

нормативно оправдана и минимальна.

Она нужна, чтобы одновременно обеспечить:
- incremental scan без full-history replay;
- сохранение pending candidates между KOO reconciliation cycles;
- отсутствие повторной передачи уже processed RED events.

Но это **operational KOO current-state**, а не новый Project Source и не новый обязательный per-cycle artifact.

Канон не должен навязывать exact filename. State можно хранить в existing current queue/current-state либо в одном compact dedicated current artifact.

## Обязательная коррекция RED cursor semantics

В RED candidate cursor продвигается в разделе “Cursor advancement” после RED terminal result.

Для deterministic incremental mechanism этого недостаточно.

Если candidates нет, RED sweep не происходит; cursor тогда не продвинется и KOO будет повторно смотреть тот же диапазон.

Если candidates есть, но batch ещё не сформирован, cursor также можно и нужно продвинуть после успешного scan, сохранив refs в pending.

Поэтому v1.3 delta устанавливает:

- `last_scanned_commit` продвигается после **каждого успешно завершённого bounded significance sweep**;
- наличие pending candidates не блокирует cursor advancement;
- pending refs хранят candidates отдельно;
- при incomplete/gap/ambiguous scan cursor не продвигается;
- после RED sweep processed refs удаляются из pending, `last_red_journal_sweep_ref` обновляется.

Это bounded correction, а не возврат RED candidate на переработку.

## Initial activation boundary

При первом включении v1.3 запрещён full historical rescan.

Initial cursor:
- exact verified activation/reconciliation boundary нового правила.

Historical backfill:
- только отдельным явно авторизованным bounded task.

Уже известные explicit unprocessed signals могут быть seed refs без полного просмотра истории.

## Материализованная successor-дельта

Artifact:

`entities/kancelar/outbox/KAN__task-conveyor-v1_3-journal-feed-r02-delta-candidate__KOO.md`

commit:

`d06773bbd91f1105e6c2657f6a3ccf8f51748e00`

blob:

`1f561d4a0e0c8f8129687ed609aca4397d817b39`

status:

`candidate / not approved / not active`.

Exact readback:

`PASS`.

## Сохранённые anti-bureaucracy boundaries

Successor delta запрещает:

- per-task reporting;
- обязательную классификацию каждого result;
- обязательное `JOURNAL_CANDIDATE: no`;
- полный пересмотр Git history при каждом reconciliation;
- отдельный artifact на routine result;
- automation/cron/scheduler;
- automatic journal inclusion;
- новую Entity role;
- новый Project Source;
- обязанность ОПЕРАТОРА быть литературным диспетчером.

`JOURNAL_CANDIDATE` остаётся optional fast path.

RED остаётся владельцем редакторского отбора.

## Resume-First / writer boundary

`entities/kancelar/current/` по-прежнему не содержит explicit KAN current-writer artifact.

Writer state не выдумывался.

Текущая задача создаёт только candidate/review/outbox evidence и не изменяет authoritative current-state, поэтому исполнена в границе:

`WRITER_NOT_REQUIRED_FOR_TASK`.

## Следующий допустимый шаг

Next owner:

`KOO / single-source OPERATOR decision gate`.

KOO должен:
1. fresh-reconcile exact RED/KAN identities;
2. проверить current active v1.2 и exact v1.3 delta;
3. подготовить один OPERATOR decision gate для v1.3;
4. не менять core/roles/file-work/source-loading/recovery;
5. только после explicit OPERATOR approval материализовать full `task-conveyor-canon-v1_3-approved.md`;
6. выполнить source activation/readback barrier;
7. после PASS инициализировать journal-feed operational state на exact activation boundary, без full-history scan.

## Terminal result

`PASS_KAN_JOURNAL_FEED_R02_NORMATIVE_READY_FOR_KOO_GATE`

---

sender: KAN
recipient: KOO
document_type: literary-journal-feed-r02-normative-review
approved_source_mutations: 0
next_owner: KOO
project_time: omitted; trusted project-time source not used
