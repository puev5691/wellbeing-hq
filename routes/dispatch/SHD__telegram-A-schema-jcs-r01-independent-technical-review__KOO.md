# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__telegram-A-schema-jcs-r01-independent-technical-review__KOO.md`
artifact_commit: `e4a4cef25ec7605e6beddaa554e01d7c558aeb99`
artifact_blob: `6aa923f833a1cbbfc1bf322d144d6556b653ae0e`
inbox_pointer: `entities/koordinator/inbox/SHD__telegram-A-schema-jcs-r01-independent-technical-review__KOO.md`
inbox_pointer_commit: `bda9f601fcab59f15027b0ca913b6aa799ef80ac`
inbox_pointer_blob: `2970c3f7a7bf5bd67a7461ac607ffcea65e7c619`
source_task: `entities/koordinator/outbox/KOO__telegram-A-schema-jcs-r01-shd-independent-technical-review__SHD.md`
source_task_commit: `2fcb9d1b2e0714841d573b1237d088ed3e976f6a`
candidate_commit: `bde5e6caf988b255e52aaa191de41e1f6b354572`
candidate_blob: `a0fa6d972dc26aa009c55318f03347515bbb7982`
terminal_result: `PASS_SHD_TELEGRAM_A_SCHEMA_JCS_R01_WITH_BOUNDARIES`
required_action: KOO receipt, reconciliation and bounded documentary correction/routing decision
failure_mode: if artifact or inbox pointer is unavailable or immutable identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted
