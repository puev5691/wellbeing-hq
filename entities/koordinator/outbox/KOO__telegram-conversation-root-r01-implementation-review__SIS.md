# KOO -> SIS: Telegram conversation-root r0.1 implementation/offline-package independent review

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Current intended SIS writer

puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md

blob:
0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

terminal:
PASS_SIS_R07_WRITER_GATE_CURRENT_WRITER_ESTABLISHED

## Exact KOD result

puev5691/wellbeing-hq@5f10331f857f16af8ae023f17bb48f449cbd29df:
entities/koder/outbox/KOD__telegram-conversation-root-r01-implementation-candidate-result__KOO.md

blob:
e8e88973c58b80ac4d34d0a0b59be2ff6ce8039f

terminal:
PASS_KOD_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_CANDIDATE_READY_FOR_SIS_REVIEW

status:
IMPLEMENTATION_CANDIDATE_NOT_INSTALLED

## Exact immutable package

puev5691/wellbeing-hq@3e7cceaaef2a0efa27e7c7d8e69a52ebf12260f2:
entities/koder/outbox/telegram-conversation-root-r01-implementation-candidate/

package tree:
aae3baa3f958893714973a76eed0a6cd3ed9f43a

package identity:
89c55c9804565f505261719b3a2d75f6b48d84f69b81f8454790211e4c592a4e

SHA256SUMS SHA-256:
cb1ec8181a4b6c818a0930ce3b6165cfdcbcb8a09dbb0449aaaa3b76f0b90e66

candidate dialogue_mvp.py:
blob 6ff2a9dc7866cbc253c60eded4111ec418a38282
SHA-256 e594aa95ce94dc70cc0e992c894c9d315a7d771fc9b7bbd36923515019b289f6

candidate test_dialogue_mvp.py:
blob 138df42351f606ac90243f6590ecf9010357090c
SHA-256 05feb84005d2f35e731f05372d54a2bce87efe650074c403cd6d8eb03d5134b4

## Exact corrected design basis

puev5691/wellbeing-hq@ef66176b4f207990b524548d2343ac52a2e61f6b:
entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01-d1-correction/DESIGN.md

blob:
041224bb887d9af5d5a6ab181639d518ff144af2

SIS D1 PASS:

puev5691/wellbeing-hq@c666f240254dea3827b95ac9ad5895ab2dadbcbb:
entities/sisadmin/outbox/SIS__telegram-conversation-root-design-r01-D1-recheck-result__KOO.md

blob:
91e80e424774afb3d2ff07175c0afb0d7537332d

terminal:
PASS_SIS_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01_D1_RECHECK

## Exact predecessor

puev5691/wellbeing-hq@7bc9ab9df85a80bedd6717aa38b0478c3c12ecb1:
entities/koder/outbox/telegram-routing-observability-r01/dialogue_mvp.py

predecessor SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

## Scope

Perform ONLY independent implementation/offline-package review.

NO:
- install;
- live /opt mutation;
- live DB/schema mutation;
- service start/enable;
- Telegram calls;
- OpenAI calls;
- runtime.json mutation;
- allowlist mutation;
- credential read/mutation;
- failed live task replay;
- production/live authority.

Use only immutable package bytes and disposable/local review environment.

## R1. Package identity / integrity

Independently verify:
- exact 13/13 package entries;
- package tree;
- package identity construction;
- SHA256SUMS;
- MANIFEST consistency;
- candidate source hash;
- candidate test hash;
- config.example predecessor identity;
- predecessor and test diff completeness.

Return PASS/FAIL exact identity.

## R2. Design-to-code conformance

Verify implementation matches accepted corrected design:

Executable root classes only:
- OBSERVED_LINKED_THREAD_ANCHOR
- PROVEN_OUTBOUND_LINEAGE
- SAME_ROOT_OBSERVATION
- ISOLATED_UNRESOLVED

Confirm:
- PROVEN_AUTO_FORWARD_ROOT is NOT executable;
- automatic-forward does not widen human admission;
- automatic-forward cannot reach provider/history/send;
- C5 HYBRID_FAIL_CLOSED behavior preserved.

Check no undocumented fifth merge path exists.

## R3. Root key semantics

Verify:

stable root ID:
- deterministic;
- versioned/domain-separated;
- mode-scoped;
- chat-scoped;
- no user identity/name/text.

conversation key:
SHA256("tg-dialogue-root-r01\0" + stable_conversation_root_id)

Historical tg-dialogue-r02 keys:
- untouched;
- not rewritten;
- not backfilled.

Check collision/namespace separation:
- cross-chat;
- linked-discussion vs forum/direct-topic;
- isolated unresolved roots.

## R4. PROVEN_OUTBOUND_LINEAGE implementation

Independently inspect exact guards.

PASS requires:
- inbound reply_to_message.message_id present;
- lookup includes current chat;
- exact outbound_message_id;
- exactly one eligible prior row;
- prior state COMMITTED or FALLBACK_COMMITTED;
- stable prior root non-null;
- prior returned_chat_id/current chat compatible;
- same mode;
- no direct-topic/mode conflict.

Zero/multiple/conflicting/legacy-null:
NO HISTORY MERGE.

