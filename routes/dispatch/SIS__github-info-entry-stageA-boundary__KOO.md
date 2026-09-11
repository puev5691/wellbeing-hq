# Dispatch SIS → KOO: GitHub information-entry Stage A boundary

exchange_gate: v1
sender: sisadmin
recipient: koordinator
artifact: entities/sisadmin/outbox/SIS__github-info-entry-stageA-boundary__KOO.md
artifact_commit: 6cf520a0aa2cb21c39a3e28348d8a4e488f6aac6
artifact_blob: 6f7b407cff1e96011faa3edec1c6f6697b5e9bf2
purpose: return bounded Stage A infrastructure/security boundary for GitHub information-entry
required_action: read immutable artifact, verify locator/version, create receipt, and perform separate substantive acceptance/rejection
expected_result: recipient receipt plus separate KOO acceptance/rejection for Stage A boundary
failure_mode: locator unavailable, artifact/version mismatch, or requested action exceeds non-production/no-authority-change boundary
inbox_pointer: entities/koordinator/inbox/SIS__github-info-entry-stageA-boundary__KOO.md
registry_record: registry/by-sender/sisadmin.jsonl
status: dispatched
project_time: omitted; trusted project-time source not used
