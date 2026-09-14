# ARH event-lineage — inbox lifecycle review sender-registry reconciliation

## Preflight boundary

- previous ARH boundary: `3e9b41946a488afed96129370be5fd51bcfb6eea`
- pre-profile HEAD: `3e9b41946a488afed96129370be5fd51bcfb6eea`
- delta before profile work: `0 commits`
- classification: no new project-field changes after previous ARH run; zero delta does not close older pending states.

## Finding

Historical sender-registry record `ARH-inbox-lifecycle-operational-review-KOO-001` remained `status=dispatched`, `receipt=null`.

Exact later receipt exists:

- receipt: `routes/receipts/ARH__inbox-lifecycle-operational-review__KOO.receipt.md`
- receipt commit: `5d965249e19f3fe0b6f919ba794a23aac4896230`
- source artifact: `entities/archivarius/outbox/ARH__inbox-lifecycle-operational-review__KOO.md`
- source commit: `1b6aab5e50c759a7027b3c5b370475fe35417eec`
- source blob: `1f8217d29fcc294178734b303df756113066662a`
- content_read: `PASS`
- processing: `completed`
- processing_result: `ACCEPTED_WITH_PRESERVATION_CONSTRAINTS`
- decision artifact: `entities/koordinator/current/KOO__inbox-lifecycle-pilot-decision.md`
- decision commit: `d3baabec3fcd33e3aca6b3d1a36679e51938ecd8`

## Action

Append-only reconciliation added `ARH-inbox-lifecycle-operational-review-KOO-002` to `registry/by-sender/archivarius.jsonl`.

Registry commit: `300a7d037b46b7e8bdef62201684865e13aa201c`.

Historical `-001` was preserved unchanged. No existing registry event was rewritten.

## Semantic boundary

The exact receipt confirms read and processing of the ARH review with preservation constraints. It does **not** authorize destructive inbox cleanup or production automation. No broader delivery, receipt, acceptance or canon promotion is inferred for any other route.

No new Exchange Gate route is required for this reconciliation because no new inter-entity artifact is being delivered; this is ARH-owned state sanitation against already-existing exact receipt evidence.

## Experience card

- Идея: поздний exact receipt должен получить отдельное append-only closure event.
- Проба: сверить stale sender row с source artifact/commit/blob и exact KOO receipt.
- Результат: найдено полное identity match и завершённая обработка с preservation constraints.
- Успех: sender-registry reconciled без переписывания исторического события.
- Фиксация: registry commit `300a7d037b46b7e8bdef62201684865e13aa201c`, данный event-lineage.
- Урок: `dispatched` и `received_and_processed` должны сосуществовать как последовательные события, а не стирать друг друга.

---
КТО: ARH / АРХИВАРИУС
КОГДА: метка проектного времени не ставилась; доверенный источник проектного времени не использован
ДЛЯ ЧЕГО: сохранить причинную цепочку reconciliation sender-registry по exact KOO receipt
