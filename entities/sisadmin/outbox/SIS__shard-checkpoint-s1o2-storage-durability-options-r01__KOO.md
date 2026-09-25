# SIS → KOO: S1+O2 storage durability profile options r0.1

terminal: PASS_SIS_S1O2_STORAGE_DURABILITY_PROFILE_OPTIONS_R01_DOCUMENT_ONLY
scope: DOCUMENT_ONLY_COMPARATIVE_DECISION_INPUT
project_time: omitted
governance_candidate: CANDIDATE_NOT_ACTIVE
CHECKPOINT_DURABLE: NOT_ESTABLISHED
resume_authority: NOT_GRANTED
operational_owner: NOT_APPOINTED

## Человеческий смысл

Для S1+O2 сейчас недостаточно данных, чтобы честно выбрать конкретный backend, host, число реплик, срок хранения, RPO или RTO.

Зато данных достаточно, чтобы сравнить три контрактные модели хранения и понять, какие доказательства понадобятся для выбора.

Все три модели обязаны сохранять уже зафиксированные границы:
- immutable checkpoint object отдельно от current pointer;
- PUT_IMMUTABLE отдельно от COMMIT_CURRENT_CAS;
- operation-qualified dedupe/outcome journal;
- lost-ack reconciliation без blind retry;
- StorageAck отдельно от independent readback;
- durable bytes отдельно от resume authority;
- backup/restore отдельно от live replica и current promotion;
- UNKNOWN не превращается в PASS.

Существующий mazhor gateway не является доказательством ни одной из моделей: он подтверждён только как VERIFY-only read-only one-shot без checkpoint WRITE.

Главный недостающий факт для осмысленного выбора между моделями:
**какой exact класс отказа S1 должен переживать без потери уже подтверждённого checkpoint/current pointer**.

Пока этот failure objective не выбран, нельзя обоснованно определить:
- сколько независимых failure domains нужно;
- нужен ли synchronous multi-domain commit;
- какой RPO допустим;
- какой RTO нужен;
- как часто делать backup;
- сколько хранить payload/dependencies/dedupe/fence lineage.

## Resume-First / authority

Exact task:
puev5691/wellbeing-hq@8d4ab91bf3760e25034743bbd6fe7740c5a2f432:
entities/koordinator/outbox/KOO__shard-checkpoint-s1o2-storage-durability-options-r01__SIS.md
blob:
ccc0053c359b44226a23a57365a80b9330d50463

Authority:
AUTHORIZE_SIS_S1O2_STORAGE_DURABILITY_PROFILE_OPTIONS_R01_DOCUMENT_ONLY

Fresh HQ HEAD before result:
8d4ab91bf3760e25034743bbd6fe7740c5a2f432

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

No competing SIS writer, superseding task or competing storage-options result was found at the execution boundary.

Approved Project Sources loaded and exact blobs matched:
- core v2.5: a42f7dca6a7469a54fa2da24aae0da4e549c9d33;
- roles v2.4: 1772339cb74dae8550bfbd2e33401c34a929e911;
- recovery v1.6: 233117e1c9509d730e1f5ec532b1cabe3f786609;
- file-work v2.4: e9c29d62057f34e4f771d6057a36d9b7f72e74c2;
- source-loading v2.2: 69eb657f260a019f76e8e707c880ea88c1dfa0bf;
- task-conveyor v1.2: df7896d867eeeffff506319538fedad938856686.

Historical PROMPT replay: 0.
Memory-layering attempt 3: NOT_AUTHORIZED.

## Exact evidence basis

Selected S1+O2 scope:
puev5691/wellbeing-hq@8a5dc8dffd12a158f6501eacbece46b55a805246:
entities/koordinator/outbox/KOO__shard-checkpoint-option-b-s1o2-nonlive-scope-draft-r01__OPERATOR.md
blob:
30a8444646a84cf8eff7a7941c3b1ca5fa0a70e3

SIS storage fit-gap:
puev5691/wellbeing-hq@e58e40ca1cf478b95a91f611dd64055d3fb6c50e:
entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-storage-profile-fitgap-r01__KOO.md
blob:
cffcd2c9a7531dd0589877d3c31527e94682f33b

KAN accountability card:
puev5691/wellbeing-hq@230e1d6040717217952a27304caab775bdff2751:
entities/kancelar/outbox/KAN__shard-checkpoint-s1o2-accountability-decision-card-r01__KOO-OPERATOR.md
blob:
736bd49c8b199717a8029c758e62df01c96e6d11

