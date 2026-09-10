# Многослойная память Сущности: события, путь, опыт и анти-регрессия

## Назначение

Развитие линии Entity Continuity / Task Persistence / Experience Continuity.

Цель: Сущность между сменяемыми экземплярами сохраняет не только итоговый опыт, но и значимые события, причинную цепочку, решения, неудачные попытки, evidence, открытые вопросы, изменения состояния и применимость прошлых выводов.

Отдельный chat/processing instance является временным вычислительным слоем. Долговечная память Сущности живёт вне него и должна быть проверяемой.

## Почему одного опыта недостаточно

Карточка «в следующий раз делай X» полезна, но часто теряет причину, почему X стало правильным.

Нужно сохранять путь:

`событие → наблюдение → гипотеза → действие → результат → проверка → решение → последствия → опыт`

Это позволяет не повторять проверенные ошибки, отличать правило от разового обхода, восстанавливать причинность после смены instance, пересматривать старые выводы и искать закономерности между разными задачами.

## Слои памяти

**L0 Raw event log.** Проверяемые события: входящие задачи, dispatch/receipt/acceptance, изменения файлов, результаты команд и тестов, ошибки, блокеры, переходы состояния, явные решения. Это сырьё, не «знание».

**L1 Operational state.** Активные Task ID, этап, зависимости, блокеры, safe next step, current-writer/instance state, незавершённые цепочки. Слой ответа на вопрос «где мы сейчас».

**L2 Episode / causal chain.** Связанный эпизод: `trigger → context → hypothesis → attempt → evidence → result → decision → consequence`. Он отвечает не только «что произошло», но и «как мы к этому пришли».

**L3 Experience memory.** Обобщённый опыт: lesson, next_time_behavior, failed_attempts, prohibited_repeat, applicability_boundary, confidence, freshness, supersedes, evidence_refs, behavior_test_candidate. Опыт не стирает эпизод и должен ссылаться на L2/L0.

**L4 Durable concepts and procedures.** Проверенные концепции, алгоритмы, процедуры, preflight, anti-regression scenarios и типовые рабочие паттерны.

**L5 log16 / digest layer.** Короткий высокоплотный слой cold-start: что изменилось, что важно, чего не повторять, какие решения рабочие, что открыто и куда идти за evidence.

## Навигация между слоями

`L5 digest → L4 concept/procedure → L3 experience → L2 episode → L0 evidence`

Отдельно: `L1 current state → active Task ID → связанные L2/L3/L4`.

Новая инстанция стартует с малого и углубляется только при необходимости.

## Событийная родословная

Для значимого события нужны как минимум: event_id, entity_id, task_id при наличии, instance_id при наличии, event_type, source_ref, immutable_version_ref, parents/causal_refs, observed_result, state_transition, confidence/status, проверяемое время либо явное отсутствие доверенного project-time.

Ключевой элемент — `parents/causal_refs`. Событие без причинных связей полезно как журнал, но слабее как материал для обучения.

## Анти-регрессия

Прошлый failure должен становиться не просто текстом «так нельзя», а одним из проверяемых механизмов:

`failure episode → lesson → prohibited_repeat/invariant → behavior test/preflight/validation rule → check before similar action`

Иначе память об ошибке превращается в литературу.

## Рефлексивный цикл

Помимо task-driven работы нужен consolidation:

`новые L0/L2 → поиск повторов/аномалий → candidate pattern → hypothesis → test → L3/L4 или отказ`

Состояния: `observation → hypothesis → under_test → confirmed | rejected | bounded`.

Гипотеза не становится знанием автоматически.

## Cold-start новой инстанции

1. Проверить identity/recovery/current-writer.
2. Загрузить L5 digest.
3. Загрузить L1 current state.
4. Определить активный Task ID.
5. Подобрать релевантные L4 procedures.
6. Подобрать L3 experience.
7. При конфликте углубиться в L2/L0 evidence.
8. Работать.
9. После значимого этапа писать новые события и обновлять state.
10. При завершении запускать consolidation / experience extraction.

## Принцип стоимости

Не грузить весь архив в каждый cold-start.

Использовать progressive disclosure: `digest → current state → relevant concepts → relevant experience → exact episode/evidence`.

Это уменьшает стоимость контекста и снижает риск вытеснения актуального состояния старым шумом.

## Требования к Entity supervisor

Supervisor должен уметь выбирать минимальный стартовый memory set, проверять currentness/supersedes, связывать работу с Task ID, фиксировать события и causal chain, запускать experience extraction, не превращать гипотезы в канон, инициировать anti-regression после доказанного failure и сохранять restart-safe checkpoint.

## Минимальный проверяемый эксперимент

Для одной Entity и одной Task ID:

1. создать задачу;
2. выполнить несколько шагов, включая одну контролируемую неудачную попытку;
3. сохранить L0 event, L2 episode и L3 experience;
4. завершить instance до DONE;
5. поднять новый instance;
6. восстановить L5 + L1;
7. подтянуть релевантный L3;
8. проверить, что ошибка не повторена;
9. завершить ту же Task ID;
10. сохранить DONE и обновить digest.

PASS: одна Task ID пережила смену instance; causal chain сохранилась; failure доступен новой инстанции; ошибка не повторилась; DONE подтверждён evidence; сырые события не стали автоматически «истиной».

## Статус

Рабочая архитектурная концепция и кандидат требований для дальнейшей разработки Entity supervisor / continuity memory.

Не является новым Project Source и не заменяет действующие каноны без отдельного решения КООРДИНАТОРА/ОПЕРАТОРА.

---
sender: koder
audience: koordinator, shtabist, archivarius
status: concept_candidate_for_review
project_time: omitted; trusted project-time source not used
