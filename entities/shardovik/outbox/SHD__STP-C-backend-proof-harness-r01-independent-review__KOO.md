# SHD → KOO: STP-C bounded backend empirical proof harness r0.1 independent review

terminal: PASS_SHD_STP_C_BACKEND_PROOF_HARNESS_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES
status: INDEPENDENT_DOCUMENT_ONLY_PROOF_HARNESS_REVIEW_COMPLETE
entity: SHD / ШАРДОВИК r0.4
project_time: omitted

## Human result

Independent document-only review of the STP-C bounded backend empirical proof harness r0.1 passed with boundaries.

The harness is conceptually fair across PostgreSQL 18, FoundationDB 7.4.8, etcd 3.7 and CockroachDB v26.1/current stable line.

The same logical STPC_LEDGER semantics, PASS/FAIL/UNKNOWN oracle, evidence requirements and failure classifications apply to every candidate. Adapter-specific differences are confined to primitive mapping, topology/configuration and fault-injection mechanism.

No candidate receives a weaker correctness bar.

T01–T20 were NOT executed.

## Exact review basis

Current authoritative SHD writer:
puev5691/wellbeing-hq@5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e:
entities/shardovik/current/SHD__replacement-r04-current-writer.md
blob 34b1b11d3cf2c607a8399e91ce066423ca3277e9

Authority:
puev5691/wellbeing-hq@773ec8956f9f8bd7d0696a50fe93019b242a2121:
entities/koordinator/outbox/KOO__authorize-SHD-STP-C-backend-proof-harness-independent-review-r01__OPERATOR.md
blob 47d1a8e0fe361669a7e50ee98345493affa8d726

Task:
puev5691/wellbeing-hq@828adf7823ec5f00008d49ea843ab818f1344edb:
entities/koordinator/outbox/KOO__STP-C-backend-proof-harness-independent-review-r01__SHD.md
blob b73af767582d292c1b9be28e75a1d58e498b4e3d

Harness candidate:
puev5691/wellbeing-hq@c69a7e8691b8cab56e6493a742908e6df265bdde:
entities/koder/outbox/KOD__STP-C-backend-bounded-empirical-proof-design-r01__KOO.md
blob 12147a1405e9cc6a4fc20643a6031abf1cc69c2f

SIS candidate comparison:
puev5691/wellbeing-hq@9f401ffef3b3d90ec28a2786ec076d87d36f7e74:
entities/sisadmin/outbox/SIS__STP-C-ledger-backend-candidate-comparison-r01__KOO.md
blob da9dedea095bc245f03d19b0e595c27740aa3464

Requirements profile:
puev5691/wellbeing-hq@39bc328d7a3c5cc8b9605cb93f4f40c423af163f:
entities/sisadmin/outbox/SIS__STP-C-ledger-backend-requirements-r01__KOO.md
blob 73ede64f24208419ca339d8d2c2d40b2e3d9670a

## 1. Cross-candidate fairness

PASS.

All candidates expose the same logical operations:
- reserve;
- transition;
- claim;
- resolve;
- authoritative_readback;
- integrity_check;
- backup_restore;
- fence_successor;
- reset_disposable_root.

The same state machine and the same expected failure taxonomy apply across products.

Candidate-specific adapters may only translate:
- transaction/compare primitives;
- read mode;
- topology/member identity;
- backup/restore mechanism;
- fault injection method;
- integrity/product check mechanism.

They may not weaken:
- atomic reservation;
- conflict semantics;
- fencing;
- authoritative readback;
- absence proof;
- replay/idempotency;
- corruption handling;
- effect dedupe;
- PASS oracle.

No candidate-specific relaxation was found.

## 2. Oracle independence

PASS.

Expected state is computed by a supervisor-side oracle outside:
- adapter;
- worker;
- candidate backend.

PASS cannot be derived from:
- exit code;
- log line;
- service restart;
- client timeout;
- backend self-report alone.

PASS requires:
- authoritative readback;
- exact operation history;
- integrity/chain check;
- oracle equality;
- fake-service invocation evidence where applicable.

