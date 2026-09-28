# SIS → KOO: STP-C ledger backend candidate discovery/comparison r0.1

terminal: PASS_SIS_STP_C_LEDGER_BACKEND_CANDIDATE_COMPARISON_R01_READY_FOR_DECISION_OR_PROOF
gate: READY_FOR_BOUNDED_EMPIRICAL_BACKEND_PROOF
status: CANDIDATE_COMPARISON_NOT_SELECTION
scope: DOCUMENT_ONLY_BACKEND_CANDIDATE_DISCOVERY_COMPARISON
project_time: omitted

## 0. Human result

A bounded discovery/comparison was performed against the exact mandatory requirements from:

puev5691/wellbeing-hq@39bc328d7a3c5cc8b9605cb93f4f40c423af163f:
entities/sisadmin/outbox/SIS__STP-C-ledger-backend-requirements-r01__KOO.md

blob:
73ede64f24208419ca339d8d2c2d40b2e3d9670a

Four technically plausible candidates remain after documentary screening:

1. PostgreSQL 18
2. FoundationDB 7.4.8
3. etcd 3.7
4. CockroachDB v26.1 / current stable documentation line

No candidate is selected.
No ranking or scoring is performed.

All four expose a plausible path to the mandatory STP-C ledger guarantees, but all retain deployment/configuration and fault-model assumptions that must be proven in a bounded non-production harness before OPERATOR backend selection.

Therefore:

READY_FOR_BOUNDED_EMPIRICAL_BACKEND_PROOF

CHECKPOINT_DURABLE remains NOT_ESTABLISHED.

## 1. Exact authority and task basis

Current authoritative SIS writer:

puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

Writer Gate:

puev5691/wellbeing-hq@f5b7cb520a9f357d95292556fe87efd11570b09f:
entities/sisadmin/outbox/SIS__emergency-replacement-writer-gate-r06__KOO.md

Exact authority:

puev5691/wellbeing-hq@23858faf814e6c3254c16045212bb3e6c47087bd:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-ledger-backend-candidate-comparison-r01__OPERATOR.md

Exact task:

puev5691/wellbeing-hq@0f60fcb56a493d8637405f0c642d3d87f9c86ba7:
entities/koordinator/outbox/KOO__STP-C-ledger-backend-candidate-comparison-r01__SIS.md

Exact SHD ledger review:

puev5691/wellbeing-hq@3a485af0511e59516504a6357df3caf841bcad8a:
entities/shardovik/outbox/SHD__STP-C-replay-effect-ledger-atomicity-r01-independent-review__KOO.md

Exact KOD ledger contract:

puev5691/wellbeing-hq@1901fa683df010e9bf3e98d250ba7032c1fdf018:
entities/koder/outbox/KOD__STP-C-replay-effect-ledger-atomicity-design-r01__KOO.md

blob:
98bcee62b376b3d9b1ac52812d483b01fae9daa5

## 2. Status vocabulary

Only these statuses are used for candidate requirement evaluation:

SUPPORTED_BY_DOCUMENTED_PRIMITIVE
SUPPORTED_WITH_DESIGN_CONSTRAINT
NEEDS_EMPIRICAL_PROOF
UNKNOWN
DISQUALIFIED

UNKNOWN is never treated as PASS.

Product feature is not treated as configured deployment guarantee.

## 3. Discovery method and source rule

Inclusion required a plausible documented path for all core mandatory properties:

- atomic multi-key reservation or equivalent;
- uniqueness under concurrency;
- compare-and-transition / fencing equivalent;
- crash durability;
- exact operation-history recovery;
- authoritative absence semantics;
- corruption handling;
- cross-process correctness.

Marketing claims were not used as sole technical evidence.

Primary/official technical documentation was used where practically available.

## 4. Candidate A — PostgreSQL 18

### Official technical source locators

- Transactions / isolation:
  https://www.postgresql.org/docs/18/transaction-iso.html
- Unique constraints:
  https://www.postgresql.org/docs/18/ddl-constraints.html
