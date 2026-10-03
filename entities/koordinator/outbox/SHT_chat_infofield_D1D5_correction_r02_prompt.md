# SHT — CHAT_TO_INFORMATION_FIELD_MATERIALIZATION_GAP correction D1-D5 r0.2

conveyor_attempt: SHT_CHAT_INFOFIELD_CANDIDATE_CORRECTION_D1_D5_R02_A1
attempt_state: AWAITING_OPERATOR_TRANSFER
project_time: omitted

АДРЕСАТ: ШТАБИСТ / SHT

Resume-First.

Выполни ТОЛЬКО bounded correction-only successor exact SHT candidate package CHAT_TO_INFORMATION_FIELD_MATERIALIZATION_GAP по замечаниям D1-D5 независимого KAN review.

Не replay исходную r0.1 task как будто она снова current.
Не меняй Project Sources/canons.
Не активируй candidate/effectivity.
Не запускай implementation/runtime/automation.
Не создавай KOD task или task authority другой Сущности.
Не реконструируй и не replay historical KOD v0.6 chat-only work.

## Exact OPERATOR authority

ОПЕРАТОР явно решил в текущем KOO r1.1 chat:

AUTHORIZE_SHT_CHAT_INFOFIELD_CANDIDATE_CORRECTION_D1_D5_R02 = YES

Authority scope:
one bounded SHT correction-only successor limited strictly to D1-D5 below.

This authority permits:
- fresh currentness verification;
- creation of one new immutable corrected CANDIDATE_NOT_ACTIVE successor package;
- correction of the exact documentary candidate semantics/fixtures/source-impact required by D1-D5;
- terminal result back to KOO.

This authority does NOT permit:
- Project Source/canon amendment or approval;
- source-set activation/effectivity;
- candidate activation;
- implementation/runtime/automation;
- production authority;
- historical task replay;
- KOD task creation;
- automatic adoption after correction.

## KOO current authority / reconciliation basis

Current KOO writer:

puev5691/wellbeing-hq@a7214a3e227844698b6968556dc28102cc5af363:
entities/koordinator/current/KOO__replacement-current-writer-r11.md

blob:
d0e74b6a22ddd1880f725786a313d067aaace2c2

terminal:
PASS_KOO_REPLACEMENT_CURRENT_WRITER_R11

KAN NEEDS_REWORK reconciliation:

puev5691/wellbeing-hq@b7aa7ae24f94c66e7c0e70ab3e6eb2bafa49d303:
entities/koordinator/outbox/KOO__chat-infofield-rework-reconciliation-r01__OPERATOR.md

blob:
bd3c41f4d6e84aaa9915472b99a30b4a550647ec

terminal:
PASS_KOO_CHAT_INFOFIELD_REWORK_RECONCILIATION_WAITING_OPERATOR_DECISION

That decision gate is now resolved only for this exact correction by the OPERATOR authority above.

## Current SHT writer

Verify fresh before profile work.

puev5691/wellbeing-hq:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md

blob:
a019c21cffeb99bb7c387b8fa95a4629137dc6da

status:
CURRENT_WRITER

writer_generation:
SHT-CURRENT-INSTANCE-R01

Exact writer artifact states that any next task requires fresh reconciliation after Writer Gate and does not itself create task authority. This PROMPT carries the exact OPERATOR correction authority for this step.

## Original SHT candidate r0.1

Terminal:

puev5691/wellbeing-hq@53c59a8b9534bf27ed7d842e7edfe2d854cccdef:
entities/shtabist/outbox/SHT__chat-infofield-materialization-gap-r01__KOO.md

blob:
649c52279f858f8618b94460bbb2671477a94871

terminal:
PASS_SHT_CHAT_INFOFIELD_MATERIALIZATION_GAP_R01_CANDIDATE_READY_FOR_REVIEW

status:
CANDIDATE_NOT_ACTIVE

Original package:

puev5691/wellbeing-hq@53c59a8b9534bf27ed7d842e7edfe2d854cccdef:
entities/shtabist/outbox/chat-infofield-materialization-gap-r01/

tree:
583a8b42059fe088c9afe9a0471a3af8f73263c3

