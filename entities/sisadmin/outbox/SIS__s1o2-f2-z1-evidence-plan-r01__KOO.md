# SIS → KOO: S1+O2 F2 Z1 evidence plan r0.1

terminal: PASS_SIS_S1O2_F2_Z1_EVIDENCE_PLAN_R01_DOCUMENT_ONLY
scope: BOUNDED_DOCUMENT_ONLY_EVIDENCE_PLAN
project_time: omitted

Z1_boundary:
SELECT_S1_F2_DOMAIN_Z1_PROVIDER_ZONE_OR_SITE_DESIGN_ONLY

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

F2_Z1_PROOF:
NOT_ESTABLISHED

runtime_test:
NOT_AUTHORIZED

provider_host_access:
NOT_AUTHORIZED

resume_authority:
NOT_GRANTED

Memory-layering_attempt_3:
NOT_AUTHORIZED

## Человеческий смысл

Для Z1 нужно доказать не просто наличие двух VPS или двух IP, а то, что два будущих placement действительно относятся к разным independently verified provider availability zones или physical sites и не разделяют критическую инфраструктуру, которая превращает их в один общий failure domain.

Сейчас такой proof отсутствует.

Имеется только bounded inventory одного mazhor host. Он подтверждает scoped host facts, но ничего не доказывает про:
- provider zone/site identity;
- второй placement;
- cross-zone/site independence;
- shared storage/power/network/control plane;
- гипервизорную/физическую развязку.

Следовательно, до любого future runtime test сначала нужен документированный evidence package о placement/failure-domain identity. Runtime без этого был бы красивой демонстрацией двух серверов, а не доказательством Z1.

## Resume-First / authority

Exact task:
puev5691/wellbeing-hq@6255b39a690fd661b9c3c0c03eb44b07baa7aaf8:
entities/koordinator/outbox/KOO__s1o2-f2-z1-evidence-plan-r01__SIS.md
blob:
547dea3df8e25659f2ea555b9340b62750544f9b

Exact OPERATOR authority:
puev5691/wellbeing-hq@5b3c10b9fe30ed762320649f09edf1c7fdebab3b:
entities/koordinator/outbox/KOO__authorize-SIS-s1o2-f2-z1-evidence-plan-r01__OPERATOR.md
blob:
9fff9c21fecc55ceca5d27f5a48aad416605107c

decision:
AUTHORIZE_SIS_S1O2_F2_Z1_EVIDENCE_PLAN_R01_DOCUMENT_ONLY

Exact Z1 decision:
puev5691/wellbeing-hq@b3c2b5e340d1c9ca96a11e65549b8ea03b084187:
entities/koordinator/outbox/KOO__select-s1-f2-domain-z1-provider-zone-site-design-only__OPERATOR.md
blob:
490ad6e44aa25672d5cbc18f5f5a75c2e07e2c02

Current SIS writer:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md
blob:
05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca

Writer Gate:
writer_gate_pass_replacement_sis_r06_authoritative

Fresh HQ HEAD at execution entry:
18092f1f871bdafe0a39c76c4af701882b7f8ce3

No newer valid SIS writer/handoff/recovery, superseding exact Z1 task or competing SIS Z1 evidence-plan terminal was found.

Approved Project Sources exact blobs matched:
- core v2.5 — a42f7dca6a7469a54fa2da24aae0da4e549c9d33
- roles v2.4 — 1772339cb74dae8550bfbd2e33401c34a929e911
- recovery v1.6 — 233117e1c9509d730e1f5ec532b1cabe3f786609
- file-work v2.4 — e9c29d62057f34e4f771d6057a36d9b7f72e74c2
- source-loading v2.2 — 69eb657f260a019f76e8e707c880ea88c1dfa0bf
- task-conveyor v1.2 — df7896d867eeeffff506319538fedad938856686

Historical PROMPT replay:
0

## Facts already established

### Z1 design boundary

The selected protected failure domain is:

