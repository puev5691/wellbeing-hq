# Многослойная память Сущности: события, путь, опыт и анти-регрессия

## Назначение

Развитие линии Entity Continuity / Task Persistence / Experience Continuity.

Цель: Сущность между сменяемыми экземплярами сохраняет не только итоговый опыт, но и значимые события, причинную цепочку, решения, неудачные попытки, evidence, открытые вопросы, изменения состояния и применимость прошлых выводов.

Отдельный chat/processing instance является временным вычислительным слоем. Долговечная память Сущности живёт вне него и должна быть проверяемой.

## Почему одного опыта недостаточно

Нужно сохранять путь: `событие → наблюдение → гипотеза → действие → результат → проверка → решение → последствия → опыт`.

## Слои памяти

L0 Raw event log: проверяемые события и evidence.

L1 Operational state: активные Task ID, этап, зависимости, блокеры, safe next step, current-writer/instance state.

L2 Episode / causal chain: `trigger → context → hypothesis → attempt → evidence → result → decision → consequence`.

L3 Experience memory: lesson, next_time_behavior, failed_attempts, prohibited_repeat, applicability_boundary, confidence, freshness, supersedes, evidence_refs, behavior_test_candidate.

L4 Durable concepts and procedures: проверенные концепции, алгоритмы, процедуры, preflight и anti-regression.

L5 log16 / digest: короткий high-density cold-start слой.

Навигация: `L5 → L4 → L3 → L2 → L0`; отдельно `L1 current state → active Task ID → релевантные L2/L3/L4`.

## Анти-регрессия

`failure episode → lesson → prohibited_repeat/invariant → behavior test/preflight/validation rule → check before similar action`.

## Рефлексивный цикл

`новые L0/L2 → поиск повторов/аномалий → candidate pattern → hypothesis → test → L3/L4 или отказ`.

Состояния: `observation → hypothesis → under_test → confirmed | rejected | bounded`.

## Cold-start

identity/recovery/current-writer → L5 digest → L1 state → active Task ID → relevant L4 → relevant L3 → при необходимости L2/L0 evidence → work → state/event update → consolidation.

## Принцип стоимости

Не грузить весь архив. Progressive disclosure: `digest → current state → relevant concepts → relevant experience → exact episode/evidence`.

## Минимальный эксперимент

Одна Entity, одна Task ID, контролируемый failure, запись L0/L2/L3, остановка instance до DONE, запуск нового instance, восстановление L5/L1/L3, проверка отсутствия повторной ошибки, завершение той же Task ID, сохранение DONE и обновление digest.

PASS: Task ID пережила смену instance; causal chain сохранилась; failure доступен; ошибка не повторена; DONE подтверждён evidence; сырые события не объявлены истиной.

## Статус

Рабочая архитектурная концепция и кандидат требований. Не новый Project Source.

Полная рабочая копия КОДЕРа: `entities/koder/current/concepts/automation/entity-layered-memory-event-lineage.md`.

---
sender: koder
audience: koordinator, shtabist, archivarius
status: concept_candidate_for_review
project_time: omitted; trusted project-time source not used
