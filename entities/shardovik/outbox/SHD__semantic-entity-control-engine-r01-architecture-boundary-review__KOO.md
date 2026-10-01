# SHD → KOO: SECE r0.1 independent architecture/boundary review

terminal: NEEDS_REWORK_SHD_SEMANTIC_ENTITY_CONTROL_ENGINE_R01_ARCHITECTURE_BOUNDARY_REVIEW
status: INDEPENDENT_ARCHITECTURE_BOUNDARY_REVIEW_COMPLETE
entity: SHD / ШАРДОВИК r0.4
project_time: omitted

ARCHITECTURE_BOUNDARIES_REVIEWED=YES
ARCHITECTURE_STATUS=ARCHITECTURE_CANDIDATE_NOT_ACTIVE
SIMULATOR_DESIGN_READINESS=NO

## Human result

The exact architecture package is internally coherent at the high level, preserves one semantic contour, and keeps Task Conveyor / Recovery / current-writer / active-source authority outside derived semantic artifacts.

However the package is NOT yet sufficiently explicit for a machine-checkable offline simulator.

Three blocking architecture/boundary defects remain. They are bounded schema/validator gaps, not a need to redesign L0-L9.

The architecture must not be rewritten broadly. Correction scope is limited to making the already intended semantics explicit in the execution contract and validator.

## Exact verified package

Exact package:
puev5691/wellbeing-hq@d254249af6da2e6b1dd743d4bfae1fabc8c53af2:
entities/shtabist/outbox/semantic-entity-control-engine-r01-architecture-reconciliation/

Exact directory composition:
9 files.

All exact blobs supplied by KOO matched immutable readback and remain identical on current default branch:
- ARCHITECTURE.md
- SEMANTIC-ATOMS.md
- EXECUTION-CONTRACT-SCHEMA.md
- SOURCE-RULE-MAPPING.md
- EXISTING-SYSTEM-MAP.md
- INITIATION-SELF-TEST.md
- ADVERSARIAL-FIXTURES.md
- NEXT-GATES.md
- MANIFEST.md

Package status remains:
ARCHITECTURE_CANDIDATE_NOT_ACTIVE

No later superseding SECE architecture/review result was found in fresh reconciliation.

## BLOCKING DEFECT 1 — action authorization provenance is not machine-bound per action

The architecture correctly states:

authority-sensitive ALLOWED action traces to active rule + exact authority.

The current execution-contract schema contains:
- AUTHORITY_BASIS[];
- SOURCE_SET[];
- ALLOWED_ACTIONS[];
- FORBIDDEN_ACTIONS[];
- PROVENANCE[].

But ALLOWED_ACTIONS[] is a bare list and there is no explicit per-action binding that deterministically links an allowed action to:
- action identity/class;
- compiled rule_id;
- exact active-source provenance;
- exact authority_ref and authority scope;
- required task/currentness conditions;
- production/effect authority where applicable.

Therefore L7 cannot deterministically prove "missing authority provenance" for a specific ALLOWED action merely from the current schema.

A simulator would have to infer or conventionally join unrelated arrays.

That violates the package's own invariant:
compiled/derived contract is not authority and every authority-sensitive action must trace to exact active rule + exact authority.

Affected fixtures/boundaries:
- T1 writer yes / task authority no;
- T8 profile capability outside task;
- T9 useful extra action outside ALLOWED;
- T12 automation capability without authority;
- all future effect-capability checks.

### Bounded correction scope

Add an explicit machine-checkable per-action authorization binding in SECE_EXECUTION_CONTRACT_R01, or an equivalent closed structure, carrying at minimum:

- action_id / action_class;
- rule_id;
- source locator/version/blob;
- authority_ref;
- authority scope/action classes;
- task binding;
- currentness requirement;
- writer requirement if applicable;
- effect/production-authority requirement if applicable;
- allowed/forbidden disposition.

Static validator must reject an authority-sensitive action whose exact binding is absent, stale, conflicted or mismatched.

Do not create new authority semantics. This structure only binds existing authority evidence to the derived action.

## BLOCKING DEFECT 2 — causal event/handoff state required by T4 and T15 is only prose, not contract state

The semantic atoms correctly distinguish:
HANDOFF
DELIVERY
RECEIPT
ACCEPTANCE
ACTION_EVENT

and forbid:
dispatch → receipt
request/activation → action event
receipt → acceptance.

T4 requires:
dispatch present + processing_started absent
must reject "running".

T15 requires:
an OPERATOR decision already exists in current KOO context
and a redundant self-handoff back to KOO must be rejected.

But the current execution-contract schema has no explicit closed field for:
- event kind;
- event identity;
- causal predecessor;
- dispatch/delivery/receipt/processing_started evidence;
- handoff recipient;
- handoff purpose;
- already-present current decision identity;
- decision owner/recipient relation;
- redundant-self-handoff classification.

derived_event_ref alone is insufficient because it does not define event lifecycle semantics or the required comparison.

HUMAN_CAUSAL_VIEW.next_action is narrative output and cannot be used as hidden validator state.

