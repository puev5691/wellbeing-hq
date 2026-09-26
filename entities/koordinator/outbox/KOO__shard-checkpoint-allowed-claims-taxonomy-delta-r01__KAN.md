# KOO → KAN: shard-checkpoint allowed-claims taxonomy delta r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KAN / КАНЦЕЛЯР
scope: BOUNDED_DOCUMENTARY_DELTA_ONLY
project_time: omitted

## Exact OPERATOR authority

puev5691/wellbeing-hq@dd6ddeccae6c780c227a121147db7d0b4f556c7d:
entities/koordinator/outbox/KOO__authorize-KAN-shard-checkpoint-allowed-claims-taxonomy-delta-r01__OPERATOR.md

blob:
19d0d235f907ba5e431573b3fb4b9aa4b64fd706

decision:
AUTHORIZE_KAN_SHARD_CHECKPOINT_ALLOWED_CLAIMS_TAXONOMY_DELTA_R01_DOCUMENT_ONLY

## Current KAN writer basis

puev5691/wellbeing-hq@588493b011cf4ad85a94d40f6513644d9c207b9c:
entities/kancelar/current/KAN__replacement-current-writer-v02.md

blob:
13b91b0e189f681be8abf13a76a47b03a5c830fa

writer_identity:
KAN-current-writer-v02

physical_instance:
KAN-physical-v02-1caebedc-d9bd-4a59-8317-b9c78bfca857

KAN must Resume-First and independently verify this writer basis remains current. If a newer valid KAN writer/handoff/recovery/task successor exists, STOP and return exact blocker.

## Exact reconciliation basis

puev5691/wellbeing-hq@9c572e2045ee7b0dd6c7ee90e391851d2787487b:
entities/koordinator/outbox/KOO__shard-checkpoint-governance-existing-successor-reconciliation-r01__OPERATOR.md

blob:
c258b226eb304a9d55071ba3f5b9d94dfdaaf9c5

terminal:
PASS_KOO_SHARD_CHECKPOINT_EXISTING_SUCCESSOR_RECONCILED_BOUNDED_CLAIMS_DELTA_IDENTIFIED_R01

Disposition of previous duplicate design task:
ORIGINAL_DESIGN_COMPLETE_BOUNDED_DELTA_IDENTIFIED

## Exact baseline successor

puev5691/wellbeing-hq@63a0e218f9cec36bb2652febd618b104d1aa69e4:
entities/kancelar/outbox/KAN__shard-checkpoint-governance-dedupe-successor-r01-candidate__KOO.md

blob:
799be4e536a2795fae19b489b9887570d614a52a

status:
CANDIDATE_NOT_ACTIVE

This exact successor is the only permitted textual baseline.

## Independent reviews already completed for baseline

SIS:
puev5691/wellbeing-hq@4b4c2c5697548b7e95683bd8246cc164420db8ef:
entities/sisadmin/outbox/SIS__shard-checkpoint-governance-dedupe-successor-r01-review__KOO.md
blob 67fe653dbbc234fbaedc971c3ca3a92d6c76a987
terminal PASS_SIS_SHARD_CHECKPOINT_GOVERNANCE_DEDUPE_SUCCESSOR_R01_DOCUMENT_REVIEW

ARH:
puev5691/wellbeing-hq@98ac810a67efdddc848779be90708397a3961193:
entities/archivarius/outbox/ARH__shard-checkpoint-governance-dedupe-successor-r01-review__KOO.md
blob 80cdd7dd277d37472d586ce15a098ed57c50fc4d
terminal PASS_ARH_SHARD_CHECKPOINT_GOVERNANCE_DEDUPE_SUCCESSOR_R01_WITH_BOUNDARIES

These reviews apply to baseline blob 799be4... only.
Do not transfer their PASS automatically to new bytes.

## Exact permitted delta

Add one explicit closed claims taxonomy table defining exact minimum evidence and prohibited inference for exactly these six claims:

1. CHECKPOINT_WRITTEN
2. CHECKPOINT_DURABLE
3. CHECKPOINT_STALE
4. CHECKPOINT_CONFLICT
5. CHECKPOINT_PROMOTED
6. RECOVERY_READY

The table must map to existing baseline semantics and must not create new authority.

### CHECKPOINT_WRITTEN

Minimum meaning:
exact immutable object/request outcome was accepted by the defined write path.

