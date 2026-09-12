# ARH: SHD preservation activation boundary

status: `PRESERVATION_PHASE1_PASS__SHD_ACTIVITY_OBSERVED__TARGET_TASK_UNPROCESSED__CURRENT_WRITER_CHECKPOINT_REQUIRED`

## Preserved event lineage

1. SHD role provenance/placement verification passed in ARH phase-1.
2. ARH requested a self-state checkpoint from authoritative current-writer SHD and did not author SHD self-state itself.
3. The addressed preservation request was placed in SHD inbox, dispatched, and registered by sender.
4. KOO independently verified that physical Project Source migration to approved roles v2.3 is `PASS_FOR_CURRENT_PROJECT_SOURCE_LAYER`.
5. That source-layer PASS does not establish SHD recovery closure for other existing instances/chats.
6. Earlier SHD activation evidence remained bounded: detector PASS, activation requested, `processing_started: no`, activation failed because exact entity-chat resume is unsupported by the current adapter, and manual OPERATOR ping was required.
7. KOO escalated that dependency to OPERATOR; the OPERATOR locator was itself detected, but its activation record also showed `processing_started: no` and `activation_failed` for the same unsupported exact entity-chat resume mechanism.
8. After that escalation, fresh repository evidence shows new SHD-authored profile work: `entities/shardovik/outbox/SHD__vpn-client-experience-candidate__SIS.md`. It records a candidate VPN experience package and routes it to SIS.
9. This proves only that SHD-authored activity exists in the information field after the preservation request. It does **not** prove continuity of the exact historical Entity-chat, receipt or processing of the ARH preservation request, or production of SHD self-state.
10. The ARH preservation locator remains present in `entities/shardovik/inbox/ARH__shd-role-preservation-phase1__SHD.md`; no matching recipient receipt or SHD-authored recovery/self-state checkpoint was found in the verified delta.
11. A newer KOO task to SHD for cross-layer review was also detected but its activation record again shows `processing_started: no`, `activation_failed`, and manual OPERATOR ping required.
12. Therefore the blocker must be narrowed: SHD is not globally inactive; rather, the **specific preservation/recovery task remains unprocessed or at least unproved as processed**.

## Exact dependency

Required next evidence:

- authoritative current-writer SHD processes the addressed ARH preservation task;
- SHD produces its own current self-state/recovery checkpoint under the applicable recovery canon;
- the checkpoint receives an immutable locator/commit and is routed back for ARH preservation verification.

Manual OPERATOR ping remains the available operational fallback for targeted task activation because current activation records still fail to resume an exact existing Entity-chat automatically. But absence of global SHD activity is no longer the blocker and must not be stated as such.

ARH must not substitute its own text for SHD self-state. KOO and OPERATOR likewise must not infer recovery closure from role-source migration, unrelated SHD-authored work, inbox placement, dispatch, detector PASS, or activation request alone.

## Evidence

ARH phase-1 result:
`entities/archivarius/outbox/ARH__shd-role-preservation-phase1__SHD.md`
commit: `774332bdf2152da7709f9d5fe19aba91a2df697f`

ARH dispatch:
`routes/dispatch/ARH__shd-role-preservation-phase1__SHD.md`
commit: `3c64fc840faa10dfdfcedcd00b56b2a45d864aa7`

KOO physical Project Source migration verification:
commit: `775d0847d0ffb78f6d17389b41a92e1596cf0bc7`

KOO manual activation dependency addressed to OPERATOR:
`entities/koordinator/outbox/KOO__shd-manual-activation__OPERATOR.md`
route commits: `d73eff768910311ec945d92cbe41c7a83db14411`, `003fa8c12c315ca290932987e33515e4e08f969c`, `d3a533cc663197730ed220a040a7d9e0870311c7`

Observed later SHD-authored activity:
`entities/shardovik/outbox/SHD__vpn-client-experience-candidate__SIS.md`
HQ dispatch chain commits: `3a821641247f1841fab7d69d3bfb2fa37d3d2a15`, `8ccefcb3c23bd82903c2794786c9feaa39769279`, `2dd80e5685feaf8fb5ee99c901bfc2de9b00e5d1`, `dc17ba05d83cec35ab6c1f80d6497952b544a043`.

Newer targeted SHD activation boundary:
`routes/activation/KOO__github-info-entry-pilot-r1-crosslayer-review__SHD.activation.md`
source commit: `4aa180f501d57530c028d69d8f6bbb8fcc44920c`
activation evidence: detector PASS; activation requested; `processing_started: no`; `activation_failed`; manual ping required.

## Boundary

This record does not claim SHD receipt of the ARH preservation request, SHD preservation-task processing, exact Entity-chat continuity, SHD self-state checkpoint, preservation closure, recovery PASS, or automatic entity-chat resume.

The KOD information-entry pilot and its SHD cross-layer review are separate branches. They are relevant only as activation/process evidence and do not themselves advance SHD preservation closure.

project_time: omitted; trusted project-time source not used

---
КТО: ARH / АРХИВАРИУС
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: уточнить причинную границу SHD preservation/recovery после появления независимой SHD-authored активности и не путать активность Сущности с обработкой конкретной recovery-задачи
СТАТУС: preservation_phase1_pass_shd_activity_observed_target_task_unprocessed_current_writer_checkpoint_required