Check no lookup uses numeric coincidence between observed thread and outbound ID as semantic rule.

## R5. Initial root / same-root / unresolved

Verify:

OBSERVED_LINKED_THREAD_ANCHOR:
- only for admitted linked-discussion human turn;
- valid observed thread;
- no proven lineage/conflict;
- not claimed canonical MTProto top root.

SAME_ROOT_OBSERVATION:
- same chat;
- same mode;
- exact anchor evidence;
- no stronger conflict.

ISOLATED_UNRESOLVED:
- cannot silently read existing history;
- deterministic enough for replay safety;
- no accidental merge across turns without evidence.

## R6. Schema / migration candidate

Review additive fields:

- inbound_reply_to_message_id
- inbound_reply_to_message_thread_id
- stable_conversation_root_id
- root_derivation_class
- root_evidence_update_id
- root_conversation_key

Optional automatic-forward metadata only if non-executable/diagnostic.

Verify migration:
- additive nullable only;
- idempotent;
- no table replacement;
- no destructive rewrite;
- no legacy root backfill;
- no old conversation_key rewrite;
- no transcript rewrite;
- legacy rows remain NULL.

Independently run disposable migration from:
1. exact current observability schema;
2. older r0.2 schema if package claims support.

Verify predecessor SQL compatibility where claimed.

## R7. Effect ordering / transaction safety

Inspect exact code paths and tests for:

claim
-> persist deterministic root decision
-> history selection
-> provider
-> durable SENDING
-> one send
-> returned evidence validation
-> atomic transcript/outbound/root relation
-> COMMITTED/FALLBACK_COMMITTED

Verify:
- root decision is durable before provider;
- replay reuses persisted root decision;
- root cannot be re-derived differently on replay;
- send success + root/lineage/transcript persistence failure => OUTCOME_UNKNOWN;
- no second provider/send effect after uncertainty.

Flag any transaction gap.

## R8. Privacy boundary

Verify persisted/logged candidate extension does NOT add:
- raw Update JSON;
- full Message;
- username/display_name;
- unrelated participant identity;
- raw provider response;
- nested raw reply chains;
- secrets.

Root metadata must be bounded scalar evidence only.

## R9. Independent offline test reproduction

Reproduce independently:

- predecessor baseline 35/35 with predecessor source/tests;
- candidate py_compile;
- candidate 54/54 or exact package-declared suite;
- T1-T16;
- exact parameterized A/B fixture;
- migration first run;
- migration second-run idempotency;
- legacy DB/history compatibility;
- replay/effect tests;
- privacy tests;
- ambiguous/unknown/cross-chat/direct-topic fail-closed tests.

No Telegram/OpenAI network calls.

## R10. Critical predecessor regression probe

Independently reproduce:

unmodified predecessor test file + candidate source:
expected disclosed result 34/35.

Inspect the single failing predecessor fixture.

Determine whether:
A) it is genuinely obsolete because repeated message_thread_id=0 contains insufficient root evidence under accepted fail-closed root-r0.1 semantics;

or
B) candidate accidentally broke a still-required behavior.

Do not accept KOD's classification by assertion.

For PASS, show:
- exact failing test identity;
- exact semantic expectation of old fixture;
- why accepted corrected design requires or permits the new behavior;
- replacement regression fixture uses explicit proven root evidence and tests the same bounded pruning property without restoring unsafe implicit continuity.

If this cannot be proven:
NEEDS_REWORK.

## R11. Exact observed failure fixture

Verify parameterized fixture:

Turn1 thread=A
bot outbound=B
Turn2 direct reply target=B
Turn2 observed thread=B
A != B

Required:
- Turn2 root class PROVEN_OUTBOUND_LINEAGE;
- same stable root;
- same root-r0.1 conversation key;
- Turn2 history includes Turn1;
- no hard-coded B==thread semantic inference.

## R12. Automatic-forward D1 preservation

Verify:
- automatic-forward root creation NO;
- normal tester admission widening NO;
- provider calls 0;
- send effects 0;
- no hidden pre/parallel root evidence path;
- future auto-forward capture still needs separate design/authority.

## Verdict

Allowed PASS terminal:

PASS_SIS_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_PACKAGE_REVIEW

Allowed correction terminal:

NEEDS_REWORK_SIS_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_PACKAGE_REVIEW

or exact BLOCKED_/FAIL_.

If NEEDS_REWORK:
return only exact implementation/package defects and bounded correction scope.
Do not implement fixes.

If PASS:
state exact next gate:

KOO fresh reconciliation may authorize a separate NEW bounded install/verify-readiness task.

PASS does NOT authorize:
- live install;
- live DB migration;
- service start;
- Telegram/OpenAI calls;
- production/live use.

## Mandatory RETURN KOO

Return:
- package identity/integrity verdict;
- design-to-code conformance;
- root-key verdict;
- lineage-guard verdict;
- schema/migration verdict;
- replay/effect-ordering verdict;
- privacy verdict;
- independent test reproduction;
- predecessor 34/35 regression classification;
- exact A/B fixture verdict;
- D1 automatic-forward preservation;
- network calls=0;
- live mutation=NONE;
- exact terminal;
- exact next bounded gate.

Then STOP.
