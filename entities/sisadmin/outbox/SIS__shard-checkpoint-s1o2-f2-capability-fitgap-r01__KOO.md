# SIS → KOO: S1+O2 F2 capability fit-gap r0.1

terminal: PASS_SIS_S1O2_F2_CAPABILITY_FITGAP_R01_DOCUMENT_ONLY
scope: ONE_BOUNDED_NONLIVE_DOCUMENT_REVIEW
project_time: omitted

governance_candidate: CANDIDATE_NOT_ACTIVE
CHECKPOINT_DURABLE: NOT_ESTABLISHED
resume_authority: NOT_GRANTED
operational_owner: NOT_APPOINTED
memory_layering_attempt_3: NOT_AUTHORIZED

## Человеческий смысл

ОПЕРАТОР зафиксировал F2: будущий положительно подтверждённый S1 checkpoint должен переживать полную потерю одного независимо проверенного storage failure domain без потери уже подтверждённых:
- immutable checkpoint object;
- принятого current-pointer перехода;
- PUT/CAS operation outcomes;
- dedupe/fence/transaction lineage, необходимой для доказательства состояния.

При этом безопасность важнее доступности: при partition, недостаточном quorum или неоднозначном current система вправе прекратить новые acknowledgements и STOP.

Из этого решения следует важный архитектурный отсев.

M1 в исходном виде — один durable failure domain + independent readback + backup — F2 НЕ удовлетворяет, потому что потеря единственного durability domain оставляет только eventual backup recovery. F2 требует не потерять уже acknowledged state при такой потере.

M2 — synchronous commit across independently verified failure domains — документально подходит как возможный pattern, но capability не доказана. Нужны независимые evidence физической/административной независимости domains и synchronous durability не только object bytes, но pointer/CAS/outcome/fence lineage.

M3 — separated object plane + transactional pointer/control plane — также может удовлетворить F2, но только если каждый plane, необходимый для признания checkpoint current/durable, сам переживает одну domain loss и cross-plane lineage остаётся доказуемой после отказа. Простое разделение planes F2 не создаёт.

В репозитории нет доказательства работающей F2-системы. Исторический mazhor gateway остаётся VERIFY-only read-only evidence и ничего не доказывает о multi-domain WRITE/durability.

## Resume-First / authority

Exact KOO task:
puev5691/wellbeing-hq@dc353d2a885eca461f1a3878d31ca22652f1c58e:
entities/koordinator/outbox/KOO__shard-checkpoint-s1o2-f2-capability-fitgap-r01__SIS.md
blob:
87cbe5fe80675687e3b0c3e57cbd23af35015ac4

Authority:
AUTHORIZE_SIS_S1O2_F2_CAPABILITY_FITGAP_R01_DOCUMENT_ONLY

Exact F2 decision:
puev5691/wellbeing-hq@8dc6da614f75ea9c3a3e322b6c5a5168acfea050:
entities/koordinator/outbox/KOO__s1o2-f2-failure-objective-decision-r01__OPERATOR.md
blob:
8115ed76e0c8953e80426f89a7d52747e1763bf7

Fresh HQ HEAD before result:
dc353d2a885eca461f1a3878d31ca22652f1c58e

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

No newer competing SIS writer, superseding F2 task, conflicting F1/F2 decision or competing SIS terminal was found at the execution boundary.

Approved Project Sources loaded and exact blobs matched:
- project core v2.5 — a42f7dca6a7469a54fa2da24aae0da4e549c9d33;
- roles v2.4 — 1772339cb74dae8550bfbd2e33401c34a929e911;
- recovery v1.6 — 233117e1c9509d730e1f5ec532b1cabe3f786609;
- file-work v2.4 — e9c29d62057f34e4f771d6057a36d9b7f72e74c2;
- source-loading v2.2 — 69eb657f260a019f76e8e707c880ea88c1dfa0bf;
- task-conveyor v1.2 — df7896d867eeeffff506319538fedad938856686.

Historical PROMPT replay: 0.

## Exact evidence reconciled

S1+O2 scope:
puev5691/wellbeing-hq@8a5dc8dffd12a158f6501eacbece46b55a805246
blob 30a8444646a84cf8eff7a7941c3b1ca5fa0a70e3.

SIS storage fit-gap:
puev5691/wellbeing-hq@e58e40ca1cf478b95a91f611dd64055d3fb6c50e
blob cffcd2c9a7531dd0589877d3c31527e94682f33b.

SIS M1/M2/M3 options:
puev5691/wellbeing-hq@8cda2ace78d6e27d4d9ada3344d5e2f3af6ca274
blob 3641bce5e40d73677f22e48903e8c6b72b709d08.

