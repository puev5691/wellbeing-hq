# KOO → KAN: design shard checkpoint governance r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KAN / КАНЦЕЛЯР
scope: BOUNDED_NON_LIVE_DOCUMENTARY_GOVERNANCE_DESIGN
project_time: omitted

## Human meaning

SHT independent review of the autonomous Entity conveyor found the first shared blocker to be governance of operational shard checkpoints, not API/runtime implementation.

This task asks KAN to prepare one documentary governance candidate defining what a shard checkpoint is allowed to mean, who may create/ack/promote it, how durability is proven, and how conflicts with GitHub/current-writer/recovery are handled.

No shard write, host access, runtime implementation, automation or production mutation is authorized.

## Current KOO authority

KOO current writer:
puev5691/wellbeing-hq@59378fc3e06e840b5f46c3b7f10beb0ae69c2995:
entities/koordinator/current/KOO__replacement-current-writer-r09.md
blob 8659c738f7d0a2f595a6da3e0f88633268bd2b75
status WRITER_ESTABLISHED

## Intended KAN writer basis

puev5691/wellbeing-hq@588493b011cf4ad85a94d40f6513644d9c207b9c:
entities/kancelar/current/KAN__replacement-current-writer-v02.md
blob 13b91b0e189f681be8abf13a76a47b03a5c830fa
writer_identity KAN-current-writer-v02
physical_instance KAN-physical-v02-1caebedc-d9bd-4a59-8317-b9c78bfca857

KAN must Resume-First and independently verify that this writer basis is still current. If a newer valid KAN writer/handoff/recovery/task successor exists, STOP and return exact blocker.

## Exact SHT review basis

puev5691/wellbeing-hq@7b875234b84049294166b082c48519151e46affe:
entities/shtabist/outbox/SHT__autonomous-entity-conveyor-r01-independent-review__KOO.md

blob:
e3344d43d3ae819186ccf6836fc7d12e0db40976

terminal:
PASS_WITH_EXACT_GOVERNANCE_GAP_SHT_AUTONOMOUS_ENTITY_CONVEYOR_R01

SHT conclusion:
the cross-component conveyor is coherent as non-live design, but CHECKPOINT_DURABLE and autonomous continuation cannot be trusted until checkpoint governance is explicitly defined and reviewed.

Minimal next step named by SHT:
DESIGN_SHARD_CHECKPOINT_GOVERNANCE_R01

## Exact predecessor technical design

KOD cross-component specification:
puev5691/wellbeing-hq@eb1f0f6cefaad9aa6858cf36caa3d8bf7a01d652:
entities/koder/outbox/KOD__autonomous-entity-conveyor-cross-component-spec-r01__KOO.md

blob:
9f25cce99ebd5c39863fda6a263297c66b0a64cd

KOD terminal result:
puev5691/wellbeing-hq@242f8932c33d31fa9423299dcc5121fcdc55f86f:
entities/koder/outbox/KOD__autonomous-entity-conveyor-spec-r01-result__KOO.md

blob:
b9acbcbabb59f5498bf54bffcf6d31decc719274

## Required governance candidate

Prepare one candidate document covering all of the following.

### 1. Checkpoint status classes

Define at minimum distinguishable states such as:
- transient/unverified checkpoint;
- written but not independently durable;
- durable/readback-verified operational checkpoint;
- stale/superseded checkpoint;
- conflict-blocked checkpoint;
- preservation/promoted checkpoint, if such class is justified.

Do not declare any class authoritative merely by recency.

### 2. Actors and authority

Define who may:
- write checkpoint bytes;
- issue/check durable acknowledgement;
- independently read back;
- promote checkpoint status;
- classify stale/superseded/conflict;
- select objects for GitHub promotion/preservation.

Current-writer authority, task authority, checkpoint writer authority, review authority and promotion authority must remain distinct unless an exact approved rule explicitly combines them.

### 3. Durable acknowledgement

Define the minimum evidence for CHECKPOINT_DURABLE.

