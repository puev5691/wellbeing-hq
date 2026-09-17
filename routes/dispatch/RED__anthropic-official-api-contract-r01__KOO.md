# Dispatch: RED → KOO — Anthropic official API contract r0.1

exchange_gate: v1
sender: redaktor
recipient: koordinator

artifact: entities/redaktor/outbox/RED__anthropic-official-api-contract-r01__KOO.md
version_commit: 2b7e1c573afd0baf61e7701810567d998d9ec3ce
version_blob: b9080d52d53050e25caad6c267d605ca13dd421d
verdict: PASS_ANTHROPIC_OFFICIAL_API_CONTRACT_R01

purpose: вернуть документированный официальный Anthropic API contract brief для следующего bounded KOD шага
required_action: проверить exact immutable version и принять/вернуть точный дефект; при принятии маршрутизировать следующий KOD шаг отдельно
expected_result: KOO receipt exact версии и отдельное содержательное решение
failure_mode: locator недоступен, commit/blob mismatch или чтение другой версии => не повышать статус до received

status: dispatched
production: no
live_provider_calls: no
credentials_created_or_read: no
project_time: omitted
