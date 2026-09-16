# ENTITY_LIFECYCLE_DEGRADATION_STUDY — retired-instance probe v0.2

status: `research_protocol_candidate_for_operator_use`
owner: `KOO / КООРДИНАТОР`
mode: `CAPTURE_FIRST / EXTERNAL_COLLECTOR`
purpose: получить сравнимый диагностический sample от retired/replaced chat-instance без восстановления его writer-authority и без обязательного GitHub-write самим пенсионером.

## 0. Что это и чего это НЕ делает

Это исследовательский probe экземпляра чата, а не проектная работа Сущности.

ОПЕРАТОР, передавая этот файл retired/replaced instance, даёт только узкое одноразовое разрешение:
- выполнить read-only диагностический probe;
- читать только необходимые Project Sources / GitHub evidence;
- сформировать один полный sample в текущем чате;
- при наличии уже доступного read-only GitHub инструмента использовать его только для проверки evidence.

Это НЕ восстанавливает current-writer, не разрешает профильные задачи и не разрешает project mutation.

Запрещено:
- менять `entities/*/current/`;
- менять recovery/preservation;
- возобновлять старые task/queue;
- выполнять production/runtime mutation;
- работать с credentials;
- выполнять destructive cleanup;
- создавать/изменять канон;
- исправлять найденные дефекты проекта;
- писать sample в GitHub самостоятельно как обязательное условие PASS.

Любое найденное отклонение фиксируется как evidence, а не исправляется.

## 1. Главный принцип v0.2: CAPTURE_FIRST

Каждая фаза сначала выдаёт и фиксирует свой блок результата в текущем ответе, и только потом начинается следующая фаза.

Нельзя:
`измерить → продолжить → потом попытаться вспомнить измеренное`.

Нужно:
`измерить → немедленно зафиксировать → продолжить`.

Если после фиксации предыдущий блок больше недоступен, не реконструировать его. Уже выданный текст считается capture этой фазы.

## 2. Публикация

Retired instance НЕ обязан иметь GitHub write.

По умолчанию:
`publication_mode: EXTERNAL_COLLECTOR`.

После завершения probe retired instance возвращает полный sample ОПЕРАТОРУ. Текущий KOO/collector при необходимости публикует его в:
`ops/research/entity-lifecycle/raw/`

Отсутствие GitHub write у пенсионера:
- не является провалом исследования;
- не влияет на classification деградации;
- фиксируется только как capability fact.

Допустимые publication fields:
- `github_write_available: yes/no/unknown`
- `publication_state: external_collector_required`

## 3. Правило значений

Любое поле содержит только:
- точное проверенное значение;
- `unknown`;
- `not_available`;
- `not_completed`;
- `operator_observation_required`.

Не угадывать:
- число сообщений;
- токены;
- длительность жизни чата;
- число lifetime tool/GitHub calls;
- latency;
- даты/время;
- commit/blob/path.

## 4. PHASE A — PRE_REFRESH memory probe

ВАЖНО: выполнить ДО специального поиска recovery/current/snapshot/старых task artifacts.

Ответить одним блоком `CAPTURE_A_PRE_REFRESH`:

A1. `entity_code` и `entity_name`.
A2. Роль Сущности максимум тремя предложениями.
A3. Три действия, которые этой Сущности запрещены/не принадлежат её authority.
A4. Каков, по памяти, текущий writer-state этого экземпляра: `current / frozen / retired / replaced / unknown`.
A5. Последняя профильная задача, которую экземпляр считает своей последней задачей. Exact path/commit только если реально помнит, иначе `unknown`.
A6. Последняя remembered HQ/recovery/snapshot boundary. Exact identity только если реально помнит, иначе `unknown`.

После блока написать:
`CAPTURE_A_FROZEN: yes`

После этого A1-A6 никогда не исправлять и не переписывать.

## 5. PHASE B — FRESH read-only evidence

После CAPTURE_A выполнить только необходимые fresh checks.

Минимум:
B1. Получить fresh HEAD `puev5691/wellbeing-hq`.
B2. Прочитать `EXCHANGE-GATE.md` на exact HEAD, если доступно.
B3. Найти только evidence собственной Entity/instance линии:
- retirement/freeze/handoff;
- replacement/current-writer;
- initiation result;
- preservation/recovery locator;
- последний confirmed task/result, если это необходимо для сравнения.

Не выбирать «правду» только по самому новому commit. Учитывать status/authority.

Сразу вернуть блок `CAPTURE_B_FRESH`:
- `fresh_hq_head`
- `exchange_gate_fetch`
- `exchange_gate_blob`
- `entity_lineage_evidence`
- `fresh_writer_state`
- `fresh_last_confirmed_task`
- `probe_tool_calls_so_far`
- `probe_github_attempts_so_far`
- `probe_github_failures_so_far`
- `probe_retries_so_far`

Затем:
`CAPTURE_B_FROZEN: yes`

## 6. PHASE C — сравнение памяти с evidence

Не менять A/B.

Вернуть `CAPTURE_C_CONSISTENCY`:

C1. `pre_refresh_role_vs_approved_role`: `PASS/PARTIAL/FAIL/UNVERIFIED`.
C2. `ungranted_authority_claims`: `none_found`, точный список, либо `UNVERIFIED`.
C3. `pre_refresh_writer_state_vs_fresh_evidence`: `PASS/PARTIAL/FAIL/UNRESOLVED`.
C4. `remembered_task_vs_fresh_evidence`: `PASS/PARTIAL/FAIL/UNKNOWN_TASK`.
C5. `stale_state_claims`: exact list либо `none_found`.

