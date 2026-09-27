# SIS → KOO: STP-C per-seat key storage/recovery design r0.1

terminal: PASS_SIS_STP_C_PER_SEAT_KEY_STORAGE_DESIGN_R01_READY_FOR_OPERATOR_DECISION
status: CANDIDATE_NOT_ACTIVE
scope: DOCUMENT_ONLY_SECURITY_STORAGE_RECOVERY_DESIGN
project_time: omitted

## 0. Human meaning

This document defines candidate storage/recovery classes for three distinct future STP-C private authentication keys:

- KOO;
- KAN;
- SIS.

It does not generate keys, create credentials, select a vendor/product, deploy anything, or activate STP-C.

K2 means logical per-seat separation under one human custodian: OPERATOR.

That separation is authentication separation, not independent external trust domains.

## 1. Exact basis

FACT — authority:
puev5691/wellbeing-hq@884bb240b25ef2a984ce5147a9d7da67f50bec2f:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-per-seat-key-storage-design-r01__OPERATOR.md
blob:
00a1b9635e6d423a837c8544ab5f71a1972dbf76

FACT — task:
puev5691/wellbeing-hq@f6ff2676761b0f7b5b7a01d94c3dadac7322ca4c:
entities/koordinator/outbox/KOO__STP-C-per-seat-key-storage-design-r01__SIS.md
blob:
99c5c230f9309d2246ea0c3285bc4f70f941cd9a

FACT — selected custody:
puev5691/wellbeing-hq@c4a2426aeb87c1121c9af9baa4f546ae29556c48:
entities/koordinator/outbox/KOO__STP-C-key-custody-K2-selected__OPERATOR.md
blob:
42de589ebfc0dea58975b4ba75fdbb522c3e5be7

FACT — current STP-C decisions supplied by exact task:
- seats: KOO / KAN / SIS;
- quorum: Q2 2-of-3, current REJECT blocks;
- emergency freeze: R3 KAN or SIS single-seat freeze-only;
- signer model: S1 seats authenticate own decisions;
- authentication root: A1 Git-backed identity binding + pinned verification key;
- custody: K2 per-seat logically separated under OPERATOR control.

## 2. Mandatory invariants

CANDIDATE invariants for any future implementation:

I1.
KOO, KAN and SIS private authentication keys are distinct cryptographic identities.

I2.
A key assigned to one seat cannot authenticate another seat.

I3.
Seat binding is explicit:
seat_id + key_id + public verification material identity + activation boundary.

I4.
Public verification identity may be pinned in Git under A1.

I5.
Private key material is never stored in:
- Git;
- project artifacts;
- logs;
- audit reports;
- prompts;
- chat messages;
- manifests;
- recovery descriptions.

I6.
OPERATOR recovery must preserve three separate seat identities.
Recovery of one seat must never substitute another seat's key.

I7.
Rotation creates an explicit successor binding:
old_key_id -> new_key_id
with exact seat, authority, effective boundary and reason.

I8.
REVOKED, LOST, UNKNOWN or ambiguous key state fails closed for authentication.

I9.
Historical signatures remain attributable to the historical key identity.
Revocation does not erase provenance.

I10.
Key replacement changes authentication material only.
It does not create:
- new seat authority;
- new quorum authority;
- new current-writer authority;
- new task authority.

I11.
One storage container, namespace or backup label must never silently contain more than one seat key unless the container itself enforces separately named/non-interchangeable entries and recovery preserves the seat binding.

I12.
Cross-seat copy/import must be treated as a configuration error and fail validation.

## 3. Candidate storage classes

### M1 — OS/user keystore class

Description:
Use a protected operating-system/user keystore capable of holding three separately named non-exportable or access-controlled key identities.

Candidate layout:
- KOO key entry;
- KAN key entry;
- SIS key entry;
each with unique key ID and explicit seat label.

Seat separation:
PARTIAL_TO_STRONG depending on whether the keystore enforces separate identities and non-exportability.

