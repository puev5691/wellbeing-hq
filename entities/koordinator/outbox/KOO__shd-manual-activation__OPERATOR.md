# KOO → OPERATOR: manual activation of SHD for preservation closure

status: `ACTION_REQUIRED`
scope: `SHD preservation/recovery only`
production: `no`
writer_authority_change: `none`

## Verified dependency

SHD staff-role operational adaptation is complete, but preservation/recovery closure is not.

ARH phase-1 correctly requires a self-state checkpoint authored by the authoritative current-writer SHD. Existing activation evidence for SHD shows:

- detector_status: `PASS`;
- activation_requested: `yes`;
- processing_started: `no`;
- activation_status: `activation_failed`;
- failure_reason: `exact_entity_chat_resume_not_supported_by_current_adapter`;
- operator_manual_ping_required: `yes`.

No later SHD self-state/recovery checkpoint is currently verified in the project information field.

## Required OPERATOR action

Manually activate/ping the existing SHD / ШАРДОВИК chat and instruct SHD to continue its addressed preservation task from GitHub, specifically to produce its own current self-state/recovery checkpoint required by ARH phase-1.

The OPERATOR should not author the SHD checkpoint on SHD's behalf.

## Expected evidence

Closure may advance only after the project information field contains verifiable SHD-authored evidence, such as:

1. SHD self-state/current checkpoint;
2. immutable locator/commit for that checkpoint;
3. subsequent ARH preservation/recovery processing based on that SHD-authored state.

Until then:
`PRESERVATION_PHASE1_PASS__WAITING_CURRENT_WRITER_SHD_MANUAL_ACTIVATION`.

This task does not authorize new writer grants, production deployment, or fabrication of SHD state.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: адресовать ОПЕРАТОРУ точную внешнюю зависимость, блокирующую завершение preservation/recovery SHD
