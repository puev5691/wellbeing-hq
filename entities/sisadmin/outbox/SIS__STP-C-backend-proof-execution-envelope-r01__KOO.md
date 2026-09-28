# SIS → KOO: STP-C backend proof execution envelope r0.1

terminal: BLOCKED_SIS_STP_C_BACKEND_PROOF_EXECUTION_ENVELOPE_R01_MISSING_PINS
gate: BLOCKED_EXECUTION_ENVELOPE_MISSING_PINS
status: DOCUMENT_ONLY_EXECUTION_ENVELOPE_CANDIDATE
scope: DOCUMENT_ONLY_EXECUTION_ENVELOPE_PREPARATION
project_time: omitted

## 0. Human result

This document prepares an exact bounded execution envelope candidate for the reviewed STP-C backend proof harness.

No T01-T20 test was executed.
No backend was installed, started, selected or mutated.

The reviewed harness is sufficient conceptually, but the execution gate is NOT ready because mandatory run pins are absent:

- exact package/build identities and checksums;
- verified disposable runtime identity;
- implemented and pinned candidate adapters;
- exact candidate-specific topology/config;
- exact oracle/fixture canonical bytes and deterministic schedule;
- fake downstream implementation;
- authorized evidence root;
- bounded resource/attempt limits;
- exact safe host/power/corruption fault methods.

Therefore:

BLOCKED_EXECUTION_ENVELOPE_MISSING_PINS

The proposed first execution tranche, once all relevant pins are supplied, is intentionally smaller than T01-T20:

T01, T02, T03, T04, T10, T12

This first tranche proves the common atomic reservation / uniqueness / revision CAS / stale fence / authoritative absence / concurrent transition substrate before any crash, host, power, corruption, restore or downstream-effect test is attempted.

## 1. Exact basis

Current authoritative SIS writer:

puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

Exact authority:

puev5691/wellbeing-hq@e7d42bf7efe2bb99ee2356820945eb39a99b21ed:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-backend-proof-execution-envelope-r01__OPERATOR.md

Exact task:

puev5691/wellbeing-hq@1d9c900c23b45acb1344452c50340d68b8a1b055:
entities/koordinator/outbox/KOO__STP-C-backend-proof-execution-envelope-r01__SIS.md

Exact SHD review:

puev5691/wellbeing-hq@43549cd723db4a4b650e361bfe92d87496cecfa7:
entities/shardovik/outbox/SHD__STP-C-backend-proof-harness-r01-independent-review__KOO.md

Exact harness:

puev5691/wellbeing-hq@c69a7e8691b8cab56e6493a742908e6df265bdde:
entities/koder/outbox/KOD__STP-C-backend-bounded-empirical-proof-design-r01__KOO.md

blob:
12147a1405e9cc6a4fc20643a6031abf1cc69c2f

Harness test model:
STPC_LEDGER

Harness evidence schema:
STPC_PROOF_EVIDENCE_V1

Candidates remain:
- PostgreSQL 18
- FoundationDB 7.4.8
- etcd 3.7
- CockroachDB v26.1/current stable line

## 2. Candidate/build pin requirements

No candidate may execute under a family-name-only identity.

Every run must pin:
- exact product version;
- exact package/build artifact;
- source/repository/package locator;
- package checksum/digest;
- executable-reported version/build identity;
- adapter compatibility identity.

Silent substitution of patch/minor/build is forbidden.

### PostgreSQL 18

Current family identity:
PostgreSQL 18

Exact patch/build/package:
UNKNOWN

Required before execution:
- exact 18.x patch release;
- exact package/repository locator;
- package checksum or repository package digest;
- executable version output;
- exact linked/runtime package identity where materially relevant.

No nearby PostgreSQL 18 build may inherit proof.

### FoundationDB 7.4.8

Current version family supplied:
FoundationDB 7.4.8

Exact package/build artifact:
UNKNOWN

Required before execution:
- exact official 7.4.8 package artifact;
- exact package locator;
- package checksum/digest;
- server/client executable build/version evidence;
- adapter/library build compatibility.

