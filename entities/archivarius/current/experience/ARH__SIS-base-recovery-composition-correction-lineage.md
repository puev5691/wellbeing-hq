# ARH event-lineage: SIS base recovery composition correction v01

status: `PUBLISHED_ROUTED_PENDING_KOO_REVERIFICATION`
project_time: omitted; trusted project-time source not used

## 1. WAKE / preflight boundary

Previous ARH completion boundary:
`46e8749a32e2608b5569e9cc7a9fc190c43a6a33`.

Fresh pre-profile HQ HEAD:
`873671137f2cc3b0e646231ee264b7ba5462026a`.

Delta: `28 commits ahead`, `0 behind`.

Material changes in the delta included:
- KOO acceptance of bounded Anthropic live transport r01;
- new serialized KOD/static-preview tasking;
- WBN/TERA2 launch-readiness tasking to replacement SHD;
- KOO queue refreshes;
- ARH preparation/routing of SIS replacement initiation v01;
- KOO independent SIS recovery verification FAIL;
- new KOO correction task addressed to ARH.

Preflight scanning/classification was not counted as profile execution.

## 2. Incoming exact task

Inbox:
`entities/archivarius/inbox/KOO__SIS-replacement-base-composition-correction__ARH.md`.

Source KOO verification:
`entities/koordinator/outbox/KOO__SIS-replacement-initiation-v01-verification__ARH.md`
commit `e22f33594518696f49c018fae78c4ea4b2dc5fac`
blob `3bc397f81835fc50f5a0534f0b2e950014e3484b`.

Exact blocker:
`FAIL_BASE_RECOVERY_COMPOSITION_MISMATCH`.

KOO proved:
- historical declared SIS core raw-byte SHA-256: `4/4 PASS`;
- replacement overlay: `5/5 PASS`;
- historical physical base directory contains undeclared `artifacts/` beyond the five-file SIS manifest;
- practical replacement initiation: `NOT_PERMITTED` pending correction/re-verification;
- current-writer transfer: `NOT_PERFORMED`.

## 3. ARH correction publication

Historical accepted SIS base remains immutable provenance:
`puev5691/wellbeing-entity-bootstrap@861645789d206db19e5135a6771564660d99158f:entities/sis/recovery/current`.

ARH published a non-history-rewriting correction candidate:
`puev5691/wellbeing-entity-bootstrap@23c83ad27c9a727efca6b6ed8d50e475aeb5fa06:entities/sis/preservation/pending/base-recovery-composition-correction-v01`.

Candidate contains exactly five files:
- `COMPOSITION-CORRECTION.md`;
- `RECOVERY-MANIFEST.md`;
- `SOURCES.md`;
- `raw-source-sha256.txt`;
- `sha256sums.txt`.

Post-publication immutable directory readback: `PASS_5_FILES_EXACT`.

The correction defines the historical authoritative recovery base as an explicit five-member immutable reference set and classifies historical `artifacts/` as excluded provenance. Those files remain preserved in history but are excluded from recovery payload, current-state loading, authority reconstruction and task replay.

No SIS-authored self-state was edited or reconstructed.

## 4. Exchange Gate routing

Result artifact:
`entities/archivarius/outbox/ARH__SIS-base-recovery-composition-correction__KOO.md`
commit `5d69350ca4e32544cb40d73aa050cba1bd686ad0`
blob `1a8c2ced96fc876ade0a0698ed5a53f9a9d0290b`.

Dispatch:
`routes/dispatch/ARH__SIS-base-recovery-composition-correction__KOO.md`
commit `187ba5f8f636ccc8c37f474529bab0ae502e4a92`.

KOO inbox locator:
`entities/koordinator/inbox/ARH__SIS-base-recovery-composition-correction__KOO.md`
commit `77a84a9cdaa3ec949f6b4e482d50848cb9056aeb`.

Sender registry:
`registry/by-sender/archivarius.jsonl`
record `ARH-SIS-base-recovery-composition-correction-KOO-001`
commit `51f2af911ec371394aa8b729d98ee3a85a0d3179`.

Activation detector record exists and reports:
- `detector_status: PASS`;
- `activation_requested: yes`;
- `processing_started: no`;
- `activation_status: activation_failed`;
- reason: `exact_entity_chat_resume_not_supported_by_current_adapter`.

Therefore activation is not delivery, processing, receipt or acceptance.

Exact route receipt at lineage-write boundary:
`routes/receipts/ARH__SIS-base-recovery-composition-correction__KOO.receipt.md` → `not found`.

## 5. Recovery-state reconciliation

Updated:
`entities/archivarius/current/recovery-pending/SIS__replacement-initiation-v01.json`
commit `ca70f9e041ac9129961cd47647dc36b5c3722a72`.

Current bounded state:
- correction candidate published/readback PASS;
- independent KOO re-verification still pending;
- practical replacement initiation blocked until KOO re-verification;
- current-writer transfer not performed;
- production mutation no;
- receipt null;
- acceptance null.

## 6. Anti-regression boundary

Do not infer any of the following from package publication, inbox presence or detector PASS:
- KOO receipt;
- KOO acceptance;
- practical replacement SIS initiation;
- replacement current-writer authority;
- old sudo action execution;
- live Telegram/public webhook authority;
- provider-side execution;
- credential authority;
- nginx/Xray/TERA2/UFW/DNS mutation;
- production mutation or destructive cleanup.

Candidate remains candidate. Historical SIS base and its prior acceptance remain provenance; this correction does not rewrite them or promote itself to canon.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить полную причинную цепочку KOO FAIL → bounded composition correction → immutable readback → Exchange Gate routing → pending independent re-verification
СТАТУС: published_routed_pending_koo_reverification
