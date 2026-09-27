# SIS → KOO: operational shard admission profile design r0.1

terminal: PASS_SIS_OPERATIONAL_SHARD_ADMISSION_PROFILE_DESIGN_R01_READY_FOR_REVIEW
status: CANDIDATE_NOT_ACTIVE
scope: DOCUMENT_ONLY_ADMISSION_PROFILE_DESIGN
project_time: omitted

## 0. Назначение и статус

Этот документ — standalone candidate admission profile для будущего operational shard store.

Он НЕ:
- назначает trust root;
- выбирает active backend;
- назначает operator/service account;
- создаёт credentials;
- разрешает deployment;
- разрешает host mutation;
- разрешает live WRITE/CAS;
- устанавливает CHECKPOINT_DURABLE;
- разблокирует EOM pilot;
- разрешает memory-layering attempt 3;
- активирует Project Source/canon.

### Классы утверждений

FACT:
факт из действующего project field / exact authority / exact immutable artifact.

VERIFIED_RESULT:
результат независимой проверки, ограниченный её scope.

CANDIDATE:
предлагаемая структура/вариант для будущего решения; не активен.

UNKNOWN:
решение или факт не установлен действующими источниками.

## 1. Exact basis

FACT — Exact authority:
puev5691/wellbeing-hq@bb79c50ed20b789e620eb4acfdcee6f62c25409e:
entities/koordinator/outbox/KOO__authorize-SIS-operational-shard-admission-profile-design-r01__OPERATOR.md
blob:
965c6e16d7b0f8c9c485c3716c00321dacd21e89

FACT — Exact task:
puev5691/wellbeing-hq@3a77b023d8dfd88512efa9fa34ec970895c504c8:
entities/koordinator/outbox/KOO__operational-shard-admission-profile-design-r01__SIS.md
blob:
7244abc39a376b9a7d27f99ceef3cf77b1f378e1

FACT — Reviewed offline candidate:
puev5691/wellbeing-hq@9faa1ede62460fdcc073e48fd13b10f93027e957:
entities/koder/outbox/operational-shard-store-offline-r02
tree:
8c5cb47ce3267dac4b1810e93cf993a35a3a0492

VERIFIED_RESULT — SIS:
puev5691/wellbeing-hq@92038724366a4fb7e54c2e3014b70445bf28ae16
PASS_SIS_OPERATIONAL_SHARD_STORE_OFFLINE_R02_REREVIEW

VERIFIED_RESULT — SHD:
puev5691/wellbeing-hq@a76dfcea52627cbe73fe8b29abc152c3b3f25404
PASS_SHD_OPERATIONAL_SHARD_STORE_OFFLINE_R02_REREVIEW

VERIFIED_RESULT — SHT:
puev5691/wellbeing-hq@79a351255020a4a94b007117abefbb087bb59880
PASS_SHT_OPERATIONAL_SHARD_STORE_OFFLINE_R02_BOUNDARY_REVIEW

VERIFIED_RESULT:
r0.2 proves only bounded local/synthetic properties.
It does not establish live trust, backend, operator, production durability or live authority.

## 2. Candidate profile object

CANDIDATE — profile type:

OperationalShardAdmissionProfileV1

Candidate closed fields:

- schema = operational-shard-admission-profile-v1
- profile_id
- revision
- status
- namespace_scope
- allowed_operations
- supervisor_trust_profile_ref
- writer_fence_policy_ref
- currentness_policy_ref
- backend_profile_ref
- store_operator_profile_ref
- isolation_profile_ref
- retention_gc_policy_ref
- canonical_unavailable_policy_ref
- verifier_profile_ref
- file_service_profile_ref
- publisher_profile_ref
- activation_authority_ref
- supersedes
- evidence_refs

Candidate statuses:
- CANDIDATE
- REVIEWED_CANDIDATE
- ADMITTED
- STALE
- REVOKED
- SUPERSEDED

FACT:
No ADMITTED profile currently exists.

UNKNOWN:
who is authorized to issue the first real profile.

## 3. SupervisorTrustProfile

### 3.1 Purpose

CANDIDATE:
SupervisorTrustProfile is the external trust contract that tells the store which externally authenticated evidence may be used to decide whether a mutation request is admissible.

