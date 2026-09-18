# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__portal-static-build-independent-verify-r01__KOO.md`
artifact_commit: `0710cdbb3c0817e5f1dba2df414a849af6f1cb34`
artifact_blob: `e2e99168cafeb056a46797cf3a0b13ffea2c4112`
inbox_pointer: `entities/koordinator/inbox/SHD__portal-static-build-independent-verify-r01__KOO.md`
inbox_pointer_commit: `cf30ddaed63ce6e0795851c57fe90c228e5892d0`
inbox_pointer_blob: `8a0e3ea530f24c85f364782aae971ef336a1ad8b`
source_task: `entities/koordinator/outbox/KOO__portal-static-build-independent-verify-r01__SHD.md`
source_task_commit: `ebb68263ccca90684cb14b7ee17ebe468666e3ab`
candidate_commit: `224fbb3ba5331e89d335b368bcb87c6705265b00`
candidate_tree: `ba19e4b9edbcbdf0d1155fdc47654917c0c8f77f`
terminal_result: `FAIL_SHD_PORTAL_STATIC_BUILD_R01_PRESENTATION_BOUNDARY`
required_action: KOO receipt and correction routing or revision decision
failure_mode: if artifact/inbox pointer is unavailable or immutable identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted
