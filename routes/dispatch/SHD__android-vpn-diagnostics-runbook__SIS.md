# Dispatch: SHD → SIS

exchange_gate: v1
sender: shardovik
recipient: sisadmin
artifact: `entities/shardovik/outbox/SHD__android-vpn-diagnostics-runbook__SIS.md`
artifact_commit: `04cb499ad42087ad08353b9ffab27ed17d21d5cf`
artifact_blob: `93dd45f5e0281761e691ef5212fd33d995a45557`
inbox_pointer: `entities/sisadmin/inbox/SHD__android-vpn-diagnostics-runbook__SIS.md`
registry_record: `registry/by-sender/shardovik.jsonl`
external_candidate: `puev5691/wellbeing-experience:experience/candidates/sis/android-vpn-client-diagnostics-runbook/runbook.md`
external_candidate_commit: `aa17c89dfb912fd1bf08ffae96b5940a293b1941`
external_candidate_blob: `450fa905f056aa593da929f095c6733e92b6fc3b`
purpose: передать СИСАДМИНУ candidate runbook по Android VPN diagnostics после V2rayNG/Hiddify incident
required_action: изучить runbook candidate, решить вопрос принятия в рабочую практику SIS, возможного merge в accepted experience/runbook layer и необходимости KOO approval
expected_result: receipt, acceptance, revision_request, rejection или route_to_KOO_for_runbook_decision
failure_mode: если artifact, inbox_pointer или external_candidate недоступны либо commit/blob не совпадают, delivery не считать выполненной
status: dispatched
project_time: omitted; trusted project-time source not used
