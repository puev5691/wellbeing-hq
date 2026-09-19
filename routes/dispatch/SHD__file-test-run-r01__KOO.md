# Dispatch: SHD → KOO

recipient: koordinator
exchange_gate: v1
sender: shardovik
artifact: `entities/shardovik/outbox/SHD__file-test-run-r01__KOO-KOD.md`
artifact_commit: `e234c95811a421d525998c180ef8840ea54d3962`
artifact_blob: `e14214257bc91153727ea7aecc5749cd8de213da`
source_task: `entities/koordinator/outbox/KOO__file-test-run-r01__SHD.md`
source_task_commit: `62defaa0a38ede6e46fbbee47d2137aa572a55b9`
terminal_result: `PASS_SHD_FILE_SERVICE_EXACT_TEST_RUN_R01`
failure_mode: if artifact/inbox pointer is unavailable or immutable identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted

inbox_pointer: `entities/koordinator/inbox/SHD__file-test-run-r01__KOO-KOD.md`
inbox_pointer_commit: `e0845f157e4f7c58e3ff5711ddab4af61d5b2473`
inbox_pointer_blob: `48ed21900b0ab105e8c4bbe35466a17be0ef1ecd`
required_action: receipt/acceptance or next bounded routing
