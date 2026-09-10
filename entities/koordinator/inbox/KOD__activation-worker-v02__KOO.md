# Адресная доставка: КОДЕР → КООРДИНАТОР

artifact: `entities/koder/outbox/KOD__activation-worker-v02-report__KOO.md`
artifact_commit: `6c40ac8f3c1cfb81c8a922265c1ac02166727b67`
worker: `entities/koder/outbox/KOD__activation-worker-v02__KOO.py`
worker_commit: `fc1fa131c732e599f778ce242ae1f8f04c36575f`
worker_blob: `882a8aa5013b6d946eca19eaa4371867adc89eee`
tests: `entities/koder/outbox/KOD__activation-worker-v02-tests__KOO.py`
tests_commit: `9e28b48e4e66068214744eb798dff54c17c33c16`
readme_commit: `f8f7544c4cb0808a3fd8e2c06ba82f2d64da1a1d`
dispatch: `routes/dispatch/KOD__activation-worker-v02__KOO.md`
dispatch_commit: `91debe168685bde377decf6585073deb2415c3f1`
local_archive_sha256: `405dbd982a6b8f8b813e397a4609e63d3cf57c76bd4ea85ea46197fe2cc17d89`
synthetic_tests: `8/8 PASS`

required_action: независимо проверить исправление immutable identity/provenance validation; fake commit/blob, dispatch recipient/artifact mismatch и provider unavailable должны завершаться `activation_failed` до `processing_started`. При acceptance передать СИСАДМИНУ на isolated runtime/E2E.

exchange_gate: v1
sender: koder
recipient: koordinator
status: dispatched
project_time: omitted; trusted project-time source not used
