# WEB → OPERATOR: KOD manual activation for Telegram Media Gateway Phase 0

recipient: operator

Artifact:
`entities/webmaster/outbox/WEB__telegram-phase0-kod-manual-activation__OPERATOR.md`

Immutable version:
commit: `a580416f2a2a8608c8d632d50b994ca40e707456`
blob: `8ea6c0628c26a55022d3e8f643af4a709f21c3e9`

Required action:
Open/activate the existing KOD chat and tell KOD to process the already delivered `KOO__telegram-media-phase0__KOD.md` task.

No file copying is required.

Evidence:
Entity activation detector run `34695954348` found the KOD inbox task and reported `activation_detector=PASS`, but exact existing Entity-chat resume failed and manual ping is required.

dispatch: `routes/dispatch/WEB__telegram-phase0-kod-manual-activation__OPERATOR.md`

---
created_by: WEB
purpose: addressed manual activation dependency for Telegram Media Gateway Phase 0
project_time: not_recorded_no_trusted_source