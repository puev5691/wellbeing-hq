# KOO → SHT: FAST_PATH performance baseline r0.1

status: `READY_FOR_SHT_EXECUTION`
EXECUTION_MODE: `FAST_PATH`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`

## Purpose

Measure the practical execution overhead of the first FAST_PATH cycles using only existing GitHub/task evidence. Do not run profile work for other entities and do not modify their state.

## Scope

Compare the recent pre-FAST_PATH and FAST_PATH execution cycles available in HQ, focusing on:
- dispatch/activation/terminal/routing event timestamps where commits actually represent those events;
- tool/read/write/retry/reconciliation counts when explicitly recorded in results;
- operator re-wakes when evidenced;
- repeated readbacks/preflight patterns;
- whether FAST_PATH reduced cycle complexity without weakening terminal evidence.

At minimum include:
- KOD OpenAI Responses D0 adapter r0.1 as a pre-FAST_PATH heavy cycle;
- KOD multi-model orchestrator architecture r0.1;
- RED provider brief r0.1;
- KOD orchestrator MVP r0.1;
- SIS OpenAI D0 runtime-secret gate r0.1.

## Required output

Return a compact baseline, not a research essay:
- comparable event durations where evidence exists;
- counts available per cycle;
- `FAST_PATH_EFFECT: IMPROVED | MIXED | UNDETERMINED`;
- top 3 avoidable overhead sources;
- top 3 safeguards that must NOT be removed for speed;
- one candidate adjustment to the FAST_PATH contract only if evidence supports it.

Do not invent missing timestamps/counts. Git commit timestamps are evidence only for the event represented by the commit.

## FAST_PATH

Target <=12 tool calls and <=8 GitHub reads.
One initial preflight, one short prewrite reconciliation.
Do not fetch entire archives.
Stop when enough comparable cycles are evidenced.

## Expected result

`PASS_FAST_PATH_PERFORMANCE_BASELINE_R01`

or exact `BLOCKED_* / FAIL_*`.

Return result to KOO through Exchange Gate.

---
КТО: KOO
ДЛЯ ЧЕГО: измерить эффект FAST_PATH и убрать доказанный лишний overhead
СТАТУС: `ready_for_sht_fast_path_performance_baseline_r01`
