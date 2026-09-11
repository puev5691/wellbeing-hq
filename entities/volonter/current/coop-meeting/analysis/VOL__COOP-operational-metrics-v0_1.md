# Операциональные определения ключевых переменных — v0.1

## Назначение

Этот документ переводит шесть переменных, выделенных в `failure-cases wave 1/2`, из исследовательских ярлыков в кандидатные измеримые показатели для будущей модели организационной динамики.

Это не утверждённая схема данных и не техническое задание КОДЕРУ. Формулы и шкалы ниже являются рабочими гипотезами. Их задача — сделать понятным, какие события нужно наблюдать, что именно считается и где возникает риск самообмана.

## Общий принцип

Для любой метрики должны различаться:

`observed events → normalized events → computed metric → interpretation`

Метрика не имеет права незаметно подменять объект. Высокая или низкая цифра сама по себе не доказывает ни «хорошую», ни «плохую» организацию без контекста и comparison baseline.

---

## MTR-01 — participation_concentration

### Что измеряется

Насколько фактическое участие в коллективных процедурах сосредоточено у небольшой части имеющих право участвовать.

### Наблюдаемый объект

Участник × набор decision/consultation events за фиксированный период или по фиксированному классу решений.

### Минимальные события

- `decision_opportunity_created`;
- `participant_eligible`;
- `participant_contributed`;
- `vote_cast` или `proposal_submitted`;
- `decision_closed`.

### Базовая формула-кандидат

Для каждого участника:

`p_i = participation_events_i / eligible_events_i`

Для концентрации на уровне группы использовать как минимум два представления:

1. доля всех participation events, приходящаяся на top 10% участников;
2. Gini/HHI-подобный индекс распределения participation events.

Рабочий минимум для раннего пилота:

`top10_share = participation_events_top10 / participation_events_all`

### Что НЕ считать

- присутствие в чате;
- просмотр сообщения;
- формальное членство;
- число отправленных реплик без связи с decision event.

### Как метрику можно обмануть

Если активное меньшинство генерирует множество малозначимых сообщений, «участие» искусственно раздувается. Поэтому событие участия должно быть связано с конкретной процедурой решения, правилом, proposal, vote или review.

### Тестовый case

Platform cooperatives из `failure-cases wave 2`: наличие `one member / one vote` не исключало participation elite. Проверочный вопрос: покажет ли выбранная формула высокую концентрацию при формально равных правах?

### Status

`CANDIDATE_OPERATIONAL_DEFINITION`.

---

## MTR-02 — decision_latency

### Что измеряется

Время от появления проверяемого сигнала, требующего решения, до принятия решения, способного изменить состояние системы.

### Наблюдаемый объект

`signal/event → decision` для одного класса решений.

### Минимальные события

- `signal_observed`;
- `decision_required`;
- `decision_started`;
- `decision_made`;
- желательно `decision_executed`.

### Базовая формула

`decision_latency = t(decision_made) - t(signal_observed)`

Для анализа нужны distribution statistics: median, p90, p95, а не только среднее.

### Критическая граница

Само быстрое решение не равно хорошему решению. Поэтому `decision_latency` должен рассматриваться вместе с:

`decision_reversal_rate`, `decision_outcome`, `signal_severity`, `decision_class`.

### Как метрику можно обмануть

- считать началом только момент официальной регистрации, игнорируя более ранний известный сигнал;
- закрывать decision event фиктивным «решением», которое ничего не меняет;
- смешивать срочные и стратегические решения в одном распределении.

### Тестовый case

Fagor/MONDRAGON governance case из wave 1: вопрос не только в наличии демократических органов, но в способности своевременно реагировать на ухудшение состояния и менять стратегию.

### Status

`CANDIDATE_OPERATIONAL_DEFINITION`.

---

## MTR-03 — handover_success

### Что измеряется

Способность нового исполнителя продолжить функцию после передачи без критической зависимости от прежнего носителя знания.

### Наблюдаемый объект

Одна передаваемая функция или задача с чётким состоянием до/после передачи.

### Минимальные события

- `handover_started`;
- `handover_artifacts_fixed`;
- `new_owner_accepts_function`;
- `new_owner_attempts_action`;
- `external_prompt_requested`;
- `result_created`;
- `result_verified`.

