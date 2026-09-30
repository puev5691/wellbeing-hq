# KOO -> SIS: Telegram thread/conversation-key visibility diagnosis r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

terminal:
PASS_SIS_R07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Exact failed live result

puev5691/wellbeing-hq@8ea458ac7c50aa179e8220656435f1404cf483c2:
entities/sisadmin/outbox/SIS__telegram-single-entity-bounded-live-pilot-r02-result__KOO.md

blob:
ed5a82f4ccdff9f931c6cd189bf63124fb6d91e3

terminal:
FAIL_SIS_TELEGRAM_SINGLE_ENTITY_BOUNDED_LIVE_PILOT_R02_CROSS_THREAD_CONTAMINATION

Verified facts:
- pre-live gates PASS;
- service start PASS;
- LIVE_READY PASS;
- tester 6384602715;
- chat -1002429106148;
- provider/model OpenAI / gpt-5.6-luna;
- two NEW turns COMMITTED;
- Telegram reply message IDs 101 and 104;
- request_complete_200 = 2;
- OUTCOME_UNKNOWN = NONE;
- replay collision = NO EVIDENCE;
- privacy/log = PASS;
- final clean stop PASS.

New turn 1:
- update_id 560511149
- conversation_key a93afb2296e00d32d63d976452824376fae25b2dee0dcc39e1ac9a09879d6314
- telegram_reply_message_id 101

New turn 2:
- update_id 560511151
- conversation_key 6e0d67535c74d3d9319afb5536af35b2040d9b459db49d65b95a76dec6b0ee8a
- telegram_reply_message_id 104

## Goal

Determine the exact Telegram thread/topic/UI mapping of the two NEW committed turns and the exact reason the runtime produced distinct conversation_key values.

This task is READ-ONLY DIAGNOSTIC ONLY.

No provider calls.
No sendMessage.
No service start.
No DB content mutation.

## Diagnostic questions

### Q1. Exact inbound Telegram mapping

For update_id 560511149 and 560511151, recover from existing persisted/runtime evidence, if available:

- chat.id;
- message_id;
- message_thread_id;
- reply_to_message.message_id if preserved;
- reply_to_message.message_thread_id if preserved;
- is_topic_message;
- sender_chat presence;
- from.id;
- bot_command/reply/mention trigger class;
- any linked-channel auto-forward marker;
- any discussion-root/reference metadata already persisted.

Do not expose raw dialogue text.

If some field was not preserved, mark UNKNOWN.
Do not reconstruct it from assumptions.

### Q2. conversation_key derivation

Read-only inspect the installed accepted runtime/package code and config sufficient to establish:

- exact inputs used to derive conversation_key;
- whether message_thread_id is part of the key;
- whether reply target/root message ID is part of the key;
- whether chat_id + tester_id + thread/topic identifier are used;
- what fallback is used when message_thread_id is null/absent;
- whether a new top-level discussion comment naturally generates a different conversation_key.

Return the exact derivation rule or, if code ownership/semantics cannot be conclusively interpreted within SIS role, return:
BLOCKER_REQUIRES_KOD_CODE_SEMANTICS_REVIEW
with exact file/function/lines or locator to hand to KOD.

Do not modify code.

### Q3. Outbound message IDs 101 and 104

Using only read-only evidence already available from:
- runtime DB;
- invocation journal;
- service logs;
- Telegram API methods that do NOT create messages/effects;
- linked discussion/channel metadata;

determine, as far as the evidence permits:

- exact chat_id used for sendMessage for message 101;
- exact reply/thread parameter used;
- exact chat_id used for sendMessage for message 104;
- exact reply/thread parameter used;
- whether Telegram assigned message_thread_id;
- whether replies belong to different discussion comment roots/topics;
- whether both sends were in the linked discussion supergroup;
- whether either reply is attached to an automatically forwarded channel post thread.

Do not call sendMessage/editMessage/deleteMessage.
Do not create any external effect.

If Bot API cannot retrieve message content by ID and no persisted evidence exists, state that limitation explicitly rather than inferring.

### Q4. Operator UI visibility

Reconcile the server-side evidence with the OPERATOR fact:

OPERATOR did not see reply message IDs 101 and 104 in the expected UI surface.

Classify the most supported UI/routing explanation among:

A. replies landed under two different linked-post comment threads;
B. replies landed in supergroup main discussion surface but not the UI view OPERATOR was watching;
C. replies landed in topic/thread surfaces not exposed by the current Android view;
D. OPERATOR created two separate top-level comments, so Telegram assigned distinct logical discussion roots;
E. runtime replied to different root/reply targets because of trigger semantics;
F. evidence insufficient.

Do not assert a client-UI fact that Bot API/runtime evidence cannot prove.

### Q5. Linked-channel discussion behavior

Using current exact Telegram metadata and official/runtime evidence already available locally, determine whether the linked discussion is:
- is_forum false/true;
- ordinary linked discussion group;
- how channel post comments map to discussion messages/threads for this exact chat;
- whether "Комментарий", "Новый комментарий", replying to a bot message, and posting a new top-level message can produce distinct message_thread_id / root semantics in this runtime.

If exact Telegram client behavior cannot be proven read-only, distinguish:
PROTOCOL_FACT
from
UI_INFERENCE.

No web research is required unless existing task evidence is insufficient and current SIS role already permits it; prefer exact live-system evidence.

### Q6. Exact future two-turn procedure

Return one precise OPERATOR procedure for the next live test that maximizes probability of two turns mapping to the SAME conversation_key.

It must specify what the OPERATOR should do in Telegram UI, for example only if supported by evidence:
- send first addressed command;
- wait for bot reply;
- use Reply on that exact bot reply;
- send second message from personal identity;
- do not use "new comment" / new top-level comment;
- remain in the same linked-post comment thread.

Do not guess wording. Tie every step to the established conversation_key derivation.

### Q7. Runtime defect vs operator procedure

Classify final cause as one of:

RUNTIME_MAPPING_DEFECT
OPERATOR_UI_PROCEDURE_MISMATCH
TELEGRAM_THREAD_SEMANTICS_MISMATCH
INSUFFICIENT_EVIDENCE
MIXED_CAUSE

If runtime mapping defect is proven or likely requires code correction:
STOP with exact KOD handoff requirement.
Do not patch code in SIS task.

## Safety boundaries

Must remain throughout:
- service inactive/dead/disabled/MainPID=0;
- dialogue process absent;
- webhook absent unless read-only evidence proves otherwise;
- no OpenAI call;
- no Telegram sendMessage/edit/delete;
- no credential mutation;
- no allowlist mutation;
- no dialogue DB content mutation;
- no Telegram rights/settings mutation.

Do NOT replay:
- live r0.2;
- failed live r0.1;
- provenance r0.3/r0.4/r0.5/r0.6;
- final gate.

## Output

Return one immutable SIS diagnostic result to KOO.

Expected terminal:

PASS_SIS_TELEGRAM_THREAD_CONVERSATION_KEY_VISIBILITY_DIAGNOSIS_R01

or exact BLOCKED_/FAIL_.

Mandatory RETURN:
- exact inbound mapping table for update 560511149 and 560511151;
- exact/UNKNOWN conversation_key derivation;
- outbound 101/104 routing evidence;
- UI visibility diagnosis with fact/inference separation;
- root cause class;
- one exact future same-thread OPERATOR procedure;
- whether KOD correction is required;
- service remains inactive/dead/disabled/MainPID=0;
- OpenAI calls NONE;
- Telegram send effects NONE;
- DB mutation NONE.

Then STOP.
