# KOO → OPERATOR: один нормативный выбор для разблокировки COOP

status: OPERATOR_DECISION_REQUIRED

## Конфликт

SHT остановил P1-задачу COOP research conveyor, потому что действующие approved-источники расходятся в определении терминальной адресной доставки.

### Модель A

`project-instructions-core-v2.1` + `file-work-canon-universal-v2.3`:

разрешают два способа адресной доставки:
1. фактическая передача файла;
2. проверяемая locator-based delivery существующего immutable artifact с адресатом, dispatch, доступным locator, version identity, receipt и failure-mode.

### Модель B

`source-loading-policy-v2`, раздел 5:

описывает завершение маршрута как:
- фактическую загрузку файла в адресный чат; либо
- фиксацию невозможности доставки и следующего шага.

Locator-based delivery там не отражена.

## Требуется один выбор

### Вариант 1 — рекомендуемый

Подтвердить, что в части способов завершения адресной доставки раздел 5 `source-loading-policy-v2` superseded более новой моделью:

`project-instructions-core-v2.1 + file-work-canon-universal-v2.3`.

После этого:
- SHT продолжает ту же P1-задачу;
- KAN получает задачу гармонизировать `source-loading-policy`;
- locator-based delivery остаётся действующей общей нормой.

### Вариант 2

Сохранить физическую загрузку файла в адресный чат как обязательную для данного класса маршрутов.

Тогда:
- COOP conveyor проектируется с этим исключением;
- locator-based delivery не считается terminal delivery для этого класса;
- исключение придётся отдельно учитывать в OSS/process model.

## Рекомендация KOO

`ВАРИАНТ 1`.

Причина:
core v2.1 и file canon v2.3 согласованы между собой, новее и уже фактически используются проектом с immutable locator + dispatch + receipt + readback.

Но KOO не объявляет старый approved source superseded без явного решения ОПЕРАТОРА.

## Минимальный допустимый ответ

`Вариант 1`

или

`Вариант 2`.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: получить минимальное явное нормативное решение и разблокировать COOP research conveyor
СТАТУС: operator_decision_required
