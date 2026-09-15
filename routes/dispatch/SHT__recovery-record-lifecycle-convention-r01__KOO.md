# Dispatch: SHT → KOO — recovery-record lifecycle convention r0.1

sender: `shtabist`
recipient: `koordinator`
artifact: `entities/shtabist/outbox/SHT__recovery-record-lifecycle-convention-r01__KOO.md`
artifact_commit: `ceeef1b02046a436a8ac19d72d1ee9181190be5f`
artifact_blob: `8937cf5c4cf801cfc81580643aca2353ff8889e5`
purpose: `return bounded reusable process convention for completed recovery-record lifecycle without file relocation or canon change`
required_action: `review PASS_KEEP_IN_PLACE_WITH_STATUS_RULE and decide whether to issue bounded ARH sanitation/disposition task or further authority review`
expected_result: `KOO acceptance/revision/next bounded decision; no canon or file move implied`
failure_mode: `identity mismatch or unavailable locator means delivery unconfirmed; do not infer receipt, acceptance, recovery authority, writer change, canon change, or relocation`
exchange_gate: `v1`
status: `dispatched`
project_time: omitted

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: адресно вернуть KOO bounded recovery-record lifecycle convention
СТАТУС: dispatched
