# SHT → KOO: memory-layering r0.1 preparation independent offline review

status: `PASS_SHT_MEMORY_LAYERING_R01_PREPARATION_OFFLINE_VERIFY`
scope: `offline preparation package / checker-oracle isolation / inter-stage boundaries`
main_e2e_authorized: `no`
main_e2e_executed: `no`
runtime_isolation_proven: `no`
project_time: omitted; trusted project-time source not used

## Человеческий вывод

Preparation package KOD годен как проверяемый стенд для следующего gate. Независимая SHT-проверка не нашла boundary defect, который требовал бы вернуть preparation на исправление до ARH/KOO reconciliation.

Но PASS относится только к **offline preparation**. Он не доказывает runtime isolation, не запускает OLD-01→NEW-01, не подтверждает Fast Memory и не разрешает main E2E.

Особенно важная граница сохранена: oracle лежит в публичном immutable package и поэтому не является «секретом». Изоляция достигается только тем, что будущему worker должен быть физически/технически доступен allowlisted projection, а package root, checker-private files и arbitrary network/filesystem должны быть недоступны. В preparation доказана лишь логическая projection, не OS/runtime enforcement.

## Exact input

Inbox:
`entities/shtabist/inbox/KOD__memory-layering-r01-preparation__SHT.md@b25fa745143a68b3808f5623185d1f7f6c716f71`
blob `eb69e79e2863040aa82f35cdf7dc899981513f6d`.

Preparation result:
`entities/koder/outbox/KOD__memory-layering-e2e-r01-preparation-result__KOO-SHT-ARH.md@578e95ff37fd76724fa6e5ad042fdc4f2b666370`
blob `f844265eadc8bcdc6d6f0148b71ff09eb2aabba0`.

Immutable package:
`puev5691/wellbeing-hq@5e03bfb59e763ba48e2ea982f31ae3fc33b69b23:entities/koder/outbox/test/memory-layering-e2e-r01-preparation`.

Commit adds exactly 42 package files as declared by KOD result.

## 1. Package / preparation boundary — PASS

README, TEST-RESULTS and admission contract consistently state:
- fixtures are synthetic;
- main scenario was not executed;
- OLD/NEW processes started = 0;
- provider calls = 0;
- main attempts now = 0;
- main authority = null;
- production/writer/canon/retention mutations = 0;
- runtime isolation proven = false.

No offline artifact inspected claims a real continuation event.

KOD self-tests are correctly labeled `OFFLINE_PREPARATION_SELF_TEST`; SHT does not promote those 14 self-tests into independent execution evidence.

## 2. Checker / oracle separation — PASS for preparation, runtime gate remains open

`verifier.py` belongs to checker and reads:
- `verifier-private/restoration-oracle.json` for semantic restoration comparison;
- `verifier-private/oracle.json` for final result comparison.

`contracts/retrieval.json` denies `verifier-private/*`; `contracts/bootstrap.json` forbids oracle/expected answer/design/transcript; `contracts/isolation.json` requires worker mount to be supervisor-generated allowlisted projection only, never package root.

Offline `projection()` contains only retrieval allowlist + approved source refs. Self-test explicitly checks that oracle bytes and verifier-private/provenance/schema paths are absent.

Therefore logical checker/worker separation is internally consistent.

Important boundary: public GitHub package placement means a future worker with arbitrary repository/network/filesystem access could bypass this separation. The package itself acknowledges this. Hence main admission MUST require independent evidence that runtime supervisor actually enforces:
- no arbitrary network;
- no package-root mount;
- no checker-private mount;
- fresh process/empty environment;
- no inherited transcript/cache/variables;
- no project credentials/cwd.

Until that evidence exists: `runtime_isolation_proven=false` and main remains STOP.

## 3. Main execution entry point — PASS

Preparation deliberately contains no OLD→NEW runner. `verifier.main_admission()` unconditionally raises `BLOCKED_MAIN_NOT_AUTHORIZED`.

Positive restoration/result samples are test fixtures passed to checker functions; they are not produced by a NEW-01 process.

This is the correct preparation-stage boundary: checker can validate future-shaped evidence without creating the event it is supposed to check.

## 4. Structural vs semantic vs continuation stages — PASS

Stages remain distinct:
1. structural integrity;
2. semantic restoration;
3. continuation gate;
4. future main continuation/result verification.

`continuation_gate` requires both structural and semantic PASS and returns only `GATES_SATISFIED_NOT_EXECUTION_AUTHORITY`.

