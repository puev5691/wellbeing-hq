# KOO -> SIS: Telegram discussion pilot allowlist + final live-gate preparation r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Exact tester discovery PASS:
puev5691/wellbeing-hq@fbbcb48ca30488bb8060744194b5d460a8984bf9:
entities/sisadmin/outbox/SIS__telegram-discussion-tester-id-discovery-r02__KOO.md
blob d2136e52a8a167fca7527dedff16e8b3b25cc951
terminal PASS_SIS_TELEGRAM_DISCUSSION_TESTER_ID_DISCOVERED_R02

Exact OPERATOR confirmation:
TESTER_1_CANDIDATE=777000
IS_INTENDED_FIRST_TESTER=YES

Verified Telegram state:
bot @WBNP_Media_Bot
bot_id 8866633840
discussion_chat_id -1002429106148
chat_type supergroup
WEBHOOK_ACTIVE=NO

Installed package PASS:
puev5691/wellbeing-hq@59455e46db80c490e740ce96fa3834348576506c:
entities/sisadmin/outbox/SIS__telegram-discussion-admission-r02-independent-review-install-verify__KOO.md
blob 3ed6d57f020f526f6c383e62c71498050c48bcd3
terminal PASS_SIS_TELEGRAM_DISCUSSION_ADMISSION_R02_READY_FOR_BOUNDED_LIVE_DISCUSSION_PILOT_GATE

Installed code:
/opt/wellbeing/telegram-single-entity-mvp-r02

Service:
wellbeing-telegram-single-entity-pilot.service

Allowlist:
/etc/wellbeing/telegram-single-entity-pilot/testers.allow

Telegram credential:
/etc/wellbeing/telegram-single-entity-pilot/secrets/telegram_bot_token

OpenAI credential:
/etc/wellbeing/telegram-single-entity-pilot/secrets/openai_api_key

Task:

1. Fresh-verify:
   - current SIS writer;
   - exact discovery/install/result lineage;
   - no superseding Telegram task/result;
   - service remains loaded/inactive/dead/disabled;
   - MainPID=0;
   - webhook evidence remains the current discovery fact for this prep step;
   - installed r0.2 package/config/unit identities remain unchanged.

2. Write the exact closed-pilot tester allowlist:
   - exactly one numeric tester ID: 777000;
   - no username/display-name;
   - root-controlled file at exact allowlist path;
   - owner root:wellbeing-tg-dialog;
   - mode 0640;
   - atomic replacement;
   - readback proves exactly one allowed numeric ID.

3. Verify Telegram credential slot non-secret facts only:
   - file exists;
   - root:root;
   - 0600;
   - non-empty.
   Do not print/read token value.

4. Verify OpenAI credential slot non-secret facts only.
   If absent/empty:
   - prepare ONE OPERATOR-assisted hidden-input root block to populate it;
   - token/key value must never be pasted to ChatGPT/GitHub, echoed, logged, or placed in command arguments;
   - install root:root 0600 atomically;
   - clear temporary variables/material;
   - print only non-secret owner/mode/non-empty evidence.
   If already valid, do not replace it unnecessarily.

5. Run local/offline final config admission checks only:
   - config parses;
   - exact discussion chat binding;
   - allowlist contains 777000 only;
   - credential files referenced correctly by systemd LoadCredential;
   - service unit points to r0.2 package;
   - state path writable only as designed;
   - no public listener.

6. Prepare final bounded live-activation evidence/checklist using these fixed pilot limits:
   - tester IDs: [777000];
   - accepted user turns max: 50;
   - provider calls max: 50;
   - live window max: 2 hours from observed successful service start;
   - nominal cost ceiling: USD 5;
   - provider: OpenAI only;
   - Telegram transport: long polling;
   - no tools/project mutation;
   - exact discussion chat only;
   - addressed triggers only: reply-to-bot / exact mention / exact /ask command.

Cost rule:
if exact monetary spend cannot be observed live, provider_calls_max=50 plus package output-token bound is the hard technical cap; do not invent spend evidence.

7. Preserve accepted data-handling boundary:
   - admitted dialogue text goes to OpenAI;
   - bounded visible transcript retained locally;
   - raw Telegram Update JSON not persisted;
   - usernames/display names not persisted;
   - secrets not logged/persisted;
   - tester has accepted this bounded transcript policy via OPERATOR decision.

8. Define final live success criteria:
   - tester 777000 gets at least two consecutive same-thread replies;
   - coherent multi-turn context;
   - non-addressed ambient group text ignored;
   - foreign/unlisted user causes no provider call;
   - replay causes no duplicate provider/send effect;
   - controlled provider failure yields visible fallback;
   - no secret/raw-message leakage in operational logs;
   - service can be stopped cleanly.

9. Final STOP conditions for future live task:
   - secret exposure/suspected secret logging;
   - provider effect for unlisted user;
   - cross-thread/chat context contamination;
   - replay collision / OUTCOME_UNKNOWN requiring reconciliation;
   - three consecutive provider/runtime failures;
   - 50 provider calls reached;
   - 2-hour window reached;
   - operator STOP;
   - unexpected project mutation;
   - need to widen scope.

10. DO NOT in this task:
   - start or enable service;
   - call Telegram API;
   - call OpenAI API;
   - send Telegram message;
   - change Telegram rights/settings;
   - modify project Sources/canons;
   - replay any consumed discovery task.

Expected result:

PASS_SIS_TELEGRAM_DISCUSSION_PILOT_R01_FINAL_LIVE_GATE_READY

or exact BLOCKED_/FAIL_ reason.

Mandatory RETURN KOO:
- allowlist exact readback;
- non-secret credential readiness;
- config/unit/package readiness;
- service inactive/dead/disabled confirmation;
- final live limits and stop conditions;
- statement whether KOO may issue NEW exact bounded live-activation task.

Then STOP.
