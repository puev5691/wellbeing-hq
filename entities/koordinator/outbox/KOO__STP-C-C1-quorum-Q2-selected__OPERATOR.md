# KOO record: OPERATOR selects STP-C C1 quorum Q2

status: OPERATOR_QUORUM_SELECTION_RECORDED
project_time: omitted

Exact OPERATOR token:

SELECT_STPC_C1_QUORUM_Q2_2_OF_3_CONFLICT_BLOCKING

Selected seats:
GOV = KOO
NORM = KAN
INFRA = SIS

Selected quorum:
Q2 — 2 of 3 with conflict blocking.

Operational meaning:
- two current APPROVE decisions may satisfy candidate quorum;
- any contradictory current REJECT blocks admission;
- silence/absence is not approval;
- stale/unknown currentness blocks;
- no casting vote;
- no timeout-as-consent.

Established boundary:
KOO/KAN/SIS remain one shared technical control/failure domain.
This quorum provides governance/decision diversity only.
It does not create technical threshold independence.

Not selected/authorized:
- emergency revoke rule;
- authentication root;
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
memory-layering attempt 3 remains NOT_AUTHORIZED.

Decision basis:
puev5691/wellbeing-hq@f76fba77b86cd4cee7ad614903c35c4b6a5086ba:
entities/koordinator/outbox/KOO__STP-C-C1-quorum-decision-r01__OPERATOR.md