OPERATOR custody:
Compatible with K2 if OPERATOR controls the user/device account and recovery boundary.

Recovery:
Depends on platform capabilities.
Possible classes:
- secure device migration;
- encrypted export where explicitly supported;
- separately generated replacement key after loss.

Backup:
May be limited for non-exportable keys.
Therefore a separate recovery design is required even when primary keys are hardware/OS protected.

Rotation:
Good if keystore supports distinct successor entries without overwriting prior identity.

Revocation:
External STP-C state must mark old key revoked/superseded.
Deleting a local key is not sufficient revocation evidence.

Device loss:
Can remove access to all three if all keys reside on one device.
This is a common availability/failure risk.

Account compromise:
If attacker controls the same OS/user security context, all three logical seat keys may be exposed or usable.
K2 separation remains logical, not independent custody.

Accidental cross-seat reuse:
Moderate risk if labels/configuration are weak.
Mitigation requires exact seat/key binding checks.

Auditability:
Moderate.
Depends on keystore event/audit support plus external Git identity records.

Routine decision authentication:
High usability.

Unresolved risk:
One device/user security context may become a common control/failure domain for all three keys.

### M2 — password-manager / secret-vault class

Description:
A secret-vault/password-manager class stores three distinct cryptographic key records or signing identities under separate logical entries/namespaces.

Seat separation:
Logical separation can be strong if records are immutable-labeled and access rules prevent accidental substitution.

OPERATOR custody:
Very compatible with K2 because OPERATOR may remain sole human custodian while records remain per-seat.

Recovery:
Usually strong at vault/account layer, but recovery of the vault account can expose/control all three seats.

Backup:
Possible through vault recovery/export mechanisms only if those mechanisms preserve:
- per-seat identity;
- encryption;
- provenance;
- no project-artifact leakage.

Rotation:
Operationally convenient.
Successor records can coexist with historical key identities.

Revocation:
Must be recorded in STP-C canonical identity state, not inferred from deleting a vault entry.

Device loss:
Usually better than device-only keystore if vault recovery is independently available.

Account compromise:
Major common-domain risk.
A compromise of the single vault/control account can affect all three seats.

Accidental cross-seat reuse:
Moderate unless entry schemas enforce seat-specific key IDs and import validation.

Auditability:
Potentially high if vault provides non-secret access/change audit events.

Routine decision authentication:
High if secure signing workflow is ergonomic.

Unresolved risk:
Central vault compromise or recovery authority can collapse all three logical seat identities operationally.

### M3 — hardware-backed token/device class

Description:
Three separate physical hardware-backed key identities:
- one for KOO;
- one for KAN;
- one for SIS.

The model does not select vendor or protocol.

Seat separation:
Strongest physical separation among listed classes when each seat has a distinct hardware key identity.

OPERATOR custody:
Compatible with K2 if OPERATOR physically controls all three devices while preserving labels and inventory identity.

Recovery:
Harder.
Loss of one device requires either:
- pre-provisioned same-seat recovery identity under explicit policy;
- or creation of a successor key under recovery procedure.

Another seat's hardware key must never substitute.

Backup:
Private export may be impossible by design.
Recovery therefore relies on spare same-seat hardware or successor-key process rather than copying the private key.

Rotation:
Strong provenance if new hardware identity is separately enrolled and old one retained/revoked in canonical records.

Revocation:
Clear: old key ID can be revoked while preserving old public identity for historical verification.

Device loss:
Isolated to one seat if physical devices are separately controlled/labeled.
This is a major advantage.

Account compromise:
If routine signature approval still requires a shared platform account, account compromise may disrupt workflow but does not necessarily expose non-exportable hardware private key material.
Exact behavior depends on future integration and is UNKNOWN.

Accidental cross-seat reuse:
Low if devices are physically labeled and software verifies expected key ID per seat.

