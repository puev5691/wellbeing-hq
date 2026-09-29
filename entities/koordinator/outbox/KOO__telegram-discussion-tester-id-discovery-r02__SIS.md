# KOO -> SIS: Telegram discussion tester-ID discovery r0.2

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Exact credential replacement PASS:
puev5691/wellbeing-hq@457a39e62354640f0f8de1b5cd2938de2eeabf93:
entities/sisadmin/outbox/SIS__telegram-bot-credential-replacement-r01__KOO.md
blob 504145dac855976aac6d7fba9b9a8a567ffc6db3
terminal PASS_SIS_TELEGRAM_BOT_CREDENTIAL_REPLACED_R01

Consumed predecessor discovery:
puev5691/wellbeing-hq@6180695711b65aa94e529088937430bfd626796f:
entities/koordinator/outbox/KOO__telegram-discussion-pilot-tester-id-discovery-r01__SIS.md

Exact predecessor blocker:
puev5691/wellbeing-hq@560064232e02564dbe60c6cc5190594fbf497799:
entities/sisadmin/outbox/SIS__telegram-discussion-tester-id-discovery-r01-blocker__KOO.md

Predecessor disposition:
CONSUMED / NON_REPLAYABLE

Verified Telegram binding:
bot @WBNP_Media_Bot
bot_id 8866633840
discussion_chat_id -1002429106148
chat_type supergroup

Installed dialogue service:
wellbeing-telegram-single-entity-pilot.service

Task:

1. Fresh-verify:
   - current SIS writer;
   - exact task/result lineage;
   - no superseding Telegram task/result;
   - service remains loaded/inactive/dead/disabled;
   - no dialogue process is running;
   - protected Telegram bot credential exists under the verified local path.

2. Perform exactly one read-only Telegram getWebhookInfo using the protected credential.
3. If webhook is active:
   STOP.
   Return exact blocker:
   BLOCKED_SIS_TELEGRAM_DISCUSSION_TESTER_ID_DISCOVERY_R02_WEBHOOK_ACTIVE
   Include only non-secret webhook metadata needed for the next decision.
   Do NOT remove webhook in this task.

4. If webhook is absent:
   perform bounded getUpdates discovery only.

5. Discovery target:
   exact command
   /ask@WBNP_Media_Bot

   in exact discussion:
   chat.id = -1002429106148
   chat.type = supergroup

6. Candidate acceptance requires:
   - exact addressed command match;
   - message.from.id is integer;
   - sender is not bot id 8866633840.

7. First exact matching sender after task activation becomes:
   TESTER_1_CANDIDATE.

8. Return minimal evidence only:
   - update_id;
   - discussion chat_id;
   - numeric tester from.id;
   - trigger class;
   - generic success/failure metadata.

9. Do NOT persist or return:
   - raw message text;
   - username;
   - display name;
   - raw Update JSON;
   - unrelated participant/member data.

10. Do NOT modify tester allowlist.
11. Do NOT start/enable dialogue service.
12. Do NOT send Telegram messages.
13. Do NOT call OpenAI.
14. Do NOT touch OpenAI credential.
15. Do NOT change Telegram rights/settings.
16. Do NOT replay predecessor discovery task.

Expected result:

PASS_SIS_TELEGRAM_DISCUSSION_TESTER_ID_DISCOVERED_R02

with exact TESTER_1_CANDIDATE numeric ID,

or exact BLOCKED_/FAIL_ reason.

Mandatory RETURN KOO.
Then STOP.
