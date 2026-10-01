# KOO -> SIS: Telegram conversation-root r0.1 install/verify readiness

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Current SIS writer

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

terminal:
PASS_SIS_R07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Exact SIS implementation PASS

puev5691/wellbeing-hq@29e3cfca5c5bf6231b0d05d36986404820db231c:
entities/sisadmin/outbox/SIS__telegram-conversation-root-r01-I1-rereview-result__KOO.md

blob:
7a92c9d8779ce6f3cdd4d0b199023abf9cbdbd1a

terminal:
PASS_SIS_TELEGRAM_CONVERSATION_ROOT_R01_I1_CORRECTION_REREVIEW

Verified:
I1_CLOSED=YES
I1_DIFF_CONTAINED=YES
RAW_CARDINALITY_ATOMICITY=PASS
IMPLEMENTATION_STATUS=IMPLEMENTATION_CANDIDATE_NOT_INSTALLED

## Exact corrected implementation package

puev5691/wellbeing-hq@33a85aa2ab8130ef5b41e0dd87fda32fa89c3b4a:
entities/koder/outbox/telegram-conversation-root-r01-implementation-candidate-i1-correction/

tree:
9ccc58d9002bfcd0daeafe48cf6db44bc864934d

package identity:
09a608a2fa24f15f1fb6d26fbf06c3b1715c3a6bb1bb667dec40caf42d13f02f

candidate dialogue_mvp.py SHA-256:
f42cb4c256191738a9068181a628cdee5d877b85d08ff9c3fed780553fee03cf

candidate tests SHA-256:
8a2e5b70ae53b85f892483f00d20d2b319a6e1fed353e7af2ecf79fe4f386771

## Exact currently installed predecessor basis

puev5691/wellbeing-hq@d6d9d0dafde9170b2ee8d7b0b069025e99f76f4e:
entities/sisadmin/outbox/SIS__telegram-routing-observability-r01-install-verify-r02-result__KOO.md

blob:
a81a6cd3590c9f491d34e1a4b732f003c79a9562

terminal:
PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_INSTALLED_VERIFIED_NO_LIVE_R02

Current installed predecessor dialogue_mvp.py SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

Pinned runtime.json raw SHA-256:
57f7e44f70056021fc2ac227b7e4e06e2ef0c886b047139548d83cc5d8f2d7e1

Pinned runtime.json canonical semantic SHA-256:
2ebf58286499a7d7a166d38abf80d2ca6a8a2dfbbe8d5b8a4b16c833a47c40f8

## Goal

Perform READ-ONLY / NON-INSTALL install/verify-readiness analysis for the corrected conversation-root r0.1 implementation package on the current live host.

This task does NOT authorize installation.

Determine whether a future separate exact install/verify task can safely install the candidate and migrate the live DB while the service remains stopped.

## R1. Fresh host prestate

Read-only verify:

- service loaded/inactive/dead/disabled/MainPID=0;
- dialogue process absent;
- exact installed predecessor source SHA;
- exact runtime.json raw and semantic SHA;
- bootstrap/unit identities;
- allowlist identity and tester count;
- webhook state;
- credential metadata only;
- DB path;
- DB integrity;
- current schema;
- updates/messages/runtime_meta counts;
- unresolved/OUTCOME_UNKNOWN inventory;
- current migration/version markers if any.

Do not read credential contents.

If current host state differs from accepted immutable basis, return exact blocker.

## R2. Candidate/package identity

Independently read exact corrected package and verify:

- tree 9ccc58d9002bfcd0daeafe48cf6db44bc864934d;
- package identity 09a608a2fa24f15f1fb6d26fbf06c3b1715c3a6bb1bb667dec40caf42d13f02f;
- source SHA f42cb4c256191738a9068181a628cdee5d877b85d08ff9c3fed780553fee03cf;
- package manifest/checksums;
- exact migration/schema docs.

No package mutation.

## R3. Exact future host delta

Derive exact minimal future install delta.

Expected candidate delta should be limited to:

1. replace runtime dialogue_mvp.py with exact candidate bytes;
2. add only candidate nullable root/lineage columns to updates table as required by package;
3. no runtime.json change;
4. no bootstrap change;
5. no systemd unit change;
6. no allowlist change;
7. no credential change;
8. no Telegram settings change;
9. no persistent service enablement.

List exact columns, types and migration order from package evidence.

Do not perform the delta.

## R4. Live DB migration readiness

Using read-only live DB inspection plus disposable/offline copy if needed, establish whether candidate migration is safe for current live schema.

Check:
- current schema matches expected predecessor;
- no duplicate/constraint condition blocks additive migration;
- all candidate fields can be added nullable;
- legacy rows remain NULL;
- current conversation_key values remain untouched;
- transcript/history rows remain untouched;
- runtime_meta compatibility;
- migration idempotency proven on disposable copy from exact current schema;
- predecessor code SQL remains compatible with migrated schema as rollback prerequisite.

Do not mutate live DB.

## R5. I1 live-data precondition

Because corrected lineage semantics require raw cardinality fail-closed, inspect read-only whether current live DB contains any existing duplicate raw relation:

(returned_chat_id, outbound_message_id)

among rows where outbound_message_id is non-null.

Return:
- duplicate relation count;
- exact bounded identifiers only if needed;
- whether any duplicate would block or merely remain safely ambiguous under candidate semantics.

Do not infer roots/backfill.

No raw dialogue text.

## R6. Rollback readiness

Design exact future rollback prerequisites:

- exact predecessor code rollback bytes/hash;
- SQLite-consistent DB prestate backup before migration;
- DB backup integrity/readback;
- predecessor SQL compatibility with migrated nullable-column schema;
- condition when code-only rollback is safe;
- condition when DB restore is required;
- service remains stopped throughout rollback.

Do not execute rollback now.

## R7. Install procedure readiness

Prepare exact future install/verify sequence only:

A. PRESTATE
B. DB backup
C. stage candidate
D. verify candidate hash/py_compile
E. atomic code replacement
F. stopped-service additive migration
G. first-run readback
H. second-run idempotency
I. local/offline candidate smoke checks with no network
J. rollback proof
K. final service stopped

Do not execute any install step.

## R8. Post-install verification plan

Specify exact evidence a future install task must return:

- installed source SHA;
- migrated schema;
- legacy row preservation;
- root fields NULL on legacy rows;
- duplicate raw relation inventory;
- runtime/config identities unchanged;
- privacy/effect semantics static verification;
- final service inactive/dead/disabled/MainPID=0;
- Telegram/OpenAI calls=0.

No live conversation test in install task.

## R9. Stop conditions

Return BLOCKED if any of:

- host predecessor identity mismatch;
- runtime config mismatch;
- unresolved OUTCOME_UNKNOWN;
- DB integrity failure;
- schema mismatch;
- candidate package identity mismatch;
- migration cannot be proven additive/idempotent on exact current schema;
- rollback evidence insufficient;
- current writer/supersession conflict.

Do not repair in readiness task.

## Boundary

READ-ONLY host inspection only.

Do NOT:
- replace code;
- migrate live DB;
- mutate schema;
- start/enable service;
- call Telegram;
- call OpenAI;
- mutate runtime.json;
- mutate allowlist;
- read/mutate credential contents;
- alter bot/channel/webhook settings;
- replay failed live task.

## Expected terminal

PASS_SIS_TELEGRAM_CONVERSATION_ROOT_R01_INSTALL_VERIFY_READINESS

or exact BLOCKED_/FAIL_.

If PASS state exact next gate:

READY_FOR_SEPARATE_NEW_BOUNDED_INSTALL_VERIFY_TASK

PASS is NOT install authority and NOT live authority.

## Mandatory RETURN KOO

Return:
- exact host prestate;
- exact package identity;
- exact future code/schema delta;
- current duplicate raw relation inventory;
- disposable migration/idempotency proof;
- rollback readiness;
- future install sequence;
- exact stop conditions;
- live mutation=NONE;
- Telegram/OpenAI calls=NONE;
- exact terminal;
- exact next gate.

Then STOP.
