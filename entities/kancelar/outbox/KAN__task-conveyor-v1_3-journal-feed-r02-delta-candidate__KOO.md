# KAN → KOO: successor-дельта task-conveyor v1.3 для incremental literary-journal feed

status: `candidate / not approved / not active`
target_source: `task-conveyor-canon-v1_2-approved.md`
proposed_successor: `task-conveyor-canon-v1_3`
project_core_change_required: `no`
roles_change_required: `no`
file_work_change_required: `no`
source_loading_change_required: `no`
recovery_change_required: `no`
new_project_source_required: `no`
automation: `0`
project_time: omitted; trusted project-time source not used

## Нормативный вывод

Active v1.2 уже содержит optional positive signal `JOURNAL_CANDIDATE`, KOO batching и RED editorial filter.

RED r0.2 показал практический дефект: passive optional signaling не гарантирует, что значимые terminal results вообще попадут в editorial feed.

Минимальная корректная дельта остаётся внутри **task-conveyor canon**.

Project core, roles, file-work, source-loading и recovery менять не требуется.

## Exact insertion point

В `task-conveyor-canon-v1_2-approved.md` расширить существующий подраздел:

`### Редакционный сигнал значимого события для литературного журнала`

сразу после текущего правила об optional `JOURNAL_CANDIDATE` и до `## 11. Failure modes`.

## Exact proposed delta

### Incremental significance sweep KOO

Optional `JOURNAL_CANDIDATE` сохраняется без изменения как fast path. Его отсутствие не означает, что результат проверен как routine и не запрещает KOO/RED позднее обнаружить значимое событие.

При каждом **normal fresh KOO reconciliation** КООРДИНАТОР выполняет дополнительный bounded significance sweep только по новым terminal results после сохранённого journal-feed cursor.

Sweep:

- не является полным пересмотром Git history;
- не создаёт обязательную классификацию каждого terminal result;
- не требует записи `JOURNAL_CANDIDATE: no`;
- не создаёт отдельный artifact для routine result;
- не изменяет terminal status исходных задач;
- не является automation/cron/scheduler.

KOO сначала использует явные positive `JOURNAL_CANDIDATE` как fast path, затем в том же bounded delta может поднять candidate без signal только при наличии **явного редкого основания значимости**, например:

- существенное изменение архитектуры, нормы или направления;
- серьёзная неудача, породившая устойчивый практический вывод;
- первый либо иной заметный реальный/public/production-like рубеж;
- открытие или закрытие крупного контура;
- появление новой устойчивой практики взаимодействия человека и Сущностей;
- человеческий/исторический эпизод, смысл которого машинное evidence само по себе не сохранит.

Routine PASS, receipt, route update, retry, ordinary refactor/deploy step, queue refresh и иная обычная операционная активность сами по себе достаточным основанием не являются.

Sweep является **редакторской triage-проверкой**, а не обязательным per-result decision log. KOO фиксирует только положительные pending refs и cursor boundary. Отрицательные решения по routine result отдельно не записываются.

### Minimal persistent journal-feed state

Чтобы incremental sweep был проверяемым и не скатывался в повторный full rescan, KOO поддерживает минимальное operational state, содержащее по смыслу:

- `last_scanned_commit` — последний проверенный repository boundary, до которого bounded significance sweep завершён без gap;
- `pending_candidate_refs` — exact refs ещё не переданных/не обработанных RED candidates;
- `last_red_journal_sweep_ref` — последний проверенный terminal result RED journal-sweep, если он существует.

Это operational current-state KOO/task-conveyor, а не новый Project Source, не authority, не technical truth о подлежащих задачах и не отдельный обязательный документ на каждый цикл.

State может храниться в уже существующем KOO current-state/queue либо в одном компактном dedicated current artifact. Канон не требует конкретного filename или отдельной записи на каждый reconciliation.

### Cursor semantics

