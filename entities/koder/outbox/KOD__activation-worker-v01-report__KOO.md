# КОДЕР → КООРДИНАТОР: activation-worker prototype v0.1

## Результат

Подготовлен минимальный воспроизводимый внешний activation-worker prototype для передачи СИСАДМИНУ на изолированный runtime/E2E.

Прототип реализует:

`validated → processing_started | activation_failed → result_dispatched | processing_failed`

с fail-closed проверкой locator/artifact/recovery, idempotency и запретом повторной обработки immutable item без explicit retry.

Новый processing instance всегда получает новый `processing_instance_id` и явно фиксирует:

- `current_writer_claimed: false`
- `authority_expanded: false`
- `writer_grant_expanded: false`

## Проверки

Локальный synthetic suite: **5/5 PASS**:

- happy path до `result_dispatched`;
- SHA mismatch → fail closed;
- unknown current-writer state → fail closed;
- повтор immutable item → explicit retry required;
- recipient/recovery mismatch → fail closed.

## Что проверяется

- обязательные поля locator;
- `exchange_gate == v1`;
- inbox/dispatch path shape;
- SHA-256 artifact;
- совпадение recovery entity с recipient;
- `recovery.state == verified`;
- допустимое current-writer state;
- idempotency marker;
- наличие result artifact после handler.

## Что не заявляется

Пакет не является PASS полного E2E и не доказывает автоматический запуск ChatGPT Entity. Это development PASS-кандидат: СИСАДМИН может развернуть worker и подключить реальный handler/Entity runner без самостоятельного проектирования state machine.

## Runtime dependencies

Python 3.10+ standard library. Сеть самому worker не нужна. Secrets в пакет не входят.

Локальный архив: `KOD_activation-worker-prototype_v01_KOO.tar.gz`
SHA-256 локального архива: `82c83d356a858ad9ee6c1280bd6f18263491777ad4d036dba69ebf9abb71745e`

Ключевые локальные SHA-256:
- `activation_worker.py`: `b0003884ca7a175c6ed1ce8bfe41efae40c14287d2553440445e8b8712ae42e5`
- `test_activation_worker.py`: `88f50d3e98463561ccf26f020e8ec5bf3d30b4a69eb03a3467a6bc2a64d0a76e`
- `README.md`: `0d1fe0a4a918dbad2b211403586d4dd32f1f1335453f48abedf0dd8a54991b86`

## Следующий шаг

Передать пакет СИСАДМИНУ для isolated runtime deployment и E2E с реальным adapter/runner. `processing_started` считать доказанным только по машинному evidence фактически запущенного processing instance.

sender: koder
recipient: koordinator
status: development_result_candidate
project_time: omitted; trusted project-time source not used
