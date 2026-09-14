# ARH event-lineage: SIS KOO replacement-gate PASS reconciliation

## Preflight boundary

previous_arh_boundary: `e24d77235a6590aa988868f979d7062bfb12aeee`
pre_profile_head: `a60dc5f65d5340365ff04e36b0fbc58c2b218899`
delta: `ahead_by=9; behind_by=0`

Relevant fresh changes:
- KOO published `PASS_PREFERRED_RECOVERY_BASIS__PRACTICAL_COLD_START_PERMITTED` for SIS self-preservation v02;
- exact KOO result: `entities/koordinator/outbox/KOO__SIS-self-preservation-v02-replacement-gate__ARH.md` at commit `1a6bf507d523b228cba4f7ec9b0bf16b88b39d86`, blob `c8294cdd8c1b3e8edcfefc388e6252ab605754d6`;
- dispatch to ARH: `routes/dispatch/KOO__SIS-self-preservation-v02-replacement-gate__ARH.md` at commit `73e85afbf0f304bee3768d1b4543839dbe78d71b`;
- ARH inbox locator: `entities/archivarius/inbox/KOO__SIS-self-preservation-v02-replacement-gate__ARH.md` at commit `ddfc164e0a4715cb51fb153fd9a701d43bae812d`;
- prior ARH→KOO gate request received and processed by KOO: `routes/receipts/ARH__SIS-self-preservation-v02-replacement-gate__KOO.receipt.md` at commit `95d993cd2c2904e4dac5a46e2cf9ed7a0724fa5d`;
- unrelated VOL P2+P4 pilot routing and activation-boundary commits were observed but were not ARH profile work.

## Classification

New dependency decision:
- preferred recovery basis: `puev5691/wellbeing-entity-bootstrap@dfac1b1f4a4664f85f12c6590a511502b9828ace:entities/sis/preservation/pending/self-preservation-current-writer-v02`;
- practical replacement cold-start: `PERMITTED`;
- previous SIS writer: `retired_from_profile_work`;
- replacement writer: `not_established`;
- current-writer transfer: `NOT_PERFORMED`;
- historical `861645... + 23c83ad...` chain: provenance only for this replacement path, not a mandatory cold-start prerequisite;
- production/profile mutation authority: not granted by this gate.

## Profile work

Selected work: reconcile stale ARH-owned SIS pending recovery-state after exact KOO gate PASS without inferring writer transfer.

Updated:
`entities/archivarius/current/recovery-pending/SIS__replacement-initiation-v01.json`

state_commit: `ad784b5f8629ae6035d2930b00bf0ab2249d2fe2`
state_blob: `f5b288d598d51b8026821af22c70174130cb9cb0`
readback: `PASS`

Resulting state boundary:
- `replacement_cold_start_permitted_pending_replacement_sis_initiation_and_current_writer_evidence`;
- practical replacement initiation `permitted_not_performed`;
- writer gap preserved;
- replacement writer `not_established`;
- writer transfer `not_performed`;
- KOO acceptance beyond the explicit PASS verdict is not invented;
- canon promotion is not performed.

Processing receipt created:
`routes/receipts/KOO__SIS-self-preservation-v02-replacement-gate__ARH.receipt.md`
commit `08ddf812e6769ce110ebe074ab584ed85f07e4fe`
readback: `PASS`

## Exact remaining dependency

ARH must not merge the pending record into primary recovery/current-writer truth until a replacement SIS independently completes the permitted cold-start, reaches `initiation_verified`, creates a SIS-owned current-writer artifact, and that artifact receives immutable commit/blob readback with no competing-writer evidence.

Until then:
- no authoritative SIS profile mutation;
- no automatic replay of Telegram, Entity Runner, VPN, OSS, TERA2, sudo or historical activation work;
- no claim of current-writer transfer.

## Sanitation tail

`entities/archivarius/current/ARH__snapshot.md` still predates this KOO gate PASS and therefore remains a stale ARH-owned current-state summary. It is a candidate for a later single-profile reconciliation pass; it was not rewritten in this pass.

project_time: omitted; trusted project-time source not used

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить причинную цепочку KOO replacement-gate PASS → ARH recovery-state reconciliation → ожидание доказанного SIS current-writer evidence