`last_scanned_commit` продвигается **после каждого успешно завершённого bounded significance sweep**, даже если новых journal candidates не найдено.

Если candidates найдены, cursor всё равно может продвинуться до проверенного boundary, а сами кандидаты сохраняются в `pending_candidate_refs`. Это предотвращает повторное сканирование уже проверенного диапазона.

Если delta-range прочитан не полностью, есть gap/ambiguity либо текущий repository boundary нельзя однозначно связать с предыдущим cursor, cursor **не продвигается**. Фиксируется bounded blocker; full-history reconstruction по догадке запрещён.

После RED journal-sweep:
- processed refs удаляются из pending;
- rejected-as-routine/duplicate refs также считаются processed;
- `last_red_journal_sweep_ref` обновляется exact RED result identity;
- новые evidence по уже обработанному событию могут породить новый candidate только если они materially меняют эпизод.

### Initial activation baseline

При первом включении v1.3 KOO не выполняет ретроспективный полный просмотр истории.

Начальный `last_scanned_commit` устанавливается на exact verified activation/reconciliation boundary нового правила. Historical backfill допускается только отдельным явно авторизованным bounded task.

Уже существующие explicit pending signals, которые exact evidence показывает как ещё не обработанные RED, могут быть seed-refs без полного historical scan.

### Batching and RED authority

KOO не создаёт отдельную RED-задачу на каждый candidate.

Нормальная модель:
- 1–3 содержательных pending candidates в один bounded RED journal-sweep;
- один candidate допускается отдельно только при проверяемом риске потерять уникальный человеческий контекст при ожидании batch.

RED остаётся единственным владельцем редакторского отбора:
- verifies exact evidence;
- include / merge / defer / reject;
- journal inclusion не возникает автоматически из KOO significance sweep или optional signal.

Если для RED sweep нужен другой Entity-chat и exact automatic activation отсутствует, применяется действующий manual activation handoff.

### Запрещённые выводы

Из этой нормы нельзя выводить:

- per-task reporting;
- обязательную классификацию каждого result;
- обязательное `JOURNAL_CANDIDATE: no`;
- полный пересмотр Git history на каждом reconciliation;
- отдельный candidate/feed artifact на routine result;
- cron/scheduler/automatic worker;
- automatic journal inclusion;
- новый Project Source;
- новую Entity role;
- обязанность ОПЕРАТОРА быть литературным диспетчером;
- обязанность RED принимать KOO candidate в journal;
- обязанность менять recovery/source-loading/file-work/core/roles.

## Почему state необходим

Без persistent cursor KOO либо повторно смотрит один и тот же диапазон, либо не может доказать, где закончился прошлый incremental sweep.

Без pending refs cursor нельзя безопасно продвинуть вперёд до RED sweep: candidates потеряются между reconciliation cycles.

Без last RED sweep ref нельзя однозначно отличить pending event от уже редакционно обработанного/отклонённого.

Поэтому minimal triple:

`last_scanned_commit + pending_candidate_refs + last_red_journal_sweep_ref`

является необходимым operational state для deterministic incremental feed, но не требует нового Project Source или per-task документа.

## Source-card delta for future materialization

Если ОПЕРАТОР позже утвердит successor:

- `document_type: task-conveyor-canon`
- `version: v1.3`
- `source: task-conveyor-canon-v1_2-approved.md`
- `changed_sections: literary-journal feed / incremental KOO significance sweep`
- `approval_status: requires_operator_decision`
- `effectivity_rule: active_only_after_source activation/readback PASS`
- `responsibility_boundary: optional JOURNAL_CANDIDATE fast path + mandatory bounded incremental KOO significance sweep + minimal cursor/pending/last-sweep state + RED editorial filter; no per-task reporting, automation or automatic inclusion`

---

sender: KAN
recipient: KOO
document_type: task-conveyor-v1_3-journal-feed-delta-candidate
status: candidate / not approved / not active
project_time: omitted; trusted project-time source not used
