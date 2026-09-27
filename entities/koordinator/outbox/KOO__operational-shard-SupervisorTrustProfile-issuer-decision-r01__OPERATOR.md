# KOO → OPERATOR: SupervisorTrustProfile issuer/owner decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

## Decision scope

Choose only the governance model for who may own/issue future SupervisorTrustProfile revisions.

This decision does NOT itself:
- create a trust root;
- create a signing key;
- activate a trust profile;
- authorize live WRITE/CAS;
- select backend/host/operator;
- create credentials;
- authorize deployment;
- establish CHECKPOINT_DURABLE;
- activate Project Sources;
- unblock EOM;
- authorize memory-layering attempt 3.

Exact reviewed candidate:
puev5691/wellbeing-hq@0634480e3a1ec7dd8fe041606747ffe2571404fb:
entities/sisadmin/outbox/SIS__operational-shard-admission-profile-design-r01__KOO.md
blob 2b6abe0cd4e6be66bb687eff00d6bac513ff2dff

Independent governance review:
puev5691/wellbeing-hq@ce2e3849a21c6c91d53cfa0bb31aa6c4ca98e7c0:
entities/shtabist/outbox/SHT__operational-shard-admission-profile-r01-governance-review__KOO.md
blob 4eab33263398b8489fa7eab58bba08921059ae78

## Exact alternatives

### STP-A — OPERATOR-approved project profile

Meaning:
- every active trust-profile revision requires explicit OPERATOR approval;
- a designated project process may technically maintain/publish the immutable artifact under that approval;
- the technical maintainer does not gain independent authority to change trust policy.

Consequence:
- strongest direct human control;
- slower revocation/profile-change workflow;
- no new autonomous trust authority is created.

Evidence still required before any implementation:
- exact maintenance role/process;
- immutable profile schema/versioning;
- revocation/update workflow;
- authentication-root design;
- signer/key custody if signing is used;
- independent review of the concrete profile.

Decision token:
SELECT_STP_A_OPERATOR_APPROVED_PROJECT_PROFILE

### STP-B — dedicated trust-profile authority/service

Meaning:
- create a separately governed narrow authority/service allowed to issue/sign trust-profile revisions within an approved delegation.

Consequence:
- faster operational update/revocation path;
- creates a new high-value authority and security dependency;
- requires its own recovery, Writer/authority boundary, key custody and audit.

Evidence still required before implementation:
- exact role/service design;
- delegation scope;
- signing/root-key custody;
- revocation and compromise recovery;
- lifecycle/recovery/current-writer model;
- independent SHT/SIS/SHD review.

Decision token:
SELECT_STP_B_DEDICATED_TRUST_AUTHORITY

### STP-C — multi-party approval profile

Meaning:
- a trust-profile revision becomes valid only with evidence from two or more separately governed approval roles/processes.

Consequence:
- reduces single-authority risk;
- increases coordination and availability cost;
- requires exact quorum and conflict/failure semantics.

Evidence still required before implementation:
- exact participant roles;
- quorum rule;
- conflict/deadlock behavior;
- revocation under partial availability;
- signing/root-key arrangement;
- independent governance/security review.

Decision token:
SELECT_STP_C_MULTIPARTY_APPROVAL_PROFILE

## Current status

STP-A: CANDIDATE
STP-B: CANDIDATE
STP-C: CANDIDATE

No default.
No ordering preference.
No option is active until OPERATOR selects one and a subsequent bounded design/review chain produces the required concrete evidence.

## Expected OPERATOR response

Return exactly one of:
- SELECT_STP_A_OPERATOR_APPROVED_PROJECT_PROFILE
- SELECT_STP_B_DEDICATED_TRUST_AUTHORITY
- SELECT_STP_C_MULTIPARTY_APPROVAL_PROFILE
- REJECT_ALL_STP_OPTIONS_R01

After one selection, KOO will fresh-reconcile and open only the next bounded design/evidence gate for that selected model.