- INSERT / ON CONFLICT:
  https://www.postgresql.org/docs/18/sql-insert.html
- WAL:
  https://www.postgresql.org/docs/18/wal-intro.html
- Reliability / durable storage assumptions:
  https://www.postgresql.org/docs/18/wal-reliability.html
- Non-durable settings and power-loss implications:
  https://www.postgresql.org/docs/18/non-durability.html
- Data checksums:
  https://www.postgresql.org/docs/18/checksums.html
- pg_amcheck:
  https://www.postgresql.org/docs/18/app-pgamcheck.html
- Backup/restore:
  https://www.postgresql.org/docs/18/backup.html
- pg_verifybackup:
  https://www.postgresql.org/docs/18/app-pgverifybackup.html
- HA/replication overview:
  https://www.postgresql.org/docs/18/high-availability.html
- Hot standby freshness caveat:
  https://www.postgresql.org/docs/18/hot-standby.html
- Replication configuration / synchronous standbys:
  https://www.postgresql.org/docs/18/runtime-config-replication.html

### Documentary capability summary

PostgreSQL 18 provides ACID transactions, unique constraints, SERIALIZABLE isolation, WAL-based crash recovery, configurable durable commit behavior, data-page checksums, corruption-check tooling, backup/restore and synchronous/asynchronous replication options.

The STP-C ledger semantics would be application schema/protocol layered on these primitives.

### Requirement matrix

| Requirement | Status | Basis / constraint |
|---|---|---|
| Multi-key atomic reservation | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | One SQL transaction can atomically persist request/operation/nonce/evidence rows. |
| Uniqueness under concurrency | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | UNIQUE constraints and conflict handling are documented concurrency primitives. |
| Revision/state CAS equivalent | SUPPORTED_WITH_DESIGN_CONSTRAINT | Conditional UPDATE/locking/serializable transaction must bind expected revision. |
| Process fencing equivalent | SUPPORTED_WITH_DESIGN_CONSTRAINT | Fence token/revision must be application data atomically checked on every protected transition. |
| Durable commit | SUPPORTED_WITH_DESIGN_CONSTRAINT | Requires durable settings; disabling fsync/synchronous_commit/full_page_writes weakens guarantees. |
| Process crash recovery | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | WAL recovery model is documented. |
| Host crash/restart | SUPPORTED_WITH_DESIGN_CONSTRAINT | Depends on durable storage and configuration. |
| Power-loss boundary | NEEDS_EMPIRICAL_PROOF | PostgreSQL documents assumptions; actual storage/controller flush behavior remains deployment-specific. |
| Torn/partial-write handling | SUPPORTED_WITH_DESIGN_CONSTRAINT | WAL/full-page-write path plus checksums; exact injected-fault behavior still must be tested. |
| Cross-process visibility | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Transaction isolation/locking provides shared DB concurrency semantics. |
| Partition/unavailability semantics | NEEDS_EMPIRICAL_PROOF | Depends on single-primary vs synchronous/asynchronous replication and client routing. |
| Authoritative absence | SUPPORTED_WITH_DESIGN_CONSTRAINT | Must query authoritative primary/current transaction; hot standby may lag and cannot prove absence. |
| Corruption/integrity detection | SUPPORTED_WITH_DESIGN_CONSTRAINT | Checksums/amcheck/backup verification exist; application transition-chain integrity remains required. |
| Exact operation-history recovery | SUPPORTED_WITH_DESIGN_CONSTRAINT | Requires append-only/immutable ledger schema and retention policy. |
| Retention/GC feasibility | SUPPORTED_WITH_DESIGN_CONSTRAINT | Tables can retain exact evidence; GC must be application-governed. |
| Backup/restore implications | SUPPORTED_WITH_DESIGN_CONSTRAINT | Backup/PITR exists; restore must be treated as authority/fence epoch event, not transparent continuation. |
| Observability/readback | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SQL readback, system views and backup/check tools exist. |
| Deterministic test harness suitability | NEEDS_EMPIRICAL_PROOF | Fault injection and exact test oracle must be built for selected topology/config. |

