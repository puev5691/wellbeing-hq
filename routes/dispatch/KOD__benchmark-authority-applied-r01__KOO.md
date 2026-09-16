exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__benchmark-authority-applied-r01__KOO.md
artifact_commit: f2ffcc122a937313eca982dcc8b3e78716bb7717
purpose: apply explicit OPERATOR authority to concurrent OpenAI benchmark lineage without rewriting immutable history
required_action: review authoritative benchmark lineage and use B only for current OpenAI path
expected_result: PASS_BENCHMARK_AUTHORITY_APPLIED_R01
failure_mode: if selected B identity or authority record is unavailable, stop and return exact blocker
inbox_pointer: entities/koordinator/inbox/KOD__benchmark-authority-applied-r01__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt:
