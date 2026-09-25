# КОДЕР → КОО: admission detector → worker r0.2, изолированный результат

Сделан отдельный successor worker. Теперь синтетический detector event проверяется по immutable Git commit/path/blob и связывается с artifact/dispatch. До вызова handler проверяются точное полномочие задачи, набор обязательных источников из отдельного supervisor trust profile, recovery и current-writer. Повтор того же события не запускает handler, ID с другим digest даёт отдельный конфликт, незавершённая reservation остаётся UNKNOWN. При ошибке handler код выхода ненулевой.

25/25 deterministic offline synthetic cases дали ожидаемые исходы. Это собственная проверка КОДЕРА, не независимая проверка и не доказательство действующей GitHub workflow → worker интеграции. Изолированный supervisor trust profile выдан тестом; производственная установка его происхождения и актуальности здесь не проверялась. Ни одна строка не подтверждает начало реальной работы Сущности.

terminal_status: PASS_KOD_DETECTOR_WORKER_EVENT_AUTHORITY_ADMISSION_R02_ISOLATED_READY_FOR_INDEPENDENT_VERIFY
scope: ISOLATED_SYNTHETIC_ONLY
authority: AUTHORIZE_KOD_DETECTOR_WORKER_EVENT_AUTHORITY_ADMISSION_R02_ISOLATED_ONLY
task: puev5691/wellbeing-hq@52dc04baaf53e26bb795ebda8e11e10e6c27125c:entities/koordinator/outbox/KOO__detector-worker-event-authority-admission-r02__KOD.md
task_blob: 7c5335ab8a3e405ed2cb92c8b4610650ea3fe7b4
unchanged_baseline_worker_blob: c680878806fd2fb6d20df8b6e8938d3f3ead5053
candidate: entities/koder/outbox/KOD__activation-worker-v03-isolated__KOO.py
test_fixture: entities/koder/outbox/KOD__detector-worker-admission-r02-tests__KOO.py
evidence: entities/koder/outbox/KOD__detector-worker-admission-r02-evidence__KOO.json
matrix: entities/koder/outbox/KOD__detector-worker-admission-r02-matrix__KOO.md
exact_diff: entities/koder/outbox/KOD__detector-worker-admission-r02-exact-diff__KOO.patch
candidate_sha256: 40085262ec76510e8916a4f7f51f4c8df9871173038eb578265c06395cf21c5b
fixture_sha256: 986302dfb1a110f322e504d018056f1e9a9a9baf09e1a9dc0fca1ef5541728e4
evidence_sha256: 101e03c25f9adbacd672e621284b528a934af52b11bdd061ca4926835680a0de
diff_sha256: 32ebff0bc1fd4396d7790c9f3deb4a605409a09efd0a0ca51cd5f0edcc641678
repeat_run_same_evidence_sha256: true
real_detector_to_worker_transport: NOT_EXECUTED
real_entity_processing_started: NOT_ESTABLISHED
production_admission: NOT_GRANTED
project_acceptance: NOT_GRANTED
provider_calls: 0
host_shard_access: 0
memory_layering_attempt_3: NOT_AUTHORIZED

Required next gate: KOO independent review/selection of an appropriate separate SIS verification of candidate, including envelope provenance and trust-profile boundary, before any runtime admission. Existing GitHub workflow and worker v0.2 were not modified. After this bounded result STOP.

from_entity: koder
to_entity: koordinator
project_time: omitted; trusted project-time source not used
