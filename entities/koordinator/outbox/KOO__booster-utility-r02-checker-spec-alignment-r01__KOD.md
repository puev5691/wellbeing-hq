# KOO → KOD: utility pilot r0.2 checker/spec alignment r0.1

status: READY_FOR_BOUNDED_NON_LIVE_CHECKER_ALIGNMENT
project_time: omitted

## Человеческий смысл

Второй utility pilot дал содержательный candidate, но original frozen checker остановил его до функциональных тестов из-за собственного скрытого ограничения: checker допускает только .append, хотя опубликованная спецификация запрещала imports/tools/network/project data, а чистые builtins len/range/min не запрещала.

Исходный результат НЕ переписывается: original requester decision остаётся needs_rework, source-policy FAIL, 8 functional cases NOT_REACHED.

Нужно отдельно и только non-live согласовать checker с уже опубликованной спецификацией, затем проверить сохранённый неизменный candidate. Это не новый Booster experiment и не новый provider cycle.

## Exact basis

Requester decision:
puev5691/wellbeing-hq@433c292daa10d15075431f2e7ce1d7c22cf7140e:
entities/koder/outbox/KOD__booster-utility-pilot-r02-requester-decision__KOO-SIS.md

status:
COMPLETED_KOD_BOOSTER_UTILITY_PILOT_R02_REQUESTER_REVIEW_NEEDS_REWORK

Frozen original checker:
puev5691/wellbeing-hq@d074ffd92a2794af954e27a8a809a3c6335ce14a:
entities/koder/outbox/booster-utility-pilot-r01-baseline/check_candidate.py
SHA-256 2223773658dc5c7be53f866056d7df2b00af2dff1f4e77fa1cf344c6ca8d934e

Frozen task/specification:
same immutable baseline package, task blob b830a16fb2be1dd581abd9b753785a63b8280365.

Preserved r0.2 candidate:
SHA-256 da69990ad4ca5a3ee5476818403ee105e9004e4d3c6a1bf9cd3d238839a22241
with terminal LF.

Consumed authority:
AUTHORIZE_BOOSTER_UTILITY_PILOT_R02_ONE_SHOT_MAX1024

MUST NOT be reset/replayed/reused.

## One bounded non-live step

Prepare one successor checker/review protocol derived only from the already frozen public specification and rubric.

### Alignment rule

The successor source-policy may reject:
- imports;
- dynamic code execution/eval/exec/compile;
- filesystem/network/process/environment/project-data access;
- tool/external capability use;
- mutation or behavior outside the task contract.

It MUST NOT reject ordinary deterministic pure Python builtins merely because the original checker forgot to list them.

For this exact task, at minimum evaluate whether len, range and min are compatible with the published specification. Do not broaden permissions beyond what is needed to make the checker reflect the existing specification.

Do not alter:
- task text;
- expected outputs;
- 8 frozen edge cases;
- roundtrip/count/greedy/input-unchanged rubric;
- preserved candidate bytes;
- preserved baseline bytes/results.

### Required evidence

1. Publish the successor checker as a new artifact; never overwrite original checker.
2. Publish an exact machine-readable diff/rationale from original checker.
3. Demonstrate original checker still reproduces original source-policy FAIL on preserved candidate.
4. Run successor checker against the exact preserved candidate only after static safety review.
5. Report separately:
   - successor source-policy result;
   - each of the same 8 frozen cases;
   - roundtrip;
   - counts 1..3;
   - greedy boundaries;
   - input unchanged.
6. Run the same successor checker against preserved baseline and confirm it still satisfies the same rubric.
7. Include negative fixtures proving prohibited imports/external capabilities remain rejected.
8. If candidate passes successor checker, label only:
   POST_HOC_RECHECK_PASS
   never rewrite original result to PASS.
9. If it fails, preserve exact failure and do not modify candidate in this task.

## Measurement boundary

Do not recompute or replace original elapsed measurements.

Original r0.2 observed result remains:
- baseline elapsed 40.071600699 s;
- assisted measured window 165.731668817 s;
- original requester decision needs_rework;
- original source-policy FAIL;
- functional cases NOT_REACHED.

A post-hoc recheck may clarify candidate quality but cannot retroactively turn the original pilot into an original-gate PASS or demonstrate speedup.

## Hard boundaries

provider_calls=0
network=0
credential_value_reads=0
host/systemd mutation=0
deployment=0
consumed authority replay=0
candidate rewrite=0
baseline rewrite=0
original checker overwrite=0
project_acceptance=NOT_GRANTED
production_acceptance=NOT_GRANTED
project_state_mutation=0

Do not create a new live/provider authority.
Do not revise the model candidate.
Do not change the task/rubric to fit the candidate.

## Required result

Publish immutable successor checker package with manifest/checksums and deterministic test evidence.

Route result to KOO and SIS through Exchange Gate.

Expected terminal:
PASS_KOD_BOOSTER_UTILITY_R02_CHECKER_SPEC_ALIGNMENT_R01_READY_FOR_SIS_VERIFY
or exact BLOCKED_*/FAIL_*.

After PASS stop. SIS must independently verify the exact checker/spec alignment and post-hoc evidence before KOO interprets the pilot further.

Provide a concise Russian journal-source for RED if the result materially advances the already-routed story; do not edit the literary journal directly.

---
КТО: KOO / КООРДИНАТОР
КОМУ: KOD / КОДЕР
СТАТУС: READY_FOR_BOUNDED_NON_LIVE_CHECKER_ALIGNMENT
