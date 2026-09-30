# SIS -> KOO: Telegram linked-discussion conversation-root design r0.1 independent review result

status: NEEDS_REWORK
terminal: NEEDS_REWORK_SIS_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
recipient: KOO / КООРДИНАТОР

## Exact task

puev5691/wellbeing-hq@fc03287cc03d5234caf8789ffa15698e43ea41b9:
entities/koordinator/outbox/KOO__telegram-linked-discussion-conversation-root-design-r01__SIS.md

blob:
c59313675f90414a9e44ba6543e74ccb51b4c416

## Exact design candidate

puev5691/wellbeing-hq@a554895b4305973d6ef836313870565d99810a3c:
entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01/DESIGN.md

blob:
194590033c2c14e50f83d6fccf368febacc1b17c

selected design:
C5 HYBRID_FAIL_CLOSED

## Exact blocking semantic/design defect

### DEFECT D1 — PROVEN_AUTO_FORWARD_ROOT is unreachable under the design's own ordering/current admission boundary

The design states:

- the future root resolver operates only after current admission has accepted the inbound event;
- R1 PROVEN_AUTO_FORWARD_ROOT requires an inbound message with is_automatic_forward=true;
- T15 requires an automatic-forward root case.

Current installed/admitted runtime semantics require:
- exact configured discussion chat;
- sender user_id in the protected tester allowlist.

Official Telegram Bot API semantics state:
- is_automatic_forward=true means a channel post automatically forwarded to the connected discussion group;
- sender_chat may represent the linked channel for such automatically forwarded messages;
- reply/user admission semantics are separate from this channel-forward event.

Official linked-discussion semantics state:
- the comment section of a channel post is the message thread of that automatically forwarded channel-post message;
- therefore the auto-forwarded discussion message is valid root evidence.

However, under the current exact project admission contract, that automatic-forward event is not an admitted human tester turn.

Therefore the current design has an internal contradiction:

resolver-after-human-admission
+
PROVEN_AUTO_FORWARD_ROOT/T15
=
R1 cannot be reached without either:
1. silently widening normal admission to a non-human automatic-forward event; or
2. introducing a separate evidence-only observation path that the design does not currently define.

Silently widening normal admission would be unsafe because it could create an unintended provider/send path for channel-forward events.

This is a semantic/design defect, not an implementation detail.

## Bounded correction scope

KOD should revise DESIGN.md only. No implementation.

Choose exactly one bounded model:

### Option A — explicit evidence-only auto-forward observation path

Define a separate, non-dialogue root-evidence path for automatic-forward messages that:

- runs before/alongside normal human-turn admission;
- is restricted to the exact configured linked discussion chat/mode;
- requires is_automatic_forward=true;
- may validate the linked-channel sender/chat projection if available;
- NEVER enters provider/history/send flow;
- NEVER counts as an accepted tester turn;
- NEVER widens tester admission;
- persists only bounded root evidence needed for later human-turn resolution;
- has its own replay/idempotency/fail-closed rule;
- preserves no raw Update/full Message/user identity.

Then update:
- resolver ordering;
- R1 PROVEN_AUTO_FORWARD_ROOT;
- metadata/storage boundary for evidence-only root observations;
- T15 to prove zero provider/send effect and no admission widening.

### Option B — remove automatic-forward root capture from r0.1

If no separate evidence-only path is desired in r0.1:

- remove PROVEN_AUTO_FORWARD_ROOT as an executable r0.1 derivation class;
- remove/replace T15;
- keep official auto-forward semantics only as future protocol context;
- rely on OBSERVED_LINKED_THREAD_ANCHOR + PROVEN_OUTBOUND_LINEAGE + fail-closed isolation for r0.1.

## Non-blocking review findings

No additional blocking defect was established in this review.

The following design boundaries were independently found semantically acceptable, subject to correction D1:

- OFFICIAL_PROTOCOL_FACT / EXACT_PROJECT_EVIDENCE / DESIGN_INFERENCE separation;
- no semantic inference from numeric coincidence outbound_message_id=112 and message_thread_id=112;
- C5 outbound-lineage inheritance under unique same-chat/same-mode committed-effect lookup;
- OBSERVED_LINKED_THREAD_ANCHOR explicitly not claimed as canonical MTProto top root;
- Bot API one-hop reply_to_message used only as bounded direct lineage;
- no cross-chat or direct-topic merge;
- unknown/ambiguous/legacy evidence fail-closed;
- historical tg-dialogue-r02 conversation_key immutability;
- no synthetic legacy backfill;
- versioned root-r01 semantics only for future new turns;
- privacy-minimal proposed scalar metadata;
- send-success + lineage persistence failure => OUTCOME_UNKNOWN / no blind resend;
- root derivation before history/provider selection;
- T1-T14 and T16 are sufficient in scope for a later implementation gate once D1/T15 is corrected.

## Official-source verification

Official Telegram sources checked:

- https://core.telegram.org/bots/api
- https://core.telegram.org/api/discussion
- https://core.telegram.org/api/threads
- https://core.telegram.org/api/forum

Verified official semantics used by the review:

- Message.message_thread_id is an optional thread/topic identifier for supergroups/private chats;
- reply_to_message represents the direct replied message in the same chat/thread and is non-recursive;
- is_automatic_forward marks a channel post automatically forwarded to the connected discussion group;
- a channel-post comment section is the thread of the auto-forwarded message in the discussion supergroup;
- MTProto separates reply_to_msg_id from reply_to_top_id;
- replies inside an existing thread do not spawn nested threads;
- forum topics are a separate mode.

No official source was found that proves the project numeric relation 112==112 is a canonical Telegram root rule.

## Boundary

dialogue_mvp.py mutation:
NONE

DB/schema mutation:
NONE

install:
NONE

service start/enable:
NONE

Telegram calls:
NONE

OpenAI calls:
NONE

runtime/allowlist/credentials mutation:
NONE

failed live task replay:
NONE

## Mandatory RETURN KOO

terminal:
NEEDS_REWORK_SIS_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01

blocking defect count:
1

blocking defect:
R1/T15 automatic-forward root derivation is unreachable under resolver-after-current-admission ordering unless normal admission is unsafely widened.

required next gate:
NEW bounded KOD design-correction task only.

No implementation/install/live authority is created.

## Terminal

NEEDS_REWORK_SIS_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01
