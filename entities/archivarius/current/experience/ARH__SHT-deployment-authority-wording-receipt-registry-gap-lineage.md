# ARH event-lineage: SHT deployment-authority wording receipt / sender-registry gap

status: VERIFIED_REGISTRY_PROVENANCE_GAP
scope: bounded information-field sanitation
project_time: omitted; trusted project-time source not used

## Wake / preflight boundary

The mandatory GitHub preflight completed before this profile step.

Previous ARH boundary and pre-profile `main`:

`7e39a314e87d3c233c8c2196f13c5a0d0a1dc213`

Fresh delta at wake: `0 commits ahead / 0 behind`.

No new ARH task/result/blocker/approval/acceptance or dependency change was introduced by a fresh commit at wake.

## Sanitation finding

A completed ARH → SHT Exchange Gate chain exists for:

`entities/archivarius/outbox/ARH__SHT-entity-runner-deployment-authority-wording-gap__SHT.md`

but `registry/by-sender/archivarius.jsonl` contains no sender event for this exact artifact.

This is a sender-side provenance/bookkeeping gap. It is not evidence that delivery, processing, correction or acceptance failed.

## Exact source identity

artifact: `entities/archivarius/outbox/ARH__SHT-entity-runner-deployment-authority-wording-gap__SHT.md`
artifact_commit: `9cac584d3e12b188aae38869961f9cc84e6dcf33`
artifact_blob: `8b746671fe84fabb1e9bff39ff77aa42571c171e`

dispatch: `routes/dispatch/ARH__SHT-entity-runner-deployment-authority-wording-gap__SHT.md`
dispatch_commit: `089a6cb8c756a9296e9935c642d47c337390aa00`

receipt: `routes/receipts/ARH__SHT-entity-runner-deployment-authority-wording-gap__SHT.receipt.md`
receipt_commit: `ecb4741bf76a40ced480205187ab99c641e427d2`
receipt_blob: `ba885542538a11db4761a8be9710d0931610b64e`

## Receipt semantics

The exact receipt proves:

- `status: received`;
- `content_review: completed`;
- `finding: accepted`;
- correction commit `61ed3dc198c334ad1cf260e961d27d3d9df52a3d`;
- correction scope limited to status/provenance wording.

The correction narrows the SHT state from a deployment-authority implication to bounded SIS preparation only. Provider-side action, deployment and E2E remain unproven/unapproved. The historical package-integrity FAIL remains preserved.

No broader semantic acceptance, provider execution, deployment PASS, E2E PASS, writer authority or canon promotion is inferred.

## Registry check

Exact search of the current `registry/by-sender/archivarius.jsonl` for:

`ARH__SHT-entity-runner-deployment-authority-wording-gap__SHT.md`

returned no match.

Therefore the sender registry is incomplete for an otherwise evidenced completed exchange.

## Allowed next sanitation step

Append one sender-side reconciliation event to `registry/by-sender/archivarius.jsonl` that:

- preserves all historical rows unchanged;
- records the exact artifact/dispatch/receipt identities above;
- records `received`, `content_review: completed`, and `finding: accepted` only as proven by the receipt;
- records correction commit `61ed3dc198c334ad1cf260e961d27d3d9df52a3d`;
- preserves the bounded authority note that provider action, deployment and E2E remain unproven/unapproved;
- does not invent acceptance beyond the receipt wording.

This lineage file itself does not perform that registry append and does not alter any canonical or writer authority state.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: зафиксировать доказанный sender-registry provenance gap завершённой ARH → SHT sanitation-цепочки
СТАТУС: verified_registry_provenance_gap
