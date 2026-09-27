# KOO → SHT: STP-C multi-party governance model design r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHT / ШТАБИСТ
scope: DOCUMENT_ONLY_GOVERNANCE_MODEL_DESIGN
project_time: omitted

Resume-First.

Current authoritative SHT writer:

puev5691/wellbeing-hq@44a8181b7a6ebf42640bcd3f6e7e94750bb8b641:
entities/shtabist/current/SHT__current-instance-current-writer-r01.md
blob a019c21cffeb99bb7c387b8fa95a4629137dc6da

Exact OPERATOR selection:

puev5691/wellbeing-hq@b3989e477a74ec84efc4158a1db6ada62349afd6:
entities/koordinator/outbox/KOO__select-STP-C-multiparty-approval-profile-r01__OPERATOR.md

Selected model:
STP-C_MULTI_PARTY_APPROVAL_PROFILE

Exact admission-profile candidate basis:

puev5691/wellbeing-hq@0634480e3a1ec7dd8fe041606747ffe2571404fb:
entities/sisadmin/outbox/SIS__operational-shard-admission-profile-design-r01__KOO.md
blob 2b6abe0cd4e6be66bb687eff00d6bac513ff2dff

Governance review basis:

puev5691/wellbeing-hq@ce2e3849a21c6c91d53cfa0bb31aa6c4ca98e7c0:
entities/shtabist/outbox/SHT__operational-shard-admission-profile-r01-governance-review__KOO.md
terminal PASS_SHT_OPERATIONAL_SHARD_ADMISSION_PROFILE_R01_GOVERNANCE_REVIEW

Design only the selected STP-C governance model.

Required outputs:

1. Participant-role model
- identify 2–4 candidate role compositions;
- distinguish approval role from technical signer/attestor;
- do not appoint actual participants;
- identify forbidden role combinations due to conflict of interest/capability concentration.

2. Quorum models
Compare candidate forms such as:
- 2-of-2;
- 2-of-3;
- role-constrained quorum;
- unanimous high-impact change / reduced quorum emergency revoke if separately justified.

For each:
- availability consequence;
- compromise consequence;
- deadlock behavior;
- revocation behavior;
- evidence needed.

Do not select a quorum unless exact evidence already supports it.

3. Approval object
Define candidate immutable approval evidence:
- profile revision identity;
- participant identity/role;
- approval/rejection;
- scope;
- decision digest;
- validity/revocation evidence;
- no secret material.

4. Conflict / disagreement / deadlock
Define fail-closed states for:
- approvals below quorum;
- contradictory approvals;
- revoked participant;
- stale evidence;
- participant unavailable;
- profile superseded during approval;
- split decision.

5. Revocation model
Design candidate behavior for:
- ordinary profile supersession;
- urgent revoke;
- participant/key compromise;
- partial availability;
- stale revocation information.

6. Separation of duties
Show exact boundaries among:
- OPERATOR;
- KOO;
- KAN;
- SHT;
- SIS;
- future signer/attestor;
- store mutation service;
- verifier;
- publisher.

No role acquires authority merely because named.

7. Authentication-root interaction
Describe how STP-C approvals could bind to a future authentication-root design WITHOUT selecting:
- Git+pinned key;
- offline root;
- threshold root;
or any concrete root technology.

8. Decision table for OPERATOR
List only decisions still required after this design:
- actual participant-role composition;
- quorum;
- urgent-revoke rule;
- signer/attestor separation;
- authentication-root technology;
- key custody;
- revocation transport/currentness.

For each:
option → consequence → evidence needed → current status.

9. Failure rule
Default must be fail-closed:
no quorum / unknown currentness / conflicting evidence => profile NOT ADMITTED.

Hard boundaries:

Do NOT:
- appoint participants;
- select quorum as active;
- create trust root;
- create keys/credentials;
- select attestor;
- select backend/host/operator;
- activate profile;
- activate Project Source;
- authorize live WRITE/CAS;
- deploy;
- claim CHECKPOINT_DURABLE;
- unblock EOM pilot;
- authorize memory-layering attempt 3.

Return one standalone immutable candidate to KOO with exact readback.

Expected terminal:

PASS_SHT_STP_C_MULTIPARTY_GOVERNANCE_MODEL_DESIGN_R01_READY_FOR_REVIEW

or exact BLOCKED_/FAIL_.

After immutable result + exact readback + return KOO, STOP.
