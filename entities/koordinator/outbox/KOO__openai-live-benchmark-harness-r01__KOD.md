# KOO → KOD: OpenAI live benchmark harness r0.1

status: `READY_FOR_KOD_EXECUTION`
EXECUTION_MODE: `FAST_PATH`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
live_provider_calls: `no`
credentials: `no`

## Priority

Top-priority lane:
OpenAI-first coordination infrastructure → first bounded live call → measured routing by latency/cost/quality → Anthropic/Google adapters.

TERA2/WBN remains `PARKED_BACKGROUND`.

## Accepted basis

Use the accepted results already in HQ:
- orchestrator MVP r0.1;
- OpenAI Responses D0 adapter r0.1;
- orchestrator runtime integration r0.1;
- SIS OpenAI D0 runtime/secret gate r0.1.

Do not redesign those boundaries unless an exact incompatibility is demonstrated.

## Purpose

Prepare a minimal benchmark/eval harness that is ready to run after a separately authorized OpenAI live gate.

The harness must support the first practical comparison of current OpenAI model routes used by Project WELLBEING, beginning with:
- `gpt-5.6-luna`;
- `gpt-5.6-terra`;
- `gpt-5.6-sol`.

No live provider call is authorized by this task.

## Required candidate

Materialize a runnable local package that can later execute a small bounded synthetic benchmark set through the accepted orchestrator/runtime path.

Minimum benchmark task classes:
1. routine extraction/classification;
2. concise Russian operator summary;
3. bounded coding/reasoning task;
4. structured JSON output task.

For each run capture only evidence actually returned/observed:
- provider/model;
- task class;
- input/output tokens where available;
- provider request id where available;
- wall/provider latency when observable;
- retries;
- result status;
- estimated cost from a separately versioned price snapshot;
- deterministic quality/eval fields where possible.

The harness must:
- default to `dry_run` / no-network;
- require explicit live authority before network execution;
- never store API keys;
- use synthetic/public benchmark content only;
- keep model/provider switch explicit, never silent;
- allow one-model or multi-model bounded run selection;
- emit compact JSON/Markdown summary suitable for KOO routing decisions.

## FAST_PATH

Target <=12 tool calls and <=8 GitHub reads.
One initial preflight, one short prewrite reconciliation.
Stop after sufficient terminal evidence.

## Hard boundaries

Do not:
- request/read/create API keys;
- make authenticated provider calls;
- mutate billing/account;
- deploy production service;
- send project/private data externally;
- resume TERA2/WBN.

## Expected result

`PASS_OPENAI_LIVE_BENCHMARK_HARNESS_R01_READY_FOR_ACCOUNT_GATE`

or exact `BLOCKED_* / FAIL_*`.

Return result to KOO through current Exchange Gate.

---
КТО: KOO
ДЛЯ ЧЕГО: подготовить измеримый benchmark-контур для первого OpenAI live этапа
СТАТУС: `ready_for_kod_openai_live_benchmark_harness_r01`
