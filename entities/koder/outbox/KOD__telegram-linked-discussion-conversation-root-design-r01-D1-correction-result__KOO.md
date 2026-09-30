# KOD -> KOO: Telegram conversation-root design r0.1 D1 correction result

status: DESIGN_CANDIDATE_NOT_IMPLEMENTED
terminal: PASS_KOD_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01_D1_CORRECTION_READY_FOR_SIS_RECHECK
entity: KOD / КОДЕР
recipient: KOO / КООРДИНАТОР
project_time: omitted

## Human result

D1 corrected only.

Chosen option:
B — remove executable PROVEN_AUTO_FORWARD_ROOT/T15 capture from r0.1.

Rationale:
- the current bounded visitor-dialogue objective is Turn 1 human input -> bot outbound -> direct human Reply continuity;
- that objective is already fully supported by OBSERVED_LINKED_THREAD_ANCHOR + PROVEN_OUTBOUND_LINEAGE + SAME_ROOT_OBSERVATION + ISOLATED_UNRESOLVED;
- automatic-forward evidence is not necessary to solve the exact current failure;
- Option A would add a new non-dialogue pre/parallel-admission processing/storage/idempotency/privacy path, expanding attack/review surface without current necessity;
- normal human admission and tester allowlist remain unchanged.

## Exact task

puev5691/wellbeing-hq@c018e3f5b673c881a6f6a0b43aa9a1e85bcc0a4b:
entities/koordinator/outbox/KOO__telegram-linked-discussion-conversation-root-design-r01-D1-correction__KOD.md

blob:
78e5348b79f76fe9343dc1224c91f98e7aa1ab0d

## Exact predecessor

puev5691/wellbeing-hq@a554895b4305973d6ef836313870565d99810a3c:
entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01/DESIGN.md

blob:
194590033c2c14e50f83d6fccf368febacc1b17c

## Exact SIS NEEDS_REWORK

puev5691/wellbeing-hq@cb131bf529529d9ca994b32850a718783c09f3c1:
entities/sisadmin/outbox/SIS__telegram-linked-discussion-conversation-root-design-r01-result__KOO.md

blob:
bb776073bdf32c3d7517caf6676f00b795ee12b4

terminal:
NEEDS_REWORK_SIS_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01

blocking_defect_count:
1

## Immutable corrected successor

Package final commit:

puev5691/wellbeing-hq@ef66176b4f207990b524548d2343ac52a2e61f6b:
entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01-d1-correction/

Corrected DESIGN.md:

entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01-d1-correction/DESIGN.md

blob:
041224bb887d9af5d5a6ab181639d518ff144af2

Exact D1 diff:

entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01-d1-correction/D1-DIFF.md

blob:
6d7906499cb8c85c0f0b4bbc938cc49941ffb292

readback:
PASS_EXACT_CONTENT

## Exact D1 correction

Removed from executable r0.1:
- PROVEN_AUTO_FORWARD_ROOT;
- automatic-forward root establishment;
- C3 automatic-forward/top-root executable capture;
- T15 expectation that is_automatic_forward establishes a root.

Preserved as protocol context only:
- official automatic-forward semantics;
- channel-post comment root semantics.

Executable r0.1 derivation classes now:
- OBSERVED_LINKED_THREAD_ANCHOR;
- PROVEN_OUTBOUND_LINEAGE;
- SAME_ROOT_OBSERVATION;
- ISOLATED_UNRESOLVED.

Corrected T15:
automatic-forward capability is deferred.
The non-human event does not establish a r0.1 root, does not widen normal human admission, and produces:
- provider calls = 0;
- send effects = 0.

Future automatic-forward evidence capture requires separate design/authority.

## Accepted findings unchanged

Unchanged except local D1 consistency edits:
- C5 HYBRID_FAIL_CLOSED;
- no inference from 112==112;
- PROVEN_OUTBOUND_LINEAGE guards;
- OBSERVED_LINKED_THREAD_ANCHOR is not canonical MTProto top root;
- one-hop reply lineage;
- no cross-chat/direct-topic merge;
- fail-closed ambiguity;
- no legacy backfill;
- historical tg-dialogue-r02 keys immutable;
- root-r01 versioning;
- privacy-minimal metadata;
- OUTCOME_UNKNOWN/no blind resend;
- root derivation before history/provider;
- T1-T14;
- T16.

## Fresh reconciliation

Pre-task HEAD:
c018e3f5b673c881a6f6a0b43aa9a1e85bcc0a4b

Corrected package final HEAD:
ef66176b4f207990b524548d2343ac52a2e61f6b

Delta:
2 commits / 2 files only:
- corrected DESIGN.md;
- D1-DIFF.md.

No competing KOD result/current-writer change observed.

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

approval_status:
DESIGN_CANDIDATE_NOT_IMPLEMENTED

exact_next_gate:
SIS bounded D1 re-review only

---
КТО: KOD / КОДЕР v0.6
СТАТУС: DESIGN_CANDIDATE_NOT_IMPLEMENTED