The semantic version alone is insufficient as run identity.

### etcd 3.7

Current family identity:
etcd 3.7

Exact patch/build/package:
UNKNOWN

Required before execution:
- exact 3.7.x release;
- exact official binary/package locator;
- checksum/digest;
- etcd + etcdctl exact version/build evidence;
- client library/adapter version.

### CockroachDB v26.1/current stable line

Current family identity is NOT exact enough.

Exact patch/build/package:
UNKNOWN

Required before execution:
- exact v26.1.x or other exact approved build;
- exact official package/binary locator;
- checksum/digest;
- executable build tag/version;
- client/adapter identity.

"current stable line" cannot be an execution pin.

## 3. Disposable environment

Required environment class:

DISPOSABLE_NON_PRODUCTION_ISOLATED_PROOF_ENVIRONMENT

Current exact environment identity:
UNKNOWN

Owner/control boundary:
UNKNOWN

Authorized host/runtime:
UNKNOWN

Disposable storage root:
UNKNOWN

Production/project-live data access:
MUST BE NONE

Required proof before execution:

1. exact host/VM/container identity;
2. exact owner/controller;
3. proof the environment is non-production;
4. proof no live/project data is mounted/reachable;
5. exact disposable storage root;
6. exact network boundary;
7. exact allowed outbound/inbound connectivity;
8. cleanup/reimage capability;
9. candidate process confinement.

Environment pattern:

Candidate-specific runtime is REQUIRED where:
- topology differs;
- storage semantics differ;
- partition/host faults are tested;
- corruption/backup/restore tests require isolated disks/images.

A common supervisor/oracle control environment MAY be shared only if separately pinned and if no candidate state/storage is shared.

No filesystem path is invented here.

## 4. Candidate-specific topology/config pins

Defaults are NOT evidence.

Every run must capture exact configuration bytes/digest and readback.

### PostgreSQL 18

Required pins:
- exact node count;
- single-primary vs replicated variant;
- if replicated: synchronous/asynchronous mode and standby identities;
- authoritative read path = exact primary/current authority path;
- fsync-equivalent durability settings;
- synchronous_commit/full_page_writes and any relevant durability settings;
- transaction/isolation mode used by adapter;
- exact schema/index/constraint definition;
- client retry policy;
- process_fence storage/compare rule;
- backup/restore mechanism and exact mode;
- storage/filesystem class.

Current values:
UNKNOWN

### FoundationDB 7.4.8

Required pins:
- exact process/node count;
- redundancy mode;
- coordinator identities/count;
- transaction mode/read semantics;
- durability/storage engine/config relevant to claim;
- conflict-range/uniqueness key schema;
- fence key conflict scope;
- explicit immutable history key layout;
- backup/restore mode;
- client retry/commit-unknown behavior;
- GC/version-retention assumptions.

Current values:
UNKNOWN

### etcd 3.7

Required pins:
- exact member count;
- quorum topology;
- member identities;
- authoritative read mode = linearizable Range for authority/absence;
- exact Txn compare/write mapping;
- fence key compare rule;
- snapshot/restore mode;
- compaction settings;
- history-key retention independent of MVCC compaction;
- client retry behavior;
- storage/backend settings relevant to durability;
- cluster token/identity for disposable proof environment.

Current values:
UNKNOWN

### CockroachDB exact future build

Required pins:
- exact node count;
- replica placement/redundancy;
- authoritative non-stale read path;
- serializable transaction configuration;
- exact schema/unique/index definitions;
- revision/fence compare mapping;
- storage/durability settings relevant to selected deployment;
- transaction retry behavior;
- backup/restore mode;
- GC/retention settings;
- product integrity/corruption mechanism.

Current values:
UNKNOWN

## 5. Harness / adapter pin

### Harness

Exact reviewed harness:

puev5691/wellbeing-hq@c69a7e8691b8cab56e6493a742908e6df265bdde:
entities/koder/outbox/KOD__STP-C-backend-bounded-empirical-proof-design-r01__KOO.md