### Deployment/configuration dependencies

Single-host:
- simpler authoritative read path;
- no replica-lag ambiguity;
- host/storage loss is a larger availability/fault boundary;
- power-loss durability depends strongly on local storage correctness.

Replicated:
- asynchronous standby cannot be used to prove current absence because PostgreSQL documents measurable replication delay;
- synchronous replication can improve failover durability but must be configured and empirically tested;
- failover requires a fresh process-fence/authority epoch so the old primary cannot later publish stale state.

### Current disqualifiers

None proven at documentary discovery stage.

A concrete PostgreSQL deployment becomes DISQUALIFIED if:
- authority-bearing reads are allowed from stale asynchronous replicas;
- durability settings permit acknowledged commits to vanish under claimed failure model;
- stale-primary/fence behavior is not externally prevented.

### Empirical proofs still required

- crash after acknowledged commit;
- power loss at transaction boundaries;
- torn-write/corruption injection;
- concurrent unique reservation/transition races;
- stale process after fence rollover;
- failover/partition with old primary delayed response;
- backup/restore followed by fence/currentness re-establishment;
- exact operation-history readback after restart.

## 5. Candidate B — FoundationDB 7.4.8

### Official technical source locators

- Current docs/version:
  https://apple.github.io/foundationdb/
- Developer Guide / ACID / strict serializability:
  https://apple.github.io/foundationdb/developer-guide.html
- Transaction API:
  https://apple.github.io/foundationdb/javadoc/com/apple/foundationdb/Transaction.html
- Consistency model:
  https://apple.github.io/foundationdb/consistency.html
- Architecture:
  https://apple.github.io/foundationdb/kv-architecture.html
- Configuration / redundancy modes:
  https://apple.github.io/foundationdb/configuration.html
- Consistency scan / CLI:
  https://apple.github.io/foundationdb/command-line-interface.html
- Backup/restore/DR:
  https://apple.github.io/foundationdb/backups.html
- Operations:
  https://apple.github.io/foundationdb/operations.html

### Documentary capability summary

FoundationDB 7.4.8 documents global ACID transactions with strict serializability, optimistic concurrency/conflict detection, committed-write durability, multi-node replication modes, consistency scanning and backup/restore/DR.

Uniqueness, process fences and ledger history are not relational built-ins; they must be encoded as transactional keys and conflict ranges.

### Requirement matrix

| Requirement | Status | Basis / constraint |
|---|---|---|
| Multi-key atomic reservation | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | FDB transactions atomically read/write multiple keys. |
| Uniqueness under concurrency | SUPPORTED_WITH_DESIGN_CONSTRAINT | Unique sentinel/index keys must be read/written transactionally with conflict detection. |
| Revision/state CAS equivalent | SUPPORTED_WITH_DESIGN_CONSTRAINT | Transactional read/conflict-range design can reject changed revision/fence. |
| Process fencing equivalent | SUPPORTED_WITH_DESIGN_CONSTRAINT | Fence key and protected transition keys must share transactional conflict scope. |
| Durable commit | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Docs state accepted transactions are redundantly stored and durable. |
| Process crash recovery | SUPPORTED_WITH_DESIGN_CONSTRAINT | Cluster transaction durability exists; application continuation semantics still need exact ledger design. |
| Host crash/restart | SUPPORTED_WITH_DESIGN_CONSTRAINT | Depends on redundancy mode; single mode is explicitly not fault tolerant. |
| Power-loss boundary | NEEDS_EMPIRICAL_PROOF | Product durability is documented; exact selected machines/storage/fault envelope still needs proof. |
| Torn/partial-write handling | NEEDS_EMPIRICAL_PROOF | Product architecture is fault tolerant, but STP-C requires explicit injected-fault observation for selected storage engine/config. |
| Cross-process visibility | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Strict serializability and causal visibility after commit are documented. |
| Partition/unavailability semantics | SUPPORTED_WITH_DESIGN_CONSTRAINT | Availability depends on configured redundancy/coordinators; transaction correctness remains strong. |
| Authoritative absence | SUPPORTED_WITH_DESIGN_CONSTRAINT | Must use ordinary strict-serializable transaction reads, not weakened snapshot semantics. |
| Corruption/integrity detection | SUPPORTED_WITH_DESIGN_CONSTRAINT | Native consistency scan verifies replicas; application transition-chain integrity still required. |
| Exact operation-history recovery | SUPPORTED_WITH_DESIGN_CONSTRAINT | Immutable event/history keys must be stored explicitly; native MVCC history alone must not be the only retention basis. |
| Retention/GC feasibility | SUPPORTED_WITH_DESIGN_CONSTRAINT | Persistent keys can preserve evidence; application must own GC horizon. |
| Backup/restore implications | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Consistent point-in-time backup and DR are documented; restore requires new ledger/fence epoch reconciliation. |
| Observability/readback | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Machine-readable status and transactional reads are documented. |
| Deterministic test harness suitability | NEEDS_EMPIRICAL_PROOF | Candidate-specific harness must verify our exact ledger protocol and selected redundancy mode. |

