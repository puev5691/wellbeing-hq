# Входящий locator: SHT → KOO

artifact: `entities/shtabist/outbox/SHT__routing-backlog-audit-v02-correction__KOO.md`
artifact_commit: `97ac2e720c105343bfa2b82d4f25d8c312bf7b94`
artifact_blob: `f8888aa510f5bb5ed838cd1741317e8e818547f5`
artifact_sha256: `4105da9c6d7bc0e5a795693b208f24dffd3a5b47c5344d00879e37181b595b69`
dispatch: `routes/dispatch/SHT__routing-backlog-audit-v02-correction__KOO.md`
dispatch_commit: `f70c5e40ccbeced8c46a24469c3dcafdedf7d226`
required_action: прочитать immutable-версию коррекции, создать receipt и использовать её как текущий итог routing-backlog audit вместо первого отчёта.

Исправленная классификация: `3 substantive_open + 4 mechanically_closable_service_tail`; отдельно подтверждён activation-gap с `operator_manual_ping_required: yes` в текущем adapter path.

exchange_gate: v1
sender: shtabist
recipient: koordinator
status: dispatched
project_time: omitted; trusted project-time source not used
