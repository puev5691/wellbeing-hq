exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/openai-live-benchmark-harness-r01.py
artifact_commit: 2393c42e5d9ee3887b3d95666463def217de033c
purpose: deliver bounded dry-run OpenAI Luna/Terra/Sol benchmark harness r0.1 ready for account-gate review
required_action: verify exact immutable harness and decide next account/model-policy gate
expected_result: KOO receipt and acceptance/rejection/next-gate decision
failure_mode: if artifact identity or price-source evidence differs, do not infer PASS from another version
inbox_pointer: entities/koordinator/inbox/KOD__openai-live-benchmark-harness-r01__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt:
verdict: PASS_OPENAI_LIVE_BENCHMARK_HARNESS_R01_READY_FOR_ACCOUNT_GATE
artifact_blob: 8eddc0a041e5ca1581226410ffbfa378fdc3a9dc
artifact_sha256: c268989b1c7d6ee4408e86563704cb8f3e15118dc48d8b9508764ee3fe422b9d
price_snapshot_id: openai-gpt56-text-pricing-r01-2026-09-16
price_snapshot_sha256: 65b3fe09fb07bb7e6a9c5fe348de89174e1d257d4da003a21ad6d0b73aafd405
live_provider_calls: 0
api_keys: 0
tera2_wbn: PARKED_BACKGROUND
