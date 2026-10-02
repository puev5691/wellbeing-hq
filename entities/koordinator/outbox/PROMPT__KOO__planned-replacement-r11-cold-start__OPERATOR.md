# PROMPT -> NEW KOO application chat: planned replacement cold-start r1.1

АДРЕСАТ: НОВЫЙ КООРДИНАТОР / KOO

Planned replacement / Initiation-required.

ОПЕРАТОР создаёт genuinely NEW KOO chat в приложении вместо выработанного predecessor KOO r1.0.

Выполни ТОЛЬКО Initiation Gate.

Не выполняй Writer Gate в этом шаге.

## Predecessor current writer

puev5691/wellbeing-hq:
entities/koordinator/current/KOO__replacement-current-writer-r10.md

blob:
8416e945418a4a86764edafbbd06682f6c84682b

status:
WRITER_ESTABLISHED

terminal:
PASS_KOO_REPLACEMENT_CURRENT_WRITER_R10

Predecessor disposition:
planned replacement due exhausted/unresponsive application chat.

Do NOT invent predecessor freeze/handoff if exact artifact is absent.

## Exact external recovery lineage

BASE:

puev5691/wellbeing-entity-bootstrap@ab4c7ad12db9760fe825d2a93b6467499e1a09f4:
entities/koo/recovery/versions/koo-recovery-r09

DELTA:

puev5691/wellbeing-entity-bootstrap@e07047dfce0684638e2164d1712dee06ac313cfc:
entities/koo/recovery/versions/koo-recovery-r10

SUCCESSOR:

puev5691/wellbeing-entity-bootstrap@f478b936e4cba58c8a81490463541b6ecd76a4c1:
entities/koo/recovery/versions/koo-recovery-r11

package tree:
26754ce41321085a9593b526b5162160c3ea3147

ARH preservation result:

puev5691/wellbeing-hq@2d211de3b2bce45c5418eeb4d805fef863f49963:
entities/archivarius/outbox/ARH__KOO-planned-replacement-r11-preserved__KOO.md

blob:
c0aa1dbbea93a2418c2af7af19ac78cdd124d3f3

terminal:
PASS_ARH_KOO_PLANNED_REPLACEMENT_R11_EXTERNALLY_PRESERVED

## r1.1 exact package composition

1. KOO__browser-transition-r11-initiation-correction.md
blob:
22a58ed7b940b8a3ffd46492e6dcc11326d4292a

2. KOO__human-interface-contract-r02.md
blob:
fdea31034c370220dfb961993059500716ccfe20

3. KOO__planned-replacement-initiation-draft-r11.md
blob:
8cf487661348a7420c84f26f78d3817c4eb74270

4. KOO__planned-replacement-self-snapshot-r11.md
blob:
0ed912ad6b3be78e3aecf01e2946c8b06d46fdb9

5. RECOVERY-MANIFEST.md
blob:
08a8e6c9640480f69889fc87f48be96900fcda75

Composition/readback:
5/5 PASS

## Approved Project Sources

Load and verify current approved baseline source identities:

project-instructions-core v2.5
blob:
a42f7dca6a7469a54fa2da24aae0da4e549c9d33

entity-roles-short v2.4
blob:
1772339cb74dae8550bfbd2e33401c34a929e911

source-loading-policy v2.2
blob:
69eb657f260a019f76e8e707c880ea88c1dfa0bf

entity-state-preservation-and-recovery-canon v1.6
blob:
233117e1c9509d730e1f5ec532b1cabe3f786609

file-work-canon-universal v2.4
blob:
e9c29d62057f34e4f771d6057a36d9b7f72e74c2

task-conveyor-canon v1.2
blob:
df7896d867eeeffff506319538fedad938856686

Do not treat candidates/drafts as active canon.

## Mandatory Human Interface Gate

Load exact:

entities/koo/recovery/versions/koo-recovery-r11/KOO__human-interface-contract-r02.md

