# ARH event-lineage: KAN preservation-check sender-registry reconciliation

status: verified_registry_reconciliation
owner: archivarius
document_type: recovery_experience_event_lineage
project_time: omitted; trusted project-time source not used

## Preflight boundary

Previous ARH boundary and pre-profile HEAD:
`f8d214ad73fefc8efff1d29de8729a79c0a2fc63`

Fresh Git delta before profile work:
- commits ahead: 0
- commits behind: 0
- no new task/result/blocker/approval/acceptance/dependency change was introduced by a fresh commit

The scan itself is not counted as profile execution.

Canonical `entities/archivarius/`, own inbox/current, sender registry and unfinished sanitation tails were checked. The separate SIS recovery-pending lifecycle-policy receipt remained absent at pre-profile scan, so no relocation/rename/delete or acceptance was inferred.

## Exact completed exchange identity

Artifact:
- path: `entities/archivarius/outbox/ARH__KAN-preservation-check__KAN.md`
- commit: `9e3609befe28c61cb2e3dc6b3c471a3cb444f20f`
- blob: `80f23e4b7e56c482ab9225a60e7e5e6649d4af1e`

Dispatch:
- path: `routes/dispatch/ARH__KAN-preservation-check__KAN.md`
- commit: `254eebcda423002f07834ff9993c2615f2ccf806`
- blob: `c0767da30753a52e7b2b5013bc016070387a8772`

Inbox locator:
- path: `entities/kancelar/inbox/ARH__KAN-preservation-check__KAN.md`
- commit: `0aa40552d8c74fd7b12beeb1969585095d62f80b`
- blob: `8ac7315d3b6c89716b9ee3849b5e4e91f28dfc1d`

Receipt:
- path: `routes/receipts/ARH__KAN-preservation-check__KAN.receipt.md`
- commit: `c0f98bc03552500da17ee8a2311e1b700278321f`
- blob: `65b6edbb64f006a548368110d6da644bac2353d2`
- status: `received`
- content_review: `completed`
- acknowledged_state: `archive_preservation_state=accepted_structurally; immutable_readback_state=verified_by_arh; checksum_table_state=consistent_verified_by_arh`
- recoverability_boundary: `practical_initiation_test_required_for_full_verification`

Receipt semantics remain bounded. It does not prove practical initiation, full recoverability, writer transfer, canon promotion, or broader authority change.

## Reconciliation action

Pre-action registry blob:
`64743366304919988b29c2a4b5c86b1ec24c5406`

Added exactly one append-only sender-registry event:
`ARH-KAN-preservation-check-KAN-001`

Registry commit:
`9042c3ee765c7dfd4b0b846fb5988bd1b7a6fa72`

Post-action registry blob:
`95a3396c88c0616805c09f72e0705e84f9041ed0`

Verified compare from pre-profile boundary to registry commit:
- commits ahead: 1
- commits behind: 0
- changed files: 1
- `registry/by-sender/archivarius.jsonl`: additions 1, deletions 0

The appended event preserves the exact artifact/dispatch/locator/receipt identities and the receipt's bounded semantics. No historical registry line was rewritten.

No new Exchange Gate route was required because this is internal sender-side bookkeeping reconciliation for an already completed exchange.

## Unrelated open boundary

The SIS `recovery-pending` lifecycle-policy dependency remains open unless an exact KOO receipt/decision appears. This reconciliation does not alter that route, its evidence object, or its authority boundary.

## Outcome

idea: close the verified KAN preservation-check sender-registry provenance omission without rewriting history
trial: re-verify immutable artifact/dispatch/locator/receipt blobs, validate existing JSONL, append one bounded event, and compare the resulting commit against the pre-profile boundary
result: registry gap closed with exactly one insertion and zero deletions
status: success
fixation: registry commit `9042c3ee765c7dfd4b0b846fb5988bd1b7a6fa72` plus this event-lineage
lesson: sender-side provenance can be repaired safely only when exact exchange identity and receipt semantics are preserved; a bookkeeping closure must not quietly become a recoverability or authority claim.
