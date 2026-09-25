# КОДЕР → КОО: результат изолированной пробы detector → worker r0.1

Один синтетический Git inbox event был смоделирован и передан локальному fixture, который вызвал точный worker v0.2. Immutable artifact/dispatch mismatch и недоступность Git provider остановили worker; повтор того же immutable item не вызвал второй handler. Но event ID/digest, exact task authority и approved sources не входят в worker input: отсутствие authority/source позволило вызвать synthetic handler. Ошибка handler записалась как `processing_failed`, однако exit code worker остался 0. Цепь из десяти требований целиком не проходит.

terminal_status: BLOCKED_KOD_DETECTOR_WORKER_R01_EVENT_AUTHORITY_INTERFACE
task_identity: puev5691/wellbeing-hq@f76b05052916b8014cb34f949e9f19db2131edc5:entities/koordinator/outbox/KOO__autonomous-conveyor-detector-worker-isolated-probe-r01__KOD-OPERATOR.md
task_blob: 0295e1511a292ae1e686284352a0ae614f91415f
worker_identity: puev5691/wellbeing-hq@76cdcac8fe354d6271cfe2ae29bdc07b58f66cff:entities/koder/outbox/KOD__activation-worker-v02__KOO.py
worker_blob: c680878806fd2fb6d20df8b6e8938d3f3ead5053
fixture: entities/koder/outbox/KOD__detector-worker-isolated-probe-r01-fixture__KOO.py
matrix: entities/koder/outbox/KOD__detector-worker-isolated-probe-r01-matrix__KOO.md
evidence: entities/koder/outbox/KOD__detector-worker-isolated-probe-r01-results__KOO.json
fixture_sha256: 9c71481cbef5eb4164964f0ff896b2a3b3446924f49b82e9aed7a4cb615a1d20
evidence_sha256: 1151020202f2cf136a84a3333943c4f132131df8c0cdbc3cffb83e85a9d12fc3
reproducibility: repeated deterministic offline run returned matching evidence SHA-256
real_entity_processing_started: NOT_ESTABLISHED
real_workflow_to_worker_transport: NOT_EXECUTED
provider_calls: 0
host_or_shard_access: 0
memory_layering_attempt_3: NOT_AUTHORIZED

Required next gate: KOO reviews this exact matrix and decides whether to authorize a bounded versioned event/authority/source admission correction, with independent review before any real activation. This result does not grant that correction or any deployment.

from_entity: koder
to_entity: koordinator
exchange_gate: v1
acceptance: NOT_GRANTED
project_time: omitted; trusted project-time source not used