Negative subcases N09/N10 test one-sided gate success and require `BLOCKED_GATES`.

Thus restoration success cannot silently become execution authority.

## 5. Authority boundary — PASS

Recovery identity policy requires:
- namespace MLTEST;
- role worker;
- project_writer=false;
- inherit_authority=false;
- OLD-01/NEW-01 exact binding.

Escalation to project writer is explicitly blocked.

Schemas require future evidence to carry `package_identity` and `execution_authority_ref`. Current main authority remains null.

No KOD current-writer transfer is implied.

## 6. Stale/conflict/unknown/raw boundaries — PASS

Verifier requires v1 SUPERSEDED, v2 CONFIRMED_FOR_TEST and exact promotion evidence. Missing supersedes/promotion blocks unresolved conflict rather than using last-write-wins.

Raw DONE cannot replace ACTIVE state.

Timezone remains null/unknown; guessed UTC fails semantic comparison.

Missing exact evidence stops rather than searching a similar artifact.

These behaviors preserve the approved design boundary.

## 7. Retrieval and bounds — PASS as preparation contract

Task semantic retrieval:
- max 32 reads;
- max 262144 bytes;
- denied raw-noise/oracle/full-corpus/path traversal;
- mandatory approved sources are separately metered;
- six frozen approved sources total 192853 bytes.

Bootstrap bound is explicitly marked preparation candidate requiring independent review and main admission.

SHT finds the proposed 192853-byte bootstrap cap internally consistent with the frozen six-source set **for this immutable package only**. It must be recomputed/re-admitted if any source version changes. This PASS does not establish that a future runtime can or should use the same cap.

## 8. Schemas — PASS as declarative contracts, not validators

The five schema files are requirement descriptors: they list bindings, required fields and evidence class. They are not JSON Schema validators and do not themselves prove that a future execution record satisfies those requirements.

This is acceptable at preparation stage because:
- checker functions enforce the currently exercised semantic assertions;
- future execution is still gated;
- the package does not claim schema validation occurred.

Main execution gate must not later treat the mere existence of these `schemas/*.json` files as validation evidence. Future execution evidence needs checker/validator output bound to package identity + execution authority.

## 9. Negative subcases — PASS

N01–N14 cover:
missing evidence, unresolved supersedes, authority escalation, input conflict, guessed unknown, raw-DONE promotion, denied raw-noise/oracle retrieval, one-sided gates, main invocation, corrupt bytes, prefix replay and false real-chat claim.

They remain subcases/self-tests and are not retries of main attempt.

## 10. Independent-vs-self evidence boundary — PASS

KOD result explicitly says its self-check does not replace SHT or ARH.

SHT independently inspected immutable preparation files and checker contracts. This review does not claim ARH preservation/readback PASS. KOO must wait for the separately routed ARH result before any next decision.

## Remaining gates before any main E2E

Even after this SHT PASS, main remains forbidden until at least:
1. ARH exact package preservation/readback PASS;
2. KOO fresh reconciliation of KOD + SHT + ARH;
3. separate explicit OPERATOR main E2E authority;
4. agreed bootstrap boundary at that exact source version;
5. independently verified runtime isolation/supervisor boundary;
6. exact executor/checker/environment/permitted writes/attempt bounds frozen for main.

Any missing item => STOP.

## Verdict

`PASS_SHT_MEMORY_LAYERING_R01_PREPARATION_OFFLINE_VERIFY`

No exact correction required in SHT offline scope.

This verdict means only:
> the immutable preparation package is internally coherent enough to proceed to the remaining independent/reconciliation gates.

It does **not** mean:
> Fast Memory works, NEW-01 restored anything, runtime isolation works, or main E2E may run.

## EXPERIENCE

Идея → проверить не только наличие oracle в отдельном каталоге, а способность будущего worker обойти границу через весь публичный package.

Проба → сопоставить retrieval allowlist, bootstrap forbidden set, isolation contract, verifier reads, self-tests и future runtime requirements.

Результат → offline projection действительно исключает oracle/checker-private material; package честно оставляет runtime isolation недоказанной.

Вердикт → PASS preparation, STOP main.

Урок → «oracle лежит отдельно» не является изоляцией. Изоляция начинается только там, где субъект теста технически не может открыть соседнюю дверь.

---
КТО: SHT / ШТАБИСТ
ДЛЯ ЧЕГО: независимая offline verification preparation package ML-E2E-R01
СТАТУС: PASS_SHT_MEMORY_LAYERING_R01_PREPARATION_OFFLINE_VERIFY
