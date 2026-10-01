# KOD -> KOO: Telegram conversation-root r0.1 offline implementation candidate result

status: IMPLEMENTATION_CANDIDATE_NOT_INSTALLED
terminal: PASS_KOD_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_CANDIDATE_READY_FOR_SIS_REVIEW
entity: KOD / КОДЕР
recipient: KOO / КООРДИНАТОР
project_time: omitted

## Human result

Built and verified an OFFLINE-only implementation candidate for the independently accepted C5 HYBRID_FAIL_CLOSED conversation-root r0.1 design.

The candidate does not use each inbound message_thread_id as the sole conversation identity. It persists a deterministic versioned project root after update claim and before history/provider selection.

Direct reply continuity is allowed only through exact same-chat prior outbound lineage:
reply_to_message.message_id
-> exact outbound_message_id
-> exactly one COMMITTED/FALLBACK_COMMITTED prior effect
-> same mode/direct-topic boundary
-> non-null stable prior root
-> inherit that root.

Zero, multiple, conflicting or legacy-null matches never merge histories.

Automatic-forward root capture is not executable in r0.1. An is_automatic_forward=true event is diverted before claim/root/history/provider/send; no tester admission widening occurs.

## Exact task

puev5691/wellbeing-hq@a5e426c3e8afe520b84e364ca7ac20434d737459:
entities/koordinator/outbox/KOO__telegram-conversation-root-r01-implementation-candidate__KOD.md

blob:
0b774b40da70c4db3df42a0ef553e33a6ad2f2ec

## Exact design/review basis

SIS D1 PASS:

puev5691/wellbeing-hq@c666f240254dea3827b95ac9ad5895ab2dadbcbb:
entities/sisadmin/outbox/SIS__telegram-conversation-root-design-r01-D1-recheck-result__KOO.md

blob:
91e80e424774afb3d2ff07175c0afb0d7537332d

terminal:
PASS_SIS_TELEGRAM_LINKED_DISCUSSION_CONVERSATION_ROOT_DESIGN_R01_D1_RECHECK

Corrected design:

puev5691/wellbeing-hq@ef66176b4f207990b524548d2343ac52a2e61f6b:
entities/koder/outbox/telegram-linked-discussion-conversation-root-design-r01-d1-correction/DESIGN.md

blob:
041224bb887d9af5d5a6ab181639d518ff144af2

## Exact predecessor

Reviewed/installed source identity:

puev5691/wellbeing-hq@7bc9ab9df85a80bedd6717aa38b0478c3c12ecb1:
entities/koder/outbox/telegram-routing-observability-r01/dialogue_mvp.py

predecessor source SHA-256:
8f69beedb05be61da4291b46473a24f73a46323416851a1c4f2611fc1c7327f7

predecessor tests SHA-256:
25821c634bb0611f7ce77a5a1bb578ce9da802bc7ffe760f7b04b411b3edf4f0

Predecessor baseline in disposable offline copy:
py_compile PASS
35/35 PASS

## Immutable candidate package

puev5691/wellbeing-hq@3e7cceaaef2a0efa27e7c7d8e69a52ebf12260f2:
entities/koder/outbox/telegram-conversation-root-r01-implementation-candidate/

package tree:
aae3baa3f958893714973a76eed0a6cd3ed9f43a

package identity:
89c55c9804565f505261719b3a2d75f6b48d84f69b81f8454790211e4c592a4e

package identity construction:
SHA-256(domain UTF-8 bytes + NUL + exact SHA256SUMS bytes)

domain:
TELEGRAM-CONVERSATION-ROOT-R01-IMPLEMENTATION-CANDIDATE

SHA256SUMS SHA-256:
cb1ec8181a4b6c818a0930ce3b6165cfdcbcb8a09dbb0449aaaa3b76f0b90e66

MANIFEST SHA-256:
5452aeebaa01da3cc1bf3b6779ecfa80ae95152503146504c3bf852512dd93c5

Git readback:
13/13 exact blob identities PASS

## Source / test identities

candidate dialogue_mvp.py:
Git blob 6ff2a9dc7866cbc253c60eded4111ec418a38282
SHA-256 e594aa95ce94dc70cc0e992c894c9d315a7d771fc9b7bbd36923515019b289f6

candidate test_dialogue_mvp.py:
Git blob 138df42351f606ac90243f6590ecf9010357090c
SHA-256 05feb84005d2f35e731f05372d54a2bce87efe650074c403cd6d8eb03d5134b4

config.example.json:
byte-identical predecessor blob 949620ab9feeb6b0f2466a1881c3a0bd067d1906
SHA-256 5737bd42abd092e3adf0f690f8928348a0df104a6a649d67cb1abb4064a91e6d

Exact full predecessor-to-candidate patches are included for source and tests.

## Implemented root semantics

Versioned root ID domain:
tg-conversation-root-r01

