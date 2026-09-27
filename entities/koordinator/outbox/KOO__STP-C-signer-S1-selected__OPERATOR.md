# KOO record: OPERATOR selects STP-C signer model S1

status: OPERATOR_SIGNER_MODEL_SELECTION_RECORDED
project_time: omitted

Exact OPERATOR token:

SELECT_STPC_SIGNER_S1_SEATS_AUTHENTICATE_OWN_DECISIONS

Current governance:
- composition: C1 GOV/NORM/INFRA
- seats: GOV=KOO, NORM=KAN, INFRA=SIS
- ordinary quorum: Q2 2-of-3 conflict-blocking
- emergency freeze: R3 KAN or SIS single-seat freeze-only

Selected signer model:
S1 — each governance seat authenticates its own decision evidence.

Meaning:
- KOO authenticates its own GOV decision evidence;
- KAN authenticates its own NORM decision evidence;
- SIS authenticates its own INFRA decision evidence;
- no separate mechanical attestor is introduced at this stage.

Boundary:
this does NOT establish independent signing domains, keys, credentials, or technical independence.
KOO/KAN/SIS remain one shared technical control/failure domain.

Not selected/authorized:
- authentication-root technology;
- key custody;
- concrete credentials;
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
puev5691/wellbeing-hq@725f28be4ea96e9a14c7c09121617bae0052990c:
entities/koordinator/outbox/KOO__STP-C-signer-attestor-separation-decision-r01__OPERATOR.md