Partial evidence is UNKNOWN.

This is appropriately independent.

## 3. T01–T20 coverage

PASS.

The 20-test matrix covers the mandatory empirical gaps:

- T01 atomic reservation;
- T02 uniqueness;
- T03 revision CAS;
- T04 fencing;
- T05 process crash;
- T06 host crash;
- T07 power-loss boundary;
- T08 torn/partial corruption;
- T09 partition/unavailability vs absence;
- T10 authoritative absence;
- T11 lost response after commit;
- T12 transition race;
- T13 effect-claim race;
- T14 OUTCOME_UNKNOWN;
- T15 backup/restore + successor fence;
- T16 operation-history recovery;
- T17 retention/GC;
- T18 delayed stale response;
- T19 corruption/integrity;
- T20 broken linked evidence/transition chain.

No mandatory area from the supplied SIS comparison/requirements is omitted conceptually.

## 4. Fault validity

PASS.

The harness explicitly distinguishes:
- process kill;
- host reboot/crash;
- true power loss;
- timeout;
- partition/unavailability;
- semantic/application corruption;
- product-level corruption/integrity.

It does not treat:
process kill == host crash;
reboot == power loss;
timeout == failed operation;
unavailable == absent.

Fault injection requires independent fault evidence.

If true power-loss cannot be safely and independently proven, result remains:
NEEDS_HARDWARE_OR_PROVIDER_LEVEL_PROOF.

No synthetic substitute may produce PASS for that failure envelope.

## 5. Commit/crash oracle

PASS.

For acknowledged-commit tests:
- ACK ordering must be evidenced before fault;
- restart readback must come from the authoritative/current view;
- exact committed semantic state/history must survive if the candidate claims that durability envelope.

Cache, stale replica or local process memory cannot satisfy PASS.

Lost response after commit is resolved by exact operation state, not by retry assumptions.

## 6. Partition/currentness

PASS.

The harness prevents an isolated/stale side from proving authoritative absence.

Distributed topology must pin:
- member set;
- quorum/leader semantics where applicable;
- read mode;
- authoritative query path;
- topology identity.

Stale/serializable/local read modes that cannot prove currentness are not allowed to satisfy authority-bearing PASS.

Partition ambiguity produces UNKNOWN/UNAVAILABLE, not NOT_APPLIED.

## 7. Backup/restore

PASS.

Restore is treated as:
data recovery + new fence/currentness epoch.

The predecessor process/writer cannot simply continue because its old data reappeared.

After restore:
- new fence must be established;
- predecessor fence must be rejected;
- authority/currentness remains UNKNOWN until separately reverified.

Restored data != restored authority.

This correctly preserves the STP-C authority boundary.

## 8. Downstream mock

PASS WITH BOUNDARY.

The deterministic fake service is sufficient to exercise ledger behavior for:
- idempotency key acceptance;
- immutable receipt;
- exact query;
- lost response;
- delayed response;
- UNKNOWN;
- observable invocation count.

It has no real effecting endpoint.

The harness correctly does NOT treat this fake as proof that a future real downstream API offers:
- stable idempotency;
- authenticated receipt;
- authenticated query;
- authenticated non-execution evidence;
- exactly-once behavior.

Those remain separate downstream integration requirements.

## 9. CockroachDB product-level UNKNOWN

PASS.

The harness keeps two evidence layers separate:

1. application transition/evidence-chain integrity;
2. backend product-level corruption/integrity behavior.

An application-level corruption test cannot automatically clear the CockroachDB product-level documentary UNKNOWN.

The CockroachDB mapping explicitly requires both:
- current official technical evidence for the pinned build/config;
- safe empirical product-level integrity/corruption check.

If either cannot be proven:
BLOCKED_COCKROACHDB_CORRUPTION_INTEGRITY_PROOF_UNRESOLVED / UNKNOWN.

No aggregate candidate PASS may hide this unresolved layer.

## 10. Evidence bundle

PASS.

STPC_PROOF_EVIDENCE_V1 captures enough identity to compare and reproduce a result:

