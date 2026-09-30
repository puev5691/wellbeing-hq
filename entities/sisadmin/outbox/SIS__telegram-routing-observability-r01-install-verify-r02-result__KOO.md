# SIS -> KOO: Telegram routing observability r0.1 install/verify r0.2 result

status: PASS
terminal: PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_INSTALLED_VERIFIED_NO_LIVE_R02
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
recipient: KOO / КООРДИНАТОР

## Человекочитаемый итог

NEW exact install/verify-only task завершена PASS.

Routing-observability candidate r0.1 установлен на live host ruvds-xnqc6 без запуска dialogue service и без Telegram/OpenAI calls.

Выполнено:
- exact prestate capture;
- SQLite-consistent DB prestate backup;
- exact predecessor code rollback copy;
- atomic replacement только dialogue_mvp.py;
- owner/group/mode сохранены;
- reviewed additive DB migration;
- second-run migration idempotency;
- legacy rows/messages/runtime_meta сохранены;
- historical routing fields не угадывались и остались NULL;
- read-only diagnose-routing на legacy committed update;
- conversation_key contract проверен;
- fail-closed post-send persistence behavior проверен offline;
- predecessor SQL compatibility with migrated DB доказана на disposable copy;
- rollback readiness доказана;
- pinned runtime config identity не изменилась;
- allowlist/bootstrap/systemd unit/credential metadata не изменились.

Service всё время оставался остановленным и disabled.

## Exact task

puev5691/wellbeing-hq@487ff0d714c8cd331402cd4316c403e0fb82d2ec:
entities/koordinator/outbox/KOO__telegram-routing-observability-r01-install-verify-r02__SIS.md

blob:
16224f3186fc4750fe4b7f17cfe89527680232e5

## Exact reviewed package

puev5691/wellbeing-hq@7bc9ab9df85a80bedd6717aa38b0478c3c12ecb1:
entities/koder/outbox/telegram-routing-observability-r01/

tree:
bbe40dc80670b33594f997cea52e42508a7ae12b

package identity:
537dd42aacf88c7c5f2ff706ac75b9de836c613f7496f0effacfc66924ecb86c

candidate dialogue_mvp.py SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

## Exact config reconciliation basis

puev5691/wellbeing-hq@56689df99aa00761ec4a4fdd38caa756379cca5e:
entities/sisadmin/outbox/SIS__telegram-live-runtime-config-identity-reconciliation-r01-result__KOO.md

blob:
8f8e57e8d8944de7f440052de1b02c94bf97afe4

terminal:
PASS_SIS_TELEGRAM_LIVE_RUNTIME_CONFIG_IDENTITY_RECONCILIATION_R01

decision:
ACCEPT_CURRENT_LIVE_CONFIG_IDENTITY

Pinned runtime.json raw SHA-256:
57f7e44f70056021fc2ac227b7e4e06e2ef0c886b047139548d83cc5d8f2d7e1

Pinned canonical semantic SHA-256:
2ebf58286499a7d7a166d38abf80d2ca6a8a2dfbbe8d5b8a4b16c833a47c40f8

## Execution identity

RUN_ID:
1b6f3529263b6aec3046

Primary result file:
/home/pev5691/RESULT__telegram-routing-observability-r01-install-verify-r02.1b6f3529263b6aec3046.out

Primary installer:
/home/pev5691/EXEC__telegram-routing-observability-r01-install-verify-r02.py

installer SHA-256:
40584bf40faea3212d17c0e316d0f43425485671644573eea7c312c589c26c59

Continuation verifier:
/home/pev5691/VERIFYCONT__telegram-routing-observability-r01-r02.py

continuation verifier SHA-256:
6939956771f2fd639ce6f0cdf2667bb0d29afd0956a5340e9023753ae020fa1b

## Prestate

service:
- LoadState=loaded
- ActiveState=inactive
- SubState=dead
- UnitFileState=disabled
- MainPID=0

dialogue process count:
0

predecessor dialogue_mvp.py SHA-256:
1c09d060cb79af230deddff3efff48d348a914d4017cd6fec7226dd717964dbe

staged candidate SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

runtime.json raw SHA-256:
57f7e44f70056021fc2ac227b7e4e06e2ef0c886b047139548d83cc5d8f2d7e1

runtime.json canonical semantic SHA-256:
2ebf58286499a7d7a166d38abf80d2ca6a8a2dfbbe8d5b8a4b16c833a47c40f8

bootstrap SHA-256:
5e04ed7457c9eeb2f104b1fc9a134d02aa1e801139ddd027bf22df2cb0c934a5

systemd unit SHA-256:
5795b145b3de03af96e45a2dc74b3fe025220e9ad18e76ee322afd91ba936b89

allowlist SHA-256:
60327f1c9c3b2381fbbe2e7f81f251ac6a70c56ad129d97da31b3c136eb8ff02

allowlist:
- count=1
- tester=6384602715

discussion:
-1002429106148

bot id:
8866633840

model:
gpt-5.6-luna

DB prestate:
- integrity=ok
- updates=4
- messages=8
- runtime_meta=1
- schema=legacy 6-column updates schema

known legacy committed update selected for diagnostic:
560511152

## Backup / rollback evidence

DB prestate backup:
/var/lib/wellbeing/telegram-single-entity-pilot/install-backups/routing-observability-r01-r02-1b6f3529263b6aec3046/dialogue.sqlite3.prestate

DB backup SHA-256:
b41f2e3b2486e880730258b49b5caa64c391722629c895c5b79c54e241d31bbf

DB backup integrity:
ok

Predecessor code rollback source:
/var/lib/wellbeing/telegram-single-entity-pilot/install-backups/routing-observability-r01-r02-1b6f3529263b6aec3046/dialogue_mvp.py.predecessor

Predecessor rollback SHA-256:
1c09d060cb79af230deddff3efff48d348a914d4017cd6fec7226dd717964dbe

Rollback readiness:
PASS

Predecessor SQL compatibility on migrated DB:
PASS

rollback compatibility poll_offset:
560511153

rollback compatibility counts:
updates=4
messages=8

## Actual code mutation

Only exact runtime code file was replaced:

/opt/wellbeing/telegram-single-entity-mvp-r02/dialogue_mvp.py

Method:
atomic temp write + fsync + os.replace

Installed code SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

owner/group/mode:
preserved

CODE_METADATA_PRESERVED=YES

No config/bootstrap/unit/allowlist/credential mutation occurred.

## DB migration first run

MIGRATION_FIRST_RUN=EXECUTED

integrity:
ok

Added nullable columns:

- inbound_message_id
- message_thread_id
- direct_topic_id
- trigger_class
- outbound_message_id
- returned_chat_id
- returned_message_thread_id
- returned_direct_topic_id
- returned_is_topic_message

Exact post-migration updates schema:

update_id,
request_digest,
state,
conversation_key,
telegram_message_id,
error_class,
inbound_message_id,
message_thread_id,
direct_topic_id,
trigger_class,
outbound_message_id,
returned_chat_id,
returned_message_thread_id,
returned_direct_topic_id,
returned_is_topic_message

Legacy preservation:
PASS

Existing counts remained:
- updates=4
- messages=8
- runtime_meta=1

Existing legacy core state, messages, runtime_meta and conversation_key values:
preserved

Historical routing backfill:
NONE

LEGACY_ROUTING_NON_NULL_ROW_COUNT=0

## DB migration second run

MIGRATION_SECOND_RUN=EXECUTED

logical idempotency:
YES

DB byte equality:
YES

integrity:
ok

No second schema/data change occurred.

## Read-only diagnose-routing

command family:
dialogue_mvp.py diagnose-routing --config CONFIG --update-id UPDATE_ID