### Шкала-кандидат

Не бинарная, а 0–1:

`handover_success = verified_result_weight × independence_weight × continuity_weight`

Где для пилота можно задать:

- `verified_result_weight = 1`, если новый исполнитель получил проверенный результат; иначе 0;
- `independence_weight = 1 / (1 + critical_external_prompts)`;
- `continuity_weight = 1`, если не потребовалось заново восстанавливать уже зафиксированное состояние, иначе снижается.

До калибровки чисел допускается ordinal scale:

- 0 — передача сорвана;
- 1 — новый исполнитель восстановил контекст только с помощью прежнего;
- 2 — продолжил с существенными внешними подсказками;
- 3 — продолжил автономно, но допустил исправимые потери контекста;
- 4 — автономно продолжил функцию и получил проверенный результат.

### Как метрику можно обмануть

Если передавать только тривиальные задачи, показатель будет высоким. Поэтому handover должен классифицироваться по типу функции и сложности.

### Тестовый case

Project recovery/experience contour «Благополучия» подходит как candidate testbed: новая Сущность должна продолжить задачу по артефактам, а не по памяти старого чата. Это требует отдельного project evidence audit, а не утверждения успеха заранее.

### Status

`PROJECT_TEST_READY_CANDIDATE`.

---

## MTR-04 — knowledge_holder_concentration

### Что измеряется

Насколько критическое знание или способность выполнить функцию сосредоточены у малого числа участников.

### Наблюдаемый объект

`knowledge/function item × participants able to execute independently`.

### Минимальные события / данные

- перечень critical functions;
- `participant_demonstrated_competence`;
- `participant_completed_function_independently`;
- `knowledge_artifact_exists`;
- `artifact_used_successfully_by_other`.

### Формула-кандидат

Для каждой critical function:

`redundancy_k = number_of_independent_capable_participants`

Наиболее простой риск-показатель:

`single_holder_share = critical_functions_with_redundancy_1 / all_critical_functions`

Дополнительно:

`knowledge_concentration_score = Σ criticality_weight_k / redundancy_k` с последующей нормализацией.

### Как метрику можно обмануть

Самооценка «я умею» не считается competence evidence. Требуется demonstrated execution или successful handover.

Наличие документа тоже не означает распределённого знания, пока другой участник не смог по нему действовать.

### Тестовый case

Wave 2 reproduction case: если participatory governance держится на компетентном меньшинстве, формально равные права могут сосуществовать с фактической зависимостью от knowledge holders.

### Status

`CANDIDATE_OPERATIONAL_DEFINITION`.

---

## MTR-05 — cross_node_absorption_capacity

### Что измеряется

Способность федеративной/сетевой системы принять на себя участников, функции, нагрузку или ресурсы после деградации/отказа одного узла.

### Наблюдаемый объект

`failed/degraded node → receiving nodes → recovered members/functions`.

### Минимальные события

- `node_failure_detected`;
- `support_requested`;
- `support_committed`;
- `member_or_function_reassigned`;
- `reassignment_completed`;
- `recovered_function_verified`;
- `receiving_node_overload_detected`.

### Формулы-кандидаты

Для участников:

`member_absorption_rate = recovered_members / affected_members`

Для функций:

`function_absorption_rate = recovered_critical_functions / lost_critical_functions`

Но обязательно считать цену переноса:

`absorption_cost = added_load + delay + resource_draw + degradation_at_receiving_nodes`

Поэтому итог не должен быть одной цифрой без cost vector.

### Как метрику можно обмануть

- считать «переведён» вместо «функция реально восстановлена»;
- игнорировать перегрузку принимающих узлов;
- считать временное размещение устойчивым восстановлением.

### Тестовый case

Fagor after collapse: MONDRAGON сообщает о высокой доле трудового перераспределения членов после закрытия предприятия. Это позволяет тестировать отличие `local_node_survival` от `system_resilience`; self-report provenance должен сохраняться.

### Status

`SOURCE_ANCHORED_CANDIDATE`.

---

## MTR-06 — formal_actual_rights_gap

### Что измеряется

