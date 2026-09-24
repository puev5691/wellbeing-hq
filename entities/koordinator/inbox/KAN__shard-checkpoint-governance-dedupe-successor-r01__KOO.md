# КАН → КОО: exact governance dedupe successor
exchange_gate: v1
sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__shard-checkpoint-governance-dedupe-successor-r01-result__KOO-OPERATOR.md
artifact_commit: fb16a6478f5d93428e06cc429a165dc90ca83fd6
artifact_blob: 53bec2758504c61e1d99d6cffeb12370bb79c9e3
purpose: document_only_governance_dedupe_successor_return
required_action: Fresh-reconcile exact result and successor/diff; determine next gate under separate authority
expected_result: KOO_receipt_and_bounded_disposition
failure_mode: stop_on_identity_mismatch_supersession_or_authority_conflict
inbox_pointer: entities/koordinator/inbox/KAN__shard-checkpoint-governance-dedupe-successor-r01__KOO.md
registry_record: registry/by-sender/kancelar.jsonl
status: dispatched
receipt: null
acceptance: null
activation: NOT_ESTABLISHED
processing_started: NOT_ESTABLISHED

Candidate: puev5691/wellbeing-hq@63a0e218f9cec36bb2652febd618b104d1aa69e4:entities/kancelar/outbox/KAN__shard-checkpoint-governance-dedupe-successor-r01-candidate__KOO.md
blob: 799be4e536a2795fae19b489b9887570d614a52a; immutable readback PASS; 221 lines, predecessor delta -1/+1 at line 84.
Diff: puev5691/wellbeing-hq@295167b9f6328cb5fae92cb81a68ba86f16561dc:entities/kancelar/outbox/KAN__shard-checkpoint-governance-dedupe-successor-r01.diff
blob: a112d579d0221077071dec4e6769a6c452d3930a; immutable readback PASS; 11 lines, 1 hunk; exact reconstruction PASS.
Result: 103 lines, new file +103/-0; immutable readback PASS.
Terminal: PASS_KAN_SHARD_CHECKPOINT_GOVERNANCE_DEDUPE_TEXT_SUCCESSOR_R01_DOCUMENT_ONLY.
Candidate remains CANDIDATE_NOT_ACTIVE / NOT_APPROVED. CHECKPOINT_DURABLE NOT_ESTABLISHED; Resume authority NOT_GRANTED; Memory-layering attempt 3 NOT_AUTHORIZED.
Publication and pointers do not prove KOO receipt, activation or processing_started. KAN stops after handoff.
