# KOO → OPERATOR: admission-blocker reporting contract r0.1

status: `CANDIDATE_FOR_IMMEDIATE_USE`
production: `no`

## Problem

Current FAST_PATH / instance-admission pattern can create a dead reporting loop:

1. task requires current-writer verification before profile execution;
2. current-writer evidence is missing or mismatched;
3. fail-closed policy correctly forbids profile work and project-state mutation;
4. the same task also requires exact `BLOCKED_*` result routing through Exchange Gate;
5. if all GitHub writes are treated as profile/project-state mutation, the Entity cannot publish the blocker that explains why it stopped.

Observed example:
`BLOCKED_SHT_CURRENT_WRITER_BOUNDARY_UNVERIFIED` on SHT FAST_PATH performance baseline r0.1.
The chat returned the blocker, but HQ received no terminal blocker artifact.

## Immediate bounded contract

An admission failure MUST NOT authorize profile execution, profile-state mutation, task acceptance, production action, or normal Entity outbox writes.

But an exact admission failure MAY emit one narrowly-scoped diagnostic return if and only if the task explicitly pre-authorizes it.

Allowed diagnostic payload:
- entity name / claimed instance;
- exact task path + commit/blob if verified;
- exact admission verdict (`WRONG_INSTANCE_OR_WRONG_CHAT`, `BLOCKED_*_WRITER_*`, etc.);
- observed conflicting/missing writer evidence;
- read-only telemetry counts actually observed;
- no profile result, no acceptance, no mutation claim.

Preferred routing:
1. dedicated `ops/admission-blockers/` or coordinator-owned collector path written by an already-authorized KOO/collector; OR
2. task-specific pre-authorized diagnostic-only path that cannot be interpreted as Entity profile output.

If the blocked Entity itself lacks verified writer authority, KOO/collector should materialize the diagnostic record from the chat-returned blocker. The record must say `source_instance_unverified` and MUST NOT impersonate a valid Entity outbox result.

## FAST_PATH prompt rule

Future prompts should distinguish:

`ADMISSION_FAIL_ACTION: RETURN_DIAGNOSTIC_BLOCKER_ONLY`

from:

`PROFILE_WRITE_AUTHORITY: REQUIRES_VERIFIED_CURRENT_WRITER`

Thus:
- writer admission failure stops profile work;
- blocker still reaches the coordination system;
- missing writer evidence is not converted into PASS;
- the OPERATOR is not forced to manually relay the same blocker.

## Current SHT case

The SHT response was methodologically correct:
- fresh preflight performed;
- task/inbox verified;
- current-writer evidence not found;
- no profile execution;
- no GitHub writes;
- exact blocker returned in chat.

The defect is therefore in the reporting contract, not in SHT's fail-closed decision.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: устранить ситуацию, когда admission blocker существует только в чате и не попадает в системное поле
СТАТУС: `candidate_admission_blocker_reporting_r01`