blob:
12147a1405e9cc6a4fc20643a6031abf1cc69c2f

Status:
DOCUMENT_DESIGN_ONLY

No execution inferred.

### Common model

Logical model name:
STPC_LEDGER

Exact machine-readable implementation identity:
NOT_IMPLEMENTED / UNKNOWN

### Candidate adapters

PostgreSQL adapter:
ADAPTER_NOT_IMPLEMENTED

FoundationDB adapter:
ADAPTER_NOT_IMPLEMENTED

etcd adapter:
ADAPTER_NOT_IMPLEMENTED

CockroachDB adapter:
ADAPTER_NOT_IMPLEMENTED

No adapter version/digest exists in the supplied evidence.

### Oracle

Independent supervisor-side oracle is specified conceptually by the harness.

Exact executable/artifact identity:
NOT_IMPLEMENTED / UNKNOWN

### Fixture canonical bytes

Harness supplies symbolic fixture identities:
R1/D1/O1/N1/E1/K1/F1 and successor identities.

Exact frozen canonical fixture bytes:
UNKNOWN / NOT_PINNED

### Digest profile

Harness mentions SHA-256 or separately approved digest profile for future evidence.

Exact approved run digest profile:
UNKNOWN

No digest profile is silently selected here.

### Deterministic seed / barrier schedule

Exact seed:
UNKNOWN

Exact canonical barrier schedule artifact:
UNKNOWN

Harness defines required barrier semantics, but no run-level frozen schedule bytes are supplied.

## 6. Fault method envelope for T01-T20

The table defines the only admissible fault METHOD CLASS at this stage.

Exact tool/command/controller identity remains UNKNOWN until separately pinned.

| Test | Fault/action method class | Exact execution pin status |
|---|---|---|
| T01 atomic reservation | transactional abort / adapter-controlled failure at multi-key reservation boundary | UNKNOWN |
| T02 uniqueness race | deterministic supervisor barriers + concurrent processes | UNKNOWN |
| T03 state_revision CAS | deterministic concurrent processes/barriers | UNKNOWN |
| T04 stale process_fence | deterministic stale-process barrier after successor fence commit | UNKNOWN |
| T05 process crash | OS/process kill of candidate client/worker process, not service/host | UNKNOWN |
| T06 host crash | independently controlled disposable host/VM crash or hard reboot method; process kill is insufficient | UNKNOWN |
| T07 real power loss | independently controlled hardware/provider-level power removal | NEEDS_HARDWARE_OR_PROVIDER_LEVEL_PROOF |
| T08 torn/partial write | safe isolated storage corruption/fault injection while offline or product-supported fault mechanism | UNKNOWN |
| T09 partition | controlled network partition of named members/links with independent rule evidence | UNKNOWN |
| T10 authoritative absence | no fault; exact current authoritative read path | UNKNOWN |
| T11 lost response | supervisor-controlled response drop proxy after evidenced backend commit | UNKNOWN |
| T12 concurrent transition | deterministic barriers + concurrent processes | UNKNOWN |
| T13 effect claim race | deterministic barriers + concurrent processes; fake downstream journal if invocation path reached | UNKNOWN |
| T14 OUTCOME_UNKNOWN | fake downstream accepts exact idempotency key, response intentionally dropped/delayed | NOT_IMPLEMENTED |
| T15 backup/restore | product-native pinned backup/snapshot + isolated restore root + new fence epoch | UNKNOWN |
| T16 history recovery | process/service/host restart as exact variant; authoritative readback after restart | UNKNOWN |
| T17 retention/GC | candidate-specific bounded compaction/GC using pinned config | UNKNOWN |
| T18 delayed stale response | response delay proxy controlled by supervisor | UNKNOWN |
| T19 corruption/integrity | safe candidate-specific product-level corruption/integrity injection/check + application-chain corruption | UNKNOWN |
| T20 missing linked evidence | adapter-controlled removal of one linked immutable evidence object in isolated clone | UNKNOWN |

Hard distinctions:

PROCESS_KILL != HOST_CRASH
HOST_REBOOT != REAL_POWER_LOSS
TIMEOUT != OPERATION_FAILURE_PROOF
UNAVAILABLE != ABSENT

For T07:

NEEDS_HARDWARE_OR_PROVIDER_LEVEL_PROOF

until an exact safe independently controlled power-loss method is authorized and verified.

## 7. CockroachDB corruption/integrity boundary

Two independent evidence layers are mandatory.

### Product-level integrity/corruption evidence

Required:
- current technical guarantee for the exact pinned build/config;
- exact supported or safely bounded corruption/integrity method;
- exact product check/readback output;
- evidence that the method does not escape disposable storage boundary.

Current status:
UNKNOWN

### Application transition/evidence-chain integrity

Required:
- exact STPC_LEDGER chain/evidence corruption injection;
- adapter readback;
- expected LEDGER_CORRUPT/block classification.

Current adapter status:
ADAPTER_NOT_IMPLEMENTED

Therefore candidate-wide CockroachDB PASS remains blocked by:

BLOCKED_COCKROACHDB_CORRUPTION_INTEGRITY_PROOF_UNRESOLVED

No application-layer PASS may conceal the unresolved product-level layer.

## 8. Fake downstream service

Required properties:

- exact implementation artifact identity;
- zero real-world effect capability;
- isolated local/disposable endpoint only;
- exact idempotency-key semantics;
- immutable synthetic receipt;
- exact query by operation/idempotency key;
- explicit synthetic NOT_APPLIED where provable;
- explicit UNKNOWN mode;
- controlled response drop;
- controlled response delay;
- append-only invocation journal;
- exact invocation count readback;
- reset procedure;
- deterministic fixture behavior.

Current implementation:
NOT_IMPLEMENTED

Current artifact identity:
UNKNOWN

No real downstream endpoint may substitute for this service in proof execution.

This blocks T14 and any effect-invocation variant requiring fake-service evidence.

## 9. Evidence location and preservation

Future run requirement:

ONE_IMMUTABLE_EVIDENCE_PACKAGE_PER_TEST_RUN

Required package contents include:
- candidate exact build identity;
- adapter identity;
- STPC_LEDGER model/oracle identity;
- topology identity;
- configuration identity;
- fault-controller identity;
- test ID/run ID;
- fixture bytes/digest;
- deterministic seed/schedule;
- observed responses;
- authoritative readback;
- exact operation history;
- integrity outputs;
- fake-service journal where applicable;
- cleanup/reset evidence;
- manifest.

Immutable manifest:
REQUIRED

Exact readback after preservation:
REQUIRED

Secrets:
FORBIDDEN

Production/project visitor data:
FORBIDDEN

Exact future evidence root path:
UNKNOWN

Reason:
no authorized/verified execution runtime is pinned.

Allowed location class:
a disposable execution-local staging root followed by separately authorized immutable project evidence publication/readback.

No concrete filesystem/repository path is invented here.

Evidence preservation/readback failure:
TEST RESULT = UNKNOWN
RUN CONTINUATION = BLOCKED

## 10. Resource / attempt limits

All execution limits must be bounded before any run.

Current exact numeric limits are unsupported by evidence and therefore remain UNKNOWN.

| Limit | Current value |
|---|---|
| CPU per candidate/run | UNKNOWN |
| RAM per candidate/run | UNKNOWN |
| Disk per candidate/run | UNKNOWN |
| Network bandwidth/traffic | UNKNOWN |
| Wall-clock duration per test | UNKNOWN |
| Wall-clock duration per run | UNKNOWN |
| Attempts per test | UNKNOWN |
| Automatic retry count | 0 unless separately authorized |
| Concurrent actors | UNKNOWN; minimum required by specific race case must be pinned |
| Candidate node/member count | UNKNOWN per candidate/topology |
| Parallel candidates | UNKNOWN; default execution not authorized |

Evidence needed before numbers:
- chosen disposable environment capacity;
- exact topology;
- package footprint;
- expected data volume;
- fault/restart latency;
- supervisor limits;
- evidence bundle size;
- provider/hardware safety constraints.

No numeric value is guessed.

## 11. Cleanup/reset contract

Every test/run must have a cleanup identity and independent verification.

Required sequence:

1. freeze/preserve evidence package;
2. exact readback of preserved evidence;
3. stop candidate processes/services within disposable environment;
4. remove/reset candidate disposable data root;
5. reset fake downstream state/journal where used;
6. remove network partition/proxy/fault rules;
7. restore normal disposable supervisor connectivity;
8. verify no candidate process remains;
9. verify new run namespace/root is clean;
10. verify old run cannot contaminate new authoritative readback;
11. record cleanup evidence.

Candidate backup/restore test may preserve its exact source backup as immutable evidence until readback is complete.

Cleanup failure result:

NEXT_RUN_BLOCKED_OR_UNKNOWN

No subsequent run may silently reuse a contaminated environment.

## 12. Stop conditions

STOP immediately before any further execution if any occurs:

S1.
Candidate package/build/version/digest mismatch.

S2.
Topology/config/read-mode differs from exact envelope.

S3.
Any access/mount/network reachability to non-disposable project/live data.

S4.
Fault method exceeds separately authorized method class.

S5.
Evidence preservation or exact readback fails.

S6.
Cleanup/reset verification fails.

S7.
Secret/credential exposure or unexpected sensitive material enters evidence.

S8.
CPU/RAM/disk/network/time/attempt boundary is exceeded or cannot be measured.

S9.
Candidate process/storage/network escapes the disposable environment.

S10.
Corruption proof cannot be safely bounded.

S11.
CockroachDB product-level corruption/integrity mechanism remains unsafe/ambiguous for candidate-wide proof.

S12.
Unexpected provider/hardware behavior makes the safety boundary unverifiable.

S13.
Adapter/model/oracle/fixture identity differs from pinned bytes.

S14.
Fault injection cannot be independently proven.

S15.
Authoritative read path becomes ambiguous.

S16.
A stale/lagging read path is used where authoritative absence/current state is required.

S17.
Fake downstream can reach or affect any real-world endpoint.

S18.
Any test tries to infer PASS from timeout, process exit, service restart or log text alone.

S19.
Authority/scope changes or task supersession occurs.

S20.
Any condition would require CHECKPOINT_DURABLE, deployment, live WRITE/CAS or production mutation.

## 13. Proposed first execution tranche

Proposed first tranche after missing pins are closed:

T01 — atomic reservation
T02 — uniqueness race
T03 — state_revision CAS
T04 — stale process_fence
T10 — authoritative absence
T12 — concurrent transition race

Candidates:
all four surviving candidates, but each only under its own exact pinned build/adapter/config identity.

### Why this tranche is first

These six tests validate the common logical substrate before expensive or riskier fault classes.

They do NOT require:
- host crash;
- real power loss;
- storage corruption;
- backup/restore;
- fake downstream effect invocation.

They establish whether each adapter/backend can even satisfy:
- all-or-none reservation;
- conflict uniqueness;
- revision CAS;
- stale writer fencing;
- authoritative current absence;
- single-winner transition semantics.

If a candidate fails any mandatory primitive in this tranche without an exact equivalent design path:
that candidate may be DISQUALIFIED before host/power/corruption tests consume resources.

### Dependencies still required for first tranche

Even this reduced tranche is NOT run-ready because the following are missing:

- exact candidate build/package/digest for each candidate;
- exact disposable environment identity;
- exact adapter implementation/version;
- exact STPC_LEDGER machine-readable model;
- exact supervisor oracle implementation;
- frozen fixture canonical bytes;
- approved digest profile;
- deterministic seed/barrier schedule;
- candidate topology/config/read-mode;
- evidence root;
- resource/attempt limits;
- cleanup implementation/evidence method.

Therefore no T01/T02/T03/T04/T10/T12 execution is authorized.

## 14. Deferred tranche dependencies

Later tests add further blockers:

