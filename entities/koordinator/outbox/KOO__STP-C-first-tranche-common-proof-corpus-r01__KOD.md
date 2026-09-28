# KOO → KOD: STP-C first-tranche common proof corpus r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KOD / КОДЕР
scope: DOCUMENT_ONLY_COMMON_PROOF_CORPUS_PREPARATION
project_time: omitted

Resume-First.

Current authoritative KOD writer:

puev5691/wellbeing-hq@df92a8bfcce29294332f6e4de3391a3e7966adfd:
entities/koder/current/KOD__replacement-current-writer-v05.md

writer_gate_outcome:
WRITER_ESTABLISHED

Exact authority:

puev5691/wellbeing-hq@54a6af07aa123764bd3dde359570717b41b1c7c6:
entities/koordinator/outbox/KOO__authorize-KOD-STP-C-first-tranche-common-proof-corpus-r01__OPERATOR.md

Exact SIS execution-envelope blocker:

puev5691/wellbeing-hq@398d875db1a265e4c941288642250c6f42f6cbab:
entities/sisadmin/outbox/SIS__STP-C-backend-proof-execution-envelope-r01__KOO.md

blob:
875fb2f2365fdd62d4a7ae5207bb51d35304fa43

Exact reviewed harness:

puev5691/wellbeing-hq@c69a7e8691b8cab56e6493a742908e6df265bdde:
entities/koder/outbox/KOD__STP-C-backend-bounded-empirical-proof-design-r01__KOO.md

blob:
12147a1405e9cc6a4fc20643a6031abf1cc69c2f

Prepare only the common machine-readable proof corpus for the proposed first tranche:

T01 atomic reservation
T02 uniqueness race
T03 state_revision CAS
T04 stale process_fence
T10 authoritative absence
T12 concurrent transition race

Do NOT implement candidate adapters.
Do NOT execute any test.

The goal is to close only SIS blockers M11-M15.

## 1. Package contents

Create one standalone candidate package containing at minimum:

A. machine-readable STPC_LEDGER_V1 model/schema;
B. independent supervisor-side oracle implementation;
C. frozen canonical fixture bytes;
D. fixture manifest;
E. exact digest/identity profile;
F. deterministic seed artifact;
G. deterministic barrier/schedule artifact for T01/T02/T03/T04/T10/T12;
H. expected outcome vectors;
I. package README/spec tying artifacts to harness r0.1.

No candidate-specific backend primitive or driver code.

## 2. Machine-readable model

Define closed machine-readable fields for the first tranche sufficient to represent at minimum:

- namespace;
- request_id;
- request_digest;
- operation_id;
- nonce_identity;
- intended_effect_identity/idempotency_key where needed by common model;
- current_state;
- state_revision;
- process_fence;
- transition_identity;
- evidence_identity;
- collision/conflict classification;
- authoritative absence classification;
- ordered transition history.

Unknown fields must fail validation.
No implicit defaults for authority-relevant fields.

Keep this model consistent with:
KOD replay/effect ledger atomicity r0.1
and
KOD bounded empirical proof harness r0.1.

## 3. Independent oracle

Implement a candidate-independent oracle that consumes:
- frozen fixture;
- exact test_id;
- deterministic schedule/barrier events;
- actor actions;
- observed candidate-neutral outputs/evidence;

and returns expected:
- authoritative projection;
- allowed classification set;
- forbidden outcomes;
- PASS / FAIL / UNKNOWN only after evidence completeness validation.

The oracle must not:
- call any backend;
- import/use any candidate adapter;
- infer expected state from candidate logs;
- convert missing evidence to PASS;
- convert unavailable to absent.

Provide deterministic self-tests for oracle logic only.
Self-tests are NOT T01-T20 execution.

## 4. Canonical fixture bytes

Freeze exact bytes for common synthetic values used by tranche, including at minimum:
- namespace;
- R1/D1/O1/N1/E1/K1/F1;
- R2/D2/O2/N2/E2/K2/F2;
- exact initial state fixtures S0/S1 and any common transition input required by T03/T04/T12;
- authoritative-absence fixture for T10.

No real seat identity, secret, credential, task authority or production identifier.

The frozen bytes and manifest must be immutable inside the package.

## 5. Digest profile

Choose and specify one exact non-secret digest/identity profile suitable for test corpus identity, including:
- algorithm;
- byte encoding;
- domain-separation labels;
- lowercase/uppercase rule;
- field ordering/canonicalization;
- whether newline termination is significant;
- how composite identities are built.

This digest profile is for test corpus/evidence identity only.
It does NOT choose STP-C production signing/key algorithms and does NOT activate any trust root.

If using SHA-256, state this boundary explicitly.

## 6. Deterministic seed and schedule

Freeze:
- exact seed bytes/value;
- actor naming;
- barrier IDs;
- release order;
- schedule representation;
- race-overlap validation rule.

For T02/T03/T12:
a race cannot PASS unless overlap/barrier participation is evidenced.

For T04:
the stale actor must be proven paused before F2 establishment and released after F2 is authoritative.

For T10:
schedule must prove a healthy authoritative read path with no injected unavailability.

## 7. Expected outcome vectors

For each of T01/T02/T03/T04/T10/T12 define machine-readable expected vectors:
- initial projection;
- actor operations;
- allowed outcomes;
- exact forbidden outcomes;
- required evidence fields;
- PASS conditions;
- UNKNOWN conditions.

No candidate-specific relaxation.

## 8. Corpus identity

Produce:
- immutable package tree identity;
- per-file identities;
- exact readback verification;
- one corpus identity derived under the selected digest profile.

Any later change to:
- model;
- oracle;
- fixture bytes;
- digest profile;
- seed;
- schedule;
- expected vectors
must create a new corpus identity/version.

## 9. Security/boundary checks

Verify package contains:
- no secrets;
- no host path assumptions;
- no backend credentials;
- no live endpoint;
- no install/start/stop commands;
- no candidate adapter code;
- no production data.

## 10. Result

Return exact status for each closed pin:

M11 machine-readable STPC_LEDGER model
M12 independent oracle implementation identity
M13 frozen fixture canonical bytes + manifest
M14 exact digest profile
M15 deterministic seed + barrier schedule artifact

If all five are complete and read back:
COMMON_PROOF_CORPUS_M11_M15_READY_FOR_INDEPENDENT_REVIEW

Otherwise return exact missing blocker.

Expected terminal:

PASS_KOD_STP_C_FIRST_TRANCHE_COMMON_PROOF_CORPUS_R01_READY_FOR_INDEPENDENT_REVIEW

or exact BLOCKED_/FAIL_.

Do NOT:
- implement PostgreSQL/FoundationDB/etcd/CockroachDB adapters;
- install/run any backend;
- execute T01-T20;
- select backend;
- pick candidate-specific topology/config;
- create live storage;
- mutate hosts;
- deploy;
- use secrets;
- enable live WRITE/CAS;
- claim CHECKPOINT_DURABLE;
- activate Fast Gate/profile;
- activate Project Sources;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
