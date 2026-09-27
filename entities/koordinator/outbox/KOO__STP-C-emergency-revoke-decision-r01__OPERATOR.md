# KOO → OPERATOR: STP-C emergency revoke decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

Current governance state:
- composition: C1 GOV/NORM/INFRA
- seats: KOO / KAN / SIS
- ordinary quorum: Q2 2-of-3 conflict-blocking

Exact quorum record:
puev5691/wellbeing-hq@f260cdb49a7bfacef90515bde4677fb92dc20e27:
entities/koordinator/outbox/KOO__STP-C-C1-quorum-Q2-selected__OPERATOR.md

Emergency revoke is a separate decision.

Purpose:
define how an already admitted profile may be urgently FROZEN/REVOKED when waiting for the ordinary 2-of-3 path would be unsafe.

Hard boundary:
emergency revoke may ONLY remove/freeze authority.
It may NOT:
- approve a successor;
- widen scope;
- appoint participants;
- change quorum;
- create writer/task/trust authority;
- reactivate a profile.

## Option R1 — same quorum as ordinary admission

Token:
SELECT_STPC_REVOKE_R1_SAME_Q2_2_OF_3

Meaning:
urgent revoke/freeze also requires 2 of 3 current valid revoke decisions.

Consequence:
- symmetric and simple;
- lower risk of one mistaken revoker causing outage;
- slower containment if one or two seats are unavailable.

## Option R2 — any one seat may emergency-freeze

Token:
SELECT_STPC_REVOKE_R2_ANY_1_OF_3_FREEZE_ONLY

Meaning:
any one current valid seat may place exact profile/revision/scope into emergency FROZEN state.

Important:
- this is FREEZE only;
- it cannot permanently revoke/replace/activate anything by itself;
- ordinary governance is required to resolve and either revoke permanently or restore through a separate authorized path.

Consequence:
- fastest containment;
- one mistaken/compromised seat can cause denial of service;
- cannot grant privilege.

## Option R3 — role-constrained single-seat freeze

Token:
SELECT_STPC_REVOKE_R3_NORM_OR_INFRA_SINGLE_FREEZE

Meaning:
only NORM (KAN) or INFRA (SIS) may individually emergency-freeze.
GOV (KOO) alone may not.

Consequence:
- fast containment by review/security functions;
- avoids routing/governance seat unilaterally freezing;
- KAN or SIS compromise/error can still cause denial of service;
- still freeze-only.

## Defer

Token:
DEFER_STPC_EMERGENCY_REVOKE_DECISION

## Not part of this gate

No:
- root/signing technology;
- signer/attestor;
- credentials;
- backend/host/operator;
- Fast Gate;
- profile activation;
- live WRITE/CAS;
- deployment;
- CHECKPOINT_DURABLE;
- Project Source activation.

EOM pilot remains BLOCKED.
Memory-layering attempt 3 remains NOT_AUTHORIZED.

Return exactly one token:
- SELECT_STPC_REVOKE_R1_SAME_Q2_2_OF_3
- SELECT_STPC_REVOKE_R2_ANY_1_OF_3_FREEZE_ONLY
- SELECT_STPC_REVOKE_R3_NORM_OR_INFRA_SINGLE_FREEZE
- DEFER_STPC_EMERGENCY_REVOKE_DECISION
