# KOO -> SIS: Telegram confirmed tester allowlist correction + final live-gate prep r0.1

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

## Exact protocol provenance PASS

puev5691/wellbeing-hq@8f137e7031b5c4f9e498a3c87996124b49b1320b:
entities/sisadmin/outbox/SIS__telegram-single-instance-human-provenance-verification-r06-result__KOO.md

blob:
6589435077b5351453fef493c5c1080f30371630

terminal:
PASS_SIS_TELEGRAM_SINGLE_INSTANCE_HUMAN_PROVENANCE_R06

Verified candidate:
6384602715

Verified:
- exact discussion chat -1002429106148;
- exact /ask@WBNP_Media_Bot;
- sender_chat absent;
- is_automatic_forward=false;
- from.is_bot=false;
- owner non-anonymous;
- webhook absent;
- allowlist unchanged;
- service inactive/dead/disabled/MainPID=0.

## Exact OPERATOR confirmation

puev5691/wellbeing-hq@aba0ba4bbbda5420233409289e0ae26c040513c3:
entities/koordinator/inbox/SIS__telegram-human-tester-id-operator-confirmation-r01__KOO.md

blob:
478c5d0606ce2cc2a9b483f05524897924a463c5

terminal:
PASS_SIS_OPERATOR_CONFIRMED_TELEGRAM_HUMAN_TESTER_ID_R01

Confirmed intended tester:
6384602715

Known invalid old allowlist value:
777000

## Goal

Prepare the runtime for a separate future bounded live pilot by correcting only the tester allowlist and verifying the final live gate.

DO NOT start the live pilot in this task.

## Task

1. Fresh-verify:
   - current SIS writer;
   - exact provenance result;
   - exact OPERATOR confirmation;
   - no superseding Telegram allowlist/live-gate/live task/result;
   - service currently loaded/inactive/dead/disabled;
   - MainPID=0;
   - no dialogue process running;
   - webhook absent;
   - exact runtime path/config remains the accepted r0.2 installation unless fresh evidence says otherwise.

2. Exact allowlist path:

/etc/wellbeing/telegram-single-entity-pilot/testers.allow

3. Before mutation:
   - read current file safely;
   - verify invalid value 777000 is present as the stale tester value expected from prior state;
   - verify no unexpected unrelated tester IDs are present.
   If unexpected values/state exist:
   STOP with exact blocker.
   Do not normalize or widen allowlist by guess.

4. Perform one atomic replacement so final allowlist contains exactly:

6384602715

and does NOT contain:
777000

No additional tester IDs.

Use safe atomic write/replace semantics preserving required ownership/permissions.

5. Read back exact allowlist after mutation.

Required final state:

ALLOWLIST_COUNT=1
ALLOWLIST_TESTER_ID=6384602715
ALLOWLIST_HAS_777000=NO

6. Verify file safety metadata remains appropriate for runtime use.
   Do not expose secrets.
   Tester ID is non-secret protocol metadata.

7. Re-check runtime safety:

Dialogue service:
- LoadState=loaded
- ActiveState=inactive
- SubState=dead
- UnitFileState=disabled
- MainPID=0

Dialogue process:
ABSENT

Webhook:
WEBHOOK_ACTIVE=NO

Do NOT start or enable service.

8. Final live-gate preparation check only.

Verify without provider/send side effects:
- accepted runtime package still installed;
- exact discussion binding remains -1002429106148;
- bot id remains 8866633840;
- runtime model remains gpt-5.6-luna;
- OpenAI credential file metadata/nonempty state remains present without API call;
- Telegram credential file metadata/nonempty state remains present without sendMessage;
- dialogue DB path exists/accessible as expected;
- no OUTCOME_UNKNOWN precondition is present from prior bounded work if this can be checked read-only;
- no competing dialogue service/process is running.

Do not perform live provider/API generation call.

9. Historical tasks/results are evidence only.

DO NOT replay:
- r0.6;
- r0.5;
- r0.4;
- r0.3;
- failed live r0.1.

10. DO NOT:
- start/enable dialogue service;
- call OpenAI;
- send Telegram message;
- mutate Telegram settings;
- mutate Telegram bot token;
- mutate OpenAI credential;
- mutate dialogue DB contents;
- widen chat/user admission;
- create a second tester;
- issue live authority by implication.

## Expected terminal

PASS_SIS_TELEGRAM_CONFIRMED_TESTER_ALLOWLIST_FINAL_LIVE_GATE_R01

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact pre-mutation allowlist state summary;
- atomic replacement result;
- exact final allowlist readback;
- confirmation 777000 absent;
- confirmation 6384602715 is sole tester;
- ownership/permissions summary;
- service final state inactive/dead/disabled/MainPID=0;
- webhook absent;
- no OpenAI call;
- no sendMessage;
- no dialogue DB content mutation;
- final readiness verdict:
  READY_FOR_SEPARATE_NEW_BOUNDED_LIVE_TASK
  or exact blocker.

Then STOP.

This task does NOT authorize live start.
