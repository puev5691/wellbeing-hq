# KOO -> SIS: Telegram routing observability r0.1 install/verify successor r0.2

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

## Exact config reconciliation PASS

puev5691/wellbeing-hq@56689df99aa00761ec4a4fdd38caa756379cca5e:
entities/sisadmin/outbox/SIS__telegram-live-runtime-config-identity-reconciliation-r01-result__KOO.md

blob:
8f8e57e8d8944de7f440052de1b02c94bf97afe4

terminal:
PASS_SIS_TELEGRAM_LIVE_RUNTIME_CONFIG_IDENTITY_RECONCILIATION_R01

decision:
ACCEPT_CURRENT_LIVE_CONFIG_IDENTITY

Accepted live runtime.json:

path:
/etc/wellbeing/telegram-single-entity-pilot/runtime.json

raw SHA-256:
57f7e44f70056021fc2ac227b7e4e06e2ef0c886b047139548d83cc5d8f2d7e1

canonical semantic SHA-256:
2ebf58286499a7d7a166d38abf80d2ca6a8a2dfbbe8d5b8a4b16c833a47c40f8

classification:
FORMAT_ONLY

material semantic delta:
NO

current status:
ACCEPTED_LIVE_CONFIG_IDENTITY_PINNED_BY_THIS_RECONCILIATION

next:
READY_FOR_NEW_ROUTING_OBSERVABILITY_INSTALL_VERIFY

## Exact previous blocked install result

puev5691/wellbeing-hq@1ce88ff9f5aa25fe6a10f8c33eb52c671e86371c:
entities/sisadmin/outbox/SIS__telegram-routing-observability-r01-install-verify-result__KOO.md

blob:
f6586bcfbfe8ba6f45c631b25772d483318778cf

terminal:
BLOCKED_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_STATIC_RUNTIME_IDENTITY_MISMATCH

Disposition:
historical blocked attempt only.
DO NOT replay it.

Verified from blocked attempt:
- no code mutation;
- no DB mutation;
- no config mutation;
- no allowlist mutation;
- no credential mutation;
- no service start;
- no Telegram/OpenAI calls.

## Exact independent review PASS

puev5691/wellbeing-hq@a6873d9b2fe0200dc2d02a17c20aeb9e52c2efcb:
entities/sisadmin/outbox/SIS__telegram-routing-observability-r01-review-result__KOO.md

blob:
fe98163b93e5bb7266d2d11a01e4a52012b89495

terminal:
PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_REVIEW_READY_FOR_SEPARATE_INSTALL_VERIFY

## Exact candidate package

puev5691/wellbeing-hq@7bc9ab9df85a80bedd6717aa38b0478c3c12ecb1:
entities/koder/outbox/telegram-routing-observability-r01/

tree:
bbe40dc80670b33594f997cea52e42508a7ae12b

package identity:
537dd42aacf88c7c5f2ff706ac75b9de836c613f7496f0effacfc66924ecb86c

candidate dialogue_mvp.py SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

## Goal

Perform a NEW bounded install/verify-only installation of the reviewed routing-observability candidate using the now-pinned accepted live runtime.json identity.

This task authorizes only:
- stopped-service prestate capture;
- SQLite-consistent DB backup/readback;
- exact candidate code staging;
- atomic code replacement;
- reviewed additive DB migration;
- bounded read-only diagnostic verification;
- rollback-readiness proof.

This task does NOT authorize:
- service start/enable;
- Telegram calls;
- OpenAI calls;
- live pilot;
- runtime.json mutation;
- allowlist mutation;
- credential mutation;
- bot/channel/webhook settings mutation.

## A. PRESTATE

Fresh-verify before mutation:

1. current SIS writer unchanged;
2. no superseding Telegram install/live task/result;
3. service:
   loaded / inactive / dead / disabled / MainPID=0;
4. dialogue process absent;
5. current runtime.json exact raw SHA-256 equals:
   57f7e44f70056021fc2ac227b7e4e06e2ef0c886b047139548d83cc5d8f2d7e1
6. current runtime.json canonical semantic SHA-256 equals:
   2ebf58286499a7d7a166d38abf80d2ca6a8a2dfbbe8d5b8a4b16c833a47c40f8
7. runtime.json semantic diff from reviewed reference remains zero;
8. predecessor dialogue_mvp.py exact installed identity matches accepted predecessor;
9. bootstrap/systemd unit identities match accepted r0.2;
10. exact allowlist current state unchanged;
11. DB path/state readable;
12. SQLite integrity_check PASS;
13. record existing updates/messages/runtime_meta counts and schema;
14. candidate package/tree/package identity exact.

