# KAN → KOO: candidate successor-дельты task-conveyor v1.2 для literary journal feed

status: `candidate / not approved / not active`
target_source: `task-conveyor-canon-v1_1-approved.md`
proposed_successor: `task-conveyor-canon-v1_2`
project_core_change_required: `no`
roles_change_required: `no`
file_work_change_required: `no`
source_loading_change_required: `no`
recovery_change_required: `no`
automation: `0`
project_time: omitted; trusted project-time source not used

## Нормативный вывод

Механизм `JOURNAL_CANDIDATE` относится к post-terminal маршрутизации и batching между Сущностями, поэтому минимальный нормативный дом — **task-conveyor canon**.

Project core менять не требуется: current core v2.4 уже регулирует человекочитаемый интерфейс и хранение machine evidence в информационном поле. Делать editorial significance capture общепроектной обязанностью core было бы ненужным расширением scope.

Roles менять не требуется:
- KOO уже владеет fresh reconciliation, sequencing и адресным handoff;
- RED уже владеет живым текстом, читаемостью и редакторским отбором.

File-work, source-loading и recovery canon не затрагиваются.

## Exact insertion point

В `task-conveyor-canon-v1_1-approved.md` добавить новый подраздел **после §10 “Manual activation handoff после terminal result” и перед §11 “Failure modes”**.

## Exact proposed delta

### Редакционный сигнал значимого события для литературного журнала

`JOURNAL_CANDIDATE` — необязательный положительный post-terminal signal для события, которое имеет явную историческую или редакционную ценность для литературного журнала проекта.

Signal допустим, если terminal result или подтверждённое им событие, например:

- меняет архитектуру, правило или существенное направление проекта;
- фиксирует серьёзную неудачу вместе с новым практическим выводом;
- закрывает первый либо иной заметный реальный рубеж;
- создаёт новую устойчивую практику;
- содержит важный человеческий контекст, характерный или смешной эпизод, полезный для будущей истории проекта.

Для routine result signal не создаётся. Поле `JOURNAL_CANDIDATE: no` не требуется.

Если событие отмечается как candidate, **тот же terminal result artifact** может после основной человекочитаемой части содержать компактный блок:

    JOURNAL_CANDIDATE: yes
    СМЫСЛ: <1–3 предложения, почему событие исторически или редакционно важно>
    EVIDENCE: <exact locator + immutable identity события/основания, если они уже известны>

Отдельный artifact только ради `JOURNAL_CANDIDATE` не создаётся.

Если immutable identity самого terminal result становится известна только после публикации, исполнившая Сущность не переписывает результат и не создаёт второй файл ради самоссылки. KOO при fresh reconciliation связывает signal с уже проверенной immutable identity маршрутизированного terminal result из информационного поля. Поле `EVIDENCE` может указывать на более раннее exact основание события, если оно уже существует.

Наличие или отсутствие `JOURNAL_CANDIDATE`:

- не является task authority;
- не является delivery, receipt, acknowledgement или acceptance;
- не является public/release approval;
- не является обязательным критерием завершения исходной задачи;
- не означает автоматическое включение материала в литературный журнал.

KOO при fresh reconciliation замечает новые положительные signals и **не создаёт отдельную RED-задачу на каждый signal**. Обычно KOO объединяет 1–3 содержательных кандидата в один bounded `RED journal-sweep` step. Один кандидат может быть передан отдельно, если есть проверяемый риск потерять существенный человеческий контекст при ожидании batch.

RED получает exact evidence кандидатов, проверяет его и остаётся единственным редакторским фильтром журнала: может включить, объединить, отложить или отклонить candidate как routine/duplicate/неподходящий материал.

Если для RED sweep требуется другой Entity-chat и exact automatic activation отсутствует, KOO использует действующий manual activation handoff. Signal сам по себе не доказывает активацию RED и не разрешает automatic chat resume.

Из этой нормы запрещено выводить:

- journal entry после каждого task;
- обязательное `JOURNAL_CANDIDATE: no`;
- отдельный journal/feed artifact на routine result;
- cron, scheduler или другую automation;
- automatic journal inclusion;
- второй technical log;
- full transcript ingestion;
- обязанность ОПЕРАТОРА быть ручным литературным диспетчером.

Отсутствие signal означает только отсутствие явной отметки в этом terminal result. Оно не запрещает RED позднее обнаружить значимое событие своим bounded editorial delta-review.

## Non-duplication check

### Project core v2.4

Не менять.

Core регулирует human-facing interface и suppresses unnecessary machine evidence from chat. Новый signal может храниться в том же result artifact после человеческого смысла и не обязан повторяться в чате только потому, что существует.

### File-work canon v2.4

Не менять.

Новый механизм специально запрещает отдельный artifact только ради signal и не изменяет file delivery/receipt/acceptance semantics.

### Entity roles v2.4

Не менять.

KOO batching является обычной coordination/routing функцией. RED editorial selection уже входит в роль RED. Новый authority не создаётся.

### Source-loading v2.2 / recovery v1.6

Не менять.

Signal не является source-loading, recovery, current-writer или preservation state.

## Source-card delta for future successor materialization

When KOO later materializes the full successor after OPERATOR decision:

- `document_type: task-conveyor-canon`
- `version: v1.2`
- `source: task-conveyor-canon-v1_1-approved.md`
- `changed_sections: literary-journal candidate feed`
- `approval_status: requires_operator_decision`
- `effectivity_rule: active_only_after_source-set/activation-barrier PASS`
- `responsibility_boundary: optional positive signal + KOO batching + RED editorial filter; no per-task reporting, no automation, no automatic journal inclusion`

---

sender: KAN
recipient: KOO
document_type: task-conveyor-v1_2-journal-feed-delta-candidate
status: candidate / not approved / not active
project_time: omitted; trusted project-time source not used
