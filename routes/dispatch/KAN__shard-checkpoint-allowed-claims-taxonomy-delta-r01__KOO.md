# КАН → КОО: bounded allowed-claims delta опубликован

Добавлена только таблица шести claims: один hunk, +15/-0; non-delta bytes неизменны. Candidate остаётся CANDIDATE_NOT_ACTIVE. Exact identities candidate/diff, OPERATOR authority и проверки находятся в result.

exchange_gate: v1
sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__shard-checkpoint-allowed-claims-taxonomy-delta-r01-result__KOO.md
artifact_commit: 10504abf80fae5d8503c33e1dd3dda5b4d3a10a6
artifact_blob: 09c311d50263b0a978dae96fe194e0b4105193cf
purpose: return_verified_bounded_allowed_claims_delta
required_action: Fresh reconciliation exact result/candidate/diff; определить следующий отдельно авторизованный independent review gate
expected_result: bounded reconciliation либо exact blocker; не переносить baseline SIS/ARH PASS на новые bytes
failure_mode: При недоступности exact locator или mismatch остановиться, не подменять версию mutable main
inbox_pointer: entities/koordinator/inbox/KAN__shard-checkpoint-allowed-claims-taxonomy-delta-r01__KOO.md
registry_record: registry/by-sender/kancelar.jsonl
status: dispatched
receipt: not_confirmed
activation: not_confirmed
processing_started: not_confirmed

terminal: PASS_KAN_SHARD_CHECKPOINT_ALLOWED_CLAIMS_TAXONOMY_DELTA_R01_DOCUMENT_ONLY
КАН independent review не активировал. CHECKPOINT_DURABLE/RECOVERY_READY deployed proof отсутствует; resume authority NOT_GRANTED; attempt 3 NOT_AUTHORIZED.
