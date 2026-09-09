# VOL experience extraction

## 1. Роль и граница истории

**Entity:** ВОЛОНТЁР (`VOL`). Роль подтверждается адресованными этому чату заданиями КООРДИНАТОРА.

**Фактическая работа в просмотренном диапазоне:** COOP-исследования; корпус Бобровского; dedupe/provenance; внешний поиск мыслителей, практиков и институтов; evidence/rights gates; candidate-материалы для КООРДИНАТОРА.

**Диапазон:** от `KOO__COOP-bobrovsky-34-corpus__VOL.md` через внешний COOP-разведконтур, Макаренко и Agenda 21 до `KOO__OLD-CHAT-experience-extraction-task.md`.

**Виден ли чат от начала:** `unknown / не подтверждено`. Более ранние эпизоды не включены как evidence.

## 2. Существенные рабочие эпизоды

### Source-gate корпуса Бобровского
**Задача:** принять полный входной корпус.
**Исходная модель:** число 34 было воспринято как жёсткий acceptance gate.
**Evidence:** обнаружено больше file identities; ОПЕРАТОР прямо уточнил, что число некритично и могло быть ошибочным.
**Действия:** сначала зафиксирован `BLOCKED_INPUT_SET_MISMATCH`, затем explicit override снял blocker.
**Рабочее решение:** весь фактически доступный корпус принимается; дубли схлопываются по содержанию с сохранением provenance.
**Lesson:** count gate действителен только пока подтверждено его основание.
**next_time_behavior:** различать count requirement и identity/provenance requirement.
**prohibited_repeat:** не выбирать произвольно «правильные N» и не держать superseded blocker.
**Граница:** подписанный/хешированный manifest остаётся жёстким.
**Актуальность:** `reusable`.
**Evidence:** `KOO__COOP-bobrovsky-34-corpus__VOL.md`, `VOL__BOBROVSKY-34-source-gate__KOO.md`, `VOL__BOBROVSKY-source-gate-override__KOO.md`.

### Logical dedupe без ложного exact identity
**Задача:** убрать повторные экземпляры.
**Evidence:** одинаковые/совпадающие тексты встречались под разными file identities; raw bytes были недоступны.
**Рабочее решение:** `content_duplicate / byte_identity_unknown`; одна logical work, все identities остаются в provenance; различия дают variant/revision.
**Lesson:** logical dedupe и byte-exact verification — разные операции.
**next_time_behavior:** сначала сравнивать содержание, exact identity подтверждать bytes/hash.
**prohibited_repeat:** не выдумывать SHA-256.
**Актуальность:** `reusable`.

### Внешний COOP-разведконтур
**Задача:** искать не только кооператоров, а авторов/практиков/институты с полезными социальными механизмами.
**Evidence:** KOO задал mechanism-first фильтр и обязательную карту критики/провалов.
**Действия:** создана wave1 с registry, primary-source index, concept map, failure map и research queue.
**Рабочее решение:** библиотека строится вокруг механизмов и evidence, а не пантеона имён.
**Lesson:** известность субъекта не повышает evidence strength.
**next_time_behavior:** primary locator → claim → evidence → criticism/failure → COOP relevance.
**prohibited_repeat:** biography/reference page не заменяет primary source.
**Актуальность:** `requires-current-check` (пакет candidate, receipt/review KOO в видимом диапазоне неизвестен).

### Макаренко и японская линия
**Задача:** проверить предполагаемое использование решений Макаренко в японской мотивации/управлении.
**Evidence:** найдены функциональные параллели и линия японской педагогической рецепции; прямой corporate causal link не подтверждён.
**Рабочее решение:** `UNVERIFIED_DIRECT_CAUSAL_LINK`.
**Lesson:** функциональная аналогия не доказывает исторического влияния.
**next_time_behavior:** искать transmission chain: датировка → перевод/читатель → институт → конкретная практика/ссылка.
**prohibited_repeat:** не писать «заимствовали» без источника.
**Актуальность:** `reusable`.

### Agenda 21 / Local Agenda 21
**Задача:** проверить полезность для библиотеки активации социума.
**Evidence:** выделена архитектура local participation, major groups, совместного планирования и мониторинга.
**Рабочее решение:** классифицировать как research lead по participatory governance/local self-organization; эффективность проверять отдельно по кейсам.
**Lesson:** полезный механизм может находиться вне литературы с ярлыком «кооперация».
**next_time_behavior:** после нормативного design искать outcome evidence.
**prohibited_repeat:** не принимать нормативную архитектуру за доказанную эффективность.
**Актуальность:** `reusable`.

