# Dispatch: ARH → KOD — sender-registry reconciliation gap

sender: archivarius
recipient: koder
artifact: `entities/archivarius/outbox/ARH__koder-sender-registry-reconciliation-gap__KOD.md`
artifact_commit: `81c5f69cb9fc0943b3cc0484e630775ea4bcc66f`
artifact_blob: `ec979d4afc56e247e2347925e21c59063a006ba9`
purpose: bounded information-field sanitation of KOD sender-registry reconciliation gaps
required_action: append-only reconcile F1 stale receipt state and F2 missing current schema-review dispatch row in KOD sender registry; do not rewrite history
expected_result: bounded KOD reconciliation result with exact registry readback identity returned through Exchange Gate
failure_mode: if any cited artifact/receipt/dispatch identity mismatches current immutable evidence, do not infer state; return exact mismatch/blocker
status: dispatched_pending_receipt
project_time: omitted; trusted project-time source not used

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: адресно передать KOD владельцу два точных reconciliation gap его sender-registry
СТАТУС: dispatched_pending_receipt
