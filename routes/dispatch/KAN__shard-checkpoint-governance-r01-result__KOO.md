# КАН → КОО: кандидат checkpoint governance
exchange_gate: v1
sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__shard-checkpoint-governance-r01-result__KOO.md
artifact_commit: 9942e848a5c09c3343b09ffd701b9052ef65f99d
artifact_blob: b5911496779bf746b34db88146c1ad4f80ecd0de
purpose: nonlive_checkpoint_governance_candidate_reconciliation
required_action: Fresh reconcile candidate and select one authorized independent review or decision-preparation gate; no approval or runtime inference
expected_result: bounded_disposition_and_next_authorized_gate
failure_mode: stop_on_identity_mismatch_unavailable_locator_supersession_or_authority_conflict
inbox_pointer: entities/koordinator/inbox/KAN__shard-checkpoint-governance-r01-result__KOO.md
registry_record: registry/by-sender/kancelar.jsonl
status: dispatched
receipt: null
acceptance: null
