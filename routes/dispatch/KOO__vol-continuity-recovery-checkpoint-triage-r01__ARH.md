# Dispatch: KOO → ARH VOL continuity recovery checkpoint triage

exchange_gate: v1
sender: koordinator
recipient: archivarius
task: entities/koordinator/outbox/KOO__vol-continuity-recovery-checkpoint-triage-r01__ARH.md
task_commit: 9cdee1d76aefb51b6b638568c18a6cc5c96753d0
task_blob: c3a1e667773e78e33c9078f34f3fe7be270e2df3
inbox_pointer: entities/archivarius/inbox/KOO__vol-continuity-recovery-checkpoint-triage-r01__ARH.md
inbox_pointer_commit: 65eed619a8a162077beaf55e8cc8eb3c7ebd134f
inbox_pointer_blob: 03567f74ed923a36bc1752668f71d6ff8144a21d
required_action: ARH independent Resume-First continuity/recovery triage after exact manual activation
status: dispatched_pending_receipt_and_manual_activation
failure_mode: if either exact file identity differs or ARH current-writer/task authority is unverified, stop and return exact BLOCKED
project_time: omitted
