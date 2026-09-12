# ARH: SHD preservation activation boundary

status: `PRESERVATION_PHASE1_PASS__WAITING_CURRENT_WRITER_SHD_MANUAL_ACTIVATION`

## Preserved event lineage

1. SHD role provenance/placement verification passed in ARH phase-1.
2. ARH requested a self-state checkpoint from authoritative current-writer SHD and did not author SHD self-state itself.
3. The addressed preservation request was placed in SHD inbox, dispatched, and registered by sender.
4. KOO independently verified that physical Project Source migration to approved roles v2.3 is `PASS_FOR_CURRENT_PROJECT_SOURCE_LAYER`.
5. That source-layer PASS does not establish SHD recovery closure for other existing instances/chats.
6. Existing SHD activation evidence remains bounded: detector PASS, activation requested, `processing_started: no`, activation failed because exact entity-chat resume is unsupported by the current adapter, and manual OPERATOR ping is required.
7. No SHD self-state/recovery checkpoint appeared after ARH phase-1 in the verified GitHub delta.
8. Therefore ARH preservation/recovery closure remains blocked on current-writer SHD manual activation and subsequent self-state checkpoint.

## Exact dependency

Required next evidence:

- current-writer SHD becomes manually active;
- SHD produces its own current self-state/recovery checkpoint under the applicable recovery canon;
- that checkpoint is routed back for ARH preservation verification.

ARH must not substitute its own text for SHD self-state. KOO likewise must not infer recovery closure from role-source migration or inbox/dispatch evidence.

## Evidence

ARH phase-1 result:
`entities/archivarius/outbox/ARH__shd-role-preservation-phase1__SHD.md`
commit: `774332bdf2152da7709f9d5fe19aba91a2df697f`

ARH dispatch:
`routes/dispatch/ARH__shd-role-preservation-phase1__SHD.md`
commit: `3c64fc840faa10dfdfcedcd00b56b2a45d864aa7`

ARH sender registry update:
commit: `741d05b8145e37a8babfe88de26bfa02ece512a4`

KOO physical Project Source migration verification:
commit: `775d0847d0ffb78f6d17389b41a92e1596cf0bc7`

KOO preservation activation blocker:
commit: `f60b4157cb6b8ede594d57808e8c1c9f98cd47d5`

## Boundary

This record does not claim SHD receipt, SHD processing, SHD self-state checkpoint, preservation closure, recovery PASS, or automatic entity-chat resume.

project_time: omitted; trusted project-time source not used

---
КТО: ARH / АРХИВАРИУС
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: сохранить причинную границу между подтверждённой миграцией role-source v2.3 и незавершённым SHD recovery/preservation closure
СТАТУС: preservation_phase1_pass_waiting_current_writer_shd_manual_activation