It must NOT be issued by the shard itself.

### 3.2 Candidate owner/issuer models

#### Option STP-A — OPERATOR-approved profile, technically maintained by KOO/KAN boundary

CANDIDATE:
OPERATOR approves exact trust profile identity and issuer scope.
A designated project process maintains the immutable profile artifact under that approval.

Consequence:
strong human approval boundary; operational updates require explicit project process.

Risk:
may be slower for revocation/freshness.

#### Option STP-B — dedicated trust-profile authority/service

CANDIDATE:
A separately approved technical authority signs/version-controls trust profiles under a narrow standing delegation.

Consequence:
faster operational revocation/update path.

Risk:
creates a new high-value security authority requiring independent lifecycle, key custody and audit.

#### Option STP-C — multi-party approval profile

CANDIDATE:
Profile becomes valid only with exact evidence from two independent approval roles/processes.

Consequence:
reduced single-authority risk.

Risk:
higher availability/coordination cost.

UNKNOWN:
which model is selected.

### 3.3 Authentication-root options

CANDIDATE options:

1. exact Git canonical artifact + independently pinned signing/verification key;
2. offline root key with signed versioned trust-profile artifacts;
3. threshold/multi-signature root;
4. hardware-backed signing root, if later available and separately approved.

NOT SUFFICIENT:
- request-supplied public key;
- unsigned JSON;
- a shard-local file declaring itself trusted;
- repository path alone without authenticated currentness;
- cache copy without revocation/currentness verification.

UNKNOWN:
root technology, key owner, custody and recovery model.

### 3.4 Required scope

CANDIDATE minimum scope fields:

- profile_id / revision;
- admitted store_id;
- namespace patterns;
- allowed operations: READ / VERIFY / PUT / CAS separately;
- allowed attestor identities;
- allowed writer-fence verifier;
- allowed authority source class;
- approved source-set identity rule;
- backend profile identity;
- revocation state;
- supersession link;
- activation authority locator;
- validity/currentness rule.

### 3.5 Version and revocation

CANDIDATE:
- immutable revision;
- successor creates new revision;
- no silent in-place mutation;
- old revision becomes SUPERSEDED or REVOKED;
- store checks exact current revision before mutation;
- revocation overrides cached admission;
- missing/ambiguous revocation state => fail closed.

UNKNOWN:
revocation channel and freshness SLA.

## 4. WriterFenceAttestation

### 4.1 Purpose

CANDIDATE:
WriterFenceAttestation binds a writer instance to a specific:
- entity;
- task;
- task version;
- stream/namespace;
- writer identity;
- monotonic epoch;
- authority_ref;
- trust_profile_ref;
- approved_sources_ref;
- validity/revocation evidence.

### 4.2 Attestor candidate models

#### WFA-A — dedicated epoch attestor

CANDIDATE:
A narrow technical attestor issues signed epochs only after verifying canonical Writer Gate/current-writer evidence.

Consequence:
clean monotonic-fence semantics.

Risk:
attestor becomes critical availability/security dependency.

#### WFA-B — KOO-coordinated attestation using external signing component

CANDIDATE:
KOO supplies reconciled governance evidence; a separate signing component emits the attestation.

Consequence:
keeps routing/governance interpretation with KOO but cryptographic issuance separate.

Risk:
must ensure KOO message cannot itself bypass signing verification.

#### WFA-C — admission profile issuer also issues epoch attestations

CANDIDATE:
single authority issues both trust profile and writer epochs.

Consequence:
simpler operationally.

Risk:
larger blast radius and weaker separation of duties.

UNKNOWN:
attestor selection.

### 4.3 Monotonic epoch

CANDIDATE:
- epoch is monotonically increasing per exact namespace/task-version;
- store persists highest admitted epoch;
- lower epoch rejected;
- same epoch + different writer identity => conflict;
- replacement requires canonical handoff/Writer Gate plus epoch strictly greater than high-water;
- numeric epoch alone never creates authority.

### 4.4 Freeze/replacement

FACT:
project writer/recovery governance exists outside the store.

