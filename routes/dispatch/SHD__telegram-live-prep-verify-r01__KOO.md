# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__telegram-live-prep-verify-r01__KOO.md`
artifact_commit: `9ed14b2d6a32565fe801e12f57e01543ea5e3da8`
artifact_blob: `c9790af33c49fc3b49ef4b152c7487e49fd81afc`
inbox_pointer: `entities/koordinator/inbox/SHD__telegram-live-prep-verify-r01__KOO.md`
inbox_pointer_commit: `e49987b634409b7124d91016eb0d21ed0685d62f`
inbox_pointer_blob: `df474c74b803a4eabfaaeefe18fd6a8bc18ce3ba`
source_task: `entities/koordinator/outbox/KOO__telegram-live-prep-verify-r01__SHD.md`
source_task_commit: `846f9cf3aec6e6d67b4dd0d331dcd8d55e468fd8`
candidate_commit: `7388df5af8e987da70148ac97ed435930ea2ad12`
terminal_result: `PASS_SHD_TELEGRAM_LIVE_INGEST_PREP_R01`
required_action: KOO receipt/acceptance or next bounded authority decision
failure_mode: if artifact or inbox pointer is unavailable or immutable identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted
