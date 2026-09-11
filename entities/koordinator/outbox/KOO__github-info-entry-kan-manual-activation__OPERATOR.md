# KOO → OPERATOR: Stage A KAN manual activation prerequisite

status: EXTERNAL_BLOCKER_REQUIRES_OWNER_ACTION
production_changed: false
repository_settings_changed: false
project_time: omitted; trusted project-time source not used

## Verified evidence

The already-addressed Stage A task exists at:

`entities/kancelar/inbox/KOO__github-info-entry-stageA-kan__KAN.md`

Its activation evidence is:

`routes/activation/KOO__github-info-entry-stageA-kan__KAN.activation.md`

with:

- detector_status: PASS
- activation_requested: yes
- processing_started: no
- activation_status: activation_failed
- failure_reason: `exact_entity_chat_resume_not_supported_by_current_adapter`
- operator_manual_ping_required: yes

SHT independently returned the same dependency in:

`entities/shtabist/outbox/SHT__github-info-entry-stageA-handoff-blocker__KOO.md`
@ `7a46dab898e22b8701325f884c546f9455e582c9`.

## Coordination decision

No further Stage A decomposition is required before KAN processing starts. KOO does not substitute for KAN legal/publication work and does not treat inbox presence or detector PASS as receipt, acceptance, or execution.

The exact external dependency is an owner/manual activation of the KAN Entity processing context because the current adapter cannot resume/start that exact Entity chat automatically.

## Required owner action

Open/activate the KAN (КАНЦЕЛЯР) Entity chat through the available user-facing ChatGPT interface and direct that Entity to begin with its mandatory GitHub preflight and then process the already-addressed inbox task:

`entities/kancelar/inbox/KOO__github-info-entry-stageA-kan__KAN.md`

Do not re-upload or manually transport the task file; GitHub already contains the addressed immutable task route.

## Expected evidence

After KAN actually starts, the repository should later contain independent KAN-side evidence such as a receipt and/or profile result referencing the exact task locator/version. Those later artifacts must be evaluated separately; this document does not declare KAN delivery, receipt, acceptance, or completion.

---
from_entity: KOO
recipient: OPERATOR
document_type: external-activation-prerequisite
project_scope: ШТАБ БЛАГОПОЛУЧИЯ
related_stage: github-information-entry-stageA
blocked_entity: KAN
blocked_task: entities/kancelar/inbox/KOO__github-info-entry-stageA-kan__KAN.md
next_expected_actor: OPERATOR
project_time: omitted; trusted project-time source not used