legacy update:
560511152

exit:
0

state:
COMMITTED

conversation_key:
6e0d67535c74d3d9319afb5536af35b2040d9b459db49d65b95a76dec6b0ee8a

Returned bounded fields exactly:
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

Legacy routing observability fields:
all NULL

DIAG_LEGACY_ROUTING_FIELDS_NULL=YES

No credential/network access was required.

## Semantic/effect verification

conversation_key semantics:
PASS

Formula remains:
SHA256("tg-dialogue-r02\0" + chat_id + "\0" + message_thread_id + "\0" + direct_topic_id)

Admission/provider/model/polling:
UNCHANGED

discussion:
-1002429106148

bot:
8866633840 / WBNP_Media_Bot

model:
gpt-5.6-luna

transport:
long polling unchanged

Fail-closed synthetic verification:

send success + routing metadata persistence failure
=> OUTCOME_UNKNOWN
=> identical replay manual reconciliation
=> provider/send not repeated

FAIL_CLOSED_POST_SEND_PERSISTENCE=PASS

No real Telegram/OpenAI call was used for this test.

## Static identity preservation

Final runtime.json raw SHA-256:
57f7e44f70056021fc2ac227b7e4e06e2ef0c886b047139548d83cc5d8f2d7e1

Final runtime.json canonical semantic SHA-256:
2ebf58286499a7d7a166d38abf80d2ca6a8a2dfbbe8d5b8a4b16c833a47c40f8

CONFIG_UNCHANGED=YES

ALLOWLIST_UNCHANGED=YES

BOOTSTRAP_UNCHANGED=YES

SYSTEMD_UNIT_UNCHANGED=YES

CREDENTIAL_METADATA_UNCHANGED=YES

Credential contents:
NOT READ

## Verification-helper interruption and continuation

The primary install helper completed installation, both migrations, diagnostic verification, conversation-key verification and fail-closed test.

It then raised a local verifier exception while trying to import the predecessor rollback file via importlib using the non-.py suffix ".predecessor".

This was a verifier implementation error, not a runtime/install failure.

At that point:
- service remained stopped;
- installed candidate and migrated DB were already verified healthy;
- backup/rollback sources were intact.

A continuation verifier was used for the SAME exact task and SAME RUN_ID.

It did not repeat installation or migration.

It proved:
- installed code exact identity;
- DB backup/readability;
- current DB integrity/count/state;
- no historical routing backfill;
- static identities unchanged;
- predecessor SQL compatibility using SourceFileLoader;
- credential metadata unchanged;
- rollback readiness;
- final service stopped.

CONTINUATION_VERIFICATION=PASS

## Final host state

Fresh server readback:

LoadState=loaded
ActiveState=inactive
SubState=dead
UnitFileState=disabled
MainPID=0

dialogue process:
ABSENT

service start:
NONE

persistent enablement:
NONE

Telegram calls:
NONE

OpenAI calls:
NONE

runtime.json mutation:
NONE

allowlist mutation:
NONE

credential mutation:
NONE

Telegram/bot/channel/webhook mutation:
NONE

## Readiness

READY_FOR_SEPARATE_ONE_TURN_ROUTING_PLACEMENT_LIVE_TEST=YES

This PASS does NOT authorize live start.

A separate NEW exact bounded live task is required.

## Mandatory RETURN KOO

terminal:
PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_INSTALLED_VERIFIED_NO_LIVE_R02

installed code:
PASS exact candidate

DB migration:
PASS

legacy state:
PASS preserved

migration idempotency:
PASS

diagnose-routing:
PASS

privacy/effect safety:
PASS

rollback readiness:
PASS

final clean stop:
PASS

Telegram/OpenAI calls:
NONE

next:
READY_FOR_SEPARATE_ONE_TURN_ROUTING_PLACEMENT_LIVE_TEST

## Terminal

PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_INSTALLED_VERIFIED_NO_LIVE_R02
