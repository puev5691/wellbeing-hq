# Booster: метаданные отказа r0.1

Bounded non-live successor utility bridge. Сохраняет отдельный диагностический файл перед normalizer; при reasoning-only ответе metadata остаётся, а review/candidate не создаётся.

Exact task: puev5691/wellbeing-hq@5071514b38c4ec3a81a77d63dfe084ce2dc437fe:entities/koordinator/outbox/KOO__booster-failure-diagnostic-metadata-r01__KOD.md; blob 7ec70b078547f83d8f863f0bfa7c16841bfc9bdd.
Predecessor: 9aef9ada9b27f6526a0f5326213748ad689c5a8e:entities/koder/outbox/booster-utility-pilot-live-evidence-bridge-r01. Перед изменениями проверены все 30 исходных Git blobs.

Изменены bridge.py (доступ к transport latency), deps/diagnostic_reviewable_live_worker.py (metadata before normalization), run_tests.py и dependency pins. Добавлены deps/failure_metadata_store.py и test_failure_metadata.py. Код normalizer, worker/ledger, response-shape v2 не изменён. Копии deps/utility_adapter неизменны; их внутренние manifest/TEST — evidence предшественника. Текущее evidence successor — в корневых MANIFEST.json и TEST-RESULTS.json.

Проверка: `python3 run_tests.py`. Synthetic clients, temporary directories; audit guard запрещает сеть, дочерние процессы, реальное окружение и доступ к файлам вне тестовых корней/интерпретатора. Счётчик forbidden attempts проверяется независимо от исключений внутри тестов. TEST-LOG исключает изменчивую длительность запуска.

Проверка пакета: `sha256sum -c SHA256SUMS.txt`. MANIFEST перечисляет payload. Checksums включают MANIFEST и все файлы, кроме самого списка checksums; immutable Git identities публикуются в result.

Нет нового live CLI, host_caller, systemd unit, resolver, admission либо authority. Библиотека сохраняет прежнюю injected transport capability и authority checks; это не разрешение на запуск. Лимит output=64, prompt и reasoning effort не изменены. Реальное consumed разрешение не использовалось. Установка запрещена до независимой SIS проверки и отдельного gate.

Provider calls=0; host/systemd/deployment/credential operations=0. Тестовые status/usage не доказывают причину исторического ответа; token-budget causality остаётся unconfirmed. Утраченные metadata не восстановлены.