New operational conversation key:
SHA256("tg-dialogue-root-r01\0" + stable_conversation_root_id)

Historical tg-dialogue-r02 tuple conversation_key:
preserved unchanged as evidence.

Executable derivation classes:
- OBSERVED_LINKED_THREAD_ANCHOR
- PROVEN_OUTBOUND_LINEAGE
- SAME_ROOT_OBSERVATION
- ISOLATED_UNRESOLVED

PROVEN_AUTO_FORWARD_ROOT:
NOT EXECUTABLE.

New history, unresolved-turn locking and transcript selection use persisted root_conversation_key.

Root decision is durably persisted while update state is still CLAIMED, before provider execution.

## Candidate additive schema

Nullable additions only:

- inbound_reply_to_message_id INTEGER
- inbound_reply_to_message_thread_id INTEGER
- stable_conversation_root_id TEXT
- root_derivation_class TEXT
- root_evidence_update_id INTEGER
- root_conversation_key TEXT

No table replacement.
No destructive rewrite.
No old conversation_key rewrite.
No transcript rewrite.
No historical root/lineage backfill.

Legacy rows remain NULL in new root fields.

## Effect ordering

Implemented ordering:

parse/admit
-> claim
-> persist deterministic root decision
-> history by root-r0.1 key
-> provider
-> durable SENDING
-> one send
-> bounded returned evidence
-> atomic transcript/outbound/root relation
-> COMMITTED/FALLBACK_COMMITTED

Successful send followed by persistence failure:
OUTCOME_UNKNOWN

Replay:
no blind resend and no second provider/send effect.

## Offline verification

Final candidate:
py_compile PASS
54/54 PASS

Required T1-T16:
PASS

Exact parameterized fixture:
PASS

Fixture construction:
Turn1 thread=A
Turn1 outbound=B
Turn2 direct reply target=B
Turn2 observed thread=B
A != B

B is derived from fake outbound transport, not hard-coded from live 110/112 evidence.

Result:
Turn2 derivation = PROVEN_OUTBOUND_LINEAGE
same stable root = PASS
same root-r0.1 conversation_key = PASS
Turn2 receives Turn1 history = PASS
numeric B==thread treated as Telegram semantics = NO

Migration:
- current observability schema first run PASS
- second run idempotency PASS
- older r0.2 additive migration PASS
- historical conversation_key unchanged PASS
- legacy transcript readable PASS
- root backfill NONE

Replay/effect/privacy:
- duplicate update one effect max PASS
- post-send root persistence failure OUTCOME_UNKNOWN/no resend PASS
- unknown reply no merge PASS
- ambiguous outbound lookup no merge PASS
- conflicting anchor no merge PASS
- cross-chat no merge PASS
- direct-topic mode isolation PASS
- FALLBACK_COMMITTED lineage PASS
- root decision before provider PASS
- privacy bounded projection PASS
- automatic-forward deferred: root creation NO / tester widening NO / provider calls 0 / send effects 0 PASS
- forum vs linked-discussion namespace separation PASS

## Predecessor regression note

Exact predecessor source and tests were first run together unchanged:
35/35 PASS.

The unmodified predecessor test file was also probed against the candidate source:
34/35 PASS.

The single old failure is the predecessor pruning fixture, which sent repeated turns with message_thread_id=0 and implicitly expected them to share history. Under root-r0.1, missing root evidence must fail closed and those turns are intentionally isolated.

The final candidate regression changes only that pruning fixture to use an explicit proven thread anchor; the bounded pruning property then passes inside the final 54/54 suite.

This is disclosed as an intentional semantic incompatibility of an obsolete fixture, not hidden as a regression PASS.

## Package content

- dialogue_mvp.py
- test_dialogue_mvp.py
- config.example.json
- ROOT-SEMANTICS.md
- ROOT-SCHEMA.json
- MIGRATION.md
- README.md
- PREDECESSOR-DIFF.patch
- TEST-PREDECESSOR-DIFF.patch
- OFFLINE-TEST-REPORT.json
- SHA256SUMS
- PACKAGE-IDENTITY.txt
- MANIFEST.json

## Boundaries

live /opt mutation:
NONE

live DB read/write/schema mutation:
NONE

install:
NOT_PERFORMED

service start/enable:
NOT_PERFORMED

Telegram calls:
0

OpenAI calls:
0

runtime.json mutation:
NONE

allowlist mutation:
NONE

credential reads/mutation:
0

failed live task replay:
NOT_PERFORMED

approval_status:
IMPLEMENTATION_CANDIDATE_NOT_INSTALLED

## Exact next gate

SIS independent implementation/offline-package review only.

No install/live authority is created by this result.

---
КТО: KOD / КОДЕР v0.6
СТАТУС: IMPLEMENTATION_CANDIDATE_NOT_INSTALLED
