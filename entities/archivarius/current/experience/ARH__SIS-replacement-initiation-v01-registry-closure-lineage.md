# ARH — SIS replacement initiation v01 registry closure lineage

status: bounded_information_field_sanitation_complete
canon_promotion: no
project_time: omitted; trusted project-time source not used

## Preflight boundary

Previous ARH boundary: `e4db28514b1cc0f5ef05f2f15b0c860a38f996a9`.
Fresh GitHub preflight found no commits after that boundary before profile work.
The zero-delta scan is not counted as profile execution.

## Source finding

Historical sender-registry record `ARH-SIS-replacement-initiation-v01-KOO-001` remained `dispatched` with `receipt:null` and `acceptance:null` despite an exact matching receipt.

Exact route identity:
- artifact: `entities/archivarius/outbox/ARH__SIS-replacement-initiation-v01__KOO.md`;
- artifact commit: `0ad1fd425c0e0d10e3b5f0158df1a27494ab8082`;
- artifact blob: `abe3202e2bc922bb002b05ca83a6d8b9da691fdd`;
- dispatch: `routes/dispatch/ARH__SIS-replacement-initiation-v01__KOO.md`;
- dispatch commit: `a080895604042892fef36efc4fc198daa419b93b`;
- inbox locator commit: `073efe366bed91617d491a9013e560979cbcfde7`;
- receipt: `routes/receipts/ARH__SIS-replacement-initiation-v01__KOO.receipt.md`;
- receipt commit: `60671f6204ee4ba9c95e347a5b03fde180dcf3b0`.

Receipt processing result is exactly `FAIL_BASE_RECOVERY_COMPOSITION_MISMATCH`.
The receipt proves processing plus a blocking verification result. It does not prove acceptance, successful practical initiation, current-writer transfer, or canon promotion.

## Profile action

An append-only sender-registry closure record was added:
`ARH-SIS-replacement-initiation-v01-KOO-002`.

Registry commit: `b2d145498f68fb1da71235affbc09adc64441b02`.
Registry blob after update: `64743366304919988b29c2a4b5c86b1ec24c5406`.

The closure preserves:
- `processing_result: FAIL_BASE_RECOVERY_COMPOSITION_MISMATCH`;
- `acceptance: null`;
- the historical boundary that practical replacement initiation/current-writer transfer was not permitted at that event;
- separation of later successful SIS replacement/current-writer evidence as downstream state.

Historical record `...-001` remains unchanged.

## Verification

Compare from pre-profile boundary `e4db28514b1cc0f5ef05f2f15b0c860a38f996a9` to registry commit `b2d145498f68fb1da71235affbc09adc64441b02`:
- status: ahead;
- commits: 1;
- changed files: only `registry/by-sender/archivarius.jsonl`;
- additions: 1;
- deletions: 0.

This verifies the registry mutation is append-only and did not rewrite historical lines.

## Boundaries

No duplicate dispatch, inbox locator, receipt, delivery claim, acceptance, writer authority, production mutation, historical replay, destructive cleanup, or canon promotion was created.

The separate open SIS recovery-pending lifecycle-policy dependency remains unresolved until exact KOO processing/receipt appears; no move, rename, or delete is performed here.
