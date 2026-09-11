# KOO → OPERATOR: manual activation dependency for KOD memory-layering E2E design

## Decision

The repaired KOO → ARH preservation-decision route is now closed at recipient side by an actual ARH receipt. That prior ARH activation blocker is therefore no longer the next actionable dependency.

The current bounded memory-layering validation branch is waiting on KOD profile processing of the already routed design task:

`entities/koder/inbox/KOO__memory-layering-e2e-design__KOD.md`

No KOD result for that task is present in `entities/koder/outbox/`.

## Exact blocker

Activation evidence for the addressed KOD task states:

- detector_status: PASS
- activation_requested: yes
- processing_started: no
- activation_status: activation_failed
- failure_reason: `exact_entity_chat_resume_not_supported_by_current_adapter`
- operator_manual_ping_required: yes

Evidence:
`routes/activation/KOO__memory-layering-e2e-design__KOD.activation.md`

Therefore repository routing is complete, but KOD profile execution is not proven started.

## One required external step

OPERATOR manually opens/activates the existing KOD Entity chat/context and instructs KOD to begin with the mandatory GitHub preflight, then process the already present task `KOO__memory-layering-e2e-design__KOD.md` from its canonical inbox.

Do not resend or rewrite the task unless KOD reports a precise defect in the existing artifact. The expected next evidence is an actual KOD receipt/result produced from profile work.

Until such evidence exists:
- do not claim `processing_started`;
- do not claim recovery E2E execution or PASS;
- do not infer exact historical Entity/chat continuity;
- do not promote the bounded candidate requirements to active canon;
- do not grant new writer authority.

status: `WAITING_ON_OPERATOR_MANUAL_KOD_ACTIVATION`
from_entity: `KOO`
to_entity: `OPERATOR`
document_type: `external-activation-blocker-routing`
project_time: omitted; trusted project-time source not used

---
WHO: KOO / КООРДИНАТОР
WHEN: omitted; trusted project-time source not used
PURPOSE: route the exact remaining external dependency for starting KOD profile work on the bounded memory-layering E2E design after ARH recipient-side routing closure.