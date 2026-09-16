# KOO → KOD: apply benchmark authority resolution r0.1

status: `READY_FOR_KOD_EXECUTION`
EXECUTION_MODE: `FAST_PATH`
RECOMMENDED_REASONING: `MEDIUM`
production: `no`
live_provider_calls: `no`
credentials: `no`

## Authority decision

OPERATOR explicitly selected:
- authoritative benchmark implementation: `aa36f7a99105d367b6b2cc5038952c428301c7a0`;
- non-authoritative reference: `2393c42e5d9ee3887b3d95666463def217de033c`;
- reference A may be studied later only for possible WBN integration ideas and must not re-enter current OpenAI authoritative path.

Authority record:
`entities/koordinator/outbox/KOO__openai-benchmark-r01-authority-resolution__OPERATOR.md`
commit `d8b133b1c2d5ba958da0fe119af153262bb89860`.

## Purpose

Apply this authority decision to the active benchmark lineage without rewriting immutable artifacts.

Required:
1. verify exact selected package at commit `aa36f7a99105d367b6b2cc5038952c428301c7a0`;
2. publish one authoritative KOD result/locator bound to selected package;
3. mark A commit `2393c42e5d9ee3887b3d95666463def217de033c` as non-authoritative reference only;
4. close `BLOCKED_CONCURRENT_KOD_SAME_TASK_MUTATION` by explicit operator authority, not by overwrite;
5. preserve A for future bounded WBN study only;
6. do not modify benchmark implementation bytes unless exact inconsistency is found.

## FAST_PATH

Target <=12 tool calls and <=8 GitHub reads.
One initial preflight, one short prewrite reconciliation.
Stop after authority/routing state is unambiguous.

## Hard boundaries

No live provider calls.
No API keys.
No billing changes.
No production deploy.
No TERA2/WBN execution.
No silent replacement of immutable history.

## Expected result

`PASS_BENCHMARK_AUTHORITY_APPLIED_R01`

or exact `BLOCKED_* / FAIL_*`.

Return to KOO through Exchange Gate.
