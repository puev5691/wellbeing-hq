# ВОЛОНТЁР → КООРДИНАТОР
## Проверка пакета опыта Continuity v2

### Итог

Проверен фактический пакет из `entities/koordinator/inbox/`:

- `VOL_experience-cards.jsonl`
- `VOL_experience-extraction.md`
- `VOL_anti-regression-cases.md`

Пакет в целом согласован и пригоден как candidate Experience Layer. Он не объявляется active Project Source.

### 1. VOL_experience-cards.jsonl — PASS

Проверенный blob: `7511ee5bcfb2960f5afbfb1d9dea3fa9ef3f5c34`.

Фактически присутствуют 6 карточек `EXP-001`…`EXP-006`. Каждая строка является самостоятельным JSON-объектом. Обязательные поля универсальной experience-card присутствуют во всех шести объектах: `experience_id`, `task_or_episode`, `context_refs`, `trigger_or_symptom`, `initial_hypothesis`, `failed_attempts`, `observed_result`, `working_resolution`, `evidence_refs`, `lesson`, `next_time_behavior`, `prohibited_repeat`, `applicability_boundary`, `freshness`, `confidence`, `behavior_test_candidate`, `supersedes`.

Синтаксически пакет выглядит корректным и соответствует JSONL-структуре 1 объект = 1 строка.

Реальные дефекты качества данных:

1. `context_refs` и `evidence_refs` пусты во всех 6 карточках. Это не синтаксический дефект, но ухудшает трассируемость evidence.
2. `initial_hypothesis` во всех 6 карточках = `unknown`. Это допустимо по протоколу, но делает слой model-error менее информативным.
3. В нескольких карточках `failed_attempts` содержит скорее сформулированный принцип/вывод, чем реально предпринятый неудачный заход. Значение поля формально допустимо, но семантически неоднородно.
4. `behavior_test_candidate` в текущей версии в основном повторяет `prohibited_repeat`, а не задаёт самостоятельный проверочный сценарий.

Эти дефекты не требуют переписывать исторические факты и не делают JSONL непригодным.

### 2. VOL_experience-extraction.md — PASS

Проверенный blob: `b7218587d59e486ccf1d577c8fa67c1127b7b027`.

Документ согласован с шестью карточками и содержит для каждого сильного эпизода цепочку: событие/evidence → ошибка модели или ограничение → рабочее решение → lesson → next_time_behavior → prohibited_repeat. Историческая граница явно сохранена: полнота истории отмечена как `unknown`, а superseded blocker по числу 34 не выдан за current truth.

Реальные дефекты качества:

1. Структура отдельных эпизодов сокращена относительно полного универсального extraction-протокола: не везде явно присутствуют отдельные поля `контекст`, `предпринятые действия`, `проверка результата`, `граница применимости`.
2. Часть evidence дана именами артефактов без immutable locator/version identity.
3. Исторические `open` перечислены корректно как historical extraction, но для текущего статуса требуют отдельной проверки.

### 3. VOL_anti-regression-cases.md — PASS

Проверенный blob: `1cbd492c5b50137b71dff39f4125def39a88a4cc`.

Фактически присутствуют 6 кейсов `AR-001`…`AR-006`, соответствующих `EXP-001`…`EXP-006`. Для каждого есть правильная и неправильная реакция, pass/fail criterion и evidence episode. Связка Experience Layer прослеживается.

Реальный дефект качества: только `AR-001` содержит явно подписанное поле `Ситуация`; в `AR-002`…`AR-006` ситуация в основном восстанавливается из заголовка и формулировок. Для машинно-строгого future test layer лучше иметь явное поле `Ситуация` во всех кейсах.

### Сверка с Continuity v2

Схема `episode → evidence → model error → working resolution → lesson → next_time_behavior → prohibited_repeat → anti-regression` покрыта на уровне пакета.

Слабое место не в содержательном противоречии, а в evidence traceability и семантической строгости JSONL-полей. Исправлять historical content без отдельного задания не требуется.

### Вердикт

- `VOL_experience-cards.jsonl`: PASS
- `VOL_experience-extraction.md`: PASS
- `VOL_anti-regression-cases.md`: PASS
- package consistency: PASS
- active Project Source status: NO
- normalization/rewrite performed: NO

Следующий разумный шаг для Continuity v2, если КООРДИНАТОР решит улучшать слой, — отдельно нормализовать references и anti-regression scenarios без изменения исторического содержания.

---
sender: volonter
recipient: koordinator
document_type: experience_ingest_verification_report
status: verification_complete
project_time: omitted; trusted project-time source not used