one independently verified provider availability zone or physical site, including all hosts/storage in that zone/site.

The future design must tolerate total loss of one such zone/site without loss of the positively acknowledged required S1 checkpoint state.

This is DESIGN_ONLY.

### Existing mazhor evidence

Exact prior result:
puev5691/wellbeing-hq@4635cbd8b16ed0d9ca58f19d18c511fc10bb111b:
entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-f2-mazhor-nonsecret-host-inventory-r01__KOO.md
blob:
177204daf9093688db49c75749a36bec4f5352fd

What it establishes:
- one verified host identity;
- bounded nonsecret local package/service inventory;
- no verified C1/C2/C3 installation in scoped inventory;
- historical host_inventory metadata/hash match;
- existing gateway VERIFY-only.

What it does NOT establish:
- provider availability zone;
- physical site;
- hypervisor identity;
- storage failure domain;
- second candidate placement;
- cross-zone independence;
- shared power/network/control plane;
- F2 Z1 capability.

## 1. Exact Z1 assertion that must be proven before runtime test

A valid Z1 documentary proof for candidate placements A and B must establish all of the following:

Z1-A:
Placement A belongs to exact provider-defined availability zone or physical site ZA.

Z1-B:
Placement B belongs to exact provider-defined availability zone or physical site ZB.

Z1-C:
ZA != ZB under the provider's own failure-domain semantics, not merely under a human geographic label.

Z1-D:
The storage/state components required for positively acknowledged S1 checkpoint state are placed so that loss of all resources in ZA does not remove the required acknowledged state.

Z1-E:
No required state component silently depends on a shared single failure domain spanning both placements that would invalidate the one-zone/site-loss claim.

Z1-F:
The evidence is current, exact, attributable to the specific resource instances/configuration, and independently read back or cross-checked.

Only after Z1-A through Z1-F have acceptable evidence may a future runtime verification be designed as a Z1 test.

The documentary proof does NOT itself prove runtime survival.

## 2. Evidence that can establish provider zone/site identity

Acceptable evidence classes, strongest first:

### A. Provider authoritative resource metadata

Best case:
provider account/control-plane metadata for the exact resource instance exposes:
- immutable instance/resource ID;
- region;
- availability zone/site/facility identifier;
- placement/failure-domain group if applicable.

Requirements:
- exact resource identity bound to project instance;
- provider-generated value, not caller label;
- readback captured without secrets;
- version/time/context sufficient to know which live resource it refers to.

Status now:
UNKNOWN / not collected.

### B. Provider authoritative documentation plus exact account metadata

Provider documentation defines what a zone/site label means operationally, while account metadata binds each resource to one label.

Both are needed if the provider only exposes a symbolic zone identifier.

Documentation alone does not bind a particular VPS to that zone.
Account label alone does not prove what the label means.

Status:
UNKNOWN / not collected.

### C. Provider invoice/order/resource-placement record

Potentially acceptable if it contains:
- exact instance/resource ID;
- exact zone/site/facility field;
- authoritative provider provenance;
- no ambiguity between marketing location and failure domain.

Marketing city/country labels alone are insufficient.

Status:
UNKNOWN.

### D. Provider support attestation

Can be acceptable if provider transparency is otherwise limited, but only if the attestation:
- identifies exact resources;
- states whether they are in distinct failure domains/sites;
- distinguishes physical site from region/city marketing;
- is retained as immutable evidence.

A vague support statement such as "different servers" is insufficient.

Status:
UNKNOWN.

### E. Host-visible metadata

Host metadata may corroborate provider evidence if it exposes provider-specific zone/site identity through trusted metadata.

It is not sufficient if:
- value is user-configurable;
- it is just hostname;
- it reflects guest config;
- provider semantics are undocumented.

Status:
UNKNOWN.

## 3. Evidence that two placements are actually in different zones/sites

Required evidence should compare exact resource identities, not display names.

Minimum acceptable structure:

