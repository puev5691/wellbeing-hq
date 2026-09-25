# SIS → KOO: S1+O2 F2 capability evidence discovery r0.1

terminal: PASS_SIS_S1O2_F2_CAPABILITY_EVIDENCE_DISCOVERY_R01_DOCUMENT_ONLY
scope: SINGLE_BOUNDED_DOCUMENTARY_DISCOVERY
project_time: omitted

governance_candidate: CANDIDATE_NOT_ACTIVE
CHECKPOINT_DURABLE: NOT_ESTABLISHED
resume_authority: NOT_GRANTED
operational_owner: NOT_APPOINTED
memory_layering_attempt_3: NOT_AUTHORIZED

## Человеческий смысл

Для F2 найдено три полезных класса документированных storage capability. Это не выбор продукта и не доказательство, что любой из них уже доступен проекту.

Наиболее полный по форме F2 интерфейс из просмотренных публичных документов показывает consensus transactional KV class: документированы durable completed operations, strict serializability, atomic compare/transaction semantics, quorum-based progress and safe stop on majority loss.

Synchronous replicated SQL class документирует transaction commit, synchronous standby acknowledgement and quorum-style standby selection. Но built-in PostgreSQL не решает сам fencing/failover orchestration: официальная документация прямо требует отдельный механизм, чтобы старый primary не стал вторым primary. Значит F2 composition остаётся неполной без independently verified failover/fence layer.

Replicated distributed object storage class документирует failure-domain placement, persistence of acknowledged writes across the PG Acting Set and atomic operations on one object. Это сильная object-plane база. Но проектный S1 требует ещё exact current-pointer/CAS, operation-qualified PUT/CAS journal, dedupe/fence lineage and lost-ack proof. Публичные Ceph interfaces не доказывают эту полную composition автоматически.

Ни один класс нельзя повысить до PROJECT_DEPLOYMENT_VERIFIED. Для проекта всё это пока DOCUMENTED_INTERFACE_CAPABILITY / PROPOSED / UNKNOWN.

## Resume-First / authority

Exact task:
puev5691/wellbeing-hq@4b86fb002d5aa1024bbe2f63948d2def25f92492:
entities/koordinator/outbox/KOO__shard-checkpoint-s1o2-f2-capability-evidence-discovery-r01__SIS.md
blob:
192b5e1b72ea54873139e27e9d27a15e047de7d8

Authority:
AUTHORIZE_SIS_S1O2_F2_CAPABILITY_EVIDENCE_DISCOVERY_R01_DOCUMENT_ONLY

Fresh HQ HEAD before discovery:
4b86fb002d5aa1024bbe2f63948d2def25f92492

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

No newer competing SIS writer, superseding exact task, or competing discovery terminal was found at execution boundary.

Approved Sources verified by exact Git blobs:
- core v2.5: a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- roles v2.4: 1772339cb74dae8550bfbd2e33401c34a929e911
- recovery v1.6: 233117e1c9509d730e1f5ec532b1cabe3f786609
- file-work v2.4: e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- source-loading v2.2: 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- task-conveyor v1.2: df7896d867eeeffff506319538fedad938856686

Historical PROMPT replay: 0.

## Exact project evidence baseline

F2 decision:
puev5691/wellbeing-hq@8dc6da614f75ea9c3a3e322b6c5a5168acfea050:
entities/koordinator/outbox/KOO__s1o2-f2-failure-objective-decision-r01__OPERATOR.md
blob:
8115ed76e0c8953e80426f89a7d52747e1763bf7

SIS F2 fit-gap:
puev5691/wellbeing-hq@f336c4c5b51467d1df833ffca211a6315c34991a:
entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-f2-capability-fitgap-r01__KOO.md
blob:
5152869bb139e26c98962af523b90cd13cb0b37f

Prior durability models:
puev5691/wellbeing-hq@8cda2ace78d6e27d4d9ada3344d5e2f3af6ca274:
entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-storage-durability-options-r01__KOO.md
blob:
3641bce5e40d73677f22e48903e8c6b72b709d08

KOD operation-specific interface:
puev5691/wellbeing-hq@ea632cd672994fc7ce6356d77a9fcb7c56854702:
entities/koder/outbox/KOD__shard-checkpoint-s1o2-operation-dedupe-correction-r01.md
blob:
085d13164487b18569b28d1ab6a589b63d0a4118

Governance successor:
blob:
799be4e536a2795fae19b489b9887570d614a52a
status:
CANDIDATE_NOT_ACTIVE

## Status labels

DOCUMENTED_INTERFACE_CAPABILITY:
public first-party documentation describes a mechanism relevant to F2.

PROJECT_DEPLOYMENT_VERIFIED:
exact capability has been independently demonstrated in project deployment.

PROPOSED:
composition appears technically plausible from documented interfaces but has not been implemented/proven.

UNKNOWN:
evidence is absent or insufficient.

BLOCKED_FOR_F2:
the described composition cannot satisfy F2 without changing the model.

## Class selection rationale

Three classes were selected because they exercise materially different F2 designs:

C1:
consensus transactional KV / replicated state-machine class.
Reference implementation documentation: etcd v3.7.

C2:
synchronous replicated transactional SQL class.
Reference implementation documentation: PostgreSQL 18.

C3:
replicated distributed object store with explicit failure-domain placement and object-local atomic operations.
Reference implementation documentation: Ceph Squid.

These are capability exemplars only. They are not recommendations, backend selections or evidence of installed project software.

## External first-party sources

### etcd v3.7

1. etcd v3.7 API guarantees
https://etcd.io/docs/v3.7/learning/api_guarantees/

Documented:
- completed KV operations are durable;
- KV operations are strictly serializable;
- API requests are atomic;
- linearizable operations use Raft consensus.

2. etcd v3.7 API
https://etcd.io/docs/v3.7/learning/api/

Documented:
- Txn is atomic If/Then/Else;
- comparisons can be against key version/revision/value;
- transactions can implement compare-and-swap;
- multiple KV modifications can be processed atomically.

3. etcd v3.7 Failure modes
https://etcd.io/docs/v3.7/op-guide/failures/

Documented:
- committed writes are not lost on leader failover;
- majority loss stops the cluster from accepting writes;
- writes not committed before failure may remain uncertain/lost.

### PostgreSQL 18

1. PostgreSQL 18 Replication configuration
https://www.postgresql.org/docs/18/runtime-config-replication.html

Documented:
- synchronous_standby_names controls synchronous replication;
- commits proceed after required synchronous standby replies;
- FIRST and ANY forms support priority/quorum-style synchronous standby selection;
- synchronous replication can wait for WAL to be replicated to multiple standbys.

2. PostgreSQL 18 warm-standby / synchronous replication
https://www.postgresql.org/docs/18/warm-standby.html

Documented:
- synchronous_commit=on waits for standby durable storage confirmation;
- remote_apply can wait for replay/visibility.

3. PostgreSQL 18 Failover
https://www.postgresql.org/docs/18/warm-standby-failover.html

Documented:
- old primary must be fenced/informed after promotion to avoid two primaries and data loss;
- PostgreSQL does not itself provide the external failover-detection/orchestration software.

4. PostgreSQL 18 transaction model
https://www.postgresql.org/docs/18/sql-begin.html
https://www.postgresql.org/docs/18/sql-update.html

Documented:
- multiple changes can be grouped into one transaction;
- conditional UPDATE can restrict mutation to matching rows.

### Ceph Squid

1. Ceph Squid CRUSH Maps
https://docs.ceph.com/en/squid/rados/operations/crush-map/

Documented:
- CRUSH hierarchy models host/rack/datacenter and other failure domains;
- replicas can be placed across chosen failure domains.

2. Ceph Squid Monitoring OSDs and PGs
https://docs.ceph.com/en/squid/rados/operations/monitoring-osd-pg/

Documented:
- Ceph does not acknowledge a write until it is persisted by every OSD in the Acting Set;
- PG peering reconstructs an authoritative history from acknowledged operations;
- degraded/failed OSD conditions affect service/recovery behavior.

