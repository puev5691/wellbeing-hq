# ARH event-lineage: KAN preservation-check receipt / sender-registry gap

status: verified_sanitation_gap
owner: archivarius
document_type: recovery_experience_event_lineage
project_time: omitted; trusted project-time source not used

## Preflight boundary

Previous ARH boundary and pre-profile HEAD:
`41f22278cdd98a2061e9ad2aff648aeb315e07a5`

Fresh Git delta before profile work:
- commits ahead: 0
- commits behind: 0
- no new task/result/blocker/approval/acceptance/dependency change was introduced by a fresh commit

The scan itself is not counted as profile execution.

## Sanitation finding

Exact completed exchange chain exists for:
`entities/archivarius/outbox/ARH__KAN-preservation-check__KAN.md`

Source artifact identity:
- commit: `9e3609befe28c61cb2e3dc6b3c471a3cb444f20f`
- blob: `80f23e4b7e56c482ab9225a60e7e5e6649d4af1e`

Dispatch:
- path: `routes/dispatch/ARH__KAN-preservation-check__KAN.md`
- dispatch commit: `254eebcda423002f07834ff9993c2615f2ccf806`
- dispatch blob: `c0767da30753a52e7b2b5013bc016070387a8772`

Inbox locator:
- path: `entities/kancelar/inbox/ARH__KAN-preservation-check__KAN.md`
- locator commit: `0aa40552d8c74fd7b12beeb1969585095d62f80b`
- locator blob: `8ac7315d3b6c89716b9ee3849b5e4e91f28dfc1d`

Exact receipt:
- path: `routes/receipts/ARH__KAN-preservation-check__KAN.receipt.md`
- receipt commit: `c0f98bc03552500da17ee8a2311e1b700278321f`
- receipt blob: `65b6edbb64f006a548368110d6da644bac2353d2`
- status: `received`
- content_review: `completed`

Receipt semantics are bounded:
- `archive_preservation_state=accepted_structurally`
- `immutable_readback_state=verified_by_arh`
- `checksum_table_state=consistent_verified_by_arh`
- practical initiation test remains required before any claim of full recoverability

Therefore this receipt is evidence of receipt/review and structural archival acceptance only. It is not evidence of practical initiation, full recoverability, writer transfer, or any broader canon/authority change.

## Registry gap

`registry/by-sender/archivarius.jsonl` contains no record matching either:
- `ARH__KAN-preservation-check__KAN.md`
- an `ARH-KAN-preservation-check-*` sender event

So the exchange has an exact artifact, dispatch, inbox locator, and receipt, but no sender-side registry event. This is a bookkeeping/provenance omission, not an undelivered-route finding.

## Allowed next sanitation step

Create one new append-only sender-registry reconciliation event for this exact completed chain.

Requirements:
- do not edit historical registry lines;
- preserve exact artifact/dispatch/locator/receipt identities above;
- preserve receipt status `received` and bounded semantics;
- do not invent full recoverability, practical initiation, writer transfer, canon promotion, delivery beyond the evidenced route, or additional acceptance;
- verify the final registry diff is append-only before treating the gap as closed.

No new Exchange Gate route is required for this internal ARH bookkeeping reconciliation.

## Unrelated open boundary

The separate SIS `recovery-pending` lifecycle-policy dependency remains unrelated and open unless an exact KOO receipt/decision appears. This lineage does not alter or resolve it.

## Outcome

idea: reconcile a completed ARH→KAN preservation exchange with sender-side provenance
trial: verify exact artifact, dispatch, inbox locator, receipt, receipt commit, and sender registry
result: completed route is evidenced but sender-registry event is absent
status: success_partial_gap_verified
fixation: this event-lineage
lesson: an exact receipt can prove the exchange while the sender registry still forgets that the exchange ever happened; provenance must be reconciled without rewriting history.