Placement A:
- provider/resource ID;
- zone/site ID ZA;
- evidence locator EZA;
- provider semantics reference SZA.

Placement B:
- provider/resource ID;
- zone/site ID ZB;
- evidence locator EZB;
- provider semantics reference SZB.

Comparison:
- ZA != ZB;
- provider states ZA/ZB are independent zone/site failure domains for the relevant service class.

If provider defines zones only for compute but attached storage belongs to a region-wide/shared pool, compute-zone difference alone is insufficient for S1 checkpoint storage Z1.

The proof must cover every component whose loss can destroy or invalidate acknowledged checkpoint state.

## 4. Common dependencies that must be checked or remain UNKNOWN

### Shared storage

Must establish whether A and B depend on:
- same underlying block-storage failure domain;
- same storage cluster;
- same NFS/object gateway;
- same single storage controller/pool;
- same snapshot/backup service if required by the claim.

If provider does not disclose this sufficiently:
SHARED_STORAGE_DEPENDENCY = UNKNOWN.

Unknown critical shared storage blocks a strong Z1 storage-independence claim.

### Shared physical host / hypervisor

Where provider exposes placement/anti-affinity/host IDs, check whether A and B can co-reside on the same physical host.

If not knowable:
PHYSICAL_HOST_SEPARATION = UNKNOWN.

For a provider-zone/site Z1 claim, same physical host across two distinct genuine zones should be structurally impossible, but that must follow from provider semantics, not assumption.

### Shared availability zone/site

Must be explicitly ruled out.

Different instance names, public IPs or DNS names do not establish this.

### Shared power

If Z1 claim is physical-site loss, shared power dependency across placements may matter.

If provider's zone definition explicitly includes independent power failure domains, provider semantics may satisfy this evidence class.

Otherwise:
POWER_INDEPENDENCE = UNKNOWN.

### Shared network

Need distinguish:
- shared Internet upstream;
- shared top-of-rack/site switching;
- shared provider regional backbone;
- shared control-plane access.

Not every shared network component invalidates durability, but any component whose failure can simultaneously make all required acknowledged state unavailable or corrupt the proof must be identified.

If relevance cannot be determined:
NETWORK_COMMON_MODE = UNKNOWN.

### Shared control plane

A shared provider control plane may affect ability to provision/manage/fail over without necessarily destroying stored state.

For F2 design, separate:
- data durability survival;
- control-plane availability;
- operational recovery.

If control plane is required for state survival/readback under Z1 test, shared control-plane failure becomes relevant.

Otherwise it remains a documented limitation, not automatically a durability failure.

## 5. Acceptable evidence classes

Acceptable documentary evidence may include:

1. provider authoritative documentation;
2. provider account placement metadata;
3. exact host/provider inventory tied to resource ID;
4. immutable infrastructure/config placement records;
5. independently read-back provider metadata;
6. provider support attestation with exact resource IDs and domain semantics;
7. later separately authorized runtime verification evidence.

Strength rule:

self-declared local label < immutable project config < provider account metadata < independently corroborated provider placement evidence.

No single hierarchy is universal; what matters is whether the evidence proves the exact assertion and its provenance.

A valid proof should use at least two logically distinct evidence steps where practical:
- resource→zone binding;
- zone semantics/independence definition.

## 6. What must remain UNKNOWN if provider transparency is insufficient

Keep UNKNOWN for any of the following not independently established:

- exact availability zone;
- exact physical site;
- physical host/hypervisor identity;
- rack/power domain;
- storage cluster/failure domain;
- replication placement;
- network common-mode dependency;
- control-plane common-mode dependency;
- whether two provider labels correspond to distinct failure domains;
- whether attached storage follows compute-zone placement;
- whether provider can migrate a VPS across sites without changing exposed identity;
- whether snapshots/backups share the same site;
- anti-affinity enforcement;
- provider-side replication/quorum policy.

UNKNOWN must not be converted into "probably independent".

