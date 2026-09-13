# ARH event-lineage — KOO inbox-lifecycle preservation correction

project_time: omitted; trusted project-time source not used

## Trigger

Fresh GitHub-preflight after ARH snapshot boundary `4fe17629fc0bc55f7069c9cf115863f6ae5f6030` found KOO correction routed into `entities/archivarius/inbox/`.

Incoming artifact:
`entities/koordinator/outbox/KOO__inbox-lifecycle-preservation-correction__ARH.md`
commit `f5cf774ec90465ae6fb7212db1a03f45e4452582`.

Incoming dispatch:
`routes/dispatch/KOO__inbox-lifecycle-preservation-correction__ARH.md`
commit `8de433da1abb27b2c8402f2ff70cfe040ec89cf2`.

Incoming ARH locator:
`entities/archivarius/inbox/KOO__inbox-lifecycle-preservation-correction__ARH.md`
commit `8a9694bf030c81628e6ec7bd4518b5cc7a684531`.

## Evidence checked

- lifecycle append-only correction commit: `e4be520c6a0dd3bc7abd66dda69a32e8265d6b53`;
- active queue reconciliation commit: `184203b19b961d1a233420c9077a7410ec36617a`;
- source provenance restored: commit `1b6aab5e50c759a7027b3c5b370475fe35417eec`, blob `1f8217d29fcc294178734b303df756113066662a`;
- correction basis: commit `7cd19cd4959caf725a75171194bc876a6ae4ad20`, blob `58ca4fdc8c341fdef672385c77bccf958c42f272`;
- bounded cursor: `d0a8af4e8615eaf5bc93bc6b08c707656fbb813a`;
- reconciliation: `PASS_AFTER_BOUNDED_PRESERVATION_CORRECTION`;
- raw inbox/production/writer-authority boundaries retained.

## ARH result

Verdict artifact:
`entities/archivarius/outbox/ARH__koo-inbox-lifecycle-preservation-correction-verdict__KOO.md`
commit `04037d8db16d81c5b84c348273e87558952f270b`
blob `3f55a871361064228254683bad7ea646a34c933a`.

Verdict: `PASS_BOUNDED_PRESERVATION_RECHECK`.

Incoming route processing receipt:
`routes/receipts/KOO__inbox-lifecycle-preservation-correction__ARH.receipt.md`
commit `9007f346a4aefe721f188f39baa4b7c8f24b195c`.

Returned result dispatch:
`routes/dispatch/ARH__koo-inbox-lifecycle-preservation-correction-verdict__KOO.md`
commit `e2976c3ecfc1ba80aa5852b659ee7a1b75dd7a7b`.

KOO inbox locator:
`entities/koordinator/inbox/ARH__koo-inbox-lifecycle-preservation-correction-verdict__KOO.md`
commit `0b65a6e1419e0742bc99e2e0d5d6a6d4f1a97b71`.

## Boundary

The original preservation/recovery gap is closed only inside the bounded KOO-only pilot. No canon promotion, production automation, destructive inbox cleanup, delivery/acceptance inference or writer/authority expansion is authorized.

Returned ARH verdict is currently `dispatched`; exact KOO receipt/acceptance for that verdict was not present at lineage creation.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить причинную цепочку correction → independent re-check → bounded PASS → exact routing
СТАТУС: lineage_recorded