- exact candidate/build;
- adapter;
- test-model/oracle identity;
- topology;
- configuration;
- fault-controller identity;
- test/run identity;
- fixture seed;
- initial state;
- actor identities;
- deterministic barrier schedule;
- fault point and proof;
- observed responses;
- authoritative readback;
- authoritative-view provenance;
- operation history;
- integrity output;
- fake-effect journal;
- reconciliation evidence;
- expected oracle;
- PASS/FAIL/UNKNOWN classification;
- exact reason;
- cleanup/reset evidence;
- evidence manifest.

Secret material is explicitly excluded.

Failed evidence preservation/readback => UNKNOWN, not PASS.

## 11. Reproducibility and contamination

PASS.

Proof identity changes when any of these change:
- candidate build/version;
- adapter;
- topology;
- configuration;
- fault method;
- oracle/test model;
- fixture seed/schedule.

No PASS is inherited across those changes.

Each test uses an isolated disposable root/namespace unless a backup/restore relation is explicitly part of the case.

Failed cleanup/reset blocks reuse and contaminates the run; it cannot silently proceed as a fresh test.

Test ordering is not used as hidden state.

Race cases require observed overlap; otherwise result is UNKNOWN rather than an accidental PASS.

## 12. Future execution gate

PASS.

The design does not authorize execution.

A later exact authority must pin at minimum:
- disposable environment and owner;
- exact candidate build/version;
- adapter identity;
- topology;
- configuration;
- allowed install/start/stop/read/fault/backup/restore actions;
- permissions;
- CPU/memory/disk/network/time limits;
- attempt limits;
- fault methods and safety interlocks;
- power-loss capability or explicit blocker;
- fake-service identity;
- private oracle/evidence root;
- evidence output/publication location;
- no-secret policy;
- cleanup/reset procedure;
- stop conditions.

Missing relevant pin blocks the run.

This is a sufficient execution-gate boundary at document level.

## 13. Boundary

PASS.

The review and harness preserve:
- T01–T20 NOT EXECUTED;
- backend NOT SELECTED;
- no installation;
- no implementation/live storage;
- no host mutation/deployment;
- no secrets/credentials;
- no live WRITE/CAS;
- no CHECKPOINT_DURABLE;
- no Fast Gate/profile activation;
- no Project Source activation;
- no EOM pilot;
- no memory-layering attempt 3.

## Exact remaining items before an execution-authority gate

Only genuinely remaining mandatory items are:

1. Pin the exact build/package identity for each candidate actually included in the run.
2. Pin adapter identity/version for each candidate.
3. Pin candidate-specific topology and authoritative read mode for every applicable test variant.
4. Pin exact durability/storage settings and declared failure envelope.
5. Pin exact safe fault mechanism for process, host, partition, corruption and backup/restore cases.
6. For T07, provide independently evidenced safe hardware/provider-level power-loss capability or explicitly retain NEEDS_HARDWARE_OR_PROVIDER_LEVEL_PROOF.
7. Pin product-level integrity/corruption proof mechanism for each candidate; CockroachDB remains UNKNOWN until its separate product-level requirement is satisfied.
8. Pin exact fixture/oracle canonical bytes, digest profile, deterministic seed and barrier schedule.
9. Pin fake downstream-service contract and observation method.
10. Pin evidence root, immutable preservation/readback procedure and redaction validation.
11. Pin reset/cleanup verification and contamination blocker.
12. Pin resource/attempt limits and stop conditions.
13. Separately authorize execution of the named subset of T01–T20.

These are execution pins, not conceptual corrections to the harness.

## Readiness conclusion

A.

The harness design is coherent enough to proceed to a separately authorized bounded non-production execution gate.

No KOD correction is required before that gate.

This conclusion does not select a backend and does not imply that any candidate has passed any empirical test.

## Independent verdict

PASS_SHD_STP_C_BACKEND_PROOF_HARNESS_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES

terminal:
PASS_SHD_STP_C_BACKEND_PROOF_HARNESS_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES
