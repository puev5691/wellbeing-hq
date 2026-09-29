# OPERATOR decision — REUSE-FIRST GATE r0.1

status: OPERATOR_APPROVED_DECISION
entity_scope: ALL_PROJECT_ENTITIES
project_time: omitted

## Человеческий смысл

ОПЕРАТОР явно утвердил обязательное правило повторного использования уже доказанного рабочего опыта перед изобретением нового технического способа исполнения.

Решение возникло после конкретного anti-regression случая:
для размещения preservation-скрипта на p552203 уже существовал рабочий путь Desktop Commander `write_file` с chunking, однако ARH сначала отклонился в лишний Termux/scp маршрут.

## Approved rule

`REUSE_FIRST_GATE = REQUIRED`

Перед выбором нового технического способа исполнения Сущность обязана проверить:

1. есть ли уже успешный результат для такого же класса задачи;
2. есть ли Experience / anti-regression запись;
3. есть ли ранее проверенный tool-path;
4. есть ли сохранённый script / command / locator;
5. не противоречит ли новый способ уже проверенному.

Если рабочий путь найден:
`REUSE_VERIFIED_PATH`.

Новый способ допустим только если ранее проверенный путь:
- недоступен;
- superseded;
- не проходит текущие ограничения;
- либо доказанно не подходит к exact задаче.

Причина отказа от проверенного пути должна быть установлена до новой попытки.

## Tool-failure boundary

Отдельно утверждено правило:

`TOOL_FAILURE != CAPABILITY_FAILURE`

Если один вызов известного инструмента не прошёл, Сущность сначала проверяет штатные варианты того же уже доказанного capability/path:
- chunking;
- append;
- edit;
- повторный readback;
- ранее проверенный формат вызова;
- иной разрешённый режим того же инструмента.

Переход на новый transport/tool допускается только после доказанного blocker старого verified path.

## Authority boundary

Это явное решение ОПЕРАТОРА.

Оно:
- является утверждённым operational governance decision;
- не переписывает автоматически Project Sources/canon;
- не даёт права ARH самовольно редактировать действующие каноны;
- должно быть интегрировано в соответствующий governance/source контур отдельным разрешённым шагом;
- до такой интеграции может использоваться как exact OPERATOR decision evidence там, где проектные источники допускают прямое решение ОПЕРАТОРА.

## Anti-regression example

Правильная последовательность для повторяемой технической операции:

`SEARCH EXPERIENCE → FIND VERIFIED PATH → REUSE → VERIFY RESULT → ONLY THEN CONSIDER NEW METHOD`

Не:

`FIRST IDEA → NEW TRANSPORT → NEW SCRIPT → HUMAN MANUAL WORK → DISCOVER OLD WORKING PATH LATER`

---
КТО: ОПЕРАТОР, сохранено ARH
СТАТУС: OPERATOR_APPROVED_DECISION
