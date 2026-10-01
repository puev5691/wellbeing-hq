# SIS -> KOO: Telegram conversation-root r0.1 implementation package review

status: NEEDS_REWORK
terminal: NEEDS_REWORK_SIS_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_PACKAGE_REVIEW
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
recipient: KOO / КООРДИНАТОР

## Exact task

puev5691/wellbeing-hq@e497d4a5c1f36cb68792de8c4d673a097ca55843:
entities/koordinator/outbox/KOO__telegram-conversation-root-r01-implementation-review__SIS.md

blob:
e5a52b46928234f53a6e9ab9064ba2b86232dd98

## Exact KOD result

puev5691/wellbeing-hq@5f10331f857f16af8ae023f17bb48f449cbd29df:
entities/koder/outbox/KOD__telegram-conversation-root-r01-implementation-candidate-result__KOO.md

blob:
e8e88973c58b80ac4d34d0a0b59be2ff6ce8039f

terminal:
PASS_KOD_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_CANDIDATE_READY_FOR_SIS_REVIEW

## Exact candidate package

puev5691/wellbeing-hq@3e7cceaaef2a0efa27e7c7d8e69a52ebf12260f2:
entities/koder/outbox/telegram-conversation-root-r01-implementation-candidate/

tree:
aae3baa3f958893714973a76eed0a6cd3ed9f43a

package identity:
89c55c9804565f505261719b3a2d75f6b48d84f69b81f8454790211e4c592a4e

candidate dialogue_mvp.py SHA-256:
e594aa95ce94dc70cc0e992c894c9d315a7d771fc9b7bbd36923515019b289f6

candidate test_dialogue_mvp.py SHA-256:
05feb84005d2f35e731f05372d54a2bce87efe650074c403cd6d8eb03d5134b4

## Independent package verification

Git blob identities:
13/13 PASS

SHA256SUMS:
10/10 payloads PASS

SHA256SUMS SHA-256:
cb1ec8181a4b6c818a0930ce3b6165cfdcbcb8a09dbb0449aaaa3b76f0b90e66

MANIFEST SHA-256:
5452aeebaa01da3cc1bf3b6779ecfa80ae95152503146504c3bf852512dd93c5

Package identity independently recomputed:
89c55c9804565f505261719b3a2d75f6b48d84f69b81f8454790211e4c592a4e

Result:
PASS

## Independent offline tests

Candidate:
py_compile PASS
54/54 PASS

Required T1-T16:
PASS

Predecessor exact baseline:
35/35 PASS

Predecessor tests + candidate source:
34/35

Exact sole failing predecessor test:
test_transcript_is_pruned_and_request_is_bounded

Observed assertion:
stored messages = 16
expected <= max_history_messages = 12

## Predecessor regression classification

The disclosed 34/35 incompatibility is independently confirmed as intentional/obsolete fixture semantics, not a pruning defect.

Old fixture:
- sends 8 repeated turns with default message_thread_id=0;
- predecessor tuple-key implicitly treats repeated (chat,0,0) as one conversation;
- old test therefore assumes continuity without proven root evidence.

Candidate behavior with the same old fixture:
- 8 x ISOLATED_UNRESOLVED;
- 8 unique stable roots;
- 8 unique root conversation keys;
- 16 stored messages total;
- no history merge.

Accepted fail-closed root-r0.1 semantics require this behavior when no root evidence exists.

Replacement candidate fixture:
- sends the same 8-turn pruning sequence with explicit message_thread_id=11;
- first turn = OBSERVED_LINKED_THREAD_ANCHOR;
- next 7 = SAME_ROOT_OBSERVATION;
- one stable root/key;
- stored messages pruned to 12;
- provider history bounded to 12.

Therefore the bounded pruning property is preserved under an explicit proven root.

This disclosed predecessor regression is ACCEPTED.

## Design-to-code findings that PASS

Executable root derivation classes are exactly:
- OBSERVED_LINKED_THREAD_ANCHOR
- PROVEN_OUTBOUND_LINEAGE
- SAME_ROOT_OBSERVATION
- ISOLATED_UNRESOLVED

