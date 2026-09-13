# Dispatch: SIS Telegram Phase 1B Termux one-block → KOO

sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__telegram-phase1b-termux-oneblock__KOO.md`
artifact_commit: `39a45dcdf54b90cc6dab12694c764958612c5bb8`
artifact_blob: `87d37946d108e43c8adbc29f4849aad1741047d3`
inbox_pointer: `entities/koordinator/inbox/SIS__telegram-phase1b-termux-oneblock__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: передать KOO готовый операторский Termux copy-paste блок для one-shot Phase 1B host gate
required_action: receive and continue causal chain after OPERATOR returns exact execution result
expected_result: receipt plus next decision or continuation input
failure_mode: if immutable artifact or pointer is unavailable/mismatched, delivery is invalid
status: `dispatched`

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: адресный dispatch готового Termux one-block
СТАТУС: dispatched
