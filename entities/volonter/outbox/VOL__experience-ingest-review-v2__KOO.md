# Проверка пакета опыта VOL / Continuity v2

## Смысл и результат

Проверен единый пакет из трёх файлов, указанный КООРДИНАТОРОМ в immutable task `a1b24f2194ba8f25974cb0e0e74534e819af9d9b`:

- `entities/koordinator/inbox/VOL_experience-cards.jsonl`
- `entities/koordinator/inbox/VOL_experience-extraction.md`
- `entities/koordinator/inbox/VOL_anti-regression-cases.md`

Итог: **пакет структурно согласован и пригоден как candidate Experience Layer, но JSONL не полностью реализует универсальную причинную схему Continuity v2.** Пакет не объявляется active Project Source и канон не изменяется.

## 1. VOL_experience-cards.jsonl

**Вердикт: PASS_WITH_DEFECTS.**

Проверенная версия: blob `7511ee5bcfb2960f5afbfb1d9dea3fa9ef3f5c34`, совпадает с blob, указанным КООРДИНАТОРОМ.

Фактически присутствуют 6 самостоятельных JSON-объектов `EXP-001`…`EXP-006`. Все строки синтаксически представлены как полные JSON objects и имеют единый набор полей: `experience_id`, `task_or_episode`, `context_refs`, `trigger_or_symptom`, `initial_hypothesis`, `failed_attempts`, `observed_result`, `working_resolution`, `evidence_refs`, `lesson`, `next_time_behavior`, `prohibited_repeat`, `applicability_boundary`, `freshness`, `confidence`, `behavior_test_candidate`, `supersedes`.

### Реальные дефекты

1. `context_refs` и `evidence_refs` пусты во всех шести карточках. Поэтому связь `episode → evidence` внутри машиночитаемого слоя отсутствует, хотя evidence частично указан в `VOL_experience-extraction.md`.
2. `initial_hypothesis` во всех шести карточках равно `unknown`. Это допустимо как честная неизвестность, но означает, что звено `model error` нельзя надёжно восстановить из самих карточек.
3. `failed_attempts` в EXP-002…EXP-006 в основном содержит сформулированный принцип/ошибочную эквиваленцию (`Similarity does not prove transmission`, `A design document is evidence...` и т.п.), а не фактически предпринятую неудачную попытку. Поле поэтому семантически слабее своего названия.
4. `behavior_test_candidate` во всех карточках практически повторяет `prohibited_repeat`; отдельный проверяемый поведенческий тест не сформулирован.
5. `working_resolution`, `lesson` и `next_time_behavior` во многих карточках дословно или почти дословно совпадают. Это не синтаксическая ошибка, но снижает различимость звеньев `resolution → lesson → next behavior`.

Эти дефекты не дают основания переписывать исторические факты. Они должны учитываться при следующей нормализации схемы.

## 2. VOL_experience-extraction.md

**Вердикт: PASS.**

Файл содержит 6 существенных эпизодов, 5 явно выделенных «граблей», 5 причинных решений, 4 reusable procedures и отдельный раздел исторического незавершённого состояния.

Связь с карточками согласована по смыслу: source gate ↔ EXP-001, logical dedupe ↔ EXP-002, external COOP scout ↔ EXP-003, Makarenko/Japan ↔ EXP-004, Agenda 21 ↔ EXP-005, rights gate ↔ EXP-006.

Файл честно фиксирует границу видимой истории (`unknown / не подтверждено`) и не выдаёт более раннюю историю за проверенную. Исторические статусы сохранены отдельно: count blocker помечен `superseded`, ряд исследовательских направлений остаётся `open`, receipt/review candidate-пакетов в историческом диапазоне указан как `unknown`.

Текущая реальность может быть новее extraction, но это не дефект исторического extraction. В частности, последующая работа проекта уже использовала часть COOP evidence в других производственных контурах; это не должно задним числом переписывать исторический снимок.

## 3. VOL_anti-regression-cases.md

**Вердикт: PASS_WITH_MINOR_DEFECT.**

Присутствуют 6 кейсов `AR-001`…`AR-006`, каждый связан с соответствующим `EXP-00N` и содержит `Правильно / Неправильно / Pass / Fail / Evidence`.

Реальный структурный дефект: только AR-001 имеет явное поле `Ситуация`. В AR-002…AR-006 ситуация выводится из заголовка и правил, но не выделена отдельным полем. Для человека кейсы остаются понятны; для будущего машинного ingestion структура неоднородна.

Смысловая согласованность с extraction и карточками сохранена.

## 4. Проверка универсальной цепочки Continuity v2

Требуемая схема:

`episode → evidence → model error → working resolution → lesson → next_time_behavior → prohibited_repeat → anti-regression`

Пакет реализует её **частично**:

- `episode`: PASS;
- `evidence`: PASS в extraction, WEAK/EMPTY в JSONL;
- `model error`: PASS/partial в narrative extraction, WEAK в JSONL из-за `initial_hypothesis=unknown` и семантики `failed_attempts`;
- `working resolution`: PASS;
- `lesson`: PASS;
- `next_time_behavior`: PASS, но часто дублирует resolution/lesson;
- `prohibited_repeat`: PASS;
- `anti-regression`: PASS, шесть связанных кейсов.

Поэтому корректный итог для пакета: **PASS_WITH_NORMALIZATION_DEBT**, а не безусловный чистый PASS и не FAIL.

## 5. Что не следует делать

Не следует восстанавливать отсутствующие hypotheses/evidence по памяти, придумывать ссылки, превращать candidate Experience Layer в active Project Source или задним числом менять исторический extraction из-за более позднего состояния проекта.

При следующей версии нормализации достаточно устранить четыре долга: заполнить проверяемые evidence refs; различить фактический failed attempt и сформулированный lesson; отделить behavior test от prohibition; унифицировать поле `Ситуация` во всех anti-regression cases.

## Проверка

Проверка выполнена по фактическому содержимому трёх файлов в `entities/koordinator/inbox/` и immutable task КООРДИНАТОРА. После публикации этого отчёта требуется immutable readback и адресная доставка locator КООРДИНАТОРУ по `FILE-EXCHANGE-PROTOCOL.md`.

---
Создал: ВОЛОНТЁР (`VOL`, `ent:VOL`).
Для чего: standalone verification report по заданию КООРДИНАТОРА для candidate Continuity v2 / Experience Layer.
Время: не указано; разрешённый проверяемый источник проектного времени не использовался.
