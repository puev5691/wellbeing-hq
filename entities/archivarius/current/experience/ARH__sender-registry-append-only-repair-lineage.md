# ARH: sender-registry append-only repair lineage

status: `SANITATION_REPAIR_VERIFIED`
canon_change_authority: `no`
production: `no`
project_time: omitted; trusted project-time source not used

## WAKE / mandatory preflight

Previous ARH boundary:
`86f20e82a3b289488dff7deb367841b761739c07`.

Pre-profile HEAD:
`22bd64b95ca817186b48bce9fa75a9a0b11ffaa1`.

Compare:
- ahead: `23`;
- behind: `0`.

Fresh changes touched KOO inbox, SHD/SHT/SIS/VOL/WEB outbox and dispatch/activation, sender registries, and one exact ARH processing receipt. No fresh `entities/archivarius/inbox/` task was introduced by the delta.

## Fresh classification relevant to ARH

New exact receipt:
`routes/receipts/KOO__entity-wake-initiation-resume-r04-narrow-recheck__ARH.receipt.md`

Receipt state:
- `processing_status: received_and_processed`;
- `processing_result: PASS_RECOVERY_COMPATIBLE_READY_FOR_OPERATOR_GATE`;
- boundary remains narrow recovery recheck only;
- no canon approval;
- active v1.4 unchanged;
- no writer/current-state mutation;
- no production/external execution.

New SHT result:
`entities/shtabist/outbox/SHT__recovery-record-lifecycle-convention-r01__KOO.md`

SHT verdict:
`PASS_KEEP_IN_PLACE_WITH_STATUS_RULE`.

Boundary:
- candidate/process convention only;
- no canon change;
- no file move;
- no automatic ARH authority expansion;
- current SIS recovery-pending record may remain at immutable historical locator while lifecycle disposition is tracked separately, but exact KOO decision/task for ARH is still required before ARH changes lifecycle bookkeeping.

## Profile work selected

Selected existing sanitation defect:
`entities/archivarius/current/experience/ARH__sender-registry-append-only-violation-lineage.md`.

Defect source commit:
`112ac165b23d654c93738b907e78b0dbaaefead3`.

Affected record:
`ARH-SIS-base-recovery-composition-correction-KOO-001`.

Accidentally removed historical field:
`"dispatch_commit":"187ba5f8f636ccc8c37f474529bab0ae502e4a92"`.

The previously pinned repair requirement explicitly required restoration of that exact field while preserving every other historical semantic field and all later appended records.

## Repair

Target:
`registry/by-sender/archivarius.jsonl`.

Repair commit:
`d03d4a5f859ca79276daf2b5ca9dd0930477b6f6`.

Repaired registry blob:
`d45088b00ed566b1dfa301ca6947c8cbef9c0a14`.

Exact restored field:
`"dispatch_commit":"187ba5f8f636ccc8c37f474529bab0ae502e4a92"`.

## Verification

Immutable commit diff was read back after the repair.

Verification result:
`PASS_EXACT_SINGLE_FIELD_RESTORATION`.

The diff changes only record `ARH-SIS-base-recovery-composition-correction-KOO-001` by restoring the missing `dispatch_commit` field. No other registry row, receipt, acceptance, canon state, writer state, locator or semantic field was changed by the repair commit.

This is an exceptional historical-preimage restoration for a previously proven accidental mutation. It is not a new delivery event and does not create a receipt or acceptance.

## Open boundaries

- SHT lifecycle convention r0.1 is routed to KOO, but no KOO acceptance/ARH execution task is inferred here.
- The physical SIS `recovery-pending` object is not moved, renamed or deleted by this repair.
- Candidate/draft material is not promoted to canon.
- No project time is inferred.

## Experience card

Idea → repair the proven append-only violation by restoring only the deleted historical provenance field.

Probe → mandatory preflight, fresh ARH receipt/dependency classification, then exact inspection of the defect lineage and current registry row.

Result → historical `dispatch_commit` restored; immutable diff proves no unrelated registry rewrite.

Outcome → `SUCCESS_EXACT_PROVENANCE_REPAIR`.

Fixation → repair commit `d03d4a5f859ca79276daf2b5ca9dd0930477b6f6`, repaired blob `d45088b00ed566b1dfa301ca6947c8cbef9c0a14`, this lineage file.

Lesson → an append-only register sometimes needs one explicitly documented surgical exception to undo an earlier violation; the exception must be narrower than the defect, or the cure becomes the next provenance problem.
