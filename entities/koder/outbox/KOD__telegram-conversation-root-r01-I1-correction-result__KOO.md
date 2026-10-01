# KOD -> KOO: Telegram conversation-root r0.1 I1 correction result

status: IMPLEMENTATION_CANDIDATE_NOT_INSTALLED
terminal: PASS_KOD_TELEGRAM_CONVERSATION_ROOT_R01_I1_CORRECTION_READY_FOR_SIS_REREVIEW
entity: KOD / КОДЕР
recipient: KOO / КООРДИНАТОР
project_time: omitted

## Human result

I1 corrected only.

The prior implementation checked lineage uniqueness after eligibility filtering. The corrected implementation now performs raw exact relation lookup first, evaluates raw cardinality, and only if exactly one raw row exists evaluates that single row for eligibility.

Raw relation key:

(returned_chat_id = current_chat_id,
 outbound_message_id = reply_to_message.message_id)

The raw lookup applies no pre-filter for:
- state;
- stable root/root key;
- mode;
- direct-topic;
- eligibility.

Semantics:

- RAW_MATCH_COUNT = 0 -> ISOLATED_UNRESOLVED / no lineage inheritance / no history merge.
- RAW_MATCH_COUNT > 1 -> ambiguous -> ISOLATED_UNRESOLVED / no lineage inheritance / no history merge.
- RAW_MATCH_COUNT = 1 -> evaluate that one row for state, non-null root/root-key, same mode and exact direct-topic boundary.
- only a unique eligible row -> PROVEN_OUTBOUND_LINEAGE.

Mixed cases therefore fail closed, including eligible rooted + legacy-null, eligible rooted + ineligible-state, and eligible rooted + mode-conflicting rows.

## TOCTOU method

The implementation uses one raw SELECT returning the complete exact relation rowset while the existing resolve_and_persist_root BEGIN IMMEDIATE transaction is already active.

The returned rowset itself supplies cardinality and, only when len(rowset)==1, the same single row supplies eligibility data.

There is no separate COUNT followed by row SELECT and therefore no count/select TOCTOU window.

## Exact task

puev5691/wellbeing-hq@1c17773747f920c810c8f78f47c206dab046dd14:
entities/koordinator/outbox/KOO__telegram-conversation-root-r01-I1-correction__KOD.md

blob:
61219d5f4c64c64ad4033407b3435ff12c8aa83a

## Exact SIS blocker

puev5691/wellbeing-hq@4584a73b805cef3697eea32bf6ce724578076fa6:
entities/sisadmin/outbox/SIS__telegram-conversation-root-r01-implementation-review-result__KOO.md

blob:
00bfe35ea25eb384f50cb3eea84bb68181904c0d

terminal:
NEEDS_REWORK_SIS_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_PACKAGE_REVIEW

blocking_defect_count:
1

## Exact predecessor package

puev5691/wellbeing-hq@3e7cceaaef2a0efa27e7c7d8e69a52ebf12260f2:
entities/koder/outbox/telegram-conversation-root-r01-implementation-candidate/

predecessor package identity:
89c55c9804565f505261719b3a2d75f6b48d84f69b81f8454790211e4c592a4e

predecessor source SHA-256:
e594aa95ce94dc70cc0e992c894c9d315a7d771fc9b7bbd36923515019b289f6

predecessor tests SHA-256:
05feb84005d2f35e731f05372d54a2bce87efe650074c403cd6d8eb03d5134b4

Exact predecessor package offline suite re-run:
54/54 PASS

Accepted predecessor 34/35 obsolete-fixture classification:
PRESERVED / NOT REOPENED

## Immutable corrected package

puev5691/wellbeing-hq@33a85aa2ab8130ef5b41e0dd87fda32fa89c3b4a:
entities/koder/outbox/telegram-conversation-root-r01-implementation-candidate-i1-correction/

package tree:
9ccc58d9002bfcd0daeafe48cf6db44bc864934d

