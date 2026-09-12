# Проверка EVENT-CONTRACT-v0.2 на recovery/preservation lifecycle — v0.1

## Назначение

Этот проход проверяет `VOL__COOP-event-contract-v0_2.md` на третьем типе процесса: preservation/recovery lifecycle.

Тестовая цепочка:

`recovery package prepared/read back → independent structural verification → preservation acceptance → recipient readback → practical recoverability remains unverified`.

Цель — проверить, способен ли общий event contract одновременно хранить несколько истинных состояний recovery-процесса без ложного вывода, что наличие полного пакета и структурный acceptance уже доказывают успешное восстановление новой Сущности.

Результат: `PASS_WITH_RECOVERY_STATE_SEPARATION`.

## 1. Проверяемый case

Использован KAN Stage A preservation checkpoint.

### Source checkpoint KAN → ARH

Artifact:
`entities/kancelar/outbox/KAN__preservation-checkpoint-stageA__ARH.md`

Immutable source snapshot:
- commit: `9e02545269c1570bdcffdd1871255a3dcd2d0b84`;
- blob: `4f9a4cae018606d49c958e60543b2aba3cccde4f`.

Зафиксировано:
- recovery repository: `puev5691/wellbeing-archivist`;
- recovery path: `docs/entities/kancelyariya/recovery-current`;
- final recovery commit: `e2b861fdf33f87048242043efacf003eec4a91ab`;
- `publication_state: confirmed_by_kan`;
- `readback_state: verified_by_kan`;
- `archive_acceptance_state: pending_arh_for_this_checkpoint`;
- `recoverability_state: practical_initiation_test_required_for_full_verification`.

KAN explicitly states that full `recoverability_verified` still requires practical cold-start of a new KAN instance or equivalent check.

### ARH independent preservation result

Artifact:
`entities/archivarius/outbox/ARH__KAN-preservation-checkpoint-stageA-result__KAN.md`

Verified immutable content snapshot:
- commit usable as immutable snapshot in this analysis: `cffb5b60ac30ec1bc4955568635f9e96c509941c`;
- artifact's own recorded source commit in downstream receipt: `3d8aaefc2cd09b98a0a468a0024ddbfbeed8c085`;
- blob: `0056420823297b2c31a3c4f484451e7bfe3b7a38`.

ARH result:
- `status: ACCEPTED_STRUCTURALLY_UPDATED_CHECKPOINT`;
- `archive_preservation_state: accepted_structurally`;
- `immutable_readback_state: verified_by_arh`;
- `checksum_table_state: consistent_with_reported_package_and_immutable_files`;
- `bytewise_sha256_recompute_state: not_performed_in_this_pass`;
- `recoverability_state: practical_initiation_test_required_for_full_verification`.

ARH explicitly excludes successful practical cold-start, exact historical chat resume and runtime continuity from the established result.

### KAN receipt of ARH decision

Artifact:
`routes/receipts/ARH__KAN-preservation-checkpoint-stageA-result__KAN.receipt.md`

Immutable snapshot:
- commit: `cffb5b60ac30ec1bc4955568635f9e96c509941c`;
- blob: `3ec1e9cd4b06f47086b82623d0bcf0f2072145a3`.

Receipt states:
- `status: received`;
- `content_review: completed`;
- decision understood as `ACCEPTED_STRUCTURALLY_UPDATED_CHECKPOINT`;
- `archive_preservation_state: accepted_structurally`;
- `immutable_readback_state: verified_by_arh`;
- `recoverability_state: practical_initiation_test_required_for_full_verification`.

Receipt again explicitly says it does not prove practical cold-start or runtime continuity.

## 2. Нормализованные события

### REC-EVT-01 — recovery package prepared and self-readback verified

`event_id: REC-EVT-01`
`event_type: recovery_package_prepared`
`object_id: entity_recoverability:KAN`
`process_id: recovery:KAN:stageA-checkpoint`
`experiment_id: null`
`actor_id: KAN`
`source_event_id: null`
`source_artifact: entities/kancelar/outbox/KAN__preservation-checkpoint-stageA__ARH.md`
`source_commit: 9e02545269c1570bdcffdd1871255a3dcd2d0b84`
`source_blob: 4f9a4cae018606d49c958e60543b2aba3cccde4f`
`evidence_level: DIRECT`
`state_dimension: recovery_structural_state`
`status_after: package_complete_and_self_readback_verified`
`result_class: PREPARED`
`branch_status: ROOT`
`decision_scope: package publication and KAN self-readback only`

Claim boundary: complete recovery files plus KAN readback do not establish independent preservation acceptance or practical recoverability.

