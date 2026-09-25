# Entity activation record

detector_status: PASS
source_event: github_push
source_commit: e2ab0c7c18cb06d7216814d3e932f533a31e187b
inbox_locator: entities/koordinator/inbox/SIS__shard-checkpoint-s1o2-f2-mazhor-nonsecret-host-inventory-r01__KOO.md
recipient: koordinator
activation_requested: yes
processing_started: no
activation_status: activation_failed
failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter
operator_manual_ping_required: yes
retry_policy: explicit_after_adapter_available
project_time: omitted; trusted project-time source not used

Этот файл фиксирует границу текущего прототипа: адресное входящее автоматически обнаружено, но доступного адаптера, который доказанно возобновляет конкретный существующий ChatGPT Entity-chat, в этом workflow нет. Delivery не объявляется activation.