If a critical Z1 assertion depends on an UNKNOWN, Z1 documentary proof is NOT_ESTABLISHED.

## 7. What must NOT be inferred from superficial identifiers

The following alone are NOT evidence of Z1 independence:

- VPS names;
- hostnames;
- public IP addresses;
- different subnets;
- reverse DNS;
- DNS names;
- city labels;
- country labels;
- provider product names;
- different order numbers;
- different VM UUIDs;
- different guest MAC addresses;
- different operating-system host IDs;
- latency differences;
- traceroute differences;
- rough geography;
- different billing products;
- different datacenter marketing pages without exact resource binding.

Even two cities do not prove independent storage/control-plane failure domains if provider architecture is unknown.

Likewise, same city does not prove same site if provider exposes multiple independent zones.

## 8. Evidence required before future cross-zone runtime verification

Before any runtime Z1 test, require an immutable pre-test evidence package containing:

### Resource identity
- exact provider/resource IDs for both placements;
- exact project aliases only as secondary labels.

### Zone/site identity
- exact zone/site IDs for both;
- provider semantics defining those IDs.

### Independence basis
- exact evidence that ZA and ZB are distinct failure domains for the relevant resource type.

### Storage/state placement
- exact placement model for all required S1 checkpoint state:
  - immutable object;
  - current pointer;
  - PUT outcomes;
  - CAS outcomes;
  - dedupe/fence/transaction evidence.

### Common dependencies
- shared storage assessment;
- hypervisor/site assessment;
- power/network/control-plane assessment where relevant.

### Runtime version/config
- exact future implementation version/config identity;
- exact backend/topology;
- exact quorum/replication semantics;
- exact acknowledgement rule.

### Test authority
- separate OPERATOR authority for:
  - host/provider access;
  - runtime test;
  - failure injection/site isolation if any;
  - shard WRITE if required.

### Stop criteria
- identity mismatch;
- zone/site ambiguity;
- missing critical placement proof;
- shared single failure domain discovered;
- topology differs from documented evidence;
- implementation/config mismatch;
- inability to prove safe failure boundary.

Without this pre-test package, future "cross-zone runtime test" is not a Z1 test.

## 9. Evidence/failure modes that invalidate a claimed Z1 proof

A Z1 claim becomes invalid or blocked if any of the following occurs:

### Identity mismatch
Resource IDs in runtime/test do not match documented placement evidence.

### Zone ambiguity
Provider cannot establish whether placements are in distinct zones/sites.

### Marketing-label substitution
Proof relies only on city/region/product labels without failure-domain semantics.

### Shared critical storage
Both placements depend on one storage failure domain whose loss destroys required acknowledged state.

### Same-site discovery
Provider evidence later shows both resources share the same physical site/zone.

### Placement drift
Provider migration or reprovisioning changes zone/site without refreshed evidence.

### Topology drift
Storage/replication/quorum layout changes after evidence was captured.

### Common-mode dependency discovered
A supposedly independent path shares a critical single point of failure relevant to the S1 state.

### Evidence staleness
Resource or provider metadata is no longer current for exact instances.

### Unverifiable provider assertion
Provider claims independence but gives no exact resource binding or meaningful failure-domain definition.

### Readback mismatch
Independent verification yields different zone/site/config identity.

### Runtime mismatch
Future test uses backend/config/version different from the one documented in the evidence package.

Any such condition:
Z1_PROOF = BLOCKED or STALE;
do not silently downgrade test meaning.

## 10. Privacy, secret boundaries and stop conditions

### Do not collect in the documentary plan

- credentials;
- API tokens;
- private keys;
- secret-bearing URLs;
- raw provider cookies/session data;
- billing secrets;
- unrelated account data;
- visitor/user data.

### Future provider/account evidence must be minimized

Preserve only what is needed:
- provider name if approved for project evidence;
- exact resource ID or redacted immutable derivative if policy requires;
- zone/site/failure-domain identifier;
- exact relevant placement attributes;
- evidence locator/version;
- verification result.

