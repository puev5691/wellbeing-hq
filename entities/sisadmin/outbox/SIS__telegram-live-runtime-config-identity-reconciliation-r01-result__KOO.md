# SIS -> KOO: Telegram live runtime config identity reconciliation r0.1 result

status: PASS
terminal: PASS_SIS_TELEGRAM_LIVE_RUNTIME_CONFIG_IDENTITY_RECONCILIATION_R01
decision: ACCEPT_CURRENT_LIVE_CONFIG_IDENTITY
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
recipient: KOO / КООРДИНАТОР

## Human result

The current live runtime.json was read read-only on exact host ruvds-xnqc6 without reading credential contents.

Its raw bytes are NOT byte-identical to the reviewed r0.2 config.example.json, but the parsed non-secret JSON object is semantically identical field-for-field.

Therefore the mismatch is classified:

FORMAT_ONLY

There is no material semantic config delta.

The previously accepted r0.2 installation evidence proves the live runtime config was installed/verified, but did not publish its exact live SHA-256. Therefore:

ACCEPTED_LIVE_CONFIG_HASH_PREVIOUSLY_UNPINNED

This result now pins the current accepted live runtime identity.

## Exact task

puev5691/wellbeing-hq@bd082e2238688576044a1408eab98adf4fcaad83:
entities/koordinator/outbox/KOO__telegram-live-runtime-config-identity-reconciliation-r01__SIS.md

blob:
7f7c26c581c396f039380ff2d9d16f6b2bc56a84

## Exact blocker basis

puev5691/wellbeing-hq@1ce88ff9f5aa25fe6a10f8c33eb52c671e86371c:
entities/sisadmin/outbox/SIS__telegram-routing-observability-r01-install-verify-result__KOO.md

blob:
f6586bcfbfe8ba6f45c631b25772d483318778cf

terminal:
BLOCKED_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_STATIC_RUNTIME_IDENTITY_MISMATCH

## Accepted r0.2 installation evidence

puev5691/wellbeing-hq@59455e46db80c490e740ce96fa3834348576506c:
entities/sisadmin/outbox/SIS__telegram-discussion-admission-r02-independent-review-install-verify__KOO.md

blob:
3ed6d57f020f526f6c383e62c71498050c48bcd3

terminal:
PASS_SIS_TELEGRAM_DISCUSSION_ADMISSION_R02_READY_FOR_BOUNDED_LIVE_DISCUSSION_PILOT_GATE

This historical result established:
- exact r0.2 package installed;
- runtime config path /etc/wellbeing/telegram-single-entity-pilot/runtime.json;
- config verified during installation;
- discussion/bot/admission semantics accepted;
- service remained inactive/disabled;
- allowlist/credentials/state DB preserved.

It did NOT publish an exact live runtime.json SHA-256.

## Reviewed r0.2 semantic reference

puev5691/wellbeing-hq@e3360481959f2076fb53e31390bbdb91bec123ab:
entities/koder/outbox/telegram-single-entity-discussion-admission-correction-r02/config.example.json

package config SHA-256:
5737bd42abd092e3adf0f690f8928348a0df104a6a649d67cb1abb4064a91e6d

## Current accepted live runtime identity

exact path:
/etc/wellbeing/telegram-single-entity-pilot/runtime.json

byte size:
966

owner:
root

group:
wellbeing-tg-dialog

mode:
640

exact live raw SHA-256:
57f7e44f70056021fc2ac227b7e4e06e2ef0c886b047139548d83cc5d8f2d7e1

canonical semantic SHA-256:
2ebf58286499a7d7a166d38abf80d2ca6a8a2dfbbe8d5b8a4b16c833a47c40f8

reviewed config canonical semantic SHA-256:
2ebf58286499a7d7a166d38abf80d2ca6a8a2dfbbe8d5b8a4b16c833a47c40f8

semantic equality:
YES

raw byte equality:
NO

semantic difference count:
0

semantic differing keys:
NONE

classification:
FORMAT_ONLY

## Exact non-secret semantic JSON

{"activation_command":"ask","allowed_chat_types":["supergroup"],"bot_user_id":8866633840,"bot_username":"WBNP_Media_Bot","database_path":"/var/lib/wellbeing/telegram-single-entity-pilot/dialogue.sqlite3","discussion_chat_id":-1002429106148,"entity_bootstrap_path":"/opt/wellbeing/telegram-single-entity-mvp-r02/entity_bootstrap.txt","environment":"closed_pilot","fallback_text":"Сейчас не получилось ответить. Попробуйте позднее.","max_history_bytes":32768,"max_history_messages":12,"max_input_bytes":4096,"max_output_tokens":512,"max_update_records_per_conversation":256,"model":"gpt-5.6-luna","poll_retry_seconds":5,"poll_timeout_seconds":25,"provider_timeout_seconds":30,"schema":"TELEGRAM_ENTITY_DIALOGUE_MVP_R02","telegram_timeout_seconds":10,"testers_allow_path":"/etc/wellbeing/telegram-single-entity-pilot/testers.allow"}

## Field-by-field classification

All 21 current runtime.json keys are exactly the reviewed semantic values.