Governance successor:
puev5691/wellbeing-hq@63a0e218f9cec36bb2652febd618b104d1aa69e4:
entities/kancelar/outbox/KAN__shard-checkpoint-governance-dedupe-successor-r01-candidate__KOO.md
blob:
799be4e536a2795fae19b489b9887570d614a52a

SIS review:
puev5691/wellbeing-hq@4b4c2c5697548b7e95683bd8246cc164420db8ef:
entities/sisadmin/outbox/SIS__shard-checkpoint-governance-dedupe-successor-r01-review__KOO.md
blob:
67fe653dbbc234fbaedc971c3ca3a92d6c76a987

ARH review:
puev5691/wellbeing-hq@98ac810a67efdddc848779be90708397a3961193:
entities/archivarius/outbox/ARH__shard-checkpoint-governance-dedupe-successor-r01-review__KOO.md
blob:
80cdd7dd277d37472d586ce15a098ed57c50fc4d
terminal:
PASS_ARH_SHARD_CHECKPOINT_GOVERNANCE_DEDUPE_SUCCESSOR_R01_WITH_BOUNDARIES

Corrected KOD interface:
puev5691/wellbeing-hq@ea632cd672994fc7ce6356d77a9fcb7c56854702:
entities/koder/outbox/KOD__shard-checkpoint-s1o2-operation-dedupe-correction-r01.md
blob:
085d13164487b18569b28d1ab6a589b63d0a4118

## Common mandatory contract for every option

These requirements are VERIFIED_FROM_DOCUMENTS as design requirements, not runtime capability.

### Object and pointer

- checkpoint object is immutable/content-addressed;
- current pointer is a separate state transition;
- PUT_IMMUTABLE does not advance current;
- COMMIT_CURRENT_CAS atomically compares exact expected tuple;
- orphan object without successful pointer CAS is not current.

### PUT/CAS dedupe and lost ack

- PUT dedupe domain:
  {namespace, task_revision_ref, PUT_IMMUTABLE, request_id};
- CAS dedupe domain:
  {namespace, task_revision_ref, COMMIT_CURRENT_CAS, cas_request_id};
- identical payload in same operation domain may return persisted prior outcome;
- different payload with same operation-qualified key is conflict;
- lost PUT/CAS ack is reconciled separately;
- absence of a record is not durable NOT_COMMITTED proof;
- blind retry is forbidden.

### Ack / readback

- durable ack must bind exact operation, payload/tuple, transaction token, principal, durability profile and evidence;
- PUT ack does not prove CAS;
- CAS ack does not prove stored object bytes;
- independent object readback and pointer readback are distinct;
- submitted buffer/cache is not independent readback.

### Authority

- storage capability does not appoint writer;
- fence/lease does not appoint writer;
- durable bytes do not grant resume;
- recovery eligibility, ARH preservation, initiation, Writer Gate and processing_started remain separate.

### Retention / recovery

Required graph includes at least:
- immutable object bytes;
- current pointer state/provenance;
- PUT outcomes;
- CAS outcomes;
- operation payload digests;
- transaction IDs;
- dedupe records/tombstones;
- epoch/fence lineage;
- authoritative durable negative proof where used;
- manifest/dependency refs;
- task/writer/authority refs required to interpret the checkpoint.

A checkpoint cannot outlive the dependencies required to interpret or safely resume it.

## Comparative storage contract card

### Option M1 — one durable storage failure-domain + separate independent readback path + backup

Model:
one selected persistent storage failure-domain is authoritative for object/pointer/operation journal commit. Independent readback must use a separately controlled read path, but physical durability remains one failure-domain. Backup is a distinct recovery mechanism, not a synchronous replica.

Documentary status:
PROPOSED_FOR_DECISION.

What is supported by current documents:
- a contract may define an explicit limited failure profile;
- one failure-domain can only support a durable claim if that exact limited profile is approved;
- backup, readback and live storage are separate evidence;
- D1 must state allowed failures explicitly;
- loss outside the approved profile must fail closed.

What this model can potentially establish:
- process crash durability;
- service restart durability;
- object/pointer persistence within one approved storage domain;
- independent exact-byte verification if read path/control is genuinely separate.