blob:
fdea31034c370220dfb961993059500716ccfe20

Explicitly verify H1-H8.

If any H1-H8 cannot be verified:
return HUMAN_INTERFACE_GATE_NOT_VERIFIED and STOP.

## Browser-transition correction

Load exact correction:

entities/koo/recovery/versions/koo-recovery-r11/KOO__browser-transition-r11-initiation-correction.md

blob:
22a58ed7b940b8a3ffd46492e6dcc11326d4292a

The historical artifact:

entities/koordinator/outbox/KOO__browser-transition-r11-initiation-result__OPERATOR.md

is NOT valid initiation evidence for this NEW application chat.

Its:
writer effect = NONE
task authority effect = NONE
profile work effect = NONE

## Current durable frontier from r1.1

KOD v0.7 current writer:

puev5691/wellbeing-hq@efd030dccc5ba96f61d4a45e1f19705a18fee98a:
entities/koder/current/KOD__replacement-current-writer-v07.md

blob:
5245ba13c892300dd9d7b7e51cf5aa09ae5ecd9e

KOD task reconciliation:

puev5691/wellbeing-hq@37a7a2c17045224fcd6950a3e838350579190e4b:
entities/koordinator/outbox/KOO__KOD-v07-task-reconciliation-continuity-gap-r01__OPERATOR.md

blob:
8afd4bce4621cf73a19df3725cce2cc7c22c5e11

Durable KOD profile state:
WAITING_EXACT_TASK

Possible predecessor KOD chat-only work:
UNKNOWN / NOT_MATERIALIZED
DO_NOT_RECONSTRUCT
DO_NOT_REPLAY

SHT continuity/materialization candidate:

puev5691/wellbeing-hq@53c59a8b9534bf27ed7d842e7edfe2d854cccdef:
entities/shtabist/outbox/SHT__chat-infofield-materialization-gap-r01__KOO.md

blob:
649c52279f858f8618b94460bbb2671477a94871

terminal:
PASS_SHT_CHAT_INFOFIELD_MATERIALIZATION_GAP_R01_CANDIDATE_READY_FOR_REVIEW

status:
CANDIDATE_NOT_ACTIVE

DURABLE_EXECUTION_STATE_R01:
candidate only

Suggested KAN review:
NOT_AUTO_AUTHORIZED

## Initiation procedure

1. Verify exact recovery BASE r09, DELTA r10 and SUCCESSOR r11.
2. Verify r11 package composition 5/5 and immutable identities.
3. Verify predecessor current writer r1.0 exact identity/status.
4. Verify no newer KOO current-writer exists.
5. Verify no competing replacement/initiation/writer attempt supersedes this cold-start.
6. Fresh-preflight wellbeing-hq after r11 preservation.
7. Fresh-reconcile only enough current KOO/KOD/SHT durable state to detect supersession/conflict.
8. Load and pass Human Interface Gate H1-H8.
9. Do NOT replay historical queue/task/PROMPT.
10. Do NOT infer current task from priority, inbox, dispatch, activation record or model memory.
11. Do NOT start KAN review or any other profile work during Initiation Gate.
12. Do NOT mutate Project Sources/canons.
13. Do NOT create current-writer artifact.
14. Do NOT execute Writer Gate.

## Required initiation result

Return exactly one:

initiation_verified_waiting_writer_gate

or

HUMAN_INTERFACE_GATE_NOT_VERIFIED

or

initiation_loaded_external_unverified

or

initiation_failed

If verified, create a standalone immutable initiation-result artifact in KOO outbox containing:

- this exact recovery lineage;
- predecessor writer identity;
- r11 package verification;
- current fresh HEAD/preflight boundary;
- supersession/competing-writer checks;
- H1-H8 results;
- explicit statement:
  Writer Gate = NOT_PERFORMED
- historical PROMPT replay = NONE
- profile work = NOT_STARTED

Return exact result locator/blob to ОПЕРАТОР.

Then STOP before Writer Gate.
