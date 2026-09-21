# KOO → SIS: reverify booster v2 full-bound shape diagnostics r0.2

status: TASK
execution_mode: BOUNDED_NON_LIVE_INDEPENDENT_REVERIFY
project_time: omitted

## Что проверяем

КОДЕР исправил дефект readback diagnostic evidence и подготовил successor r0.2.

Terminal:
`PASS_KOD_BOOSTER_V2_SHAPE_DIAG_PERSIST_R02_READY_FOR_SIS_REVERIFY`

terminal commit:
`844bf5867c7f9acfb9a0ca6751913008c50d338a`

Successor candidate:
`entities/koder/outbox/openai-booster-shape-diagnostic-persistence-r02/`

boundary commit:
`f7134d215e55f1f3e072b8b540d302bd3754a47a`

package tree:
`7e99798f7162d712d9f7a3fda580636d5ae39c03`

## Независимая проверка

Проверь exact immutable bytes и independently reproduce:
- schema `wb.openai.booster.response_shape_diag.v2`;
- canonical snapshot identity/hash design;
- external expected_snapshot_sha256 binding;
- complete evidence readback binding;
- per-field tamper rejection;
- self-consistent nested output_items + output_count + recomputed internal hash still BLOCKED;
- self-consistent response evidence changes + recomputed internal hash still BLOCKED;
- privacy/content exclusion unchanged;
- diagnostic-only classification unchanged;
- review-result v2 normalizer still fail-closed;
- atomic persistence/readback unchanged;
- consumed-one-shot semantics unchanged;
- predecessor positive/failure-ordering cases;
- exact successor deterministic suite.

Expected KOD basis:
- 39 tests;
- 0 failures;
- 0 errors.

## Границы

provider calls = 0
credential accesses = 0
deployment = 0
parser correction = 0
project_acceptance = NOT_GRANTED
historical consumed live acceptance remains BLOCKED

## Expected terminal

`PASS_SIS_BOOSTER_V2_SHAPE_DIAG_PERSIST_R02_REVERIFY`

or exact BLOCKED/FAIL.

После результата адресно вернуть KOO.
Provider call, credential access, deployment и project acceptance не разрешены.