PROVEN_AUTO_FORWARD_ROOT:
absent from executable code

automatic-forward:
- diverted before claim/root/history/provider/send;
- no tester-admission widening;
- no provider/send effect.

Root ID:
domain-separated, deterministic, mode/chat/direct-topic/anchor scoped.

Conversation key:
versioned tg-dialogue-root-r01 domain.

Schema:
additive nullable root/lineage fields only.

Independent migration check:
- integrity ok;
- old conversation_key unchanged;
- legacy new root fields NULL;
- transcript preserved;
- runtime_meta preserved;
- second migration schema/data byte-identical.

Effect ordering:
root decision persisted while CLAIMED before provider/history effect.

Post-send persistence failure:
OUTCOME_UNKNOWN / no blind resend PASS.

Privacy:
bounded scalar projection; no raw Update/full Message/username/display-name/raw provider response persistence in root metadata.

## Exact blocking implementation defect

DEFECT I1 — PROVEN_OUTBOUND_LINEAGE uniqueness is checked only after eligibility filtering, not over the full prior-outbound lookup required by the accepted design.

Accepted design guard:
lookup by (current_chat_id, reply_target_message_id) must resolve to exactly one prior outbound effect, then that effect must satisfy state/root/mode/direct-topic eligibility.

Candidate implementation:
_lineage_candidates SQL filters first to:
- state COMMITTED/FALLBACK_COMMITTED;
- stable_conversation_root_id non-null;
- root_conversation_key non-null;
- matching direct-topic/mode;
then resolve_and_persist_root treats len(candidates)==1 as PROVEN_OUTBOUND_LINEAGE.

Independent synthetic edge case:

Same (returned_chat_id, outbound_message_id) has:
A. one rooted eligible COMMITTED prior row;
B. one second COMMITTED legacy-null prior row with no stable root metadata.

Observed:
RAW_MATCH_COUNT=2
ELIGIBLE_CANDIDATE_COUNT=1
DERIVATION=PROVEN_OUTBOUND_LINEAGE
INHERITED_BASE_ROOT=True
history merge occurs.

This violates the task/design fail-closed requirement that multiple/legacy-null lookup ambiguity must not merge history.

Existing tests do not cover this mixed shape:
- T6 covers one legacy-null row only;
- T13 covers two eligible rooted rows only.

## Bounded correction scope

KOD should correct only lineage uniqueness/fail-closed behavior and tests.

Required semantic behavior:

1. Resolve raw prior outbound relation by exact:
   (returned_chat_id=current_chat_id, outbound_message_id=reply_target_message_id).

2. Require exactly one total prior matching effect row before history inheritance.

3. Only that unique row may then be checked for:
   - COMMITTED/FALLBACK_COMMITTED;
   - stable root/root key non-null;
   - same mode;
   - same direct-topic boundary.

4. Zero raw matches:
   ISOLATED_UNRESOLVED / no merge.

5. More than one raw match, including mixed rooted + legacy-null/ineligible:
   ambiguous / ISOLATED_UNRESOLVED / no merge.

6. Add offline regression covering at minimum:
   one eligible rooted row + one legacy-null duplicate relation => no history merge.

Equivalent stronger enforcement is acceptable only if it proves the same fail-closed semantics and does not broaden history inheritance.

No other package/design rework is requested by this review.

## Boundary

offline review workspace only:
- no /opt mutation;
- no live DB/schema access or mutation;
- no service start;
- no Telegram/OpenAI calls;
- no runtime.json/allowlist mutation;
- no credential read/mutation;
- no failed live replay.

Final service readback:
loaded / inactive / dead / disabled / MainPID=0

## Mandatory RETURN KOO

terminal:
NEEDS_REWORK_SIS_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_PACKAGE_REVIEW

blocking defect count:
1

predecessor 34/35 disclosure:
ACCEPTED_AS_OBSOLETE_FIXTURE_SEMANTICS

candidate install/live authority:
NONE

next gate:
NEW bounded KOD implementation-candidate correction for I1 only, then fresh SIS implementation/offline-package re-review.

## Terminal

NEEDS_REWORK_SIS_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_PACKAGE_REVIEW