3. Ceph Squid librados C API
https://docs.ceph.com/en/squid/rados/api/librados/

Documented:
- multiple operations on one object can execute atomically;
- object version assertions and compare operations are available;
- compare-xattr / compare-extent can fail an object write operation if condition is not met.

## C1 — consensus transactional KV class

Reference:
etcd v3.7.

### Failure-domain independence

DOCUMENTED_INTERFACE_CAPABILITY:
cluster consensus/quorum and failure behavior exist.

PROJECT_DEPLOYMENT_VERIFIED:
NO.

UNKNOWN:
whether project deployment would place members in independently verified F2 domains.

Required project evidence:
- exact member/domain mapping;
- common power/network/storage/controller dependency analysis;
- administrative identity/ACL mapping;
- independently reviewed domain-separation evidence.

### Synchronous acknowledged survival

DOCUMENTED_INTERFACE_CAPABILITY:
completed KV operations are documented durable; consensus/majority controls commit; committed writes are documented not lost on leader failure.

This is a strong abstract match to M2.

UNKNOWN:
whether an exact deployment survives total loss of the OPERATOR-selected failure domain.

Required evidence:
- domain loss leaves quorum containing committed entry;
- storage persistence on surviving members;
- operation ack emitted only after the relevant Raft commit/persistence guarantee;
- all S1-critical state stored in the same qualifying durability class.

### Object + pointer/CAS + operation lineage

DOCUMENTED_INTERFACE_CAPABILITY:
Txn comparisons/atomic request groups can implement compare-and-swap and atomically update multiple keys.

PROPOSED mapping:
- immutable object key;
- current pointer key;
- PUT/CAS result journal keys;
- dedupe/fence lineage keys.

UNKNOWN:
exact S1 key layout and whether object bytes should reside in this class or a separate object plane.

### Lost ack

DOCUMENTED_INTERFACE_CAPABILITY:
client can be uncertain if operation times out/network fails; completed operations have durable state.

PROPOSED:
operation-specific request record plus linearizable read can resolve persisted outcome.

UNKNOWN:
project's exact durable negative-proof contract and request-id retention.

### Readback after one domain loss

DOCUMENTED_INTERFACE_CAPABILITY:
linearizable reads and durable accessible data are documented.

UNKNOWN:
independent project reader path and surviving-domain deployment.

### Partition behavior

DOCUMENTED_INTERFACE_CAPABILITY:
loss of majority stops writes; consensus safety is preferred over continuing arbitrary writes.

This aligns well with F2 STOP semantics.

### Backup / restore / retention

DOCUMENTED_INTERFACE_CAPABILITY:
etcd has disaster-recovery/snapshot mechanisms, but these were not examined here as F2 proof.

UNKNOWN:
project backup/restore/retention composition for S1.

### C1 F2 documentary disposition

DOCUMENTED_INTERFACE_CAPABILITY:
STRONG_F2_RELEVANCE.

PROJECT_DEPLOYMENT_VERIFIED:
NO.

Remaining blocker:
no project topology, domain-independence proof, S1 composition or runtime evidence.

## C2 — synchronous replicated transactional SQL class

Reference:
PostgreSQL 18.

### Failure-domain independence

DOCUMENTED_INTERFACE_CAPABILITY:
multiple synchronous standbys can be configured; ANY/FIRST can require replies from multiple standbys.

UNKNOWN:
whether standbys occupy independent F2 failure domains.

Required evidence:
- physical/common-mode mapping;
- storage durability of each synchronous participant;
- administrative separation where required.

### Synchronous acknowledged survival

DOCUMENTED_INTERFACE_CAPABILITY:
with synchronous replication, commits can wait for required standby confirmation; documentation distinguishes durable standby flush from weaker remote_write semantics.

Potential F2 mapping:
store object/pointer/outcome/fence rows in one SQL transaction whose WAL commit receives the selected synchronous durability.

UNKNOWN:
exact configuration and whether chosen failover process preserves the F2 no-loss acknowledgement promise.

### Atomic object + pointer/CAS + journal

DOCUMENTED_INTERFACE_CAPABILITY:
SQL transactions can group related changes.

PROPOSED:
one transaction can conditionally update pointer row while recording operation result/dedupe/fence journal and immutable-object metadata/blob.

UNKNOWN:
exact S1 schema, isolation/concurrency policy, payload size/model and conditional-update design.

### Lost ack

PROPOSED:
operation journal keyed by operation-qualified request IDs can resolve post-timeout outcome.

DOCUMENTED_INTERFACE_CAPABILITY:
transactional commit state exists.

UNKNOWN:
authoritative negative-proof semantics and project read path after failover.

### Partition / stale primary

CRITICAL GAP.

DOCUMENTED_INTERFACE_CAPABILITY:
official PostgreSQL failover docs explicitly require a mechanism to ensure an old primary cannot reappear as another primary; PostgreSQL itself does not provide the complete external failover orchestration.

Therefore:
a PostgreSQL-like SQL class alone is not a complete F2 control-plane design.

Required independent evidence:
- externally verified fencing/STONITH or equivalent;
- promotion authority;
- split-brain prevention;
- failover process preserving synchronous-commit guarantees;
- stale writer cannot accept S1 CAS.

### Readback after one domain loss

DOCUMENTED_INTERFACE_CAPABILITY:
standby can be queryable/promoted depending configuration.

UNKNOWN:
which surviving node is authoritative and independently read under the project's failover/fence contract.

### Backup / restore / retention

DOCUMENTED_INTERFACE_CAPABILITY:
PostgreSQL has backup/WAL recovery facilities generally, but they are not F2 proof.

UNKNOWN:
S1 backup/isolated restore/lineage retention.

### C2 F2 documentary disposition

DOCUMENTED_INTERFACE_CAPABILITY:
F2_RELEVANT_SYNC_COMMIT_AND_TRANSACTION_CLASS.

PROJECT_DEPLOYMENT_VERIFIED:
NO.

Major blocker:
external failover/fencing composition is required and unproven.

## C3 — replicated distributed object storage class

Reference:
Ceph Squid RADOS/librados.

### Failure-domain independence

DOCUMENTED_INTERFACE_CAPABILITY:
CRUSH can explicitly place replicas across host/rack/datacenter-style failure domains.

This is unusually relevant to F2 because failure-domain placement is a first-class documented construct.

UNKNOWN:
whether proposed project domains are physically/administratively independent in reality.

Required evidence:
- exact CRUSH/failure-domain map or equivalent;
- common-mode dependency review;
- proof selected domain loss leaves required Acting Set/replica state.

### Synchronous acknowledged object survival

DOCUMENTED_INTERFACE_CAPABILITY:
Ceph Squid docs state that a client write is not acknowledged until persisted by every OSD in the Acting Set.

This is strong evidence for an object-plane F2-capable pattern if the Acting Set spans independently verified domains.

PROJECT_DEPLOYMENT_VERIFIED:
NO.

### CAS / current pointer

DOCUMENTED_INTERFACE_CAPABILITY:
librados supports atomic multi-action operations on one object, object-version assertion and compare operations.

PROPOSED:
model current pointer and its CAS fields as one control object with compare/assert + atomic update.

UNKNOWN:
whether this exact mapping satisfies the full KOD expected tuple and whether pointer/journal need multiple objects.

### Cross-object atomicity

UNKNOWN / POTENTIAL BLOCKER.

First-party docs reviewed here establish atomicity for a single RADOS object, not a general atomic transaction spanning arbitrary separate objects.

Therefore:
if immutable checkpoint object, pointer, PUT outcome, CAS outcome and fence journal require an all-or-nothing cross-object transaction, this capability is NOT established.

The current KOD model does not require PUT object creation and pointer CAS to be one transaction, but it does require exact per-operation durable reconciliation. That makes a composition possible in principle, not proven.

### Operation journal / dedupe / fence lineage

PROPOSED:
store operation journal as dedicated object(s), omap/xattr or separate control objects.

DOCUMENTED_INTERFACE_CAPABILITY:
object-local atomic metadata compare/update primitives exist.

UNKNOWN:
exact journal schema, retention, cross-object consistency and durable negative proof.

### Lost ack

PROPOSED:
read exact operation journal/object/pointer separately.

UNKNOWN:
whether the required negative proof and request-id lookup are supported by the designed object layout.

### Partition behavior

DOCUMENTED_INTERFACE_CAPABILITY:
Ceph PGs require peering/acting-set state and may degrade/recover; writes depend on PG state and replication policy.

UNKNOWN:
exact S1 STOP semantics under chosen failure-domain/partition conditions and whether a control-object CAS can remain uniquely authoritative.

### Independent post-loss readback

DOCUMENTED_INTERFACE_CAPABILITY:
objects can be read from the cluster; replicated placement/authoritative PG history exists.

UNKNOWN:
independent verifier principal/path and exact object+pointer post-domain-loss procedure.

### Backup / isolated restore / retention

UNKNOWN for S1 composition.

Ceph replication is not treated as backup here.
Project still needs isolated backup/restore and retention of operation/fence/dependency lineage.

### C3 F2 documentary disposition

DOCUMENTED_INTERFACE_CAPABILITY:
STRONG_OBJECT_PLANE_F2_RELEVANCE.

PROJECT_DEPLOYMENT_VERIFIED:
NO.

Major gap:
full S1 control-plane and operation-journal composition, especially cross-object consistency and lost-ack negative proof, is unproven.

## Compact comparison

| F2 dimension | C1 consensus KV | C2 sync SQL | C3 replicated object store |
|---|---|---|---|
| Explicit consensus/quorum safety | DOCUMENTED | PARTIAL via sync standby; failover external | PG/peering model documented |
| Atomic CAS primitive | DOCUMENTED Txn compare | PROPOSED via transactional conditional row update | DOCUMENTED per-object compare/assert |
| Multi-key/record atomicity | DOCUMENTED Txn | DOCUMENTED SQL transaction | UNKNOWN beyond one object |
| Sync durability before positive ack | DOCUMENTED completed/durable consensus op | DOCUMENTED configurable sync commit | DOCUMENTED persisted Acting Set write |
| Explicit failure-domain placement | Deployment concern, not API guarantee | Deployment concern | DOCUMENTED CRUSH failure-domain model |
| One-domain-loss F2 project proof | UNKNOWN | UNKNOWN | UNKNOWN |
| Safe stop when consensus insufficient | DOCUMENTED majority-loss stop | Requires external failover/fence design | Depends on PG/cluster state; S1 mapping UNKNOWN |
| Stale writer fencing | Consensus leader/state-machine semantics help; S1 writer mapping PROPOSED | External STONITH/fence required | S1 epoch/fence mapping PROPOSED |
| Lost-ack journal | PROPOSED on linearizable KV | PROPOSED transaction table | PROPOSED object/control journal |
| Independent object/pointer readback | PROPOSED/project-specific | PROPOSED/project-specific | PROPOSED/project-specific |
| Backup alone meets F2 | NO | NO | NO |
| PROJECT_DEPLOYMENT_VERIFIED | NO | NO | NO |

## Relation to M1/M2/M3

M1:
remains BLOCKED_FOR_F2_AS_DEFINED regardless of these products if only one durability domain participates in acknowledgement.

M2:
C1 and C2 are direct examples of synchronous replicated state patterns.
C3 also documents replicated acknowledgement across an Acting Set and may instantiate M2 for object/control objects if exact failure-domain and control semantics are proven.

M3:
C3 is a natural object-plane exemplar; C1 or C2 could serve as a separate transactional control plane.
This composition is only PROPOSED.
No cross-product composition is selected or proven.

## Physical failure-domain proof still required

Public docs cannot prove project deployment separation.

Minimum future evidence:
- exact topology inventory;
- storage devices/controllers;
- hosts/hypervisors;
- power dependencies;
- rack/site/network dependencies where selected;
- shared control-plane services;
- common storage/SAN/cloud dependency if any;
- mapping of each F2-critical state class to surviving domains.