Corrected KOD operation interface:
puev5691/wellbeing-hq@ea632cd672994fc7ce6356d77a9fcb7c56854702
blob 085d13164487b18569b28d1ab6a589b63d0a4118.

Accountability card:
puev5691/wellbeing-hq@230e1d6040717217952a27304caab775bdff2751
blob 736bd49c8b199717a8029c758e62df01c96e6d11.

Governance successor:
puev5691/wellbeing-hq@63a0e218f9cec36bb2652febd618b104d1aa69e4
blob 799be4e536a2795fae19b489b9887570d614a52a
status CANDIDATE_NOT_ACTIVE.

SIS review:
blob 67fe653dbbc234fbaedc971c3ca3a92d6c76a987.

ARH review:
blob 80cdd7dd277d37472d586ce15a098ed57c50fc4d.

## Status vocabulary

VERIFIED_FROM_DOCUMENTS:
explicitly supported by repository evidence as a requirement or observed historical property.

PROPOSED:
coherent design pattern or rule, not implemented capability.

UNKNOWN:
not evidenced and not selected.

BLOCKED:
current evidence is insufficient for a positive F2 or D1–D9 claim.

## Existing capability inventory

| Capability / fact | Status | Evidence |
|---|---|---|
| Existing mazhor gateway is checkpoint WRITE backend | BLOCKED | Historical gateway is VERIFY-only, read-only, WRITE disabled. |
| Existing mazhor gateway proves multiple independent failure domains | BLOCKED | No such evidence exists. |
| Existing gateway proves synchronous multi-domain commit | BLOCKED | No checkpoint WRITE or replication proof. |
| Existing gateway proves object/pointer CAS durability | BLOCKED | No checkpoint object store/current pointer implementation. |
| Exact operation-qualified PUT/CAS contract | VERIFIED_FROM_DOCUMENTS | Corrected KOD interface defines separate PUT/CAS request domains, outcomes and ResolveRequest semantics. |
| Lost-ack fail-closed semantics | VERIFIED_FROM_DOCUMENTS | UNKNOWN/STOP without operation-specific durable proof; no blind retry. |
| D1–D9 requirement set | VERIFIED_FROM_DOCUMENTS | Governance successor + SIS/ARH reviews. |
| Actual D1–D9 runtime compliance | BLOCKED | No implementation/deployed verification. |
| Failure-domain identity/independence | UNKNOWN | No selected topology or independent domain evidence. |
| Numeric quorum/replica count | UNKNOWN | Not selected and not inferable. |
| Numeric RPO/RTO | UNKNOWN | Not selected and not inferable. |
| Backup cadence / retention | UNKNOWN | Not selected and not inferable. |
| Operational owner | UNKNOWN / NOT_APPOINTED | O2 is a design shape only. |

## F2 minimum semantics

A future positive F2 ack can be accepted only if, after total loss of one selected independently verified storage failure domain, the system can still independently demonstrate all of the following without reconstructive guessing:

1. exact acknowledged immutable checkpoint object still exists and matches digest;
2. exact accepted current-pointer transition remains provable;
3. exact PUT outcome remains provable;
4. exact CAS outcome remains provable;
5. dedupe operation records/tombstones required to prevent replay remain provable;
6. epoch/fence lineage required to reject stale writer remains provable;
7. transaction IDs/payload digests/provenance required to bind these facts remain provable;
8. required manifest/dependency refs remain available for the claimed recoverable interval;
9. no divergent current head is silently selected;
10. a surviving system may STOP rather than acknowledge if the above cannot be proven.

Backup restoration after loss may support disaster recovery but cannot retrospectively satisfy the no-loss promise for already acknowledged state if the acknowledged current state was absent after the selected domain failed.

## M1 fit against F2

M1:
one durable storage failure domain + separate independent readback path + backup.

### Verdict
BLOCKED_FOR_F2_AS_DEFINED.

### Why
The single durability domain is itself the selected loss event. If it is totally lost, current acknowledged object/pointer/outcome/fence lineage can only survive if an additional synchronous independent durability domain existed before ack. Once such a synchronous second domain is required, the model is no longer M1 in its original form.

Independent readback does not create another durable copy.
Backup-only eventual restore does not prove no loss of acknowledged state.

### What remains useful from M1
VERIFIED_FROM_DOCUMENTS / PROPOSED:
- independent readback separation;
- backup/isolated restore requirements;
- fail-closed corruption/unavailable behavior;
- retention/dependency rules.