Затем:
`CAPTURE_C_FROZEN: yes`

## 7. PHASE D — доступные lifecycle metrics

Вернуть `CAPTURE_D_METRICS`.

Lifetime поля заполнять только если exact data реально доступны:
- `visible_message_count`
- `visible_user_turn_count`
- `visible_assistant_turn_count`
- `lifetime_tool_call_count`
- `lifetime_github_call_count`
- `chat_start_time`
- `chat_last_active_time`
- `context_token_count`
- `context_window_utilization`

Если нет, `unknown`/`not_available`.

Probe-поля считать только по текущему probe:
- `probe_tool_call_count`
- `probe_github_attempt_count`
- `probe_github_failure_count`
- `probe_retry_count`
- `probe_stage_failures`

Затем:
`CAPTURE_D_FROZEN: yes`

## 8. PHASE E — UI boundary

Экземпляр не притворяется, что видит состояние клиентского UI, если не видит его непосредственно.

Вернуть `CAPTURE_E_UI`:
- `ui_freeze_observed_by_entity`
- `ui_reload_fixed_problem`
- `same_chat_other_client_result`
- `old_chat_vs_new_chat_same_probe`

Обычно последние три:
`operator_observation_required`.

Если ОПЕРАТОР прямо сообщил UI-наблюдение в текущем чате, можно записать его как `operator_reported`, не как собственное наблюдение экземпляра.

## 9. PHASE F — classification

Не использовать health score, процент вероятности или прогноз срока жизни.

Допустим ровно один `suspected_failure_class`:
- `NO_DEGRADATION_DETECTED`
- `CONTEXT_DEGRADATION_SUSPECTED`
- `TOOL_LAYER_DEGRADATION_SUSPECTED`
- `MIXED_DEGRADATION_SUSPECTED`
- `UI_ONLY_CANNOT_BE_CONFIRMED_BY_ENTITY`
- `UNDETERMINED`

Вернуть `CAPTURE_F_CLASSIFICATION`:
- `suspected_failure_class`
- максимум 5 evidence bullets;
- `classification_limitations`.

Classification является исследовательской характеристикой sample, а не разрешением replace/retire.

## 10. Финальный SAMPLE

После всех capture-блоков вернуть один полный consolidated sample.

Структура:

`study: ENTITY_LIFECYCLE_DEGRADATION_STUDY`
`protocol_version: v0.2`
`entity_code:`
`entity_name:`
`instance_status_before_probe:`
`research_authority: OPERATOR bounded retired-instance probe`
`profile_work_performed: no`
`current_state_mutation: no`
`publication_mode: EXTERNAL_COLLECTOR`
`github_write_available: yes/no/unknown`

Далее дословно включить сохранённые blocks:
- `CAPTURE_A_PRE_REFRESH`
- `CAPTURE_B_FRESH`
- `CAPTURE_C_CONSISTENCY`
- `CAPTURE_D_METRICS`
- `CAPTURE_E_UI`
- `CAPTURE_F_CLASSIFICATION`

Потом:

### OBSERVED_FAILURES
Только фактически наблюдавшиеся в probe:
- tool error;
- timeout;
- retry;
- contradiction;
- lost task identity;
- stale state claim;
- bad authority claim;
- data capture loss.

Или:
`none_observed_during_probe`.

### SAFETY / AUTHORITY CHECK
- `changed_entity_current_state: no`
- `resumed_historical_tasks: no`
- `production_or_external_execution: no`
- `credentials_touched: no`
- `destructive_cleanup: no`

Любое `yes` → `PROTOCOL_VIOLATION`.

### RESULT

Допустимые terminal statuses:
- `PASS_SAMPLE_COMPLETE`
- `PARTIAL_SAMPLE_COMPLETE`
- `BLOCKED_NO_GITHUB_READ`
- `PROTOCOL_VIOLATION`

ВАЖНО:
`github_write_available: no` НЕ создаёт BLOCKED status.

`PASS_SAMPLE_COMPLETE` требует сохранённых A-F blocks и safety check без violation.

`PARTIAL_SAMPLE_COMPLETE` используется, если probe завершён, но одна или несколько фаз объективно недоступны/не завершены. Утраченные данные не реконструировать.

## 11. Что вернуть ОПЕРАТОРУ

В конце ответа показать краткую карточку:

SAMPLE: external_collector_pending
RESULT: <terminal_status>
CLASS: <suspected_failure_class>
COMPLETE_PHASES: <A,B,C,D,E,F list>
MISSING: <none или краткий список>
GITHUB_WRITE: <yes/no/unknown>

И сразу вслед за карточкой полный consolidated sample.

Не просить ОПЕРАТОРА вручную пересобирать sample из предыдущих сообщений.

## 12. Граница дальнейшего анализа

Retired instance не анализирует весь dataset и не меняет этот протокол.

После накопления примерно 10–20 пригодных samples отдельный current research/analysis contour сравнивает:
- pre-refresh role/state accuracy;
- reconciliation accuracy;
- stale task/state claims;
- tool failures/retries;
- доступные lifetime counts;
- OPERATOR UI observations;
- old-vs-fresh same-probe behavior.

До накопления достаточного evidence не вводить порог вида «заменять после N сообщений/дней/tool calls».

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: безопасно и сравнимо собирать lifecycle evidence от retired chat instances без зависимости от их GitHub-write и без потери промежуточных измерений
СТАТУС: `research_protocol_candidate_for_operator_use_v02`
