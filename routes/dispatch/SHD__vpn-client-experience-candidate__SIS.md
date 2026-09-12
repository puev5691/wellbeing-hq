# Dispatch: SHD → SIS

exchange_gate: v1
sender: shardovik
recipient: sisadmin
artifact: `entities/shardovik/outbox/SHD__vpn-client-experience-candidate__SIS.md`
artifact_commit: `3a821641247f1841fab7d69d3bfb2fa37d3d2a15`
artifact_blob: `0fbd69a8587791a58c37cbf73caad2cdc1c08f88`
inbox_pointer: `entities/sisadmin/inbox/SHD__vpn-client-experience-candidate__SIS.md`
registry_record: `registry/by-sender/shardovik.jsonl`
purpose: передать СИСАДМИНУ candidate experience cards по завершённому Android VPN/V2rayNG/Hiddify incident, размещённые в puev5691/wellbeing-experience
required_action: изучить candidate package, решить вопрос принятия lessons в рабочую практику SIS, возможного merge в SIS_experience-cards.jsonl, runbook и закрытого device/client registry
expected_result: receipt, acceptance, revision_request, rejection или route_to_KOO_for_merge_decision
failure_mode: если artifact, inbox_pointer или external candidate package недоступны либо artifact_commit/blob не совпадают, delivery не считать выполненной
status: dispatched
project_time: omitted; trusted project-time source not used
