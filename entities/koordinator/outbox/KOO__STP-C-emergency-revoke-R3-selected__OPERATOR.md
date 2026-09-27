# KOO record: OPERATOR selects STP-C emergency revoke R3

status: OPERATOR_EMERGENCY_REVOKE_SELECTION_RECORDED
project_time: omitted

Exact OPERATOR token:

SELECT_STPC_REVOKE_R3_NORM_OR_INFRA_SINGLE_FREEZE

Current governance:
- composition: C1 GOV/NORM/INFRA
- seats: GOV=KOO, NORM=KAN, INFRA=SIS
- ordinary quorum: Q2 2-of-3 conflict-blocking

Selected emergency rule:
R3 — NORM or INFRA may individually emergency-FREEZE exact profile/revision/scope.

Meaning:
- KAN may single-seat emergency-freeze;
- SIS may single-seat emergency-freeze;
- KOO alone may NOT emergency-freeze;
- emergency action is FREEZE/REVOKE containment only.

It may NOT:
- approve successor;
- widen scope;
- appoint participants;
- change quorum;
- create task/writer/trust authority;
- reactivate profile;
- bypass ordinary admission governance.

A later unfreeze/restore/replacement requires a separately authorized normal governance path.

Established technical boundary:
KOO/KAN/SIS remain one shared technical control/failure domain.
R3 is governance role separation, not technical independence.

Not selected/authorized:
- authentication root;
- signer/attestor model;
- credentials;
- backend/host/operator;
- Fast Gate;
- profile activation;
- live WRITE/CAS;
- deployment;
- CHECKPOINT_DURABLE;
- Project Source activation.

EOM pilot remains BLOCKED.
memory-layering attempt 3 remains NOT_AUTHORIZED.

Decision basis:
puev5691/wellbeing-hq@871aec5441d7e715f6a48470ba48dfc97ed18000:
entities/koordinator/outbox/KOO__STP-C-emergency-revoke-decision-r01__OPERATOR.md
