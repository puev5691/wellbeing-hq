# Entity Operational Continuity Contract r0.1 — correction-only addendum r0.2

status: CANDIDATE_NOT_ACTIVE
scope: CORRECTIONS_R1_R5_AND_SECTION_5_3_ONLY
project_time: omitted

Exact predecessor:
puev5691/wellbeing-hq@7f7aa19e0453580c6c5a17ace7acf29a2da8456a:
entities/koordinator/outbox/KOO__entity-operational-continuity-contract-r01-candidate__KAN.md
blob ff2288267c200711c8c34c5b91373c96915a392f

Exact review basis:
puev5691/wellbeing-hq@f8175895e2a34721830a3816719f2af1a3ffd087:
entities/kancelar/outbox/KAN__entity-operational-continuity-r01-independent-review__KOO.md
blob 4dc23f7454a691de3ef6f06ea88f3862d2fae509

Predecessor remains byte-unchanged.
Combined candidate for next review = exact r0.1 predecessor + this r0.2 addendum.
All predecessor text not explicitly corrected below remains unchanged.

## R1 — WAIT/NONE semantics

Replace G6 with:

G6 NONE_OR_WAIT_JUSTIFIED.

NONE/WAIT is allowed only when one exact basis is proven:
- causal chain complete; or
- no next transition exists; or
- next transition exists but is not currently enabled and no manual action is required now; or
- waiting for an external event/condition is the authorized current state; or
- next transition is already automatically activated by separately proven authority and working mechanism.

For WAIT state identify exact awaited event/condition, applicable authority/state, why no current manual action is required, and what evidence enables the next transition. WAIT does not prove activation, receipt, acceptance or processing_started.

Replace G8 with:

G8 SINGLE_OPERATOR_ACTION_OR_JUSTIFIED_WAIT.

Human-facing terminal result ends with exactly one clear OPERATOR action, one exact decision request, or justified NONE/WAIT satisfying G6.

Replace C08 with:

C08 FAIL only when operator_action is NONE/WAIT and no valid G6 basis exists.

FAIL:
UNJUSTIFIED_NO_ACTION_OR_WAIT

The existence of a possible future transition is not enough for FAIL; current enablement and present manual-action requirement control.

Clarify C01/C02:
initiation/writer status never creates missing Writer Gate or conveyor authority. If separate approval is still required, output a bounded decision request or exact HOLD/WAIT where independently established.

## R2 — requested decision versus granted authority

Distinguish:

DECISION_REQUEST = proposed bounded OPERATOR choice.
GRANTED_AUTHORITY = separately verified evidence that OPERATOR approved a permitted choice.

A DECISION_REQUEST must state subject, scope, effect if approved, preserved boundaries and applicable alternatives/HOLD. It is not execution authority.

Execution requiring new authority begins only after separately verified GRANTED_AUTHORITY.

Replace C06 with:

C06 FAIL when:
next_step_requires_operator_authority = YES
AND granted_authority = NOT_PRESENT
AND complete_bounded_decision_request = NOT_PRESENT.

FAIL:
MISSING_OPERATOR_DECISION_GATE

C06 does not require approval to pre-exist before asking OPERATOR. Publication/dispatch/inbox or a proposed decision string do not equal GRANTED_AUTHORITY.

## R3 — derived projections never arbitrate truth

CURRENT_STATE_CAPSULE and CONVEYOR_HEAD remain derived projections.

If Capsule, Head, human-facing result, current-writer, exact task/authority, terminal evidence or recovery dependencies conflict:
1. fresh-reconcile authoritative exact evidence;
2. never choose winner by timestamp, plausibility or last-write-wins;
3. authorized current-writer may update/invalidate derived projection only after reconciliation;
4. unresolved conflict becomes UNKNOWN/BLOCKED with exact reason;
5. authoritative evidence is never rewritten to make a projection pass.

For KOO, Capsule and Head may share only compact linkage to the same exact task/terminal/causal evidence. This is not a second queue and does not prove absence of other lines.

C09 detects mismatch but chooses no winner. It triggers fresh evidence reconciliation.
C10 continues to block promotion of stale/superseded derived projection.
If fresh evidence supersedes Capsule/Head, update/invalidate projection rather than downgrade evidence.

## §5.3 attribution correction

Existing Task Conveyor v1.2 classifications:
- CURRENT
- COMPLETED
- BLOCKED
- SUPERSEDED

Candidate-only descriptive flags:
- PAUSED
- UNKNOWN

PAUSED/UNKNOWN do not create authority or transition outcomes and are not claimed as existing Conveyor v1.2 machine classes. They require exact basis when used.

## R4 — existing requirements versus proposed mechanism/effectivity

Replace the broad claim that the candidate "only materializes" active rules with explicit separation:

[EXISTING_REQUIREMENT]
Active Sources already require human-readable causal explanation, exact recovery/current evidence, authority/writer/task separation, fresh reconciliation, no historical PROMPT replay, and complete manual handoff where applicable.

[PROPOSED_CHECK_OR_ARTIFACT]
This candidate newly proposes CURRENT_STATE_CAPSULE, CONVEYOR_HEAD, named PRE_SEND_GATE, C01-C10 and concrete lifecycle/schema rules for them.

Proposed mechanisms are not universal active requirements merely because they help enforce existing requirements.

A bounded pilot may use them under exact OPERATOR pilot authority if scope/stop conditions are explicit and no approved Source meaning or authority is changed.

Universal mandatory adoption of new objects/schema/COMPLETE criterion/recovery requirement/workflow gate requires separate OPERATOR adoption/effectivity. If it changes approved Core/Recovery/Conveyor/File Work meaning, exact amendment and applicable activation barrier are required first.

Emergency recovery:
Capsule/Head are preserved only when they exist, are applicable and are included in the exact recovery scope. Missing/stale/unreadable Capsule/Head alone must not block otherwise valid emergency initiation, cause synthetic reconstruction, or outrank externally verified recovery/current-writer/task evidence.

## R5 — gate result versus execution terminal

PRE_SEND_GATE/linter result and profile execution terminal are separate facts.

Gate contradiction may block a positive claim that causal handoff/continuity validation is complete. It does NOT:
- erase actual PASS/FAIL/BLOCKED execution result;
- change parent completion by itself;
- prevent reporting exact blocker/partial/emergency result;
- require replay of completed execution merely to repair handoff.

A defective handoff after completed work is repaired as handoff/continuity work unless separate evidence requires rerun.

Future linter/check outcomes must distinguish:

PASS = all applicable continuity checks proven.
CONTRADICTION = sufficient evidence proves an applicable contradiction.
UNVERIFIED = applicable condition cannot be evaluated because evidence/input is missing, unreadable or semantically indeterminate.

UNVERIFIED is neither PASS nor invented proof of contradiction.

Gate FAIL/UNVERIFIED remains reportable to the human together with preserved execution terminal, exact diagnostic and next safe correction/escalation.

Declared terminal criterion and parent completion remain governed by Task Conveyor v1.2.

## Effect on C01-C10

C01/C02 respect missing decision authority and explicit HOLD/WAIT.
C06 checks for decision-request presence, not imaginary prior approval.
C08 uses G6 basis rather than mere existence of future transition.
C09 triggers reconciliation, not machine-summary supremacy.
C10 preserves stale projection boundary.
All continuity contradictions remain separate from execution terminal/effectivity.

No completeness claim for C01-C10 is made.

## Implementation concern boundary

Semantic checks such as "human understands", "repeats unchanged", inferred receipt, human-prose/metadata consistency, prompt completeness, projection atomicity/versioning and evidence availability remain implementation concerns for future SHT/KOD. Self-declared prompt_complete=YES is not sufficient proof.

No implementation authority is created.

## Effectivity

Combined r0.1 + r0.2 remains CANDIDATE_NOT_ACTIVE.

No Project Source/canon mutation, candidate activation, universal Capsule/Head requirement, KOD implementation, automation, automatic chat activation or foreign current-state mutation is authorized.

## Next review

Exact predecessor bytes + this correction addendum are ready for independent SHT stress-review only.

terminal:
CANDIDATE_R02_CORRECTIONS_READY_FOR_SHT_STRESS_REVIEW