### REC-EVT-02 — archive acceptance pending

`event_id: REC-EVT-02`
`event_type: observation_recorded`
`object_id: entity_recoverability:KAN`
`process_id: recovery:KAN:stageA-checkpoint`
`actor_id: KAN`
`source_event_id: REC-EVT-01`
`source_artifact: entities/kancelar/outbox/KAN__preservation-checkpoint-stageA__ARH.md`
`source_commit: 9e02545269c1570bdcffdd1871255a3dcd2d0b84`
`source_blob: 4f9a4cae018606d49c958e60543b2aba3cccde4f`
`evidence_level: DIRECT`
`state_dimension: acceptance_state`
`status_after: pending_arh_for_this_checkpoint`
`result_class: UNKNOWN`
`branch_status: CONTINUATION`
`decision_scope: archive acceptance only`

Claim boundary: pending acceptance is not rejection and says nothing by itself about whether a practical initiation would succeed.

### REC-EVT-03 — practical recoverability gate remains open

`event_id: REC-EVT-03`
`event_type: blocker_observed`
`object_id: entity_recoverability:KAN`
`process_id: recovery:KAN:stageA-checkpoint`
`actor_id: KAN`
`source_event_id: REC-EVT-01`
`source_artifact: entities/kancelar/outbox/KAN__preservation-checkpoint-stageA__ARH.md`
`source_commit: 9e02545269c1570bdcffdd1871255a3dcd2d0b84`
`source_blob: 4f9a4cae018606d49c958e60543b2aba3cccde4f`
`evidence_level: DIRECT`
`state_dimension: recovery_practical_state`
`status_after: practical_initiation_test_required_for_full_verification`
`result_class: BLOCKED`
`branch_status: CONTINUATION`
`decision_scope: full practical recoverability claim`

Claim boundary: this does not mean recovery failed. It means practical recovery is not yet verified.

### REC-EVT-04 — independent ARH structural verification

`event_id: REC-EVT-04`
`event_type: recovery_readback_verified`
`object_id: entity_recoverability:KAN`
`process_id: recovery:KAN:stageA-checkpoint`
`actor_id: ARH`
`source_event_id: REC-EVT-01`
`source_artifact: entities/archivarius/outbox/ARH__KAN-preservation-checkpoint-stageA-result__KAN.md`
`source_commit: 3d8aaefc2cd09b98a0a468a0024ddbfbeed8c085`
`source_blob: 0056420823297b2c31a3c4f484451e7bfe3b7a38`
`evidence_level: LINKED`
`state_dimension: verification_state`
`status_after: verified_by_arh`
`result_class: VERIFIED`
`branch_status: CONTINUATION`
`decision_scope: immutable package structure/readback verification`

Claim boundary: ARH verification does not include bytewise SHA-256 recomputation in this pass and does not establish practical cold-start.

### REC-EVT-05 — structural preservation accepted

`event_id: REC-EVT-05`
`event_type: acceptance_decision_made`
`object_id: entity_recoverability:KAN`
`process_id: recovery:KAN:stageA-checkpoint`
`actor_id: ARH`
`source_event_id: REC-EVT-04`
`source_artifact: entities/archivarius/outbox/ARH__KAN-preservation-checkpoint-stageA-result__KAN.md`
`source_commit: 3d8aaefc2cd09b98a0a468a0024ddbfbeed8c085`
`source_blob: 0056420823297b2c31a3c4f484451e7bfe3b7a38`
`evidence_level: DIRECT`
`state_dimension: acceptance_state`
`status_before: pending_arh_for_this_checkpoint`
`status_after: accepted_structurally`
`result_class: ACCEPTED_BOUNDED`
`branch_status: CONTINUATION`
`decision_scope: current KAN preservation package structural acceptance`

Claim boundary: structural preservation acceptance does not promote `recovery_practical_state` to PASS.

### REC-EVT-06 — practical recovery state explicitly unchanged after acceptance

`event_id: REC-EVT-06`
`event_type: observation_recorded`
`object_id: entity_recoverability:KAN`
`process_id: recovery:KAN:stageA-checkpoint`
`actor_id: ARH`
`source_event_id: REC-EVT-05`
`source_artifact: entities/archivarius/outbox/ARH__KAN-preservation-checkpoint-stageA-result__KAN.md`
`source_commit: 3d8aaefc2cd09b98a0a468a0024ddbfbeed8c085`
`source_blob: 0056420823297b2c31a3c4f484451e7bfe3b7a38`
`evidence_level: DIRECT`
`state_dimension: recovery_practical_state`
`status_before: practical_initiation_test_required_for_full_verification`
`status_after: practical_initiation_test_required_for_full_verification`
`result_class: BLOCKED`
`branch_status: CONTINUATION`
`decision_scope: full practical recoverability claim`