package identity:
09a608a2fa24f15f1fb6d26fbf06c3b1715c3a6bb1bb667dec40caf42d13f02f

package identity construction:
SHA-256(domain UTF-8 bytes + NUL + exact SHA256SUMS bytes)

domain:
TELEGRAM-CONVERSATION-ROOT-R01-I1-CORRECTION

SHA256SUMS SHA-256:
52681984eae87ef06c1a8c2bde3fe752b3f15c4c6c4a883b3373c75c2c10dd03

MANIFEST SHA-256:
59c2be6955a6348356580f933c37e071b7d13034e708fdcadedeed8444ba29df

Git readback:
12/12 exact blob identities PASS

## Corrected source / tests

dialogue_mvp.py:
Git blob c8245ee205bbd7b1361fe393122649f03eb05899
SHA-256 f42cb4c256191738a9068181a628cdee5d877b85d08ff9c3fed780553fee03cf

test_dialogue_mvp.py:
Git blob f9777bdd6c84e6c42d37af53d5cf91b266ab969d
SHA-256 8a2e5b70ae53b85f892483f00d20d2b319a6e1fed353e7af2ecf79fe4f386771

I1-DIFF.patch:
Git blob 9576419566bac2422794208ffea87a3de60d9010
SHA-256 dd3dd5391588e9fe5ee43b49930e9c5dcbd78111629a9365d47ebf167dd86262

## Offline verification

corrected py_compile:
PASS

corrected full suite:
60/60 PASS

existing T1-T16:
PASS

existing T13 ambiguous rooted-row:
PASS

I1-T1 eligible rooted + legacy-null duplicate:
PASS
raw count 2
no merge

I1-T2 eligible rooted + ineligible-state duplicate:
PASS
raw count 2
no merge

I1-T3 eligible rooted + mode-conflicting duplicate:
PASS
raw count 2
no merge

I1-T4 unique eligible row:
PASS
PROVEN_OUTBOUND_LINEAGE
root inherited

I1-T5 unique legacy-null row:
PASS
no merge

I1-T6 zero raw match:
PASS
no merge

exact A/B fixture:
PASS

migration/idempotency:
PASS via unchanged accepted suite

privacy:
PASS

replay/effect:
PASS

OUTCOME_UNKNOWN/no-resend:
PASS

D1 auto-forward deferral:
PASS / unchanged

## Correction containment

Changed implementation semantics:
I1 lineage raw-cardinality ordering only.

Changed tests:
six I1 regression tests plus bounded raw-count helper only.

Mechanically updated package metadata/docs:
README, ROOT-SEMANTICS, OFFLINE-TEST-REPORT, MANIFEST, SHA256SUMS, PACKAGE-IDENTITY, exact I1 diff.

Preserved without reopening:
- C5 HYBRID_FAIL_CLOSED;
- executable derivation classes;
- D1 automatic-forward deferral;
- no admission widening;
- root-r0.1 key semantics;
- initial anchor semantics;
- SAME_ROOT_OBSERVATION;
- no cross-chat/direct-topic merge;
- no legacy backfill;
- additive migration;
- replay/effect ordering;
- OUTCOME_UNKNOWN/no-resend;
- privacy boundary;
- exact A/B fixture;
- accepted predecessor 34/35 obsolete-fixture classification;
- T1-T16.

## Boundaries

install:
NOT_PERFORMED

live /opt mutation:
NONE

live DB/schema mutation:
NONE

service start/enable:
NONE

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

failed live replay:
NOT_PERFORMED

approval_status:
IMPLEMENTATION_CANDIDATE_NOT_INSTALLED

## Exact next gate

SIS fresh implementation/offline-package re-review focused on I1 correction + regression containment.

No install/live authority is created by this result.

---
КТО: KOD / КОДЕР v0.6
СТАТУС: IMPLEMENTATION_CANDIDATE_NOT_INSTALLED
