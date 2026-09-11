# Bounded Work E2E recovery input

entity_id: `ent:KOD-E2E-WORK-01`
task_id: `task:activation-work-e2e-01`
recovery_role: immutable recovery seed
production: false

## Recovery contract

A fresh processing run must:

1. verify this file by exact commit and blob identity supplied by the manifest;
2. retain the same Entity ID and Task ID only as logical recovery inputs;
3. create a new Instance ID for this processing run;
4. reject any claim that the new Instance ID equals a pre-existing chat/runtime instance unless separately proven;
5. fail closed if any required locator cannot be resolved exactly.

Expected recovery token: `WB-HQ-KOD-E2E-RECOVERY-01`

Project time omitted; trusted project-time source not used.
