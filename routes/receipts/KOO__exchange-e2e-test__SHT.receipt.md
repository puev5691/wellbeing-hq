# Receipt SHT ← KOO: end-to-end test

exchange_gate: v1
sender: koordinator
recipient: shtabist
artifact: entities/koordinator/outbox/KOO__exchange-e2e-test__SHT.md
artifact_commit: 1d27fa1bd6b5befeb16a0aa3bb6a89f82608a95c
artifact_blob: 20174a943debf3ba7a184d7dea9f5fa0356aa8d2
dispatch: routes/dispatch/KOO__exchange-e2e-test__SHT.md
status: received
identity_check: PASS
content_read: yes
acceptance: separate
acceptance_result: entities/shtabist/outbox/SHT__exchange-e2e-test-result__KOO.md
project_time: omitted; trusted project-time source not used

Receipt подтверждает доступ ШТАБИСТА к требуемой immutable-версии и совпадение locator/version identity. Содержательное acceptance зафиксировано отдельно.