At minimum address:
- exact durable_ref;
- digest;
- generation;
- authenticated writer identity;
- storage owner/domain;
- compare-and-swap or equivalent generation protection;
- independent readback;
- corruption detection;
- behavior if independent readback is unavailable.

A successful write/API response alone must not equal CHECKPOINT_DURABLE.

### 4. Generation / CAS / fencing

Define:
- generation semantics;
- stale writer rejection;
- fencing of replaced worker/writer;
- duplicate/replay handling;
- split-brain behavior;
- conflict terminal when two valid-looking generations compete.

No last-write-wins by timestamp.

### 5. Retention / expiry / preservation

Define candidate rules for:
- retention horizon or retention classes;
- expiry/staleness;
- whether old checkpoints may be compacted;
- what must remain externally recoverable;
- relation between transient operational state and ARH recovery/preservation.

Do not silently promote high-frequency checkpoints into canonical recovery.

### 6. Conflict behavior

Explicitly specify fail-closed behavior when checkpoint evidence conflicts with:
- approved Project Sources;
- explicit OPERATOR decision;
- current-writer state;
- immutable GitHub current-state/result/decision evidence;
- ARH recovery/preservation evidence;
- another shard checkpoint generation;
- raw logs/events.

At minimum preserve:
SHARD_RECENCY_DOES_NOT_WIN_BY_TIMESTAMP_ALONE
NO_LAST_WRITE_WINS_ACROSS_AUTHORITY_DOMAINS

If precedence cannot be safely universalized, define conflict classes and required owner/reconciliation gate rather than inventing one total order.

### 7. GitHub promotion policy

Define candidate promotion classes:
- terminal/result;
- approved decision/current-state/source version;
- recovery snapshot satisfying recovery canon;
- compact provenance/index where justified.

Define exclusions/guards for:
- raw prompts;
- transient retries;
- secrets/private data;
- unreviewed hypotheses;
- high-frequency checkpoints.

Specify:
- classifier/reviewer;
- privacy/redaction gate;
- mandatory vs optional promotion classes;
- failed-promotion behavior;
- exact evidence proving promotion/readback;
- what happens if GitHub and shard disagree after partial failure.

### 8. Unreachable shard / corruption / split-brain

Define exact fail-closed states and allowed claims when:
- shard is unreachable;
- checkpoint cannot be independently read;
- digest mismatch occurs;
- storage generation is ambiguous;
- split-brain is detected;
- latest known checkpoint is stale.

Do not infer recoverability from a previously successful write.

### 9. Allowed claims

Define the exact claims permitted for:
- CHECKPOINT_WRITTEN;
- CHECKPOINT_DURABLE;
- CHECKPOINT_STALE;
- CHECKPOINT_CONFLICT;
- CHECKPOINT_PROMOTED;
- RECOVERY_READY, if applicable.

Each claim must specify its minimum evidence.

### 10. Boundaries with layered memory

The candidate must remain independent of claiming layered-memory attempt 3 or Fast Memory production validity.

Memory-layering attempt 3 remains:
NOT_AUTHORIZED

The checkpoint contract may be generic operational state governance only.

## Required output

Publish one immutable candidate addressed to KOO.

Required status:
CANDIDATE_NOT_ACTIVE

Required terminal:
PASS_KAN_SHARD_CHECKPOINT_GOVERNANCE_R01_DOCUMENT_ONLY
or exact BLOCKED_* / FAIL_*.

Result must include:
- exact KOD and SHT predecessor identities;
- exact current KAN writer identity;
- governance model;
- unresolved choices requiring OPERATOR decision, if any;
- explicit implementation/runtime prohibitions;
- immutable readback;
- recommended independent review boundaries for SHT / ARH / SIS without activating them automatically.

## Prohibited

- shard write;
- host access;
- runtime implementation;
- provider call;
- automation mutation;
- production deployment;
- Project Sources/canon mutation;
- memory-layering attempt 3;
- historical PROMPT replay;
- declaring CHECKPOINT_DURABLE implemented;
- declaring autonomous conveyor operational.

After one immutable result, exact readback and addressed return to KOO, STOP.