CANDIDATE:
- freeze/handoff/replacement evidence must be verified before accepting a higher epoch;
- frozen prior writer becomes invalid for mutation immediately once revocation/currentness evidence is accepted;
- replacement cannot be inferred from technical access or later timestamp.

### 4.5 Revocation/replay/staleness

CANDIDATE:
- attestation carries unique immutable identity and exact scope;
- replay with stale profile/task/writer/source state is rejected;
- revoked attestation is rejected even if signature is valid;
- reuse outside exact namespace/task/version is rejected;
- missing currentness evidence => BLOCKED_TRUST_ROOT / STALE_ATTESTATION;
- cached attestation cannot fail open beyond approved freshness policy.

UNKNOWN:
exact freshness duration and revocation delivery mechanism.

## 5. Currentness / freshness

### 5.1 Checks before every mutation

CANDIDATE mandatory pre-mutation check set:

1. exact admission profile is current and not revoked/superseded;
2. exact writer attestation is valid and current;
3. canonical current-writer evidence matches writer;
4. task authority is current and addressed to the exact action/entity;
5. task_version is not superseded;
6. approved source-set identity is current where required;
7. freeze/handoff/replacement state has not changed;
8. backend profile is admitted and current;
9. store operator/process identity matches profile;
10. namespace and operation are allowed;
11. retained fence high-water is compatible;
12. no unresolved integrity blocker exists;
13. canonical authority source is reachable within approved freshness rule.

### 5.2 Candidate freshness model

CANDIDATE:
two-layer model:

A. mutation-time hard freshness:
canonical authority/current-writer/task evidence must be freshly verified or covered by an explicitly approved short-lived freshness token.

B. read-only degraded mode:
when canonical authority is unavailable, previously verified immutable objects may remain readable/inspectable under separate READ policy, but mutation admission fails closed.

UNKNOWN:
numeric freshness interval.

### 5.3 Fail-closed behavior

CANDIDATE:
if canonical authority cannot be verified:
- PUT = BLOCKED_CURRENTNESS
- CAS = BLOCKED_CURRENTNESS
- writer epoch advancement = BLOCKED_CURRENTNESS
- new admission = BLOCKED_CURRENTNESS
- deletion/GC that could remove recovery evidence = BLOCKED_GC_CURRENTNESS

No fail-open cache.

## 6. Backend candidates

No backend is selected active.

### 6.1 Candidate class B-A — embedded transactional database

Examples as class only:
embedded DB with atomic transactions, WAL/journal and explicit durability controls.

Required properties:
- atomic transaction for pointer + fence + operation ledger;
- compare-and-set/serializable mutation;
- durable commit semantics;
- crash recovery;
- checksums/integrity behavior;
- fsync/sync controls;
- corruption detection;
- backup/snapshot procedure.

Evidence required before selection:
- process-crash tests;
- power-loss/fault-injection where feasible;
- WAL recovery tests;
- torn-write/corruption tests;
- concurrent writer tests;
- disk-full tests;
- fsync verification;
- platform/filesystem compatibility;
- independent SIS/SHD review.

### 6.2 Candidate class B-B — server transactional database

Required properties:
- serializable transaction or proven equivalent;
- exact CAS semantics;
- transactional ledger/fence/pointer commit;
- durable WAL;
- authenticated client identity;
- transaction retry semantics that do not violate operation idempotency;
- isolation from unrelated databases.

Evidence required:
same as above plus:
- network partition behavior;
- leader/failover semantics;
- replication consistency;
- credential/role isolation;
- backup/restore;
- split-brain handling.

### 6.3 Candidate class B-C — dedicated transactional KV/store with CAS

Required:
- atomic compare-and-set;
- operation ledger durability;
- fence high-water atomicity or one transaction domain;
- persistent request/outcome binding;
- exact recovery semantics.

Evidence:
vendor/runtime semantics must be tested, not assumed from API names.

### 6.4 Explicit non-candidate without extra protocol

Plain filesystem files + rename alone:
NOT SUFFICIENT for full pointer/fence/ledger atomic contract unless a separately reviewed WAL/transaction protocol proves equivalence.

UNKNOWN:
which backend class will be selected.

## 7. Store owner / operator

### 7.1 Role boundary

