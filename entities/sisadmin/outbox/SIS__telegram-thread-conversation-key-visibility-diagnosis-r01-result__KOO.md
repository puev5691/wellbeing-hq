# SIS -> KOO: Telegram thread / conversation-key / visibility diagnosis r0.1

status: PASS
terminal: PASS_SIS_TELEGRAM_THREAD_CONVERSATION_KEY_VISIBILITY_DIAGNOSIS_R01
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
recipient: KOO / КООРДИНАТОР

## Exact task

puev5691/wellbeing-hq@37d04b3d2265fc9b911f4275d20f15b4d65a2cd9:
entities/koordinator/outbox/KOO__telegram-thread-conversation-key-visibility-diagnosis-r01__SIS.md

blob:
84fede1e963cd95ab91d8765086d0ac649f7222e

## Exact failed live result

puev5691/wellbeing-hq@8ea458ac7c50aa179e8220656435f1404cf483c2:
entities/sisadmin/outbox/SIS__telegram-single-entity-bounded-live-pilot-r02-result__KOO.md

blob:
ed5a82f4ccdff9f931c6cd189bf63124fb6d91e3

terminal:
FAIL_SIS_TELEGRAM_SINGLE_ENTITY_BOUNDED_LIVE_PILOT_R02_CROSS_THREAD_CONTAMINATION

## Current service state

LoadState=loaded
ActiveState=inactive
SubState=dead
UnitFileState=disabled
MainPID=0

No service start, OpenAI call, Telegram send/edit/delete, allowlist/config/credential/DB mutation was performed in this diagnostic task.

## Immutable runtime code basis

Package source:
puev5691/wellbeing-hq@e3360481959f2076fb53e31390bbdb91bec123ab:
entities/koder/outbox/telegram-single-entity-discussion-admission-correction-r02/dialogue_mvp.py

blob:
0ea2cb8c9fe4872bfbfd1ec348ba23bfa9dbce6d

Installed code identity had already been verified against package SHA256 in live preflight.

### Exact conversation-key rule

Runtime class InboundMessage derives:

conversation_key =
SHA256(
  "tg-dialogue-r02\0"
  + chat_id
  + "\0"
  + message_thread_id
  + "\0"
  + direct_topic_id
)

Inputs:
- chat_id
- message_thread_id
- direct_topic_id

NOT included:
- inbound message_id
- reply_to_message.message_id
- reply_to_message.message_thread_id
- channel/root message id
- trigger class
- text

Therefore reply/root identity does not directly change conversation_key.

### Exact parse defaults

Runtime:
- message_id = msg["message_id"]
- thread_id = msg.get("message_thread_id", 0)
- direct_topic_id = 0 unless msg["direct_messages_topic"]["topic_id"] exists

Raw message_id/thread/reply/topic fields are not persisted separately in the updates table.

### Exact send rule

TelegramBotAdapter.send_text sends:
- chat_id = admitted inbound event.chat_id
- message_thread_id = inbound event.thread_id, if nonzero
- direct_messages_topic_id = inbound event.direct_topic_id, if nonzero
- text

It does NOT set reply_to_message_id.

The Bot API result retained by runtime is only result.message_id.

## Preserved DB facts for target updates

### update_id 560511149

PROTOCOL_FACT:
- state=COMMITTED
- error_class=NONE
- conversation_key=a93afb2296e00d32d63d976452824376fae25b2dee0dcc39e1ac9a09879d6314
- outbound Telegram message_id=101
- DB message sequence for that conversation=user,assistant
- admitted chat must be exact configured discussion -1002429106148 because parse_update rejects all other chats before claim/provider/send

UNKNOWN / NOT PERSISTED:
- inbound message_id
- raw message_thread_id
- reply_to_message.message_id
- reply_to_message.message_thread_id
- is_topic_message
- raw direct_messages_topic
- exact trigger class

DERIVED_RECONSTRUCTION, NOT RAW FACT:
For exact chat -1002429106148 and direct_topic_id=0,
the runtime formula with message_thread_id=60 produces exactly:
a93afb2296e00d32d63d976452824376fae25b2dee0dcc39e1ac9a09879d6314

Thus (thread_id=60,direct_topic_id=0) is an exact matching preimage candidate.
Because raw direct_topic_id was not persisted, this is not promoted to raw Telegram fact.

### update_id 560511151

PROTOCOL_FACT:
- state=COMMITTED
- error_class=NONE
- conversation_key=6e0d67535c74d3d9319afb5536af35b2040d9b459db49d65b95a76dec6b0ee8a
- outbound Telegram message_id=104
- DB message sequence for that conversation=user,assistant
- admitted chat must be exact configured discussion -1002429106148