### Deployment/configuration dependencies

Single mode:
- explicitly not fault tolerant;
- suitable only as a test/development topology for our host-failure requirement.

Replicated modes:
- double/triple/data-hall modes provide different progress/failure envelopes;
- coordinator layout matters;
- exact selected redundancy topology must be pinned before any availability/durability claim.

### Current disqualifiers

None proven for a properly replicated deployment.

A FoundationDB deployment becomes DISQUALIFIED if:
- deployed in a topology whose documented redundancy cannot satisfy the claimed host-failure model;
- conflict ranges are weakened/omitted so uniqueness/fence predicates are not protected;
- application relies on compactable/native historical versions instead of explicit retained ledger evidence.

### Empirical proofs still required

- concurrent uniqueness sentinel race;
- fence rollover with stale client;
- commit-unknown-result handling;
- host/process crash after commit;
- power loss/storage fault injection;
- consistency-scan/corruption reaction;
- partition/redundancy loss;
- restore/DR and successor-fence behavior;
- exact operation-history persistence independent of MVCC cleanup.

## 6. Candidate C — etcd 3.7

### Official technical source locators

- v3.7 docs:
  https://etcd.io/docs/v3.7/
- API / atomic transaction / linearizable Range:
  https://etcd.io/docs/v3.7/learning/api/
- Data model / MVCC revisions:
  https://etcd.io/docs/v3.7/learning/data_model/
- Client design:
  https://etcd.io/docs/v3.7/learning/design-client/
- Disaster recovery:
  https://etcd.io/docs/v3.7/op-guide/recovery/
- Data corruption:
  https://etcd.io/docs/v3.7/op-guide/data_corruption/
- API reference / HashKV:
  https://etcd.io/docs/v3.7/dev-guide/api_reference_v3/
- Versioning:
  https://etcd.io/docs/v3.7/op-guide/versioning/

### Documentary capability summary

etcd 3.7 documents atomic multi-operation transactions guarded by comparisons, cluster revisions, linearizable Range reads by default, MVCC history, Raft-based cluster operation, snapshot/restore and corruption checking.

Its transaction primitive maps naturally to conditional multi-key reservation and fence/revision checks, but ledger retention must not rely on compactable MVCC history.

### Requirement matrix

