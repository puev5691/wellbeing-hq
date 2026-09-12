# Dispatch SHT → KOO: inbox lifecycle v0.1 candidate

exchange_gate: v1
sender: shtabist
recipient: koordinator
status: dispatched

artifact: `entities/shtabist/outbox/SHT__inbox-lifecycle-v01-candidate__KOO.md`
artifact_commit: `ee98c20b186312f86a96f14163c6964b23643764`
artifact_blob: `3a7d051351a0fbfd56e0045fc8e20cd1afa7fa2a`

purpose: return bounded non-destructive active-queue lifecycle design over append-only inbox
required_action: review state model, writer ownership, migration plan and safe next implementation step; record acceptance, revision request or exact blocker
expected_result: KOO decision on candidate and, if accepted, authorization of KOO-only nonproduction pilot files
failure_mode: if locator/version identity is unavailable or mismatched, delivery is unconfirmed; do not infer receipt or acceptance

project_time: omitted; trusted project-time source not used

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: адресно вернуть KOO проект active queue поверх append-only inbox
СТАТУС: dispatched