What it cannot claim without additional measures:
- survival of total loss/corruption of the one durability domain;
- zero-loss continuity across domain loss;
- multi-domain partition tolerance.

Required ack evidence:
- persistent commit token for PUT/CAS operation;
- exact operation payload/outcome journal;
- proof that commit reached the defined durable medium before ack;
- operation-specific StorageAck;
- independent object/pointer readback.

Backup/restore:
- backup must include object/pointer + operation/dedupe/fence/dependency lineage;
- restore only to isolated location first;
- old restored epoch never auto-promoted;
- restore proof separate from live readback.

Failure behavior:
- storage domain unavailable => UNAVAILABLE/STOP;
- domain corruption => BLOCKED_INTEGRITY;
- loss of live domain => restore path required; no claim of current continuity until reconciliation.

Advantages:
- smallest conceptual/operational contract;
- easiest future negative-test surface;
- clear separation between durability and disaster recovery.

Costs/limits:
- weaker failure tolerance;
- backup cadence may dominate RPO;
- recovery procedure may dominate RTO;
- one domain remains a correlated failure boundary.

Unknown:
- whether such limited failure tolerance is acceptable to OPERATOR;
- exact durable medium/domain;
- backup interval;
- RPO/RTO;
- readback principal separation.

D1-D9 fit:
possible in principle only if D1 explicitly excludes total domain loss from guaranteed durability and D7/D8 prove backup/restore/restart behavior.

### Option M2 — synchronous replicated commit across independent failure-domains

Model:
PUT object and CAS/pointer journal are acknowledged only after the selected synchronous replication/commit rule has been satisfied across separately defined failure domains. The operation journal/dedupe/fence lineage receives the same or explicitly compatible durability guarantee.

Documentary status:
PROPOSED_FOR_DECISION.

What is supported by current documents:
- D1 requires explicit failure domains and commit/replication rule;
- same-disk copies do not count as independent durability;
- replica count by itself is not semantic authority;
- CAS/fencing still determines current successor;
- split-brain remains BLOCKED_CONFLICT.

Required ack evidence:
- exact list/class of participating failure domains or verifiable quorum evidence;
- operation-specific transaction identity;
- proof selected commit rule completed before ack;
- durable persisted dedupe outcome;
- exact object/pointer readback through independently authorized verifier.

Pointer/CAS:
- only one successor;
- quorum/replication must not weaken exact expected-tuple CAS;
- stale epoch remains fenced;
- divergent heads are conflict, not majority-by-timestamp or last-write-wins.

Backup/restore:
still required unless OPERATOR explicitly defines otherwise.
Replication is not backup and does not replace isolated restore verification.

Failure behavior:
- failures inside approved tolerance => service may remain available only if exact commit/read rules remain satisfied;
- insufficient quorum / ambiguous partition => STOP/UNAVAILABLE;
- divergent accepted heads => BLOCKED_CONFLICT;
- corruption requires exact digest/readback reconciliation.

Advantages:
- can support stronger durability against selected domain failure;
- backup cadence need not be the only determinant of recent-state loss.

Costs/limits:
- more complex commit evidence;
- harder failure-domain independence proof;
- partition/quorum semantics become part of correctness;
- CAS/dedupe journal must be at least as durable as object data;
- more negative cases needed under D8.

Unknown:
- required number/type of failure domains;
- quorum/replication rule;
- acceptable write unavailability during partition;
- actual domain independence;
- numeric RPO/RTO.

D1-D9 fit:
potentially strongest straightforward durability profile, but only after exact replication/failure assumptions and D8 partition/concurrency evidence are separately approved and proven.

### Option M3 — separated immutable-object plane and transactional pointer/operation-journal plane

Model:
immutable checkpoint objects live in one durable object plane; current pointer, CAS, generation/epoch, operation-dedupe journal and durable negative-proof records live in a separate transactional control plane. Each plane may itself be single-domain or replicated; that is a second decision dimension.

Documentary status:
PROPOSED_FOR_DECISION.

What is supported by current documents:
- corrected KOD interface already separates immutable PUT from current-pointer CAS;
- governance explicitly states put+CAS atomic boundary is UNKNOWN and success of one cannot imply the other;
- orphan objects are permitted evidence;
- operation-specific reconciliation can distinguish object-only vs pointer committed.

Required ack evidence:
PUT side:
- object commit token;
- object/checkpoint digest;
- PUT operation journal outcome;
- object durable ref.

