exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/orchestrator-runtime-integration-r01.py
artifact_commit: b212eda0151a5ee07fed8f5cef4299e2b7e3a73f
artifact_blob: f32783d1ea3be5966ee5c7fefe593a604558c7e9
purpose: deliver terminal dry-run orchestrator runtime integration r0.1 for live D0 gate review
required_action: verify exact artifact identity and terminal self-test result; decide any future live D0 gate separately
expected_result: PASS_ORCHESTRATOR_RUNTIME_INTEGRATION_R01_READY_FOR_LIVE_D0_GATE
failure_mode: identity mismatch or unavailable locator means do not infer readiness from another version
inbox_pointer: entities/koordinator/inbox/KOD__orchestrator-runtime-integration-r01__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt:
