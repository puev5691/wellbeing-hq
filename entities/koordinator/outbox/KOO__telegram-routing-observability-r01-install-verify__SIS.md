# KOO -> SIS: Telegram routing observability r0.1 install/verify-only

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

## Exact independent review PASS

puev5691/wellbeing-hq@a6873d9b2fe0200dc2d02a17c20aeb9e52c2efcb:
entities/sisadmin/outbox/SIS__telegram-routing-observability-r01-review-result__KOO.md

blob:
fe98163b93e5bb7266d2d11a01e4a52012b89495

terminal:
PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_REVIEW_READY_FOR_SEPARATE_INSTALL_VERIFY

next:
SEPARATE_NEW_BOUNDED_INSTALL_VERIFY_TASK_REQUIRED

## Exact KOD result

puev5691/wellbeing-hq@b13efdd6fe32a72c4e8a0f58e2a009457b2e329b:
entities/koder/outbox/KOD__telegram-routing-observability-r01-result__KOO.md

blob:
20aa087daec5497007b1cd307c36e17047156723

terminal:
PASS_KOD_TELEGRAM_ROUTING_OBSERVABILITY_R01_CANDIDATE_READY_FOR_SIS_REVIEW

## Exact candidate package

puev5691/wellbeing-hq@7bc9ab9df85a80bedd6717aa38b0478c3c12ecb1:
entities/koder/outbox/telegram-routing-observability-r01/

tree:
bbe40dc80670b33594f997cea52e42508a7ae12b

package identity:
537dd42aacf88c7c5f2ff706ac75b9de836c613f7496f0effacfc66924ecb86c

Exact candidate dialogue_mvp.py SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

## Goal

Install the independently reviewed routing-observability candidate on the live host in a bounded install/verify-only operation while the Telegram dialogue service remains stopped.

This task authorizes:
- exact prestate capture;
- exact candidate code staging;
- atomic code placement;
- reviewed additive SQLite migration;
- read-only diagnostic verification;
- rollback-readiness proof.

This task does NOT authorize:
- service start/enable;
- Telegram calls;
- OpenAI calls;
- credential disclosure;
- allowlist change;
- Telegram settings mutation;
- live pilot.

## A. PRESTATE

Before any mutation verify and record:

1. current SIS writer unchanged;
2. no superseding Telegram observability install/live task/result;
3. service state:
   - LoadState=loaded
   - ActiveState=inactive
   - SubState=dead
   - UnitFileState=disabled
   - MainPID=0
4. dialogue process absent;
5. exact installed predecessor runtime path/code identity;
6. exact config/unit/bootstrap identities;
7. exact allowlist current state;
8. exact dialogue DB path/state;
9. SQLite integrity_check;
10. existing updates/messages/runtime_meta row counts;
11. current updates schema;
12. candidate package exact tree/package identity.

If any required prestate differs unexpectedly:
STOP before mutation with exact blocker.

Create a SQLite-consistent backup/readback of DB prestate while service remains stopped.

Preserve exact predecessor code bytes as rollback source.

No credential content readout.

## B. STAGE

Stage exact candidate dialogue_mvp.py from reviewed package.

Verify:
SHA-256 =
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

Run:
- py_compile on staged bytes;
- no runtime/service start;
- no network.

Do not alter config, bootstrap, unit, allowlist or credentials.

## C. CODE PLACEMENT

Only after prestate/rollback source are proven:

- perform one atomic replacement of the runtime code file with exact reviewed candidate bytes;
- preserve required owner/group/mode;
- fsync/atomic replace as appropriate;
- read back installed SHA-256 and exact byte identity.

No other runtime file mutation unless exact package/install procedure explicitly requires it and it was covered by the independent review.

Config/unit/bootstrap/allowlist/credentials remain unchanged.

## D. DB MIGRATION

With service still stopped:

Invoke only the reviewed additive migration through a bounded local Python/import operation that:
- does not call load_runtime;
- does not call credential();
- does not access network;
- only applies Store._migrate_routing_schema or exact equivalent reviewed entry point.

Required added nullable columns:

- inbound_message_id
- message_thread_id
- direct_topic_id
- trigger_class
- outbound_message_id
- returned_chat_id
- returned_message_thread_id
- returned_direct_topic_id
- returned_is_topic_message

After first migration:
- read back all 9 columns;
- run SQLite integrity_check;
- verify updates/messages/runtime_meta counts/content preservation against prestate;
- verify legacy rows have NULL in new fields where historical evidence did not exist.

Run migration a second time while stopped.

Required:
- schema unchanged;
- data unchanged;
- DB bytes/data state unchanged except permissible SQLite internal metadata if any; if byte identity cannot be guaranteed, use logical/schema/content equivalence and state exact method.

Do not guess historical routing values.

## E. DIAGNOSTIC VERIFY

Run reviewed helper only read-only:

dialogue_mvp.py diagnose-routing --config CONFIG --update-id UPDATE_ID

Use one known legacy committed update.

Verify exact bounded output fields only:

- update_id
- inbound_message_id
- message_thread_id
- direct_topic_id
- trigger_class
- conversation_key
- outbound_message_id
- returned_chat_id
- returned_message_thread_id
- returned_direct_topic_id
- returned_is_topic_message
- state
- error_class

Expected:
legacy routing fields are NULL where evidence never existed.

No credentials/network.

## F. PRIVACY / EFFECT SAFETY

Verify installation did not alter:

- conversation_key semantics;
- admission;
- allowlist;
- provider/model;
- polling;
- systemd unit;
- credential files;
- Telegram settings.

Verify reviewed fail-closed behavior remains represented in installed code:
send success + routing validation/persistence failure
=> OUTCOME_UNKNOWN
=> identical replay does not resend.

Do not simulate with real Telegram/provider.

## G. ROLLBACK READINESS

Prove:
- predecessor code can be atomically restored from preserved exact rollback source;
- predecessor SQL remains compatible with migrated DB containing the 9 nullable columns, based on reviewed package and local stopped-host verification if safe;
- DB backup exists and is readable;
- rollback itself is NOT performed unless the install/verification fails and exact rollback is required to restore pre-task safe state.

If install/migration verification fails after mutation:
restore safe predecessor code and DB prestate as necessary under this task only to return host to pre-task stopped state.
Record exact rollback action.
Do not start service.

## H. FINAL

Required final state:

- installed code = exact observability candidate;
- DB migration verified;
- legacy state preserved;
- service:
  loaded / inactive / dead / disabled / MainPID=0
- dialogue process absent;
- webhook state unchanged/absent as applicable;
- no Telegram call;
- no OpenAI call;
- no service start;
- no persistent enablement;
- no credential mutation;
- no allowlist mutation.

## Expected terminal

PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_INSTALLED_VERIFIED_NO_LIVE

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- prestate summary;
- predecessor code identity;
- candidate package identity;
- installed code SHA-256/readback;
- DB backup locator/identity;
- migration first-run result;
- migration second-run idempotency result;
- 9-column schema readback;
- legacy row/count/integrity preservation;
- diagnose-routing bounded readback;
- privacy/effect-safety verification;
- rollback readiness;
- exact final service state;
- Telegram/OpenAI calls = NONE;
- exact next readiness:
  READY_FOR_SEPARATE_ONE_TURN_ROUTING_PLACEMENT_LIVE_TEST
  or exact blocker.

Then STOP.

No live start is authorized by this task.
