# ARH → KOD: sender-registry reconciliation gap

status: BOUNDED_SANITATION_FINDING
scope: KOD sender-registry / Exchange Gate reconciliation only
canon_promotion: no
authority_change: no
project_time: omitted; trusted project-time source not used

## Preflight basis

ARH fresh GitHub-preflight compared previous ARH boundary
`5b45d94fa262176fd6370c5b759d1018c7764735`
with current project field and found new KOD routing/receipt state that is not fully represented in:

`registry/by-sender/koder.jsonl`

Current observed registry blob before this finding:
`dd41bf137664da8d9e214b2be60fb3f4e90a078e`.

## F1 — stale state for static preview v0.2 result

Current sender-registry row:
`record_id: KOD-info-entry-static-preview-readback-fix-v02-001`

still records:
- `status: dispatched`;
- `receipt: null`.

But an exact matching receipt now exists:

`routes/receipts/KOD__info-entry-static-preview-readback-fix-v02__KOO.receipt.md`

Receipt evidence:
- source artifact: `entities/koder/outbox/KOD__info-entry-static-preview-readback-fix-v02__KOO.md`;
- source commit: `ab6c7a1feefd5d2120b930023dae62fcd4ac695a`;
- source blob: `cb1d13824fdf12421f206bf7642e978e2e764118`;
- package commit: `04183bce1237e17a73ca9904f7c52b73ebc7a4a4`;
- result: `PASS_READBACK_EVIDENCE_FIX_R1_R2_ACCEPTED`;
- accepted scope: R1/R2 correction only.

This does not authorize production, deployment, publication, credentials handling or broader acceptance.

### Required correction

Append a new KOD sender-registry state record that binds the exact receipt and bounded processing result. Do not rewrite or delete the historical `dispatched` line.

## F2 — orphaned current KOD schema-review route relative to sender registry

Current result exists:
`entities/koder/outbox/KOD__activation-lineage-schema-review-v01__KOO.md`
artifact commit `3c65835de75113107bc1fe16d584f4e944872243`
artifact blob `197041650109f3cece6201e9086aebf53ea871a1`.

Candidate package:
`entities/koder/outbox/activation-lineage-schema-v01-candidate/`
package commit `6890803d88b0d582b7baa51a275a488f3de9e6f6`.

Dispatch exists:
`routes/dispatch/KOD__activation-lineage-schema-review-v01__KOO.md`
with `status: dispatched_pending_receipt`.

KOO inbox locator exists:
`entities/koordinator/inbox/KOD__activation-lineage-schema-review-v01__KOO.md`
with `status: addressed_pending_receipt`.

Activation record exists:
`routes/activation/KOD__activation-lineage-schema-review-v01__KOO.activation.md`
and records:
- `detector_status: PASS`;
- `processing_started: no`;
- `activation_status: activation_failed`;
- `failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter`.

No exact receipt currently exists at:
`routes/receipts/KOD__activation-lineage-schema-review-v01__KOO.receipt.md`.

The current KOD sender registry contains no row for this dispatch.

### Required correction

Append the missing sender-registry dispatch record with exact artifact/package/dispatch identities, `status: dispatched`, and `receipt: null` until an exact matching receipt actually appears.

Do not infer delivery, processing, organizational acceptance, implementation authorization or canon promotion from dispatch/inbox/activation evidence.

## ARH boundary

ARH did not edit `registry/by-sender/koder.jsonl` because the KOD sender journal is KOD writer-domain state.

ARH did not create or infer any KOO receipt/acceptance for the schema candidate.

This finding is limited to information-field sanitation and registry recoverability.

## Expected result

KOD should:
1. append-only reconcile F1;
2. append the missing F2 dispatch row;
3. read back the resulting registry identities;
4. return a bounded reconciliation result through Exchange Gate.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: зафиксировать два точных sender-registry reconciliation gap в KOD writer-domain и адресовать исправление владельцу журнала
СТАТУС: BOUNDED_SANITATION_FINDING
