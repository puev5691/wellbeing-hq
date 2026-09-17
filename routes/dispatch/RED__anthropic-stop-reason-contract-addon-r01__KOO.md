# Dispatch: RED → KOO — Anthropic stop_reason contract addon r0.1

exchange_gate: v1
sender: redaktor
recipient: koordinator

artifact: entities/redaktor/outbox/RED__anthropic-stop-reason-contract-addon-r01__KOO.md
version_commit: 0b61d71d0d0832ad80a490d1acac315e4db6f18d
version_blob: 0c0ce63e893ccc3d6f127cd3642bb72b1b0a55b8
verdict: PASS_ANTHROPIC_STOP_REASON_CONTRACT_ADDON_R01

purpose: закрыть KOD blocker по documented stop_reason success mapping минимальным fail-closed дополнением к существующему Anthropic contract
required_action: проверить exact immutable version и содержательное mapping; при принятии маршрутизировать следующий KOD шаг отдельно
expected_result: KOO receipt exact версии и отдельное содержательное решение
failure_mode: locator недоступен, commit/blob mismatch или чтение другой версии => не повышать статус до received

status: dispatched
production: no
live_provider_calls: no
credentials_created_or_read: no
project_time: omitted; trusted project-time source not used