Status:
UNKNOWN.

## Administrative independence proof still required

Need OPERATOR/D1 decision whether administrative independence is part of F2 trust profile.

If yes, future evidence must include:
- service principals;
- ACLs;
- deployment/config write authority;
- ack issuer identity;
- independent reader/verifier identity;
- whether one credential/admin domain can fabricate or destroy all copies/evidence.

Status:
UNKNOWN / POLICY_DECISION_REQUIRED.

## What public documentation does NOT prove

No public vendor documentation proves:
- the project actually runs that product;
- exact project version/configuration;
- project failure-domain independence;
- project service-account separation;
- project S1 schema integration;
- project PUT/CAS/dedupe/fence journal layout;
- retention/RPO/RTO;
- successful one-domain-loss test;
- D1–D9 PASS;
- CHECKPOINT_DURABLE.

All remain UNKNOWN/BLOCKED until project-specific evidence exists.

## First independently checkable next evidence

Before any runtime test, the smallest useful non-live evidence step is:

**exact deployment-capability inventory for candidate classes already available to the project environment, without mutation**.

It should establish, for each candidate class:
- whether binaries/services/packages/configuration evidence exist in repository inventory;
- exact version available or deployable under existing approved environment;
- documented filesystem/network/admin dependencies;
- whether a plausible set of independent failure domains can even be formed from known infrastructure;
- whether object/pointer/journal can share one atomic durability plane or require M3 composition.

This discovery should use existing repository/inventory records only unless separately authorized for host inspection.

If repository evidence cannot establish installed capability, the next fact remains UNKNOWN rather than prompting implicit host access.

## Future tests requiring separate permission

If a candidate later receives explicit implementation/test authority, F2 evidence would require at least:

1. positive ack under exact profile;
2. total loss/isolation of one selected verified failure domain;
3. surviving exact object readback;
4. surviving exact current pointer/CAS readback;
5. surviving PUT/CAS operation journal;
6. surviving dedupe/fence/generation lineage;
7. ResolveRequest after lost ack;
8. insufficient-quorum partition refuses positive ack;
9. stale writer cannot advance pointer;
10. split-brain/divergent head remains BLOCKED_CONFLICT;
11. isolated backup restore preserves lineage without auto-promotion.

None were executed here.

## OPERATOR decisions still required

- whether administrative independence is part of F2 trust boundary;
- exact definition of one storage failure domain for S1;
- acceptable unavailability during partition;
- owner appointment;
- privacy/read scope;
- retention policy;
- later implementation/test authority.

Still UNKNOWN:
backend, host, topology, replica count, quorum, RPO/RTO, backup cadence, retention values.

## Boundary accounting

Backend selected: NO
Host selected: NO
Topology selected: NO
Operational owner appointed: NO
Project deployment verified for C1/C2/C3: NO
Code/tests: 0
Host/shard access: 0
Shard WRITE: 0
Secrets: 0
Provider calls: 0
Automation change: 0
Project Sources/canon mutation: 0

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

Resume authority:
NOT_GRANTED

Memory-layering attempt 3:
NOT_AUTHORIZED

Historical PROMPT replay:
0

## EXPERIENCE

Идея → проверить не маркетинговое слово "HA", а конкретные primitives, из которых можно собрать F2.

Проба → сравнить consensus KV, synchronous SQL и replicated object store по exact first-party docs и затем вычесть всё, что не доказано для проекта.

Результат → C1 наиболее полно документирует consensus/CAS/fail-stop primitives; C2 документирует sync durability but needs external fencing/failover; C3 документирует failure-domain placement and replicated object ack but leaves S1 control/journal composition open. Ни один не является project-verified capability.

Вердикт → documentary discovery PASS; оснований выбрать backend нет.

Урок → опубликованная "durability" продукта и F2 системы — разные вещи. F2 появляется только когда exact project topology, ack semantics, control lineage and failure behavior доказаны вместе.

## Terminal

PASS_SIS_S1O2_F2_CAPABILITY_EVIDENCE_DISCOVERY_R01_DOCUMENT_ONLY

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
