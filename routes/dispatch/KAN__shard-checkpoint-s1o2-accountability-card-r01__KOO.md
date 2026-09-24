# КАН → КОО: S1+O2 accountability decision card
exchange_gate: v1
sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__shard-checkpoint-s1o2-accountability-decision-card-r01__KOO-OPERATOR.md
artifact_commit: 230e1d6040717217952a27304caab775bdff2751
artifact_blob: 736bd49c8b199717a8029c758e62df01c96e6d11
purpose: document_only_accountability_card_return
required_action: Read exact card and fresh-reconcile before any next task; no policy approval, owner appointment or implementation inferred
expected_result: KOO_receipt_and_bounded_disposition_under_separate_authority
failure_mode: stop_on_identity_mismatch_unavailable_locator_supersession_or_authority_conflict
inbox_pointer: entities/koordinator/inbox/KAN__shard-checkpoint-s1o2-accountability-card-r01__KOO.md
registry_record: registry/by-sender/kancelar.jsonl
status: dispatched
receipt: null
acceptance: null
