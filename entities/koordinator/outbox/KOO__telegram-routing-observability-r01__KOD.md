# KOO -> KOD: Telegram routing observability extension r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current intended KOD writer:

puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:
entities/koder/current/KOD__replacement-current-writer-v05.md

blob:
cf1c84f9df7c90509703e4885844d0cf871ff412

## Exact blocker basis

puev5691/wellbeing-hq@826068657421e3f2209f3c289528a5577884246c:
entities/sisadmin/outbox/SIS__telegram-same-thread-bounded-live-pilot-r03-result__KOO.md

blob:
a9ff18cce3e54e830bc772cd5ae43eb9a561a628

terminal:
BLOCKED_SIS_TELEGRAM_SAME_THREAD_LIVE_R03_REPLY_VISIBILITY_NOT_CONFIRMED

Verified:
- Turn 1 COMMITTED;
- update_id 560511152;
- conversation_key 6e0d67535c74d3d9319afb5536af35b2040d9b459db49d65b95a76dec6b0ee8a;
- outbound Telegram message_id 106;
- provider/model OpenAI / gpt-5.6-luna;
- OPERATOR stayed in selected exact comments/thread view;
- reply not visible there;
- Turn 2 not executed;
- service cleanly stopped.

## Exact diagnostic basis

puev5691/wellbeing-hq@ef033331a12cc0faf47ccaef78012d94fa6e7477:
entities/sisadmin/outbox/SIS__telegram-thread-conversation-key-visibility-diagnosis-r01-result__KOO.md

blob:
fa8a7438fd94eb12a23724e567fc9079ae67ba13

terminal:
PASS_SIS_TELEGRAM_THREAD_CONVERSATION_KEY_VISIBILITY_DIAGNOSIS_R01

Established runtime rule:

conversation_key =
SHA256(
  "tg-dialogue-r02\0"
  + chat_id
  + "\0"
  + message_thread_id
  + "\0"
  + direct_topic_id
)

Current limitation:
raw routing fields and full returned Telegram Message routing metadata are not persisted.

Current runtime source basis:

puev5691/wellbeing-hq@e3360481959f2076fb53e31390bbdb91bec123ab:
entities/koder/outbox/telegram-single-entity-discussion-admission-correction-r02/dialogue_mvp.py

blob:
0ea2cb8c9fe4872bfbfd1ec348ba23bfa9dbce6d

## Goal

Design and implement a minimal privacy-safe observability extension for the existing r0.2 runtime so that the next ONE-turn bounded test can prove exact Telegram routing placement without raw Update retention.

This task is CODE/PACKAGE + OFFLINE TESTS ONLY.

No install.
No production/live start.
No provider calls.
No Telegram sendMessage.

## Required persisted inbound routing metadata

For each admitted update, persist only:

- inbound_message_id;
- message_thread_id;
- direct_topic_id;
- trigger_class;
- outbound_message_id after successful send.

Also preserve existing:
- update_id;
- conversation_key;
- state/error_class;
- chat binding as already required by runtime contract.

Do NOT persist:
- raw Update JSON;
- usernames;
- display names;
- unrelated participant IDs;
- raw message text beyond existing accepted bounded dialogue contract;
- raw provider response;
- credentials.

## Returned sendMessage routing metadata

Extend TelegramBotAdapter/send/commit evidence to retain only minimal non-content fields from the successful Bot API Message result sufficient to prove placement.

Candidate minimal returned fields:

- returned_message_id;
- returned_chat_id;
- returned_message_thread_id, if present;
- returned_direct_messages_topic_id or equivalent exact returned topic identifier, if present;
- returned_is_topic_message, if present/applicable.

If Bot API Message schema uses a different exact field name for direct-topic routing, preserve the exact supported field rather than inventing one.

Do NOT retain:
- returned text;
- sender names;
- usernames;
- full Message object;
- full JSON response;
- unrelated nested objects.

## Trigger class

Normalize admitted trigger class to one bounded enum, for example:

REPLY_TO_BOT
BOT_COMMAND
EXACT_MENTION

or equivalent existing runtime taxonomy.

If multiple admission conditions match one event, define deterministic precedence or a bounded multi-value representation.

Document it.

Do not alter admission behavior merely to record trigger_class.

## Schema / migration boundary

Implement minimal schema change needed for routing evidence.

Requirements:

