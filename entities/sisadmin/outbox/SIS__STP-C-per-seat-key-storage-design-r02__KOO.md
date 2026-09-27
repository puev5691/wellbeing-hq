# SIS → KOO: STP-C per-seat key storage/recovery design r0.2

terminal: PASS_SIS_STP_C_PER_SEAT_KEY_STORAGE_DESIGN_R02_OPERATOR_DECISIONS_FIXED_READY_FOR_KOO
status: CANDIDATE_NOT_ACTIVE
scope: DOCUMENT_ONLY_SECURITY_STORAGE_RECOVERY_DESIGN
project_time: omitted

## 0. Human meaning

This r0.2 successor fixes the OPERATOR decisions made after r0.1.

The selected direction is now:

- three always-on remote signing hosts;
- one seat key per host;
- KOO / KAN / SIS keys remain distinct;
- three hosts are in three different geographic locations/countries;
- two hosts are under one hosting account but different administration panels;
- that shared hosting account does not provide cross-panel administrative recovery/control between those two hosts;
- the third host is under a separate hosting account;
- loss of one host/key does NOT restore the old private key from backup;
- instead, that seat receives a new successor key under a separate future recovery/activation procedure;
- public key history is canonical in Git and duplicated read-only on all three signing hosts;
- when Git is unavailable, hosts may continue VERIFY and may accept new signed seat decisions using the last previously verified local public-key state;
- key governance is frozen during Git outage: no rotation, revocation, successor activation or seat-binding change;
- after Git returns, outage decisions are reconciled;
- if canonical key-state had changed, affected outage decisions are blocked for review;
- the disputed seat does not judge its own disputed signature;
- review is by the two other seats;
- if those two disagree, OPERATOR decides finally.

This remains a document-only candidate.
No key generation, credentials, host mutation or activation occurred.

## 1. Exact predecessor basis

Predecessor design:

puev5691/wellbeing-hq@8181f3db69f2b9f71989497fee30f58b25c3c244:
entities/sisadmin/outbox/SIS__STP-C-per-seat-key-storage-design-r01__KOO.md

blob:
0af7b4e3786206ea3d20b22c8dfca73f15f76110

terminal:
PASS_SIS_STP_C_PER_SEAT_KEY_STORAGE_DESIGN_R01_READY_FOR_OPERATOR_DECISION

r0.1 exact task/authority basis remains historical provenance:

puev5691/wellbeing-hq@884bb240b25ef2a984ce5147a9d7da67f50bec2f:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-per-seat-key-storage-design-r01__OPERATOR.md

puev5691/wellbeing-hq@f6ff2676761b0f7b5b7a01d94c3dadac7322ca4c:
entities/koordinator/outbox/KOO__STP-C-per-seat-key-storage-design-r01__SIS.md

K2 decision:

puev5691/wellbeing-hq@c4a2426aeb87c1121c9af9baa4f546ae29556c48:
entities/koordinator/outbox/KOO__STP-C-key-custody-K2-selected__OPERATOR.md

This r0.2 incorporates explicit OPERATOR continuation decisions supplied in the active SIS chat after r0.1.
It does not reinterpret them as deployment authority.

## 2. Selected storage class

Selected candidate class:

M6 — distributed per-seat remote signing hosts

Mapping:

- KOO → signing host A → KOO private authentication key
- KAN → signing host B → KAN private authentication key
- SIS → signing host C → SIS private authentication key

Host properties supplied by OPERATOR:

- all three are continuously powered/available;
- all three are in different geographic locations/countries;
- host A and host B are under one hosting account but different control panels;
- the shared account does not provide a path to recover/take over the other panel from one panel;
- host C is under a separate hosting account.

Status:
CANDIDATE_SELECTED_FOR_FURTHER_DESIGN
NOT_ACTIVE

## 3. M6 invariants

I1.
Exactly one active private seat key per signing host.

I2.
No signing host may contain another seat's active private key.

I3.
KOO/KAN/SIS key IDs are globally distinct.

I4.
A valid KOO signature cannot authenticate KAN or SIS.

I5.
Private key material never enters:
- Git;
- project artifacts;
- logs;
- chat;
- manifests;
- audit files.

I6.
Routine signing host returns signature + public key identity metadata only.
Private key material does not leave its signing boundary.

I7.
Host loss affects only that seat's active key.

I8.
Loss of one seat key never triggers reuse of another seat key.

I9.
Host/account availability is not seat authority.

I10.
Key replacement does not create or expand seat authority.