### Evidence needed to remove BLOCKED
Not a test of M1. A design change is needed:
introduce at least one additional independently verified durability domain into the acknowledged commit path for every F2-critical state class.

At that point the result should be classified under M2 or an M3 profile with qualifying per-plane replication.

## M2 fit against F2

M2:
synchronous commit across independently verified storage failure domains.

### Verdict
PROPOSED_F2_CAPABLE_PATTERN / CAPABILITY_UNPROVEN.

M2 is the most direct abstract match to F2, but no current repository evidence establishes an implementation.

### Required physical failure-domain evidence

UNKNOWN now.

Minimum future evidence:
- explicit domain definition;
- inventory of components assigned to each domain;
- proof that the domains do not share the selected failure cause;
- physical dependencies relevant to F2, e.g. storage media/controller/host/power/rack/site as applicable to chosen boundary;
- failure injection or independently witnessed loss of one domain after positive ack with state preserved elsewhere.

No particular domain boundary is chosen here.

### Required administrative independence evidence

UNKNOWN now.

Need:
- named write/ack/readback principals;
- ACLs/service identities;
- proof one compromised or failed administrative principal/domain cannot silently fabricate both sides of an "independent" durability/readback claim where the selected trust profile requires separation;
- audit/provenance identities for each participant.

Administrative separation requirement itself must be selected in D1.

### Required synchronous commit evidence

BLOCKED today.

For every positive ack:
- exact operation transaction/token;
- proof commit rule satisfied across the required independent domains before ack issuance;
- ack tied to durability profile version;
- exact placement/quorum evidence;
- no acknowledgement from queue/buffer/cache alone.

### F2-critical state that must share qualifying durability

At minimum:
- immutable object bytes/digest;
- current pointer/current-transition evidence;
- PUT persisted outcome;
- CAS persisted outcome;
- operation payload digests;
- transaction IDs;
- dedupe/tombstone evidence needed during recovery/retry window;
- generation/epoch/fence lineage.

If any of these lives only in one failure domain, F2 fails even if object bytes are replicated.

### PUT/CAS semantics

PROPOSED and coherent.

Need future runtime evidence:
- PUT ack after required multi-domain object durability;
- CAS ack after required multi-domain pointer/journal durability;
- operation-specific ResolveRequest surviving one domain loss;
- PUT proof never substitutes for CAS proof.

### Independent readback

PROPOSED, runtime UNKNOWN.

Need:
- readback of object via surviving domain/path after one-domain loss;
- pointer/CAS state readback via surviving qualified domain/path;
- digest/transaction/profile binding;
- verifier identity;
- no writer buffer/cache reuse.

### Partition behavior

VERIFIED_FROM_DOCUMENTS as requirement:
safety may STOP and refuse ack.

Runtime capability:
BLOCKED.

Need:
- proof insufficient quorum/ambiguous pointer prevents new positive ack;
- proof no last-write-wins/timestamp resolution;
- proof stale writer/fenced epoch cannot commit.

### F2 conclusion for M2

Contractually compatible with F2.
Implementation capability remains UNKNOWN/BLOCKED pending independently verified domains and runtime evidence.

## M3 fit against F2

M3:
separated immutable-object plane and transactional pointer/operation-journal plane.

### Verdict
PROPOSED_F2_CAPABLE_ONLY_IF_EACH_NECESSARY_PLANE_MEETS_F2.

Separation itself is not durability.

### Object plane requirement

Must survive one selected failure-domain loss without losing:
- acknowledged checkpoint bytes;
- checkpoint digest;
- PUT operation outcome and transaction identity, unless those are deliberately in control plane with equal F2 guarantee.

If object plane is single-domain with backup only:
F2 FAIL/BLOCKED.

### Control plane requirement

Must survive one selected failure-domain loss without losing:
- accepted current pointer;
- exact CAS outcome;
- generation;
- epoch/fence lineage;
- dedupe/tombstones;
- transaction/payload provenance;
- authoritative negative proof relied upon.

If control plane is single-domain:
F2 FAIL/BLOCKED even if object bytes survive.

### Cross-plane reconciliation requirement

After one domain loss system must still prove:
- object referenced by current pointer exists and is intact;
- pointer points to exact intended object;
- PUT and CAS outcomes belong to exact operations;
- orphan object is not current;
- no surviving branch ambiguity.

Cross-plane mismatch:
BLOCKED_INTEGRITY / BLOCKED_CONFLICT / STOP.

### Independent evidence required

