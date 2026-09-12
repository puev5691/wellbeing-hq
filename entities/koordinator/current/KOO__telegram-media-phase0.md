# KOO: Telegram Media Gateway Phase 0

status: IMPLEMENTATION_ASSIGNED__WAITING_KOD_MANUAL_ACTIVATION

## Accepted launch boundary

WEB launch request was received and the implementation cycle was opened for Phase 0 only.

KOO task:
`entities/koordinator/outbox/KOO__telegram-media-phase0__KOD.md`

task_commit:
`b994d9a5cc9806a95c321f5ef6bcaaac11ae75f1`

KOD inbox locator:
`entities/koder/inbox/KOO__telegram-media-phase0__KOD.md`

inbox_commit:
`81d07d460c232a588d42a57f525502bc943d5a11`

dispatch:
`routes/dispatch/KOO__telegram-media-phase0__KOD.md`

dispatch_commit:
`1635a4c6af1952865ee2ff026ea667018e99ebb5`

## Current dependency

Fresh WEB evidence records that the activation detector found the KOD inbox task and requested activation, but processing was not proven and activation failed at the known exact-chat resume boundary.

Exact dependency:
`OPERATOR must manually activate the existing KOD chat and instruct KOD to process KOO__telegram-media-phase0__KOD.md`.

WEB escalation artifact:
`entities/webmaster/outbox/WEB__telegram-phase0-kod-manual-activation__OPERATOR.md`

artifact_commit:
`a580416f2a2a8608c8d632d50b994ca40e707456`

The dependency is already addressed to OPERATOR by WEB. KOO does not duplicate that escalation.

## Allowed Phase 0 scope

Only credential-free local/sandbox implementation against the exact WEB Phase 0 contract, using a fake Telegram adapter.

Not authorized:
- real Telegram network calls;
- bot token or webhook secret;
- real channel/group identifiers;
- MTProto;
- production publication;
- repository settings mutation;
- authority/writer-grant expansion.

## Next admissible KOO action

Wait for actual KOD processing/result evidence. On result arrival, independently verify immutable package, manifest/checksums, dependency versions, test evidence, safe receipt fixture, limitations, cleanup/run instructions, and explicit absence of Telegram/network/credential side effects before any acceptance or next-stage routing.

No KOD receipt, processing start, result, PASS, or acceptance is claimed by this checkpoint.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать текущее проверяемое состояние Telegram Media Gateway Phase 0 и точную внешнюю зависимость без дублирования уже выполненной WEB-маршрутизации.
