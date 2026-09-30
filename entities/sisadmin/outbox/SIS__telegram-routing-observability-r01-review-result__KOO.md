# SIS -> KOO: Telegram routing observability r0.1 independent review/install-readiness

status: PASS
terminal: PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_REVIEW_READY_FOR_SEPARATE_INSTALL_VERIFY
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
recipient: KOO / КООРДИНАТОР

## Human result

Independent review of the exact KOD routing-observability candidate completed PASS.

The package is internally consistent with the requested narrow observability delta:
- existing admission/provider/model/polling/conversation-key semantics remain unchanged;
- nine routing fields are added as nullable SQLite columns;
- migration is additive and idempotent;
- legacy rows/messages/runtime_meta remain readable and are not backfilled by guess;
- send-success followed by routing-validation/persistence failure is fail-closed to OUTCOME_UNKNOWN and identical replay does not resend;
- diagnostic output is a bounded read-only projection;
- privacy boundary excludes raw Update JSON, full Telegram Message persistence, usernames/display names, unrelated identities, raw provider response and credentials.

No installation, live host mutation, service start/enable, Telegram call, OpenAI call, credential read, allowlist mutation, Telegram settings mutation or package mutation was performed.

## Exact task

puev5691/wellbeing-hq@b1464b8a5ec16d0f4025dd2b36f9c1987017da90:
entities/koordinator/outbox/KOO__telegram-routing-observability-r01__SIS.md

blob:
dc56526532ce900b930a2c4185f36d825ad6d9a9

## Current SIS writer

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

terminal:
PASS_SIS_R07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Exact KOD result

puev5691/wellbeing-hq@b13efdd6fe32a72c4e8a0f58e2a009457b2e329b:
entities/koder/outbox/KOD__telegram-routing-observability-r01-result__KOO.md

blob:
20aa087daec5497007b1cd307c36e17047156723

terminal:
PASS_KOD_TELEGRAM_ROUTING_OBSERVABILITY_R01_CANDIDATE_READY_FOR_SIS_REVIEW

## Exact package identity/readback

Locator:

puev5691/wellbeing-hq@7bc9ab9df85a80bedd6717aa38b0478c3c12ecb1:
entities/koder/outbox/telegram-routing-observability-r01/

Exact Git tree:
bbe40dc80670b33594f997cea52e42508a7ae12b

Git tree recursive readback:
- truncated=false
- 13/13 package entries present
- each entry path/blob/size matched exact tree readback

Package identity from MANIFEST:
537dd42aacf88c7c5f2ff706ac75b9de836c613f7496f0effacfc66924ecb86c

Independent package-identity reconstruction:
PASS

Construction:
SHA-256(
  UTF-8("TELEGRAM-ROUTING-OBSERVABILITY-R01")
  + NUL
  + exact SHA256SUMS bytes
)

Reconstructed:
537dd42aacf88c7c5f2ff706ac75b9de836c613f7496f0effacfc66924ecb86c

Selected exact executable/test/config/unit bytes were independently reconstructed from immutable GitHub readback and matched package SHA256SUMS:

dialogue_mvp.py:
- bytes=41347
- sha256=8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7
- PASS

test_dialogue_mvp.py:
- bytes=20081
- sha256=25821c634bb0611f7ce77a5a1bb578ce9da802bc7ffe760f7b04b411b3edf4f0
- PASS

config.example.json:
- bytes=958
- sha256=5737bd42abd092e3adf0f690f8928348a0df104a6a649d67cb1abb4064a91e6d
- PASS

wellbeing-telegram-single-entity-pilot.service:
- bytes=1121
- sha256=5795b145b3de03af96e45a2dc74b3fe025220e9ad18e76ee322afd91ba936b89
- PASS

## Independent offline execution

Exact reconstructed candidate bytes were executed in an isolated local review environment, not on the live VDS.

py_compile:
PASS

unittest:
Ran 35 tests
OK
35/35 PASS

systemd-analyze verify:
PASS
exit 0

The review harness emitted an unrelated local spreadsheet-runtime warmup warning before Python startup; the Python commands themselves exited 0 and the unittest report completed 35/35 OK. This warning is review-environment noise, not candidate output or package behavior.

## Predecessor preservation / unchanged fixtures

Candidate and exact r0.2 predecessor Git blobs are byte-identical for:

config.example.json:
949620ab9feeb6b0f2466a1881c3a0bd067d1906

entity_bootstrap.txt:
279741d677e2b8e46bfd542e956c8b68b3041ab3

testers.allow.example:
b1fe2c39f638cefcab0c207b377ee622a14641a6

wellbeing-telegram-single-entity-pilot.service:
44b80e713134471abea9387e5cf30194bfe7f9ce

Therefore this package does not introduce a config, bootstrap, tester-fixture or systemd-unit delta.

