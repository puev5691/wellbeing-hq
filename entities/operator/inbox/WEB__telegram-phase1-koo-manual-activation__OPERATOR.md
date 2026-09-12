# WEB → OPERATOR: combined KOO activation for Telegram Phase 0/1

recipient: operator

Artifact:
`entities/webmaster/outbox/WEB__telegram-phase1-koo-manual-activation__OPERATOR.md`

Immutable version:
commit: `6fec6350b442ce225e3925035666c595dbe7d3d7`
blob: `7f76c71474791fb9984cb47e6c72c9185b3e8183`

Required action:
Open/activate the existing KOO chat once and instruct it to process both already delivered WEB inputs:
- `WEB__telegram-phase0-verify-phase1-mapping__KOO.md`;
- `WEB__telegram-experimental-surface-public-readback__KOO.md`.

No file copying is required.

dispatch: `routes/dispatch/WEB__telegram-phase1-koo-manual-activation__OPERATOR.md`

---
created_by: WEB
purpose: one manual KOO activation for both Telegram Phase 0 review and Phase 1 surface mapping inputs
project_time: not_recorded_no_trusted_source