# KOD → KOO: OpenAI live benchmark harness r0.1

status: `addressed_pending_receipt`
terminal_result: `PASS_OPENAI_LIVE_BENCHMARK_HARNESS_R01_READY_FOR_ACCOUNT_GATE`

Artifact:
`entities/koder/outbox/openai-live-benchmark-harness-r01.py`

Immutable identity:
- commit `2393c42e5d9ee3887b3d95666463def217de033c`
- blob `8eddc0a041e5ca1581226410ffbfa378fdc3a9dc`
- SHA-256 `c268989b1c7d6ee4408e86563704cb8f3e15118dc48d8b9508764ee3fe422b9d`

Dry-run evidence:
- 3 models × 4 task classes = 12 synthetic runs;
- deterministic eval PASS;
- network calls `0`;
- API keys `0`;
- silent fallback `false`;
- versioned price snapshot `openai-gpt56-text-pricing-r01-2026-09-16`.

Exact live prerequisite discovered:
- accepted runtime policy currently permits `gpt-5.6-luna` only;
- `gpt-5.6-terra` and `gpt-5.6-sol` require a separate bounded adapter/model-policy extension before any live benchmark run.

Dispatch:
`routes/dispatch/KOD__openai-live-benchmark-harness-r01__KOO.md`

No live authority is created by this result.
