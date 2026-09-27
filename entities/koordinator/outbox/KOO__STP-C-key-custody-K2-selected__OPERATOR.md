# KOO record: OPERATOR selects STP-C key custody K2

status: OPERATOR_KEY_CUSTODY_SELECTION_RECORDED
project_time: omitted

Exact OPERATOR token:

SELECT_STPC_KEY_CUSTODY_K2_PER_SEAT_SEPARATED_UNDER_OPERATOR

Selected custody model:
K2 — per-seat logically separated custody under OPERATOR control.

Meaning:
- OPERATOR remains ultimate human custodian/recovery authority;
- KOO, KAN and SIS future authentication keys must be distinct per seat;
- one seat key must not be reused as another seat key;
- storage/recovery/rotation/revocation boundaries must be designed separately per seat.

Established technical boundary preserved:
KOO/KAN/SIS remain one shared technical control/failure domain.
K2 provides seat-specific authentication separation, not independent external trust domains.

Not established:
- concrete storage mechanism;
- key algorithm;
- key generation;
- private-key location;
- backup medium;
- recovery procedure;
- rotation interval;
- revocation transport;
- compromise handling;
- runtime integration.

Not authorized:
- key generation;
- secret storage in GitHub/project artifacts;
- credential creation;
- backend/host/operator selection;
- Fast Gate;
- profile activation;
- live WRITE/CAS;
- deployment;
- CHECKPOINT_DURABLE;
- Project Source activation.

EOM pilot remains BLOCKED.
memory-layering attempt 3 remains NOT_AUTHORIZED.

Decision basis:
puev5691/wellbeing-hq@d51d5d1bec997de5d72320608966e2b5fa5e22da:
entities/koordinator/outbox/KOO__STP-C-key-custody-model-decision-r01__OPERATOR.md
