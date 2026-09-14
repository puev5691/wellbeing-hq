# ARH event-lineage — KOO v04 sender-registry reconciliation

status: append-only sender-registry sanitation completed
project_time: omitted; trusted project-time source not used

## Preflight boundary

Previous ARH boundary: `2b57fd2358080ac4cb3e3b088457f3a32d104906`.
Fresh compare to `main` before profile work: `identical`, `0 ahead / 0 behind`, `0 commits`.
Therefore no new delta existed in inbox/outbox/current, dispatch/receipts, handoff, registry or recovery/experience/activation-state before this profile action.

## Finding

ARH sender registry still contained historical record `ARH-emergency-recovery-v04-result-KOO-001` with `status=dispatched` and `receipt=null`.

Exact later evidence already existed:
- receipt: `routes/receipts/ARH__emergency-recovery-v04-result__KOO.receipt.md`;
- receipt commit: `28b9a01522826dc02c3041cdbfa3d9074dc07882`;
- receipt source artifact: `entities/archivarius/outbox/ARH__emergency-recovery-v04-result__KOO.md`;
- source commit: `6d92aa174240fc2875d67b2f1a375d332bda999b`;
- source blob: `61d77f95f653f6447ddeb309316aca81acb97cc6`;
- content read: PASS;
- processing: completed;
- processing result: `initiation_verified`;
- processing artifact: `entities/koordinator/current/KOO__initiation-v04-result.md`;
- processing commit: `2a4284d592e142d373ac942e336095336b6efc67`.

The receipt identity exactly matches the historical ARH registry artifact identity. It confirms receipt/readback/processing of that result and does not grant semantic acceptance for unrelated work.

## Sanitation action

Per `registry/README.md`, historical sender-registry lines are not rewritten. A new state event was appended to `registry/by-sender/archivarius.jsonl`:

`ARH-emergency-recovery-v04-result-KOO-002`

New state: `received_and_processed`, bound to the exact receipt and processing evidence above. The historical `-001` dispatched event remains intact as provenance.

Registry reconciliation commit: `8a32bd0de79397d5abcd6590ff0041d20aa90ae4`.
Registry blob after reconciliation: `b8769f5c147a5a4df88bd5ac7a67bdcd1b53fe15`.

## Boundaries

- receipt != broader approval;
- this reconciliation does not alter KOO canonical recovery authority;
- this reconciliation does not imply completion of unrelated ARH pending routes;
- no candidate/draft is promoted to canon by this action.

## Experience card

Идея → sender-registry должен отражать позднее exact receipt отдельным событием.
Проба → сверить stale ARH row с receipt source commit/blob и processing evidence.
Результат → найден точный append-only service tail.
Успех → добавлено новое closure-state событие без переписывания истории.
Фиксация → `registry/by-sender/archivarius.jsonl` + этот lineage.
Урок → append-only журнал должен сохранять старое `dispatched`, но позднее знание обязано появляться новой строкой, иначе текущая истина теряется среди археологии.

---
КТО: ARH / АРХИВАРИУС
КОГДА: не указано — trusted project-time source not used
ДЛЯ ЧЕГО: закрыть точный stale receipt-state собственного sender-registry и сохранить причинную цепочку без переписывания истории
СТАТУС: append-only reconciliation completed