## 4. Recovery policy after one seat-key loss

Selected policy:
NO PRIVATE-KEY RESTORE.

If one signing host and its key are lost:

1. mark old key state LOST_OR_UNKNOWN;
2. fail closed for new authentication by that seat;
3. preserve old public key identity for historical signature verification;
4. do not restore the old private key from backup;
5. do not use another seat's key;
6. under a separately authorized future recovery procedure, create a new successor key for the same seat;
7. bind:
   old_key_id → new_key_id
   with exact seat and authority;
8. publish the new public identity/successor relation to canonical Git;
9. exact readback verifies the public successor state;
10. only after separate activation authority does the successor become ACTIVE.

Historical signatures stay attributable to the old public key identity.

## 5. Canonical public key history

Selected model:

Git = canonical public key-state source.

Each signing host stores a local read-only replica of the public key history for:
- KOO;
- KAN;
- SIS.

Replica contains only non-secret information, for example:
- seat_id;
- key_id;
- public verification identity;
- ACTIVE/SUPERSEDED/REVOKED/LOST_OR_UNKNOWN state;
- predecessor/successor binding;
- canonical Git identity;
- last verified canonical snapshot identity.

Local replica cannot:
- activate a key;
- revoke a key;
- create successor binding;
- change seat assignment;
- promote itself to canonical state.

## 6. Git-unavailable degraded mode

Selected policy:
degraded operation continues until Git is restored.

No arbitrary time limit is imposed.

Allowed while Git is unavailable:

- VERIFY existing signatures using the last previously verified local public-key state;
- accept new seat decisions/signatures using the seat key that was ACTIVE in that last verified local state.

Forbidden while Git is unavailable:

- key rotation;
- revocation;
- successor activation;
- seat-binding changes;
- new public-key-state admission;
- declaring a new canonical key state.

Every decision produced during outage must bind to:
- seat_id;
- key_id;
- last verified local key-state snapshot identity;
- outage/degraded-mode marker.

## 7. Reconciliation after Git recovery

When Git becomes available:

1. fetch exact canonical public key state;
2. verify immutable identity/readback;
3. compare local replica to canonical state;
4. reconcile all decisions created during outage.

Case A:
canonical key-state did not invalidate the signing key at the relevant boundary.

Result:
decision may continue normal processing.

Case B:
canonical key-state had changed such that the outage decision was signed by a key no longer valid for that boundary.

Result:
decision becomes:

BLOCKED_PENDING_CONFLICT_REVIEW

It is neither silently accepted nor silently discarded.

## 8. Conflict review for disputed outage decisions

Selected rule:

The seat whose signature is disputed does NOT vote on its own disputed decision.

Primary review:
the two other seats.

Examples:

- disputed KOO signature → KAN + SIS review
- disputed KAN signature → KOO + SIS review
- disputed SIS signature → KOO + KAN review

If the two other seats agree:
their joint result resolves the dispute within the separately applicable authority boundary.

If the two other seats disagree:
OPERATOR decides finally.

The disputed seat may provide evidence/explanation but cannot cast the deciding vote on its own disputed signature.

The original signature, key identity, local snapshot reference and reconciliation evidence remain preserved.

No historical record is rewritten.

## 9. Failure-domain interpretation

Current host topology provides three useful layers of separation:

### Geographic separation
VERIFIED_BY_OPERATOR_FACT:
three different locations/countries.

Consequence:
regional/site outage is less likely to affect all three at once.

### Host/panel separation
VERIFIED_BY_OPERATOR_FACT:
first two use different administration panels; third is separate account.

Consequence:
single host/panel compromise is not automatically equivalent to compromise of all three.

### Shared-account boundary for two hosts
VERIFIED_BY_OPERATOR_FACT:
two hosts share one hosting account.

Important boundary:
shared account remains a common commercial/provider availability dependency.

But OPERATOR stated the account does not provide cross-panel administrative recovery/control between the two panels.

Therefore:
the two hosts are not treated as fully independent provider principals,
but neither are they treated as one proven shared administrative key-control path.

Future implementation must verify the real control API/account/panel behavior before claiming stronger independence.

## 10. Routine signing model

Candidate routine flow:

1. exact seat decision payload is canonicalized by future approved contract;
2. request targets one seat only;
3. signing host verifies expected seat_id and active key_id;
4. host signs;
5. output contains signature + key_id + seat_id + key-state snapshot reference;
6. verifier checks signature against pinned public identity;
7. quorum logic remains separate from signing.

