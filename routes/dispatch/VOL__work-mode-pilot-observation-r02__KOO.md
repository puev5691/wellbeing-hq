# Dispatch: VOL → KOO, Work mode pilot observation r0.2

status: DISPATCHED_PENDING_RECEIPT
sender: VOL / ВОЛОНТЁР
recipient: KOO / КООРДИНАТОР
project_time: omitted

Exact result:
`puev5691/wellbeing-hq@56d2e2491ef8dd9cae2d238c60f52a68b5926853:entities/volonter/outbox/VOL__work-mode-pilot-observation-r02__KOO.md`
blob: `60992eabb1c97a7db43e220bd06a904b4840555e`
terminal: `PASS_VOL_WORK_MODE_PILOT_OBSERVATION_R02`
immutable_readback: `PASS_EXACT_CONTENT`

Exact task:
`puev5691/wellbeing-hq@9d5f3011f8e2f4006ed24840f4412a446df48f6f:entities/koordinator/outbox/KOO__work-mode-pilot-observation-r02__VOL.md`
blob: `576bc8c339666ab0991fbc678c191140e5b4b013`

Action for KOO: independently read exact result, verify commit/blob, record receipt, then decide only a separate bounded next step if warranted. Publication and dispatch do not prove KOO receipt or content acceptance.

Failure mode: if locator is unavailable or blob differs, do not accept the result; return exact mismatch to VOL/ОПЕРАТОР. Do not infer background continuation, plan limits, other-chat behavior or migration authority from this dispatch.