- per-plane failure-domain map;
- proof chosen F2 loss does not simultaneously eliminate all qualifying copies from either required plane;
- per-plane synchronous ack/commit evidence;
- exact cross-plane linkage evidence;
- independent readback for both object and pointer;
- operation journals retained and restorable consistently;
- one-domain loss drill showing surviving consistent pair without inferred state.

### M3 conclusion

Potentially F2-compatible.
More complex proof burden than M2 because both per-plane durability and cross-plane consistency must be independently established.

## Compact M1/M2/M3 F2 matrix

| Criterion | M1 | M2 | M3 |
|---|---|---|---|
| Survive one total durability-domain loss without acknowledged-state loss | BLOCKED | PROPOSED capable | PROPOSED capable only with F2 per required plane |
| Existing deployed evidence | NONE | NONE | NONE |
| Requires independent failure domains in ack path | Not in original model -> fails F2 | Yes | Yes, for every critical plane |
| PUT/CAS operation-specific durability | Can be designed but one-domain loss breaks promise | Required across F2 domains | Required per relevant plane |
| Independent object/pointer readback | Required | Required | Required separately per plane |
| Lost-ack durable reconciliation after one-domain loss | Not guaranteed | Required | Required per plane + cross-plane |
| Partition safety STOP | Compatible | Required | Required |
| Backup still required | Yes | Yes | Yes |
| Backup alone meets F2 | NO | NO | NO |
| D8 proof burden | Lower but cannot satisfy F2 | High | Highest |
| Backend choice justified now | NO | NO | NO |

## Fit-gap by capability

### 1. Failure-domain definition and independence

Status:
UNKNOWN.

Need separately checkable evidence:
- exact F2 domain boundary definition;
- component/dependency inventory;
- common-mode dependency analysis;
- independent review of claimed separation;
- later separately authorized failure-domain loss verification.

No domain names or topology inferred.

### 2. Synchronous durability of immutable object

Status:
BLOCKED runtime / PROPOSED contract.

Need:
- exact ack rule;
- proof all required copies/domains reached durable commit before ack;
- transaction identity;
- post-loss exact-byte readback from survivor;
- digest/profile match.

### 3. Synchronous durability of current pointer / CAS

Status:
BLOCKED runtime / PROPOSED contract.

Need:
- atomic expected-tuple CAS;
- pointer/current journal durability meeting F2;
- surviving evidence after one-domain loss;
- exactly one current successor;
- stale/fenced writer rejection.

### 4. PUT/CAS outcomes and dedupe journal

Status:
PROPOSED contract / BLOCKED runtime.

Need:
- operation-qualified durable journal;
- payload digest binding;
- outcome durability in F2-qualified domains;
- tombstone/dedupe retention;
- post-loss ResolveRequest evidence.

### 5. Generation / epoch / fencing

Status:
PROPOSED semantics; issuer UNKNOWN; runtime BLOCKED.

Need:
- named/authorized issuer;
- durable epoch/generation lineage surviving one-domain loss;
- fencing rule verified across partition/restart;
- stale writer rejection evidence.

Storage availability/token never creates writer authority.

### 6. Lost ack / authoritative negative proof

Status:
PROPOSED; implementation UNKNOWN.

Need:
- durable operation journal query;
- proof negative result is authoritative under one-domain loss;
- proof missing record does not become NOT_COMMITTED;
- object/pointer readback;
- no blind retry.

### 7. Independent readback

Status:
PROPOSED; runtime UNKNOWN.

Need:
- independently controlled read path;
- exact reader identity;
- object and pointer readback separate;
- transaction/profile provenance;
- post-domain-loss readback from surviving qualified state.

### 8. Partition / quorum / split-brain

Status:
STOP semantics VERIFIED_FROM_DOCUMENTS;
runtime enforcement BLOCKED.

Need:
- selected quorum/commit rule;
- proof partition with insufficient certainty causes refusal of positive ack;
- proof no timestamp/LWW;
- divergent heads retained as conflict;
- reconciliation procedure and authority.

Numeric quorum remains UNKNOWN.

### 9. Backup / isolated restore

Status:
VERIFIED_FROM_DOCUMENTS as requirement;
capability UNKNOWN.

Need:
- backup contains object + pointer + operation journal + dedupe/fence + manifest/dependencies;
- isolated restore procedure;
- digest/provenance verification;
- old epoch not auto-promoted;
- missing lineage causes STOP.

Backup remains required even for M2/M3, but does not satisfy F2 no-loss ack promise by itself.

### 10. Dependency retention

Status:
PROPOSED; numeric values UNKNOWN.