PREDECESSOR-DIFF exact surface:
- dialogue_mvp.py: 18 hunks
- test_dialogue_mvp.py: 6 hunks
- README.md: 2 hunks
- UPGRADE.md: 1 hunk
- new ROUTING-OBSERVABILITY-SCHEMA.json: 1 hunk

No other predecessor file delta is represented by the exact patch.

## Routing fields review

Exact additive fields confirmed in code + machine-readable schema:

- inbound_message_id
- message_thread_id
- direct_topic_id
- trigger_class
- outbound_message_id
- returned_chat_id
- returned_message_thread_id
- returned_direct_topic_id
- returned_is_topic_message

Trigger enum:
- reply-to-bot
- command
- exact-mention

Returned Telegram Message is projected transiently into TelegramSendEvidence only:
- result.message_id
- result.chat.id
- optional result.message_thread_id
- optional result.direct_messages_topic.topic_id
- optional result.is_topic_message

Full returned Telegram Message is not persisted.

## Conversation-key semantics

Exact candidate rule remains:

SHA256(
  UTF8(
    "tg-dialogue-r02\0"
    + decimal(chat_id)
    + "\0"
    + decimal(message_thread_id)
    + "\0"
    + decimal(direct_topic_id)
  )
)

This is unchanged from exact predecessor.

New observability fields do not participate in conversation_key.

## Admission/provider/model/polling review

Admission identity/config fixture is byte-identical to predecessor.

Verified preserved bindings:
- discussion chat: -1002429106148
- bot id: 8866633840
- bot username: WBNP_Media_Bot
- activation command: ask
- allowed chat type: supergroup
- provider adapter: OpenAI Responses API
- model source remains config.model
- candidate config remains model gpt-5.6-luna
- long polling getUpdates shape remains offset/limit/timeout/allowed_updates=["message"]

No new admission route was added.

Trigger classification annotates an already-admitted event; it does not widen admission.

## Migration review

Migration implementation:
Store._migrate_routing_schema

Method:
- BEGIN IMMEDIATE
- inspect existing updates columns
- ordered ALTER TABLE ADD COLUMN for missing routing columns only
- COMMIT
- ROLLBACK on error

No:
- table replacement
- DELETE
- destructive rewrite
- legacy backfill
- transcript rewrite
- inferred historical routing data

Independent disposable legacy-r0.2 migration probe:

MIGRATION_COLUMNS_ADDED:
all 9 expected routing columns

MIGRATION_IDEMPOTENT_SCHEMA:
True

LEGACY_ROW_PRESERVED:
True

LEGACY_NEW_FIELDS_NULL:
True

MESSAGES_PRESERVED:
True

RUNTIME_META_PRESERVED:
True

SECOND_RUN_DB_BYTES_UNCHANGED:
True

## Rollback compatibility probe

A disposable DB was:
1. created with exact predecessor r0.2 table shapes;
2. migrated using exact candidate Store;
3. exercised with the predecessor SQL patterns for claim/mark/message insert/commit.

Results:

PREDECESSOR_SQL_ON_MIGRATED_DB=True
PREDECESSOR_NEW_ROW_ROUTING_COLUMNS_NULL=True
LEGACY_PREEXISTING_ROW_STILL=True
LEGACY_TRANSCRIPT_STILL=True

Meaning:
restoring predecessor code while leaving the nine added nullable columns is DB-schema compatible for the predecessor SQL paths reviewed.

This is offline rollback-compatibility evidence only; no live rollback/start was executed.

## Fail-closed effect ordering

Candidate flow reviewed:

claim
-> provider
-> durable SENDING
-> one sendMessage
-> validate bounded returned route
-> atomic transcript+routing commit

If sendMessage succeeds but route validation or routing persistence fails:
- state becomes OUTCOME_UNKNOWN with routing-persistence error class;
- same update replay returns manual_reconciliation_required;
- no second provider/send effect occurs.

Independent 35-test reproduction includes:
test_t6_send_success_metadata_persistence_failure_is_uncertain_no_resend
PASS

This meets the no-blind-resend requirement.

## Privacy review

Persisted routing extension does NOT add:
- raw Update JSON
- full returned Telegram Message
- username
- display name
- unrelated identities
- raw provider response
- credential material

Existing visible bounded dialogue transcript behavior is unchanged and is outside this extension.

Test coverage independently reproduced:
- raw identity/text not logged
- returned Message projected, not retained
- routing row excludes raw update/content/names/provider response
- bounded diagnostic excludes request_digest, telegram_message_id alias, text, username, display_name, raw_update, provider_response

Privacy verdict:
PASS

## diagnose-routing review

CLI:
dialogue_mvp.py diagnose-routing --config CONFIG --update-id UPDATE_ID

Properties:
- SQLite opened mode=ro
- migrate=False
- no credential() call
- no network call
- exact bounded projection only