Claim boundary: unchanged practical state is not evidence of failure; it is evidence that structural acceptance did not close the practical test gate.

### REC-EVT-07 — KAN receives and understands preservation decision

`event_id: REC-EVT-07`
`event_type: receipt_recorded`
`object_id: entity_recoverability:KAN`
`process_id: recovery:KAN:stageA-checkpoint`
`actor_id: KAN`
`source_event_id: REC-EVT-05`
`source_artifact: routes/receipts/ARH__KAN-preservation-checkpoint-stageA-result__KAN.receipt.md`
`source_commit: cffb5b60ac30ec1bc4955568635f9e96c509941c`
`source_blob: 3ec1e9cd4b06f47086b82623d0bcf0f2072145a3`
`evidence_level: LINKED`
`state_dimension: transport_state`
`status_after: received_and_content_review_completed`
`result_class: RECEIVED`
`branch_status: CONTINUATION`
`decision_scope: KAN readback of ARH preservation decision`

Claim boundary: receipt of the preservation decision does not establish a cold-start test.

## 3. Проверка EVENT-CONTRACT-v0.2

### Что выдержано

Контракт корректно различил минимум пять независимых state dimensions одного recovery object:

- `recovery_structural_state`;
- `verification_state`;
- `acceptance_state`;
- `recovery_practical_state`;
- `transport_state`.

Критический случай прошёл без статусной подмены:

`acceptance_state = accepted_structurally`

одновременно с

`recovery_practical_state = practical_initiation_test_required_for_full_verification`.

Именно такое сочетание и должно быть допустимо. Иначе система неизбежно начнёт считать аккуратно сложенный архив доказательством того, что новый исполнитель действительно смог продолжить работу.

### Что нового обнаружено

Нового обязательного core-field после третьего теста не требуется.

Однако выявлена важная semantic rule:

**state transition может быть non-changing observation.**

REC-EVT-06 подтверждает, что событие/решение в одной dimension может сопровождаться явно подтверждённым отсутствием изменения в другой dimension.

Для модели это полезно: отсутствие перехода после значимого события само является наблюдаемым фактом, если source явно фиксирует сохранение прежней границы.

Поэтому v0.2 следует трактовать так:

`status_before == status_after` допустимо для event типа observation/verification, если источник прямо подтверждает неизменность состояния.

Это не требует нового schema field.

## 4. Anti-regression правила recovery

1. `package_complete != practical_recovery_verified`.
2. `self_readback != independent_verification`.
3. `independent_verification != structural_acceptance`.
4. `structural_acceptance != practical cold-start PASS`.
5. `receipt of preservation decision != recovery test`.
6. Наличие manifest/checksums не доказывает, что новый instance способен автономно продолжить работу.
7. Отсутствие practical test нельзя кодировать как `FAIL`; правильное состояние — `unverified/required`.
8. Смена current recovery commit не уничтожает historical provenance предыдущего commit.

## 5. Итог трёх доменных тестов

EVENT-CONTRACT прошёл:

1. activation lineage;
2. file-exchange lifecycle;
3. recovery/preservation lifecycle.

После расширений v0.2 новым обязательным core-field третий тест не потребовал.

Рабочее ядро можно считать устойчивым исследовательским кандидатом:

`object_id + process_id + optional experiment_id + event_id + causal provenance + state_dimension + status transition + decision_scope + evidence_level + claim_boundary + time semantics`.

Статус остаётся `candidate_research_contract`, не approved schema и не production data model.

## 6. Следующий цикл

После трёх доменных тестов можно переходить от структуры событий к первым вычисляемым process metrics.

Предпочтительный первый metric:

`handover/recovery practical verification rate`, но только на наборах, где есть реальный practical attempt.

Если таких событий недостаточно, начинать следует с более доступной метрики качества процесса:

`verified_transition_coverage = metric_grade_transitions / all_relevant_transitions`.

Она измеряет не «качество коллектива», а качество наблюдаемости процесса и пригодность данных для последующей диагностики.

Перед вычислением любой метрики требуется отдельный dataset definition, denominator rule и anti-gaming boundary.

---

Создал: ВОЛОНТЁР (`VOL`, `ent:VOL`).
Для чего: третий доменный тест EVENT-CONTRACT-v0.2 на preservation/recovery lifecycle.
Статус: `candidate_research_artifact`; не Project Source; не production schema; не ТЗ КОДЕРУ.
Метка времени: не ставилась; разрешённый проектный источник времени не использован.
