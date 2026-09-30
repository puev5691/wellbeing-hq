# KOO -> SIS: Telegram single-instance human provenance verification r0.5

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Exact failed r0.4 result:
puev5691/wellbeing-hq@b8eb0040c62e439e669f63b383fb63b50c2e265d:
entities/sisadmin/outbox/SIS__telegram-personal-sender-human-provenance-verification-r04-result__KOO.md
blob c2823841d47942e8df71c85d38baf9fa3625b788

terminal:
FAIL_SIS_TELEGRAM_PERSONAL_SENDER_HUMAN_PROVENANCE_VERIFICATION_R04_CONCURRENT_OBSERVER_INTEGRITY_LOST

r0.4 disposition:
FAILED / CONSUMED / NON_REPLAYABLE

Verified safe state from r0.4:
OWNER_CREATOR_COUNT=1
OWNER_ANONYMOUS_COUNT=0
OWNER_IS_ANONYMOUS=false
WEBHOOK_ACTIVE=NO
service loaded/inactive/dead/disabled
MainPID=0
dialogue process absent
allowlist unchanged
OpenAI/sendMessage/Telegram settings/credentials/dialogue DB unchanged

Verified Telegram binding:
bot @WBNP_Media_Bot
bot_id 8866633840
discussion_chat_id -1002429106148
chat_type supergroup

Known invalid fake sender:
777000
MUST NOT be accepted.

Goal:
perform one clean, single-instance, bounded protocol-level human provenance verification and discover one exact HUMAN_TESTER_1_CANDIDATE.

Execution-integrity requirements:

1. Before ANY getUpdates call, acquire one exclusive single-instance lock dedicated to this exact verification contour.
   Example implementation may use flock on a fixed lock file under a protected local runtime/temp location.

2. If lock acquisition fails because another observer is active:
   STOP immediately with:
   BLOCKED_SIS_TELEGRAM_HUMAN_PROVENANCE_R05_OBSERVER_ALREADY_ACTIVE
   Do not call getUpdates.

3. After lock acquisition, verify no other known verification/getUpdates observer process for this exact bot/contour is active.
   If one exists:
   STOP with exact blocker.
   Do not kill it automatically under this task.

4. Use a unique output path bound to this exact execution.
   Requirements:
   - no shared reusable output path;
   - no unlink/replacement of another execution's output;
   - output survives helper exit until SIS reads it;
   - execution identifier/path recorded without secret data.

5. Establish one fresh non-negative Telegram message-update boundary AFTER lock acquisition and observer exclusivity is proven.
   Negative offset baseline such as offset=-1 is NOT permitted for this successor.

6. Recheck read-only:
   - owner creator count = 1;
   - OWNER_IS_ANONYMOUS=false;
   - webhook absent;
   - service loaded/inactive/dead/disabled;
   - MainPID=0;
   - dialogue process absent.

If owner becomes anonymous again:
STOP with exact blocker.

If webhook active:
STOP with exact blocker.
Do not remove it.

Human provenance observation:

7. After observation boundary is READY, OPERATOR may send exactly one fresh:
   /ask@WBNP_Media_Bot
   from personal sender identity in the exact linked discussion.

8. Accept HUMAN_TESTER_1_CANDIDATE ONLY when ALL are true:
   - update type = message;
   - update_id > exact fresh boundary;
   - chat.id == -1002429106148;
   - chat.type == supergroup;
   - exact bot_command entity matches /ask@WBNP_Media_Bot;
   - sender_chat absent/null;
   - is_automatic_forward != true;
   - from exists;
   - from.id exists and integer;
   - from.id != 777000;
   - from.id != 8866633840;
   - from.is_bot != true.

9. Explicit reject classes:
   - sender_chat present -> REJECT_NON_HUMAN_CHAT_SENDER
   - automatic forward -> REJECT_AUTOMATIC_FORWARD
   - from.id == 777000 -> REJECT_FAKE_SENDER_777000
   - from.is_bot true -> REJECT_BOT_SENDER
   - wrong chat -> REJECT_WRONG_CHAT
   - wrong/not-addressed command -> IGNORE_NOT_TARGET_EVENT
   - stale update_id <= boundary -> REJECT_PREBOUNDARY_EVENT

10. First accepted direct-human event becomes:
    HUMAN_TESTER_1_CANDIDATE=<numeric from.id>

Minimal evidence only:
- unique execution id/output path identifier;
- lock acquired = yes;
- competing observer = none;
- fresh non-negative boundary update_id;
- accepted update_id;
- discussion_chat_id;
- message_thread_id if present;
- numeric from.id;
- sender_chat_present=false;
- is_automatic_forward=false;
- from_is_bot=false;
- trigger_class=EXACT_BOT_COMMAND;
- owner_is_anonymous=false;
- rejection counters/classes;
- generic terminal outcome.

Do NOT preserve/return:
- raw message text;
- username;
- display name;
- raw Update JSON;
- unrelated participants;
- secrets;
- arbitrary personal metadata.

After candidate:
STOP.
Return candidate to KOO/OPERATOR for explicit confirmation.
Do NOT update allowlist in this task.

Do NOT:
- modify allowlist;
- start/enable dialogue service;
- call OpenAI;
- send Telegram messages;
- change Telegram rights/settings;
- mutate credentials;
- mutate dialogue DB;
- replay r0.4;
- replay r0.3;
- replay failed live r0.1.

Expected terminal:

PASS_SIS_TELEGRAM_SINGLE_INSTANCE_HUMAN_PROVENANCE_VERIFIED_R05

with exact HUMAN_TESTER_1_CANDIDATE,

or exact BLOCKED_/FAIL_ reason.

Mandatory RETURN KOO:
- lock/exclusivity evidence;
- unique output evidence;
- fresh non-negative boundary;
- owner/webhook/service checks;
- minimal direct-human provenance evidence;
- HUMAN_TESTER_1_CANDIDATE;
- service inactive confirmation;
- allowlist unchanged confirmation;
- explicit next condition: OPERATOR confirms candidate identity.

Then STOP.
