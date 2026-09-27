# KOO record: OPERATOR selects STP-C authentication root A1

status: OPERATOR_AUTH_ROOT_SELECTION_RECORDED
project_time: omitted

Exact OPERATOR token:

SELECT_STPC_ROOT_A1_GIT_BINDING_PINNED_KEY

Current governance:
- composition: C1 GOV/NORM/INFRA
- seats: GOV=KOO, NORM=KAN, INFRA=SIS
- ordinary quorum: Q2 2-of-3 conflict-blocking
- emergency freeze: R3 KAN or SIS single-seat freeze-only
- signer model: S1 seats authenticate own decisions

Selected authentication-root family:
A1 — Git-backed identity/authority binding + pinned verification key.

Meaning:
- seat identity/authority binding is represented by exact immutable Git policy/artifact evidence;
- seat decision evidence is accepted only when authenticated against an explicitly pinned verification identity/key under future approved lifecycle rules;
- Git publication alone does not create seat authority;
- key possession alone does not create governance authority;
- currentness/revocation/scope checks remain required.

Not established:
- key algorithm;
- key generation;
- key custody;
- private-key location;
- recovery path;
- rotation;
- revocation procedure;
- credential implementation;
- runtime isolation.

Established technical boundary preserved:
KOO/KAN/SIS remain one shared technical control/failure domain.
A1 does not create technical independence among them.

Not authorized:
- key/credential creation;
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
puev5691/wellbeing-hq@ba0b3ec00f7f72c06253d619baeb714d113e3fc8:
entities/koordinator/outbox/KOO__STP-C-authentication-root-decision-r01__OPERATOR.md
