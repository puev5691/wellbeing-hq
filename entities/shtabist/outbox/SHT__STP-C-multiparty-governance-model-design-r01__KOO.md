# SHT → KOO: STP-C multi-party governance model design r0.1

status: CANDIDATE_NOT_ACTIVE
terminal: PASS_SHT_STP_C_MULTIPARTY_GOVERNANCE_MODEL_DESIGN_R01_READY_FOR_REVIEW
scope: DOCUMENT_ONLY_GOVERNANCE_MODEL_DESIGN
selected_governance_family: STP-C_MULTI_PARTY_APPROVAL_PROFILE
actual_participants: NOT_APPOINTED
active_quorum: NOT_SELECTED
trust_root: NOT_SELECTED_NOT_CREATED
signer_attestor: NOT_SELECTED
keys_credentials: NOT_CREATED
backend_host_operator: NOT_SELECTED
profile_activation: no
live_write_cas: NOT_AUTHORIZED
checkpoint_durable: NOT_ESTABLISHED
eom_pilot: BLOCKED
memory_layering_attempt_3: NOT_AUTHORIZED
project_time: omitted

## Человеческий смысл

ОПЕРАТОР выбрал только семейство governance-модели STP-C: будущий SupervisorTrustProfile не должен становиться допустимым по решению одной стороны. Этот документ превращает принцип в candidate-модель, но никого не назначает, quorum не активирует, signer/root technology/keys не создаёт.

Базовое правило для всех вариантов:
NO VALID QUORUM OR CONFLICTING/STALE/UNKNOWN CURRENTNESS => PROFILE NOT ADMITTED.

## 1. Exact basis

OPERATOR selection:
entities/koordinator/outbox/KOO__select-STP-C-multiparty-approval-profile-r01__OPERATOR.md@b3989e477a74ec84efc4158a1db6ada62349afd6
blob 5c2b16545d088365962b2a44846a76190c8980da.

Task:
entities/koordinator/outbox/KOO__STP-C-multiparty-governance-model-design-r01__SHT.md@a640b180188d4177944df9a000ad066459894702
blob a07d921d6c254722257397a2ac13b727f354d7fe.

Current SHT writer:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641
blob a019c21cffeb99bb7c387b8fa95a4629137dc6da.

Admission-profile basis:
entities/sisadmin/outbox/SIS__operational-shard-admission-profile-design-r01__KOO.md@0634480e3a1ec7dd8fe041606747ffe2571404fb
blob 2b6abe0cd4e6be66bb687eff00d6bac513ff2dff.

Governance review:
entities/shtabist/outbox/SHT__operational-shard-admission-profile-r01-governance-review__KOO.md@ce2e3849a21c6c91d53cfa0bb31aa6c4ca98e7c0
terminal PASS_SHT_OPERATIONAL_SHARD_ADMISSION_PROFILE_R01_GOVERNANCE_REVIEW.

Fresh preflight found no later competing SHT writer, STP-C successor or superseding task/decision before this design.

## 2. Candidate participant-role compositions

These are role compositions only, not appointments.

C1 — governance/coordination + normative/process + infrastructure/security.
Illustrative classes only: KOO-class / KAN-or-SHT-class / SIS-class.
Strength: three failure perspectives.
Risk: governance/normative overlap may reduce real independence.

C2 — human/non-delegable governance + independent organizational/normative review + infrastructure/security.
Strength: high-impact profile changes retain direct human participation.
Risk: human-seat availability becomes deliberate bottleneck.
No OPERATOR quorum obligation is created here.

C3 — governance/coordination + normative/process + independent technical verifier.
Strength: evidence-oriented seat independent of mutation service.
Risk: verifier needs a complete evidence package and must not verify evidence it solely created.

C4 — four seats: governance/coordination + normative/process + infrastructure/security + independent verifier.
Strength: strongest separation and flexible role-constrained quorum.
Risk: highest coordination/deadlock cost.

Forbidden concentration:
- requester cannot be sole/decisive approver of its own elevation;
- mutation service cannot be sole approver;
- signer/attestor cannot alone decide governance truth and then self-attest it;
- verifier cannot verify evidence it solely created;
- publisher cannot turn publication capability into approval authority;
- host/admin capability does not grant trust approval;
- routing/reconciliation does not grant signing authority;
- review role does not grant operational/signing authority;
- one runtime/credential identity must not silently occupy multiple quorum seats.

Any future dual-role arrangement requires explicit OPERATOR approval and conflict analysis.

## 3. Candidate quorum models

### Q1 — 2-of-2

Availability: lowest; either unavailable => no admission.
Compromise: both independent seats required for forged approval.
Deadlock: any disagreement blocks.
Revocation: ordinary change requires both; urgent revoke needs separate rule.
Evidence: two distinct current identities/roles, same profile revision/digest/scope, current revocation state, independence proof.

### Q2 — 2-of-3

