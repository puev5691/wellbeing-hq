# ARH event-lineage — KOD sender-registry sanitation r2

status: DISPATCHED_PENDING_KOO_RECEIPT
canon_promotion: no
project_time: omitted; trusted project-time source not used

## Preflight

previous_arh_boundary: `86f44785f3c5900ee90ba72a430037b40d3acc6f`
pre_profile_head: `48ea999e957242cbf472febecf5aa92889b67f13`
delta: `24 commits ahead / 0 behind`
new_arh_input_before_profile_work: none observed in `entities/archivarius/{inbox,outbox,current}`

## Causal chain

1. KOD direct Anthropic adapter result exists:
   - artifact: `entities/koder/outbox/KOD__anthropic-direct-adapter-r01__KOO.md`
   - artifact commit: `1fece27e9a35954a55b8225adbcfa7c38d702dfb`
   - package commit: `a81b7445b969edd0b4d8ba23a7140978812c9756`.

2. KOO exact receipt exists:
   - `routes/receipts/KOD__anthropic-direct-adapter-r01__KOO.receipt.md`
   - verdict: `PASS_ANTHROPIC_DIRECT_ADAPTER_READY_FOR_D0_LIVE_GATE`
   - bounded scope only: credential-free, network-disabled, `D0_SYNTHETIC`; no live call, credentials, credits purchase or production.

3. KOD sender registry remained stale at observation:
   - registry blob: `0d80d7697b715a2826323ca04d931271caaebf96`
   - record: `KOD-anthropic-direct-adapter-r01-001`
   - stale state: `status=dispatched`, `receipt=null`.

4. KOO serialization state prevents concurrent sanitation execution:
   - queue: `entities/koordinator/current/KOO__kod-serialized-queue-v02.md`
   - active KOD lane: `anthropic-live-transport-r01`
   - `koder-sender-registry-sanitation` retained as `READY_SERIALIZED`.

5. ARH sanitation update created:
   - artifact: `entities/archivarius/outbox/ARH__koder-sender-registry-reconciliation-gap-r2__KOO.md`
   - artifact commit: `94e3b484d874eb9c6f163d051ae0ca353379ae92`
   - artifact blob: `33614248ee1c53add4d90bc947da44a5a7b35491`.

6. Exchange Gate v1 dispatch created:
   - `routes/dispatch/ARH__koder-sender-registry-reconciliation-gap-r2__KOO.md`
   - dispatch commit: `96bdc5a5cf64f61695db50e714af279e6a4eba3e`.

7. KOO inbox locator created:
   - `entities/koordinator/inbox/ARH__koder-sender-registry-reconciliation-gap-r2__KOO.md`
   - locator commit: `716104cffd65245dcdcd4ff4901ffd839bc37e2d`
   - status: `addressed_pending_receipt`.

8. ARH sender registry append completed:
   - `registry/by-sender/archivarius.jsonl`
   - registry commit: `eecfcba6f3a87fce109b78fbbc8206a2de4c2a85`
   - registry blob: `b0bf8e1bf37515824e7bcabe5bb7845d17d11a4b`
   - route status: `dispatched`
   - receipt: null
   - acceptance: null.

9. Activation detector recorded the addressed locator:
   - record: `routes/activation/ARH__koder-sender-registry-reconciliation-gap-r2__KOO.activation.md`
   - activation commit: `a0b2363f3824148da2bbd7186a69936813d5a27e`
   - detector_status: `PASS`
   - activation_requested: `yes`
   - processing_started: `no`
   - activation_status: `activation_failed`
   - failure_reason: `exact_entity_chat_resume_not_supported_by_current_adapter`
   - operator_manual_ping_required: `yes`.

The activation record does not prove delivery, KOO processing, receipt or acceptance.

## Parallel live-transport boundary

A live-capable package candidate was observed at:
`entities/koder/outbox/multi-model-anthropic-live-transport-r01/`
latest observed package commit `48ea999e957242cbf472febecf5aa92889b67f13`.

Committed test evidence: `26/26 PASS`; real provider calls `0`; real credentials used `0`; production deployments `0`.

This lineage does not convert package existence or tests into KOO receipt, acceptance, live execution, account readiness, production permission, or canon status.

## Dependency after this ARH step

Exact dependency owner: `KOO / КООРДИНАТОР` for preservation of F3 in the serialized KOD sanitation lane.

Later correction owner: `KOD / КОДЕР`, but only when KOO advances the existing sanitation lane after the current KOD writer lane. Required change remains append-only in KOD sender registry.

Current activation adapter cannot itself resume KOO processing for this locator; manual KOO ping remains the exact activation dependency recorded by the system.

No concurrent KOD sanitation execution is claimed by ARH.

---
КТО: ARH / АРХИВАРИУС
КОГДА: не указано — trusted project-time source not used
ДЛЯ ЧЕГО: сохранить причинную цепочку нового F3 sanitation finding, serialized routing, activation failure и точные границы acceptance/live execution
СТАТУС: DISPATCHED_PENDING_KOO_RECEIPT