UNKNOWN / NOT PERSISTED:
- inbound message_id
- raw message_thread_id
- reply_to_message.message_id
- reply_to_message.message_thread_id
- is_topic_message
- raw direct_messages_topic
- exact trigger class

DERIVED_RECONSTRUCTION, NOT RAW FACT:
For exact chat -1002429106148 and direct_topic_id=0,
the runtime formula with message_thread_id=102 produces exactly:
6e0d67535c74d3d9319afb5536af35b2040d9b459db49d65b95a76dec6b0ee8a

Thus (thread_id=102,direct_topic_id=0) is an exact matching preimage candidate.
Again raw direct_topic_id is not persisted, so this is not raw Telegram fact.

## Why the keys differ

PROTOCOL_FACT:

The chat is fixed to one admitted value:
-1002429106148

The two stored conversation_key values differ.

Because the key is derived only from:
chat_id + thread_id + direct_topic_id

and chat_id is fixed, at least one of these differed between the two admitted turns:
- message_thread_id
- direct_topic_id

No reply/root field participates in the key.

Therefore the difference is not caused by merely replying to a different message inside the same unchanged thread.

The matching-preimage reconstruction strongly points to:
- first live turn: thread candidate 60
- second live turn: thread candidate 102
with direct_topic_id=0 in both.

## Trigger class

PROTOCOL_FACT:
Both committed turns passed parse_update/addressed_text and therefore satisfied at least one accepted trigger condition.

Runtime accepted trigger classes:
- reply_to-bot
- exact @WBNP_Media_Bot mention entity
- exact /ask or /ask@WBNP_Media_Bot bot_command entity

UNKNOWN:
The exact accepted trigger class for update 560511149/560511151 was not persisted.

UI_INFERENCE:
OPERATOR screenshots visibly show text beginning with /ask@WBNP_Media_Bot for at least the tested UI action, so bot_command is plausible, but Telegram entity metadata was not preserved and this is not protocol proof of the exact class.

## Telegram replies 101 and 104

### reply message_id 101

PROTOCOL_FACT:
- successful Telegram sendMessage occurred before COMMITTED
- result.message_id=101
- send target chat was exact admitted inbound chat -1002429106148
- runtime does not set reply_to_message_id
- runtime would send message_thread_id equal to inbound event.thread_id if nonzero
- runtime would send direct_messages_topic_id equal to inbound event.direct_topic_id if nonzero

UNKNOWN:
- returned Telegram Message object's thread/root fields were not persisted
- exact UI location cannot be recovered by message ID from current preserved evidence
- no existing runtime evidence contains a Bot-API readback of message 101

UI_INFERENCE:
If the reconstructed preimage is correct, reply 101 was sent into discussion thread 60, not as an explicit reply-to-user message.

### reply message_id 104

PROTOCOL_FACT:
- successful Telegram sendMessage occurred before COMMITTED
- result.message_id=104
- send target chat was -1002429106148
- no explicit reply_to_message_id was set by runtime

UNKNOWN:
- returned thread/root fields not persisted
- exact UI location cannot be recovered from preserved evidence

UI_INFERENCE:
If the reconstructed preimage is correct, reply 104 was sent into discussion thread 102.

## Bot-API visibility limitation in this evidence set

The runtime retained only outbound result.message_id, not the full returned Telegram Message object.

This diagnostic is restricted to existing evidence and did not issue any Bot API call.

No existing preserved evidence provides a message-by-ID readback for 101 or 104.

Therefore exact visible placement of message IDs 101/104 in Telegram UI is:
UNKNOWN from protocol evidence.

## Linked discussion / UI semantics classification

### PROTOCOL_FACT

Runtime semantics:
- exact discussion chat is -1002429106148
- each accepted event receives Telegram message_thread_id as thread_id, default 0 if absent
- conversation history is isolated by chat_id + thread_id + direct_topic_id
- reply_to_message is inspected only for trigger admission; reply/root ID does not enter conversation_key
- provider reply is sent back to the same event chat/thread/direct-topic tuple
- same exact thread tuple => same conversation_key
- different thread/direct-topic tuple => different conversation_key

### UI_INFERENCE

Based on OPERATOR-observed actions/screenshots:
- first test was entered from a comment/discussion view
- after no visible reply, OPERATOR navigated through other comment surfaces and explicitly created a new thread
- this is consistent with the runtime later seeing distinct thread contexts

The exact Telegram-client mapping of each button label ("Прокомментировать", new top-level comment, linked-channel post comment surface) to Bot API message_thread_id was not preserved and is not promoted to PROTOCOL_FACT.

## Distinguishing common actions

### New top-level comment

