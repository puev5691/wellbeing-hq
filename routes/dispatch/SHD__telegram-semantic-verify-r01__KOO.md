# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__telegram-semantic-verify-r01__KOO.md`
artifact_commit: `756a0d20791d3fa224d6cb8492df41e9dff3a5d8`
artifact_blob: `fba8f36de2c4390e6978664a81118a3ab2f8f6d9`
inbox_pointer: `entities/koordinator/inbox/SHD__telegram-semantic-verify-r01__KOO.md`
inbox_pointer_commit: `0cc71a35a8ca03e3058149bda85cde8fbd7ecea1`
inbox_pointer_blob: `9ad1744c6c386345d3c72da70163a8a10c3c626d`
source_task: `entities/koordinator/outbox/KOO__telegram-semantic-verify-r01__SHD.md`
source_task_commit: `8843c8aa893e904a3aca1e7f11bc002998a84c4e`
candidate_commit: `a9de14997080d753f1676161ac6bb5c19b26bd9d`
terminal_result: `PASS_SHD_TELEGRAM_SEMANTIC_SYNTH_R01`
required_action: KOO receipt/acceptance or next bounded routing
failure_mode: if artifact or inbox pointer is unavailable or immutable identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted
