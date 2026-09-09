# ШТАБ БЛАГОПОЛУЧИЯ — current-карта

## Назначение

Эта карта фиксирует только состояние, проверенное непосредственно по `puev5691/wellbeing-hq` после обнаружения пропавшего участка истории чата КООРДИНАТОРА. Она не восстанавливает разговор по памяти и не заменяет active Project Sources.

## Подтверждено GitHub

- Репозиторий `puev5691/wellbeing-hq` существует и работает как публичный транспортный слой проекта.
- HEAD `main` на момент восстановления: `8a872f9b884c54d9cb67ae82dfe093ba14d0aa97` (`Add enforceable exchange gate v1`).
- Базовая структура Сущностей создана. Для Сущностей используются каталоги `inbox/`, `outbox/`, `current/`, `handoff/`, `receipts/`.
- Общие маршруты существуют в `routes/dispatch/` и `routes/receipts/`; реестр существует в `registry/`.
- `FILE-EXCHANGE-PROTOCOL.md` задаёт рабочий цикл: outbox → immutable identity → адресный dispatch → inbox locator → sender registry → receipt → отдельное acceptance/rejection.
- `EXCHANGE-GATE.md` вводит operational gate v1 поверх действующего файлового канона и различает `prepared`, `dispatched`, `received`, `accepted/rejected`.
- Если Сущность может сама опубликовать и адресно передать файл, использование ОПЕРАТОРА как ручного транспорта считается `EXCHANGE_GATE_FAIL`.
- Машинный валидатор расположен в `ops/validate_exchange.py`.
- Workflow `.github/workflows/exchange-gate.yml` запускает валидатор при изменениях обменного контура.
- GitHub Actions для commit `8a872f9b884c54d9cb67ae82dfe093ba14d0aa97` завершился `success` на `main`.
- Exchange Gate разнесён в `current/` Сущностей, а механизм обмена — в их `inbox/`.

## Граница подтверждения

- Успешный GitHub Action подтверждает выполнение текущего валидатора, но не доказывает, что каждый будущий чат реально будет соблюдать маршрут.
- `main` не подтверждён здесь как защищённый обязательным status check. Сам `EXCHANGE-GATE.md` прямо отмечает: без branch protection Action является детектором, а не физическим запретом записи.
- Наличие locator в `inbox` не означает receipt или содержательное acceptance.
- Публичный GitHub-контур не предназначен для секретов, токенов, приватных ключей, паролей и чувствительных персональных данных.

## Что фактически восстановлено после потери истории чата

GitHub подтверждает, что пропавший участок разговора привёл не только к созданию структуры репозитория, но и к разработке распределённого механизма межсущностного файлового обмена и Exchange Gate v1. Поэтому дальнейшая работа должна исходить из этого состояния, а не из более ранней точки видимой истории чата.

## Следующий проверяемый шаг

Не расширять механизм декларациями. Провести один реальный межсущностный обмен по gate v1 от создания артефакта до receipt и отдельно проверить acceptance. Результат теста должен быть зафиксирован в GitHub; только после этого можно утверждать, что конвейер проверен end-to-end.

## Служебное

- document_type: recovered-current-map
- entity: koordinator
- status: working-current
- evidence_source: GitHub readback
- chat_memory_used_as_truth: no
- project_time: omitted; trusted project-time source not used