CANDIDATE:
store owner governs service lifecycle/configuration.
Store operator runs the service within exact admitted profile.
Neither may create task authority, current-writer state or trust-profile authority by technical access alone.

Potential role models:

SO-A:
SIS owns infrastructure/service lifecycle; separate trust authority owns admission policy.

SO-B:
dedicated future software/storage contour owns runtime; SIS owns host/runtime boundary.

SO-C:
split owner/operator:
one role owns configuration and updates, another narrow service identity performs mutations.

UNKNOWN:
selected model.

### 7.2 Process identity

CANDIDATE requirements:
- dedicated non-login service identity;
- least privilege;
- access only to admitted store roots;
- no arbitrary project-repo write;
- no GitHub publisher credentials;
- no attestor private key;
- no requester credentials;
- separate read-only verifier identity.

No service account is appointed by this document.

### 7.3 Credential custody

CANDIDATE:
- service credentials stored outside package/artifacts/logs;
- trust signing key never readable by mutation service;
- publisher credentials never readable by store;
- verifier uses read-only credentials if credentials are required;
- rotation/revocation separately auditable;
- secret material excluded from shard records.

UNKNOWN:
credential platform/custodian.

## 8. Isolation model

CANDIDATE mandatory separation:

### Requester
May submit bounded request/evidence.
Cannot self-admit writer, trust root or backend.

### Attestor
May attest only its approved writer-fence scope.
Cannot mutate store data directly.

### Mutation service
May perform admitted PUT/CAS.
Cannot issue task authority, writer status, trust profiles or Git acceptance.

### Read-only verifier
May independently read and verify store state.
Must not share mutable store package/config path with writer where avoidable.
Cannot mutate pointer/fence/ledger.

### File/Artifact Service
Receives only isolated staged exact bytes under its existing request contract.
authority_semantics = none.
project_state_semantics = none.
No Git publication implied.

### GitHub publisher
Separately authorized.
Publishes bounded significant artifacts.
Cannot infer store mutation authority from publication capability.

### Prohibited capability sharing

CANDIDATE:
- attestor signing key unavailable to mutation service;
- publisher credentials unavailable to store;
- mutation credentials unavailable to requester;
- verifier must not inherit write capability;
- one process must not silently combine attestor + writer + verifier + publisher roles;
- package presence or host access does not create authority.

## 9. Retention / GC

### 9.1 Required policy fields

CANDIDATE RetentionPolicyV1:
- policy_id
- revision
- namespace scope
- retention_class
- expiry_class
- canonical_anchor_required
- hold semantics
- orphan policy
- unresolved-operation policy
- superseded-record policy
- deletion authority_ref
- deletion verification requirement
- supersedes
- status

UNKNOWN:
all numerical durations unless separately approved.

### 9.2 Holds

Deletion forbidden when:
- legal/project hold exists;
- preservation/recovery hold exists;
- unresolved conflict/CAS evidence exists;
- record is current pointer head;
- record is required parent in current/recovery chain;
- canonical promotion/readback is incomplete;
- policy identity/currentness is unknown.

### 9.3 Unresolved operations

CANDIDATE:
records/ledger evidence involved in UNKNOWN, unresolved CONFLICT or recovery ambiguity are not GC-eligible.

### 9.4 Orphan objects

CANDIDATE:
orphan means immutable object not referenced by current pointer.

Orphan is NOT automatically deletable.

Deletion requires:
- no unresolved operation can still bind it;
- no hold;
- no recovery dependency;
- no pending promotion;
- retention policy permits deletion;
- independent reachability check;
- deletion receipt/readback.

### 9.5 Canonical anchors

CANDIDATE:
if an object is required to reconstruct state newer than last canonical anchor, it cannot be deleted merely because it is not current.

### 9.6 Deletion conditions

All must hold:
1. exact policy current;
2. no hold;
3. no pointer/head/reference;
4. no unresolved operation;
5. no recovery dependency;
6. canonical anchor requirements satisfied;
7. deletion authority valid;
8. exact target identity checked;
9. deletion outcome recorded;
10. post-delete readback confirms intended absence.

## 10. Canonical authority unavailable

### 10.1 Exact candidate states

CANDIDATE:
- CANONICAL_AUTHORITY_UNAVAILABLE
- CURRENTNESS_UNKNOWN
- MUTATION_BLOCKED
- PROMOTION_BLOCKED
- REPLACEMENT_BOUNDARY_BLOCKED
- GC_BLOCKED_CURRENTNESS

### 10.2 What may continue

Candidate possibilities, subject to separate approved READ policy:
- read exact already stored immutable objects;
- verify hashes/ledger/pointer locally;
- inspect provisional historical records;
- prepare non-authoritative local diagnostics.

### 10.3 What may NOT continue

Never claim or perform solely from cached/local evidence:
- new PUT/CAS mutation admission;
- writer replacement;
- epoch issuance;
- task authority;
- trust-profile update;
- canonical promotion;
- Git acceptance;
- CHECKPOINT_DURABLE;
- recovery boundary beyond last verified canonical anchor;
- destructive GC of unresolved recovery evidence.

If future policy wishes to permit bounded provisional writes while canonical source is unavailable, that requires a separate explicit OPERATOR decision and a distinct profile class. This candidate does not permit it.

## 11. Exact prerequisites before any future live-admission decision

KOO must NOT open live admission merely because this document passes review.

Required evidence/decisions first:

1. OPERATOR decision selecting SupervisorTrustProfile owner/issuer model.
2. Exact authenticated trust-root technology and immutable root identity.
3. Key custody/rotation/recovery/revocation design.
4. OPERATOR decision selecting WriterFence attestor model.
5. Monotonic epoch issuance and revocation protocol.
6. Approved freshness/currentness policy with explicit failure behavior.
7. Selected backend class and exact candidate implementation.
8. Independent SIS proof of transaction/CAS/WAL/fsync/platform behavior.
9. Independent SHD proof of storage/integrity/recovery behavior.
10. Fault-injection evidence including:
   - process crash;
   - disk-full;
   - corruption;
   - power-loss/fault-domain tests where applicable;
   - concurrency;
   - lost response;
   - stale/revoked writer.
11. Exact store host/fault-domain decision.
12. Exact store owner/operator decision.
13. Exact process/service identity and least-privilege model.
14. Credential custody/rotation/revocation model.
15. Read-only verifier design and independent capability separation proof.
16. File/Artifact Service integration profile pinned to reviewed exact package.
17. GitHub publisher authority/process separated from store.
18. Retention/GC policy approved, including holds/orphans/unresolved operations.
19. Canonical-unavailable policy approved.
20. Rollback/pre-state/recovery plan for deployment itself.
21. Exact bounded live-admission authority from OPERATOR.
22. Exact current task/writer/source/trust evidence at the live gate.

Until all required items applicable to the selected option are satisfied:
LIVE WRITE/CAS = NOT_AUTHORIZED.

## 12. Decision table for OPERATOR

