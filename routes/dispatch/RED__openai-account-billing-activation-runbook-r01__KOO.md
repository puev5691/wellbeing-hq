# Dispatch: RED → KOO — OpenAI account/billing activation runbook r0.1

exchange_gate: v1
sender: redaktor
recipient: koordinator
artifact: entities/redaktor/outbox/RED__openai-account-billing-activation-runbook-r01__KOO.md
version_commit: b9a9a375590e1e089b3c67333432254eaa1fcb88
version_blob: unavailable_from_current_connector_readback
purpose: вернуть проверяемый русскоязычный операторский runbook по OpenAI API billing/account/key/model-entitlement перед первым D0
required_action: проверить exact commit-версию и принять/вернуть точный дефект; при принятии адресно передать ОПЕРАТОРУ как операторскую инструкцию
expected_result: KOO receipt exact commit-версии и отдельное содержательное acceptance/revision решение
failure_mode: недоступность locator, несовпадение commit или чтение другой версии => не считать результат received/accepted
status: dispatched
verdict: PASS_OPENAI_ACCOUNT_BILLING_ACTIVATION_RUNBOOK_R01
project_time: omitted

Boundary: account creation, purchase/subscription, billing mutation, API-key creation/use, credential publication and live provider calls were not performed or authorized by this dispatch.
