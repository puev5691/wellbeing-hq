# KOO -> KOD: Telegram conversation-root r0.1 implementation candidate

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Current KOD writer

puev5691/wellbeing-hq@5d1374d9f7396c34bde5e785f3a9b0872f451977:
entities/koder/current/KOD__replacement-current-writer-v06.md

blob:
338f1bcf6f59b53356ea6fb20f2ac081af8cda7e

status:
CURRENT_WRITER_ESTABLISHED

terminal:
PASS_KOD_REPLACEMENT_V06_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Exact SIS D1 PASS

puev5691/wellbeing-hq@c666f240254dea3827b95ac9ad5895ab2dadbcbb:
entities/sisadmin/outbox/SIS__telegram-conversation-root-design-r01-D1-recheck-result__KOO.md

blob:
91e80e424774afb3d2ff07175c0afb0d7537332d

terminal:
PASS_SIS_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01_D1_RECHECK

Verified:
D1_CLOSED=YES
D1_DIFF_CONTAINED=YES
ADMISSION_WIDENING=NO
DESIGN_STATUS=DESIGN_CANDIDATE_NOT_IMPLEMENTED

## Exact corrected design

puev5691/wellbeing-hq@ef66176b4f207990b524548d2343ac52a2e61f6b:
entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01-d1-correction/DESIGN.md

blob:
041224bb887d9af5d5a6ab181639d518ff144af2

Exact D1 diff:

puev5691/wellbeing-hq@ef66176b4f207990b524548d2343ac52a2e61f6b:
entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01-d1-correction/D1-DIFF.md

blob:
6d7906499cb8c85c0f0b4bbc938cc49941ffb292

Selected design:
C5 HYBRID_FAIL_CLOSED

Executable r0.1 derivation classes:
- OBSERVED_LINKED_THREAD_ANCHOR
- PROVEN_OUTBOUND_LINEAGE
- SAME_ROOT_OBSERVATION
- ISOLATED_UNRESOLVED

PROVEN_AUTO_FORWARD_ROOT:
NOT EXECUTABLE IN R0.1

## Exact current installed observability basis

puev5691/wellbeing-hq@d6d9d0dafde9170b2ee8d7b0b069025e99f76f4e:
entities/sisadmin/outbox/SIS__telegram-routing-observability-r01-install-verify-r02-result__KOO.md

blob:
a81a6cd3590c9f491d34e1a4b732f003c79a9562

terminal:
PASS_SIS_TELEGRAM_ROUTING_OBSERVABILITY_R01_INSTALLED_VERIFIED_NO_LIVE_R02

Current installed dialogue_mvp.py SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

## Exact failure fixture

puev5691/wellbeing-hq@d06ebe706473a0e96027322782c1b4f9b47e1ba8:
entities/sisadmin/outbox/SIS__telegram-same-thread-two-turn-multiturn-r01-result__KOO.md

blob:
e513fc629ca02700571d7993080fa38ee567684e

terminal:
FAIL_SIS_TELEGRAM_TWO_TURN_R01_INBOUND_TUPLE_MISMATCH

Fixture:
Turn 1 thread=A
bot outbound=B
Turn 2 direct reply target=B
Turn 2 observed thread=B
A != B

Expected future root behavior:
same stable project root by unique prior outbound lineage.
No hard-coded numeric semantics.

## Goal

Produce an immutable OFFLINE implementation candidate for conversation-root r0.1.

This task authorizes:
- modifying candidate source files in a NEW KOD outbox package only;
- implementing the corrected root-r0.1 semantics in candidate code;
- adding additive candidate schema/migration logic in code/tests;
- adding offline synthetic tests and fixtures;
- static/offline execution against disposable local databases;
- package identity/checksums/readback.

This task does NOT authorize:
- mutation of live /opt runtime;
- mutation of live /var/lib DB/schema;
- install;
- service start/enable;
- Telegram calls;
- OpenAI calls;
- config/allowlist/credential mutation;
- live migration;
- live test;
- replay of failed live task.

