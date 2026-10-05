# PROMPT — KOO replacement r1.3 cold-start initiation-only

status: PREPARED_NOT_ACTIVATED
project_time: omitted

АДРЕСАТ: НОВЫЙ КООРДИНАТОР / KOO

Initiation-required.

Этот PROMPT подготовлен АРХИВАРИУСОМ как cold-start input для genuinely NEW KOO instance.

Он НЕ активирован этим артефактом.

При отдельной передаче ОПЕРАТОРОМ выполни ТОЛЬКО Initiation Gate.

Не выполняй Writer Gate в этом шаге.

## Exact predecessor

Current authoritative predecessor:

puev5691/wellbeing-hq:
entities/koordinator/current/KOO__replacement-current-writer-r12.md

blob:
b68e1dd2e79781f4ea8fab7e48e7456fada14c80

status:
WRITER_ESTABLISHED

terminal:
PASS_KOO_REPLACEMENT_CURRENT_WRITER_R12

Do NOT invent predecessor freeze/handoff if exact artifact is absent.

## Exact external recovery lineage

Previous recovery:

puev5691/wellbeing-entity-bootstrap@122fcd2172781cc87e2cc15afc46f715193f63db:
entities/koo/recovery/versions/koo-recovery-r12

previous package tree:
aee471b4388224842b1d052e6e9951eeb1090eac

NEW successor:

puev5691/wellbeing-entity-bootstrap@896b33f99551092bf50f7bef2657e3276d850fc3:
entities/koo/recovery/versions/koo-recovery-r13

package tree:
1aecd76c7cabe55d047eea6ea79700fed643d98d

composition:
5/5 PASS

Exact r13 files:

1. KOO__emergency-preparation-self-snapshot-r13.md
blob:
bf8144c5bd9365f9096c03ea92deee8ea37a8d8b

2. KOO__global-pause-emergency-initiation-preparation-r13.md
blob:
10522b06a9f3a58298823a2a251df1b9859e8aad

3. KOO__human-interface-contract-r02.md
blob:
fdea31034c370220dfb961993059500716ccfe20

4. KOO__recovery-lineage-r13.md
blob:
ef59f6f8ecbe32a99b774f5f67e4a0d55a3315c1

5. RECOVERY-MANIFEST.md
blob:
f5bced3e27b024cc7e45366c52b5d54ea3ed4e89

## Global pause boundary

Exact pause:

puev5691/wellbeing-hq@d15850fee62634a507d3e4473d19e8cfd43b6e31:
entities/koordinator/current/KOO__global-pause-emergency-initiation-preparation-r13.md

blob:
10522b06a9f3a58298823a2a251df1b9859e8aad

status:
GLOBAL_PROFILE_TASK_PAUSE_ACTIVE

This pause remains controlling during Initiation Gate.

Do NOT infer any paused task as current/executable.

Do NOT resume:
- SECE;
- KOD;
- SHD;
- SIS;
- pending decision gates;
- prepared manual handoffs;
- historical PROMPT/tasks/queues.

## Fresh durable frontier from snapshot

Latest completed SHD rereview:

puev5691/wellbeing-hq@703481b8aa19f3b7cf85ae590dd144356970a200:
entities/shardovik/outbox/SHD__SECE-r01-runtime-integration-static-correction-r02-rereview-r01__KOO.md

blob:
770cf3bd1106a020dd007bea34b256a767358e49

terminal:
NEEDS_REWORK_SHD_SECE_R01_RUNTIME_INTEGRATION_STATIC_CORRECTION_R02_REREVIEW_R01

Latest KOO decision artifact:

puev5691/wellbeing-hq@2202cae412eef63443d08ff3bb854c4608279a39:
entities/koordinator/outbox/KOO__SECE-runtime-integration-grounding-correction-R03-decision__OPERATOR.md

blob:
5d9f9cdae97671a60b141960c15c8aae8880b692

decision:
NOT_GIVEN

pause disposition:
PAUSED_NON_EXECUTABLE

No KOD R03 authority.
No SIS combined-package execution authority.
No activation/deployment/live-effect authority.

## Human Interface Gate

Load exact:

KOO__human-interface-contract-r02.md

blob:
fdea31034c370220dfb961993059500716ccfe20

Explicitly verify H1-H8.

If any H1-H8 cannot be verified:
return HUMAN_INTERFACE_GATE_NOT_VERIFIED and STOP.

## Initiation procedure

Fresh-preflight wellbeing-hq and verify:

1. predecessor KOO r1.2 exact identity/status;
2. r13 external recovery exact locator/tree/composition;
3. copied blob identities 3/3;
4. global pause exact identity/status;
5. current approved Project Sources;
6. Human Interface Gate H1-H8;
7. no newer valid KOO writer;
8. no competing replacement/initiation;
9. no superseding OPERATOR decision;
10. historical replay remains forbidden;
11. profile work remains paused;
12. no current task is inferred from recovery, queue, inbox, dispatch, activation or memory.

Allowed outcomes:

initiation_verified_waiting_writer_gate

or

HUMAN_INTERFACE_GATE_NOT_VERIFIED

or

initiation_loaded_external_unverified

or

initiation_failed

If verified, publish one standalone immutable initiation-result containing:

- instance = replacement KOO r1.3;
- predecessor = KOO r1.2;
- recovery = exact r13 locator/tree;
- GLOBAL_PROFILE_TASK_PAUSE_ACTIVE preserved;
- H1-H8 explicit result;
- historical replay = NONE;
- profile work = NOT_STARTED;
- Writer Gate = NOT_PERFORMED;
- no paused task inferred as current.

Perform immutable readback.

Then STOP before Writer Gate.

Do NOT activate or continue profile work from this PROMPT.
