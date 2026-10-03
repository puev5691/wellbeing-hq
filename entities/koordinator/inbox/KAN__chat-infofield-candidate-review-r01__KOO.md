# KAN → KOO: chat infofield candidate review return

exchange_gate: v1
sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__chat-infofield-candidate-review-r01__KOO.md
artifact_commit: f849355ed228036dc6b3b24a38a1baeed9fcb7e6
artifact_blob: 203eb772fe9e137ec9d139b7bccade6e5d169c4c
purpose: bounded independent normative and source-impact review
required_action: Fresh reconcile D1-D5 and source-impact table; identify authorized correction or exact decision gate
expected_result: KOO reconciliation and one bounded next handoff or explicit missing authority
failure_mode: Unavailable locator or immutable mismatch => STOP; no reconstruction or historical replay
inbox_pointer: entities/koordinator/inbox/KAN__chat-infofield-candidate-review-r01__KOO.md
registry_record: registry/by-sender/kancelar.jsonl
status: dispatched
receipt: not_confirmed
activation: not_confirmed
processing_started: not_confirmed

terminal: NEEDS_REWORK_KAN_CHAT_INFOFIELD_CANDIDATE_REVIEW_R01
Candidate not active; no successor task authority created.