| Governance choice | Option | Consequence | Evidence needed before decision | Decision owner | Current status |
|---|---|---|---|---|---|
| SupervisorTrustProfile issuer | STP-A OPERATOR-approved project profile | strongest direct human gate; slower updates | lifecycle, update/revocation workflow | OPERATOR | CANDIDATE |
| SupervisorTrustProfile issuer | STP-B dedicated trust authority | faster revocation; new critical authority | service design, key custody, independent review | OPERATOR | CANDIDATE |
| SupervisorTrustProfile issuer | STP-C multi-party approval | reduced single-point authority | quorum semantics, availability/failure policy | OPERATOR | CANDIDATE |
| Authentication root | Git artifact + pinned signing key | integrates canonical repo with cryptographic root | key lifecycle, signature verification, Git currentness | OPERATOR | CANDIDATE |
| Authentication root | offline root key | strong separation; operational key handling burden | custody, recovery, rotation, signing procedure | OPERATOR | CANDIDATE |
| Authentication root | threshold root | lower single-key risk; more complexity | quorum/key ceremony/recovery tests | OPERATOR | CANDIDATE |
| WriterFence attestor | WFA-A dedicated epoch attestor | clean monotonic fence service | attestor implementation, canonical writer verification, key custody | OPERATOR | CANDIDATE |
| WriterFence attestor | WFA-B KOO evidence + separate signer | preserves KOO reconciliation role | binding contract, signer isolation, replay tests | OPERATOR | CANDIDATE |
| WriterFence attestor | WFA-C same as trust issuer | simpler, larger blast radius | risk review, revocation/failure analysis | OPERATOR | CANDIDATE |
| Freshness policy | hard fresh check every mutation | strongest currentness; depends on canonical availability | latency/availability evidence | OPERATOR | CANDIDATE |
| Freshness policy | short-lived signed freshness token | tolerates brief source outage | TTL decision, token replay/revocation tests | OPERATOR | CANDIDATE |
| Backend class | embedded transactional DB | simple isolated service, local fault domain | fsync/crash/corruption/disk-full tests | OPERATOR after SIS+SHD review | CANDIDATE |
| Backend class | server transactional DB | better multi-client/replication options, more moving parts | partition/failover/replication/credential tests | OPERATOR after SIS+SHD review | CANDIDATE |
| Backend class | transactional KV/CAS store | native CAS possible | atomicity/ledger/fence equivalence proof | OPERATOR after SIS+SHD review | CANDIDATE |
| Store owner model | SO-A SIS infra owner | clear host/runtime responsibility | role boundary and no trust-authority overlap | OPERATOR | CANDIDATE |
| Store owner model | SO-B dedicated software/storage contour | specialized ownership | contour authority/recovery/deployment design | OPERATOR | CANDIDATE |
| Store owner model | SO-C split owner/operator | stronger separation | runbook, capability split, failure ownership | OPERATOR | CANDIDATE |
| Canonical unavailable policy | hard block all mutations | simplest/strongest fail-closed | operational impact analysis | OPERATOR | CANDIDATE |
| Canonical unavailable policy | future separate provisional-write profile | availability gain, much higher reconciliation risk | separate design/review/authority | OPERATOR | UNKNOWN / NOT AUTHORIZED |
| Retention duration | numerical policy | controls capacity/recovery window | workload, recovery, legal/project requirements | OPERATOR / designated policy owner | UNKNOWN |
| RPO/RTO | numerical targets | determines backend/backup architecture | service criticality/failure model | OPERATOR | UNKNOWN |
| Store host/fault domain | specific host/domain | creates operational dependency | capacity, isolation, failure-domain, backup evidence | OPERATOR after SIS review | UNKNOWN |
| Credential custodian | specific custodian/platform | establishes secret lifecycle | access/recovery/rotation/audit design | OPERATOR | UNKNOWN |

## 13. Current status summary

FACT:
offline r0.2 exact package exists and is immutable at its pinned locator.

VERIFIED_RESULT:
SIS, SHD and SHT independently passed their bounded offline reviews.

VERIFIED_RESULT:
the candidate does not itself mint project authority.

CANDIDATE:
this document defines one possible admission governance structure.

UNKNOWN:
- trust-profile owner/issuer;
- authentication root;
- attestor;
- root-key custody;
- revocation channel;
- freshness interval;
- backend;
- host;
- operator/service account;
- credential custodian;
- retention duration;
- RPO/RTO;
- live-admission authority.

NOT ESTABLISHED:
- production durability;
- live WRITE/CAS;
- CHECKPOINT_DURABLE.

BLOCKED / NOT AUTHORIZED:
- EOM pilot;
- memory-layering attempt 3.

## EXPERIENCE

Идея → превратить набор технических «неизвестно» вокруг trust/backend/operator в один decision-ready admission profile, не назначая никого самовольно.

Проба → разделить trust issuance, writer fence, currentness, backend, operator, isolation, retention и canonical-failure behavior на отдельные gates и options.

Результат → появился standalone candidate, по которому ОПЕРАТОР может принимать точные решения по одному вопросу за раз, не смешивая storage correctness с authority.

Успех → document-only candidate ready for independent review.

Урок → база данных может отлично хранить доказательства доверия, но не должна сама решать, кому доверять. Стоит позволить ей это один раз — и вот уже SQLite требует кабинет и печать.

## Terminal

PASS_SIS_OPERATIONAL_SHARD_ADMISSION_PROFILE_DESIGN_R01_READY_FOR_REVIEW

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
