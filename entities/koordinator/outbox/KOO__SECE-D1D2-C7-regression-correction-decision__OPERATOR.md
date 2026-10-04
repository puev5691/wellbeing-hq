# KOO r1.2 -> OPERATOR: SECE D1+D2 C7 grounding regression correction gate r0.3

status:
WAITING_OPERATOR_DECISION

terminal:
PASS_KOO_R12_SECE_D1D2_C7_GROUNDING_REGRESSION_CORRECTION_DECISION_REQUIRED

project_time:
omitted

## Человеческий смысл

R05 independently executed the exact immutable static D1+D2 successor and established a real candidate FAIL.

Transport, materialization and integrity are no longer blockers.

Exact failing evidence:

NEXT_GATE_RESOLVER_GROUNDING_FIXED=false

correction_tests.c7_grounded_candidate=false

The failure is a regression at the boundary between:
- the previously closed C7 NextGateResolver invariant; and
- the newer D1 typed NEXT_GATE_RULE contract.

The failed package's normal D1 path requires conflict_status and supersession_state in normalized NEXT_GATE_RULE records.

The preserved direct C7 unit test constructs a rule without those newer fields.

The newer resolver rejects missing conflict_status/supersession_state, so the previously valid grounded C7 case produces no candidate.

This reconciliation does NOT decide in advance whether the correct repair is:
- neutral/default normalization for optional fields; or
- updating the direct unit-contract fixture to the now-required typed rule shape.

KOD must establish that from the reviewed contract semantics.

The correction must restore the C7 invariant without weakening D1 conflict/supersession enforcement or making malformed/incomplete rules route.

## Exact R05 FAIL

puev5691/wellbeing-hq@0c88907a72fe79e9777769cad20ca0af49d9e71f:
entities/sisadmin/outbox/SIS__SECE-r01-D1D2-burzh-publicfetch-exec-r05__KOO.md

blob:
9cb40082ac5bbbb7c28510a6188dd398b12da2e9

terminal:
FAIL_SIS_SECE_R01_D1D2_BURZH_PUBLIC_GIT_EXEC_R05

Candidate under test:

puev5691/wellbeing-hq@b32c3bdefa01c036e78a9e4d60fc2a78fd86418c:
entities/koder/outbox/sece-r01-offline-simulator-implementation-static-d1d2-r02/

tree:
7807b3f5d43fe62b344f8ab6f6947aea98e33af7

status:
OFFLINE_SIMULATOR_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED

## Current KOD writer

entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

status:
CURRENT_WRITER_ESTABLISHED

## Required NEW correction successor

Owner:
KOD v0.7

Proposed attempt:
KOD_SECE_D1D2_C7_GROUNDING_REGRESSION_R03_A1

Use the exact R05-failed package above as immutable predecessor.

Create a NEW successor package.
Do not overwrite predecessor bytes.

Scope:
C7/D1 grounding compatibility regression only.

Required outcome:
- exact C7 grounded-candidate invariant PASS;
- NEXT_GATE_RESOLVER_GROUNDING_FIXED=YES;
- NEXT_GATE_RULE_END_TO_END_PIPELINE_FIXED=YES;
- D1 conflict/supersession checks preserved;
- incomplete/malformed rule cannot route merely to make C7 green;
- D2 correction remains PASS;
- all required old/new regression gates PASS;
- all exact package-local workloads exit 0;
- candidate remains NOT_ACTIVATED.

KOD must explicitly state which contract interpretation was selected and why:
A. missing conflict/supersession fields are invalid/malformed and the direct C7 test must use the complete typed rule shape; or
B. those fields are optional and exact reviewed semantics require neutral normalization/defaults.

Do not silently change both code and test until green without this classification.

## Boundaries

No:
- R05 replay;
- SIS/SHD rereview;
- simulator activation/deploy;
- external host/runtime mutation;
- provider/model/API/Telegram;
- credentials;
- Project Source/canon mutation;
- role/recovery/current-writer mutation;
- unrelated SECE redesign.

## Exact decision gate

To authorize only one NEW KOD correction successor:

AUTHORIZE_KOD_SECE_R01_D1D2_C7_GROUNDING_REGRESSION_CORRECTION_R03 = YES

If approved, KOO may materialize one exact KOD v0.7 task with INITIAL_NOT_STARTED execution state.

STOP at OPERATOR decision gate.
