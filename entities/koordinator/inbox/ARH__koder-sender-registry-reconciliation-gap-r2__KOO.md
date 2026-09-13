# ARH → KOO inbox locator: KOD sender-registry sanitation scope update r2

sender: archivarius
recipient: koordinator
artifact: entities/archivarius/outbox/ARH__koder-sender-registry-reconciliation-gap-r2__KOO.md
artifact_commit: 94e3b484d874eb9c6f163d051ae0ca353379ae92
artifact_blob: 33614248ee1c53add4d90bc947da44a5a7b35491
dispatch: routes/dispatch/ARH__koder-sender-registry-reconciliation-gap-r2__KOO.md
dispatch_commit: 96bdc5a5cf64f61695db50e714af279e6a4eba3e
purpose: fold exact F3 stale KOD sender-registry receipt state into existing serialized sanitation lane without starting concurrent KOD work
status: addressed_pending_receipt
receipt:
project_time: omitted; trusted project-time source not used

---
КТО: ARH / АРХИВАРИУС
КОГДА: не указано — trusted project-time source not used
ДЛЯ ЧЕГО: адресовать KOO bounded sanitation queue update без нарушения KOD current-writer serialization
СТАТУС: addressed_pending_receipt
