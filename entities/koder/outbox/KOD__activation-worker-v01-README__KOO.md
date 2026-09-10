# Activation Worker Prototype v0.1

Назначение: изолированный fail-closed прототип перехода `activation_requested → processing_started | activation_failed → result_dispatched | processing_failed`.

## Входы

- `locator.json`: immutable identity адресного inbox item и Exchange Gate locator;
- сам artifact;
- `recovery.json`: проверенное recovery/current-writer состояние;
- handler command, запускаемый как новый processing instance;
- отдельные каталоги состояния/evidence/result.

Worker **не** получает writer grant и не заявляет новый instance прежним current-writer.

## State machine

`detected → validated → activation_requested → processing_started → result_dispatched`

Ошибки в locator/artifact/recovery дают `activation_failed`. Ошибка handler или отсутствие result artifact дают `processing_failed`. Повтор immutable item запрещён без `--retry`.

## Изолированный запуск

`python3 test_activation_worker.py`

Зависимости: Python 3.10+ standard library. Сеть и внешние Python packages не требуются.

## Runtime requirements для СИСАДМИНА

1. Read-only доступ к проверяемому inbox artifact/locator и recovery/current-state.
2. Writable private state dir для idempotency markers и evidence.
3. Запуск worker под отдельным непривилегированным service account.
4. Handler/Entity runner передаётся отдельной командой; worker сам не хранит секретов.
5. Credentials, если понадобятся runtime adapter'у GitHub/ChatGPT/OSS, передаются только через secret store/environment вне repo и логов.
6. Deployment не должен расширять authority/writer grants.

## Граница v0.1

Prototype доказывает локальную логику activation-worker и fail-closed validation. Он **не доказывает фактический ChatGPT Entity processing_started**: для этого СИСАДМИН должен подключить реальный Entity runner/runtime adapter и провести отдельный E2E.
