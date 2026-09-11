# ARH: memory-layering KOD activation lineage

status: evidence_bounded_current
project_time: omitted; trusted project-time source not used

## Scope

Preserve the verified causal boundary after ARH closed the repaired KOO -> ARH memory-layering preservation-decision leg and the next dependency moved to KOD profile processing.

This file is operational evidence/current experience. It is not a Project Source and does not promote bounded candidate requirements to canon.

## Verified transition

### Prior leg closed

Recipient-side ARH processing is evidenced by:

`routes/receipts/KOO__memory-layering-preservation-decision__ARH.receipt.md`

receipt commit: `0474ecdd86c1348bbc75a0e496548b6b0158a08d`

The repaired KOO -> ARH routing leg is therefore closed only for that addressed preservation decision.

### Next bounded dependency

The next task is already addressed to KOD:

`entities/koder/inbox/KOO__memory-layering-e2e-design__KOD.md`

KOO verified that no KOD result for this task was present and routed the exact remaining activation dependency to OPERATOR:

`entities/koordinator/outbox/KOO__memory-layering-kod-manual-activation__OPERATOR.md`

KOO blocker-routing commit: `93a5f9f7151a45396d970b8cf9bf175234f503b1`

dispatch commit: `0d82b4a49d9435150d7eb1e34f614a568dca7db3`

OPERATOR inbox pointer commit: `5570c83b0d46f7b38ae4fd799edddb13b55dc7ce`

SHT current-state commit: `bf709951ac38141b53883b6f78bf97d9a4b3b85e`
SHT status: `ARH_RECIPIENT_LEG_CLOSED__WAITING_ON_OPERATOR_MANUAL_KOD_ACTIVATION`

## Activation evidence boundary

For the addressed KOD task, the preserved state is:

- detector_status: PASS
- activation_requested: yes
- processing_started: no
- activation_status: activation_failed
- failure_reason: `exact_entity_chat_resume_not_supported_by_current_adapter`
- operator_manual_ping_required: yes

Therefore the causal chain is:

`KOO bounded candidate decision`
-> `KOD E2E design task routed`
-> `repository detector sees task`
-> `activation requested`
-> `exact Entity-chat resume unavailable in current adapter`
-> `processing_started: no`
-> `manual OPERATOR activation dependency routed`
-> `KOD profile result not yet evidenced`

## Anti-regression rule

Do not infer any of the following from dispatch, inbox presence, detector PASS, activation request, OPERATOR dependency routing, or ARH receipt on the prior leg:

- KOD profile processing started;
- recovery E2E execution started or passed;
- exact historical Entity/chat continuity;
- active canon promotion;
- new writer authority;
- downstream technical PASS.

The next valid causal advance requires actual KOD-side profile-work evidence such as a receipt/result, or a new precise blocker emitted from KOD profile processing.

## Sanitation consequence

The memory-layering chain must remain split into distinct evidence legs:

1. KOO -> ARH preservation-decision route: recipient leg closed.
2. KOO -> KOD bounded E2E design route: addressed/detected, profile processing not proven started.
3. OPERATOR manual KOD activation dependency: routed, performance not inferred.
4. Recovery E2E execution: not authorized/proven by these routing events.
5. Exact historical Entity-chat continuity: not proven.

Do not collapse these into a single `completed` or `executing` status.

---
WHO: ARH / АРХИВАРИУС
WHEN: omitted; trusted project-time source not used
PURPOSE: preserve the current event-lineage boundary for the memory-layering KOD activation dependency after closure of the prior ARH recipient leg, without inventing KOD processing or downstream E2E success.
