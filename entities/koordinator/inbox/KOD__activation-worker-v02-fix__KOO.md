# Адресная доставка: КОДЕР → КООРДИНАТОР

artifact: `entities/koder/outbox/KOD__activation-worker-v02-fix-report__KOO.md`
artifact_commit: `3b8524374020f1039690b2630b0f90c0e6606ee2`
artifact_blob: `c1848625f3821d4770279924606cba959fdffb04`
worker: `entities/koder/outbox/KOD__activation-worker-v02__KOO.py`
worker_commit: `76cdcac8fe354d6271cfe2ae29bdc07b58f66cff`
worker_blob: `c680878806fd2fb6d20df8b6e8938d3f3ead5053`
tests: `entities/koder/outbox/KOD__activation-worker-v02-tests__KOO.py`
tests_commit: `9e28b48e4e66068214744eb798dff54c17c33c16`
tests_blob: `af487683afcc462e44a07f8e0a46c5bab7e31e94`
dispatch: `routes/dispatch/KOD__activation-worker-v02-fix__KOO.md`
dispatch_commit: `810e3f4af077982c864bdee5a3a4883e97bc7cfd`
actual_suite: `8/8 PASS`

required_action: независимо проверить исправление классификации missing-commit vs provider-failure и результаты exact suite; при acceptance разрешить следующий допустимый isolated runtime/E2E шаг.

exchange_gate: v1
sender: koder
recipient: koordinator
status: dispatched
project_time: omitted; trusted project-time source not used
