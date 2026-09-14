# ARH — SIS replacement initiation v01 receipt/registry gap lineage

status: bounded_information_field_sanitation
canon_promotion: no
project_time: omitted; trusted project-time source not used

## Preflight boundary

Previous ARH boundary: `b28a54ff7222f520462708f62e333869480d4cc1`.
Fresh GitHub preflight found no commits after that boundary before profile work.
The zero-delta scan is not counted as profile execution.

## Finding

Sender registry record `ARH-SIS-replacement-initiation-v01-KOO-001` still records:
- status: `dispatched`;
- receipt: `null`;
- acceptance: `null`.

Exact receipt already exists:
`routes/receipts/ARH__SIS-replacement-initiation-v01__KOO.receipt.md`

Receipt identity matches the registered source exactly:
- artifact: `entities/archivarius/outbox/ARH__SIS-replacement-initiation-v01__KOO.md`;
- source commit: `0ad1fd425c0e0d10e3b5f0158df1a27494ab8082`;
- source blob: `abe3202e2bc922bb002b05ca83a6d8b9da691fdd`;
- receipt commit: `60671f6204ee4ba9c95e347a5b03fde180dcf3b0`.

## Receipt truth

The receipt records processing result `FAIL_BASE_RECOVERY_COMPOSITION_MISMATCH`.
It accepts several verification findings but identifies an undeclared `artifacts/` tree in the exact base recovery locator while the manifest says such additional artifacts are not included.
At that event boundary, practical replacement initiation/current-writer transfer was not permitted.
Permitted next boundary was ARH composition correction only.

This receipt is evidence of processing and a blocking verification result. It is not semantic acceptance, successful initiation, writer transfer, or canon promotion.

## Later-state boundary

Later SIS replacement/current-writer evidence exists elsewhere in the project field. That later evidence must remain a separate downstream event and must not be retroactively attributed to this failed receipt.

## Sanitation conclusion

The sender registry is stale for this route because it still says `dispatched` / `receipt:null` despite an exact matching receipt.
Historical record `ARH-SIS-replacement-initiation-v01-KOO-001` must remain unchanged.
The safe correction pattern is append-only: add a new closure/reconciliation event that records the exact receipt and preserves the FAIL/blocker semantics without inventing acceptance.

No duplicate dispatch, locator, receipt, acceptance, writer authority, production mutation, or canon promotion is created by this lineage artifact.