## I1. Candidate semantic root resolver

Implement in candidate code only.

Root-r0.1 must be mode-separated and versioned.

Required executable derivation classes:

1. OBSERVED_LINKED_THREAD_ANCHOR
2. PROVEN_OUTBOUND_LINEAGE
3. SAME_ROOT_OBSERVATION
4. ISOLATED_UNRESOLVED

No executable PROVEN_AUTO_FORWARD_ROOT.

Normal admission semantics remain unchanged.

Automatic-forward events must not become human tester turns or provider/send inputs.

## I2. Root ID / conversation key

Implement deterministic stable root ID with domain separation.

Root descriptor must include at minimum:
- mode namespace;
- chat_id;
- root anchor identity/class inputs sufficient to avoid cross-chat/mode collision.

No user identity, username, display name or text.

New conversation key domain:

SHA256("tg-dialogue-root-r01\0" + stable_conversation_root_id)

Historical tg-dialogue-r02 conversation_key values remain untouched.

Do not rewrite legacy transcripts.

## I3. Reply-to-known-outbound lineage

For admitted reply-to-bot inbound:

Use exact bounded reply target:
reply_to_message.message_id

Resolve against prior outbound effect using:
- same current chat;
- exact reply target outbound_message_id;
- exactly one eligible prior row;
- prior state COMMITTED or FALLBACK_COMMITTED;
- prior stable root non-null;
- prior returned_chat_id equals current chat;
- same mode;
- no direct-topic/mode conflict.

If exactly one eligible prior effect exists:
inherit its stable root.

If zero/multiple/conflicting:
do NOT merge history.
Use fail-closed isolated/unresolved behavior or block before provider according to candidate policy.

No fuzzy lookup.
No numeric thread/outbound coincidence inference.

## I4. Initial observed root

For an admitted linked-discussion human turn with:
- no proven outbound lineage;
- valid observed message_thread_id;
- no conflicting root evidence;

establish a deterministic project root as:
OBSERVED_LINKED_THREAD_ANCHOR.

Explicitly do not label it canonical MTProto top root.

If observed root evidence is unavailable/conflicting:
ISOLATED_UNRESOLVED.

## I5. SAME_ROOT_OBSERVATION

Reuse an established root only when:
- same chat;
- same mode;
- exact observed anchor match;
- no conflicting stronger evidence.

Proven outbound lineage takes precedence when valid.

No cross-chat or cross-mode merge.

## I6. Candidate metadata

Candidate schema may add only bounded nullable scalar fields justified by corrected design.

Required candidate fields:

- inbound_reply_to_message_id
- inbound_reply_to_message_thread_id
- stable_conversation_root_id
- root_derivation_class
- root_evidence_update_id

Optional:
- inbound_is_automatic_forward only if retained strictly as bounded protocol/diagnostic metadata and NOT used to derive executable r0.1 root.

Reuse existing:
- outbound_message_id
- returned_chat_id
- message_thread_id
- direct_topic_id
- update/effect state

Do NOT persist:
- raw Update JSON;
- full Telegram Message;
- username/display name;
- unrelated participant identities;
- nested raw reply chain;
- raw provider response.

## I7. Additive candidate migration logic

Implement only in candidate package/offline test DBs.

Requirements:
- additive nullable fields only;
- idempotent;
- no table replacement;
- no destructive rewrite;
- no legacy root backfill;
- no legacy conversation_key rewrite;
- no transcript rewrite;
- no inferred historical lineage.

Legacy rows:
new root/lineage fields remain NULL.

Migration must preserve predecessor SQL compatibility where feasible and document any exact incompatibility.

Do not apply to live DB.

## I8. Effect ordering / replay safety

Preserve the existing effect safety model.

Required conceptual order:

parse/admit
-> claim update
-> derive/persist deterministic root decision
-> history selection by root-r0.1 key
-> provider
-> durable SENDING
-> one Telegram send
-> validate bounded returned evidence
-> atomically persist transcript + outbound relation + root relation
-> COMMITTED/FALLBACK_COMMITTED