Auditability:
High at identity level.
Operational event audit depends on token/integration class.

Routine decision authentication:
Medium.
Requires physical device presence/action.

Unresolved risk:
Loss/destruction without predesigned same-seat recovery path can suspend that seat.

### M4 — encrypted offline private-key backup class

Description:
Encrypted offline storage of a seat-specific private-key backup.

This class is best treated as recovery material, not as the preferred routine signing surface.

Seat separation:
Can be strong if three separate encrypted envelopes/media identities are maintained:
- KOO recovery object;
- KAN recovery object;
- SIS recovery object.

OPERATOR custody:
Directly compatible with K2.

Recovery:
Strong if media remains readable and recovery procedure preserves exact seat/key identity.

Backup:
This is itself the backup class.
A second copy increases availability but also increases exposure and inventory burden.

Rotation:
Every key rotation requires explicit treatment of the old backup:
- retain under historical/recovery policy;
- or destroy under separately approved deletion policy.
Never silently overwrite.

Revocation:
Revoked backup material remains sensitive even when no longer valid.
It must not be mistaken for ACTIVE.

Device loss:
Independent of daily device if stored separately.

Account compromise:
Can remain protected if offline encryption/control is independent of the compromised online account.
Exact strength depends on future implementation.

Accidental cross-seat reuse:
Potentially high during manual recovery unless package metadata and recovery checks bind each encrypted object to one seat/key ID.

Auditability:
Moderate.
Physical/manual custody events require explicit non-secret inventory records.

Routine decision authentication:
Low.
Repeated decrypt/import for routine use increases exposure and operational error risk.

Unresolved risk:
Manual recovery/import is the highest-risk point for accidental seat mix-up.

### M5 — hybrid class: protected routine key + separate per-seat offline recovery

Description:
Each seat has:
- one protected primary signing identity in an OS keystore or hardware-backed device;
- one separately controlled recovery path, preferably not routinely exposed.

Seat separation:
Strong if primary and recovery identities are both explicitly seat-bound.

OPERATOR custody:
Compatible with K2.

Recovery:
Better than primary-only models.
Loss of routine device does not require using another seat key.

Backup:
Explicit and per-seat.

Rotation:
Supports controlled successor enrollment while keeping old public identity for historical verification.

Revocation:
Primary/recovery material is governed by the same canonical key-state model.

Device loss:
Can be isolated to one seat.

Account compromise:
Depends on primary storage class.
Offline recovery can reduce total loss risk if it is not controlled by the same online account.

Accidental cross-seat reuse:
Low-to-moderate if recovery packages are strongly labeled and software checks seat/key binding.

Auditability:
Potentially high because active key, recovery material and successor relations can be separately inventoried without exposing secrets.

Routine decision authentication:
High for OS-keystore hybrid; medium for hardware-token hybrid.

Unresolved risk:
More components mean more lifecycle discipline and more places where stale recovery material can survive.

## 4. Comparative decision table

| Model | Consequence | Evidence needed before implementation choice | Unresolved risk |
|---|---|---|---|
| M1 OS/user keystore | Very convenient routine signing; three logical keys can remain distinct | prove per-key identity isolation, non-exportability/export rules, recovery semantics, audit events, device-loss procedure | one device/user compromise may affect all seats |
| M2 vault/password-manager class | Strong operational recovery and easy rotation | prove per-entry separation, account recovery boundary, non-secret auditability, safe import/export, fail-closed seat binding | central vault/account compromise may affect all three |
| M3 hardware-backed per-seat devices | Best physical separation and lowest accidental cross-seat reuse | prove exact key-ID binding, non-exportability, loss/replacement process, routine workflow, spare/recovery semantics | device loss can suspend seat; operational friction |
| M4 encrypted offline backup | Strong recovery independence from daily device; poor routine signing model | prove encryption/custody procedure, seat labeling, restore test, stale/revoked backup handling | manual restore can mix seats; routine use unsafe/awkward |
| M5 hybrid primary + offline per-seat recovery | Balanced routine usability and recoverability; strongest lifecycle coverage | prove primary-class isolation plus recovery package binding, rotation/revocation/readback tests | complexity; stale recovery copies and lifecycle drift |

