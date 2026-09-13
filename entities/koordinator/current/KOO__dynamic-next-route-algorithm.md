# KOO — динамический алгоритм выбора следующего маршрута

status: OPERATOR_DIRECTIVE_ACTIVE
scope: KOO dispatch / manual conveyor control
fixed_entity_order: no
project_time: omitted; trusted project-time source not used

## 1. Основание

ОПЕРАТОР установил рабочее правило: порядок Сущностей не должен считаться фиксированным; после каждого профильного результата KOO обязан заново определить и сообщить ОПЕРАТОРУ следующий маршрут.

Это правило дополняет существующий Resume-First и пятифазный polling-контур. Пятифазный порядок остается fallback/wakeup cadence, но не является алгоритмом выбора следующей содержательной работы.

## 2. Главный инвариант

После каждого значимого результата:

`EVENT/RESULT → FRESH PREFLIGHT → RECONCILE ALL PIPELINES → CLASSIFY READY/BLOCKED/WAITING → SELECT ONE NEXT OWNER → DISPATCH/LOCATOR → OPERATOR NEXT ROUTE`

KOO не должен отвечать только состоянием текущей цепочки. Каждый проход обязан проверить, не появился ли более правильный следующий владелец в другой независимой цепочке.

## 3. Модель

Каждый рабочий конвейер представляется как причинная цепочка состояний, а не как фиксированный список Сущностей.

Для каждого pipeline KOO хранит/восстанавливает по exact evidence минимум:

- pipeline / task identity;
- current verified state;
- exact last artifact/commit;
- current owner;
- required next action;
- dependencies;
- blockers;
- operator decision dependency;
- routing state;
- whether useful work is executable now.

Допустимые operational classes:

- `READY` — есть точный профильный следующий шаг и владелец;
- `BLOCKED_EXTERNAL` — нужен внешний ресурс/authority/evidence;
- `WAITING_ENTITY` — ожидается уже адресованный результат другой Сущности;
- `WAITING_OPERATOR` — требуется решение/authorization ОПЕРАТОРА;
- `SERVICE_TAIL` — receipt/registry/preservation без нового профильного действия;
- `CLOSED` — причинная цепь завершена;
- `CONTRADICTION` — evidence конфликтует; автоматический выбор запрещен.

## 4. Выбор следующего маршрута

Из всех `READY` кандидатов выбирается ровно один следующий маршрут.

Приоритеты применяются сверху вниз:

1. safety/recovery/current-writer конфликт или риск потери состояния;
2. прямое новое указание ОПЕРАТОРА;
3. результат, который разблокирует несколько downstream задач;
4. causal continuation, если предыдущий результат создал немедленный профильный следующий шаг;
5. starvation prevention: независимая готовая цепь, которая дольше других не получала рабочего прохода;
6. bounded/cheap verification, которое может быстро снять крупный blocker;
7. обычный round-robin среди остальных READY цепочек.

Равенство нельзя разрешать "по привычке" или по имени Сущности. KOO должен указать, почему выбран именно этот маршрут.

## 5. Не выбирать

Следующий запуск не назначается Сущности, если:

- её задача уже выполнена, но receipt/decision еще не прочитан KOO;
- существует только inbox placement без processing evidence;
- нужная зависимость еще не появилась;
- задача требует OPERATOR approval;
- следующий шаг будет повторять уже проверенный результат;
- профильная работа отсутствует и запуск создаст только пустой polling;
- имеется current-writer/recovery contradiction.

## 6. Выход KOO для ОПЕРАТОРА

После каждого обработанного результата KOO обязан завершать сообщение блоком:

`СЛЕДУЮЩИЙ МАРШРУТ`

с обязательными полями:

- `ENTITY` — кого запускать;
- `PIPELINE` — какая причинная цепочка;
- `EXACT INPUT` — inbox/artifact/commit;
- `WHY NOW` — почему этот маршрут выбран сейчас;
- `EXPECTED RESULT` — что Сущность должна вернуть;
- `DO NOT` — ключевая запрещенная граница, если есть;
- `RETURN TO` — кому возвращается результат, обычно KOO или профильному predecessor;
- `NEXT CANDIDATES` — 1–3 ожидающих независимых цепочки без обещания порядка.

Если следующего executable route нет, KOO обязан назвать точный blocker/OPERATOR decision вместо фиктивного запуска.

## 7. Связь с будущей автоматизацией

Будущий automatic supervisor может реализовать тот же алгоритм:

1. detector получает verified event;
2. state reconciler строит/обновляет pipeline DAG;
3. classifier назначает READY/BLOCKED/WAITING;
4. scheduler выбирает один READY node по priority + starvation;
5. activation layer будит exact Entity;
6. Entity делает Resume-First и один bounded профильный шаг;
7. Exchange Gate фиксирует artifact/dispatch/receipt;
8. result event возвращается в scheduler;
9. цикл повторяется.

Критическая недостающая часть текущего прототипа — доказанный механизм exact Entity-chat initiation/resume. Пока он отсутствует, ОПЕРАТОР выполняет activation layer вручную, а KOO выполняет route selection.

## 8. Текущий пример

Fresh preflight после последнего SIS прохода показал:

Telegram Phase 1B:
- SIS result `BLOCKED_PRE_LIVE_RUNTIME_PRIVACY_READINESS`;
- exact result commit `cff383e86644c6278b98db6a6d3769ab0fab8b5d`;
- blockers B1/B2 требуют отдельного remediation design/provisioning;
- live send остается NOT_READY.

Независимые READY pipelines при этом не должны голодать.

На текущей границе наиболее старый готовый адресный профильный шаг:
KAN literary v0.3 delta-review.

Exact input:
`entities/kancelar/inbox/KOO__snachala-ona-byla-vydumana-v03-delta-review__KAN.md`.

Следом среди READY кандидатов:
- SHT: COOP rights-transition v0.4 criterion-3 re-review;
- KOO: GitHub information-entry r2 technical review;
- Telegram remediation design: отдельный последующий KOD/SIS route после KOO фиксации SIS blockers.

## 9. Anti-regression

- не превращать polling cadence в task priority;
- не путать "Сущность проснулась" с "Сущность должна работать именно сейчас";
- не держать один pipeline монополистом рабочего времени;
- не считать fairness важнее emergency/safety/current-writer boundary;
- после каждого результата пересчитывать маршрут заново;
- предыдущий прогноз следующего маршрута не является обязательством, если fresh evidence изменился.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать решение ОПЕРАТОРА о динамическом выборе следующей Сущности и подготовить алгоритмическую основу будущего автоматического конвейера
СТАТУС: operator_directive_active
