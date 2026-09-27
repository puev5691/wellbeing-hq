# KOO → OPERATOR: STP-C key custody model decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

Current selected authentication-root family:
A1 — Git-backed identity binding + pinned verification key.

This gate selects only the custody model for future seat authentication keys.
It does NOT generate any key or credential.

## Option K1 — OPERATOR-custodied seat keys

Token:
SELECT_STPC_KEY_CUSTODY_K1_OPERATOR_CUSTODIED

Meaning:
OPERATOR is the sole human custodian/recovery authority for the future authentication keys used by KOO/KAN/SIS seats.

Consequence:
- simplest operational model;
- consistent with current single-account/shared-control reality;
- concentrates compromise/recovery risk in OPERATOR custody;
- does not create technical independence between seats.

Still required later:
- exact per-seat key separation;
- storage mechanism;
- backup/recovery procedure;
- rotation/revocation;
- compromise response.

## Option K2 — per-seat logically separated custody under OPERATOR control

Token:
SELECT_STPC_KEY_CUSTODY_K2_PER_SEAT_SEPARATED_UNDER_OPERATOR

Meaning:
OPERATOR remains ultimate custody/recovery authority, but KOO/KAN/SIS future authentication keys are separately stored and managed per seat so one seat key is not reused as another.

Consequence:
- preserves seat-specific authentication and cleaner revocation/rotation;
- still one human/control domain;
- more operational overhead than K1, but avoids one shared credential masquerading as three seats.

Still required later:
- exact storage boundaries;
- backup/recovery;
- rotation/revocation;
- compromise isolation evidence.

## Option K3 — defer custody until concrete key-storage design

Token:
DEFER_STPC_KEY_CUSTODY_UNTIL_STORAGE_DESIGN

Meaning:
retain A1 architecture but do not choose who/how custody operates until a concrete storage/recovery design exists.

Consequence:
- avoids premature commitment;
- blocks key generation and authenticated seat implementation until resolved.

## Important boundary

No option here authorizes:
- generating keys;
- storing secret values in GitHub/project files;
- using one key for multiple seats unless later explicitly authorized;
- treating key possession as task/current-writer/governance authority;
- backend/host/operator selection;
- Fast Gate/profile activation;
- live WRITE/CAS;
- deployment;
- CHECKPOINT_DURABLE;
- Project Source activation.

EOM pilot remains BLOCKED.
Memory-layering attempt 3 remains NOT_AUTHORIZED.

Return exactly one:
- SELECT_STPC_KEY_CUSTODY_K1_OPERATOR_CUSTODIED
- SELECT_STPC_KEY_CUSTODY_K2_PER_SEAT_SEPARATED_UNDER_OPERATOR
- DEFER_STPC_KEY_CUSTODY_UNTIL_STORAGE_DESIGN