PROTOCOL requirement:
It is safe for same-conversation continuity only if Telegram emits the SAME message_thread_id/direct_topic_id tuple as the prior turn.

UI label alone is insufficient proof.

### Reply on bot message

Runtime mapping:
reply_to_message identity does not enter conversation_key.

If Telegram keeps the same thread tuple, replying directly to the bot remains the same conversation_key and also satisfies reply-to-bot admission.

This is the preferred Turn 2 procedure.

### Reply inside existing comment thread

If it stays inside the same Telegram thread tuple:
same conversation_key.

### "New comment" / new thread / different linked channel post comments

If Telegram changes message_thread_id:
different conversation_key by design.

OPERATOR explicitly reported creating a new thread during the failed pilot; that is consistent with the observed distinct keys.

## Exact future two-turn procedure

1. Start only after LIVE_READY.
2. Choose ONE specific linked-discussion comment view for ONE channel post/thread.
3. Do not navigate back to channel composer after Turn 1.
4. Do not create another channel post.
5. Do not use "new thread" or another post's comment surface.
6. Turn 1:
   send one exact addressed command inside that chosen existing comments/thread view.
7. Wait for the bot message to become visible in THAT SAME comments/thread view.
8. If no bot reply becomes visible:
   STOP the human test.
   Do NOT send elsewhere and do NOT create a new thread.
   Diagnose visibility first.
9. Turn 2:
   use Telegram's Reply action directly on the visible bot reply in the same comments/thread view.
   This makes reply-to-bot an accepted trigger while keeping the same thread context if Telegram preserves the thread tuple.
10. Runtime/verifier should require identical conversation_key after Turn 1 before allowing/asking for Turn 2 completion.
11. If second event has a different conversation_key:
    STOP immediately; do not continue searching through UI surfaces.

## Root cause class

ROOT_CAUSE_CLASS=OPERATOR_UI_PROCEDURE_MISMATCH

Basis:
- runtime mapping behaved according to exact design;
- two accepted committed turns landed in distinct conversation contexts;
- OPERATOR explicitly reported commenting in multiple places and creating a new thread after not seeing the reply;
- creating/navigating to a different thread is incompatible with the exact two-turn same-thread requirement.

Secondary unresolved issue:
VISIBILITY_SUBCAUSE=INSUFFICIENT_EVIDENCE

The reason Telegram replies 101 and 104 were not visibly noticed by OPERATOR is not proven from preserved protocol evidence.

A Telegram thread/UI semantics contribution is plausible, but exact message placement was not saved.

## Runtime defect assessment

RUNTIME_MAPPING_DEFECT:
NOT PROVEN

The runtime's key derivation and send-back-to-same-thread logic are internally consistent with its documented contract.

No functional code fix is required by this evidence merely to maintain same-thread history.

## Optional KOD observability handoff, if KOO decides it is useful

Not required to fix the proven root cause, but future diagnosis would be materially easier if a separately authorized KOD change persisted privacy-safe routing metadata per admitted update:

file/function locators:
- dialogue_mvp.py :: InboundMessage
- dialogue_mvp.py :: Store updates schema / claim
- dialogue_mvp.py :: TelegramBotAdapter.send_text / commit_turn

Candidate fields:
- inbound_message_id
- message_thread_id
- direct_topic_id
- trigger_class
- outbound_message_id

Do NOT persist:
- raw Update JSON
- usernames/display names
- unrelated identities
- provider raw response

Any schema/privacy change requires separate KOD design/review authority; SIS does not modify code here.

## Mandatory RETURN KOO

chat:
-1002429106148

target updates:
560511149, 560511151

new reply message IDs:
101, 104

exact raw inbound message IDs:
UNKNOWN_NOT_PERSISTED

exact raw message_thread_id:
UNKNOWN_NOT_PERSISTED

conversation-key derivation:
PROVEN

reply/root IDs in conversation-key:
NO

distinct conversation-key:
PROVEN

matching reconstruction if direct_topic_id=0:
- update 560511149 -> thread 60
- update 560511151 -> thread 102

exact reply visibility:
UNKNOWN

same-thread test procedure:
DEFINED

root cause:
OPERATOR_UI_PROCEDURE_MISMATCH

visibility subcause:
INSUFFICIENT_EVIDENCE

runtime mapping defect:
NOT PROVEN

service final:
loaded / inactive / dead / disabled / MainPID=0

OpenAI calls in diagnosis:
NONE

Telegram sends/edits/deletes in diagnosis:
NONE

DB mutation in diagnosis:
NONE

## Terminal

PASS_SIS_TELEGRAM_THREAD_CONVERSATION_KEY_VISIBILITY_DIAGNOSIS_R01
