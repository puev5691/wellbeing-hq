# KOO → OPERATOR: memory-layering E2E r0.1 MAIN authorization decision gate

status: WAITING_OPERATOR_MAIN_E2E_DECISION
project_time: omitted

## Человеческий смысл

Испытательный пакет Fast Memory r0.1 подготовлен и прошёл две независимые preparation-проверки:
- PASS_ARH_MEMORY_LAYERING_E2E_R01_PREPARATION_PRESERVATION
- PASS_SHT_MEMORY_LAYERING_E2E_R01_PREPARATION_VERIFICATION

Это всё ещё не доказывает работающую Fast Memory. Runtime isolation не проверена фактическим запуском. Следующий этап — один bounded synthetic MAIN E2E attempt, в котором runtime isolation должна быть доказана как admission/runtime evidence, а затем проверены restoration и continuation.

## Immutable basis

Design:
puev5691/wellbeing-hq@9887cd2b3ea7ab09ba58dfa50f27a7f5f6718dca:
entities/koder/outbox/KOD__memory-layering-e2e-design-r01__KOO-SHT.md
blob b1db36b9d2f7510ce4a4efe92071d2f97d0df0a0

Preparation package:
puev5691/wellbeing-hq@5e03bfb59e763ba48e2ea982f31ae3fc33b69b23:
entities/koder/outbox/test/memory-layering-e2e-r01-preparation

ARH preservation:
commit c80f578227c864f3c6034eafd2ed410b9738422a
terminal PASS_ARH_MEMORY_LAYERING_E2E_R01_PREPARATION_PRESERVATION

SHT preparation verification:
terminal PASS_SHT_MEMORY_LAYERING_E2E_R01_PREPARATION_VERIFICATION

## Proposed MAIN scope

Executor/supervisor:
KOD v0.5 may execute exactly one synthetic MLTEST main attempt using the immutable package.

Checker:
the pinned deterministic verifier/checker from the immutable package; oracle/checker-private material must be available only to verifier/supervisor side, never NEW-01 worker.

Independent post-result reviewers:
SHT for execution/runtime-boundary verification; ARH for result/evidence preservation/readback. KOD self-verdict does not replace either.

## Admission conditions that MUST be proven before continuation

At runtime create OLD-01 and NEW-01 as separate fresh exec processes/address spaces.

NEW-01 worker must have:
- no inherited transcript;
- no inherited memory/cache;
- no inherited task variables;
- empty/explicitly allowlisted environment;
- no project credentials;
- no project writer authority;
- no project cwd;
- no arbitrary network;
- no package-root/checker-private/oracle mount or locator;
- only allowlisted bootstrap/retrieval capability.

If any isolation property cannot be evidenced before semantic continuation, STOP/BLOCKED. Do not weaken isolation to obtain PASS.

Bootstrap must use the exact pinned six-source set. Source-version change => STOP for fresh admission/recalculation.

Structural integrity PASS and semantic restoration PASS remain separate. Continuation is permitted only after both pass.

## MAIN bounds

main attempts: exactly 1
automatic retries: 0
semantic reads: <=32
semantic payload: <=262144 bytes
computation deadline: 5 seconds
provider calls: 0
arbitrary worker network: 0
production/project writes: 0

Mandatory six-source bootstrap is separately metered and pinned to the preparation package source set; it is not permission for full-corpus loading.

Permitted writes:
only isolated MLTEST runtime/evidence outputs and subsequent KOD result/Exchange Gate/journal-source/experience candidate artifacts. No production recovery/current, writer, canon, retention or real Entity task-state mutation.

## Required MAIN sequence

1. Fresh admission verifies immutable design/package/reviews/authority and runtime isolation.
2. OLD-01 executes only the designed prefix and freezes checkpoint.
3. Recovery/bootstrap is presented to fresh NEW-01 without transcript/oracle/expected result.
4. NEW-01 verifies structural package integrity.
5. NEW-01 performs selective retrieval under exact contract.
6. Independent verifier checks semantic restoration report.
7. Only structural PASS + semantic PASS opens continuation gate.
8. NEW-01 continues same synthetic task from cursor=3 without replaying prefix.
9. Independent verifier checks exact final oracle and continuation ledger.
10. Negative subcases remain separately labelled; they do not replay main.
11. Produce terminal PASS/FAIL/BLOCKED with exact evidence.
12. Stop. No second main attempt.

## Claims explicitly outside scope

Even a full PASS would prove only this bounded synthetic process recovery/continuation scenario.

It would NOT prove:
- exact existing ChatGPT chat resume;
- ChatGPT Work continuity;
- production Entity continuity;
- general Fast Memory effectiveness/performance;
- authority/writer transfer;
- project acceptance.

Any product-side ChatGPT continuity experiment requires a separate future gate.

## Decision token

To authorize exactly one bounded synthetic MAIN attempt under the conditions above:

AUTHORIZE_MEMORY_LAYERING_E2E_R01_MAIN_SYNTHETIC_EXECUTION

This token is single-attempt authority. Once a main attempt starts, no automatic retry or second attempt is authorized.

---
КТО: KOO / КООРДИНАТОР
КОМУ: OPERATOR / ОПЕРАТОР
СТАТУС: WAITING_OPERATOR_MAIN_E2E_DECISION
