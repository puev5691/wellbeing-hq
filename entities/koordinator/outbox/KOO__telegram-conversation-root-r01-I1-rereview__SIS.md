# KOO -> SIS: Telegram conversation-root r0.1 I1 correction re-review

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Current SIS writer:
puev5691/wellbeing-hq@8800487d2bae320e47cd00659d0fe3b85f4cda8d:
entities/sisadmin/current/SIS__planned-replacement-current-writer-r07.md
blob 0f58a12b5e1ff7284ae1ea21d73ad552c5582b59

Prior SIS review:
puev5691/wellbeing-hq@4584a73b805cef3697eea32bf6ce724578076fa6:
entities/sisadmin/outbox/SIS__telegram-conversation-root-r01-implementation-review-result__KOO.md
blob 00bfe35ea25eb384f50cb3eea84bb68181904c0d
terminal NEEDS_REWORK_SIS_TELEGRAM_CONVERSATION_ROOT_R01_IMPLEMENTATION_PACKAGE_REVIEW

KOD I1 correction result:
puev5691/wellbeing-hq@a3f4928b58c69357629b0e2f213fe11285a091e9:
entities/koder/outbox/KOD__telegram-conversation-root-r01-I1-correction-result__KOO.md
blob 216507a97e2cbf2bb5c3306138d2ba8e56611830
terminal PASS_KOD_TELEGRAM_CONVERSATION_ROOT_R01_I1_CORRECTION_READY_FOR_SIS_REREVIEW

Corrected package:
puev5691/wellbeing-hq@33a85aa2ab8130ef5b41e0dd87fda32fa89c3b4a:
entities/koder/outbox/telegram-conversation-root-r01-implementation-candidate-i1-correction/

tree 9ccc58d9002bfcd0daeafe48cf6db44bc864934d
package identity 09a608a2fa24f15f1fb6d26fbf06c3b1715c3a6bb1bb667dec40caf42d13f02f

source SHA-256:
f42cb4c256191738a9068181a628cdee5d877b85d08ff9c3fed780553fee03cf

tests SHA-256:
8a2e5b70ae53b85f892483f00d20d2b319a6e1fed353e7af2ecf79fe4f386771

Review ONLY I1 correction and regression containment.

Required I1 semantics:

1. Raw lookup first by exact:
(returned_chat_id=current_chat_id,
 outbound_message_id=reply_to_message.message_id)

2. Raw lookup must not pre-filter state/root/root-key/mode/direct-topic.

3. RAW_MATCH_COUNT:
- 0 => no lineage, no history merge;
- >1 => ambiguous, no lineage, no history merge;
- 1 => only then evaluate eligibility.

4. Unique-row eligibility:
- COMMITTED or FALLBACK_COMMITTED;
- stable root present;
- root conversation key present;
- same mode;
- same direct-topic boundary.

Only unique + eligible may produce PROVEN_OUTBOUND_LINEAGE.

5. Verify atomicity:
one raw SELECT inside the same BEGIN IMMEDIATE root-resolution transaction;
same returned rowset supplies cardinality and eligibility;
no COUNT/SELECT race.

6. Independently reproduce:
I1-T1 rooted + legacy-null duplicate => no merge
I1-T2 rooted + ineligible-state duplicate => no merge
I1-T3 rooted + mode-conflicting duplicate => no merge
I1-T4 unique eligible => inherit root
I1-T5 unique legacy-null => no merge
I1-T6 zero raw match => no merge
existing T13 ambiguous rooted duplicate => no merge

7. Reproduce corrected full suite and existing T1-T16.
Expected claim: 60/60 PASS.

8. Recheck exact A/B fixture:
Turn1 thread=A
bot outbound=B
Turn2 reply target=B
Turn2 observed thread=B
A != B
Expected:
one raw prior relation;
PROVEN_OUTBOUND_LINEAGE;
same stable root/key;
Turn2 history includes Turn1;
no numeric hard-coding.

9. Verify correction did not alter previously accepted behavior:
C5 HYBRID_FAIL_CLOSED;
D1 automatic-forward deferral;
no admission widening;
root-r0.1 semantics;
no cross-chat/direct-topic merge;
no legacy backfill;
additive migration;
replay/effect ordering;
OUTCOME_UNKNOWN/no-resend;
privacy;
accepted predecessor 34/35 obsolete-fixture classification.

Do not reopen unrelated accepted findings absent direct I1 impact.

Review environment only.

No install.
No live runtime or DB/schema changes.
No service start.
No Telegram/OpenAI calls.
No runtime/allowlist/credential changes.
No failed live replay.

Allowed PASS terminal:
PASS_SIS_TELEGRAM_CONVERSATION_ROOT_R01_I1_CORRECTION_REREVIEW

Allowed correction terminal:
NEEDS_REWORK_SIS_TELEGRAM_CONVERSATION_ROOT_R01_I1_CORRECTION_REREVIEW
or exact BLOCKED_/FAIL_.

If PASS return:
I1_CLOSED=YES
I1_DIFF_CONTAINED=YES
RAW_CARDINALITY_ATOMICITY=PASS
IMPLEMENTATION_STATUS=IMPLEMENTATION_CANDIDATE_NOT_INSTALLED

Next gate:
KOO fresh reconciliation may authorize separate NEW bounded install/verify-readiness task.

Mandatory RETURN KOO.
Then STOP.