| Requirement | Status | Basis / constraint |
|---|---|---|
| Multi-key atomic reservation | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Txn atomically evaluates comparisons and applies multiple operations at one revision. |
| Uniqueness under concurrency | SUPPORTED_WITH_DESIGN_CONSTRAINT | Absence/version comparisons plus transaction write set can implement reservation uniqueness. |
| Revision/state CAS equivalent | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Compare can test value/version/mod_revision. |
| Process fencing equivalent | SUPPORTED_WITH_DESIGN_CONSTRAINT | Fence key/version must be compared in every protected Txn. |
| Durable commit | NEEDS_EMPIRICAL_PROOF | Raft/WAL durability is product architecture, but exact deployment/storage boundary must be fault-tested for STP-C. |
| Process crash recovery | SUPPORTED_WITH_DESIGN_CONSTRAINT | Client/cluster fault handling documented; exact application continuation remains protocol-specific. |
| Host crash/restart | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Disaster-recovery docs state temporary machine failures are automatically recovered in a healthy quorum cluster. |
| Power-loss boundary | NEEDS_EMPIRICAL_PROOF | Exact disk/fsync/controller behavior of selected nodes must be tested. |
| Torn/partial-write handling | NEEDS_EMPIRICAL_PROOF | WAL/backend plus corruption detection exist, but exact injected-fault outcome must be observed. |
| Cross-process visibility | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Linearizable KV operations provide current consensus view by default. |
| Partition/unavailability semantics | SUPPORTED_WITH_DESIGN_CONSTRAINT | Loss of quorum blocks updates; authority reads must remain linearizable, not local serializable/stale reads. |
| Authoritative absence | SUPPORTED_WITH_DESIGN_CONSTRAINT | Linearizable Range can provide current consensus absence; serializable local reads must be forbidden for this purpose. |
| Corruption/integrity detection | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Initial/periodic corruption checks and HashKV are documented. |
| Exact operation-history recovery | SUPPORTED_WITH_DESIGN_CONSTRAINT | Explicit immutable history keys required; compaction can remove old MVCC revisions. |
| Retention/GC feasibility | SUPPORTED_WITH_DESIGN_CONSTRAINT | Ledger evidence must be explicit keys with separate GC policy; native revision compaction is not sufficient retention. |
| Backup/restore implications | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Snapshot/restore documented; revision/cluster identity effects require application reconciliation. |
| Observability/readback | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Response headers expose cluster/member/revision/raft_term; maintenance/status APIs exist. |
| Deterministic test harness suitability | NEEDS_EMPIRICAL_PROOF | Must verify our exact Txn/fence/history schema under leader loss, partition and restart. |

### Deployment/configuration dependencies

Single-member:
- technically supported for local use;
- does not satisfy replicated host-failure availability.

Replicated:
- quorum availability is fundamental;
- authority-bearing read must use linearizable Range;
- local serializable read trades correctness/currentness for availability and is therefore not admissible for authoritative absence.

### Current disqualifiers

None proven for a quorum-based deployment using linearizable authority reads.

An etcd deployment becomes DISQUALIFIED if:
- authority-bearing absence uses serializable member-local reads;
- ledger history depends solely on MVCC versions that later compaction removes;
- quorum/partition errors are translated into absence;
- fence key is not atomically compared with every protected transition.

### Empirical proofs still required

- atomic multi-key reservation at configured transaction limits;
- same-ID and effect-claim races;
- stale fence after leadership/process changes;
- quorum loss and recovery;
- lost response around committed Txn;
- power loss/restart;
- corruption alarm behavior;
- snapshot restore and ledger revision/fence reconciliation;
- explicit-history retention independent of compaction.

## 7. Candidate D — CockroachDB v26.1 / current stable documentation line

### Official technical source locators

- Current stable developer transaction documentation:
  https://www.cockroachlabs.com/docs/stable/developer-basics.html
- Current stable backup/restore monitoring:
  https://www.cockroachlabs.com/docs/stable/backup-and-restore-monitoring
- v26.1 release identification:
  https://www.cockroachlabs.com/blog/cockroachdb-v26-1-security-and-compliance/

Official technical documentation states that CockroachDB transactions are atomic and SERIALIZABLE by default and records are replicated across distributed database instances.

Where this discovery did not find a current primary technical page precise enough for a required property, the status remains NEEDS_EMPIRICAL_PROOF or UNKNOWN rather than being promoted from older marketing/blog material.

### Requirement matrix

