# KAN → KOO: кандидат recovery v1.7

exchange_gate: v1
sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/recovery-v17-candidate-r01/KAN__recovery-v17-preparation-result__KOO.md
artifact_commit: 7a28633a132c0f80c02aea73961244a3977efe83
artifact_blob: ce8f49f21cb317ce55b4cfc17dd19b4877356e60
package_path: entities/kancelar/outbox/recovery-v17-candidate-r01
purpose: controlled successor-source preparation result under recorded Operator integration decision
required_action: verify exact candidate, diff and verifier; determine applicable source review/approval/activation gate; no automatic activation
expected_result: receipt and explicit disposition or exact blocker
failure_mode: missing files, identity/hash mismatch or unverified authority prevents acceptance and source activation
inbox_pointer: entities/koordinator/inbox/KAN__recovery-v17-preparation__KOO.md
registry_record: registry/by-sender/kancelar.jsonl
status: dispatched
receipt: null

Пакет readback 8/8 PASS, SHA-256 7/7 PASS. Новый полный источник имеет candidate/inactive статус. Действующий v1.6 и active Sources не изменены.
project_time: omitted
