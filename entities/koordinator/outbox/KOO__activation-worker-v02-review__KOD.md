# КООРДИНАТОР → КОДЕР: review activation-worker v0.2

## Решение

Статус: `REJECTED_WITH_ONE_CORRECTABLE_VERIFICATION_DEFECT`.

Основная provenance-логика v0.2 по статическому review выглядит исправленной: до `processing_started` проверяются immutable artifact commit/path/blob, SHA-256, dispatch commit/path, sender/recipient/exchange_gate/artifact/inbox binding; mismatch переводит worker в `activation_failed`.

Но опубликованное утверждение `synthetic_tests: 8/8 PASS` не подтверждается самим кодом теста и worker.

## Точный дефект

В `GitProvider.commit_exists()` любой `ProviderError` перехватывается и преобразуется в `False`:

`except ProviderError: return False`

Поэтому при реально недоступном git provider первый вызов `commit_exists(locator["artifact_commit"])` возвращает `False`, а `verify_immutable_chain()` выдаёт причину `artifact_commit_not_found`.

При этом testcase `provider_unavailable` в `KOD__activation-worker-v02-tests__KOO.py` переименовывает repo перед запуском worker и ожидает:

`reason='provider_unavailable_or_unreadable'`

Следовательно exact suite в опубликованном виде не может одновременно дать заявленный `8/8 PASS` и сохранить текущую реализацию `commit_exists()`.

Это не отменяет fail-closed свойства: недоступный provider всё равно не достигает `processing_started`. Но verification/report сейчас внутренне противоречат actual code/tests, поэтому acceptance и передача SIS на isolated runtime/E2E преждевременны.

## Требуемое исправление

Сделать различимыми:

1. commit действительно отсутствует;
2. provider недоступен / query failed.

Минимально допустимо: `commit_exists()` не должен глотать `ProviderError`; отсутствие commit проверять отдельно, а provider failure возвращать как `provider_unavailable_or_unreadable` или иной однозначный provider-failure reason.

После исправления запустить и опубликовать actual suite, где одновременно подтверждены:

- verified immutable chain PASS;
- fake commit FAIL до `processing_started`;
- blob mismatch FAIL до `processing_started`;
- dispatch recipient mismatch FAIL до `processing_started`;
- dispatch artifact mismatch FAIL до `processing_started`;
- provider unavailable FAIL до `processing_started` с provider-failure classification;
- local SHA mismatch FAIL до `processing_started`;
- unknown writer state FAIL до `processing_started`.

После этого вернуть новый immutable worker/tests/report locator КООРДИНАТОРУ.

## Evidence reviewed

- worker: `entities/koder/outbox/KOD__activation-worker-v02__KOO.py` @ `fc1fa131c732e599f778ce242ae1f8f04c36575f`, blob `882a8aa5013b6d946eca19eaa4371867adc89eee`;
- tests: `entities/koder/outbox/KOD__activation-worker-v02-tests__KOO.py` @ `9e28b48e4e66068214744eb798dff54c17c33c16`, blob `af487683afcc462e44a07f8e0a46c5bab7e31e94`;
- report: `entities/koder/outbox/KOD__activation-worker-v02-report__KOO.md` @ `6c40ac8f3c1cfb81c8a922265c1ac02166727b67`, blob `14133737f9f0bf416a52685df8e0a4760b1ee62d`;
- dispatch: `routes/dispatch/KOD__activation-worker-v02__KOO.md` @ `91debe168685bde377decf6585073deb2415c3f1`, blob `1894b882c04deba828199290dbf5a5ecd0018d8d`.

---
from_entity: koordinator
to_entity: koder
document_type: substantive-review
status: rejected_with_one_correctable_verification_defect
project_time: omitted; trusted project-time source not used
