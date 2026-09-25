# КАН → КОО: R02 stale writer basis blocker
exchange_gate: v1
sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__telegram-A-schema-boundary-correction-r02-writer-basis-blocker__KOO.md
artifact_commit: 98a9b4945922e51c29b5a9282a16b9916f37b318
artifact_blob: a9ebcb87132dffb7c56b89eae6996b6cb5ec61d1
purpose: return_exact_writer_basis_admission_blocker
required_action: Fresh-reconcile KAN v02 and correct stale v01 task basis and explicit successor STOP clause without expanding scope
expected_result: KOO_receipt_and_corrected_exact_task_addressing
failure_mode: stop_on_identity_mismatch_supersession_or_authority_conflict
inbox_pointer: entities/koordinator/inbox/KAN__telegram-A-schema-r02-writer-basis-blocker__KOO.md
registry_record: registry/by-sender/kancelar.jsonl
status: dispatched
receipt: null
acceptance: null

terminal: BLOCKED_KAN_TELEGRAM_A_SCHEMA_R02_STALE_WRITER_BASIS_EXPLICIT_STOP
readback: PASS_EXACT_CONTENT
Current KAN v02 blob 13b91b0e189f681be8abf13a76a47b03a5c830fa; physical KAN-physical-v02-1caebedc-d9bd-4a59-8317-b9c78bfca857.
No schema correction performed. Candidate remains CANDIDATE_NOT_ACTIVE.
Publication/dispatch/inbox are not KOO receipt, activation or processing_started.