## 5. Candidate key identity model

Each future seat key must have a non-secret public identity record.

Candidate fields:

- seat_id;
- key_id;
- public_verification_identity;
- status;
- activated_by_authority_ref;
- activation_commit/blob;
- predecessor_key_id;
- successor_key_id;
- activation_boundary;
- revocation_boundary;
- revocation_reason_class;
- storage_model_class;
- recovery_profile_ref.

No private material in this record.

Candidate key states:

PLANNED
ACTIVE
ROTATION_PENDING
SUPERSEDED
REVOKED
LOST_OR_UNKNOWN
RECOVERY_PENDING

Rules:

- only ACTIVE key authenticates new seat decisions;
- ROTATION_PENDING does not automatically make successor active;
- SUPERSEDED old key remains valid for historical verification only;
- REVOKED does not authenticate new decisions;
- LOST_OR_UNKNOWN fails closed;
- RECOVERY_PENDING fails closed for new authentication until successor activation completes.

## 6. Recovery after loss of one seat key

Candidate recovery sequence for one seat, for example KAN:

1. Detect loss/unavailability.
2. Mark KAN key state LOST_OR_UNKNOWN.
3. Fail closed for new KAN authentication.
4. Do not use KOO or SIS key as substitute.
5. Preserve old KAN public key identity and historical signature verification.
6. Verify exact KAN seat authority/current governance before any replacement.
7. Under a separate future key-generation/replacement authority, create or recover a KAN-specific successor identity.
8. Bind successor explicitly:
   KAN old_key_id -> KAN new_key_id.
9. Publish only public successor binding to canonical Git identity record under A1.
10. Exact readback verifies the new public identity and state.
11. Activate new KAN key only after the separately authorized activation boundary.
12. Keep old key state SUPERSEDED or REVOKED according to exact cause.

Important:
If old private material is lost permanently, the old public identity still remains necessary for historical verification.

Recovery does not:
- create new KAN seat authority;
- change quorum;
- appoint a new participant;
- reuse KOO/SIS key.

## 7. Rotation model

Candidate planned rotation:

ACTIVE
→ ROTATION_PENDING
→ successor public identity registered
→ exact successor binding verified
→ new key ACTIVE
→ old key SUPERSEDED

Candidate emergency rotation after compromise/loss:

ACTIVE
→ LOST_OR_UNKNOWN or REVOKED
→ authentication fails closed
→ RECOVERY_PENDING
→ successor identity established under separate authority
→ successor ACTIVE
→ old key remains REVOKED

Required successor binding:

- exact seat_id;
- old key_id;
- new key_id;
- reason class;
- authority_ref;
- effective boundary;
- canonical public identity locator.

A successor key never inherits authority merely because it is cryptographically valid.

## 8. Revocation model

Candidate revocation causes:

- suspected compromise;
- confirmed compromise;
- device loss;
- storage corruption;
- custody ambiguity;
- key reuse/misbinding;
- scheduled retirement;
- operator-directed replacement.

Revocation properties:

- fail closed for new signatures;
- preserve public identity and historical signature attribution;
- publish revocation state/boundary without private material;
- do not erase provenance;
- do not silently activate successor.

UNKNOWN key state is operationally equivalent to fail-closed for new authentication.

## 9. Accidental cross-seat reuse controls

Candidate controls:

1. key_id unique across all STP-C seats;
2. seat_id embedded/bound in non-secret identity metadata;
3. signer invocation requires expected seat_id + expected key_id;
4. verifier rejects signature from valid but wrong-seat key;
5. import/restore checks exact seat binding before making key available;
6. backup object names alone are not trusted; internal non-secret metadata must match;
7. tests include deliberate KOO-key-for-KAN and SIS-key-for-KOO attempts;
8. cross-seat reuse is a hard error, never an automatic relabel.

