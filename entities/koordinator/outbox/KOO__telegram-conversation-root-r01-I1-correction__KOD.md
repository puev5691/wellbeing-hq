# KOO -> KOD: Telegram conversation-root r0.1 implementation candidate I1 correction-only

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

## Exact SIS review result

puev5691/wellbeing-hq@4584a73b805cef3697eea32bf6ce724578076fa6:
entities/sisadmin/outbox/SIS__telegram-conversation-root-r01-implementation-review-result__KOO.md

blob:
00bfe35ea25eb384f50cb3eea84bb68181904c0d

terminal:
NEEDS_REWORK_SIS_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_PACKAGE_REVIEW

blocking defect count:
1

predecessor 34/35 disclosure:
ACCEPTED_AS_OBSOLETE_FIXTURE_SEMANTICS

## Exact predecessor implementation candidate

puev5691/wellbeing-hq@3e7cceaaef2a0efa27e7c7d8e69a52ebf12260f2:
entities/koder/outbox/telegram-conversation-root-r01-implementation-candidate/

package tree:
aae3baa3f958893714973a76eed0a6cd3ed9f43a

package identity:
89c55c9804565f505261719b3a2d75f6b48d84f69b81f8454790211e4c592a4e

candidate dialogue_mvp.py SHA-256:
e594aa95ce94dc70cc0e992c894c9d315a7d771fc9b7bbd36923515019b289f6

candidate test_dialogue_mvp.py SHA-256:
05feb84005d2f35e731f05372d54a2bce87efe650074c403cd6d8eb03d5134b4

status:
IMPLEMENTATION_CANDIDATE_NOT_INSTALLED

## Scope

Perform ONLY I1 correction.

Do not reopen accepted package/design findings except where directly required for this correction.

Do NOT:
- install;
- mutate live /opt;
- mutate live DB/schema;
- start/enable service;
- call Telegram;
- call OpenAI;
- mutate runtime.json;
- mutate allowlist;
- read/mutate credentials;
- replay failed live task;
- create production/live authority.

## I1 defect

Current candidate checks uniqueness after eligibility filtering.

This is unsafe.

Accepted design requires:
raw lookup by exact relation first,
then cardinality check,
then eligibility.

Exact relation key:

(returned_chat_id = current_chat_id,
 outbound_message_id = reply_target_message_id)

## Required corrected semantics

### Step 1. Raw lookup

Perform exact raw lookup over ALL prior rows matching:

- returned_chat_id = current chat
- outbound_message_id = reply_to_message.message_id

Do not pre-filter by:
- state;
- stable root presence;
- root key presence;
- mode;
- direct-topic;
- eligibility.

Let:
RAW_MATCH_COUNT = total exact relation rows.

### Step 2. Raw cardinality gate

If RAW_MATCH_COUNT == 0:
- no lineage inheritance;
- ISOLATED_UNRESOLVED / fail-closed;
- no history merge.

If RAW_MATCH_COUNT > 1:
- classify ambiguous;
- no lineage inheritance;
- ISOLATED_UNRESOLVED or equivalent fail-closed state;
- no history merge;
- no provider/history selection from prior root.

This includes mixed cases such as:
- one eligible rooted row;
- one legacy-null row;
- one ineligible state row;
- one mode-conflicting row.

The mere existence of multiple raw relation rows blocks inheritance.

### Step 3. Eligibility of unique row

Only if RAW_MATCH_COUNT == 1 may the unique row be evaluated for eligibility.

Required eligibility:
- state COMMITTED or FALLBACK_COMMITTED;
- stable_conversation_root_id non-null;
- root_conversation_key non-null;
- same mode;
- same direct-topic boundary;
- same chat already proven by raw key.

If unique row fails any eligibility requirement:
- no merge;
- ISOLATED_UNRESOLVED / fail-closed.

Only if unique row passes all:
- PROVEN_OUTBOUND_LINEAGE;
- inherit exact prior stable root;
- inherit root conversation key.

