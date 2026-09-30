# KOO -> SIS: Telegram same-thread two-turn multi-turn proof r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

## Exact one-turn routing-placement PASS

puev5691/wellbeing-hq@a34027680c0e08840d9c1897fc70fe4d88ae3590:
entities/sisadmin/outbox/SIS__telegram-one-turn-routing-placement-live-r01-result__KOO.md

blob:
df054ba05aef2d4d064c86a3b5a755e89322a371

terminal:
PASS_SIS_TELEGRAM_ONE_TURN_ROUTING_PLACEMENT_LIVE_R01

Verified:
- tester 6384602715;
- chat -1002429106148;
- provider/model OpenAI / gpt-5.6-luna;
- exactly one accepted turn;
- update_id 560511154;
- inbound_message_id 108;
- message_thread_id 107;
- direct_topic_id 0;
- trigger_class command;
- conversation_key fa88de3f42e098a1bf4b8292ff1516f20889373b4f3740612698aa3917b3e572;
- outbound_message_id 109;
- returned_chat_id -1002429106148;
- returned thread/topic optional fields NULL;
- state COMMITTED;
- OPERATOR_REPLY_VISIBLE=YES;
- final service inactive/dead/disabled/MainPID=0.

Important proven interpretation:
absence of returned_message_thread_id/direct_topic_id in successful sendMessage result is NOT evidence of wrong placement when the reply is visibly confirmed in the selected exact comments view.

## Installed observability basis

puev5691/wellbeing-hq@d6d9d0dafde9170b2ee8d7b0b069025e99f76f4e:
entities/sisadmin/outbox/SIS__telegram-routing-observability-r01-install-verify-r02-result__KOO.md

blob:
a81a6cd3590c9f491d34e1a4b732f003c79a9562

terminal:
PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_INSTALLED_VERIFIED_NO_LIVE_R02

Installed dialogue_mvp.py SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

## Goal

Prove two consecutive provider-backed turns belong to the SAME Telegram thread/dialogue context and SAME runtime conversation_key.

This is a NEW live authority.
Do not replay any prior live task.

## Limits

- accepted turns: exactly 2 maximum
- OpenAI calls: max 2
- send effects: max 2
- duration: max 30 minutes
- nominal provider spend ceiling: USD 1
- one tester only: 6384602715
- one exact discussion only: -1002429106148
- provider/model only: OpenAI / gpt-5.6-luna
- no fallback

## Pre-live gates

Before start verify fresh:

1. current SIS writer unchanged;
2. no superseding two-turn/live task/result;
3. installed observability code exact SHA;
4. pinned runtime config identity unchanged;
5. 9 routing observability columns present;
6. DB integrity ok;
7. no unresolved OUTCOME_UNKNOWN;
8. allowlist exactly 6384602715;
9. 777000 absent;
10. webhook absent;
11. service loaded/inactive/dead/disabled/MainPID=0;
12. dialogue process absent;
13. discussion/bot/model bindings unchanged.

If any fail:
STOP before service start.

## Readiness

Start service only for this bounded proof.
Do not enable persistently.

Emit:

LIVE_READY=YES
TESTER_ID=6384602715
CHAT_ID=-1002429106148
TWO_TURN_SAME_THREAD_PROOF=YES

## OPERATOR procedure

### Turn 1

1. Open ONE exact comments view for one linked discussion surface.
2. Stay in that exact view.
3. Send:
   /ask@WBNP_Media_Bot
   plus a short safe Russian message.
4. Wait until the bot reply is visibly present in THAT SAME comments view.
5. Report:
   TURN1_REPLY_VISIBLE=YES
   or
   TURN1_REPLY_VISIBLE=NO

If NO:
STOP.
Do not send Turn 2.

### Turn 2

Only if Turn 1 reply visible:

6. Use Telegram Reply directly on the exact visible bot reply from Turn 1.
7. Send a short safe Russian continuation.
8. Do not create a new top-level comment/thread.
9. Stay in the same comments view.
10. Wait for second bot reply.
11. Report:
    TURN2_REPLY_VISIBLE=YES
    or
    TURN2_REPLY_VISIBLE=NO