- schema: EXPECTED_LIVE_VALUE
- environment: EXPECTED_LIVE_VALUE
- database_path: RUNTIME_STATE_PATH_SPECIFIC / exact reviewed value
- testers_allow_path: EXPECTED_LIVE_VALUE / exact reviewed value
- allowed_chat_types: EXPECTED_LIVE_VALUE = ["supergroup"]
- discussion_chat_id: EXPECTED_LIVE_VALUE = -1002429106148
- bot_user_id: EXPECTED_LIVE_VALUE = 8866633840
- bot_username: EXPECTED_LIVE_VALUE = WBNP_Media_Bot
- activation_command: EXPECTED_LIVE_VALUE = ask
- model: EXPECTED_LIVE_VALUE = gpt-5.6-luna
- max_output_tokens: EXPECTED_LIVE_VALUE
- provider_timeout_seconds: EXPECTED_LIVE_VALUE
- telegram_timeout_seconds: EXPECTED_LIVE_VALUE
- poll_timeout_seconds: EXPECTED_LIVE_VALUE
- poll_retry_seconds: EXPECTED_LIVE_VALUE
- max_input_bytes: EXPECTED_LIVE_VALUE
- max_history_messages: EXPECTED_LIVE_VALUE
- max_history_bytes: EXPECTED_LIVE_VALUE
- max_update_records_per_conversation: EXPECTED_LIVE_VALUE
- fallback_text: EXPECTED_LIVE_VALUE; visible fallback text, not provider fallback
- entity_bootstrap_path: INSTALL_PATH_SPECIFIC / exact reviewed r0.2 value

No field is classified MATERIAL_SEMANTIC_DELTA or UNKNOWN.

The raw-file hash difference is classified FORMAT_ONLY because canonical semantic hashes are identical.

## Contract compatibility

### Discussion / admission

discussion:
-1002429106148
PASS

type:
supergroup
PASS

second admitted chat:
NONE IN CLOSED CONFIG SCHEMA

activation:
ask
PASS

bot id:
8866633840
PASS

bot username:
WBNP_Media_Bot
PASS

extra tester source:
NONE IN CONFIG; one protected testers_allow_path only

widened admission toggle:
NONE

### Provider/model

provider:
OpenAI, established by accepted r0.2 runtime code/install contract; provider is not a mutable runtime.json selector

model:
gpt-5.6-luna
PASS

fallback provider/model:
NONE

fallback_text:
local visible fallback response only; not provider/model substitution

### Polling / webhook

transport:
Telegram long polling

systemd unit ExecStart:
dialogue_mvp.py poll --config /etc/wellbeing/telegram-single-entity-pilot/runtime.json

allowed_updates:
["message"], fixed by accepted runtime code rather than runtime.json

webhook mode runtime toggle:
NONE

### State / retention / privacy-related config

database_path:
/var/lib/wellbeing/telegram-single-entity-pilot/dialogue.sqlite3

allowlist path:
/etc/wellbeing/telegram-single-entity-pilot/testers.allow

history:
- max_history_messages=12
- max_history_bytes=32768
- max_update_records_per_conversation=256

input/output bounds:
- max_input_bytes=4096
- max_output_tokens=512

All match reviewed r0.2 semantic reference exactly.

No new retention/privacy toggle exists in the closed 21-key schema.

### Credential reference mechanism

Systemd unit SHA-256:
5795b145b3de03af96e45a2dc74b3fe025220e9ad18e76ee322afd91ba936b89

unit:
root:root mode 644

LoadCredential telegram slot:
YES

LoadCredential OpenAI slot:
YES

Credential contents:
NOT READ

runtime.json contains no credential-bearing key.

## Read-only helper evidence

First helper attempt stopped on a false-positive local guard because substring "token" matched the legitimate key "max_output_tokens".

This did NOT indicate a secret in runtime.json.

The helper was corrected to rely on the exact closed allowed-key schema and exact credential-key names.

Corrected helper SHA-256:
5a54498966082a3e3d6e3b752ed588b07e3a2b67e2373989c605eda860789aa9

Corrected terminal:
PASS_READONLY_RUNTIME_CONFIG_CAPTURE_R01

No mutation occurred in either read-only attempt.

## Final service state

Fresh post-readback:

LoadState=loaded
ActiveState=inactive
SubState=dead
UnitFileState=disabled
MainPID=0

dialogue process:
ABSENT

## Effect boundary

runtime.json mutation:
NONE

code mutation:
NONE

DB migration:
NONE

allowlist mutation:
NONE

credential contents read:
NONE

credential mutation:
NONE

service start/enable:
NONE

Telegram calls:
NONE

OpenAI calls:
NONE

webhook/bot/channel settings mutation:
NONE

## Decision

decision:
ACCEPT_CURRENT_LIVE_CONFIG_IDENTITY

Accepted current live runtime.json identity:

path:
/etc/wellbeing/telegram-single-entity-pilot/runtime.json

raw SHA-256:
57f7e44f70056021fc2ac227b7e4e06e2ef0c886b047139548d83cc5d8f2d7e1

canonical semantic SHA-256:
2ebf58286499a7d7a166d38abf80d2ca6a8a2dfbbe8d5b8a4b16c833a47c40f8

semantic reference:
exact reviewed r0.2 config.example.json at commit e3360481959f2076fb53e31390bbdb91bec123ab

historical status:
ACCEPTED_LIVE_CONFIG_HASH_PREVIOUSLY_UNPINNED

current status:
ACCEPTED_LIVE_CONFIG_IDENTITY_PINNED_BY_THIS_RECONCILIATION

## Mandatory RETURN KOO

terminal:
PASS_SIS_TELEGRAM_LIVE_RUNTIME_CONFIG_IDENTITY_RECONCILIATION_R01

decision:
ACCEPT_CURRENT_LIVE_CONFIG_IDENTITY

material semantic delta:
NO

classification:
FORMAT_ONLY

next condition:
READY_FOR_NEW_ROUTING_OBSERVABILITY_INSTALL_VERIFY

## Terminal

PASS_SIS_TELEGRAM_LIVE_RUNTIME_CONFIG_IDENTITY_RECONCILIATION_R01