Do not publish sensitive provider account identifiers merely because they exist.

### Stop conditions

STOP and return exact blocker if:
- provider metadata access authority is absent;
- exact resource identity cannot be bound;
- zone/site semantics are ambiguous;
- evidence requires reading secrets outside authority;
- provider API/account access would exceed scope;
- two resources cannot be proven independent;
- critical shared dependency remains unresolved and material to Z1;
- evidence conflicts;
- candidate placement changed during review;
- runtime/test authority is missing.

## Evidence plan by phase

### Phase Z1-DOC-1 — identity evidence

Goal:
bind candidate resource A/B to exact provider resource IDs.

Output:
two immutable resource identity records.

Authority needed later:
provider/account metadata read authority.

Current status:
NOT_EXECUTED.

### Phase Z1-DOC-2 — zone/site binding

Goal:
bind resource IDs to provider zone/site IDs.

Output:
resource→zone/site evidence.

Current status:
NOT_EXECUTED.

### Phase Z1-DOC-3 — provider semantics

Goal:
establish what the provider means by distinct zone/site for the relevant compute/storage class.

Output:
authoritative semantics reference.

Current status:
NOT_EXECUTED.

### Phase Z1-DOC-4 — common-mode review

Goal:
determine whether shared storage/hypervisor/power/network/control-plane dependencies invalidate Z1.

Output:
known/unknown dependency matrix.

Current status:
NOT_EXECUTED.

### Phase Z1-DOC-5 — independent reconciliation

Goal:
cross-check exact identities/placement/semantics and issue:
PASS_Z1_DOCUMENTARY_BASIS
or exact BLOCKED/UNKNOWN.

Current status:
NOT_EXECUTED.

### Phase Z1-RUNTIME

Only after Z1-DOC-1..5 provide sufficient basis.

Goal:
future separately authorized runtime survival verification.

Current status:
NOT_AUTHORIZED / NOT_EXECUTED.

## Minimum documentary acceptance criteria before runtime gate

All required:

1. two exact resource identities;
2. exact zone/site binding for each;
3. provider semantics proving zone/site distinction is a failure-domain distinction;
4. no known shared critical dependency that contradicts Z1;
5. all unresolved material dependencies explicitly classified;
6. evidence package immutable and read back;
7. candidate topology matches package;
8. separate runtime/test authority exists.

If material UNKNOWN remains:
do not call the later test "verified Z1".

## Current truth

Z1 design boundary:
SELECTED

Candidate placements:
NOT_SELECTED_BY_THIS_TASK

Provider/backend:
NOT_SELECTED

Z1 documentary proof:
NOT_ESTABLISHED

Cross-zone independence:
UNKNOWN

Second placement:
UNKNOWN

Shared storage:
UNKNOWN

Shared physical host/hypervisor:
UNKNOWN

Shared availability zone/site:
UNKNOWN

Shared power/network/control plane:
UNKNOWN

Runtime implementation:
UNVERIFIED

CHECKPOINT_DURABLE:
NOT_ESTABLISHED

Resume authority:
NOT_GRANTED

Memory-layering attempt 3:
NOT_AUTHORIZED

## EXPERIENCE

Идея → определить, что должно быть доказано до того, как два VPS торжественно назовут "двумя зонами".

Проба → разложить Z1 на resource identity, provider zone/site binding, provider semantics и common-mode dependencies.

Результат → для настоящего Z1 нужны две независимые части evidence: exact placement и смысл этого placement как failure domain. Имена машин, IP и география этого не заменяют.

Вердикт → evidence plan complete; Z1 proof still NOT_ESTABLISHED.

Урок → два сервера ещё не два failure domains. Иногда это просто два счета за один и тот же шкаф.

## Terminal

PASS_SIS_S1O2_F2_Z1_EVIDENCE_PLAN_R01_DOCUMENT_ONLY

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
