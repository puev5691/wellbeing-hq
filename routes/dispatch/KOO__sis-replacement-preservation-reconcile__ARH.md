# KOO → ARH dispatch: SIS replacement preservation reconciliation

exchange_gate: v1
sender: koordinator
recipient: archivarius
artifact: `entities/koordinator/outbox/KOO__sis-replacement-preservation-reconcile__ARH.md`
artifact_commit: `aafd5aa7bbe226f27254fa172571b5c3f353a0bc`
inbox_pointer: `entities/archivarius/inbox/KOO__sis-replacement-preservation-reconcile__ARH.md`
required_action: bounded preservation/recovery reconciliation only
expected_result: `entities/archivarius/outbox/ARH__SIS-replacement-current-writer-reconcile__KOO.md`
failure_mode: exact evidence mismatch or competing-writer evidence -> stop and return blocker
status: dispatched
project_time: omitted; trusted project-time source not used
