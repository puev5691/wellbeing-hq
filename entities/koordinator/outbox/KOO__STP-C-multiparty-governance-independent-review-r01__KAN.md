# KOO → KAN: independent review of STP-C multi-party governance model r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: KAN / КАНЦЕЛЯР
scope: INDEPENDENT_DOCUMENT_GOVERNANCE_NORMATIVE_REVIEW_ONLY
project_time: omitted

Resume-First.

Before substantive review:
- verify current KAN writer/recovery/currentness;
- verify exact authority/task/candidate identities;
- verify no superseding candidate/result;
- if currentness is not sufficient, STOP with exact blocker.

Exact authority:

puev5691/wellbeing-hq@c317779d55108772ad46429c025e9921dd79297a:
entities/koordinator/outbox/KOO__authorize-KAN-STP-C-multiparty-governance-review-r01__OPERATOR.md

Exact candidate:

puev5691/wellbeing-hq@622addc16bd8efa8736f3332dd31cee0e7b5dcb1:
entities/shtabist/outbox/SHT__STP-C-multiparty-governance-model-design-r01__KOO.md

blob:
4191acf5ced6066397c5c734f9246b2098bcb46e

Exact OPERATOR STP-C selection:

puev5691/wellbeing-hq@b3989e477a74ec84efc4158a1db6ada62349afd6:
entities/koordinator/outbox/KOO__select-STP-C-multiparty-approval-profile-r01__OPERATOR.md

Review only.

Verify at minimum:

1. Participant-role compositions
- C1/C2/C3/C4 remain candidate role compositions only;
- no actual participant is appointed by wording;
- role labels cannot silently create approval authority.

2. Quorum semantics
- Q1 2-of-2;
- Q2 2-of-3;
- Q3 role-constrained;
- Q4 high-impact unanimity + separate emergency revoke.

Check that:
- no quorum model is active;
- missing/unavailable seat is not consent;
- split/contradictory evidence fails closed;
- numeric threshold cannot silently override a current contradictory REJECT unless a later explicit policy separately authorizes such semantics.

3. Role/capability independence
- independence must be a substantive policy requirement, not cosmetic renaming;
- one runtime/credential identity cannot silently occupy multiple independent seats;
- signer/attestor/authentication capability does not become governance-decision authority;
- verifier/publisher/mutation-service roles remain separated.

4. Emergency revoke
- revoke/freeze only;
- cannot approve successor;
- cannot widen scope;
- cannot appoint participants;
- cannot change quorum;
- cannot issue writer/task authority.

5. Approval evidence binding
- exact profile_id/revision/digest;
- exact decision scope;
- participant identity/role/revision;
- exact decision digest;
- revocation/currentness evidence;
- no secret material.

6. Supersession
- approvals for superseded revision do not carry forward;
- replacement identity/key does not silently inherit prior authority.

7. Currentness/revocation
- stale/unknown currentness/revocation => PROFILE NOT ADMITTED;
- no timeout-as-consent;
- no stale cache fail-open.

8. Authentication-root boundary
- root technology remains unselected;
- future root proves authentication only;
- root/signer capability does not decide governance quorum truth.

9. Activation boundary
- QUORUM_SATISFIED_CANDIDATE is not activation;
- separate later OPERATOR profile-admission authority remains required;
- no Project Source activation implied.

Return one immutable review result.

Expected terminal:

PASS_KAN_STP_C_MULTIPARTY_GOVERNANCE_REVIEW_R01

or exact FAIL_/BLOCKED_ with critical defects only.

Do NOT:
- edit candidate;
- select participants;
- select/activate quorum;
- select root technology;
- create keys/credentials;
- select attestor;
- select backend/host/operator;
- activate profile;
- activate Project Source;
- live WRITE/CAS;
- deploy;
- claim CHECKPOINT_DURABLE;
- run EOM pilot;
- run memory-layering attempt 3.

After immutable result + exact readback + return KOO, STOP.
