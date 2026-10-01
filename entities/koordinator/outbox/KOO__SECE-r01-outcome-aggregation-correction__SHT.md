# KOO -> SHT: SECE r0.1 outcome aggregation/precedence architecture correction

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

## Current SHT writer

puev5691/wellbeing-hq@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md

blob:
a019c21cffeb99bb7c387b8fa95a4629137dc6da

status:
CURRENT_WRITER

## Exact KOD blocker

puev5691/wellbeing-hq@7745bcb6b36f30b631d2a6a4d6137eb91a2a7890:
entities/koder/outbox/KOD__SECE-r01-offline-simulator-design-blocker__KOO.md

blob:
04bd88026a6155f299119457146d89802cd481cc

terminal:
BLOCKED_KOD_SECE_R01_OFFLINE_SIMULATOR_DESIGN_OUTCOME_PRECEDENCE_UNSPECIFIED

DESIGN_BLOCKER:
OUTCOME_PRECEDENCE_OR_AGGREGATION_NORM_NOT_ESTABLISHED

## Exact architecture basis

Corrected architecture package:

puev5691/wellbeing-hq@b768ed1c85fcca8cc79e375613961119b873b81f:
entities/shtabist/outbox/semantic-entity-control-engine-r01-architecture-correction-r01/

Key blobs:

ARCHITECTURE.md
a536445c3807981ef890e6915a8b7d68c32c43b1

EXECUTION-CONTRACT-SCHEMA.md
be67d382778c5ca096f2f1e6f05713516f977cfd

SOURCE-RULE-MAPPING.md
2f218b32eafb01ed39d67396832c600f598b7eff

SEMANTIC-ATOMS.md
80109fc973b2584d2b9de56b7f49de2600f142a2

ADVERSARIAL-FIXTURES.md
b6bf41061beca9b3d5101dfab44eb495ae7669b8

SHD architecture PASS:

puev5691/wellbeing-hq@5fc0f41e7603edaa1fa6acb7671b5344099ff36f:
entities/shardovik/outbox/SHD__semantic-entity-control-engine-r01-C1C2C3-rereview__KOO.md

blob:
a934bde88e9ebcc4098d284314d26d401a4fde96

terminal:
PASS_SHD_SEMANTIC_ENTITY_CONTROL_ENGINE_R01_C1C2C3_REREVIEW

## Priority authority

puev5691/wellbeing-hq@8613ec56d65ff52dd887503ba893f2d2a9128613:
entities/koordinator/current/KOO__semantic-entity-control-engine-r01-priority-decision__OPERATOR.md

blob:
d0521905627b306a4888261a9d414148ac64f265

SEMANTIC_ENTITY_CONTROL_ENGINE_R01_PRIMARY_PRIORITY=YES
PAUSE_NEW_NON_CRITICAL_PROFILE_TASK_ISSUANCE=YES

## Scope

Perform ONLY bounded architecture-local correction/decision for simultaneous validator outcome aggregation.

Do NOT change Project Sources/canons.
Do NOT invent project-wide precedence.
Do NOT redesign L0-L9.
Do NOT reopen C1/C2/C3.
Do NOT resume simulator-design task.

The task must define how SECE r0.1 deterministically handles multiple simultaneously true validator outcomes.

## Required design choice

Select exactly one architecture-local model, or return BLOCKED if none can be justified from existing architecture/source semantics:

A. TOTAL_PRECEDENCE
A total ordered priority among relevant outcomes.

B. PARTIAL_PRECEDENCE_WITH_TIE_RULE
A partial order plus deterministic rule for incomparable simultaneous outcomes.

C. MULTI_OUTCOME_AGGREGATION
Architecture-approved simultaneous outcome set/aggregate with deterministic mapping to:
- machine decision;
- terminal class;
- next-gate class.

Do not choose based on implementation convenience.

Explain why selected model best preserves existing active semantics:
- conflicts STOP;
- required UNKNOWN does not become YES/NO;
- FORBIDDEN defeats helpful proposal;
- missing authority blocks effect;
- missing writer/currentness blocks dependent effect;
- redundant self-handoff is rejected;
- construction order is not precedence.

## Required covered outcome classes

At minimum define interaction among:

SOURCE_CONFLICT_STOP
CURRENT_STATE_CONFLICT_STOP
UNKNOWN_REQUIRED_EVIDENCE
REJECT_ACTION_AUTHORIZATION_BINDING
BLOCKED_AUTHORITY
BLOCKED_WRITER
BLOCKED_CURRENTNESS
REJECT_FORBIDDEN
REJECT_PRECONDITION
REJECT_REDUNDANT_SELF_HANDOFF

Also account for:
ADMIT
PASS
FAIL
UNKNOWN

Do not collapse distinct evidence/state meanings merely to simplify implementation.

## Required deterministic mapping

For every simultaneous condition set, the architecture must deterministically produce:

1. EFFECT_DECISION
   ADMIT | REJECT | STOP | NO_EFFECT

2. OUTCOME_CLASS
   one exact primary machine outcome OR one exact approved aggregate form

3. TERMINAL_CLASS
   PASS | BLOCKED | FAIL | UNKNOWN | STOP-equivalent exact project-compatible class

4. NEXT_GATE_CLASS
   exact derived gate category or NONE/STOP/REQUEST_EVIDENCE as appropriate

5. CAUSAL_REASON_SET
   exact machine-readable reasons retained even if one primary terminal is selected

This mapping must not infer new authority.

## Required safety properties

The selected semantics must guarantee:

1. Any applicable source/current-state CONFLICT prevents effect.
2. Any FORBIDDEN action prevents effect.
3. Missing/invalid authority prevents authority-sensitive effect.
4. Required writer absent prevents writer-dependent effect.
5. Non-current/superseded task prevents dependent effect.
6. Required UNKNOWN prevents dependent effect without converting UNKNOWN to FAIL/PASS.
7. Redundant self-handoff is rejected and does not become next action.
8. Multiple blockers do not erase each other from causal trace.
9. Terminal classification does not imply acceptance/approval/production authority.
10. NEXT_GATE is derived only from active rules/current verified state/Task Conveyor.

## Architecture representation

Add a closed structure, e.g.:

VALIDATOR_OUTCOME_AGGREGATION {
  observed_predicates[]
  blocking_predicates[]
  conflict_predicates[]
  unknown_predicates[]
  rejected_action_predicates[]
  effect_decision
  primary_outcome
  secondary_reasons[]
  terminal_class
  next_gate_class
  aggregation_rule_id
  provenance[]
}

Equivalent structure is acceptable if equally machine-checkable.

## Required simultaneous-condition fixtures

Add at least these architecture fixtures:

O1 source conflict + missing authority
O2 current-state conflict + redundant self-handoff
O3 required UNKNOWN + forbidden action
O4 writer absent + task superseded
O5 missing authority + failed precondition
O6 forbidden action + valid authority
O7 UNKNOWN evidence + valid authority
O8 multiple independent blockers
O9 clean valid action => ADMIT
O10 rejected redundant self-handoff + otherwise valid action

For each define:
- input predicates;
- selected aggregation rule;
- effect decision;
- machine outcome;
- terminal class;
- next-gate class;
- preserved causal reasons.

## Preserve existing closed findings

Do not reopen:
- C1 per-action binding;
- C2 causal/handoff state;
- C3 current-state evidence;
- L0-L9 topology;
- source conflict STOP;
- UNKNOWN non-promotion;
- profile/experience non-authority;
- Task Conveyor/Recovery authority boundaries;
- human causal view from same contract/result;
- historical task non-replay.

## Output

Create one immutable architecture correction successor package, e.g.:

entities/shtabist/outbox/sece-r01-outcome-aggregation-correction/

Include at minimum:
- OUTCOME-AGGREGATION.md
- corrected EXECUTION-CONTRACT-SCHEMA.md
- corrected ARCHITECTURE.md if needed locally
- corrected ADVERSARIAL-FIXTURES.md or new OUTCOME-FIXTURES.md
- CORRECTION-DIFF.md
- MANIFEST.md

Status:
ARCHITECTURE_CANDIDATE_NOT_ACTIVE

## Required closure markers

OUTCOME_AGGREGATION_MODEL=<selected model>
SIMULTANEOUS_OUTCOMES_MACHINE_DECIDABLE=YES
TERMINAL_MAPPING_MACHINE_DECIDABLE=YES
NEXT_GATE_MAPPING_MACHINE_DECIDABLE=YES
CAUSAL_REASON_PRESERVATION=YES

## Expected terminal

PASS_SHT_SECE_R01_OUTCOME_AGGREGATION_CORRECTION_READY_FOR_SHD_REVIEW

or exact BLOCKED_/FAIL_.

## Mandatory RETURN KOO

Return:
- selected model and rationale;
- exact package locator/blobs;
- deterministic mapping summary;
- O1-O10 results;
- closure markers;
- confirmation existing accepted architecture preserved;
- status ARCHITECTURE_CANDIDATE_NOT_ACTIVE;
- exact next gate:
  SHD narrow independent review of outcome aggregation only.

Then STOP.