CAS side:
- exact expected/successor tuple;
- CAS transaction token;
- pointer state;
- CAS operation journal outcome.

Independent readback:
- object bytes checked from object plane;
- pointer/current tuple checked independently from control plane;
- neither proof may substitute for the other.

Cross-plane reconciliation:
must explicitly support:
- object recorded / pointer not committed => orphan;
- pointer cannot validly commit a missing/unreadable object;
- lost ack resolved per plane;
- both confirmed before CHECKPOINT_DURABLE;
- no blind compensation or inferred CAS from object existence.

Backup/restore:
- both planes and their linkage must be backed up/preserved;
- restoration order and consistency point must be defined;
- restored pointer must never reference missing or incompatible object/dependency lineage;
- old control-plane epoch cannot become current automatically.

Failure behavior:
- object plane unavailable but pointer available => STOP;
- pointer plane unavailable but object available => object remains non-current evidence;
- cross-plane mismatch => BLOCKED_INTEGRITY/CONFLICT;
- split-brain control plane => freeze namespace.

Advantages:
- maps most directly to corrected PUT/CAS model;
- explicit fault isolation between immutable bytes and mutable current state;
- makes orphan/current distinction mechanically visible.

Costs/limits:
- highest reconciliation complexity;
- cross-plane consistency/backup problem becomes a first-class requirement;
- two trust/failure surfaces to evidence;
- CHECKPOINT_DURABLE requires positive evidence from both.

Unknown:
- whether separation reduces or increases correlated failure for available systems;
- transaction/consistency mechanism between planes;
- backup consistency strategy;
- domain/replication model inside each plane;
- resulting RPO/RTO.

D1-D9 fit:
conceptually the closest match to the corrected interface, but it does not by itself establish stronger durability than M1/M2. Its actual durability is determined by the failure profile chosen for each plane.

## Compact comparison matrix

| Criterion | M1 one durable domain | M2 synchronous multi-domain | M3 separated object/control planes |
|---|---|---|---|
| Current documentary support | Contractually describable | Contractually describable | Contractually describable; closest to KOD interface |
| Concrete backend evidenced | UNKNOWN | UNKNOWN | UNKNOWN |
| Synchronous domain-loss tolerance | Not inherent | Intended design objective, exact bound UNKNOWN | Depends on per-plane profile |
| PUT/CAS separation | Required | Required | Native architectural emphasis |
| Lost-ack reconciliation | Operation journal + readback | Operation journal + quorum/readback | Per-plane operation journals + cross-plane reconciliation |
| Independent readback | Required | Required | Required separately for object and pointer |
| Split-brain complexity | Lower | Higher | High in control plane; cross-plane mismatch added |
| Backup still required | Yes | Yes | Yes, both planes/linkage |
| Restore complexity | Lower | Medium/high | Highest |
| RPO determinant | Backup/commit profile | Replication + backup profile | Worst/interaction of both planes |
| RTO determinant | Restore/restart | quorum recovery/restore | restore/reconcile both planes |
| D8 negative-test burden | Lowest | Higher | Highest |
| Can be selected now | NO | NO | NO |

## Functional roles required by any future profile

These are functional roles, not appointments.

### Write principal

Must prove:
- exact namespace/task authority;
- current writer/delegation where applicable;
- operation and request identity;
- no generic current-state write capability.

Status:
PROPOSED_ROLE.
Actual principal: UNKNOWN.

### Durable ack issuer

Must attest:
- exact operation;
- exact payload/tuple;
- transaction token;
- durability/failure profile;
- retention profile;
- committed/not-committed/unknown outcome;
- sufficient placement/commit evidence.

Must not mint task/writer authority.

Status:
PROPOSED_ROLE.
Actual principal: UNKNOWN.

### Independent readback verifier

Must:
- not rely on writer buffer/put response/cache;
- independently obtain exact object/pointer evidence;
- recompute digest;
- bind readback to operation/transaction/profile;
- preserve verifier identity/evidence.

Independence must be real relative to write path.

Status:
PROPOSED_ROLE.
Actual principal: UNKNOWN.

### Future SIS accountability

SIS operational accountability remains only PROPOSED_FOR_DECISION.