No third turn.

## Required exact capture

For both fresh updates, run read-only diagnose-routing after each is COMMITTED/terminal.

Capture:

- update_id
- inbound_message_id
- message_thread_id
- direct_topic_id
- trigger_class
- conversation_key
- outbound_message_id
- returned_chat_id
- returned_message_thread_id
- returned_direct_topic_id
- returned_is_topic_message
- state
- error_class

No raw content in result.

## Critical continuity proof

Define:

TURN1_INBOUND_TUPLE =
(chat_id, message_thread_id, direct_topic_id)

TURN2_INBOUND_TUPLE =
(chat_id, message_thread_id, direct_topic_id)

Required for PASS:

TURN1_INBOUND_TUPLE == TURN2_INBOUND_TUPLE

AND

conversation_key(Turn1) == conversation_key(Turn2)

Expected Turn 2 trigger class:
reply-to-bot

If Turn 2 trigger_class is not reply-to-bot:
record exact class and treat as FAIL unless exact runtime evidence proves the Reply UI action was not represented that way for a legitimate reason.
Do not guess.

## Dialogue continuity proof

In addition to identical key/tuple, verify bounded DB/session evidence proves:

- Turn 1 user + assistant committed in conversation;
- Turn 2 user + assistant committed into the same conversation history;
- Turn 2 provider request used prior same-conversation history according to the existing runtime contract;
- no cross-thread/cross-chat contamination.

Do not expose raw dialogue content.
Use role/count/order/hash or other bounded non-content evidence sufficient to prove continuity.

## Returned Telegram routing interpretation

Returned optional thread/topic fields may be NULL.

Do NOT classify NULL returned thread/topic as routing failure by itself.

Use:
- exact inbound tuple,
- returned_chat_id,
- successful COMMITTED send,
- OPERATOR visibility in same view,
- continuity tuple/key evidence.

## PASS criteria

PASS requires:

1. exactly two accepted turns;
2. both from tester 6384602715;
3. exact chat -1002429106148;
4. both provider-backed with OpenAI / gpt-5.6-luna;
5. both COMMITTED;
6. Turn 1 visible in same comments view;
7. Turn 2 sent via Reply on Turn 1 bot reply;
8. Turn 2 visible OR, if not visible, protocol continuity remains proven but visibility failure must be separately classified;
9. inbound tuple equality;
10. conversation_key equality;
11. same-conversation history continuity proven;
12. no OUTCOME_UNKNOWN;
13. no replay/duplicate;
14. no wrong-user/wrong-chat effect;
15. privacy boundary preserved;
16. final clean stop.

If Turn 2 reply is not visible but tuple/key/history continuity are all proven:
do NOT call the multi-turn continuity a failure.
Return PASS continuity plus VISIBILITY_TURN2=NO and exact next visibility condition.

## Hard STOP

Stop immediately on:
- Turn 1 not visible;
- different Turn 2 inbound tuple;
- different conversation_key;
- wrong user/chat;
- second thread/new comment;
- OUTCOME_UNKNOWN;
- replay/duplicate;
- provider/model substitution;
- routing metadata persistence failure;
- secret exposure;
- third accepted turn;
- OPERATOR STOP.

## Final state

After two turns or any stop:

service:
loaded / inactive / dead / disabled / MainPID=0

dialogue process:
ABSENT

no persistent enablement.

## Historical tasks

Do not replay r0.3, r0.2, r0.1 one-turn, or earlier live/provenance tasks.

## Expected terminal

PASS_SIS_TELEGRAM_SAME_THREAD_TWO_TURN_MULTITURN_R01

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- RUN_ID;
- pre-live gates;
- LIVE_READY;
- Turn 1 exact routing evidence;
- TURN1_REPLY_VISIBLE;
- Turn 2 exact routing evidence if executed;
- TURN2_REPLY_VISIBLE;
- tuple equality;
- conversation_key equality;
- trigger class comparison;
- same-conversation history continuity evidence;
- provider/model/call counts;
- OUTCOME_UNKNOWN/replay/privacy status;
- final service state;
- exact next condition.

Then STOP.

No third turn or standing live use is authorized.
