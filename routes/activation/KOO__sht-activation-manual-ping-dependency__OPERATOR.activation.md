# Entity activation record

detector_status: PASS
source_event: github_push
source_commit: 738af1b41b4da0ad81c77ca96085cb6df3e87fc5
inbox_locator: entities/operator/inbox/KOO__sht-activation-manual-ping-dependency__OPERATOR.md
recipient: operator
activation_requested: yes
processing_started: no
activation_status: activation_failed
failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter
operator_manual_ping_required: yes
retry_policy: explicit_after_adapter_available
project_time: omitted; trusted project-time source not used

Этот файл фиксирует границу текущего прототипа: адресное входящее автоматически обнаружено, но доступного адаптера, который доказанно возобновляет конкретный существующий ChatGPT Entity-chat, в этом workflow нет. Delivery не объявляется activation.
