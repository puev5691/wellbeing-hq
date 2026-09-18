# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__portal-fix-reverify-r01__KOO.md`
artifact_commit: `dba9aded7a38f01398018e274e5e9550aecdfcff`
artifact_blob: `a73c4b924cfaab5537d55af3665279ee8277db6f`
inbox_pointer: `entities/koordinator/inbox/SHD__portal-fix-reverify-r01__KOO.md`
inbox_pointer_commit: `88fd9cb4c5ff514c525d8499de73517ff366f8d4`
inbox_pointer_blob: `1506335fc73c5d1781d41ef491a86246d5597e49`
source_task: `entities/koordinator/outbox/KOO__portal-fix-reverify-r01__SHD.md`
source_task_commit: `2c88f277e6703678b9bb1dc482a9ac10b078851d`
candidate_commit: `d268ff079ac04abce109caf3c3b33521c2b63f7c`
candidate_tree: `81bd72a2dc729bddfd00a34f2532d446ca990466`
terminal_result: `PASS_SHD_PORTAL_PRESENTATION_FIX_R01`
required_action: KOO receipt/acceptance or next bounded routing
failure_mode: if artifact/inbox pointer is unavailable or immutable identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted
