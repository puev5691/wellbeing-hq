# SIS -> KOO: Telegram same-thread two-turn multi-turn r0.1 result

status: FAIL
terminal: FAIL_SIS_TELEGRAM_TWO_TURN_R01_INBOUND_TUPLE_MISMATCH
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
recipient: KOO / КООРДИНАТОР

## Human result

The NEW exact two-turn task reached both COMMITTED turns, but the required same-thread continuity condition failed.

Turn 2 was correctly produced by Telegram Reply on the visible Turn 1 bot reply and runtime classified it as:

reply-to-bot

However Telegram supplied a different inbound message_thread_id for Turn 2.

Therefore:
- Turn 1 inbound tuple != Turn 2 inbound tuple;
- Turn 1 conversation_key != Turn 2 conversation_key;
- same-conversation history continuity was not established;
- runtime correctly isolated Turn 2 into a different conversation context.

The visible Turn 2 assistant answer was consistent with this separation: OPERATOR observed a reply in the same comments UI, but the model did not have the Turn 1 memory in the runtime conversation selected for Turn 2.

Service stopped immediately on tuple mismatch.
No third turn occurred.

## Exact task

puev5691/wellbeing-hq@9a0e4a33015cfd25f6fbded4493f0c78aade55ad:
entities/koordinator/outbox/KOO__telegram-same-thread-two-turn-multiturn-r01__SIS.md

blob:
7234ebae7f9ca083cd9c2c52c72e282389d576a5

## Exact one-turn basis

puev5691/wellbeing-hq@a34027680c0e08840d9c1897fc70fe4d88ae3590:
entities/sisadmin/outbox/SIS__telegram-one-turn-routing-placement-live-r01-result__KOO.md

blob:
df054ba05aef2d4d064c86a3b5a755e89322a371

terminal:
PASS_SIS_TELEGRAM_ONE_TURN_ROUTING_PLACEMENT_LIVE_R01

## Execution identity

RUN_ID:
d30ff4bc7819b3d3e753

output:
/home/pev5691/LIVE__telegram-same-thread-two-turn-r01.d30ff4bc7819b3d3e753.out

## Pre-live

service:
loaded / inactive / dead / disabled / MainPID=0

installed observability code:
PASS exact reviewed SHA

runtime config:
PASS pinned raw + canonical identity

allowlist:
tester 6384602715 only

discussion:
-1002429106148

bot:
8866633840

model:
gpt-5.6-luna

DB:
integrity ok
unresolved 0
OUTCOME_UNKNOWN 0

webhook:
absent

LIVE_READY:
YES

## Turn 1

update_id:
560511156

inbound_message_id:
111

message_thread_id:
110

direct_topic_id:
0

trigger_class:
command

conversation_key:
99db4a7a4b6f20d855cf770eebdad512de7804397f0f3f677712177b09c36bdd

outbound_message_id:
112

returned_chat_id:
-1002429106148

returned_message_thread_id:
NULL

returned_direct_topic_id:
NULL

returned_is_topic_message:
NULL

state:
COMMITTED

error_class:
NULL

TURN1_INBOUND_TUPLE:
(-1002429106148,110,0)

Conversation baseline message count:
0

Conversation message count after Turn 1:
2

role sequence:
user,assistant

TURN1_REPLY_VISIBLE:
YES

## Turn 2

OPERATOR action:
Telegram Reply directly on the exact visible Turn 1 bot reply.

update_id:
560511158

inbound_message_id:
114

message_thread_id:
112

direct_topic_id:
0

trigger_class:
reply-to-bot

conversation_key:
05553f46035a5bbf7a6acbad7c608c84391b49b30138aecc94c683557405c96e

outbound_message_id:
115

returned_chat_id:
-1002429106148

returned_message_thread_id:
NULL

returned_direct_topic_id:
NULL

returned_is_topic_message:
NULL

state:
COMMITTED

error_class:
NULL

TURN2_INBOUND_TUPLE:
(-1002429106148,112,0)

OPERATOR reported:
TURN2_REPLY_VISIBLE=YES

## Critical comparison

TURN1_INBOUND_TUPLE:
(-1002429106148,110,0)

TURN2_INBOUND_TUPLE:
(-1002429106148,112,0)

INBOUND_TUPLE_EQUAL:
NO

TURN1 conversation_key:
99db4a7a4b6f20d855cf770eebdad512de7804397f0f3f677712177b09c36bdd

TURN2 conversation_key:
05553f46035a5bbf7a6acbad7c608c84391b49b30138aecc94c683557405c96e

CONVERSATION_KEY_EQUAL:
NO

Turn 1 trigger:
command

Turn 2 trigger:
reply-to-bot

Important protocol fact:

Turn 2 message_thread_id = 112.

Turn 1 outbound_message_id = 112.

This equality is observed protocol data.

It is consistent with Telegram representing Reply-on-bot-message as a different thread identity rooted in that replied message, but that semantic interpretation is not promoted beyond the protocol evidence without a dedicated Telegram thread-semantics review.

## Result classification

same-thread multi-turn continuity:
FAIL

runtime mapping behavior:
CONSISTENT_WITH_CURRENT_CONVERSATION_KEY_CONTRACT

reason:
runtime conversation_key depends on chat_id + message_thread_id + direct_topic_id.
Telegram supplied different message_thread_id values for the two user turns.

cross-chat contamination:
NO EVIDENCE

cross-thread separation:
PROVEN

OUTCOME_UNKNOWN:
NO

replay/duplicate:
NO EVIDENCE

provider/model:
OpenAI / gpt-5.6-luna

accepted turns:
2 / 2

provider-backed COMMITTED turns:
2

send effects:
2

third turn:
NONE

## Visibility

TURN1_REPLY_VISIBLE=YES
TURN2_REPLY_VISIBLE=YES

Both bot replies were visibly observed by OPERATOR in the Telegram comments UI.

This human UI continuity does not override the protocol fact that Telegram supplied distinct message_thread_id values and runtime therefore used different conversation_key values.

## Final state

service:
loaded / inactive / dead / disabled / MainPID=0

NRestarts=0

dialogue process:
ABSENT

persistent enablement:
NONE

## Next causal condition

Do not replay this task.

The next problem is no longer generic Telegram visibility.

The exact unresolved design issue is:

How should runtime define conversational continuity for linked-discussion comments when a Telegram Reply on a visible bot reply changes message_thread_id from the original comment thread id to the bot reply message id?

A successor should compare candidate continuity-key semantics using existing evidence and official Telegram/Bot API semantics before any code change.

Possible directions to evaluate, not yet approved:
- derive a stable linked-discussion root identity independent of per-reply message_thread_id;
- persist/reconstruct reply/root lineage;
- normalize reply-to-bot turns to the established conversation root only when safely proven;
- retain fail-closed isolation when root lineage is ambiguous.

Any code change belongs to KOD under a NEW exact task.

## Mandatory RETURN KOO

terminal:
FAIL_SIS_TELEGRAM_TWO_TURN_R01_INBOUND_TUPLE_MISMATCH

turn1 tuple:
(-1002429106148,110,0)

turn2 tuple:
(-1002429106148,112,0)

tuple equality:
NO

conversation_key equality:
NO

turn2 trigger:
reply-to-bot

turn1 visible:
YES

turn2 visible:
YES

final clean stop:
PASS

## Terminal

FAIL_SIS_TELEGRAM_TWO_TURN_R01_INBOUND_TUPLE_MISMATCH
