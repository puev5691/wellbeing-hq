# KOO r1.3 — reconcile competing SHT instance-conflict successor gates

status:
WAITING_OPERATOR_DECISION

terminal:
PASS_KOO_R13_SHT_INSTANCE_CONFLICT_SUCCESSOR_RECONCILED_TO_BOUND_A2_GATE

project_time:
omitted

## Competing KOO successor proposals

Proposal A:

puev5691/wellbeing-hq@e73d59ce0f17ca4be459ff01330b8b3554136cc0:
entities/koordinator/current/KOO__SHT-r02-A1-instance-conflict-reconciliation__OPERATOR.md

blob:
c28fd1216ce7f2a0ff2222aa04f49785f61eb103

decision gate:

puev5691/wellbeing-hq@09b884d37b89e5ca0d7b1cf96b00c27a2cc90676:
entities/koordinator/outbox/KOO__SHT-replacement-initiation-r02-A2-bound-decision__OPERATOR.md

Proposal:
new Initiation Gate attempt A2 bound to the exact chat that authored durable conflict result e80dd56...

Proposal B:

puev5691/wellbeing-hq@82c97225f0f5707feeddc112549047b005e1728f:
entities/koordinator/outbox/KOO__SHT-r02-initiation-instance-conflict-reconciliation__OPERATOR.md

blob:
0e5aab83e960a99a9c5f5a575c0a9cec2435f9fe

decision gate:

puev5691/wellbeing-hq@bbfde41e1f32feb18e679e4badeccac0eb3545a1:
entities/koordinator/outbox/KOO__SHT-replacement-instance-binding-R03-decision__OPERATOR.md

Proposal:
introduce a new instance-binding handshake before any successor Initiation Gate.

## Shared facts

Both proposals agree:

- A1 must not be replayed or resumed;
- A1 processing-owner is UNKNOWN_CONFLICT;
- no last-write-wins/first-write-wins selection is allowed;
- recovery r02 remains usable and READY_FOR_REPLACEMENT_INITIATION_HANDOFF;
- predecessor SHT writer remains CURRENT_WRITER;
- Writer Gate is not authorized;
- profile continuation remains PAUSED_BY_OPERATOR;
- D1D2 is COMPLETED_PASS;
- narrow rereview is NOT_STARTED / NOT_AUTHORIZED;
- historical replay is FORBIDDEN.

## Governing manual activation boundary

The active project conveyor uses OPERATOR manual transfer to a concrete Entity-chat when exact automatic chat resume is unavailable.

The exact chat that authored:

puev5691/wellbeing-hq@e80dd56a6e92284ae875540dcb062114b9837489:
entities/shtabist/outbox/SHT__replacement-initiation-gate-r02-result__KOO.md

blob:
144a4e549ee84772e55af6b6b958de313f247abe

is a known concrete target to the OPERATOR because that exact result was returned from that chat.

The artifact itself does not establish writer authority.
It is sufficient as an immutable binding anchor for a new attempt only when the OPERATOR manually transfers the successor PROMPT back to that exact same chat.

Any other chat receiving that PROMPT must STOP.

## Minimality / authority reconciliation

Proposal A uses:
- existing manual task-conveyor semantics;
- an existing durable instance-specific result anchor;
- a fresh attempt ID;
- a fresh PROCESSING_STARTED path;
- fresh currentness checks.

Proposal B introduces:
- a new challenge/claim handshake protocol;
- a new pre-initiation state machine not required by active Project Sources for this case.

Because Proposal A can resolve the exact conflict using existing approved process boundaries, Proposal B is unnecessary additional governance/process machinery.

No safety property requires inventing the handshake before using the already-addressable result-authoring chat.

## Dispositions

e73d59ce0f17ca4be459ff01330b8b3554136cc0:
CONTROLLING_RECONCILIATION_BASIS

09b884d37b89e5ca0d7b1cf96b00c27a2cc90676:
CURRENT_EXACT_OPERATOR_DECISION_GATE

82c97225f0f5707feeddc112549047b005e1728f:
COMPATIBLE_CONSERVATIVE_ANALYSIS_BUT_NON_CONTROLLING

bbfde41e1f32feb18e679e4badeccac0eb3545a1:
NON_CONTROLLING_OVER_ENGINEERED_SUCCESSOR_GATE

This resolution is evidence/minimality based, not last-write-wins.

## Current exact next decision

AUTHORIZE_SHT_REPLACEMENT_INITIATION_GATE_R02_A2_BOUND_TO_E80DD56 = YES

If approved:
- KOO may materialize exactly one A2 authority/registry/frontier/PROMPT;
- recipient is only the exact same SHT chat that authored e80dd56...;
- A2 uses a fresh PROCESSING_STARTED path;
- recovery remains r02;
- Writer Gate remains separate;
- profile work remains paused.

STOP at OPERATOR decision.