Need:
- complete dependency graph;
- recovery/resume window requirement;
- dedupe/fence/negative-proof retention requirement;
- privacy/legal upper bounds;
- evidence required dependency cannot expire before checkpoint's recoverable interval.

### 11. Privacy/read scope

Status:
UNKNOWN / decision required.

Need:
- data classes;
- read principals;
- independent verifier access scope;
- backup/restore visibility;
- redaction/publication rules;
- delete/hold authority.

F2 does not override privacy authority.

## D1–D9 reconciliation under F2

D1 — durability contract:
BLOCKED.
F2 now supplies one important requirement: survival of one independently verified domain loss. Still missing domain definition, commit rule/topology, operational owner, principals, retention/privacy.

D2 — caller/task/writer authority:
BLOCKED for execution; unchanged by F2.
F2 is storage durability objective, not WRITE authority.

D3 — immutable object/context:
PROPOSED coherent; implementation absent.

D4 — storage commit evidence:
BLOCKED.
F2 raises the bar: positive ack must demonstrate qualifying multi-domain durability for every required state class.

D5 — independent readback:
BLOCKED runtime.
Future readback must remain possible/provable after one selected domain loss.

D6 — CAS/generation/dedupe/fencing:
PROPOSED coherent / BLOCKED runtime.
F2 requires this lineage itself to survive the domain loss.

D7 — retention/backup/restore:
PROPOSED / incomplete.
F2 does not set numeric retention, RPO/RTO or backup cadence. Backup remains distinct from synchronous survival.

D8 — deployed-version negative verification:
BLOCKED.
Future separately authorized tests must include actual one-domain total-loss scenario, partition/quorum behavior, concurrent CAS, lost ack, stale fence, corruption and restore.

D9 — object-specific provenance:
BLOCKED.
No actual object/ack/readback exists.

Therefore:
CHECKPOINT_DURABLE remains NOT_ESTABLISHED.

## Exact OPERATOR decisions still required

F2 has resolved only the failure objective at the abstract level.

Still requires human/normative selection of:
- what constitutes one independently verified storage failure domain for S1;
- whether administrative independence is required in addition to physical independence and to what degree;
- acceptable safety/availability trade under partition;
- whether M2-style unified multi-domain durability or M3-style separated planes is preferred after evidence;
- operational owner appointment;
- privacy/read scope;
- retention policy;
- later implementation/test authority.

Must remain UNKNOWN until grounded:
- backend/product;
- host;
- topology;
- replica count;
- quorum;
- numeric RPO;
- numeric RTO;
- backup cadence;
- TTL/retention periods.

## First smallest separately authorizable nonlive next step

A bounded **capability evidence discovery**, still document/read-only:

For a small set of candidate storage capability classes already available or realistically deployable in the project environment, gather evidence for:
1. what exact physical/administrative failure domains each class can expose;
2. whether acknowledged write can be synchronously durable across independently verified domains;
3. whether atomic CAS/conditional update is supported for current pointer;
4. whether operation-result/dedupe/fence journal can receive the same F2 durability;
5. whether independent post-loss object and pointer readback is possible;
6. what documented partition/quorum safety behavior exists;
7. what backup/isolated-restore primitives exist.

This would be capability discovery only, not backend selection, host access, deployment or benchmark.

Until separately authorized, it is only a proposed next step.

## Boundary accounting

Backend selected:
NO

Host selected:
NO

Topology selected:
NO

Operational owner appointed:
NO

Replica/quorum selected:
NO

Numeric retention/RPO/RTO selected:
NO

Code/tests:
0

Host/shard access:
0

Shard WRITE:
0

Provider calls:
0

Automation:
0

Project Sources/canon mutation:
0

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

Идея → применить выбранный failure objective F2 к абстрактным M1/M2/M3, не превращая архитектурное требование в выдуманную capability.

Проба → проверить, переживёт ли каждый обязательный класс подтверждённого состояния полную потерю одного durability domain.

Результат → M1 в исходном виде F2 не удовлетворяет; M2 — прямой возможный pattern; M3 — возможен только при F2-доказательстве каждого необходимого plane и cross-plane reconciliation. Реализованной F2 capability в repository evidence нет.

Вердикт → документальный fit-gap готов; F2 архитектурно сужает пространство вариантов, но backend/topology всё ещё не выбран.

Урок → реплицировать только payload недостаточно. Если pointer, CAS outcome или fence lineage умирают вместе с одним domain, "durable checkpoint" после аварии превращается в коробку байтов без доказуемого текущего состояния.

## Terminal

PASS_SIS_S1O2_F2_CAPABILITY_FITGAP_R01_DOCUMENT_ONLY

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
