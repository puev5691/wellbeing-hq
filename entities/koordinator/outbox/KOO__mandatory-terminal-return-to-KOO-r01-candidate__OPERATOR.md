# KOO candidate: Mandatory Terminal Return to Coordinator r0.1

status: CANDIDATE_NOT_ACTIVE
owner: KOO / КООРДИНАТОР
project_time: omitted

## Purpose

Prevent task conveyor stalls after an Entity reaches PASS, BLOCKED or FAIL.

## Core rule

Profile execution terminal and conveyor handoff completion are separate facts.

An Entity task may have a valid execution terminal:
PASS / BLOCKED / FAIL

but the conveyor handoff is not complete until all are true:

1. immutable terminal result exists;
2. result is explicitly addressed to KOO / КООРДИНАТОР;
3. exact result locator/identity is returned to KOO;
4. KOO receipt or fresh reconciliation is established.

Until then:

EXECUTION_TERMINAL = preserved
CONVEYOR_HANDOFF = INCOMPLETE

No completed execution is replayed merely because handoff failed.

## Mandatory terminal return

Every profile Entity finishing an exact task must end by returning KOO:

- entity identity;
- exact task ref;
- terminal;
- immutable result locator + version/blob where available;
- what changed;
- blocker if any;
- next causal condition/step;
- whether OPERATOR action is required;
- whether task is consumed/non-replayable.

## KOO responsibility

On receipt/reconciliation KOO must:

1. verify exact result identity and supersession;
2. preserve execution terminal;
3. classify conveyor state;
4. determine next causal step;
5. issue one fresh handoff/decision/WAIT basis as applicable.

KOO must not infer receipt from publication, dispatch or inbox placement.

## Fail-safe

If terminal result exists but KOO return is missing:

- do not rerun profile execution;
- create/repair handoff only;
- mark:
  EXECUTION_COMPLETE_HANDOFF_INCOMPLETE

If KOO receipt is UNKNOWN:
UNKNOWN remains UNKNOWN.

## Scope

Candidate applies to exact task completion for all project Entities.

It does not create task authority, writer authority, automatic activation or universal effectivity by itself.

## Relationship to continuity

Compatible with current continuity principle:
execution terminal != handoff quality.

This candidate makes the return-to-KOO boundary explicit and machine-checkable.

## Candidate terminal

CANDIDATE_MANDATORY_TERMINAL_RETURN_TO_KOO_R01_READY_FOR_REVIEW
