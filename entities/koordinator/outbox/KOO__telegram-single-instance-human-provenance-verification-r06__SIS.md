# KOO -> SIS: Telegram single-instance human provenance verification r0.6

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Exact r0.5 blocker:
puev5691/wellbeing-hq@5c2be5abb10dd4b11fe2d67e29c5704ea9202785:
entities/sisadmin/outbox/SIS__telegram-single-instance-human-provenance-verification-r05-result__KOO.md
blob e001d4e7cc86ef64c471e98001735532989e0cdd

terminal:
BLOCKED_SIS_TELEGRAM_HUMAN_PROVENANCE_R05_NO_FRESH_DIRECT_HUMAN_EVENT

r0.5 disposition:
CONSUMED / NON_REPLAYABLE

Verified r0.5 integrity pattern to preserve:
- exclusive lock acquired before any getUpdates;
- competing observer count = 0;
- unique run/output identity;
- shared output overwrite not used;
- negative offset not used;
- fresh non-negative boundary;
- OWNER_IS_ANONYMOUS=false;
- WEBHOOK_ACTIVE=NO;
- dialogue service inactive/dead/disabled/MainPID=0;
- allowlist unchanged;
- no OpenAI/sendMessage/dialogue DB mutation.

Verified Telegram binding:
bot @WBNP_Media_Bot
bot_id 8866633840
discussion_chat_id -1002429106148
chat_type supergroup

Known invalid fake sender:
777000
MUST NOT be accepted.

Goal:
establish one protocol-level direct-human sender event under one exclusive bounded observer, synchronized with OPERATOR action while the observation window is active.

Task:

1. Fresh-verify:
   - current SIS writer;
   - exact r0.5 result identity;
   - no superseding Telegram provenance/discovery/live task/result;
   - service remains loaded/inactive/dead/disabled;
   - MainPID=0;
   - no dialogue process running;
   - allowlist remains unchanged.

2. Before ANY getUpdates:
   - acquire one exclusive single-instance lock;
   - verify competing observer count = 0;
   - verify no other getUpdates consumer/helper is active;
   - create unique RUN_ID;
   - create unique output path for this exact run;
   - do not reuse r0.5 files/output/lock identity.

3. Read-only verify:
   - OWNER_IS_ANONYMOUS=false;
   - WEBHOOK_ACTIVE=NO.
   If either fails, STOP with exact blocker.

4. Establish fresh non-negative update boundary:
   - do not use negative offset;
   - determine current pending-message boundary without consuming/forgetting pre-boundary history ambiguously;
   - set exact next non-negative offset for this run;
   - record only minimal non-secret boundary evidence.

5. Start exactly one bounded observation process under the acquired lock.

6. Only AFTER the observer is confirmed active, emit to OPERATOR in chat/terminal exactly:

   OBSERVATION_READY=YES

   and also:
   RUN_ID=<non-secret run id>
   SEND_NOW=/ask@WBNP_Media_Bot

   This is a synchronization signal, not a success result.

7. After OBSERVATION_READY=YES, OPERATOR will immediately send one fresh exact command from the personal sender identity:

   /ask@WBNP_Media_Bot

8. Keep the bounded observation window active long enough for normal human UI action and Telegram delivery after OBSERVATION_READY.
   Do not close immediately after printing readiness.
   Use one continuous observer only.
   No second launcher invocation.

9. Accept HUMAN_TESTER_1_CANDIDATE only when ALL are true:
   - update type = message;
   - update is after the fresh r0.6 boundary;
   - chat.id == -1002429106148;
   - chat.type == supergroup;
   - exact bot_command entity matches /ask@WBNP_Media_Bot;
   - sender_chat absent/null;
   - is_automatic_forward != true;
   - from exists;
   - from.id is integer;
   - from.id != 777000;
   - from.id != 8866633840;
   - from.is_bot != true.

10. Reject classes:
   - sender_chat present -> REJECT_NON_HUMAN_CHAT_SENDER
   - automatic forward -> REJECT_AUTOMATIC_FORWARD
   - from.id == 777000 -> REJECT_FAKE_SENDER_777000
   - from.is_bot true -> REJECT_BOT_SENDER
   - wrong chat -> REJECT_WRONG_CHAT
   - wrong/not-addressed command -> IGNORE_NOT_TARGET_EVENT
   - pre-boundary update -> REJECT_PREBOUNDARY_EVENT

11. On first accepted event:
   set:
   HUMAN_TESTER_1_CANDIDATE=<numeric from.id>

   then STOP observation immediately and preserve minimal evidence.

12. Minimal evidence only:
   - RUN_ID;
   - update_id;
   - discussion_chat_id;
   - message_thread_id if present;
   - numeric from.id;
   - sender_chat_present=false;
   - is_automatic_forward=false;
   - from_is_bot=false;
   - trigger_class=EXACT_BOT_COMMAND;
   - OWNER_IS_ANONYMOUS=false;
   - WEBHOOK_ACTIVE=NO;
   - lock/exclusivity status;
   - generic accept/reject counters.

13. Do NOT preserve/return:
   - raw message text;
   - username;
   - display name;
   - raw Update JSON;
   - unrelated participant data.

14. On bounded timeout with no accepted event:
   return exact blocker:
   BLOCKED_SIS_TELEGRAM_HUMAN_PROVENANCE_R06_NO_FRESH_DIRECT_HUMAN_EVENT
   Do not use any later event outside the active window.

15. After candidate established:
   STOP.
   Return candidate to KOO/OPERATOR for explicit identity confirmation.
   Do NOT modify allowlist.

16. DO NOT:
   - replay r0.5;
   - replay r0.4/r0.3;
   - replay failed live r0.1;
   - modify allowlist;
   - start/enable dialogue service;
   - call OpenAI;
   - send Telegram messages;
   - modify Telegram rights/settings;
   - modify credentials;
   - mutate dialogue DB.

Expected terminal:

PASS_SIS_TELEGRAM_SINGLE_INSTANCE_HUMAN_PROVENANCE_R06

with exact HUMAN_TESTER_1_CANDIDATE,

or exact BLOCKED_/FAIL_ reason.

Mandatory RETURN KOO:
- RUN_ID;
- owner non-anonymous PASS;
- webhook absent PASS;
- lock/exclusivity PASS;
- unique output PASS;
- fresh non-negative boundary PASS;
- minimal direct-human provenance evidence;
- HUMAN_TESTER_1_CANDIDATE;
- service inactive confirmation;
- allowlist unchanged confirmation;
- explicit next condition: OPERATOR confirms candidate identity.

Then STOP.
