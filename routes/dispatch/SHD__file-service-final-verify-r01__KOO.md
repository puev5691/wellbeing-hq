# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__file-service-final-verify-r01__KOO.md`
artifact_commit: `a95ef7308a7a2e2f86c6e021c7f2a4c2f9438232`
artifact_blob: `41183a24abef7a6eab13f08f55f8fb258c0295d8`
inbox_pointer: `entities/koordinator/inbox/SHD__file-service-final-verify-r01__KOO.md`
inbox_pointer_commit: `97deb0a1b7baba23d0b3615194782ee7a69d0107`
inbox_pointer_blob: `72e53194adfc7c9a09ed4564b65f23d73ebeeada`
source_task: `entities/koordinator/outbox/KOO__file-service-final-verify-r01__SHD.md`
source_task_commit: `ae565534c74b4c8a54bfa55d63f8346c0447355e`
sealed_manifest_commit: `602bc9643af438a111865d6801217fbf7e50821c`
terminal_result: `PASS_SHD_FILE_ARTIFACT_SERVICE_FINAL_R01`
required_action: KOO receipt/acceptance or next bounded routing
failure_mode: if artifact or inbox pointer is unavailable or immutable identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted
