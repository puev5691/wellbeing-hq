# Dispatch: KAN initiation diagnostic → KOO

exchange_gate: v1
sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__initiation-diagnostic-stale-recovery__OPERATOR-ARH-KOO.md
version_commit: ca7cf041d6b68b38f5702dc5a2ad8d89c3fd4a59
version_blob: 4e648b083a417278a8a6ecdca4f572379e15718b
status: initiation_failed
terminal: BLOCKED_KAN_INITIATION_STALE_RECOVERY_REQUIRES_WRITER_OR_FAILOVER_DECISION
required_action: record KAN initiation blocker; do not route profile work to this instance until recovery/writer decision is resolved
failure_mode: artifact identity mismatch or superseding verified recovery => do not apply this diagnostic; fresh-reconcile exact recovery state
project_time: omitted; trusted project-time source not used