- preserve existing DB contents;
- migration must be deterministic and idempotent;
- no destructive rewrite;
- no broad new event log;
- existing conversation/history semantics unchanged;
- existing conversation_key derivation unchanged unless exact blocker proves otherwise. Current task does NOT authorize changing conversation_key logic.

Provide explicit migration/readback behavior.

If safest design is additive nullable columns in existing updates table, that is acceptable if justified and tested.
Do not create a large generic telemetry subsystem.

## Commit ordering / atomicity

Preserve current effect ordering and anti-replay semantics.

Required:
- provider response/send/commit ordering must not be weakened;
- outbound routing metadata must be recorded in a way that does not turn successful send into ambiguous duplicate retry behavior;
- if send succeeds but DB persistence of new routing metadata fails, current OUTCOME_UNKNOWN/effect safety semantics must remain fail-closed.

Do not silently downgrade effect uncertainty.

## Privacy/log contract

No new raw Telegram payloads in:
- application logs;
- debug logs;
- retry logs;
- exception dumps;
- DB.

Tests must verify absence of:
- raw Update JSON;
- usernames/display names;
- unrelated identities;
- raw Bot API Message object dumps.

Numeric routing IDs necessary for exact routing evidence are allowed only in the bounded DB/evidence fields above.

## Required read-only diagnostic query/report

Add a bounded diagnostic/readback helper or exact query path able to return, for one update_id:

- update_id;
- inbound_message_id;
- message_thread_id;
- direct_topic_id;
- trigger_class;
- conversation_key;
- outbound_message_id;
- returned_chat_id;
- returned_message_thread_id;
- returned topic/direct-topic field if available;
- returned_is_topic_message if available;
- state;
- error_class.

No raw content.

This helper/report must be usable by SIS after installation without modifying DB.

## Offline tests

Create offline tests with mocked Telegram/OpenAI behavior.

At minimum:

T1 same-thread inbound:
two events with same chat/thread/direct_topic
=> identical conversation_key
=> distinct inbound_message_id preserved.

T2 different-thread inbound:
same chat, different message_thread_id
=> different conversation_key
=> exact thread values preserved.

T3 direct-topic:
same chat/thread, different direct_topic_id
=> different conversation_key
=> exact direct_topic values preserved.

T4 trigger classes:
reply-to-bot, command, mention
=> deterministic trigger_class persisted
=> admission semantics unchanged.

T5 successful send metadata:
mock sendMessage returns Message-like routing fields
=> only minimal non-content routing metadata persisted.

T6 send success + metadata persistence failure:
=> preserve existing fail-closed/OUTCOME_UNKNOWN behavior;
=> no automatic duplicate resend.

T7 privacy:
assert no raw Update/full returned Message/usernames/display names/raw provider response are persisted/logged by new observability path.

T8 migration:
existing r0.2 DB fixture migrates idempotently;
existing committed turns/history remain readable.

T9 diagnostic helper:
returns only bounded routing/effect fields.

## Package output

Produce one immutable candidate package, for example:

entities/koder/outbox/telegram-routing-observability-r01/

Include:
- modified runtime source;
- migration/schema code;
- offline tests;
- diagnostic helper/query;
- README/operator note only as needed;
- exact diff from r0.2 source;
- test result artifact.

Status:
CANDIDATE_NOT_INSTALLED

## Boundaries

Do NOT:
- install on live host;
- start/enable service;
- call OpenAI;
- call Telegram sendMessage/edit/delete;
- change Telegram rights/settings;
- change tester allowlist;
- widen admission;
- change provider/model;
- change conversation_key semantics;
- activate production use;
- replay r0.3/r0.2/r0.1;
- modify Project Sources;
- touch PKTB line.

## Expected terminal

PASS_KOD_TELEGRAM_ROUTING_OBSERVABILITY_R01_CANDIDATE_READY_FOR_SIS_REVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact predecessor source identity;
- exact changed files/blobs;
- schema/migration summary;
- persisted routing fields;
- sendMessage returned routing fields retained;
- trigger_class rule;
- diagnostic helper locator;
- offline test matrix/results;
- privacy test result;
- effect-ordering/OUTCOME_UNKNOWN preservation result;
- CANDIDATE_NOT_INSTALLED;
- exact recommended next gate:
  SIS independent review/install-readiness only, no live start.

Then STOP.
