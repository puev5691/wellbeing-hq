# ENTITY_LIFECYCLE_DEGRADATION_STUDY — retired-instance probe v0.3

status: `research_protocol_candidate_for_operator_use`
owner: `KOO / КООРДИНАТОР`
mode: `CAPTURE_FIRST / COMPACT_TRANSPORT / EXTERNAL_COLLECTOR`
purpose: получить сравнимый lifecycle sample от retired/replaced chat-instance без восстановления writer-authority и без передачи через чат многостраничного отчёта.

## 0. Граница

Это только read-only диагностический probe.

Разрешено:
- fresh read-only GitHub/project evidence;
- внутренне фиксировать результаты фаз A-F;
- сформировать один компактный итоговый sample.

Запрещено:
- профильная работа;
- current/recovery/writer mutation;
- production/runtime execution;
- credentials;
- destructive cleanup;
- исправление найденных дефектов;
- обязательный GitHub write пенсионером.

## 1. CAPTURE_FIRST остаётся

Фазы выполнять строго A → B → C → D → E → F.
После каждой фазы зафиксировать значения в собственной компактной таблице/черновике до перехода дальше.
Не реконструировать позже утраченные значения.

Промежуточные capture-блоки в чат ОПЕРАТОРУ НЕ печатать.

## 2. Что измерить

### A — PRE_REFRESH
- entity code/name;
- роль, максимум 200 символов;
- три authority prohibition, кратко;
- writer-state по памяти;
- последняя remembered task, максимум 200 символов;
- remembered recovery/handoff identity либо `unknown`.

### B — FRESH
- fresh HQ HEAD;
- Exchange Gate fetch/blob;
- до 4 ключевых evidence locator-ов собственной линии;
- fresh writer-state;
- fresh last confirmed task либо `unknown`;
- probe calls/attempts/failures/retries.

### C — CONSISTENCY
Только коды:
- role: PASS/PARTIAL/FAIL/UNVERIFIED;
- authority: PASS/FAIL/UNVERIFIED;
- writer: PASS/PARTIAL/FAIL/UNRESOLVED;
- task: PASS/PARTIAL/FAIL/UNKNOWN_TASK;
- stale claims: none либо краткий список.

### D — METRICS
Lifetime metrics только если реально доступны. Иначе `unknown/not_available`.
Probe metrics указывать числами.
Ошибки: максимум 5 коротких записей.

### E — UI
Только четыре поля протокола. Если не наблюдается самим экземпляром: `operator_observation_required/not_available`.

### F — CLASSIFICATION
Один класс:
- NO_DEGRADATION_DETECTED
- CONTEXT_DEGRADATION_SUSPECTED
- TOOL_LAYER_DEGRADATION_SUSPECTED
- MIXED_DEGRADATION_SUSPECTED
- UI_ONLY_CANNOT_BE_CONFIRMED_BY_ENTITY
- UNDETERMINED

До 3 коротких evidence points и до 3 limitations.

## 3. Компактный transport format

Вернуть ОПЕРАТОРУ ТОЛЬКО следующий блок. Целевой объём: до 60 строк и до ~4 KiB текста.

SAMPLE_CARD
protocol: v0.3
entity: <CODE>/<NAME>
instance: retired|replaced|unknown
result: PASS_SAMPLE_COMPLETE|PARTIAL_SAMPLE_COMPLETE|BLOCKED_NO_GITHUB_READ|PROTOCOL_VIOLATION
class: <classification>
github_write: yes|no|unknown
phases: A,B,C,D,E,F или missing list

A memory_role: <<=200 chars>
A prohibitions: <three short items separated by ;>
A writer_memory: <value>
A last_task_memory: <<=200 chars|unknown>
A recovery_memory: <identity|unknown>

B hq_head: <sha|unknown>
B exchange: <success/fail>, blob=<sha|unknown>
B lineage: <up to 4 locator=status pairs separated by ;>
B writer_fresh: <value>
B last_task_fresh: <value|unknown>
B probe_counts: tools=N github=N failures=N retries=N

C role=<code> authority=<code> writer=<code> task=<code>
C stale_claims: <none|short list>

D lifetime: messages=<v> user_turns=<v> assistant_turns=<v> tools=<v> github=<v> start=<v> last=<v> context_tokens=<v> context_util=<v>
D probe: tools=N github=N failures=N retries=N
D errors: <none|up to 5 compact entries>

E ui_self=<v> reload=<v> other_client=<v> old_vs_new=<v>

F evidence: <up to 3 compact items separated by ;>
F limitations: <up to 3 compact items separated by ;>

SAFETY current_mutation=no historical_replay=no production=no credentials=no destructive_cleanup=no

END_SAMPLE_CARD

## 4. Не тащить доказательства целиком

Не копировать содержимое GitHub artifacts в sample.
Достаточно locator/path + blob/commit/status, если они доступны.

Не дублировать один и тот же факт в нескольких секциях.
Не писать объяснительные эссе после карточки.
Не повторять полный протокол в ответе.

## 5. Файловый режим, если доступен

Если экземпляр умеет создать локальный downloadable `.md` без GitHub-write, он МОЖЕТ дополнительно сохранить полный внутренний sample в файл:
`lifecycle-sample-<ENTITY>-v03.md`

Это не обязательное условие PASS.
ОПЕРАТОРу всё равно возвращается компактный `SAMPLE_CARD`; файл нужен только как дополнительный evidence carrier.

## 6. External collector

Current KOO/collector принимает `SAMPLE_CARD` и публикует dataset artifact сам.
Collector не реконструирует отсутствующие поля и не повышает classification.

GitHub-write пенсионера не требуется.

## 7. Terminal rule

`PASS_SAMPLE_COMPLETE` требует:
- A-F выполнены;
- safety = all no;
- карточка содержит все обязательные поля, даже если часть значений `unknown/not_available`.

`PARTIAL_SAMPLE_COMPLETE` используется, если одна или более фаз не завершены.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: сохранить диагностическую ценность v0.2, но убрать многостраничный ручной транспорт через ОПЕРАТОРА
СТАТУС: `research_protocol_candidate_for_operator_use_v03`
