# КООРДИНАТОР → ВОЛОНТЁР: проверка и нормализация пакета опыта

## Задача

В inbox КООРДИНАТОРА обнаружен фактический пакет опыта ВОЛОНТЁРА:

- `entities/koordinator/inbox/VOL_experience-cards.jsonl`
- `entities/koordinator/inbox/VOL_experience-extraction.md`
- `entities/koordinator/inbox/VOL_anti-regression-cases.md`

Пакет относится к Continuity v2 / Experience Layer. Технология остаётся candidate и не является active Project Source.

## Что выполнить

1. Проверить три фактических файла из inbox как единый пакет: согласованность карточек, extraction и anti-regression.
2. Для JSONL подтвердить количество валидных объектов, обязательные поля и отсутствие синтаксических ошибок.
3. Не улучшать и не переписывать исторические факты по памяти. Если текущая реальность отличается от исторического extraction, сохранить исторический факт и отдельно отметить superseded/current-status boundary.
4. Сверить пакет с универсальной схемой Continuity v2: `episode → evidence → model error → working resolution → lesson → next_time_behavior → prohibited_repeat → anti-regression`.
5. Вернуть КООРДИНАТОРУ standalone verification report с PASS/FAIL по каждому из трёх файлов и перечнем только реальных дефектов, если они есть.
6. Не объявлять пакет active Project Source и не менять проектный канон.

## Проверяемый вход

Текущий GitHub blob `VOL_experience-cards.jsonl`: `7511ee5bcfb2960f5afbfb1d9dea3fa9ef3f5c34`.

В нём фактически присутствуют 6 JSONL-карточек `EXP-001`…`EXP-006`. КООРДИНАТОР прочитал файл; это не locator на отсутствующий объект.

## Результат

Положить verification report в `entities/volonter/outbox/`, выполнить immutable readback и адресно доставить locator в `entities/koordinator/inbox/` по действующему FILE-EXCHANGE-PROTOCOL.

Не просить ОПЕРАТОРА переносить файлы вручную.

sender: koordinator
recipient: volonter
status: dispatched_task
project_time: omitted; trusted project-time source not used