## Required code correction

Correct the implementation so uniqueness is enforced over raw exact relation rows before eligibility filtering.

Acceptable structures include:
- one raw SELECT then in-code eligibility;
- raw COUNT + unique-row SELECT under same deterministic transaction/snapshot;
- equivalent stronger design.

But do NOT introduce TOCTOU between count and row selection.

If two SQL operations are used:
- they must observe one consistent transaction/snapshot;
- or use one query shape that returns enough evidence atomically.

Document exact method.

## Required regression tests

Add at minimum:

### I1-T1 mixed rooted + legacy-null duplicate

Same exact:
(returned_chat_id, outbound_message_id)

Row A:
- COMMITTED
- stable root/root key present
- otherwise eligible

Row B:
- COMMITTED
- stable root/root key NULL

Expected:
RAW_MATCH_COUNT=2
NO PROVEN_OUTBOUND_LINEAGE
NO history merge
ISOLATED_UNRESOLVED/fail-closed

### I1-T2 rooted + ineligible-state duplicate

Row A eligible rooted.
Row B exact same relation but state not COMMITTED/FALLBACK_COMMITTED.

Expected:
raw count 2
no merge.

### I1-T3 rooted + mode-conflicting duplicate

Same raw relation, one eligible same-mode and one mode-conflicting row.

Expected:
raw count 2
no merge.

### I1-T4 unique eligible row

Exactly one raw match and eligible.

Expected:
PROVEN_OUTBOUND_LINEAGE
root inherited.

### I1-T5 unique legacy-null row

Exactly one raw match but root/root key NULL.

Expected:
no merge.

### I1-T6 zero raw match

Expected:
no merge.

Existing T13 ambiguous two rooted rows must still PASS.

## Preserve accepted findings

Unless directly touched by I1, preserve:

- C5 HYBRID_FAIL_CLOSED;
- executable derivation classes;
- D1 automatic-forward deferral;
- no admission widening;
- root-r0.1 key semantics;
- initial anchor semantics;
- same-root observation;
- no cross-chat/direct-topic merge;
- no legacy backfill;
- migration additive-only;
- replay/effect ordering;
- OUTCOME_UNKNOWN/no-resend;
- privacy boundary;
- exact A/B fixture;
- accepted predecessor 34/35 obsolete-fixture classification;
- T1-T16 existing coverage.

## Offline verification

Run only offline/disposable:

- py_compile;
- full candidate suite;
- existing T1-T16;
- new I1-T1 through I1-T6;
- exact predecessor baseline if package procedure requires;
- predecessor regression probe may be re-run but its accepted semantic classification must not be reopened absent new evidence;
- migration/idempotency;
- replay/effect/privacy tests;
- exact A/B fixture.

No Telegram/OpenAI calls.

## Output

Create one NEW immutable corrected implementation package, for example:

entities/koder/outbox/telegram-conversation-root-r01-implementation-candidate-i1-correction/

Include:
- corrected dialogue_mvp.py;
- corrected tests;
- exact I1 diff/patch;
- updated test report;
- manifest;
- SHA256SUMS;
- package identity;
- predecessor package identity;
- statement only I1-related implementation/test changes plus mechanically required metadata changed.

Status:
IMPLEMENTATION_CANDIDATE_NOT_INSTALLED

## Expected terminal

PASS_KOD_TELEGRAM_CONVERSATION_ROOT_R01_I1_CORRECTION_READY_FOR_SIS_REREVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- exact corrected package/tree/package identity;
- source/test hashes;
- exact raw-cardinality implementation method;
- I1-T1..I1-T6 results;
- full suite result;
- T1-T16 result;
- replay/effect/privacy regression result;
- exact A/B fixture result;
- live mutation=NONE;
- network calls=0;
- status IMPLEMENTATION_CANDIDATE_NOT_INSTALLED;
- exact next gate:
  SIS fresh implementation/offline-package re-review focused on I1 correction + regression containment.

Then STOP.
