# KOO r1.2 -> OPERATOR: SECE runtime-integration grounding correction R03 gate

status:
WAITING_OPERATOR_DECISION

project_time:
omitted

## Human meaning

Independent SHD rereview of corrected R02 returned NEEDS_REWORK only on C1-R and C3-R.

Exact result:

puev5691/wellbeing-hq@703481b8aa19f3b7cf85ae590dd144356970a200:
entities/shardovik/outbox/SHD__SECE-r01-runtime-integration-static-correction-r02-rereview-r01__KOO.md

blob:
770cf3bd1106a020dd007bea34b256a767358e49

terminal:
NEEDS_REWORK_SHD_SECE_R01_RUNTIME_INTEGRATION_STATIC_CORRECTION_R02_REREVIEW_R01

C1_REREVIEW_VERDICT:
NEEDS_REWORK

C2_REREVIEW_VERDICT:
PASS

C3_REREVIEW_VERDICT:
NEEDS_REWORK

REVIEWED_BASELINE_CORE:
UNCHANGED

NON_LIVE_NO_IO_BOUNDARY:
PRESERVED

CANDIDATE_STATUS:
NOT_ACTIVATED

STATIC_PASS_SUFFICIENT_FOR_LATER_SIS_COMBINED_GATE:
NO

## Proposed owner

KOD / КОДЕР v0.7

Current writer blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

## Proposed NEW attempt

KOD_SECE_R01_RUNTIME_INTEGRATION_GROUNDING_CORRECTION_R03_A1

Correct only the new runtime-integration layer.

### C1-R

Carry the authoritative TrustPolicy dependency through the complete effect-sensitive chain.

Required exact dependency data:
- TrustPolicy evidence ID;
- exact immutable locator;
- exact version/blob;
- TrustPolicy binding ID;
- currentness state;
- conflict state.

These must remain bound through:
RUNTIME_EVIDENCE_RESOLUTION
-> contract / Effective Context dependency
-> EffectIntent
-> PRE_EFFECT_ADMISSION
-> invocation evidence frontier.

Any policy evidence version/currentness/conflict change before invocation:
NO_EFFECT and require NEW resolution/revalidation.

### C3-R

Make ACTOR_EXECUTION_BINDING evidence-derived, not merely normalized caller state.

Positive fields must be supported by exact evidence for:
- actor instance / execution mode;
- current_writer_ref/state;
- writer_requirement;
- writer authority where required;
- Recovery state;
- freeze state;
- handoff state;
- replacement state.

Exact evidence IDs/versions must be part of binding identity and carried through:
RUNTIME_EVIDENCE_RESOLUTION
-> contract
-> EffectIntent
-> PRE_EFFECT_ADMISSION
-> invocation frontier.

Missing/conflicting/UNKNOWN support:
NO_EFFECT / ineligible.

### Preserve C2

C2 is PASS.

Do not reopen C2 except for the minimal direct dependency plumbing required to carry the new exact C1-R/C3-R evidence references through the already accepted invocation checks.

## Preserved boundaries

Do not modify reviewed baseline core.

Candidate remains:
NOT_ACTIVATED

No:
- SIS execution;
- runtime/live activation;
- real external effect;
- provider/model/API/Telegram;
- host/service/storage mutation;
- credentials;
- Project Source/canon mutation;
- role/recovery/current-writer mutation;
- deployment;
- sandbox/live/production authority;
- automatic SHD rereview.

## Required later sequence

After corrected R03 successor:
1. separate independent static/offline rereview;
2. only if static PASS, separate OPERATOR authority for SIS combined-package execution of the exact corrected package.

This gate authorizes neither later step.

## Exact OPERATOR decision

AUTHORIZE_KOD_SECE_R01_RUNTIME_INTEGRATION_GROUNDING_CORRECTION_R03 = YES

If approved, KOO may materialize one NEW bounded KOD v0.7 correction-only task with accepted INITIAL_NOT_STARTED frontier before manual transfer.

STOP.
