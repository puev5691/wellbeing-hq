# KOO -> SIS: Telegram same-thread bounded live pilot r0.3

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

## Exact diagnostic basis

puev5691/wellbeing-hq@ef033331a12cc0faf47ccaef78012d94fa6e7477:
entities/sisadmin/outbox/SIS__telegram-thread-conversation-key-visibility-diagnosis-r01-result__KOO.md
blob fa8a7438fd94eb12a23724e567fc9079ae67ba13

terminal:
PASS_SIS_TELEGRAM_THREAD_CONVERSATION_KEY_VISIBILITY_DIAGNOSIS_R01

Root cause class:
OPERATOR_UI_PROCEDURE_MISMATCH

Visibility subcause:
INSUFFICIENT_EVIDENCE

Runtime mapping defect:
NOT PROVEN

Conversation key rule:
SHA256(chat_id + message_thread_id + direct_topic_id)

Reply/root message IDs do not participate directly in conversation_key.

## Exact prior live result

puev5691/wellbeing-hq@8ea458ac7c50aa179e8220656435f1404cf483c2:
entities/sisadmin/outbox/SIS__telegram-single-entity-bounded-live-pilot-r02-result__KOO.md
blob ed5a82f4ccdff9f931c6cd189bf63124fb6d91e3

terminal:
FAIL_SIS_TELEGRAM_SINGLE_ENTITY_BOUNDED_LIVE_PILOT_R02_CROSS_THREAD_CONTAMINATION

r0.2 is consumed / non-replayable.

## Confirmed runtime bindings

Tester:
6384602715

Discussion:
-1002429106148

Bot:
@WBNP_Media_Bot
bot_id 8866633840

Provider/model:
OpenAI / gpt-5.6-luna

Allowlist:
exactly one tester 6384602715

Transport:
Telegram long polling

## Goal

Prove two consecutive provider-backed turns in ONE exact Telegram thread/conversation_key using the SIS-diagnosed operator procedure.

Do not change runtime code in this task.

## Pre-live gates

Before service start verify fresh:
- current SIS writer unchanged;
- no superseding Telegram live/diagnostic task/result;
- final allowlist exactly 6384602715;
- 777000 absent;
- webhook absent;
- service inactive/dead/disabled/MainPID=0;
- no competing dialogue process;
- exact discussion/bot/model bindings unchanged;
- credentials present/nonempty without disclosure;
- no persisted blocking OUTCOME_UNKNOWN.

If any fail:
STOP before start.

## Live authority

This NEW task authorizes one bounded live pilot only.

Limits:
- accepted user turns max 10;
- OpenAI calls max 10;
- duration max 1 hour from successful service start;
- nominal provider spend ceiling USD 2;
- one confirmed tester only;
- one exact discussion only;
- OpenAI gpt-5.6-luna only;
- no fallback provider/model.

Do not enable service persistently.

## Readiness signal

After service is active and admission ready, emit:

LIVE_READY=YES
TESTER_ID=6384602715
CHAT_ID=-1002429106148
SAME_THREAD_PROCEDURE_REQUIRED=YES

## Exact OPERATOR procedure

The human test MUST follow this sequence:

1. Open ONE specific linked-discussion comments view for ONE channel post/thread.
2. Stay in that exact comments/thread view for the whole test.
3. Do not navigate back to the channel composer after Turn 1.
4. Do not create a new channel post.
5. Do not use "new thread", "new comment" in another surface, or another post's comments.

Turn 1:
6. Send one exact addressed command in that chosen view:
   /ask@WBNP_Media_Bot
   plus a short safe Russian message/question.

7. Wait for the bot reply to become visible in THAT SAME comments/thread view.

8. If the bot reply does NOT become visible:
   HUMAN_STOP_VISIBILITY=YES
   Do not send Turn 2 anywhere else.
   Do not create a new thread.
   Stop the pilot and return a visibility blocker.

Turn 2:
9. Use Telegram Reply directly on the visible bot reply from Turn 1.
10. Send a short safe Russian continuation.
11. Do not use a new top-level comment/thread action.

## Runtime verification

For Turn 1 and Turn 2 verify:
- tester id = 6384602715;
- chat id = -1002429106148;
- both turns COMMITTED;
- provider = OpenAI;
- model = gpt-5.6-luna;
- no OUTCOME_UNKNOWN;
- no replay collision;
- no duplicate effect.

Critical success criterion:
conversation_key(Turn1) == conversation_key(Turn2)

If Turn2 gets a different conversation_key:
STOP immediately.
Do not continue with a third exploratory turn.

## PASS criteria

PASS requires:
- Turn 1 provider-backed Telegram reply delivered;
- Turn 1 bot reply visibly observed by OPERATOR in the selected exact comments/thread view;
- Turn 2 sent using Reply on that exact visible bot reply;
- Turn 2 provider-backed Telegram reply delivered;
- identical conversation_key for Turn 1 and Turn 2;
- same-thread continuity demonstrated;
- privacy/log boundary PASS;
- no wrong-user/wrong-chat effect;
- no cross-thread/chat contamination;
- no OUTCOME_UNKNOWN;
- no replay collision/duplicate external effect;
- final clean stop.

## Visibility blocker

If provider/send COMMITTED for Turn 1 but OPERATOR cannot see the reply in the exact selected comments/thread view:
stop and return:

BLOCKED_SIS_TELEGRAM_SAME_THREAD_LIVE_R03_REPLY_VISIBILITY_NOT_CONFIRMED

Do NOT ask OPERATOR to search other Telegram surfaces during the active test.
Do NOT send Turn 2.

## Hard STOP

Stop on:
- secret exposure;
- effect for non-allowlisted user;
- wrong chat;
- cross-thread/chat contamination;
- OUTCOME_UNKNOWN;
- replay duplicate;
- provider/model substitution;
- unexpected config/admission mutation;
- 3 consecutive runtime/provider failures;
- 10 accepted turns;
- 10 provider calls;
- 1 hour;
- USD 2 ceiling;
- OPERATOR STOP.

## Final state

After PASS/BLOCKED/FAIL:
stop service and verify:
loaded / inactive / dead / disabled / MainPID=0.

## Observability boundary

No KOD observability code change is authorized here.

The diagnosis identified an optional future improvement:
privacy-safe persistence of:
- inbound_message_id;
- message_thread_id;
- direct_topic_id;
- trigger_class;
- outbound_message_id.

This is NOT required for this live task and must not be implemented here.

If r0.3 still cannot establish visibility/thread facts because the metadata is not persisted, return that exact limitation to KOO; KOO may then open a separate KOD task.

## Historical tasks

Do not replay r0.2, r0.1 or provenance tasks.

## Expected terminal

PASS_SIS_TELEGRAM_SAME_THREAD_BOUNDED_LIVE_PILOT_R03

or exact BLOCKED_/FAIL_.

Mandatory RETURN KOO:
- pre-live gates;
- RUN_ID;
- LIVE_READY;
- Turn 1 state/conversation_key/outbound message id;
- OPERATOR visibility confirmation for Turn 1;
- Turn 2 state/conversation_key/outbound message id if executed;
- equality check of conversation keys;
- provider/model/call counts;
- OUTCOME_UNKNOWN/replay/privacy status;
- exact visibility blocker if applicable;
- final clean stop state.

Then STOP.
