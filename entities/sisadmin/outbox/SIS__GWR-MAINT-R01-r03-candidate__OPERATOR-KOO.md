# SIS-GWR-MAINT-R01 r0.3 — ephemeral-residue correction candidate

status: CANDIDATE_NOT_ACTIVE
document_type: correction-successor-candidate
project_time: omitted
from_entity: SIS / СИСАДМИН r0.7
predecessor:
puev5691/wellbeing-hq@7dc9c475ea166ae3170ae9af2cbc111c0da0cc5e:
entities/shtabist/outbox/SHT__SIS-GWR-MAINT-R01-r02-candidate__OPERATOR-KOO.md
predecessor_blob:
782c4d7595aac7daeef8b09212e965753f351cc1

## Purpose

Keep the r0.2 standing-authority model, but separate durable/state-bearing objects from ephemeral runtime/log residue.

r0.3 exists to prevent a safe ephemeral residue from being blocked merely because:
- its exact bytes were not separately preserved; or
- it disappears between INSPECT and pre-mutation reverify.

Approval alone still does NOT start work.
Execution still requires a NEW exact task addressed to current SIS.

## Object classes

Before retirement admission, every exact object must be classified into one of:

1. DURABLE_STATE_OR_DATA
2. CONFIG_OR_EXECUTABLE
3. EPHEMERAL_RUNTIME_RESIDUE
4. ACTIVE_DEPENDENCY
5. SECRET_OR_SENSITIVE
6. UNKNOWN
7. OUT_OF_SCOPE

ACTIVE_DEPENDENCY / SECRET_OR_SENSITIVE / UNKNOWN / OUT_OF_SCOPE:
STOP affected retirement.

## EPHEMERAL_RUNTIME_RESIDUE

An exact object may be classified EPHEMERAL_RUNTIME_RESIDUE only when all are proven:

- object is inside the approved gateway contour;
- object belongs to the retired wellbeing-shard-gateway contour;
- no current process/open-file/socket/systemd/current consumer requires it;
- it is not durable state, recovery state, authoritative project state, configuration, executable source, credential material, or required audit evidence;
- no secret/sensitive value is detected or required to be exposed;
- exact metadata and content hash are captured when the object exists;
- disappearance of the object would not destroy required recoverability.

Examples may include transient request files, sockets, pid/runtime files, temporary logs, or equivalent residue, but path/name alone never proves this class.

## Preservation semantics

DURABLE_STATE_OR_DATA and CONFIG_OR_EXECUTABLE:
retain r0.2 preservation prerequisite and rollback requirements.

EPHEMERAL_RUNTIME_RESIDUE:
full byte-for-byte preservation is NOT mandatory when recoverability does not depend on the object.

Minimum preservation evidence before retirement:
- exact path;
- object type;
- size;
- owner/group/mode;
- inode/device identity where available;
- content hash for regular files where safely readable;
- dependency/current-use evidence;
- sensitivity classification;
- classification rationale.

If the object is itself required audit/recovery evidence:
it is NOT eligible for ephemeral treatment.

## Ephemeral retirement admission

EPHEMERAL_RUNTIME_RESIDUE may receive:

OBJECT_RETIREMENT_ADMITTED_EPHEMERAL

only when:
- current SIS writer PASS;
- NEW exact task PASS;
- exact host PASS;
- allowlist containment PASS;
- object identity PASS;
- dependency/current-consumer absence PASS;
- secret-sensitive check PASS;
- ephemeral classification PASS;
- required evidence record captured;
- no supersession/conflict PASS.

## TOCTOU rule for ephemeral objects

Immediately before mutation, fresh reverify is still mandatory.

Outcomes:

A. exact object still exists and identity/evidence matches
   -> RETIRE exact object
   -> VERIFY absence

B. exact object is already absent
   -> RETIREMENT_ALREADY_SATISFIED
   -> no mutation
   -> continue with fresh inspection of remaining exact scope

C. same pathname now identifies a different object
   -> NEW_OBJECT
   -> old admission is invalid
   -> inspect/classify new object from zero

D. active/unknown/sensitive/out-of-scope state appears
   -> STOP affected retirement

Thus:
disappearance of an admitted ephemeral object is NOT by itself an OBJECT_IDENTITY_CHANGED blocker.

## Directory/container rule

A runtime/log directory may be retired only when:
- every descendant is independently classified/admitted or already absent;
- no active/unknown/sensitive/out-of-scope descendant remains;
- no mount/symlink/path escape exists;
- fresh reverify confirms exact current contents.

If the directory is state/DATA-bearing or its deletion falls into a separate-decision class, separate OPERATOR authority remains required.

No wildcard or recursive deletion over unclassified contents.

## Mutation authority

r0.3 does NOT make STALE/EPHEMERAL classification equivalent to deletion authority.

Mutation still requires:
- standing authority approved;
- NEW exact current task;
- exact object admission;
- fresh pre-mutation reverify.

State/DATA deletion, whole state/runtime data directory deletion, recursive/mass cleanup, wildcard/path-class deletion, multi-object cleanup as one operation, or irreversible removal without demonstrated rollback still require a separate explicit OPERATOR decision.

## Allowed contour

Unchanged from r0.2:

- /etc/systemd/system/wellbeing-shard-gateway-verify.service
- /opt/wb-shard-gateway
- /run/wb-shard-gateway
- /var/lib/wellbeing/shard-gateway
- /var/log/wb-shard-gateway

## Helpers

Existing helper paths remain implementation-only:

- /home/shd/SIS-GWR-INSPECT.sh
- /home/shd/SIS-GWR-RETIRE.sh

Helpers do not create authority or admission.

## Lifecycle

NEW exact task
-> Resume-First
-> preservation prerequisite by object class
-> INSPECT
-> CLASSIFY
-> OBJECT_RETIREMENT_ADMISSION
-> pre-mutation reverify
-> RETIRE or RETIREMENT_ALREADY_SATISFIED
-> VERIFY
-> next exact object
-> immutable result/readback
-> return KOO
-> execution instance CONSUMED/NON_REPLAYABLE
-> standing authority APPROVED_DORMANT

## Hard exclusions

Unchanged:
- /data/wellbeing-lab mutation;
- proof roots;
- backend selection/install/run;
- T01-T20;
- CHECKPOINT_DURABLE;
- memory-layering attempt 3;
- credential/provider/Telegram work;
- Project Sources/canon mutation;
- historical PROMPT replay;
- automatic activation.

## Current cycle consequence if r0.3 is later approved

The already observed disappearance of:
/var/log/wb-shard-gateway/audit.jsonl

would no longer be treated as a TOCTOU blocker solely because the object became absent.

However:
- this candidate does not retroactively reopen or replay the consumed r0.2 cycle;
- a NEW exact task would still be required;
- the current contents of /var/log/wb-shard-gateway would have to be freshly inspected.

## Proposed OPERATOR decision

APPROVE_SIS_GWR_MAINT_R01_R03

Effect:
r0.3 supersedes r0.2 semantics for future NEW exact maintenance tasks while preserving the dormant-standing-authority model and all unchanged hard exclusions.

Alternative:
REJECT_SIS_GWR_MAINT_R01_R03
or
HOLD_SIS_GWR_MAINT_R01_R03

## Terminal

CANDIDATE_SIS_GWR_MAINT_R01_R03_READY_FOR_OPERATOR_DECISION
