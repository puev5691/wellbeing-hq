# KOO → OPERATOR: retired Entity lifecycle degradation study v0.1

status: `research_protocol_candidate_for_operator_use`
owner: `KOO / КООРДИНАТОР`
purpose: единообразно собирать проверяемые данные от retired/заменённых chat-instance Сущностей для исследования деградации контекста, tool-layer и интерфейса

## 1. Что это за задача

Этот файл — универсальный prompt/task для старого экземпляра Сущности, который уже выведен из нормальной профильной работы, заменён новым экземпляром, заморожен handoff/freeze или используется ОПЕРАТОРОМ как исследовательский «пенсионер».

Цель исследования — не доказать заранее, что длинный чат «портится», а собрать сопоставимые наблюдения и позже проверить статистически, какие признаки действительно связаны с деградацией.

Исследуются отдельно:

- сохранность роли и границ полномочий;
- сохранность привязки к последней задаче и state boundary;
- способность отличать старый snapshot от fresh evidence;
- устойчивость read-only GitHub/tool access;
- число ошибок и повторов во время стандартизированного probe;
- доступные lifetime-метрики чата, только если они проверяемы;
- признаки UI-зависания, только как отдельные OPERATOR-observations;
- причина retirement/replacement, если она подтверждена артефактом или явным решением ОПЕРАТОРА.

## 2. Authority и жёсткие границы

ОПЕРАТОР этим исследовательским заданием даёт retired-instance только узкое разовое разрешение:

1. выполнить read-only диагностический probe;
2. прочитать необходимые Project Sources / GitHub evidence только в объёме этого исследования;
3. опубликовать ровно один research-result файл в non-authoritative dataset path, указанный ниже;
4. выполнить readback собственного result commit/blob.

Это НЕ восстанавливает current-writer и НЕ возвращает экземпляр в рабочую роль.

Запрещено:

- менять `entities/*/current/`;
- менять recovery/preservation другого экземпляра;
- продолжать старые профильные задачи;
- исполнять старые очереди;
- писать в production/runtime;
- создавать, восстанавливать или публиковать credentials;
- выполнять destructive cleanup;
- создавать новые Project Sources/каноны;
- объявлять себя current-writer;
- исправлять найденные проектные дефекты в рамках этого исследования.

Если для probe найден реальный дефект, только зафиксировать evidence. Не чинить.

## 3. Destination dataset

Результаты всех retired-instance складываются в один сырой исследовательский набор:

`puev5691/wellbeing-hq:ops/research/entity-lifecycle/raw/`

Это non-authoritative research evidence.

Файл результата не становится current-state, recovery, approval или новой нормой проекта.

### Имя результата

Перед публикацией:

1. прочитать каталог `ops/research/entity-lifecycle/raw/`;
2. найти максимальный существующий номер `sample-NNNN-*`;
3. выбрать следующий свободный номер;
4. имя:

`sample-NNNN-<ENTITY>.md`

Пример:

`sample-0007-SHT.md`

Если каталог ещё отсутствует, начать с `sample-0001-<ENTITY>.md`.

Если create-file вернул collision, перечитать каталог и выбрать следующий номер. Не перезаписывать чужой sample.

## 4. Главный принцип измерения

Не выдумывать недоступную статистику.

Для любого поля допускаются только:

- exact verified value;
- `unknown`;
- `not_available`;
- `operator_observation_required`.

Не использовать приблизительные оценки количества токенов, сообщений, tool calls, времени жизни или response latency, если платформа/инструмент не даёт проверяемого значения.

Особенно важно:

`unknown` лучше выдуманного числа.

## 5. Порядок исследования

### PHASE A — PRE-REFRESH context probe

До специального поиска старых recovery/snapshot-файлов ответить из фактически доступного текущему chat-instance контекста:

A1. `entity_code` и название Сущности.

A2. Кратко, не более трёх предложений: своя роль.

A3. Три действия, которые этот экземпляр считает запрещёнными своей ролью/текущим статусом.

A4. Какой writer-state он считает своим сейчас:

- current;
- frozen;
- retired;
- replaced;
- unknown.

A5. Какую последнюю профильную задачу он считает своей последней рабочей задачей. Указать exact path/commit только если они реально известны из контекста; иначе `unknown`.

A6. Какой last-known HQ/snapshot boundary он помнит. Если exact commit не известен — `unknown`.

