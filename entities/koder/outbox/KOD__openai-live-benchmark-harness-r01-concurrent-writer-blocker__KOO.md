# KOD → KOO: OpenAI live benchmark harness r0.1 concurrent-writer blocker

status: `BLOCKED_CONCURRENT_KOD_SAME_TASK_MUTATION`
production: `no`
live_provider_calls: `no`
api_keys: `no`
billing_changes: `no`
project_private_data_external_send: `no`
tera2_wbn: `PARKED_BACKGROUND`
project_time: omitted; trusted project-time source not used

## Exact task

`entities/koordinator/outbox/KOO__openai-live-benchmark-harness-r01__KOD.md`
commit `5afc12021a213723f5bef8d69713018e4016c73a`
blob `c6f2ba5aea41baf613335be71db8958765b518e1`.

Fresh activation preflight HEAD:
`54734d36d7fa30188c90df25e813d8a95396cad6`.

Current writer boundary verified before profile work:
`entities/koder/current/KOD__replacement-current-writer-v02.md`
blob `23f20f04504c65497c154c099d8090cde11fba83`.

## Verified provider evidence

Current official OpenAI model documentation confirmed all three requested model IDs and standard text-token prices used by the candidate:
- `gpt-5.6-luna`: input `$0.20`, cached input `$0.02`, output `$1.20` per 1M text tokens;
- `gpt-5.6-terra`: input `$2.00`, cached input `$0.20`, output `$12.00`;
- `gpt-5.6-sol`: input `$4.00`, cached input `$0.40`, output `$20.00`.

Official source locators:
- `https://developers.openai.com/api/docs/models/gpt-5.6-luna`
- `https://developers.openai.com/api/docs/models/gpt-5.6-terra`
- `https://developers.openai.com/api/docs/models/gpt-5.6-sol`

Provider evidence itself is not the blocker.

## This execution candidate

A bounded package was generated and locally verified:
`entities/koder/outbox/openai-live-benchmark-harness-r01/`

Package terminal commit:
`aa36f7a99105d367b6b2cc5038952c428301c7a0`

Exact published blobs:
- `benchmark_harness.py` `0b740701ef6bc1367f3273be3ffc98d4a26a5448`, SHA-256 `becf19820c6ef125d89b121f1b1a2242e315462531e64183ae6e5e6218abc944`;
- `price-snapshot-r01.json` `cd149c5e3c8c57c6c7809ba480eb11c28c2dfaa4`, SHA-256 `63d3e85306b584c0a585a58cff21cc656ca1a78332bed0739f5a930bdff2951e`.

Local self-test before publication: `9/9 PASS`, 12 dry-run records, 3 explicit models × 4 required task classes, no live call, no real key use, no silent fallback, live mode default-deny, deterministic eval and compact JSON/Markdown output.

This package is **not declared authoritative or routed as the task result** because a concurrent route appeared before routing could be completed.

## Conflicting concurrent same-task lineage

During the same execution-cycle, a second KOD result for the exact same task appeared in HQ:

Artifact:
`entities/koder/outbox/openai-live-benchmark-harness-r01.py`
commit `2393c42e5d9ee3887b3d95666463def217de033c`
blob `8eddc0a041e5ca1581226410ffbfa378fdc3a9dc`
SHA-256 `c268989b1c7d6ee4408e86563704cb8f3e15118dc48d8b9508764ee3fe422b9d`.

Its artifact declares the same exact task commit/blob and the same current-writer blob and returns `PASS_OPENAI_LIVE_BENCHMARK_HARNESS_R01_READY_FOR_ACCOUNT_GATE`.

It is already routed through:
`routes/dispatch/KOD__openai-live-benchmark-harness-r01__KOO.md`
with KOO locator:
`entities/koordinator/inbox/KOD__openai-live-benchmark-harness-r01__KOO.md`.

The sender registry changed during this execution-cycle:
- prewrite observed blob `86fe3e3da810f234b11447d63271dfc606b7f35c`, without benchmark record;
- later observed blob `2f6c78ebaf2bc57933a47fd27d54ef7698a7a2dd`, containing record `KOD-openai-live-benchmark-harness-r01-001` pointing to the concurrent artifact/dispatch.

Exact receipt:
`routes/receipts/KOD__openai-live-benchmark-harness-r01__KOO.receipt.md`
was not present at blocker evaluation.

## Why execution stops

Two independently materialized KOD artifacts now claim the same exact task/current-writer authority. The existing dispatch path is already bound to one of them. Selecting, overwriting or silently superseding either immutable candidate would be an authority decision not granted to KOD by this task.

Therefore the required terminal state is:
`BLOCKED_CONCURRENT_KOD_SAME_TASK_MUTATION`.

## Minimal resolution

KOO / OPERATOR must explicitly choose which immutable artifact is authoritative for this task, or retire one lineage. After that decision, only the selected artifact should continue through receipt/acceptance/account-gate routing. No further benchmark/profile work is required before that decision.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: зафиксировать same-task concurrent-writer race без самовольного выбора terminal artifact
СТАТУС: `BLOCKED_CONCURRENT_KOD_SAME_TASK_MUTATION`