Exact composition:

ARCHITECTURE.md
blob 40af4b9ab1988bde479de67b7c50087849fe6128

CAUSAL-EVENTS.md
blob f452f16bc1e60674a05b4e02720bcd305ede11d3

CRASH-REPLACEMENT-MATRIX.md
blob 8d1cc3d4800f676cb6bc069db6e64386d67a5e80

DURABLE-EXECUTION-STATE.md
blob e7942ae00ddbbcc07df9b576e68b54d11c0dd267

FIXTURES.md
blob dcbbb6b7bee3a2e6512af60bc544148145ca35fb

INVARIANTS.md
blob b2a31e3b54a8626a6fa83cbf787ff2af1b5a6af1

MANIFEST.md
blob 198b5d341f4c773a4c52ec4f57cd26ea4c3b25e8

NEXT-GATES.md
blob 9d6e4804b3e41cd299d9aa77e0d38f0efbc16a53

SOURCE-IMPACT.md
blob 9c03230a9820c0383978ce685c1a46eaf72c394e

STATE-TRANSITIONS.md
blob 812aa29b1570b7212cf8e9d4e010a8ca559f2411

Original package remains immutable historical evidence.
Do not overwrite r0.1.

## Independent KAN review

puev5691/wellbeing-hq@f849355ed228036dc6b3b24a38a1baeed9fcb7e6:
entities/kancelar/outbox/KAN__chat-infofield-candidate-review-r01__KOO.md

blob:
203eb772fe9e137ec9d139b7bccade6e5d169c4c

terminal:
NEEDS_REWORK_KAN_CHAT_INFOFIELD_CANDIDATE_REVIEW_R01

status:
INDEPENDENT_NORMATIVE_SOURCE_IMPACT_REVIEW_COMPLETE

candidate_status:
CANDIDATE_NOT_ACTIVE

The KAN review is correction evidence only.
It creates no task authority by itself.

## Correction D1 — observed state / event evidence / attempt / CAS

Correct candidate semantics so that:

1. Missing start evidence means PROCESSING_NOT_PROVEN / UNKNOWN, not factual NOT_STARTED.
2. NOT_STARTED requires explicit valid initial state for the exact execution attempt and a verified current event/state frontier.
3. Unverifiable authority means AUTHORITY_NOT_ESTABLISHED for the proposed transition; no reconstruction and no execution.
4. Add or make unambiguous:
   - execution_attempt identity (or explicitly define state_id as exact task-attempt identity);
   - actor/instance identity;
   - predecessor/current version identity;
   - causal event identity.
5. DURABLE_TASK_BOUNDARY_READY / equivalent boundary predicate makes processing eligible only. PROCESSING_STARTED is a separate evidenced event for the exact processing instance/attempt.
6. Scheduling, publication, dispatch, activation_requested, inbox or readback do not prove PROCESSING_STARTED.
7. prior_state_ref alone is not CAS. Define a documentary conditional-acceptance model:
   - declared task-attempt scope;
   - exact expected current version;
   - conditional successor acceptance;
   - accepted successor acknowledgement/readback;
   - stale branch rejection/preservation;
   - current-writer/currentness revalidation at acceptance.
8. An old writer holding an old reference cannot commit authoritative successor state after replacement merely because the reference exists.
9. Preserve WRITER_NOT_REQUIRED_FOR_TASK where active Recovery allows independently authorized worker/read-only work; the candidate must not silently require a new authoritative writer for every task.
10. Missing predicate/currentness/acceptance evidence => UNKNOWN/BLOCK for the dependent transition.
11. No last-write-wins.

Do not choose or implement a backend/CAS engine.

## Correction D2 — pre-start initial state / checkpoint / crash tail

Correct ordering and evidence scope so that:

1. Pre-start durable object is named initial NOT_STARTED state / durable task-boundary materialization, not CHECKPOINT_DURABLE.
2. CHECKPOINT_DURABLE requires separately evidenced PROCESSING_STARTED.
3. A checkpoint proves only the exact execution prefix and evidence scope it covers.
4. Any possible unmaterialized post-checkpoint effect remains UNKNOWN.
5. Overlapping retry/resume is blocked until the affected tail and external-effect outcome are reconciled.
6. For consequential external effects define documentary:
   - durable pre-effect operation identity/intent;
   - separately evidenced outcome OR explicit unresolved status.
7. Crash between effect and post-effect checkpoint remains unresolved; no automatic replay.
8. Intent is not execution and creates no new authority.
9. Do not claim exactly-once, production durability, RECOVERY_READY or admitted shard/storage durability from this candidate checkpoint.
10. CHECKPOINT_DURABLE here is only candidate task-progress evidence with explicit scope.

## Correction D3 — terminal fact independent of next disposition

Correct the candidate so that:

1. Terminal evidence is recorded immediately when the declared task terminal criterion is met.
2. Missing next disposition does NOT:
   - erase terminal;
   - return execution to RESULT_PENDING;
   - justify profile replay.
3. Add/define separate derived property:
   TERMINAL_COMPLETE_FOR_CONTINUITY
   = terminal evidence + verified next causal disposition.
4. Missing disposition means:
   NEXT_DISPOSITION_MISSING
   and reconciliation only for that dependency.
5. Allow terminal PASS/FAIL/BLOCKED from any state where the actual terminal criterion is met; do not force every path through RESULT_PENDING.
6. Do not invent pending-result artifacts.
7. Keep separately:
   - task terminal;
   - parent/composite completion;
   - receipt;
   - acceptance;
   - next-task authority;
   - next causal disposition.

## Correction D4 — documentary fixtures / honest PASS claims

Correct FIXTURES / terminal claims so that:

1. GAP1-GAP10 bare machine-decidable PASS claims become documentary EXPECTED_BEHAVIOR / DOCUMENTARY_CASE until independently supported.
2. For each GAP1-GAP10 provide compact fields:
   - exact bounded input evidence/state;
   - attempt/applicability identity;
   - predicate evaluated;
   - expected output;
   - UNKNOWN/conflict alternative.
3. Synthetic fixture inputs must be explicitly labeled SYNTHETIC and must not be represented as historical KOD evidence.
4. GAP2 requires explicit current initial-state evidence.
5. GAP4 applies D2 prefix/tail rule.
6. GAP5 preserves TERMINAL while continuity remains incomplete.
7. GAP7 requires independent current task authority.
8. GAP9 must not collapse NO and UNKNOWN without evidence.
9. Bind all conclusions to durable causal evidence, not chronology or chat recollection.
10. Candidate may claim proposed machine-decidable field checks; it may not claim successful runtime execution or factual truth merely from prose PASS.

No code/simulator/live test is required by this correction task.

## Correction D5 — exact source impact / effectivity boundary

Replace tentative source-impact wording with the bounded conditional classification from KAN review:

### Task Conveyor Canon v1.2
- CANON_AMENDMENT_REQUIRED only if later adoption makes the new durable-start/continuity-complete prerequisite universal.
- PROFILE_OR_ADDENDUM_SUFFICIENT for an explicitly bounded compatible optional process.
- Do not redefine actual task terminal criterion.
- Do not manufacture successor authority.

### Recovery Canon v1.6
- PROFILE_OR_ADDENDUM_SUFFICIENT for consuming exact execution evidence under existing gates.
- CANON_AMENDMENT_REQUIRED only if later adoption creates an additional universal recovery/resume gate or changes writer/worker outcomes.
- Execution-state evidence is a dependency, not a replacement self-snapshot, recovery package or writer grant.

### Project Core v2.5
GLOBAL_CORE_ELEVATION_NOT_JUSTIFIED.

### File Work Canon v2.4
NO_CHANGE_NEEDED.
Reuse existing identity/publication/readback/minimal-document/privacy mechanics.
Do not invent a mandatory second store or duplicate report.

### SECE reviewed architecture boundary
PROFILE_OR_ADDENDUM_SUFFICIENT for documentary integration.
UNKNOWN_NEEDS_MORE_EVIDENCE for executable integration.
Do not make EFFECTIVE_CONTEXT authoritative execution storage or extend prior review PASS to this new integration.

