# KOO -> SIS: Telegram discussion admission correction r0.2 independent review + install/verify-only

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

KOD result:
puev5691/wellbeing-hq@89524dd052bce61ed22add8616764142265aa64a:
entities/koder/outbox/KOD__telegram-single-entity-discussion-admission-correction-r01__KOO.md
blob 20063aa431721d702f3ad400b57878809f430d37

terminal:
PASS_KOD_TELEGRAM_SINGLE_ENTITY_DISCUSSION_ADMISSION_CORRECTION_R01_READY_FOR_SIS_REVIEW

Exact successor package:
puev5691/wellbeing-hq@e3360481959f2076fb53e31390bbdb91bec123ab:
entities/koder/outbox/telegram-single-entity-discussion-admission-correction-r02/
tree 1cbb8a521f454f2c1b08f9069d805499a80445bc

Predecessor SIS provisioning PASS:
puev5691/wellbeing-hq@8c28a4c43fda96d5fc4da7a268eac1475b1feba2:
entities/sisadmin/outbox/SIS__telegram-single-entity-mvp-independent-review-provisioning-r01__KOO.md

Target host:
ruvds-xnqc6

Verified Telegram binding:
bot @WBNP_Media_Bot id 8866633840
linked discussion chat_id -1002429106148 type supergroup

Task:

1. Independently read back exact r0.2 package/tree/manifest/checksums.
2. Reproduce 24-test suite, py_compile and systemd-analyze verify.
3. Verify admission semantics:
   - exact discussion chat only;
   - unlisted tester rejected before provider/send;
   - ambient non-addressed group message ignored;
   - reply-to-bot / exact mention / exact /ask trigger;
   - same-thread multi-turn;
   - cross-thread/topic isolation;
   - replay/collision/OUTCOME_UNKNOWN protections.
4. Verify privacy/logging and systemd credential boundaries remain compatible with the previously accepted runtime contour.
5. Verify exact predecessor diff/upgrade path.
6. Prepare and, if exact install/verify authority from current pilot line remains applicable, execute install/verify-only upgrade to versioned r0.2 package path.
7. After installation verify exact hashes/unit/config and service remains inactive/dead/disabled.

Do NOT:
- start or enable service;
- call Telegram;
- call OpenAI;
- read or print secrets;
- alter Telegram rights/settings;
- change Project Sources/canons;
- replay historical Phase1B tasks.

Return immutable result to KOO:
PASS ready for bounded live discussion-pilot gate
or exact blocker.

Include exact installed package identity/path and explicit service inactive state.

Mandatory RETURN KOO.
Then STOP.
