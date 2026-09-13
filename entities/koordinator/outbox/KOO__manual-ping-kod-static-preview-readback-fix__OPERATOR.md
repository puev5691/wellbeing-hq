# KOO → OPERATOR: exact dependency — manual ping KOD for static-preview readback fix

status: EXTERNAL_DEPENDENCY
blocked_stage: KOD bounded R1/R2 readback-evidence correction

task: `entities/koordinator/outbox/KOO__info-entry-static-preview-readback-fix-v02__KOD.md`
task_commit: `83f5f87842296b1a9f9b0533f734238dc6948967`
KOD_inbox: `entities/koder/inbox/KOO__info-entry-static-preview-readback-fix-v02__KOD.md`
inbox_commit: `76aa795e4811b8ea2970fb2b245efab3e7afd42c`
activation_record: `routes/activation/KOO__info-entry-static-preview-readback-fix-v02__KOD.activation.md`
activation_commit: `264f0db62b1eb86a0cacbc8f4940ea798fd78977`
activation_status: `activation_failed`
failure_reason: `exact_entity_chat_resume_not_supported_by_current_adapter`
processing_started: no

## Required operator action

Manually resume/ping the existing KOD / КОДЕР Entity-chat so that it begins with its required GitHub preflight, scans its GitHub inbox and processes the already-routed bounded correction task above.

The correction scope remains exactly R1/R2 from the accepted WEB review. Do not recreate the task, do not widen KOD authority, and do not infer processing, receipt, corrected-package existence or acceptance from repository placement or activation request alone.

After KOD actually processes the task, its normal Exchange Gate result path is sufficient. This dependency note creates no acceptance and authorizes no production, deployment, publication or credentials use.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать точную внешнюю зависимость, мешающую началу bounded KOD R1/R2 correction
СТАТУС: blocked_waiting_operator_manual_ping