If send succeeds but root/lineage/transcript persistence fails:
OUTCOME_UNKNOWN
and no blind resend.

Replay of same update must:
- reuse persisted root decision;
- not choose a different root;
- not repeat provider/send effect.

## I9. Exact observed fixture

Add parameterized offline fixture:

- initial linked discussion thread = A;
- Turn 1 stable root = R;
- bot outbound message = B;
- Turn 2 direct reply target = B;
- Turn 2 observed message_thread_id = B;
- A != B.

Expected:
- Turn 2 derives PROVEN_OUTBOUND_LINEAGE;
- Turn 2 stable root = R;
- Turn 1 and Turn 2 root-r0.1 conversation_key equal;
- Turn 2 history includes prior Turn 1 pair;
- no hard-coded relation B==thread is used.

## I10. Required offline test matrix

Implement at least T1-T16 consistent with corrected design.

Mandatory:

T1 initial linked-discussion human command establishes OBSERVED_LINKED_THREAD_ANCHOR.

T2 direct Reply to known bot outbound with changed message_thread_id inherits same root.

T3 same observed root reuse only when exact root-anchor evidence matches.

T4 reply to bot outbound belonging to another root never merges wrong histories.

T5 unknown reply target -> no merge.

T6 legacy row with NULL lineage/root -> no guessed merge.

T7 duplicate update replay -> one provider/send effect max.

T8 send success + root/lineage persistence failure -> OUTCOME_UNKNOWN / no resend.

T9 cross-chat same numeric IDs -> no merge.

T10 direct_topic/mode change -> no merge.

T11 privacy projection only; no raw payload/name persistence.

T12 exact A/B fixture above without hard-coded IDs.

T13 ambiguous outbound lookup -> no merge, provider/send blocked or isolated per explicit policy.

T14 conflicting thread observation without proven lineage -> isolate.

T15 automatic-forward capability deferred:
- no executable root creation;
- no tester admission widening;
- provider calls=0;
- send effects=0.

T16 forum/linked-discussion namespace separation.

Also retain/re-run existing routing-observability/replay/effect tests from predecessor candidate as applicable.

## I11. Offline execution

Run only offline/local/disposable:

- py_compile;
- unit tests;
- migration first-run;
- migration second-run idempotency;
- legacy DB compatibility fixture;
- privacy assertions;
- replay/effect assertions;
- exact A/B fixture;
- fail-closed ambiguity fixture.

No Telegram/OpenAI network calls.

## I12. Candidate package

Create one immutable package, for example:

entities/koder/outbox/telegram-conversation-root-r01-implementation-candidate/

Include:
- candidate dialogue_mvp.py
- tests
- migration/schema description
- root semantics spec/readme
- exact predecessor identity
- corrected design identity
- SIS D1 PASS identity
- manifest
- SHA256SUMS
- package identity
- offline test report
- exact diff/patch from current installed/reviewed predecessor candidate

Status:
IMPLEMENTATION_CANDIDATE_NOT_INSTALLED

## I13. Boundaries

Do NOT:
- mutate live host;
- install candidate;
- mutate live DB/schema;
- start service;
- call Telegram;
- call OpenAI;
- change runtime.json;
- change allowlist;
- read/mutate credentials;
- create live authority;
- mark implementation accepted without independent SIS review.

## Expected terminal

PASS_KOD_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_CANDIDATE_READY_FOR_SIS_REVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact package/tree/blob identities;
- exact source/test hashes;
- implemented root semantics;
- schema/migration candidate;
- T1-T16 results;
- predecessor regression results;
- privacy/replay/effect results;
- exact A/B fixture result;
- network calls = 0;
- live mutation = NONE;
- status IMPLEMENTATION_CANDIDATE_NOT_INSTALLED;
- exact next gate:
  SIS independent implementation/offline-package review only.

Then STOP.
