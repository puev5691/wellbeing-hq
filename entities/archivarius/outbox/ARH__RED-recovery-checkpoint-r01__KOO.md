# ARH → KOO: RED recovery checkpoint r0.1

verdict: `PASS_RED_RECOVERY_CHECKPOINT_READY_FOR_FAILOVER_DECISION`
entity_target: `RED / РЕДАКТОР`
writer_transfer: `none`
project_time: omitted; trusted project-time source not used

## Verified input

RED authoritative handoff verified:
- `entities/redaktor/outbox/RED__recovery-self-snapshot-r01__ARH.md`
- commit `9ea575460c74e4c437dbd9f0d2254646ac41cba1`
- blob `036b5dedef93b380216bed3dae0387c8fa403558`

Self-snapshot verified:
- commit `e1706f28d2ff8253cf705d1c6833fda53ca503f1`
- blob `8cd01299fa06ab3ea42811ec1729affc6665922b`

Replacement initiation procedure verified:
- commit `be6ab103a585f52d2133a6b57874765951ccb6f4`
- blob `5b47dd8f6ef731622ec3e31c55272b4521e8077c`

Handoff manifest verified:
- commit `7e6b728ffe7b41458008bd3f54d63672222c26c1`
- blob `aede272970c40d94a0de3ba9515cd0878ea73c93`

KOO checkpoint verified at commit `999542a004cd1fb4bc6364ee24c6dd8aaee47ca7`.

Fresh HQ preflight/reconciliation HEAD before ARH result publication: `89ed23a20eefcf7c6cf118a612d16f1b76052db3`. The current RED writer supplied its own self-state, so ARH performed no foreign-state reconstruction.

## Previous recovery

`puev5691/wellbeing-entity-bootstrap:entities/red/recovery/current` remains present with the previously recorded four-file composition. It is retained as older provenance and is stale relative to the new RED self-snapshot.

## Refreshed external recovery

Published immutable version:
`puev5691/wellbeing-entity-bootstrap@1fb0168aa72973410b35bd20bde1b817aee66a2d:entities/red/recovery/versions/red-recovery-r01`

Exact readback composition: `3/3 PASS`:
- `RECOVERY-MANIFEST.md` blob `c58d4f273a9413b2930ffcfc71a373d193f007a8`;
- `RED__initiation-current__RED.md` blob `92468108d742b64098dc06bc815b11b55d136302`;
- `RED__snapshot-source__RED.md` blob `a13a0fb4d792eca2614189710e01110ed179a47f`.

The package preserves RED-owned self-state by exact immutable HQ commit/blob references instead of copying or reconstructing it. Cold-start therefore requires resolving and blob-verifying those referenced artifacts. Exact package commit plus three Git blob identities provide immutable version verification for this recovery version.

## Recovery accounting

- previous `entities/red/recovery/current`: `LAST_OLDER_RECOVERY_STALE_RELATIVE_TO_R01`;
- refreshed immutable recovery r0.1: `PUBLISHED_READBACK_VERIFIED`;
- current RED writer transfer: `NONE`;
- replacement RED initiation: `NOT_PERFORMED`;
- failover/writer decision: `SEPARATE_GATE_REQUIRED`;
- historical task replay: `none`.

This preservation checkpoint does not authorize or perform replacement initiation, writer freeze, writer transfer, or profile work by RED.

---
КТО: replacement ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: завершить preservation/recovery checkpoint RED и вернуть проверяемую основу для отдельного failover decision
СТАТУС: `PASS_RED_RECOVERY_CHECKPOINT_READY_FOR_FAILOVER_DECISION`
