# KOO -> SIS: Telegram personal-sender human provenance verification r0.4

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Exact sender-identity diagnosis PASS:
puev5691/wellbeing-hq@50da69699d9b0bbb275bb2fe65d4b943b3649551:
entities/sisadmin/outbox/SIS__telegram-personal-sender-identity-diagnosis-r01-result__KOO.md
blob 32f7a1cc88aaf1ef1c9637c34bb84e46cdd50ada

terminal:
PASS_SIS_TELEGRAM_PERSONAL_SENDER_IDENTITY_CONDITION_DIAGNOSED_R01

Verified prior diagnosis:
OPERATOR_ADMIN_ANONYMOUS_MODE

OPERATOR current decision/evidence:
UI correction completed.
Remain Anonymous / anonymous-owner mode disabled or personal sender identity is now available.

Verified Telegram binding:
bot @WBNP_Media_Bot
bot_id 8866633840
discussion_chat_id -1002429106148
chat_type supergroup

Known invalid fake sender:
777000
MUST NOT be accepted.

Consumed historical tasks:
- r0.3 human tester discovery: consumed / non-replayable
- failed live r0.1: consumed / non-replayable

Goal:
verify protocol-level personal human sender provenance after the UI correction and discover one exact HUMAN_TESTER_1_CANDIDATE.

Task:

1. Fresh-verify:
   - current SIS writer;
   - exact sender-identity diagnosis result;
   - no superseding Telegram verification/discovery/live task/result;
   - service remains loaded/inactive/dead/disabled;
   - MainPID=0;
   - no dialogue process running;
   - allowlist is NOT modified in this task.

2. Read-only verify owner/admin anonymous state in exact discussion:
   - use Bot API read-only admin/member metadata sufficient to determine current owner is_anonymous state;
   - expected condition:
     owner/admin anonymous state is no longer true.
   - preserve only aggregate/non-secret evidence.
   - if owner remains anonymous:
     STOP with exact blocker:
     BLOCKED_SIS_TELEGRAM_PERSONAL_SENDER_VERIFICATION_R04_OWNER_STILL_ANONYMOUS
     Do not continue to discovery.

3. Fresh read-only getWebhookInfo.
   If webhook active:
   STOP with exact blocker.
   Do not remove webhook.

4. If owner/admin non-anonymous state PASS and webhook absent:
   start one bounded getUpdates observation window.

5. OPERATOR may send one fresh exact command from the now-selected personal sender identity:

   /ask@WBNP_Media_Bot

6. Accept HUMAN_TESTER_1_CANDIDATE ONLY when ALL are true:
   - update type is message;
   - chat.id == -1002429106148;
   - chat.type == supergroup;
   - exact bot_command entity identifies /ask@WBNP_Media_Bot;
   - sender_chat is ABSENT/null;
   - is_automatic_forward is NOT true;
   - from exists;
   - from.id exists and is integer;
   - from.id != 777000;
   - from.id != 8866633840;
   - from.is_bot != true;
   - event is fresh after this verification boundary.

7. Explicit reject classes:
   - sender_chat present -> REJECT_NON_HUMAN_CHAT_SENDER
   - automatic forward -> REJECT_AUTOMATIC_FORWARD
   - from.id == 777000 -> REJECT_FAKE_SENDER_777000
   - from.is_bot true -> REJECT_BOT_SENDER
   - wrong chat -> REJECT_WRONG_CHAT
   - wrong/not-addressed command -> IGNORE_NOT_TARGET_EVENT

8. On first accepted direct-human event:
   set:
   HUMAN_TESTER_1_CANDIDATE=<numeric from.id>

9. Preserve only minimal evidence:
   - update_id;
   - discussion_chat_id;
   - message_thread_id if present;
   - numeric from.id;
   - sender_chat_present=false;
   - is_automatic_forward=false;
   - from_is_bot=false;
   - trigger_class=EXACT_BOT_COMMAND;
   - owner_is_anonymous=false;
   - generic validation outcome.

10. Do NOT preserve/return:
   - raw message text;
   - username;
   - display name;
   - raw Update JSON;
   - unrelated participants;
   - personal metadata beyond numeric candidate ID and protocol fields above.

11. After candidate established:
   STOP.
   Return candidate to KOO/OPERATOR for explicit confirmation.
   Do NOT infer intended identity from protocol evidence alone.

12. DO NOT:
   - modify allowlist;
   - start/enable dialogue service;
   - call OpenAI;
   - send Telegram messages;
   - mutate Telegram rights/settings;
   - mutate credentials;
   - mutate dialogue DB;
   - replay r0.3 discovery;
   - replay failed live r0.1.

Expected terminal:

PASS_SIS_TELEGRAM_PERSONAL_SENDER_HUMAN_PROVENANCE_VERIFIED_R04

with exact HUMAN_TESTER_1_CANDIDATE,

or exact BLOCKED_/FAIL_ reason.

Mandatory RETURN KOO:
- owner/admin non-anonymous verification;
- minimal direct-human provenance evidence;
- HUMAN_TESTER_1_CANDIDATE;
- service inactive confirmation;
- allowlist unchanged confirmation;
- explicit next condition: OPERATOR confirms candidate identity.

Then STOP.
