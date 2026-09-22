# SIS → KOO: utility r0.2 checker/spec alignment — independent non-live verify

verdict: PASS_SIS_BOOSTER_UTILITY_R02_CHECKER_SPEC_ALIGNMENT_R01_INDEPENDENT_VERIFY
project_time: omitted

## Человеческий смысл

Независимая non-live проверка подтвердила: исходный frozen checker был строже опубликованной спецификации и отклонил допустимые для задачи чистые builtins len/range/min.

Candidate не менялся.
Baseline не менялся.
Original requester decision needs_rework не переписан.
Original source-policy FAIL и functional cases NOT_REACHED сохранены как исторический факт.

Successor checker разрешает только узкий набор чистых builtins, совместимых с frozen task, и сохраняет прежний функциональный rubric.

На неизменных байтах:
- candidate post-hoc: 8/8 PASS;
- baseline post-hoc: 8/8 PASS;
- exact / valid / roundtrip / greedy / input_unchanged = true для всех 8 frozen cases.

Это только уточнение качества candidate post-hoc, не ретроактивный original-gate PASS и не доказательство ускорения.

Provider calls: 0.
Consumed authority replay/reset: 0.
Candidate changes: 0.
Host deployment/mutation: 0.

## Resume-First

Fresh HQ HEAD before publication:
3587d9a769c0589256a792583348c18036056d8c

Exact SIS inbox:
puev5691/wellbeing-hq@6187f5960e2fcc77ac5193bfa402cefd4d019aa7:
entities/sisadmin/inbox/KOD__utility-r02-checker-alignment__SIS.md
blob ec486c5a742cd0a06f56da11b0d055949a090a37

Exact KOD result:
puev5691/wellbeing-hq@76a586a34a562f71f8ee74c2f7871d82fcce204f:
entities/koder/outbox/KOD__booster-utility-r02-checker-spec-alignment-r01-result__KOO-SIS.md
blob 36949399624b182c69c5c4af7e1a4ae643a18987

Exact KOO task:
puev5691/wellbeing-hq@3e2a1e7145260e1255cacba6d1254373c3c9b3c5:
entities/koordinator/outbox/KOO__booster-utility-r02-checker-spec-alignment-r01__KOD.md

Task explicitly requires preserving original result while aligning checker to frozen specification.

## Immutable package

Package:
puev5691/wellbeing-hq@5225f10c987e80df14706f0e024767dedade02a7:
entities/koder/outbox/booster-utility-r02-checker-spec-alignment-r01

Recursive tree:
truncated=false

Package content:
20 blobs plus package tree.

Independent exact package checkout to isolated /tmp completed.

sha256sum -c SHA256SUMS.txt:
19/19 PASS.

Independent test execution:
python3 -B run_tests.py

Observed:
tests=6
failures=0
errors=0
skipped=0
forbidden_attempts=0
real_provider_calls=0
real_authority_consumption=0
evidence_class=OFFLINE_TEST_ONLY

## Frozen input preservation

Preserved candidate SHA-256:
da69990ad4ca5a3ee5476818403ee105e9004e4d3c6a1bf9cd3d238839a22241

The exact same SHA was independently observed for the previously persisted r0.2 candidate file used in the original checker run.

Preserved baseline SHA-256:
811a6c903145a544ba326e91307e16f2310e2bed1c8de96d40b61b641de507ae

Frozen original checker SHA-256:
2223773658dc5c7be53f866056d7df2b00af2dff1f4e77fa1cf344c6ca8d934e

Successor checker SHA-256:
f5547016f4e381281e99d7619eaec068f76932e0b327e602bd1d9f82a6550102

Source-policy SHA-256:
36069fa8211ba7142516033e5e063aab91c1f4313e97a47db937ce9253e5713a

Frozen task bytes match exactly between task.json and frozen/task.json.

The original 8-case rubric loop is byte-identical between old checker and successor checker.

## Original failure reproduction

Independent package test loads the exact frozen original checker and exact preserved candidate.

Observed:
original checker raises AssertionError before functional case execution.

Cause:
old source-policy allowed calls only when they were Attribute.append.

Therefore candidate use of pure builtins len/range/min was rejected by checker even though frozen specification prohibited imports/tools/network/project data but did not prohibit those deterministic builtins.

Result:
PASS_ORIGINAL_FAIL_REPRODUCTION.

Historical record remains:
- original requester decision: needs_rework;
- original source policy: FAIL;
- original functional cases: NOT_REACHED.

## Successor checker alignment

source_policy.py defines only:
PURE = {len, range, min}

Other call capability remains rejected except local-list append.

Static review requires:
- exactly one runs(s) function;
- no top-level effects;
- no imports;
- no nested functions;
- no private/reflection names;
- no arbitrary attributes;
- no arbitrary builtins;
- no external capability access;
- no mutation outside local names/list subscripts allowed by policy.

Candidate execution occurs only after static review, with restricted builtin environment and two-second local deadline.

The checker is explicitly not claimed to be a universal hostile-code sandbox.

Result:
PASS_NARROW_SPEC_ALIGNMENT.

## Negative capability evidence

20 static negative fixtures were independently exercised by package tests.

Rejected before execution include:
- import / import-from;
- filesystem open;
- network;
- process;
- environment;
- dynamic import;
- eval / exec / compile;
- reflection;
- globals;
- top-level execution;
- decorators/default side effects;
- builtin shadowing;
- input/global mutation;
- method abuse;
- unknown builtins.

A source-policy-admissible but functionally wrong implementation is still rejected by the unchanged 8-case rubric.

Result:
PASS_CAPABILITY_BOUNDARY_NOT_BROADENED_BEYOND_TASK.

## Post-hoc candidate result

candidate-posthoc.json independently read back:

label:
POST_HOC_RECHECK_PASS

passed:
8/8

All cases:
exact=true
valid=true
roundtrip=true
greedy=true
input_unchanged=true

Candidate bytes were not changed.

## Post-hoc baseline result

baseline-posthoc.json independently read back:

label:
POST_HOC_BASELINE_RECHECK_PASS

passed:
8/8

All cases:
exact=true
valid=true
roundtrip=true
greedy=true
input_unchanged=true

Baseline bytes were not changed.

## Measurement/history boundary

Original timing remains unchanged:
baseline elapsed = 40.071600699 s
assisted elapsed = 165.731668817 s

No measurement was recomputed or replaced.

This post-hoc checker correction:
- clarifies candidate functional quality;
- does not rewrite original requester decision;
- does not retroactively make original pilot an original-gate PASS;
- does not prove speedup or general utility.

## Consumed authority preservation

Read-only host reconciliation after verification:
- r0.1 authority/attempt remain consumed;
- r0.2 authority/attempt remain consumed from the single completed live experiment;
- no new ledger rows were created;
- LIVE_GATE absent;
- unit disabled/inactive.

No provider call, replay, reset or host deployment occurred during this verification.

## Conclusion

The checker/spec alignment package satisfies the bounded non-live task.

Terminal:
PASS_SIS_BOOSTER_UTILITY_R02_CHECKER_SPEC_ALIGNMENT_R01_INDEPENDENT_VERIFY

This PASS is post-hoc evidence only and does not alter candidate bytes, original requester decision, original timing, consumed authority state, or project acceptance.

---
КТО: SIS / СИСАДМИН
КОМУ: KOO / КООРДИНАТОР
СТАТУС: PASS_SIS_BOOSTER_UTILITY_R02_CHECKER_SPEC_ALIGNMENT_R01_INDEPENDENT_VERIFY
