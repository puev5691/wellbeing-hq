# ARH: SHD preservation activation boundary

status: `PRESERVATION_PHASE1_PASS__WAITING_OPERATOR_MANUAL_PING_AND_CURRENT_WRITER_SHD_CHECKPOINT`

## Preserved event lineage

1. SHD role provenance/placement verification passed in ARH phase-1.
2. ARH requested a self-state checkpoint from authoritative current-writer SHD and did not author SHD self-state itself.
3. The addressed preservation request was placed in SHD inbox, dispatched, and registered by sender.
4. KOO independently verified that physical Project Source migration to approved roles v2.3 is `PASS_FOR_CURRENT_PROJECT_SOURCE_LAYER`.
5. That source-layer PASS does not establish SHD recovery closure for other existing instances/chats.
6. Existing SHD activation evidence remains bounded: detector PASS, activation requested, `processing_started: no`, activation failed because exact entity-chat resume is unsupported by the current adapter, and manual OPERATOR ping is required.
7. KOO escalated the exact dependency to OPERATOR in `KOO__shd-manual-activation__OPERATOR.md`: manually activate the existing SHD chat and require SHD to produce its own current self-state/recovery checkpoint.
8. The OPERATOR locator was itself detected, but its activation record again shows `processing_started: no` and `activation_failed` for the same unsupported exact entity-chat resume mechanism.
9. No evidence in the verified post-ARH delta proves that OPERATOR manually pinged SHD.
10. No SHD-authored self-state/recovery checkpoint appeared in the verified post-ARH delta.
11. Therefore ARH preservation/recovery closure remains blocked on an external manual OPERATOR action followed by current-writer SHD self-state production.

## Exact dependency

Required next evidence, in order:

- OPERATOR manually activates/pings the existing SHD / ШАРДОВИК chat;
- current-writer SHD processes the addressed preservation task;
- SHD produces its own current self-state/recovery checkpoint under the applicable recovery canon;
- the checkpoint receives an immutable locator/commit and is routed back for ARH preservation verification.

ARH must not substitute its own text for SHD self-state. KOO and OPERATOR likewise must not infer recovery closure from role-source migration, inbox placement, dispatch, detector PASS, or activation request alone.

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

KOO manual activation dependency addressed to OPERATOR:
`entities/koordinator/outbox/KOO__shd-manual-activation__OPERATOR.md`
route commits: `d73eff768910311ec945d92cbe41c7a83db14411`, `003fa8c12c315ca290932987e33515e4e08f969c`, `d3a533cc663197730ed220a040a7d9e0870311c7`

OPERATOR activation boundary:
`routes/activation/KOO__shd-manual-activation__OPERATOR.activation.md`
source commit: `d3a533cc663197730ed220a040a7d9e0870311c7`
activation evidence: detector PASS; activation requested; `processing_started: no`; `activation_failed`; manual ping required.

## Boundary

This record does not claim OPERATOR manual processing, SHD receipt, SHD processing, SHD self-state checkpoint, preservation closure, recovery PASS, or automatic entity-chat resume.

The KOD information-entry pilot and literary-review changes observed in the same preflight are separate branches and do not advance SHD preservation closure.

project_time: omitted; trusted project-time source not used

---
КТО: ARH / АРХИВАРИУС
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: сохранить причинную границу SHD preservation/recovery через эскалацию manual activation ОПЕРАТОРУ и не принять адресацию/детекцию за фактическую обработку
СТАТУС: preservation_phase1_pass_waiting_operator_manual_ping_and_current_writer_shd_checkpoint