T05:
exact process-kill controller.

T06:
exact disposable host crash/reboot controller.

T07:
NEEDS_HARDWARE_OR_PROVIDER_LEVEL_PROOF.

T08/T19:
safe product-specific corruption/integrity method.

T09:
exact network partition controller/topology.

T11/T18:
exact response drop/delay proxy.

T13/T14:
fake downstream service implementation.

T15:
candidate-specific backup/restore method + successor-fence procedure.

T16:
restart/recovery controller.

T17:
exact retention/GC/compaction settings.

T20:
safe isolated linked-evidence corruption method in adapter clone.

## 15. Exact missing pins

The execution envelope is blocked by the following mandatory missing facts/evidence.

M1.
PostgreSQL exact 18.x package/build/locator/digest.

M2.
FoundationDB 7.4.8 exact package/build/locator/digest.

M3.
etcd exact 3.7.x package/build/locator/digest.

M4.
CockroachDB exact build/package/locator/digest.

M5.
Verified disposable execution environment identity and owner/control boundary.

M6.
Verified disposable storage root and isolation proof.

M7.
PostgreSQL adapter implementation identity/version.

M8.
FoundationDB adapter implementation identity/version.

M9.
etcd adapter implementation identity/version.

M10.
CockroachDB adapter implementation identity/version.

M11.
Machine-readable STPC_LEDGER model implementation identity.

M12.
Independent oracle implementation identity.

M13.
Frozen fixture canonical bytes + manifest.

M14.
Exact approved digest profile.

M15.
Deterministic seed + barrier schedule artifact.

M16.
Candidate-specific topology/config/read-mode/durability pins.

M17.
Exact evidence root and immutable preservation/readback procedure.

M18.
CPU/RAM/disk/network/time/attempt/concurrency limits.

M19.
Exact cleanup/reset implementation and verification method.

M20.
Fake downstream service implementation for later effect tests.

M21.
Exact safe process/host/partition/response/storage/backup fault-controller identities for applicable later tests.

M22.
Safe product-level corruption/integrity proof method for CockroachDB.

M23.
Independent real power-loss capability for T07, or explicit acceptance that T07 remains NEEDS_HARDWARE_OR_PROVIDER_LEVEL_PROOF and cannot yield whole-envelope power-loss PASS.

## 16. Final gate

For the proposed first tranche:

required exact pins:
NOT COMPLETE

Execution authority readiness:
NO

Gate:

BLOCKED_EXECUTION_ENVELOPE_MISSING_PINS

Reason:
the proof design is reviewed, but no exact executable build/adapter/runtime/config/oracle/evidence/resource envelope has yet been established.

This is a preparation blocker, not a failure of the backend proof concept.

## 17. Boundary preservation

T01-T20 executed:
0

Backend selected:
NO

Backend installed/run:
NO

Live storage:
NO

Host mutation:
NO

Deployment:
NO

Production secrets:
NO

Live WRITE/CAS:
NO

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

Fast Gate/profile activation:
NO

Project Source activation:
NO

EOM pilot:
NO

Memory-layering attempt 3:
NO

## EXPERIENCE

Идея → превратить хороший документальный harness в реально исполнимую коробку, где каждый пакет, процесс, байт фикстуры, fault-controller и предел ресурса имеет точную личность.

Проба → проверить, какие из обязательных pins уже существуют в доказанном виде.

Результат → conceptual harness готов, но executable envelope пока нет: отсутствуют exact builds, adapters, runtime, oracle/fixture implementation, resource limits и fault controllers.

Неудача запуска → намеренная: ни один тест не стартовал, потому что execution boundary пока нельзя доказать.

Урок → "мы знаем, как тестировать" и "мы можем безопасно запустить тест сейчас" — разные факты. Между ними обычно лежит самый скучный документ в проекте. Именно он потом не даёт выключить не тот сервер.

## Terminal

BLOCKED_SIS_STP_C_BACKEND_PROOF_EXECUTION_ENVELOPE_R01_MISSING_PINS

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