| Requirement | Status | Basis / constraint |
|---|---|---|
| Multi-key atomic reservation | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Atomic SQL transactions can mutate multiple rows/tables as one transaction. |
| Uniqueness under concurrency | SUPPORTED_WITH_DESIGN_CONSTRAINT | SQL unique/primary-key constraints are plausible, but exact ledger collision behavior must be harness-tested. |
| Revision/state CAS equivalent | SUPPORTED_WITH_DESIGN_CONSTRAINT | Conditional transaction on expected revision/fence is implementable; exact retry semantics must be controlled. |
| Process fencing equivalent | SUPPORTED_WITH_DESIGN_CONSTRAINT | Fence stored in ledger rows and atomically checked; not a native STP-C concept. |
| Durable commit | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | Stable docs state committed transactions are ACID and data are replicated; exact deployment persistence still needs empirical proof. |
| Process crash recovery | SUPPORTED_WITH_DESIGN_CONSTRAINT | Distributed DB transaction recovery exists; application recovery path must be tested. |
| Host crash/restart | SUPPORTED_WITH_DESIGN_CONSTRAINT | Replication architecture is intended for node failures; selected node/replica topology must be proven. |
| Power-loss boundary | NEEDS_EMPIRICAL_PROOF | Exact self-hosted storage and quorum persistence must be fault-tested. |
| Torn/partial-write handling | NEEDS_EMPIRICAL_PROOF | No current official locator was found in this bounded pass that alone proves our exact torn-write requirement. |
| Cross-process visibility | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SERIALIZABLE transactional semantics are documented. |
| Partition/unavailability semantics | NEEDS_EMPIRICAL_PROOF | Exact selected topology/quorum/client behavior must be observed. |
| Authoritative absence | SUPPORTED_WITH_DESIGN_CONSTRAINT | Must use current SERIALIZABLE transaction path; follower/stale-read features, if enabled, cannot be used for authority-bearing absence. |
| Corruption/integrity detection | UNKNOWN | Bounded current-source pass did not establish a current official technical guarantee sufficient for our semantic corruption requirement. Application integrity chain can help, but product-level evidence remains open. |
| Exact operation-history recovery | SUPPORTED_WITH_DESIGN_CONSTRAINT | Requires explicit immutable ledger/history schema. |
| Retention/GC feasibility | SUPPORTED_WITH_DESIGN_CONSTRAINT | SQL tables can retain evidence; exact GC policy/application history model required. |
| Backup/restore implications | SUPPORTED_WITH_DESIGN_CONSTRAINT | Current stable docs expose backup/restore operations/monitoring; restored state must trigger new fence/currentness reconciliation. |
| Observability/readback | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SQL queries and operational monitoring exist. |
| Deterministic test harness suitability | NEEDS_EMPIRICAL_PROOF | Distributed transaction retries/failures need explicit deterministic test oracle. |

### Deployment/configuration dependencies

Replicated deployment is the normal technical class for this candidate.

The exact number/location of nodes, replica placement, storage durability and retry policy materially change the claimable failure envelope.

A single-node development deployment cannot be treated as proof of replicated host-failure behavior.

### Current disqualifiers

None proven yet, but one mandatory area remains UNKNOWN:

corruption/integrity product-level behavior sufficient for STP-C.

This UNKNOWN does not become PASS.

It must be resolved in the bounded proof/research gate before CockroachDB can be admitted to an OPERATOR product-decision gate.

### Empirical/documentary proofs still required

- current official corruption/integrity detection semantics for the selected version;
- exact power-loss durability;
- partition/quorum behavior;
- transaction retry/collision handling in ledger schema;
- stale process/fence rollover;
- lost-response idempotent resolution;
- restore and post-restore fencing;
- exact operation-history preservation.

## 8. Cross-candidate comparison matrix