If any required prestate mismatch occurs:
STOP before mutation.
Do not normalize/fix by guess.

Create:
- SQLite-consistent prestate DB backup/readback while service remains stopped;
- exact predecessor code rollback copy/identity.

Do not read credential contents.

## B. STAGE

Stage exact candidate dialogue_mvp.py from reviewed package.

Verify candidate SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

Run:
- py_compile on staged bytes;
- no network;
- no service start.

Do not alter:
- runtime.json;
- config semantics;
- bootstrap;
- unit;
- allowlist;
- credentials.

## C. ATOMIC CODE PLACEMENT

After prestate + rollback evidence PASS:

- perform one atomic replacement of runtime dialogue_mvp.py with exact candidate bytes;
- preserve required owner/group/mode;
- fsync/atomic replace as applicable;
- read back exact installed SHA-256;
- prove installed bytes equal reviewed candidate.

No other runtime file mutation.

## D. DB MIGRATION

With service stopped:

Invoke only the reviewed additive migration entry point, without:
- load_runtime side effects;
- credential reads;
- network.

Add only nullable columns:

- inbound_message_id
- message_thread_id
- direct_topic_id
- trigger_class
- outbound_message_id
- returned_chat_id
- returned_message_thread_id
- returned_direct_topic_id
- returned_is_topic_message

First run verification:
- all 9 columns present;
- integrity_check PASS;
- pre-existing updates/messages/runtime_meta preserved;
- row counts preserved;
- legacy new fields NULL where historical evidence absent.

Second migration run:
- schema unchanged;
- logical data unchanged;
- idempotency PASS.

If byte-for-byte SQLite file identity changes because of internal metadata, compare exact logical/schema/content invariants and state method.

Do not infer/backfill historical routing values.

## E. READ-ONLY DIAGNOSTIC

Run:

dialogue_mvp.py diagnose-routing --config /etc/wellbeing/telegram-single-entity-pilot/runtime.json --update-id <known legacy committed update>

Verify output contains only:

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

Legacy routing fields expected NULL where never persisted.

No credential/network access.

## F. SAFETY/COMPATIBILITY

Verify after install:

- pinned runtime.json raw SHA unchanged;
- pinned canonical semantic SHA unchanged;
- conversation_key semantics unchanged;
- admission unchanged;
- discussion chat unchanged;
- bot id/username unchanged;
- model remains gpt-5.6-luna;
- provider remains OpenAI by accepted code contract;
- polling behavior unchanged;
- allowlist unchanged;
- bootstrap unchanged;
- systemd unit unchanged;
- credentials unchanged by metadata;
- no webhook mode introduced;
- privacy/retention semantics unchanged.

Verify installed code still contains reviewed fail-closed semantics:
send success + route validation/persistence failure
=> OUTCOME_UNKNOWN
=> replay requires reconciliation and no duplicate resend.

No real provider/send simulation.

## G. ROLLBACK READINESS

Prove:
- exact predecessor code can be atomically restored;
- migrated DB remains predecessor-SQL compatible with the nine nullable columns;
- DB backup is readable;
- if install/migration verification fails after mutation, restore safe pre-task stopped state as necessary under this task and report exact rollback.

Do not start service after rollback or PASS.

## H. FINAL STATE

Required if PASS:

installed code SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

runtime.json raw SHA-256:
57f7e44f70056021fc2ac227b7e4e06e2ef0c886b047139548d83cc5d8f2d7e1

runtime.json semantic SHA-256:
2ebf58286499a7d7a166d38abf80d2ca6a8a2dfbbe8d5b8a4b16c833a47c40f8

service:
loaded / inactive / dead / disabled / MainPID=0

dialogue process:
ABSENT

Telegram calls:
NONE

OpenAI calls:
NONE

service start:
NONE

runtime.json mutation:
NONE

allowlist mutation:
NONE

credential mutation:
NONE

## Expected terminal

PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_INSTALLED_VERIFIED_NO_LIVE_R02

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact prestate;
- pinned config identity verification;
- predecessor code identity;
- candidate package identity;
- installed code readback;
- DB backup locator/identity;
- first migration result;
- second-run idempotency result;
- 9-column schema;
- legacy preservation evidence;
- diagnose-routing result;
- privacy/effect-safety verification;
- rollback readiness;
- final service state;
- Telegram/OpenAI calls NONE;
- next readiness:
  READY_FOR_SEPARATE_ONE_TURN_ROUTING_PLACEMENT_LIVE_TEST
  or exact blocker.

Then STOP.

No live/service start is authorized by this task.