Availability: tolerates one unavailable participant.
Compromise: two compromised seats can become decisive, so independence matters.
Deadlock: 1 approve + 1 reject + 1 unavailable => no admission.
2 approve + 1 reject: candidate default is conflict/block, not silent numeric victory, unless OPERATOR later approves another rule.
Revocation: two valid revoke approvals may operate if separately approved.
Evidence: three seat identities/currentness, threshold evidence, contradiction status, role independence.

### Q3 — role-constrained quorum

Candidate form: numeric threshold plus distinct required role classes, for example one governance/normative and one technical/security/verifier class.

Availability: better than named 2-of-2 if a role class has alternates, worse than unconstrained numeric quorum.
Compromise: reduces same-domain capture.
Deadlock: unavailable required role class blocks despite numeric votes.
Revocation: may use separately approved role-constrained revoke path.
Evidence: role binding/currentness, numeric threshold, role coverage, independence, contradiction/revocation state.

### Q4 — unanimous high-impact + separate emergency revoke

High-impact admission/root-affecting revision requires unanimity of selected seats/required classes.
Urgent revoke may use a separately approved smaller quorum only to REVOKE/FREEZE exact profile/revision/scope.

Availability: lowest for high-impact admission; better for emergency removal.
Compromise: strongest admission resistance; reduced revoke path can cause denial-of-service but cannot create privilege.
Deadlock: disagreement intentionally blocks admission.
Evidence: high-impact classification, unanimous approvals, separate revoke-only policy/capability, current emergency participants, after-action audit.

SHT does not select Q1-Q4.

## 4. Immutable approval-evidence model

Candidate object STPCApprovalEvidenceV1:
- approval_evidence_id;
- profile_id;
- profile_revision;
- profile_digest;
- decision_digest;
- participant_identity_ref;
- participant_role_ref;
- participant_role_revision;
- decision = APPROVE | REJECT;
- decision_scope;
- authority_ref;
- authentication_evidence_ref;
- validity evidence/ref;
- revocation_state_ref;
- participant_currentness_ref;
- profile_supersession_ref;
- evidence_set_digest;
- supersedes where applicable;
- status.

No secret/private-key material.

Approval counts only if all counted objects bind to the same exact profile_id, profile_revision, profile_digest, decision_scope and required evidence semantics.

Candidate approval-set object STPCApprovalSetV1:
- exact profile/revision/digest;
- quorum_policy_id/revision;
- participant-role policy identity;
- included approval IDs;
- excluded/rejected/stale IDs with reason;
- calculated quorum;
- contradiction state;
- currentness/revocation verification refs;
- final state:
QUORUM_SATISFIED_CANDIDATE | NO_QUORUM | CONFLICT | STALE | REVOKED | SUPERSEDED | CURRENTNESS_UNKNOWN.

QUORUM_SATISFIED_CANDIDATE is not live activation.

## 5. Fail-closed states

NO_QUORUM => PROFILE_NOT_ADMITTED.
CONTRADICTORY_APPROVALS => PROFILE_NOT_ADMITTED_CONFLICT.
PARTICIPANT_REVOKED => evidence excluded; if quorum lost, PROFILE_NOT_ADMITTED.
STALE_EVIDENCE => PROFILE_NOT_ADMITTED_STALE.
PARTICIPANT_UNAVAILABLE => absence is neither approve nor reject; if quorum unavailable, PROFILE_NOT_ADMITTED_NO_QUORUM.
PROFILE_SUPERSEDED_DURING_APPROVAL => old approvals do not carry to successor revision.
SPLIT_DECISION => PROFILE_NOT_ADMITTED_CONFLICT; no implicit casting vote.
CURRENTNESS_UNKNOWN => PROFILE_NOT_ADMITTED_CURRENTNESS_UNKNOWN.

No timeout converts silence into consent.

## 6. Revocation model

R1 ordinary supersession:
successor revision/digest gets a new approval set. Old approval evidence remains immutable. No approval carries forward automatically.

R2 urgent revoke:
a separately approved reduced quorum may only REVOKE/FREEZE exact profile/revision/scope. It cannot approve successor, widen scope, appoint participant, change quorum or issue writer authority. Exact reduced quorum remains UNKNOWN.

R3 participant/key compromise:
affected participant/key becomes COMPROMISE_PENDING or REVOKED under future root policy; uncertain approvals stop counting; approval sets are re-evaluated; unprovable quorum => NOT ADMITTED/FROZEN. New key does not inherit old authority without explicit binding.

R4 partial availability:
ordinary admission follows selected quorum; missing seats are never implicit approvals. Emergency revoke may use only a separately approved revoke-only path.

R5 stale revocation state:
if current revocation/currentness cannot be verified within approved freshness, no new admission/quorum claim and mutation relying on profile is blocked.

## 7. Separation of duties

OPERATOR: selects governance composition/quorum/revoke/root/key/currentness policies and reserved high-impact decisions. Does not automatically sign or operate store.

KOO: reconciles current evidence/tasks and routes gates. Does not automatically become approval seat, signer, root or operator.

