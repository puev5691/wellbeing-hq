# KOO -> SIS: Telegram bot credential replacement r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Exact consumed discovery blocker:
puev5691/wellbeing-hq@560064232e02564dbe60c6cc5190594fbf497799:
entities/sisadmin/outbox/SIS__telegram-discussion-tester-id-discovery-r01-blocker__KOO.md
blob 7bd32d7add1935e0c8fd9983cccf020e24e97769

terminal:
BLOCKED_SIS_TELEGRAM_DISCUSSION_TESTER_ID_DISCOVERY_R01_BOT_TOKEN_REJECTED

Consumed discovery task:
puev5691/wellbeing-hq@6180695711b65aa94e529088937430bfd626796f:
entities/koordinator/outbox/KOO__telegram-discussion-pilot-tester-id-discovery-r01__SIS.md

disposition:
CONSUMED / NON_REPLAYABLE

Verified Telegram bot identity:
@WBNP_Media_Bot
bot id 8866633840

Target host:
ruvds-xnqc6

Protected credential source:
 /etc/wellbeing/telegram-single-entity-pilot/secrets/telegram_bot_token

Goal:
replace only the protected Telegram bot credential with a fresh correct token for @WBNP_Media_Bot through one OPERATOR-assisted local root procedure.

Required procedure:

1. Fresh-verify:
   - current SIS writer;
   - no superseding Telegram credential task/result;
   - dialogue service remains inactive/dead/disabled;
   - target credential path and parent directory identity/mode;
   - no live dialogue process exists.

2. Tell OPERATOR exactly how to obtain a fresh token in Telegram:
   - open verified official @BotFather;
   - request/select @WBNP_Media_Bot;
   - obtain a fresh/current bot API token;
   - if Telegram requires revoking/reissuing the prior token, OPERATOR performs that BotFather action explicitly;
   - token value MUST NOT be pasted into ChatGPT, GitHub, notes, command arguments or logs.

3. Prepare ONE interactive OPERATOR-assisted root shell block that:
   - uses hidden terminal input (no echo);
   - keeps token only in shell memory long enough to write it;
   - uses restrictive umask/temp handling;
   - atomically installs the value into the exact protected credential source;
   - owner root:root;
   - mode 0600;
   - does not print token;
   - does not place token in shell command arguments;
   - unsets shell variable and removes temporary material immediately;
   - prints only non-secret evidence: file exists, owner/group, mode, byte count or non-secret structural confirmation.

4. After OPERATOR runs the block, SIS independently verifies only non-secret local facts:
   - credential file exists;
   - root:root;
   - 0600;
   - non-empty;
   - no token appears in returned output/log evidence;
   - service remains inactive/dead/disabled.

5. Do NOT perform getMe/getWebhookInfo/getUpdates or any Telegram API call in this task.
6. Do NOT start/enable service.
7. Do NOT use OpenAI credential.
8. Do NOT modify tester allowlist.
9. Do NOT modify Telegram channel/chat rights/settings.
10. Do NOT print, hash into public project artifacts, or persist the token value outside the protected credential source.
11. Do NOT replay the consumed discovery task.

Expected result:

PASS_SIS_TELEGRAM_BOT_CREDENTIAL_REPLACED_R01

or exact BLOCKED_/FAIL_ reason.

Mandatory RETURN KOO:
- exact task/result locator;
- non-secret credential-path verification;
- service inactive confirmation;
- explicit statement that a NEW tester-ID discovery task may now be issued.

Then STOP.