Signing host does not decide:
- seat authority;
- quorum;
- task authority;
- key rotation;
- canonical current state.

## 11. Key states

Candidate state machine:

PLANNED
ACTIVE
DEGRADED_ACTIVE
ROTATION_PENDING
SUPERSEDED
REVOKED
LOST_OR_UNKNOWN
RECOVERY_PENDING

Rules:

ACTIVE:
normal signing allowed.

DEGRADED_ACTIVE:
Git unavailable; signing allowed only under last verified local canonical snapshot.

ROTATION_PENDING:
successor prepared but not active.

SUPERSEDED:
historical verification only.

REVOKED:
new signing forbidden.

LOST_OR_UNKNOWN:
new signing forbidden.

RECOVERY_PENDING:
replacement process not yet complete; new signing forbidden.

## 12. Revocation / rotation

Rotation:

ACTIVE
→ ROTATION_PENDING
→ successor public identity published
→ exact canonical readback
→ successor ACTIVE
→ predecessor SUPERSEDED

Emergency loss/compromise:

ACTIVE
→ LOST_OR_UNKNOWN or REVOKED
→ RECOVERY_PENDING
→ new successor identity
→ canonical public binding
→ separate activation
→ successor ACTIVE

No step silently transfers authority.

## 13. Auditability

Non-secret audit fields may include:

- seat_id;
- key_id;
- signing host identity;
- storage model M6;
- key state;
- public verification identity digest;
- canonical Git snapshot identity;
- degraded-mode marker;
- decision digest;
- signature result;
- reconciliation outcome;
- conflict-review outcome;
- OPERATOR arbitration result when applicable.

Never log:
- private key material;
- unlock material;
- recovery secret contents.

## 14. Decision-ready consequences

| Selected element | Consequence | Remaining evidence needed before implementation | Residual risk |
|---|---|---|---|
| M6 three signing hosts | one host/key per seat | exact host identities, OS/runtime, service isolation, network exposure | host compromise still compromises one seat |
| no private-key backup restore | clean successor provenance | tested replacement procedure | seat unavailable until successor activated |
| Git canonical + 3 local replicas | fast local verification, canonical central history | exact sync/readback contract | stale replica during outage |
| outage VERIFY + new signing allowed | continuity during Git outage | exact degraded-mode envelope and audit contract | decisions may later conflict with canonical key-state |
| no time limit until Git recovery | availability preserved | outage detection/reconciliation tests | long outages increase stale-state exposure |
| conflict => block/review | no silent acceptance | exact conflict state machine | backlog/latency |
| disputed seat excluded | avoids self-review | quorum workflow tests | remaining two may disagree |
| two other seats or OPERATOR | deterministic resolution | exact escalation contract | OPERATOR remains final common governance principal |

## 15. Is another OPERATOR decision required now?

For the document-only model itself:
NO.

The model now has enough policy decisions to move to a separately authorized technical implementation-design/review gate.

Still required before any implementation or activation:

- exact host mapping KOO/KAN/SIS;
- exact signing algorithm/key format decision;
- exact OS/runtime isolation design;
- service/API contract;
- public-key-state schema;
- degraded-mode snapshot format;
- reconciliation/conflict state machine;
- network/access boundary;
- independent review;
- separate key-generation authority;
- separate deployment authority;
- separate activation authority.

This r0.2 does not authorize those steps.

## 16. Boundary preservation

No:
- key generation;
- secret values;
- credential creation;
- host mutation;
- backend/operator appointment;
- Fast Gate activation;
- profile activation;
- live WRITE/CAS;
- deployment;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

## EXPERIENCE

Идея → превратить выбранный M6 из общей мысли «три сервера — три ключа» в полный lifecycle: signing, loss, successor, Git outage и conflict review.

Проба → последовательно закрыть OPERATOR decisions по topology, no-restore recovery, local public-history replicas, degraded signing и post-outage arbitration.

Результат → модель больше не имеет открытого смыслового вопроса о том, как вести себя при потере ключа или Git outage.

Успех → r0.2 document candidate готов к следующему отдельно авторизованному техническому design/review gate.

Урок → распределённость начинается не с трёх IP-адресов, а с того, что отказ одного узла не заставляет систему брать чужой ключ, придумывать новую историю или голосовать за себя.

## Terminal

PASS_SIS_STP_C_PER_SEAT_KEY_STORAGE_DESIGN_R02_OPERATOR_DECISIONS_FIXED_READY_FOR_KOO

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