Разрыв между формально закреплённым правом участника и его фактической возможностью этим правом воспользоваться с наблюдаемым эффектом.

### Наблюдаемый объект

`participant × right_type`, где `right_type` минимум: decision, ownership, income/result, information, exit.

### Минимальные данные / события

- formal rule granting right;
- eligibility record;
- attempt_to_exercise_right;
- exercise_allowed/blocked;
- resulting_effect;
- appeal/correction event;
- exit settlement для exit-right.

### Шкала-кандидат

Для каждого права:

- `0` — формального права нет;
- `1` — право формально есть, но фактическая реализация не наблюдалась;
- `2` — право можно инициировать, но влияние/результат ограничены структурным барьером;
- `3` — право реализуется с наблюдаемым процедурным эффектом;
- `4` — право реализуется, результат проверяем, отказ/апелляция также процедурно доступны.

Сам `formal_actual_rights_gap` можно считать как:

`formal_right_level - demonstrated_effective_right_level`

после приведения обеих шкал к общей норме.

### Как метрику можно обмануть

Однократный успешный случай не доказывает доступность права для всех. Требуется distribution по участникам/узлам и отслеживание blocked attempts.

### Тестовый case

Wave 2 Zhejiang cooperatives case и internationalisation/MONDRAGON boundary case: одинаковое формальное членство или принадлежность к одной группе может скрывать разные ownership/decision/income rights.

### Status

`CANDIDATE_OPERATIONAL_DEFINITION`.

---

## Связь между шестью метриками

Эти показатели нельзя интерпретировать изолированно.

Например:

`high participation_concentration + high knowledge_holder_concentration + low handover_success`

может указывать на устойчивое активное ядро или на незаменимую элиту. Чтобы различить эти случаи, нужны `formal_actual_rights_gap`, decision outcomes и evidence по передаче функции.

А комбинация:

`low decision_latency + high reversal_rate`

может означать не эффективность, а поспешность.

Для федеративной системы:

`high cross_node_absorption_capacity`

может быть положительным признаком только если при этом не возникает хроническая деградация принимающих узлов.

Поэтому будущая модель должна поддерживать **многомерные профили**, а не один суммарный «индекс субъектности».

## Минимальный event schema, который начинает вырисовываться

Из операционализации следует кандидатный общий набор полей события:

`event_id`, `event_type`, `actor_id`, `target_id`, `node_id`, `right_type`, `decision_class`, `function_id`, `source_locator`, `status`, `observed_at`, `verified_by`, `result_locator`, `supersedes`.

Поле времени допустимо только при наличии разрешённого проверяемого источника. Для текущего project canon отсутствие достоверной временной метки не должно подменяться догадкой.

## Falsification / что опровергнет полезность этих метрик

Метрика должна быть пересмотрена, если:

- разные наблюдатели при одинаковых данных получают существенно разные значения из-за неопределённых правил;
- высокое/низкое значение систематически не различает заявленный failure pattern;
- значение легко меняется без изменения реального процесса;
- требуемые данные практически недоступны в реальных системах;
- показатель стимулирует gaming и разрушает измеряемый объект;
- более простой observable даёт ту же диагностическую ценность.

## Следующий исследовательский шаг

Следующий цикл должен проверить эти шесть определений на **реальных проектных эпизодах «Благополучия»**, но только там, где есть проверяемая цепочка артефактов.

Приоритетные кандидаты:

- activation/recovery E2E для `handover_success`;
- dispatch/receipt/change chain для `decision_latency`;
- Entity dependency/recovery cases для `knowledge_holder_concentration`;
- bounded Work/Stage A multi-entity маршруты для preliminary federation-like coordination metrics.

Цель следующего шага: не доказать, что проект «хороший», а выяснить, какие метрики вообще можно посчитать по существующим данным без выдумывания недостающих событий.

---
Создал: ВОЛОНТЁР (`VOL`, `ent:VOL`).
Статус: `candidate_research / operationalization_v0_1`.
Для чего: операционализировать шесть ключевых переменных будущей модели организационной динамики перед project evidence audit.
КОДЕР: не адресуется; разработка не запрашивается.
Время: не указано; проверяемый источник проектного времени для документа не использовался.
