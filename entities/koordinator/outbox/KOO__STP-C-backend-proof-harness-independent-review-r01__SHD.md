# KOO → SHD: independent review STP-C bounded backend empirical proof harness r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHD / ШАРДОВИК
scope: INDEPENDENT_DOCUMENT_ONLY_PROOF_HARNESS_REVIEW
project_time: omitted

Resume-First.

Current authoritative SHD writer:

puev5691/wellbeing-hq@5d83ac00eeebc76fb78cc0b0e376028d5c1a8a4e:
entities/shardovik/current/SHD__replacement-r04-current-writer.md

Writer Gate result:

puev5691/wellbeing-hq@0b18917db27b81994e2de08963988812eff1728f:
entities/shardovik/outbox/SHD__replacement-r04-writer-gate-result__KOO.md

Exact authority:

puev5691/wellbeing-hq@773ec8956f9f8bd7d0696a50fe93019b242a2121:
entities/koordinator/outbox/KOO__authorize-SHD-STP-C-backend-proof-harness-independent-review-r01__OPERATOR.md

Exact harness candidate:

puev5691/wellbeing-hq@c69a7e8691b8cab56e6493a742908e6df265bdde:
entities/koder/outbox/KOD__STP-C-backend-bounded-empirical-proof-design-r01__KOO.md

blob:
12147a1405e9cc6a4fc20643a6031abf1cc69c2f

Exact SIS comparison:

puev5691/wellbeing-hq@9f401ffef3b3d90ec28a2786ec076d87d36f7e74:
entities/sisadmin/outbox/SIS__STP-C-ledger-backend-candidate-comparison-r01__KOO.md

blob:
da9dedea095bc245f03d19b0e595c27740aa3464

Exact requirements profile:

puev5691/wellbeing-hq@39bc328d7a3c5cc8b9605cb93f4f40c423af163f:
entities/sisadmin/outbox/SIS__STP-C-ledger-backend-requirements-r01__KOO.md

Review only the document-only harness design.
T01-T20 are NOT executed.

Candidates remain:

- PostgreSQL 18
- FoundationDB 7.4.8
- etcd 3.7
- CockroachDB v26.1/current stable line

No ranking. No backend selection.

Check at minimum:

1. Cross-candidate fairness
- same logical STPC_LEDGER semantics;
- same PASS/FAIL/UNKNOWN oracle;
- candidate adapters may differ only in primitive mapping/fault mechanism;
- no candidate-specific relaxation of mandatory semantics.

2. Oracle independence
- expected state must be derived outside candidate/adapter;
- candidate logs/exit codes/service restart must not define PASS;
- exact authoritative readback + history + integrity evidence required.

3. T01-T20 coverage
Confirm whether the set actually covers the mandatory empirical gaps from SIS comparison/requirements:
- atomic reservation;
- uniqueness;
- revision CAS;
- fencing;
- process/host crash;
- power-loss boundary;
- corruption/torn write;
- partition/unavailability vs absence;
- authoritative absence;
- lost response;
- transition race;
- effect-claim race;
- OUTCOME_UNKNOWN;
- backup/restore;
- operation-history recovery;
- retention;
- stale delayed response;
- corruption integrity;
- missing evidence/chain break.

4. Fault validity
- process kill != host crash;
- host reboot != power loss;
- timeout != operation failure;
- unavailable != absent;
- fault injection must be independently evidenced;
- unsafe/unavailable true power-loss proof must remain NEEDS_HARDWARE_OR_PROVIDER_LEVEL_PROOF.

5. Crash/commit oracle
- acknowledged commit test must establish ordering of ACK before injected fault;
- readback after restart must be authoritative;
- no unproven cache/replica state may satisfy PASS.

6. Partition/currentness
- isolated/stale side cannot answer authoritative absence;
- distributed candidate quorum/leader/member behavior must be pinned per topology;
- stale read modes must not silently pass authority-bearing tests.

7. Backup/restore
- restore is a fence/currentness epoch event;
- predecessor writer/process cannot resume authority after restore;
- restored data existence != restored authority.

8. Downstream mock validity
- deterministic fake service only;
- idempotency, receipt, query, lost/delayed response and UNKNOWN behavior are sufficient to exercise ledger semantics;
- fake service must not accidentally prove guarantees belonging to a real downstream API.

9. CockroachDB UNKNOWN
- verify harness does not convert missing documentary corruption/integrity evidence into product PASS by merely testing application-level chain integrity;
- product-level and application-level integrity evidence must remain distinguishable;
- unresolved product-level proof must remain UNKNOWN/blocking where required.

10. Evidence bundle
Check whether evidence is enough to reproduce/compare:
- exact candidate build;
- topology;
- config;
- fixture;
- seed/schedule;
- fault point;
- actor identity;
- responses;
- authoritative readback;
- history;
- integrity result;
- classification and reason.

No secrets.

11. Reproducibility / contamination
- reset isolates tests;
- result cannot be reused after candidate version/config/topology change;
- failed cleanup contaminates next run => block/UNKNOWN;
- run ordering cannot create hidden dependence unless explicitly specified.

12. Execution-gate completeness
Confirm later execution cannot begin without separately pinned:
- disposable environment;
- exact candidate version/build;
- topology;
- configuration;
- allowed commands/actions;
- resource limits;
- fault methods;
- evidence output location;
- cleanup;
- stop conditions.

13. Boundary
Review must explicitly preserve:
- no T01-T20 execution;
- no backend selection;
- no implementation/live storage;
- no host mutation/deployment;
- no live WRITE/CAS;
- no CHECKPOINT_DURABLE.

Return one conclusion:

A.
PASS_SHD_STP_C_BACKEND_PROOF_HARNESS_R01_INDEPENDENT_REVIEW_WITH_BOUNDARIES
and state exact remaining items needed before a later execution-authority gate;

or

B.
exact FAIL_/BLOCKED_ with only critical conceptual defects requiring KOD correction.

Do NOT:
- run tests;
- install backends;
- choose a backend;
- alter candidate;
- touch live hosts/storage;
- deploy;
- use secrets/credentials;
- enable live WRITE/CAS;
- claim CHECKPOINT_DURABLE;
- activate Fast Gate/profile;
- activate Project Sources;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
