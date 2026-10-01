# Semantic Entity Control Engine r0.1 — Architecture Candidate

status: ARCHITECTURE_CANDIDATE_NOT_ACTIVE
terminal: PASS_SHT_SEMANTIC_ENTITY_CONTROL_ENGINE_R01_ARCHITECTURE_CANDIDATE_READY_FOR_KOO_RECONCILIATION

## Purpose
One control/compiler pipeline for PROJECT_OPERATIONS, not a third semantic contour.

Core invariant:
neural interpretation may PROPOSE; compiled active rules CONSTRAIN; deterministic validation admits/rejects; only separately authorized effects execute.

## L0-L9
L0 ACTIVE AUTHORITATIVE SOURCES
Input exact active Sources/current authority evidence. Output verified SourceSet. Deterministic identity/status/applicability. Missing mandatory source=UNKNOWN; active conflict=STOP.

L1 SEMANTIC SEED / INITIATION KERNEL
Input L0 + verified initiation/recovery/role bindings. Output typed normative invariants + instance bindings + semantic self-test. PASS is evaluation only, not admission/authority.

L2 SOURCE→OPERATIONAL RULE COMPILER
Output provenance-bound rules:
MUST, MAY, MUST_NOT, REQUIRES, STOP_IF, AUTHORITY_FROM, INPUT_REQUIRED, OUTPUT_REQUIRED, NEXT_GATE.
Each retains exact source locator/version/blob + semantic basis. Extraction may be neural; provenance/schema/conflict validation deterministic. Derived rule is not authority.

L3 CURRENT STATE + EVENT/TASK BINDING
Bind current-writer, exact task/authority, terminal/supersession and verified current delta. Never infer task from writer, recovery, inbox, dispatch, capability or old queue. Missing required binding blocks dependent work.

L4 PROFILE SELECTION
Stable ROLE + exact task/event class select PROFILE_PACK. Profile never creates authority. Neural classification may propose; allowed mapping/current routing decides. Ambiguity returns to authorized router/KOO.

L5 EXPERIENCE SELECTION
Retrieve bounded relevant experience with provenance/applicability/freshness/reason. Neural ranking allowed. Experience is advisory only and cannot populate authority/current state.

L6 SEMANTIC_EXECUTION_CONTRACT
Versioned derived contract for one bounded execution scope. Not authority. Human explanation derives from same fields.

L7 STATIC VALIDATOR
Before first effect validate writer requirement, task authority/currentness, immutable inputs, source compatibility, ALLOWED/FORBIDDEN, STOP_IF, expected result/terminal. Proposed action outside ALLOWED is rejected before effect.

L8 RUNTIME STEP GUARD
One safe causal step. Before each external/irreversible/consequential effect revalidate task, authority, writer if applicable and relevant inputs. Capability/automation never creates authority.

Effects include host/storage mutation, consequential external send/publication, provider/credential operation, economy/accounting mutation, production state write, writer/recovery/source mutation and task-defined irreversible transition.

L9 RESULT VALIDATOR / FIXATION / NEXT GATE
Observed result compared with contract. Output PASS/BLOCKED/FAIL/UNKNOWN + fixation + next-gate candidate from active authority/current result/Task Conveyor only.
Never infer delivery from publication, receipt from dispatch, acceptance from receipt, processing from activation, or next task from historical queue.

## Deterministic vs neural
NEURAL MAY: semantic extraction, candidate atom/rule/profile classification, experience retrieval/ranking, diagnosis, proposed action, prose explanation.
DETERMINISTIC MUST: source identity/status, provenance completeness, exact authority/task/writer bindings, supersession, ALLOWED/FORBIDDEN membership, preconditions, STOP_IF, immutable input identity, replay IDs, self-test expected outcomes, result shape and next-gate rules.
Neural output never overrides deterministic rejection.

## Human causality
Render from L6/L9:
checked → known/UNKNOWN → authority → allowed → forbidden → observed result → significance → exact next action.
Narrative cannot add authority absent from contract provenance.