| Requirement | PostgreSQL 18 | FoundationDB 7.4.8 | etcd 3.7 | CockroachDB v26.1/stable |
|---|---|---|---|---|
| Multi-key atomic reservation | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_BY_DOCUMENTED_PRIMITIVE |
| Uniqueness concurrency | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT |
| Revision/CAS | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_WITH_DESIGN_CONSTRAINT |
| Process fencing | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT |
| Durable commit | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | NEEDS_EMPIRICAL_PROOF | SUPPORTED_BY_DOCUMENTED_PRIMITIVE |
| Crash/restart | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_WITH_DESIGN_CONSTRAINT |
| Power loss | NEEDS_EMPIRICAL_PROOF | NEEDS_EMPIRICAL_PROOF | NEEDS_EMPIRICAL_PROOF | NEEDS_EMPIRICAL_PROOF |
| Torn/partial write | SUPPORTED_WITH_DESIGN_CONSTRAINT | NEEDS_EMPIRICAL_PROOF | NEEDS_EMPIRICAL_PROOF | NEEDS_EMPIRICAL_PROOF |
| Cross-process visibility | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_BY_DOCUMENTED_PRIMITIVE |
| Partition/unavailability | NEEDS_EMPIRICAL_PROOF | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | NEEDS_EMPIRICAL_PROOF |
| Authoritative absence | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT |
| Corruption/integrity | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | UNKNOWN |
| Exact operation history | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT |
| Retention/GC | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_WITH_DESIGN_CONSTRAINT |
| Backup/restore | SUPPORTED_WITH_DESIGN_CONSTRAINT | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_WITH_DESIGN_CONSTRAINT |
| Observability/readback | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_BY_DOCUMENTED_PRIMITIVE | SUPPORTED_BY_DOCUMENTED_PRIMITIVE |
| Deterministic harness | NEEDS_EMPIRICAL_PROOF | NEEDS_EMPIRICAL_PROOF | NEEDS_EMPIRICAL_PROOF | NEEDS_EMPIRICAL_PROOF |

## 9. Shared design constraints for all surviving candidates

Regardless of product:

1. Ledger history must be explicit application evidence, not inferred from transient logs or process memory.
2. process_fence must be checked in the same atomic transition that publishes protected state.
3. Restoring an older backup/snapshot is a currentness/fence event, not transparent continuation.
4. A restored backend must not let pre-restore stale processes publish late state.
5. Unavailable/partitioned cannot mean NOT_APPLIED.
6. Exact absence requires an authoritative/current read.
7. A backend replica/read mode that can be stale is diagnostic only for authority-bearing decisions.
8. External irreversible effect remains outside backend atomicity.

## 10. Downstream effect boundary

All surviving candidates can plausibly store:

- external idempotency key;
- unique effect claim;
- PRE_EFFECT/currentness evidence identity;
- invocation identity;
- authenticated downstream receipt/query evidence;
- OUTCOME_UNKNOWN;
- reconciliation state.

None of these backend candidates, by itself, proves:

- downstream idempotency-key semantics;
- authenticated downstream query;
- authenticated receipt;
- authenticated NOT_APPLIED;
- external exactly-once execution;
- atomicity between the ledger and arbitrary external service.

Therefore the following remains mandatory and separate:

- downstream idempotency key OR independently proven exactly-once protocol;
- authenticated exact-operation query;
- authenticated receipt;
- authenticated absence/non-execution evidence where possible;
- no blind retry from uncertain outcome;
- last-enforceable PRE_EFFECT/currentness fence.

## 11. Obvious classes excluded before surviving set

The following generic classes were not advanced because, absent additional transactional/fencing layers, they directly violate mandatory requirements:

### Plain files / append-only text logs without transactional index layer

Reason:
cannot by themselves prove atomic multi-key reservation, uniqueness races, current authoritative absence and fenced transitions.

Status:
DISQUALIFIED as standalone ledger backend.

### Last-write-wins stores without conflict detection

Reason:
explicit requirements-profile disqualifier.

Status:
DISQUALIFIED.

### Per-process-only in-memory stores/locks

Reason:
cannot provide cross-process crash durability/history/fencing.

Status:
DISQUALIFIED.

### Eventually consistent replica read used as authority

Reason:
cannot prove authoritative absence or current fence/revision.

Status:
DISQUALIFIED for authority-bearing read path.

This does not disqualify a product that also provides a separately proven strong/current transaction path; it disqualifies the stale path for this use.

## 12. Operational consequences without ranking