If later appointed under a separate exact decision, SIS role can cover:
- storage service availability/configuration;
- ACL/service-principal implementation;
- failure-domain documentation;
- backup/restore operations;
- monitoring and outage/corruption evidence;
- deployed configuration/version evidence.

It does not authorize SIS to:
- author KOD self-state;
- appoint writer;
- approve retention/privacy policy;
- grant resume authority;
- replace ARH preservation/recovery review.

## Retention graph that must be decided together

A numeric TTL for checkpoint object alone is insufficient.

Any chosen profile must specify retention relationships for:

1. immutable checkpoint object;
2. current pointer/provenance;
3. PUT persisted outcome;
4. CAS persisted outcome;
5. operation payload digests;
6. transaction IDs/tokens;
7. dedupe keys/tombstones;
8. epoch/fence lineage;
9. authoritative durable negative-proof records if relied upon;
10. task/input/dependency refs;
11. manifest/composition needed for recovery;
12. privacy/read/access metadata required to interpret stored evidence.

Minimum documentary invariant:
no dependency required for safe interpretation/recovery may expire before the checkpoint's claimed recoverable interval.

Dedupe/fence evidence must survive long enough that an old request/writer cannot become executable merely because its prevention record expired.

Exact numeric periods:
UNKNOWN.

## Backup and isolated restore requirements

VERIFIED_FROM_DOCUMENTS as design requirements:

- backup is not live replication;
- live replica is not independent readback;
- restore is not automatic promotion;
- restore first goes to isolated location;
- verify bytes/digests/manifest/dependency graph;
- verify transaction/dedupe/fence lineage;
- reconcile against current writer/epoch/authority;
- older epoch/generation restored from backup remains historical until explicit reconciliation;
- missing dedupe/fence lineage blocks safe recovery;
- privacy/read/key availability required by recovery must be part of restore evidence.

Still UNKNOWN:
- backup technology;
- backup cadence;
- retention;
- number/location of copies;
- restore target;
- restore throughput;
- RPO/RTO.

## Evidence needed before proposing numeric retention

To propose a defensible retention period, need at least:

1. maximum legitimate resume/recovery window for S1;
2. maximum permitted period between checkpoint creation and promotion/final closure;
3. longest period in which duplicate/lost-ack reconciliation may still occur;
4. maximum lifetime of writer/fence lineage needed to reject stale actors;
5. dependency availability/retention constraints;
6. privacy/legal/project retention upper bounds;
7. backup/restore verification cadence;
8. whether historical forensic evidence is required after task closure.

Until these are evidenced/decided:
retention = UNKNOWN.

## Evidence needed before proposing RPO

Need first define the loss event.

For each selected failure class:
- process crash;
- host loss;
- storage-device loss;
- failure-domain loss;
- partition;
- control-plane corruption;
- backup-site loss;

must know:
- what synchronous commit guarantees are required;
- what state may legally be lost;
- whether an acknowledged current pointer may ever be lost;
- replication/backup cadence;
- whether operation/dedupe/fence journal has same RPO as object/pointer.

If requirement is "no acknowledged CHECKPOINT_DURABLE may be lost for selected failure class", then the durability profile must prove that directly; an RPO number alone cannot compensate for an ack that promised stronger durability.

Numeric RPO:
UNKNOWN.

## Evidence needed before proposing RTO

Need:
- selected outage/failure classes;
- required availability during partition;
- restore source/location;
- expected checkpoint/dependency volume;
- verification/readback workload;
- key/ACL restoration procedure;
- namespace conflict/fence reconciliation steps;
- whether KOD may wait for GitHub/preservation dependencies;
- operational staffing/activation mechanism.

Numeric RTO:
UNKNOWN.

## Evidence needed before selecting allowed failures

First decision input needed:

**S1 failure objective**:
Which exact failures must an acknowledged checkpoint survive without loss of object/current state?

Candidate classes to decide, not recommendations:
- process/service restart only;
- host restart/loss;
- local storage-device loss;
- one complete storage failure-domain loss;
- network partition while preserving safety but allowing unavailability;
- corruption detected before read/resume;
- simultaneous classes, if required.

For each selected class OPERATOR must also decide whether:
- availability may stop to preserve safety;
- acknowledged current checkpoint may be lost;
- restore from backup is acceptable vs synchronous survival required.

Without this, models M1/M2/M3 cannot be ranked objectively.

## Failure behavior common to all options

