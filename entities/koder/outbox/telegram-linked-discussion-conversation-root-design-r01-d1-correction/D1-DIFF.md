# D1 exact correction diff — Telegram linked-discussion conversation-root design r0.1

status: DESIGN_CANDIDATE_NOT_IMPLEMENTED
correction_scope: D1_ONLY
chosen_option: B_REMOVE_EXECUTABLE_AUTO_FORWARD_ROOT_CAPTURE
project_time: omitted

## Exact predecessor

puev5691/wellbeing-hq@a554895b4305973d6ef836313870565d99810a3c:
entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01/DESIGN.md

blob:
194590033c2c14e50f83d6fccf368febacc1b17c

## Exact SIS blocker

puev5691/wellbeing-hq@cb131bf529529d9ca994b32850a718783c09f3c1:
entities/sisadmin/outbox/SIS__telegram-linked-discussion-conversation-root-design-r01-result__KOO.md

blob:
bb776073bdf32c3d7517caf6676f00b795ee12b4

terminal:
NEEDS_REWORK_SIS_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01

blocking_defect_count:
1

## Corrected successor

puev5691/wellbeing-hq@050dcd179b88abf5ccfa7189623bfab4d6abbd93:
entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01-d1-correction/DESIGN.md

blob:
041224bb887d9af5d5a6ab181639d518ff144af2

## Exact D1 semantic diff

### D1-1 Selection

OLD:
R1 `PROVEN_AUTO_FORWARD_ROOT` was executable r0.1 root derivation.

NEW:
Option B selected.
Automatic-forward root capture is not executable in r0.1.
Official automatic-forward semantics remain protocol context only.
Any future automatic-forward evidence capture requires separate design and authority.

Reason:
the current bounded visitor-dialogue objective is solved without auto-forward capture by initial observed root establishment plus direct reply-to-known-outbound inheritance. Adding a separate non-dialogue evidence path would increase admission/storage/replay/privacy surface without being necessary for the exact current failure.

### D1-2 Human admission boundary

OLD:
resolver ordering after current human admission coexisted with executable automatic-forward R1, making R1 unreachable under the current admission contract.

NEW:
normal human admission is unchanged.
No pre/parallel automatic-forward evidence path is introduced.
No automatic-forward event becomes a tester turn.
No allowlist/admission widening occurs.

### D1-3 Executable derivation classes

OLD:
- PROVEN_AUTO_FORWARD_ROOT
- OBSERVED_LINKED_THREAD_ANCHOR
- PROVEN_OUTBOUND_LINEAGE
- SAME_ROOT_OBSERVATION
- ISOLATED_UNRESOLVED

NEW executable r0.1:
- OBSERVED_LINKED_THREAD_ANCHOR
- PROVEN_OUTBOUND_LINEAGE
- SAME_ROOT_OBSERVATION
- ISOLATED_UNRESOLVED

### D1-4 C5 composition

OLD:
C5 included canonical/proven top-root evidence as an executable input.

NEW:
C5 executable r0.1 consists of:
- established mode-scoped project root from bounded thread observation;
- exact reply-to-known-outbound inheritance;
- fail-closed isolation on ambiguity.

Canonical linked-discussion top-root/automatic-forward semantics remain protocol context and are not an executable capture path in r0.1.

### D1-5 D1 / Bot API evidence boundary

OLD:
`is_automatic_forward` was listed among bounded evidence available to the executable root resolver.

NEW:
`is_automatic_forward` remains documented protocol context only for r0.1.
No automatic-forward evidence is required for current root resolution.

### D1-6 C3 applicability

OLD:
C3 was accepted for use when exact top/root evidence was available.

NEW:
C3 is protocol context only in executable r0.1.
Automatic-forward/top-root capture is deferred to separate future design/authority.

### D1-7 PROVEN conditions

OLD:
the automatic-forwarded linked-discussion root itself could establish a PROVEN root.

NEW:
that executable PROVEN condition is removed.
PROVEN continuity for the current bounded visitor-dialogue objective comes from unique same-chat/same-mode prior committed outbound lineage or exact existing root-anchor evidence.

### D1-8 Metadata boundary

OLD:
`PROVEN_AUTO_FORWARD_ROOT` was part of the executable `root_derivation_class` enum.

NEW:
remove `PROVEN_AUTO_FORWARD_ROOT` from executable r0.1 derivation classes.

All other proposed privacy-minimal scalar metadata remains unchanged, including `inbound_is_automatic_forward` only as optional bounded protocol/diagnostic context if a later implementation task independently justifies retaining it. It is not required to derive a root in r0.1.

No raw Update/full Message/user identities are introduced.

### D1-9 Different-comment-root fail-closed wording

OLD:
a known auto-forward/root anchor or prior root mismatch caused separation.

NEW:
a proven prior root mismatch causes separation.
Executable r0.1 does not consume automatic-forward evidence.

### D1-10 T15

OLD:
T15 Automatic-forward root:
`is_automatic_forward=true` established `PROVEN_AUTO_FORWARD_ROOT`.

NEW:
T15 Automatic-forward capability is deferred.

Expected:
- automatic-forward event is not used to establish a r0.1 root;
- normal human admission is not widened;
- provider calls = 0;
- send effects = 0;
- future capture requires separate design/authority.

### D1-11 Ordering

Preserved:
root derivation for admitted human turns occurs before history/provider selection.

Correction:
there is no separate pre-admission automatic-forward observation path in r0.1.

## Explicitly unchanged accepted findings

The following predecessor findings remain unchanged except the local consistency edits above:

- C5 HYBRID_FAIL_CLOSED selected;
- no semantic inference from numeric coincidence `112==112`;
- PROVEN_OUTBOUND_LINEAGE unique same-chat/same-mode committed-effect guards;
- OBSERVED_LINKED_THREAD_ANCHOR is not claimed as canonical MTProto top root;
- one-hop `reply_to_message` bounded lineage;
- no cross-chat/direct-topic merge;
- ambiguity/legacy evidence fail closed;
- historical `tg-dialogue-r02` conversation_key values immutable;
- no synthetic legacy root backfill;
- versioned root-r01 future semantics;
- privacy-minimal scalar metadata;
- send-success plus lineage/root persistence failure => OUTCOME_UNKNOWN / no blind resend;
- root derivation before history/provider;
- T1-T14 unchanged;
- T16 unchanged.

## Boundary

dialogue_mvp.py:
NOT_MODIFIED

DB/schema:
NOT_MODIFIED

install/service start:
NOT_PERFORMED

Telegram/OpenAI calls:
0

config/allowlist/credentials:
NOT_MUTATED

failed live task replay:
NOT_PERFORMED

next_gate:
SIS bounded D1 re-review only

terminal:
PASS_KOD_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01_D1_CORRECTION_READY_FOR_SIS_RECHECK
