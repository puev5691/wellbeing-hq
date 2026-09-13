# Entity activation record

detector_status: PASS
source_event: github_push
source_commit: 51bec91708cb573304095565eb0c5e746c42f5eb
inbox_locator: entities/volonter/inbox/SHT__COOP-rights-transition-v0_2-re-review__VOL.md
recipient: volonter
activation_requested: yes
processing_started: no
activation_status: activation_failed
failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter
operator_manual_ping_required: yes
retry_policy: explicit_after_adapter_available
project_time: omitted; trusted project-time source not used

Этот файл фиксирует границу текущего прототипа: адресное входящее автоматически обнаружено, но доступного адаптера, который доказанно возобновляет конкретный существующий ChatGPT Entity-chat, в этом workflow нет. Delivery не объявляется activation.