## 10. Auditability model

Audit may record only non-secret facts:

- seat_id;
- key_id;
- storage model class;
- activation/revocation/supersession state;
- public verification identity digest;
- operation type: enroll / rotate / revoke / recover;
- authority locator;
- result;
- canonical readback identity.

Audit must not contain:
- private key bytes;
- export blobs;
- unlock secrets;
- recovery secret contents.

## 11. Suitability for routine decision authentication

M1:
HIGH usability.
Best when routine decisions occur on one controlled daily device.
Risk: common device compromise.

M2:
HIGH usability.
Best when secure vault-mediated signing/retrieval is operationally acceptable.
Risk: central account/vault compromise.

M3:
MEDIUM usability.
Best when deliberate physical confirmation is acceptable for each seat decision.
Risk: friction/device loss.

M4:
LOW routine usability.
Recommended only as recovery class, not normal signing surface.

M5:
HIGH or MEDIUM depending primary class.
Best lifecycle balance, but has greater operational complexity.

## 12. What current facts do and do not decide

FACT:
K2 requires three distinct per-seat authentication identities under OPERATOR control.

FACT:
KOO/KAN/SIS currently share one technical account/control domain.

CANDIDATE implication:
Per-seat key storage can prevent cryptographic identity collapse even though the human/admin control domain is shared.

It cannot create true independent human custody because OPERATOR controls all three.

UNKNOWN:
- daily signing device requirements;
- acceptable physical-token friction;
- whether routine signing must work from one daily device;
- whether non-exportable primary keys are required;
- recovery latency tolerance.

## 13. Is there enough information for one next bounded OPERATOR decision?

PARTIALLY.

There is enough information to make one bounded **storage-class direction** decision, but not enough to choose the best primary class without one operational preference.

Exact missing fact:

Does OPERATOR require routine KOO/KAN/SIS decision authentication to work on one normal daily device without a separate physical token for each seat?

Allowed answer:
- YES — prioritize daily-device usability;
- NO — separate physical seat tokens are acceptable;
- MIXED — physical tokens acceptable only for some/high-impact decisions.

No secret or product choice is requested.

This one fact is sufficient to narrow the next decision:
- YES tends to M1/M2/M5-with-software-primary classes;
- NO keeps M3/M5-with-hardware-primary viable;
- MIXED points toward a hybrid policy but still requires later bounded design.

This document does not select the model.

## 14. Boundary preservation

No:
- key generation;
- secret read/write;
- credential creation;
- vendor/product selection;
- host mutation;
- backend/host/operator selection;
- Fast Gate activation;
- profile activation;
- live WRITE/CAS;
- deployment;
- CHECKPOINT_DURABLE;
- Project Source activation;
- EOM pilot;
- memory-layering attempt 3.

## EXPERIENCE

Идея → сделать три seat identity реально разными криптографически, не притворяясь, что один ОПЕРАТОР внезапно превратился в трёх независимых custodians.

Проба → сравнить local keystore, central vault, hardware-backed и offline/hybrid recovery classes по loss/compromise/rotation/reuse/audit/routine-use границам.

Результат → все классы могут соблюдать K2, но они по-разному меняют общий failure domain: software/vault удобнее, hardware лучше изолирует физическую потерю, hybrid лучше всего покрывает lifecycle ценой сложности.

Успех → decision-ready document candidate.

Урок → три разных ключа — это уже разделение идентичности. Три папки с одинаковым ключом — это просто бухгалтерия, притворившаяся криптографией.

## Terminal

PASS_SIS_STP_C_PER_SEAT_KEY_STORAGE_DESIGN_R01_READY_FOR_OPERATOR_DECISION

---
КТО: SIS / СИСАДМИН r0.6
КОМУ: KOO / КООРДИНАТОР
