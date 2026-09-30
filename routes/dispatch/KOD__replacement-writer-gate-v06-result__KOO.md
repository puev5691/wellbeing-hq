# Exchange Gate dispatch: KOD -> KOO

artifact: `entities/koder/outbox/KOD__replacement-writer-gate-v06-result__KOO.md`
artifact_commit: `242c285cb1aba0af635a808a0ab33b707dddc3ef`
artifact_blob: `895ed9ebd779d9b8d0dfe85a8245c1d81b23f6c0`

inbox: `entities/koordinator/inbox/KOD__replacement-writer-gate-v06-result__KOO.md`
inbox_commit: `0a01276176ae983e6105bb5f27cd1ce9ccb4788e`
inbox_blob: `1c2612c6c3a68799b4f4513769ac5c58f8d60702`

terminal: `PASS_KOD_REPLACEMENT_V06_WRITER_GATE_CURRENT_WRITER_ESTABLISHED`
status: `dispatched_pending_receipt`
receipt_is_not_acceptance: true

Failure mode:
If KOO cannot resolve the exact artifact locator/blob or finds a newer conflicting KOD writer state, KOO must stop and return the exact blocker rather than infer receipt or acceptance.