KAN: normative/formal review. No signing/infrastructure/mutation authority from review role.

SHT: process/lifecycle/conflict/separation design/review. No appointment/signing/backend/profile activation authority.

SIS: infrastructure/security/backend/service design/review. Host/admin capability does not grant trust approval.

Future signer/attestor: mechanically authenticates/attests exact approved evidence within separately granted scope. Ability to sign does not determine governance truth.

Store mutation service: executes only separately admitted mutation; cannot issue profile approval, writer authority, root status or canonical acceptance.

Verifier: independently checks approval/quorum/digest/currentness/revocation; read-only for evidence/package it verifies; not silently an approval seat.

Publisher: publishes bounded artifacts under separate authority; publication does not create approval, receipt, current task/writer or activation.

## 8. Authentication-root interaction

STP-C is root-technology agnostic.

Future root architecture must allow verification of:
- participant identity;
- role/revision binding;
- immutable approve/reject evidence;
- evidence integrity;
- currentness/revocation;
- exact profile revision/digest/scope;
- quorum-policy identity/revision;
- identity/key replacement without silent authority inheritance;
- fail-closed unknown root/currentness.

Root technology proves who authenticated what; STP-C governance determines whether authenticated decisions constitute quorum.

No concrete root technology is selected.

## 9. Decision table for OPERATOR

| Decision | Candidate options | Consequence | Evidence needed | Current status |
|---|---|---|---|---|
| Participant-role composition | C1 / C2 / C3 / C4 or reviewed derivative | availability, independence and human involvement differ | conflict-of-interest map; availability/failure analysis; role authority boundaries | NOT SELECTED |
| Quorum | Q1 2-of-2 / Q2 2-of-3 / Q3 role-constrained / Q4 high-impact unanimity model | security/availability/deadlock tradeoff | threat model; role independence; outage simulations; contradiction policy | NOT SELECTED |
| Emergency revoke | same quorum / reduced revoke-only / role-constrained revoke | faster containment vs DoS risk | prove revoke-only cannot grant/widen authority; compromise/outage scenarios | NOT SELECTED |
| Signer/attestor separation | approval seats sign directly / separate mechanical signer / future threshold mechanism | simplicity vs separation/blast radius | capability-separation proof; replay/scope binding; failure model | NOT SELECTED |
| Authentication root | Git+pinned key / offline root / threshold root / other reviewed technology | custody/availability/recovery differ | cryptographic/lifecycle design; independent review; revocation/currentness proof | NOT SELECTED |
| Key custody | human/offline / dedicated custodian / split/threshold / other reviewed | operational burden vs compromise blast radius | access/recovery/rotation/audit design | UNKNOWN |
| Revocation/currentness transport | fresh canonical lookup / signed short-lived status / separately reviewed mechanism | availability vs stale-evidence risk | freshness bounds; replay/revocation/outage tests | NOT SELECTED |

No table row has default-selection semantics.

## 10. Minimum invariants for any future selection

Any future STP-C profile must preserve:
1. exact revision/digest binding;
2. authenticated participant/role evidence;
3. explicit currentness/revocation evidence;
4. no silent vote carry-forward across revisions;
5. no timeout-as-consent;
6. no numeric quorum overriding a blocking contradiction unless explicitly approved;
7. emergency revoke cannot grant or widen authority;
8. root/signing capability does not create governance authority;
9. quorum satisfaction does not itself activate live profile;
10. separate final admission authority remains required.

## 11. Failure rule

Default:
NO_QUORUM / CONFLICTING_EVIDENCE / UNKNOWN_CURRENTNESS / STALE_OR_REVOKED_EVIDENCE / SUPERSEDED_PROFILE
=> PROFILE NOT ADMITTED.

No fail-open fallback.

## 12. Still forbidden / unresolved

This candidate does not:
- appoint participants;
- select active quorum;
- create/choose trust root;
- create keys/credentials;
- select attestor;
- select backend/host/operator;
- activate profile;
- activate Project Source;
- authorize live WRITE/CAS;
- deploy;
- establish CHECKPOINT_DURABLE;
- unblock EOM pilot;
- authorize memory-layering attempt 3.

## EXPERIENCE

Идея → multi-party trust is safer only if independence is structural, not merely a count of signatures.

Проба → compare numeric, role-constrained and asymmetric grant/revoke quorums while separating governance decision from mechanical authentication.

Результат → four composition candidates, four quorum families, immutable approval model, fail-closed conflicts and revoke-only emergency path are defined without appointing anyone.

Успех → document-only STP-C model is ready for independent review.

Урок → two signatures from one administrative failure domain are mostly one signature wearing a fake moustache. Quorum needs role/capability independence, not just arithmetic.

## Terminal

PASS_SHT_STP_C_MULTIPARTY_GOVERNANCE_MODEL_DESIGN_R01_READY_FOR_REVIEW

---
КТО: SHT / ШТАБИСТ
КОМУ: KOO / КООРДИНАТОР