### Entity Roles v2.4 / Source Loading v2.2
NO_CHANGE_NEEDED.

Effectivity remains absent until an exact later decision defines scope and activation.
This correction task does not draft/apply canon amendments.

## Active approved baseline

Verify fresh before substantive correction:

project-instructions-core v2.5
blob a42f7dca6a7469a54fa2da24aae0da4e549c9d33

entity-roles-short v2.4
blob 1772339cb74dae8550bfbd2e33401c34a929e911

source-loading-policy v2.2
blob 69eb657f260a019f76e8e707c880ea88c1dfa0bf

entity-state-preservation-and-recovery-canon v1.6
blob 233117e1c9509d730e1f5ec532b1cabe3f786609

file-work-canon-universal v2.4
blob e9c29d62057f34e4f771d6057a36d9b7f72e74c2

task-conveyor-canon v1.2
blob df7896d867eeeffff506319538fedad938856686

Do not treat any candidate/draft as active canon.

## Required successor output

Create ONE new immutable successor package without overwriting r0.1:

entities/shtabist/outbox/chat-infofield-materialization-gap-r02/

Use the same functional package shape unless a file is genuinely no longer needed:

ARCHITECTURE.md
CAUSAL-EVENTS.md
CRASH-REPLACEMENT-MATRIX.md
DURABLE-EXECUTION-STATE.md
FIXTURES.md
INVARIANTS.md
MANIFEST.md
NEXT-GATES.md
SOURCE-IMPACT.md
STATE-TRANSITIONS.md

Avoid extra documents merely for form.

Each unchanged proposition may be preserved verbatim or by exact reference where the package remains self-contained enough for review; all D1-D5 affected statements must be corrected explicitly.

Status:
CANDIDATE_NOT_ACTIVE

Required terminal result:

entities/shtabist/outbox/SHT__chat-infofield-materialization-gap-r02__KOO.md

Expected terminal:

PASS_SHT_CHAT_INFOFIELD_MATERIALIZATION_GAP_R02_CORRECTED_CANDIDATE_READY_FOR_REREVIEW

or exact NEEDS_REWORK/BLOCKED/FAIL.

Terminal result must include:
- exact OPERATOR authority;
- fresh HEAD/preflight boundary;
- exact SHT writer identity/currentness;
- r0.1 predecessor locator/tree;
- exact KAN review locator/blob;
- r0.2 package locator/tree/file blobs;
- D1-D5 correction checklist;
- explicit candidate_status CANDIDATE_NOT_ACTIVE;
- explicit Project Source/canon mutation NONE;
- explicit candidate activation/effectivity NONE;
- historical KOD v0.6 reconstruction/replay NONE;
- implementation/runtime/automation NONE;
- next-gate classification only, without creating authority.

## Fresh preflight / stop conditions

Before substantive correction:

1. fetch fresh wellbeing-hq HEAD;
2. verify this PROMPT is not superseded;
3. verify SHT current-writer exact identity and no newer competing writer/handoff;
4. verify no corrected r0.2 terminal/package already exists for this exact lineage;
5. verify r0.1 package exact commit/tree/blobs;
6. verify KAN review exact commit/blob/terminal;
7. verify active six-source baseline has no approved activated successor;
8. verify the OPERATOR authority above is not withdrawn/replaced;
9. verify no second transferable/executable correction PROMPT exists for this exact task lineage.

If any required identity/currentness/authority conflict exists:
STOP with exact BLOCKED result.
Do not repair by inference.

## Execution boundaries

historical r0.1 task replay:
FORBIDDEN

historical KOD v0.6 chat-only reconstruction/replay:
FORBIDDEN

Project Source/canon mutation:
FORBIDDEN

candidate activation/effectivity:
FORBIDDEN

implementation/runtime/automation:
FORBIDDEN

foreign current-state mutation:
FORBIDDEN

new task authority for another Entity:
FORBIDDEN

## Stop after result

After publication, immutable readback and RETURN KOO:
STOP.

Do not proceed into KAN re-review, amendment drafting, approval, adoption, implementation or another Entity task without a new exact authority.
