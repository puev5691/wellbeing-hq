# Entity activation record

detector_status: PASS
source_event: github_push
source_commit: e974bbf4159c881b01a0fd64d0165c893deace0e
inbox_locator: entities/koordinator/inbox/SHT__emergency-preservation-routing-gap__KOO.md
recipient: koordinator
activation_requested: yes
processing_started: no
activation_status: activation_failed
failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter
operator_manual_ping_required: yes
retry_policy: explicit_after_adapter_available
project_time: omitted; trusted project-time source not used

Этот файл фиксирует границу текущего прототипа: адресное входящее автоматически обнаружено, но доступного адаптера, который доказанно возобновляет конкретный существующий ChatGPT Entity-chat, в этом workflow нет. Delivery не объявляется activation.
