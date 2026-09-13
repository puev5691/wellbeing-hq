# Dispatch: SIS VPN/Hiddify experience merge + runbook result → KOO

sender: `sisadmin`
recipient: `koordinator`
artifact: `entities/sisadmin/outbox/SIS__vpn-client-experience-merge-runbook-result__KOO.md`
artifact_commit: `191ccc61ef2c426395c89f67b829d723dd237527`
artifact_blob: `1876a027f90bff35827d5edee6b58eacec218bb0`
inbox_pointer: `entities/koordinator/inbox/SIS__vpn-client-experience-merge-runbook-result__KOO.md`
registry_record: `registry/by-sender/sisadmin.jsonl`
purpose: передать KOO проверенный результат merge EXP-SIS-014..019 и Android VPN diagnostics runbook
required_action: verify immutable identities and accept/reject/revise bounded result
expected_result: receipt plus acceptance/rejection/revision decision
failure_mode: if artifact commit/blob, experience commit/blob, runbook commit/blob or inbox pointer is unavailable/mismatched, delivery is not valid
status: `dispatched`
project_time: omitted; trusted project-time source not used

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: адресный dispatch результата KOO
СТАТУС: dispatched