Lost PUT/CAS ack:
operation-specific ResolveRequest/readback; UNKNOWN/STOP if unresolved; no blind retry.

Orphan:
immutable object without pointer commit remains non-current evidence.

Corrupted object/dependency:
BLOCKED_INTEGRITY; no resume.

Stale writer:
FENCED; availability/credential does not restore authority.

Concurrent CAS:
exactly one current successor; others conflict/fenced.

Partition/split-brain:
BLOCKED_CONFLICT/freeze when unique current cannot be proven; no last-write-wins.

Shard unavailable:
UNAVAILABLE/STOP; do not invent checkpoint.

Old backup:
isolated restore; no automatic current promotion.

Expired dependency:
BLOCKED_RECOVERY_ELIGIBILITY.

Unknown external side effect:
BLOCKED_EFFECT_RECONCILIATION; cursor never authorizes blind replay.

## D1–D9 fit-gap common to all options

D1:
PROPOSED / incomplete.
Need selected model, owner appointment, trust/failure domains, commit rule, retention/read access.

D2:
BLOCKED for execution.
No actual S1 execution task/writer/delegate/principal admitted.

D3:
PROPOSED.
Immutable object/interface designed; exact implemented schema/canonicalizer/object absent.

D4:
BLOCKED.
No storage implementation or persistent commit evidence.

D5:
BLOCKED.
No actual operation-specific independent readback.

D6:
PROPOSED, runtime BLOCKED.
CAS/dedupe/fence contract coherent; no deployed proof.

D7:
PROPOSED, incomplete.
Retention/backup/restore graph identified; numeric profile and proof absent.

D8:
BLOCKED.
No separately authorized implementation negative suite on deployed version.

D9:
BLOCKED.
No actual checkpoint object/ack/readback provenance exists.

Therefore:
CHECKPOINT_DURABLE remains NOT_ESTABLISHED under every option.

## Recommendation

recommendation:
UNKNOWN / NOT_YET_GROUNDED.

Reason:
current evidence defines correctness requirements but does not define the failure objective that the chosen storage profile must satisfy, nor any backend capabilities/costs against that objective.

It would be unsound to recommend M1, M2 or M3 merely from architectural taste.

## First missing verifiable fact / smallest next non-live step

First missing decision/evidence:

**exact S1 failure objective and acknowledgement promise**.

A bounded next non-live decision card should ask OPERATOR to select, for S1 only:
- which failure classes must a positively acknowledged checkpoint survive;
- whether safety may require unavailability;
- whether loss of an acknowledged checkpoint is ever acceptable;
- whether recovery from backup is sufficient for a class or synchronous survival is required.

After that human requirement is fixed, a separately authorized SIS discovery can compare available backend/failure-domain capabilities against the chosen objective without yet deploying anything.

Only then can evidence-grounded numerical RPO/RTO/retention alternatives be prepared.

This result does not activate that next step.

## Boundary accounting

Backend selected: NO
Host selected: NO
Operational owner appointed: NO
Numeric retention chosen: NO
RPO chosen: NO
RTO chosen: NO
Failure tolerance chosen: NO
Code/tests: 0
Host/shard access: 0
Shard WRITE: 0
Secrets: 0
Provider calls: 0
Automation changes: 0
Project Sources/canon mutation: 0

Governance candidate:
CANDIDATE_NOT_ACTIVE

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

Resume authority:
NOT_GRANTED

Memory-layering attempt 3:
NOT_AUTHORIZED

Historical PROMPT replay:
0

## EXPERIENCE

Идея → сравнить не продукты и серверы, которых evidence ещё не поддерживает, а сами durability contracts.

Проба → разложить S1 requirements на три модели: one-domain durability, synchronous multi-domain durability и separated object/control planes.

Результат → все три модели можно описать без выдумки, но ни одну нельзя обоснованно предпочесть без exact failure objective; численные retention/RPO/RTO зависят от того, какую потерю и какой простой ОПЕРАТОР считает допустимыми.

Вердикт → comparative decision input готов; recommendation остаётся UNKNOWN.

Урок → storage architecture нельзя выбирать раньше failure objective. Иначе сначала строят дорогую крепость, а потом выясняют, что защищали сарай. Или наоборот, что тоже по-своему бодрит.

## Terminal

PASS_SIS_S1O2_STORAGE_DURABILITY_PROFILE_OPTIONS_R01_DOCUMENT_ONLY

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