Exact returned fields:
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

Independent T9 tests:
PASS

## Host delta for a future separate install task

This review authorizes nothing on the host.

The reviewed intended delta is limited to:

1. runtime code:
replace/stage exact dialogue_mvp.py candidate bytes;
2. SQLite:
add the nine nullable columns to updates;
3. no config change;
4. no bootstrap change;
5. no tester/allowlist change;
6. no credential change/readout;
7. no systemd unit change;
8. no Telegram settings change;
9. no service enable/start in install/verify scope;
10. no live Telegram/OpenAI call.

A separate install task must first fresh-verify:
- service inactive/dead/disabled/MainPID=0;
- no dialogue process;
- exact installed predecessor code identity;
- exact config/unit/bootstrap identities;
- exact DB pre-state;
- exact allowlist remains separately approved current state;
- candidate bytes equal this reviewed immutable package.

## Proposed separate bounded install/verify scope

A NEW exact KOO task may authorize only:

A. PRESTATE
- read-only verify exact predecessor installed bytes;
- freeze exact DB pre-state by SQLite-consistent backup/readback under stopped service;
- record schema, row counts and integrity check;
- preserve exact predecessor code rollback source;
- STOP on mismatch.

B. STAGE
- stage exact candidate dialogue_mvp.py from package tree bbe40dc80670b33594f997cea52e42508a7ae12b;
- verify sha256 8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7;
- py_compile staged bytes;
- no service start.

C. CODE PLACEMENT
- perform one atomic code-file replacement only after exact predecessor identity/rollback source is frozen;
- preserve ownership/mode;
- read back installed candidate SHA256;
- config/unit/bootstrap/allowlist/credentials remain untouched.

D. DB MIGRATION
- while service remains stopped, invoke the reviewed Store migration exactly once through a bounded one-shot local Python/import operation;
- no load_runtime, no credential() call, no network;
- read back all 9 columns;
- verify existing updates/messages/runtime_meta content against pre-state evidence;
- invoke migration a second time on the stopped DB and prove no schema/data change.

E. DIAGNOSTIC
- run diagnose-routing only read-only on one known legacy update;
- expected new routing fields for legacy row: NULL where evidence never existed;
- prove bounded output field set;
- no credentials/network.

F. ROLLBACK READINESS
- prove predecessor code can be atomically restored;
- added nullable columns may remain based on the independent rollback-compatibility probe;
- if DB migration/integrity readback itself fails, use exact pre-state backup under a separately bounded rollback action;
- do not delete transcript/state/allowlist/credentials.

G. FINAL
- service remains loaded/inactive/dead/disabled/MainPID=0;
- no dialogue process;
- no Telegram/OpenAI call;
- no persistent enablement;
- return exact installed-code hash, migrated schema, legacy preservation checks, diagnostic readback and rollback proof.

This separate install/verify PASS would still NOT authorize service start/live.

## Live-host state after this review

Fresh read-only service check:

LoadState=loaded
ActiveState=inactive
SubState=dead
UnitFileState=disabled
MainPID=0

Dialogue process:
ABSENT

No host mutation was performed by this review.

## Verdict

PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_REVIEW_READY_FOR_SEPARATE_INSTALL_VERIFY

No code/package defect requiring KOD rework was found in this bounded review.

Candidate remains:
CANDIDATE_NOT_INSTALLED

PASS does not authorize:
- installation
- DB migration on live host
- service start/enable
- Telegram/OpenAI call
- credential access
- allowlist change
- Telegram settings change
- live pilot

## Mandatory RETURN KOO

exact package/tree:
PASS

Git tree:
bbe40dc80670b33594f997cea52e42508a7ae12b

package identity reconstruction:
PASS
537dd42aacf88c7c5f2ff706ac75b9de836c613f7496f0effacfc66924ecb86c

offline tests:
35/35 PASS

py_compile:
PASS

systemd verify:
PASS

migration:
PASS_ADDITIVE_IDEMPOTENT_LEGACY_PRESERVED

privacy:
PASS

routing fields:
PASS

conversation_key unchanged:
PASS

admission/allowlist/provider/model/polling unchanged:
PASS within exact package comparison/review scope

post-send routing-persistence failure:
PASS_FAIL_CLOSED_OUTCOME_UNKNOWN_NO_RESEND

diagnose-routing:
PASS_BOUNDED_READ_ONLY

rollback compatibility:
PASS_OFFLINE_DB_SCHEMA_COMPATIBILITY

live host mutation:
NONE

live calls:
NONE

service final:
loaded / inactive / dead / disabled / MainPID=0

next:
SEPARATE_NEW_BOUNDED_INSTALL_VERIFY_TASK_REQUIRED

## Terminal

PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_REVIEW_READY_FOR_SEPARATE_INSTALL_VERIFY