### PostgreSQL 18

Single-host consequence:
fewer distributed failure modes, but host/storage availability and correct durable settings become central.

Replicated consequence:
primary/standby routing and synchronous-vs-asynchronous semantics must be explicit; stale standby reads cannot prove absence.

### FoundationDB 7.4.8

Consequence:
ledger uniqueness/fencing/history is more application-key-model dependent.
Replicated topology and coordinators are part of correctness/availability evidence, not merely operations.

### etcd 3.7

Consequence:
transaction/CAS primitives map closely to reservation/fencing, but transaction-size limits, compaction and quorum availability must be incorporated into design.
Linearizable vs serializable local reads is a security-relevant configuration distinction.

### CockroachDB v26.1/stable

Consequence:
SQL/distributed transactions are a plausible fit, but the bounded source pass left corruption/integrity proof UNKNOWN and distributed fault behavior must be empirically pinned for the selected topology.

No consequence above is an overall ranking.

## 13. Bounded empirical proof gate

Documentary evidence is not sufficient for final OPERATOR backend selection because deployment-specific mandatory claims remain unproven.

Required non-production proof should run the same backend-neutral harness against each candidate that remains in scope.

Minimum proof set:

P01 atomic multi-key reservation;
P02 uniqueness race;
P03 state_revision CAS conflict;
P04 stale process_fence rejection;
P05 acknowledged commit + process crash;
P06 acknowledged commit + host restart;
P07 injected power-loss boundary where safely testable;
P08 torn/partial/corruption detection;
P09 partition/unavailability does not become absence;
P10 authoritative absence from permitted read path;
P11 lost response after commit;
P12 concurrent transition race;
P13 effect-claim race;
P14 backup/snapshot restore + new fence/currentness epoch;
P15 exact operation-history readback after restart/restore;
P16 retention/GC preserves replay/collision/uncertain-effect evidence.

For distributed candidates:
also prove loss of leader/member/quorum behavior and stale-node response handling.

For PostgreSQL replicated candidate:
also prove primary/standby failover and prohibition of authority-bearing reads from lagging standby.

For CockroachDB:
first close the current documentary UNKNOWN on corruption/integrity or demonstrate an independently testable fail-closed integrity layer sufficient to meet the exact requirement.

## 14. Gate decision

Surviving candidate count:
4

Final product selection:
NOT_AUTHORIZED
NOT_PERFORMED

Ranking/scoring:
NOT_PERFORMED

Documentary comparison is sufficient to justify bounded non-production empirical proof.

It is NOT sufficient to justify a final OPERATOR product decision yet because:
- all candidates have mandatory deployment-specific fault guarantees still requiring empirical proof;
- CockroachDB additionally has one documentary UNKNOWN in corruption/integrity in this bounded pass.

Gate:

READY_FOR_BOUNDED_EMPIRICAL_BACKEND_PROOF

## 15. Boundary preservation

No:
- backend installation;
- live storage;
- host mutation;
- deployment;
- keys/secrets/credentials;
- production testing;
- live WRITE/CAS;
- CHECKPOINT_DURABLE;
- Fast Gate/profile activation;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

## EXPERIENCE

Идея → не выбирать базу по привычке, а заставить кандидатов пройти один и тот же профиль отказов и наблюдаемых гарантий.

Проба → сопоставить четыре технически правдоподобных продукта с exact mandatory matrix и отделить documented primitive от deployment guarantee.

Результат → четыре кандидата пережили documentary screening, но ни один ещё не получил право называться доказанным backend проекта.

Успех → следующий gate определён однозначно: bounded empirical proof, не продуктовый выбор.

Урок → документация хорошо отвечает на вопрос "что система умеет". Вопрос "что останется именно в нашей конфигурации после падения питания, разделения сети и опоздавшего старого процесса" всё равно приходится задавать машине лично.

## Terminal

PASS_SIS_STP_C_LEDGER_BACKEND_CANDIDATE_COMPARISON_R01_READY_FOR_DECISION_OR_PROOF

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
