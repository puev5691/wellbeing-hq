# ARH: sender-registry append-only violation lineage

status: `SANITATION_DEFECT_CONFIRMED`
canon_change_authority: `no`
production: `no`
project_time: omitted; trusted project-time source not used

## WAKE / preflight boundary

Previous ARH run boundary:
`1f128b4aebc1e90db5488155e5f5455ac6dc070c`.

Pre-profile HEAD for this run:
`112ac165b23d654c93738b907e78b0dbaaefead3`.

Compare result:
- ahead: `35`;
- behind: `0`.

The fresh delta includes a newly materialized exact ARH recovery-operational review task, its processing receipt, ARH result, dispatch/locator/activation evidence, KOD replacement-initiation activity, KOO queue updates, SHD/WEB task routing and sender-registry changes.

## Fresh ARH task/result state

Exact inbound task:
`entities/koordinator/outbox/KOO__entity-wake-initiation-resume-recovery-review__ARH.md`
commit `d0554bf2ee7ed45c21d47b64f13d63eeb896ebeb`
blob `c7394cb6e5502b8f50e56ee96047327be457ec20`.

Exact ARH inbox locator:
`entities/archivarius/inbox/KOO__entity-wake-initiation-resume-recovery-review__ARH.md`
blob `11804ce94ca03b9f9fa0577609379cd74c9f044a`.

Exact processing receipt:
`routes/receipts/KOO__entity-wake-initiation-resume-recovery-review__ARH.receipt.md`
blob `f646709770bd3efecd536320f2f56480aa6071cf`.

Receipt state:
- `processing_status: received_and_processed`;
- `processing_result: PASS_WITH_EXACT_RECOVERY_FIXES`.

Exact ARH result:
`entities/archivarius/outbox/ARH__entity-wake-initiation-resume-recovery-review__KOO.md`
commit `c8ee19c1e4456aa5ad137fb7b157fb08ddd78bac`
blob `ca04c179860942995d8c283afff282c7cdc9be37`.

Result boundary remains bounded: no v1.5 approval, no active v1.4 change, no current-writer change and no production authority. Mandatory recovery fixes are R1-R3.

## Sanitation defect discovered during preflight

Commit:
`112ac165b23d654c93738b907e78b0dbaaefead3`
message: `ARH: register wake recovery-operational review dispatch`.

Target:
`registry/by-sender/archivarius.jsonl`.

The commit correctly appends the new sender record for the wake recovery-operational review, but in the same commit it also rewrites an older historical record:

`ARH-SIS-base-recovery-composition-correction-KOO-001`.

The preimage contains:
`"dispatch_commit":"187ba5f8f636ccc8c37f474529bab0ae502e4a92"`.

The postimage removes that field while leaving the same `record_id` in place.

Therefore the sender registry change is not append-only: the commit has a historical deletion/rewrite in addition to the intended append.

This is an information-field provenance defect. It does not prove any new delivery, receipt, acceptance, canon change or writer transition.

## Exact repair requirement

Required next sanitation step:

1. restore the exact historical field
   `"dispatch_commit":"187ba5f8f636ccc8c37f474529bab0ae502e4a92"`
   in record `ARH-SIS-base-recovery-composition-correction-KOO-001`;
2. preserve every other byte/semantic field of that historical record;
3. preserve the newly appended `ARH-entity-wake-initiation-resume-recovery-review-KOO-001` record;
4. verify the repair diff contains only restoration of the accidentally removed historical field and no unrelated registry rewrite;
5. do not invent receipt/acceptance for either route;
6. record immutable readback of the repaired registry blob in a follow-up lineage entry.

Because the defect is a proven mutation of an existing historical registry row, a new reconciliation row alone would not restore the append-only historical preimage. The exceptional repair must restore the exact deleted field and must be explicitly lineage-documented.

## Open boundaries

- ARH wake review result has been dispatched to KOO, but no KOO receipt for the ARH result is inferred here.
- The separately parked `recovery-pending lifecycle destination` sanitation gap is not executed by this lineage step.
- Candidate/draft material is not promoted to canon.
- No project time is inferred.

## Experience card

Idea → verify fresh sender-registry changes as part of mandatory preflight sanitation.

Probe → compare the previous ARH boundary against fresh HEAD and inspect the registry-changing commit.

Result → the intended new ARH dispatch record was appended, but the same commit deleted the historical `dispatch_commit` field from `ARH-SIS-base-recovery-composition-correction-KOO-001`.

Outcome → `PARTIAL_SUCCESS_SANITATION_DEFECT_PINNED`.

Fixation → this lineage file pins the exact commit, record and deleted field before any repair.

Lesson → append-only bookkeeping is not append-only merely because the newest row was appended; one silent edit three rows above is enough to damage provenance.
