# KOO -> SIS: Telegram one-turn routing placement live test r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

## Exact installed observability PASS

puev5691/wellbeing-hq@d6d9d0dafde9170b2ee8d7b0b069025e99f76f4e:
entities/sisadmin/outbox/SIS__telegram-routing-observability-r01-install-verify-r02-result__KOO.md

blob:
a81a6cd3590c9f491d34e1a4b732f003c79a9562

terminal:
PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_INSTALLED_VERIFIED_NO_LIVE_R02

next:
READY_FOR_SEPARATE_ONE_TURN_ROUTING_PLACEMENT_LIVE_TEST

Installed dialogue_mvp.py SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

Pinned runtime.json raw SHA-256:
57f7e44f70056021fc2ac227b7e4e06e2ef0c886b047139548d83cc5d8f2d7e1

Pinned runtime semantic SHA-256:
2ebf58286499a7d7a166d38abf80d2ca6a8a2dfbbe8d5b8a4b16c833a47c40f8

## Exact live bindings

Tester:
6384602715

Discussion chat:
-1002429106148

Bot:
@WBNP_Media_Bot
bot_id:
8866633840

Provider/model:
OpenAI / gpt-5.6-luna

Transport:
Telegram long polling

## Goal

Perform exactly ONE fresh live tester turn after LIVE_READY, then immediately stop accepting further test turns and run read-only diagnose-routing for that exact new update.

Prove exact inbound and outbound Telegram routing placement with the newly installed privacy-safe observability fields.

NO Turn 2 in this task.

## Limits

- accepted tester turns: max 1
- OpenAI calls: max 1
- duration: max 30 minutes from successful service start
- nominal provider spend ceiling: USD 1
- one tester only: 6384602715
- one chat only: -1002429106148
- provider/model only: OpenAI / gpt-5.6-luna

## Pre-live gates

Fresh verify:

1. current SIS writer unchanged;
2. no superseding one-turn/live task/result;
3. installed dialogue_mvp.py SHA-256 exact;
4. runtime raw SHA exact;
5. runtime semantic SHA exact;
6. all 9 routing observability columns present;
7. DB integrity ok;
8. no unresolved/OUTCOME_UNKNOWN precondition;
9. allowlist exactly tester 6384602715;
10. 777000 absent;
11. webhook absent;
12. service loaded/inactive/dead/disabled/MainPID=0;
13. dialogue process absent;
14. discussion/bot/model bindings unchanged.

If any fail:
STOP before service start.

## Readiness

Start service only for this bounded one-turn test.
Do NOT enable persistently.

When runtime is ready emit:

LIVE_READY=YES
TESTER_ID=6384602715
CHAT_ID=-1002429106148
ONE_TURN_ONLY=YES

## Exact OPERATOR procedure

1. OPERATOR chooses ONE exact comments view for one linked discussion surface.
2. Remain in that exact view.
3. After LIVE_READY send exactly one addressed tester turn from personal identity:
   /ask@WBNP_Media_Bot
   plus a short safe Russian message.
4. Do not send any second turn.
5. Stay in the same exact comments view.
6. Report only:
   OPERATOR_REPLY_VISIBLE=YES
   or
   OPERATOR_REPLY_VISIBLE=NO

Do not navigate to another thread/comments surface before visibility report if avoidable.
Do not create a new thread.

## Exact one-turn capture

After first fresh accepted update is COMMITTED or reaches a terminal error state:

- identify exact fresh update_id;
- stop admission/service promptly enough to prevent a second test turn;
- do not request Turn 2.

For that exact update_id run read-only:

dialogue_mvp.py diagnose-routing --config /etc/wellbeing/telegram-single-entity-pilot/runtime.json --update-id <EXACT_NEW_UPDATE_ID>

Capture exactly:

- update_id;
- inbound_message_id;
- message_thread_id;
- direct_topic_id;
- trigger_class;
- conversation_key;
- outbound_message_id;
- returned_chat_id;
- returned_message_thread_id;
- returned_direct_topic_id;
- returned_is_topic_message;
- state;
- error_class.

No raw dialogue text in result.

## Required routing proof

Determine from exact persisted metadata:

1. inbound chat is exact configured discussion;
2. inbound message_thread_id;
3. inbound direct_topic_id;
4. trigger_class;
5. outbound_message_id;
6. returned_chat_id;
7. returned_message_thread_id;
8. returned_direct_topic_id;
9. returned_is_topic_message.

Compare:

INBOUND_THREAD_TUPLE =
(chat_id, message_thread_id, direct_topic_id)

RETURNED_THREAD_TUPLE =
(returned_chat_id, returned_message_thread_id, returned_direct_topic_id)

Classify exact placement:

SAME_ROUTING_TUPLE
or
DIFFERENT_ROUTING_TUPLE
or
RETURNED_FIELD_ABSENT_BY_TELEGRAM
or
INSUFFICIENT_EVIDENCE

Do not infer UI semantics beyond returned protocol fields.

## Human visibility correlation

Record OPERATOR visibility fact:

OPERATOR_REPLY_VISIBLE=YES|NO

Then correlate, without overclaiming:

- protocol routing tuple;
- returned topic/thread metadata;
- OPERATOR visibility in exact selected comments view.

If protocol shows SAME_ROUTING_TUPLE but OPERATOR_REPLY_VISIBLE=NO:
return exact visibility diagnosis condition for next step.
Do not retry live in this task.

If routing tuple differs:
return exact routing mismatch.
Do not retry.

## PASS criteria

PASS for this diagnostic live task does NOT require human visibility YES.

PASS means:
- exactly one tester turn accepted;
- provider/model exact;
- one send effect at most;
- update reaches COMMITTED;
- diagnose-routing returns complete bounded routing evidence sufficient to classify placement;
- no OUTCOME_UNKNOWN;
- no replay/duplicate effect;
- privacy boundary preserved;
- service cleanly stopped.

Terminal PASS may include:
OPERATOR_REPLY_VISIBLE=NO
if routing evidence is complete.

## Hard STOP

Stop immediately on:
- secret exposure;
- wrong user/chat effect;
- second accepted user turn;
- provider/model substitution;
- OUTCOME_UNKNOWN;
- replay/duplicate effect;
- routing metadata persistence failure;
- scope widening need;
- OPERATOR STOP;
- 1 accepted turn;
- 1 provider call after required diagnostic capture.

## Final state

After diagnostic capture:
service must be:
loaded / inactive / dead / disabled / MainPID=0

dialogue process:
ABSENT

No persistent enablement.

## Historical tasks

Do not replay r0.3, r0.2, r0.1 or earlier provenance/live tasks.

## Expected terminal

PASS_SIS_TELEGRAM_ONE_TURN_ROUTING_PLACEMENT_LIVE_R01

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- RUN_ID;
- pre-live gates;
- LIVE_READY;
- exact new update_id;
- exact diagnose-routing bounded output;
- inbound routing tuple;
- returned routing tuple;
- routing placement classification;
- outbound message_id;
- provider/model call count;
- OPERATOR_REPLY_VISIBLE YES/NO;
- OUTCOME_UNKNOWN/replay/privacy status;
- final clean stop state;
- exact next condition.

Then STOP.

NO Turn 2 is authorized by this task.