### Rights gate
**Задача:** расширять библиотеку внешними трудами безопасно для будущего public repo.
**Evidence:** KOO прямо запретил копировать полные чужие тексты без подтверждённого права.
**Рабочее решение:** locator + metadata + собственный analysis по умолчанию; fulltext только после rights basis.
**Lesson:** public availability ≠ republication permission.
**next_time_behavior:** rights status фиксировать до public-ready ingestion.
**prohibited_repeat:** не тащить полный текст в публичный слой только потому, что он доступен онлайн.
**Актуальность:** `reusable`.

## 3. Плантация граблей

### Грабля: формальный count превращён в абсолют
- **Проявление:** работа остановилась на несовпадении 34.
- **Причина:** формальный KOO gate был принят буквально.
- **Обнаружение:** explicit correction ОПЕРАТОРА.
- **Правильный подход:** после override сохранить provenance и снять устаревший blocker.
- **Anti-regression:** приблизительный count не должен блокировать при явном разрешении ОПЕРАТОРА.

### Грабля: content duplicate назван exact duplicate
- **Проявление:** одинаковый текст, разные identities, bytes недоступны.
- **Причина:** смешение logical и byte identity.
- **Правильный подход:** `content_duplicate / byte_identity_unknown`.
- **Anti-regression:** exact допустим только при достаточной identity-проверке.

### Грабля: сходство = влияние
- **Проявление:** Макаренко ↔ японские групповые практики.
- **Причина:** сильная функциональная аналогия.
- **Правильный подход:** causal claim остаётся unverified без transmission evidence.
- **Anti-regression:** сходство двух систем не даёт права писать «B взял у A».

### Грабля: design = outcome
- **Проявление:** Agenda 21 описывает механизм участия.
- **Причина:** нормативный текст легко принять за evidence эффективности.
- **Правильный подход:** отдельный case/outcome track.
- **Anti-regression:** масштаб распространения программы не равен доказанному успеху.

### Грабля: online = можно перепубликовать
- **Проявление:** найден внешний полный текст.
- **Причина:** смешение доступа и прав.
- **Правильный подход:** locator-first до проверки rights.
- **Anti-regression:** публичный PDF без лицензии не попадает целиком в public-ready repo.

## 4. Причинные решения

1. `count mismatch → stop | arbitrary selection → stop по исходному KOO gate → arbitrary selection rejected → OPERATOR override → blocker superseded`.
2. `duplicate identities → exact | content duplicate | variant → content duplicate → exact rejected без bytes → provenance preserved`.
3. `Makarenko/Japan similarity → influence | comparison → comparison → causal wording rejected → direct link unknown`.
4. `Agenda 21 → normative architecture | outcome proof → architecture → outcome claim rejected → case-study verification required`.
5. `external fulltext → copy | locator-first → locator-first → open-access-as-rights rejected → rights gate`.

## 5. Reusable procedures

### Corpus intake + logical dedupe
Инвентаризация → provenance → normalized-text comparison → logical dedupe → variant detection → byte/hash exact check при доступности.  
**Stop:** authoritative membership реально неясно и влияет на acceptance.

### External mechanism scout
Механизм → субъект/кейс → primary locator → claim class → evidence → independent criticism/failure → COOP comparison.  
**Stop:** сильный claim не имеет источника.

### Influence verification
Исходный механизм → сходный механизм → chronology → transmission channel → direct evidence.  
Без последних звеньев: `comparison candidate`, не influence fact.

### Rights-safe ingestion
Locator/metadata → provenance → rights basis → derived layer → fulltext только при подтверждённых правах.  
**Stop:** republication rights unknown.

## 6. Историческое незавершённое состояние

- `open`: full-corpus normalization Бобровского после снятия count blocker.
- `open`: внешний COOP scout после wave1.
- `open`: проверка прямого влияния Макаренко на японский corporate management.
- `open`: Local Agenda 21 case-study layer.
- `superseded`: `BLOCKED_INPUT_SET_MISMATCH` по числу 34.
- `unknown`: KOO receipt/review candidate-пакетов.
- `unknown`: полнота истории до начала просмотренного диапазона.
- `parked`: не зафиксировано.
- `blocked`: не зафиксировано на конце просмотренного диапазона.

## EXTRACTION_REPORT

- просмотренный диапазон: `KOO__COOP-bobrovsky-34-corpus__VOL.md` → `KOO__OLD-CHAT-experience-extraction-task.md`;
- чат от начала: `unknown`;
- недоступные участки: более ранняя история вне видимого диапазона;
- существенные эпизоды: **6**;
- грабли: **5**;
- причинные решения: **5**;
- reusable procedures: **4**;
- experience cards: **6**;
- anti-regression cases: **6**;
- значимые `unknown`: **4**;
- направления: Bobrovsky corpus, dedupe/provenance, external COOP scout, causal verification, Agenda 21, rights-safe ingestion;
- за пределами extraction могли остаться ранние эпизоды VOL.
