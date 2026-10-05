# KOO r1.3 -> OPERATOR: SECE sandbox gate design D1+D2 correction R02

status:
WAITING_OPERATOR_DECISION

project_time:
omitted

## Exact reconciliation basis

puev5691/wellbeing-hq@d81dcab206a805f9aae6df82fadedc629e2c7910:
entities/koordinator/outbox/KOO__post-SHD-sandbox-design-review-R01-D1D2-reconciliation__OPERATOR.md

blob:
ffefe629d9417e9ddb438042db0aa411187be1dd

terminal:
PASS_KOO_R13_SECE_SANDBOX_DESIGN_R01_REVIEW_RECONCILED_TO_D1_D2_CORRECTION_GATE

## Exact SHD finding

puev5691/wellbeing-hq@2625783e24ded82db905f3abe52f982952f4515c:
entities/shardovik/outbox/SHD__SECE-r01-sandbox-gate-design-r01-review-r01__KOO.md

blob:
4ed270080598fbca66c74551a40a37d0b984ef51

terminal:
NEEDS_REWORK_SHD_SECE_R01_SANDBOX_GATE_DESIGN_R01_REVIEW_R01

## Proposed owner

SHT / ШТАБИСТ current writer

entities/shtabist/current/SHT__current-instance-current-writer-r01.md

blob:
a019c21cffeb99bb7c387b8fa95a4629137dc6da

status:
CURRENT_WRITER

## Proposed NEW attempt

SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_A1

scope:
DESIGN_CORRECTION_D1_D2_ONLY

## Correction D1

Close only race-safe path confinement/object-identity defect.

Required corrected design must define:
- exact basename-only or equivalently closed relative-path grammar;
- rejection of absolute/empty/./../separator/alternate escape forms;
- anchored verified sandbox-root directory object identity;
- creation relative to that anchored root;
- exclusive + no-follow or platform-equivalent race-safe semantics;
- no mutable-parent re-resolution after admission;
- protection from root/parent substitution between check and create;
- created-object identity obtained from the actual created/open object;
- regular-file/non-symlink proof tied to that object;
- object identity carried into stat/readback/hash/outcome/cleanup evidence;
- hardlink/replacement-race handling where supported;
- inability to prove confinement => NOT_EXECUTED/BLOCKED.

## Correction D2

Bind rollback/cleanup to corrected D1 resource identities.

Before file removal require:
- anchored root/parent identity revalidation;
- exact leaf identity match to evidenced created object;
- regular-file/non-symlink state;
- attempt ownership;
- no unresolved effect/outcome;
- mismatch/ambiguity => no destructive cleanup.

Before directory removal require:
- exact directory identity/ownership;
- expected parent identity;
- empty proof;
- no recursive fallback.

After cleanup require:
- absence via same anchored identity boundary;
- unchanged parent/root identity.

Ambiguity:
no destructive retry; preserve UNKNOWN/UNRESOLVED.

## Preserve closed areas

Do not reopen except direct D1/D2 plumbing:
- environment class;
- UNKNOWN_LATER_GATE target;
- authority separation;
- task/currentness;
- writer/Recovery;
- PRE_EFFECT_ADMISSION;
- second invocation check;
- outcome classes;
- UNRESOLVED anti-replay;
- G5 boundary;
- G6 boundary.

G4 authority-shape may only gain fields needed to bind the corrected confinement/resource-identity profile/version.

## Status boundary

Successor remains:

DESIGN_ONLY
NOT_IMPLEMENTED
NOT_ACTIVE

## Not authorized

- KOD implementation;
- real adapter implementation;
- target selection/mutation;
- G4 execution authority;
- G4 sandbox execution;
- G5 review;
- G6 authority;
- activation;
- deployment;
- production/live effect;
- host/service/storage mutation;
- credentials;
- Project Source/canon mutation;
- role/Recovery/current-writer mutation;
- automatic downstream continuation.

## Exact OPERATOR decision

AUTHORIZE_SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02 = YES

If approved, KOO may materialize exactly one NEW bounded SHT design correction task for:

SHT_SECE_R01_SANDBOX_GATE_DESIGN_D1D2_CORRECTION_R02_A1

STOP at OPERATOR decision gate.
