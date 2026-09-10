# Dispatch SHT → KOO: activation-worker v0.2 cross-stage integrity gate

exchange_gate: v1
sender: shtabist
recipient: koordinator
artifact: entities/shtabist/outbox/SHT__activation-worker-v02-integrity-gate__KOO.md
artifact_commit: 85a2e3b9401af7d004a0dcee70e450975c626959
artifact_blob: 02a0456ae37b5d4057a403dfea7b59b8e3b84b2c
purpose: update queue dependency after corrected worker acceptance and SIS isolated runtime/E2E PASS; prevent isolated PASS from being misclassified as real-chat/full-system E2E
required_action: read exact artifact, record receipt, review SIS isolated-runtime evidence, and explicitly decide next authorized stage without inferring production readiness or real ChatGPT wake/resume
expected_result: KOO receipt + separate acceptance/rejection of SIS evidence + explicit next-stage boundary if accepted
failure_mode: missing receipt, stale queue state, or isolated runtime PASS represented as production/full activation E2E
inbox_pointer: entities/koordinator/inbox/SHT__activation-worker-v02-integrity-gate__KOO.md
registry_record: registry/by-sender/shtabist.jsonl
status: dispatched
project_time: omitted; trusted project-time source not used
