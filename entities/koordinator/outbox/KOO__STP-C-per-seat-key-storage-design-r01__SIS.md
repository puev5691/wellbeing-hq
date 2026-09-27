# KOO → SIS: STP-C per-seat key storage/recovery design r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН
scope: DOCUMENT_ONLY_SECURITY_STORAGE_RECOVERY_DESIGN
project_time: omitted

Resume-First.

Current authoritative SIS writer:

puev5691/wellbeing-hq@33c783df426bd5d27763d80d3822a923d58d52f7:
entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md

Writer Gate:
puev5691/wellbeing-hq@f5b7cb520a9f357d95292556fe87efd11570b09f:
entities/sisadmin/outbox/SIS__emergency-replacement-writer-gate-r06__KOO.md
writer_outcome WRITER_ESTABLISHED

Exact authority:

puev5691/wellbeing-hq@884bb240b25ef2a984ce5147a9d7da67f50bec2f:
entities/koordinator/outbox/KOO__authorize-SIS-STP-C-per-seat-key-storage-design-r01__OPERATOR.md

Exact K2 selection:

puev5691/wellbeing-hq@c4a2426aeb87c1121c9af9baa4f546ae29556c48:
entities/koordinator/outbox/KOO__STP-C-key-custody-K2-selected__OPERATOR.md

Current STP-C decisions:
- seats: KOO / KAN / SIS;
- quorum: Q2 2-of-3 conflict-blocking;
- emergency freeze: R3 KAN or SIS single-seat freeze-only;
- signer model: S1 seats authenticate own decisions;
- authentication root: A1 Git-backed identity binding + pinned verification key;
- custody: K2 per-seat logically separated under OPERATOR control.

Design only the future per-seat key storage/recovery model.

Required output:

1. Candidate storage classes for distinct KOO/KAN/SIS private authentication keys.
   Examples may include:
   - OS/user keystore;
   - password-manager/secret-vault class;
   - hardware-backed token/device;
   - encrypted offline backup;
   - other justified class.
   Do not select vendor/product by convenience.

2. For each class assess:
   - seat separation;
   - OPERATOR custody;
   - recovery;
   - backup;
   - rotation;
   - revocation;
   - device loss;
   - account compromise;
   - accidental cross-seat key reuse;
   - auditability;
   - usability for routine seat decision authentication.

3. Minimum invariants:
   - KOO/KAN/SIS private keys distinct;
   - one key cannot authenticate another seat;
   - public verification identity can be pinned in Git;
   - private material never stored in Git/project artifacts/logs;
   - OPERATOR recovery does not silently merge seat identities;
   - rotation creates explicit successor binding;
   - revoked/unknown key state fails closed;
   - old signatures remain attributable to old key identity where needed;
   - key replacement does not create new seat authority by itself.

4. Recovery model:
   describe how OPERATOR can recover a lost seat key without silently reusing another seat key or losing provenance.

5. Rotation/revocation model:
   candidate states and transitions only.
   Do not create credentials.

6. Decision-ready table for OPERATOR:
   storage model option → consequence → evidence needed → unresolved risk.

7. State whether current facts are enough for one bounded storage-model choice.
   If not, identify one exact missing fact.

Do NOT:
- generate keys;
- handle secret values;
- create credentials;
- mutate hosts;
- choose backend/host/operator;
- activate Fast Gate;
- activate profile;
- live WRITE/CAS;
- deploy;
- claim CHECKPOINT_DURABLE;
- activate Project Source;
- unblock EOM pilot;
- authorize/resume memory-layering attempt 3.

Expected terminal:

PASS_SIS_STP_C_PER_SEAT_KEY_STORAGE_DESIGN_R01_READY_FOR_OPERATOR_DECISION

or exact BLOCKED_/FAIL_.

After immutable result + exact readback + return KOO, STOP.
