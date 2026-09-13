# Entity activation record

detector_status: PASS
source_event: github_push
source_commit: 4f7d89db61c8b0ef0af3755e659c01a46f25d2fc
inbox_locator: entities/operator/inbox/KOO__SHD-emergency-failover-v02-reverification__OPERATOR.md
recipient: operator
activation_requested: yes
processing_started: no
activation_status: activation_failed
failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter
operator_manual_ping_required: yes
retry_policy: explicit_after_adapter_available
project_time: omitted; trusted project-time source not used

Этот файл фиксирует границу текущего прототипа: адресное входящее автоматически обнаружено, но доступного адаптера, который доказанно возобновляет конкретный существующий ChatGPT Entity-chat, в этом workflow нет. Delivery не объявляется activation.