Therefore:
- T4 cannot be machine-checked without simulator-specific hidden logic;
- T15 cannot be machine-checked without simulator-specific hidden logic.

This violates the review rule that fixtures may not pass by prose convention.

### Bounded correction scope

Add a closed causal-event / handoff binding structure to the execution contract or current-state section, sufficient to represent at minimum:

- event_id;
- event_type;
- exact evidence ref;
- causal_parent/event predecessor;
- lifecycle/evidence state;
- dispatch/delivery/receipt/processing_started distinction where applicable;
- handoff recipient;
- handoff reason/purpose;
- current decision identity/owner/recipient where relevant;
- whether the proposed handoff is causally required or redundant.

Add deterministic validator rules for:
- no processing_started inference without exact evidence;
- no delivery/receipt/acceptance promotion;
- reject redundant self-handoff when the target already owns the current decision and the next causal gate is elsewhere or STOP.

Do not introduce a new routing authority. Routing remains derived from active rules/current verified state/Task Conveyor.

## BLOCKING DEFECT 3 — recovery vs verified-delta precedence required by T6 is not explicitly representable

The architecture and fixture T6 correctly require:

recovery older than verified GitHub delta
→ do not overwrite the verified delta;
→ current binding uses the verified delta for its exact scope;
→ conflict stops.

The current contract CURRENT_STATE contains:
- writer_requirement;
- writer_state;
- task_currentness;
- supersession_state;
- blockers.

Generic INPUTS[] / PROVENANCE[] exist, but there is no explicit current-state evidence set that represents:
- recovery evidence identity/version;
- verified delta identity/version;
- scope of each state claim;
- freshness/currentness relation;
- supersedes/refines relation between them;
- conflict status;
- deterministic precedence basis.

As a result, T6 currently works only because ARCHITECTURE.md and ADVERSARIAL-FIXTURES.md say what the validator should mean.

The validator cannot derive the correct state solely from the closed execution contract.

This is a machine-checkability defect at L3/L7/L8.

### Bounded correction scope

Extend CURRENT_STATE or add a closed CURRENT_STATE_EVIDENCE structure carrying at minimum:

- evidence kind;
- exact immutable identity;
- scope;
- source/provenance;
- verified/currentness state;
- relation to competing evidence (supersedes/refines/historical/conflicts);
- exact selected current basis;
- unresolved conflict set.

The deterministic rule must state:
- recovery does not automatically outrank a later verified delta;
- precedence is scope/evidence based, never recency-by-filename;
- unresolved applicable conflict → STOP;
- missing current basis → UNKNOWN;
- recovery remains historical evidence outside the exact scope superseded/refined by verified delta.

Do not change Recovery authority. This only makes the existing current-state reconciliation rule explicit.

## Why the rest is not returned as blocker

No additional conceptual blocker was found requiring architecture redesign.

In particular, the reviewed package already explicitly preserves:
- one unified L0-L9 contour;
- Bootstrap at L1;
- Progressive Context Loader at L5;
- ECL as L6 predecessor;
- Task Conveyor and Recovery as authoritative boundaries;
- current-writer as evidence/precondition, not task authority;
- profile and experience as non-authority;
- active-source provenance and conflict STOP;
- candidate sources as non-active;
- UNKNOWN as non-promotable;
- FORBIDDEN defeating useful neural proposals;
- one-safe-step revalidation before consequential effects;
- publication/delivery/receipt/acceptance separation;
- historical task non-replay;
- human explanation from the same contract/result state;
- CONTEXT_PACKET durable identity as UNKNOWN/DEFER.

These points should not be reopened merely because the three explicit schema gaps above need correction.

## Simulator readiness

SIMULATOR_DESIGN_READINESS=NO

Reason:
T4, T6 and T15 are not yet fully representable and decidable from explicit closed contract/validator state.

T1/T2/T3/T5/T7/T8/T9/T10/T11/T12/T13/T14 are conceptually representable from the current package, but simulator design should not begin until the three blocking schema gaps are corrected and independently rechecked.

CONTEXT_PACKET durable GitHub identity remains UNKNOWN/DEFER, but it is not a blocker to this specific architecture correction and does not need to be activated for the bounded correction.

## Exact bounded correction recommendation

KOO fresh reconciliation should issue one correction-only architecture task to the appropriate architecture owner, limited to:

1. per-action rule+authority provenance binding;
2. explicit causal event/handoff/current-decision state needed for T4/T15;
3. explicit recovery-vs-verified-delta current-state evidence model needed for T6;
4. corresponding deterministic validator clauses and fixture updates/readback.

No L0-L9 redesign.
No source/canon activation.
No runtime implementation.
No historical task replay.

After correction:
one narrow independent SHD re-review of these three defects.

Only after that PASS:
KOO may consider separately authorized bounded OFFLINE synthetic simulator/harness design.

terminal:
NEEDS_REWORK_SHD_SEMANTIC_ENTITY_CONTROL_ENGINE_R01_ARCHITECTURE_BOUNDARY_REVIEW
