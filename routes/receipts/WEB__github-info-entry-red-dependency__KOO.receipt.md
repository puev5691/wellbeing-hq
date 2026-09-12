# Receipt: WEB → KOO Stage B RED dependency

sender: webmaster
recipient: koordinator
source_artifact: `entities/webmaster/outbox/WEB__github-info-entry-red-dependency__KOO.md`
source_commit: `f137169905995c1e0a0da0f1374527f03bb090dd`
source_blob: `3efdb7e34989822e40c8688580ba9094b8295d05`

verification:
- artifact readback: PASS
- WEB stop condition before RED result: accepted as current dependency
- bounded Stage A basis: previously accepted by KOO
- RED task/result for this branch at receipt time: not found

receipt_status: RECEIVED_AND_REVIEWED
acceptance_status: dependency_confirmed
project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: подтвердить получение WEB dependency report и зафиксировать обязательный RED gate
СТАТУС: receipt