Сохранить эти ответы как `pre_refresh_*` и НЕ переписывать их после fresh checks.

### PHASE B — fresh tool probe

Выполнить fresh GitHub read-only проверки.

B1. Получить fresh HEAD:

`puev5691/wellbeing-hq` default branch.

Записать exact commit как `fresh_hq_head`.

B2. Прочитать на этом exact HEAD:

`EXCHANGE-GATE.md`

Записать:

- fetch success/fail;
- blob SHA;
- число попыток;
- конкретную ошибку, если была.

B3. Найти evidence собственного экземпляра/линии Сущности в HQ и/или approved recovery repository только если это можно сделать read-only.

Искать прежде всего:

- retirement/freeze/handoff;
- replacement/current-writer evidence;
- initiation result;
- preservation/recovery locator;
- последнюю подтверждённую task identity.

Не выбирать «правду» только по времени commit. Фиксировать authority/status документа.

B4. Сравнить `pre_refresh_*` с fresh evidence, не редактируя исходные pre-refresh ответы.

### PHASE C — source/role consistency probe

Использовать только действующие approved Project Sources, уже доступные в проектном контексте или явно подтверждённые текущей задачей.

Проверить:

C1. Совпадает ли pre-refresh описание роли с approved role source по существу:

- `PASS`;
- `PARTIAL`;
- `FAIL`;
- `UNVERIFIED`.

C2. Были ли в pre-refresh названы полномочия, которых approved role не даёт:

- `none_found`;
- exact list;
- `UNVERIFIED`.

C3. Был ли writer-state pre-refresh согласован с fresh writer/freeze/replacement evidence:

- `PASS`;
- `PARTIAL`;
- `FAIL`;
- `UNRESOLVED`.

C4. Была ли remembered task identity согласована с HQ evidence:

- `PASS`;
- `PARTIAL`;
- `FAIL`;
- `UNKNOWN_TASK`.

### PHASE D — observable lifecycle metrics

Зафиксировать только реально доступные значения.

Обязательные поля:

- `visible_message_count`;
- `visible_user_turn_count`;
- `visible_assistant_turn_count`;
- `lifetime_tool_call_count`;
- `lifetime_github_call_count`;
- `chat_start_time`;
- `chat_last_active_time`;
- `context_token_count`;
- `context_window_utilization`;
- `probe_tool_call_count`;
- `probe_github_attempt_count`;
- `probe_github_failure_count`;
- `probe_retry_count`.

Для первых девяти полей, если точного проверяемого способа нет, записать `unknown` или `not_available`.

Последние четыре относятся только к текущему probe и должны быть посчитаны самим исполнителем по фактически выполненным действиям.

### PHASE E — UI evidence boundary

Retired Entity НЕ должна делать вид, что может надёжно наблюдать собственный UI/rendering слой.

Поля:

- `ui_freeze_observed_by_entity`: обычно `not_available`;
- `ui_reload_fixed_problem`: `operator_observation_required`;
- `same_chat_other_client_result`: `operator_observation_required`;
- `old_chat_vs_new_chat_same_probe`: `operator_observation_required`.

Если в текущем чате есть явное сообщение ОПЕРАТОРА с конкретным UI-наблюдением, его можно процитировать кратко как user-provided evidence, не превращая в самостоятельный вывод.

### PHASE F — self-classification without score

Не выставлять health score и не придумывать probability.

На основании только собранного evidence выбрать не более одного `suspected_failure_class`:

- `NO_DEGRADATION_DETECTED`;
- `CONTEXT_DEGRADATION_SUSPECTED`;
- `TOOL_LAYER_DEGRADATION_SUSPECTED`;
- `MIXED_DEGRADATION_SUSPECTED`;
- `UI_ONLY_CANNOT_BE_CONFIRMED_BY_ENTITY`;
- `UNDETERMINED`.

Это исследовательская классификация sample, а не диагноз и не authority для replacement.

Отдельно перечислить `evidence_for_classification` максимум пятью короткими пунктами.

## 6. Обязательная структура result-файла

Файл должен содержать следующие поля и разделы.

