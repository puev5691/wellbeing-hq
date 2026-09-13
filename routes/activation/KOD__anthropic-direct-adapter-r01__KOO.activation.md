# Entity activation record

detector_status: PASS
source_event: github_push
source_commit: 8a5e55f337ad3255d2906dc4ae71f83ac6c2882f
inbox_locator: entities/koordinator/inbox/KOD__anthropic-direct-adapter-r01__KOO.md
recipient: koordinator
activation_requested: yes
processing_started: no
activation_status: activation_failed
failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter
operator_manual_ping_required: yes
retry_policy: explicit_after_adapter_available
project_time: omitted; trusted project-time source not used

Этот файл фиксирует границу текущего прототипа: адресное входящее автоматически обнаружено, но доступного адаптера, который доказанно возобновляет конкретный существующий ChatGPT Entity-chat, в этом workflow нет. Delivery не объявляется activation.
