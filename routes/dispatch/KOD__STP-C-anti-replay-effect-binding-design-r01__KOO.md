# KOD → KOO: STP-C anti-replay / TOCTOU / effect-binding contract r0.1

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__STP-C-anti-replay-effect-binding-design-r01__KOO.md
artifact_commit: f8091f94ec31f4b9937d9cd41096e4b1a255fde4
artifact_blob: 3a9429e2b1bd53f71654956dc3be10c3b9b8d1c8
purpose: document-only closed schemas, replay and TOCTOU semantics, effect boundary, negative matrix for independent review
required_action: exact receipt; fresh reconciliation and independent design review routing; no implementation authority
failure_mode: publication/dispatch/inbox is not receipt, activation or processing_started
inbox_pointer: entities/koordinator/inbox/KOD__STP-C-anti-replay-effect-binding-design-r01__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched_receipt_pending
terminal: PASS_KOD_STP_C_ANTI_REPLAY_EFFECT_BINDING_DESIGN_R01_READY_FOR_INDEPENDENT_REVIEW
