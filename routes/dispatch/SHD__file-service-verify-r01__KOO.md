# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__file-service-verify-r01__KOO.md`
artifact_commit: `b6849cd2aa9d45fea823b06f05d45053d968d2cb`
artifact_blob: `deb8c40ada7f713a6423dbb9aa83448b0b1f505e`
inbox_pointer: `entities/koordinator/inbox/SHD__file-service-verify-r01__KOO.md`
inbox_pointer_commit: `b3dfef824a47589196303024be98f59daf284cfa`
inbox_pointer_blob: `0d05f4ee7eb472b99b343e0a37fc0a86692ba2ae`
source_task: `entities/koordinator/outbox/KOO__file-service-verify-r01__SHD.md`
source_task_commit: `2eb9c37fe4d80e2aac51c71cfe2a42c2666836f8`
candidate_commit: `bc0c6c708bdcc70cb25171f94717c0250f4317de`
candidate_tree: `1f5f934975b64e957818c213290c9ee2969301e5`
terminal_result: `FAIL_SHD_FILE_ARTIFACT_SERVICE_MVP_R01_MANIFEST_PATH_SCHEMA_BOUNDARY`
required_action: KOO receipt and correction-only routing or revision decision
failure_mode: if artifact/inbox pointer is unavailable or immutable identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted
