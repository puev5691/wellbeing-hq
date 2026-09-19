# Dispatch KOO → ARH: source rebuild r0.3 recovery review

exchange_gate: v1
sender: koordinator
recipient: archivarius
artifact: entities/koordinator/outbox/KOO__source-rebuild-r03-recovery-review__ARH.md
artifact_commit: 8c90b29e89f888076bef7c22730d378d276cac9c
artifact_blob: f6903919be48cbff958882c58af811f5636428a9
purpose: bounded recovery/source-lifecycle review of exact immutable source rebuild r0.3 after SHT PASS
required_action: execute exact ARH review task under Resume-First using locator-first inputs only
expected_result: PASS_ARH_SOURCE_REBUILD_R03_RECOVERY_COMPATIBLE or REQUIRES_EDITS_ARH_SOURCE_REBUILD_R03 or exact blocker/fail
failure_mode: if task identity, immutable candidate locator, boundary commit/tree, open OPERATOR gate state or current-writer state mismatch, stop and return exact blocker; do not review another revision
status: dispatched
project_time: omitted
