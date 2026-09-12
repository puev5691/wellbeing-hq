# Entity activation record

detector_status: PASS
source_event: github_push
source_commit: 764a74ae8826461f71dd5de3ec2f030691c624fe
inbox_locator: entities/operator/inbox/SHT__telegram-phase0-koo-result-review-activation-gap__OPERATOR.md
recipient: operator
activation_requested: yes
processing_started: no
activation_status: activation_failed
failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter
operator_manual_ping_required: yes
retry_policy: explicit_after_adapter_available
project_time: omitted; trusted project-time source not used

Этот файл фиксирует границу текущего прототипа: адресное входящее автоматически обнаружено, но доступного адаптера, который доказанно возобновляет конкретный существующий ChatGPT Entity-chat, в этом workflow нет. Delivery не объявляется activation.