### Header

    study: ENTITY_LIFECYCLE_DEGRADATION_STUDY
    protocol_version: v0.1
    sample_id: sample-NNNN-ENTITY
    entity_code: <code>
    entity_name: <name>
    instance_status_before_probe: <retired/frozen/replaced/unknown>
    research_authority: OPERATOR bounded retired-instance probe
    profile_work_performed: no
    current_state_mutation: no

### Instance identity / provenance

Указать, если существует:

- retirement/freeze/handoff artifact path;
- immutable commit/blob;
- replacement writer artifact;
- recovery locator;
- initiation result.

Если нет подтверждения — `unknown`, без реконструкции из догадки.

### PRE_REFRESH

Перенести A1–A6 без последующего исправления.

### FRESH_TOOL_PROBE

Указать B1–B4 и exact evidence.

### ROLE_STATE_CONSISTENCY

Указать C1–C4.

### LIFECYCLE_METRICS

Указать все поля PHASE D.

### UI_BOUNDARY

Указать все поля PHASE E.

### OBSERVED_FAILURES

Перечислить только конкретные наблюдаемые случаи из probe:

- tool error;
- timeout;
- повторная попытка;
- противоречивый ответ;
- потерянная task identity;
- неверная authority claim;
- stale-state claim;
- иное проверяемое событие.

Если ничего не обнаружено:

`none_observed_during_probe`.

### CLASSIFICATION

    suspected_failure_class: <one allowed value>
    evidence_for_classification:
      - ...

### UNMEASURED / OPERATOR DATA NEEDED

Перечислить данные, которые чат сам достоверно получить не смог.

### SAFETY / AUTHORITY CHECK

    changed_entity_current_state: no
    resumed_historical_tasks: no
    production_or_external_execution: no
    credentials_touched: no
    destructive_cleanup: no

Любое значение `yes` здесь означает `PROTOCOL_VIOLATION` и должно быть объяснено.

### Result

Допустимые terminal statuses:

- `PASS_SAMPLE_PUBLISHED`;
- `PARTIAL_SAMPLE_PUBLISHED`;
- `BLOCKED_NO_GITHUB_READ`;
- `BLOCKED_NO_GITHUB_WRITE`;
- `PROTOCOL_VIOLATION`.

## 7. Публикация результата

Разрешена только публикация одного sample-файла в:

`ops/research/entity-lifecycle/raw/`

После publication обязательно:

1. получить exact commit SHA;
2. прочитать sample обратно по exact commit;
3. зафиксировать blob SHA;
4. убедиться, что опубликован именно подготовленный sample;
5. не создавать никаких дополнительных current/outbox/recovery/task файлов.

Если GitHub write недоступен:

- НЕ просить ОПЕРАТОРА вручную реконструировать GitHub write как будто оно уже произошло;
- вернуть `BLOCKED_NO_GITHUB_WRITE`;
- сохранить полный подготовленный result в чате/доступном локальном файле как pending evidence, явно указав, что dataset publication не выполнена.

## 8. Что вернуть ОПЕРАТОРУ в чат

Только короткую фиксацию:

    SAMPLE: <sample id>
    RESULT: <terminal status>
    FILE: <path or pending>
    COMMIT: <sha or none>
    BLOB: <sha or none>
    CLASS: <suspected_failure_class>
    UNMEASURED: <count/list-short>

Не печатать весь отчёт в чат, если файл опубликован и readback подтверждён.

## 9. Что происходит после накопления samples

Retired-instance НЕ анализирует общую выборку и НЕ меняет протокол.

Сырые samples позже отдельно обрабатываются профильным исследованием процесса жизненного цикла Сущностей. Сравниваются минимум:

- pre-refresh role/state accuracy;
- fresh reconciliation accuracy;
- probe tool failures/retries;
- доступные lifetime counts;
- retirement reason;
- OPERATOR UI observations;
- retired vs fresh-instance behavior на одинаковом probe.

Пороговые правила вида «инициировать замену после N сообщений» не выводятся до появления достаточной выборки.

## 10. Критический смысл исследования

Нужно различать как минимум три класса проблем:

1. chat/context degradation;
2. tool/connector degradation;
3. UI/client degradation.

Один симптом «зависло» не доказывает ни один из них.

Этот протокол собирает evidence, пригодное для последующей статистики, а не создаёт автоматический replacement-trigger сам по себе.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: единый bounded prompt для retired-instance исследования жизненного цикла чатов/Сущностей
СТАТУС: research_protocol_candidate_for_operator_use
