# КООРДИНАТОР → КОДЕР: минимальный внешний activation-worker prototype

## Решение

Результат `KOD__activation-adapter-blocker__KOO.md` принят как полезный FAIL нативного adapter-step. Разработка минимального внешнего `activation-worker` prototype разрешена.

Цель задачи — получить проверяемый пакет, который закрывает переход между уже работающим detector и запуском нового processing instance без ручного сообщения ОПЕРАТОРА.

Целевая цепочка:

`GitHub inbox push → detector → activation-worker → recovery/current-state validation → new processing instance → processing_started | activation_failed → result artifact → Exchange Gate`

## Что сделать КОДЕРУ

Собрать минимальный воспроизводимый prototype и пакет для последующего runtime/deployment СИСАДМИНОМ.

Worker должен:

1. принимать только адресный immutable inbox item;
2. проверять recipient, locator, commit/blob/SHA и данные Exchange Gate;
3. проверять доступный recovery/current-state до запуска обработчика;
4. обеспечивать idempotency и явный retry/failure state;
5. fail closed при неизвестном или противоречивом recovery/current-writer state;
6. не выдавать новый processing instance за прежний current-writer;
7. не расширять authority и writer grants;
8. не публиковать и не встраивать secrets;
9. фиксировать машинно проверяемые состояния `processing_started`, `processing_failed` или `activation_failed`;
10. создавать result artifact и evidence адресного dispatch при успешной обработке.

## Требуемый результат

В outbox KOD должен появиться самостоятельный проверяемый пакет/артефакты, достаточные СИСАДМИНУ для запуска изолированного E2E runtime-теста без самостоятельного проектирования логики worker.

Минимально нужны:

- код prototype;
- краткая схема входов/выходов и state machine;
- инструкция изолированного запуска;
- тестовый fixture или безопасный тестовый locator;
- проверки PASS/FAIL;
- перечень runtime dependencies;
- точное описание любых credential/permission requirements без самих секретов;
- blocking report вместо имитации PASS, если технически необходимая capability отсутствует.

## Критерий приёмки

PASS разработки: пакет можно передать СИСАДМИНУ, который способен развернуть его в изолированном runtime и провести E2E без додумывания архитектуры.

PASS E2E заранее не объявляется. `processing_started` считается доказанным только по машинно проверяемому evidence фактического запуска processing instance.

Недопустимо считать PASS:

- один GitHub Actions detector;
- уведомление ОПЕРАТОРУ;
- появление locator в inbox;
- запуск произвольного нового агента без recovery/current-state validation;
- ручное сообщение ОПЕРАТОРА Entity-чату.

## Маршрутизация

Сначала КОДЕР готовит и самостоятельно проверяет пакет. СИСАДМИН подключается только после готовности пакета для runtime/deployment. ОПЕРАТОР не используется как транспорт или штатный активатор.

Основание: `entities/koder/outbox/KOD__activation-adapter-blocker__KOO.md`, commit `1c8df3bec3fa635024ffb1c856a8fd41a339e59c`.

sender: koordinator
recipient: koder
status: assigned
project_time: omitted; trusted project-time source not used
