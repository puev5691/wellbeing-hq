# KOO r1.3 -> OPERATOR: SECE task-grounding correction R04 gate

status:
WAITING_OPERATOR_DECISION

entity:
KOO / КООРДИНАТОР r1.3

project_time:
omitted

## Человеческий смысл

Independent SHD rereview of exact R03 returned:
- C1 PASS;
- C2 PASS;
- C3 NEEDS_REWORK on one bounded task-grounding defect.

The exact R03 candidate is NOT suitable for SIS combined-package execution.

The next causal step is one new bounded KOD v0.7 correction that makes exact task authority/currentness a mandatory effect-eligibility dependency.

## Exact reconciliation basis

puev5691/wellbeing-hq@6a929cee8c6b7bad24dcacb5bf4b60ac97d49476:
entities/koordinator/outbox/KOO__post-SHD-R03-rereview-R01-reconciliation__OPERATOR.md

blob:
8fa0a5ae13d313b7ec3d9c50805a03257cad0fba

terminal:
PASS_KOO_R13_RECONCILIATION_CURRENT_TASK_GROUNDING_CORRECTION_GATE

## Exact SHD finding

puev5691/wellbeing-hq@8906ef23c2688538c07b1f5fda6ee9c0398ad1a9:
entities/shardovik/outbox/SHD__SECE-r01-runtime-integration-grounding-correction-r03-rereview-r01__KOO.md

blob:
64046c99abb20d4a8e9a62b05a533a62a08aabeb

terminal:
NEEDS_REWORK_SHD_SECE_R01_RUNTIME_INTEGRATION_GROUNDING_CORRECTION_R03_REREVIEW_R01

## Proposed owner

KOD / КОДЕР v0.7

Current writer:
entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

status:
CURRENT_WRITER_ESTABLISHED

## Proposed NEW attempt

KOD_SECE_R01_RUNTIME_INTEGRATION_TASK_GROUNDING_CORRECTION_R04_A1

Scope:
correct only remaining C3-R1 task-eligibility grounding defect.

Required behavior:

1. Add a mandatory exact task eligibility dependency, either:
   A. extend ACTOR_EXECUTION_BINDING grounding, or
   B. introduce separate TASK_EXECUTION_BINDING.

2. Before EffectIntent/admission eligibility, exact task support must prove:
- exact task identity/ref;
- exact task authority basis;
- task currentness=CURRENT;
- supersession=NONE / not superseded;
- VERIFIED;
- conflict NONE;
- exact immutable evidence IDs/versions;
- provenance.

3. Missing/UNKNOWN/conflicting/superseded task support must yield:
NO_EFFECT / no intent / no admission.

4. Exact task evidence IDs/versions must be carried through:
resolution
-> contract / Effective Context
-> EffectIntent
-> PRE_EFFECT_ADMISSION
-> invocation frontier.

5. Task evidence version/currentness/supersession drift after admission must yield:
NOT_EXECUTED.

6. Preserve C1 PASS.

7. Preserve C2 PASS.

8. Do not redesign actor/writer/Recovery grounding except where direct dependency plumbing requires it.

9. Do not modify reviewed baseline core.

## Preserved boundaries

Candidate remains:
NOT_ACTIVATED

This gate does NOT authorize:
- SHD rereview of the future corrected successor;
- SIS combined-package execution;
- runtime/live activation;
- deployment;
- provider/API/Telegram effects;
- host/service/storage mutation;
- Project Source/canon mutation;
- role/recovery/current-writer mutation;
- production authority;
- automatic downstream continuation.

## Required later sequence

After corrected successor:
1. NEW independent static rereview;
2. only if static PASS, separate OPERATOR decision on SIS combined-package execution.

## Exact OPERATOR decision

AUTHORIZE_KOD_SECE_R01_RUNTIME_INTEGRATION_TASK_GROUNDING_CORRECTION_R04 = YES

If approved, KOO may materialize exactly one NEW bounded KOD v0.7 correction task with accepted INITIAL_NOT_STARTED frontier for:

KOD_SECE_R01_RUNTIME_INTEGRATION_TASK_GROUNDING_CORRECTION_R04_A1

STOP at OPERATOR decision gate.
