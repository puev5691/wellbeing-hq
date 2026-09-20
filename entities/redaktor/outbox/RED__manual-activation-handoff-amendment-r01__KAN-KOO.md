# RED → KAN + KOO: mandatory manual activation handoff amendment r0.1

status: `OPERATOR_AUTHORIZED_NORMATIVE_AMENDMENT_INPUT`
public_ready: false
approved_source_mutations_by_RED: 0
project_time: omitted; trusted project-time source not used

## Человеческий смысл

ОПЕРАТОР уточнил фактическую архитектуру текущего task conveyor: автоматического оркестратора, который гарантированно инициирует нужный ChatGPT Entity-chat, пока нет. Поэтому ОПЕРАТОР сам выполняет ручной transport/activation между чатами.

Действующие источники уже говорят, что:
- KOO формирует готовый PROMPT;
- ОПЕРАТОР передаёт его в указанный Entity-чат;
- GitHub inbox/dispatch сами по себе не являются активацией чата.

Выявленный пробел уже уже: после terminal result любая Сущность может сообщить «KOO/KAN/другая Сущность должны продолжить», но не выдать ОПЕРАТОРУ явный адрес и готовый payload. В результате ОПЕРАТОР вынужден сам догадываться, какой чат открыть и что туда написать.

ОПЕРАТОР явно распорядился закрепить обязательное правило во всех необходимых управляющих источниках.

## Обязательная норма

Пока exact scope не покрыт утверждённым и фактически работающим automatic chat-resume/orchestrator, **каждый human-facing terminal result, после которого работа должна продолжиться в другом Entity-чате, обязан содержать готовый ручной activation handoff**:

```
АДРЕСАТ: <точное имя Сущности>
PROMPT: <готовый текст, который ОПЕРАТОР может целиком вставить в адресный чат>
ДЕЙСТВИЕ ОПЕРАТОРА: открыть чат указанной Сущности и передать PROMPT.
```

ОПЕРАТОР не обязан:
- догадываться, какой чат открыть;
- самостоятельно сочинять PROMPT из GitHub status/locator/очереди;
- переносить referenced artifacts, если адресат читает их по exact locator;
- считать publication/inbox/dispatch фактом запуска Entity-чата.

Если исполнившая Сущность **не имеет authority определить следующую профильную задачу**, она не придумывает её. Используется безопасный fallback:

```
АДРЕСАТ: КООРДИНАТОР
PROMPT: Выполни fresh Resume-First reconciliation информационного поля после terminal result <exact locator/immutable identity>. Определи следующий допустимый уже авторизованный шаг. Если нужен другой Entity-чат и automatic activation для exact scope отсутствует, верни ОПЕРАТОРУ готовый блок АДРЕСАТ + PROMPT + ДЕЙСТВИЕ ОПЕРАТОРА. Не проси ОПЕРАТОРА реконструировать задачу или собирать уже доступные основания вручную.
ДЕЙСТВИЕ ОПЕРАТОРА: открыть чат КООРДИНАТОРА и передать PROMPT.
```

Фразы:
- «Сущность должна сама продолжить»;
- «результат маршрутизирован»;
- «файл лежит в inbox»;
- «PROMPT создан»;

не заменяют activation handoff, пока автоматический оркестратор не активировал exact Entity-chat.

## Требуемые source changes

### 1. `project-instructions-core-v2_2-approved.md` → новая версия

В разделе рядом с правилом ручной активации Entity-чата закрепить обязательный `АДРЕСАТ + PROMPT + ДЕЙСТВИЕ ОПЕРАТОРА` для каждого human-facing результата, требующего продолжения в другом чате.

### 2. `task-conveyor-canon-v1-approved.md` → новая версия

Закрепить:
- универсальный post-terminal manual activation handoff;
- обязательность показа блока прямо в human-facing ответе;
- fallback на KOO, если текущая Сущность не имеет authority выбрать следующую задачу;
- публикация/inbox/dispatch/receipt не отменяют необходимость manual activation payload;
- KOO после reconciliation всегда выдаёт ОПЕРАТОРУ exact address + ready-to-paste PROMPT, пока нет automatic exact-chat resume.

### 3. `entity-roles-short-v2_4-approved.md` → новая версия

В роли ОПЕРАТОРА закрепить право получать готовый `АДРЕСАТ + PROMPT + ДЕЙСТВИЕ`, а не реконструировать следующий шаг.

В роли KOO закрепить обязанность выдавать этот блок при manual conveyor.

## Что менять не требуется

`file-work canon` менять только ради этой нормы не требуется: он уже запрещает перекладывать на ОПЕРАТОРА догадки и требует короткой конкретной инструкции.

`source-loading-policy` и recovery canon по смыслу не затрагиваются.

## Prepared candidate package

RED подготовил полный пакет candidate source copies:
- `project-instructions-core-v2_3-candidate.md`;
- `task-conveyor-canon-v1_1-candidate.md`;
- `entity-roles-short-v2_5-candidate.md`.

SHA-256:
- core candidate: `7dc13c698561d379e76d3f81ec10b833fe10821ef58d42f1c497a0ab60ea0f0f`;
- conveyor candidate: `a76088a7e186871fe3ada4f152721cbe75ca182164645cd801be94fd2a00d770`;
- roles candidate: `a463e378ae12bcab5c69fed55a3005f74d0aa404df1754122f3c587052852a3c`.

## Required KAN/KOO action

KAN:
1. проверить только нормативную корректность/недублирование;
2. материализовать новые source versions по действующей процедуре;
3. не расширять scope;
4. выполнить exact readback;
5. передать результат KOO.

KOO:
1. провести source-set activation barrier согласно действующим правилам;
2. после PASS считать новые версии active;
3. не отправлять ОПЕРАТОРА обратно к RED/KAN за уже существующими основаниями;
4. если ОПЕРАТОР должен вручную активировать следующий Entity-chat, вернуть ему готовый `АДРЕСАТ + PROMPT + ДЕЙСТВИЕ`.

---
WHO: RED / РЕДАКТОР
PURPOSE: materialize explicit OPERATOR instruction into the project normative pipeline
STATUS: `READY_FOR_KAN_CANONICAL_MATERIALIZATION`