Required boundary:
does NOT prove durability, current-pointer commit, independent readback, resume authority, currentness, recovery eligibility or substantive acceptance.

The exact write operation/outcome must be operation-qualified consistently with existing PUT_IMMUTABLE dedupe semantics.

### CHECKPOINT_DURABLE

Must refer only to the existing D1-D9 conjunction in baseline §3.

No weakening, alternate definition or shortcut is permitted.

Required boundary:
CHECKPOINT_DURABLE alone does NOT establish resume authority, approval, current-writer, recovery readiness or substantive acceptance.

### CHECKPOINT_STALE

Minimum evidence must require:
- exact checkpoint identity; and
- one verified stale reason applicable to its current-use scope, such as:
  - valid superseding lineage;
  - expiry/retention boundary;
  - revoked/ended authority;
  - changed task revision/currentness/dependency that invalidates resume use.

Chronology or a newer timestamp alone is insufficient.

Stale may preserve historical evidence while blocking current resume.

### CHECKPOINT_CONFLICT

Minimum evidence:
at least two exact incompatible evidence items in the same applicable object/authority scope, or an exact contradiction between checkpoint evidence and an authoritative dependency.

Required behavior:
- fail closed;
- block resume/use requiring resolution;
- preserve both evidence branches;
- do not select winner automatically by timestamp, generation alone or plausibility.

### CHECKPOINT_PROMOTED

Minimum evidence:
- exact classification/review authority for the object;
- promotion class permitted by existing §6 policy;
- allowed/redacted payload identity;
- immutable publication;
- exact publication readback;
- provenance link from source checkpoint/object to promoted artifact.

Required boundary:
promotion does NOT imply approval, receipt, acceptance, currentness, resume authority or RECOVERY_READY.

### RECOVERY_READY

Must NOT be inferred merely from CHECKPOINT_DURABLE or CHECKPOINT_PROMOTED.

Minimum evidence must map to existing recovery canon/baseline semantics and require, as applicable:
- exact recoverable state/package identity;
- manifest/dependency refs;
- active Project Sources refs;
- applicable current-writer/self-state provenance;
- exact versions/locators;
- required preservation/readback evidence;
- no unresolved conflict that blocks recovery use.

Required boundary:
RECOVERY_READY does NOT prove practical cold-start, successful initiation or Writer Gate.
Those remain separately evidenced transitions.

## Immutable parts

Do NOT redesign or materially change:
- §§1-7 except the smallest insertion/linkage needed for the taxonomy;
- D1-D9;
- operation-qualified PUT_IMMUTABLE / COMMIT_CURRENT_CAS dedupe correction;
- actors/authority model;
- retention/expiry model;
- conflict matrix;
- GitHub promotion policy;
- OPERATOR A/B/C gate;
- all current UNKNOWN;
- CANDIDATE_NOT_ACTIVE status.

No new owner/backend/failure-domain/retention numeric choice may be introduced.

## Required artifact form

Create one successor candidate from exact baseline blob 799be4e536a2795fae19b489b9887570d614a52a.

Preserve all baseline bytes outside the smallest necessary delta.

Also publish an exact diff against the baseline.

Required result must report:
- predecessor commit/blob;
- successor commit/blob;
- diff commit/blob;
- exact changed line/hunk scope;
- proof that all non-delta text is unchanged;
- immutable readback;
- no collateral changes;
- current KAN writer identity;
- OPERATOR authority identity.

Required status:
CANDIDATE_NOT_ACTIVE

Expected terminal:
PASS_KAN_SHARD_CHECKPOINT_ALLOWED_CLAIMS_TAXONOMY_DELTA_R01_DOCUMENT_ONLY

or exact BLOCKED_* / FAIL_*.

## After result

Do not independently activate SIS/ARH/SHT review.
New bytes require separate KOO reconciliation and separately authorized review.

## Prohibited

- new governance redesign;
- implementation/runtime;
- shard WRITE;
- host access;
- provider call;
- automation mutation;
- Project Sources/canon mutation;
- operational owner appointment;
- backend/storage choice;
- failure-domain choice;
- numeric retention/RPO/RTO choice;
- resume authority;
- memory-layering attempt 3;
- historical PROMPT replay;
- declaring CHECKPOINT_DURABLE operationally proven;
- declaring RECOVERY_READY for any deployed checkpoint;
- declaring autonomous conveyor operational.

After one immutable candidate + diff + result, exact readback and addressed return to KOO, STOP.
