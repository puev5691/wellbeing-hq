# KOO → OPERATOR: STP-C C1 seat-holder appointment decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

Exact selected composition:
C1 — GOV / NORM / INFRA

Exact selection record:
puev5691/wellbeing-hq@3dc60f768223c85de1efe1bc460b3d26864008fe:
entities/koordinator/outbox/KOO__STP-C-select-C1-governance-composition__OPERATOR.md

Established technical boundary:
KOO/KAN/SHT/SIS = ONE SHARED TECHNICAL CONTROL / FAILURE DOMAIN.
Seat assignment below is governance assignment only.

## Candidate exact seat mapping

GOV seat:
KOO / КООРДИНАТОР

Basis:
approved KOO role covers priority/dependency reconciliation, routing and governance coordination.

NORM seat:
KAN / КАНЦЕЛЯР

Basis:
approved KAN role covers normative/formal boundaries and independent review.
KAN independently reviewed the STP-C model.
SHT designed the STP-C organizational model, so using KAN for the normative seat preserves a cleaner author/reviewer separation.

INFRA seat:
SIS / СИСАДМИН

Basis:
approved SIS role covers infrastructure/security/runtime/service boundaries.

## Decision meaning

If approved, these three Entity roles become the designated governance seats for the C1 STP-C model:

GOV = KOO
NORM = KAN
INFRA = SIS

This does NOT:
- make them technically independent;
- select quorum;
- activate any profile;
- grant signing/attestation authority;
- create credentials;
- alter current-writer authority;
- grant live WRITE/CAS.

Each seat still acts only through its existing role/current-writer/task authority boundaries.

## OPERATOR response

Approve exact mapping:
APPOINT_STPC_C1_SEATS_KOO_KAN_SIS

or defer/decline:
DEFER_STPC_C1_SEAT_APPOINTMENT

No quorum decision is part of this gate.

Not authorized:
- quorum;
- emergency revoke;
- root/signing technology;
- credentials;
- signer/attestor;
- backend/host/operator;
- Fast Gate;
- profile activation;
- live WRITE/CAS;
- deployment;
- CHECKPOINT_DURABLE;
- Project Source activation.

EOM pilot remains BLOCKED.
Memory-layering attempt 3 remains NOT_AUTHORIZED.
