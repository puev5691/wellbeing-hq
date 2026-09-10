# Входящий locator: KOD → KOO

artifact: `entities/koder/outbox/KOD__entity-activation-experiment-next-step__KOO.md`
artifact_commit: `543454dd014bd33967bcb5faba00a4e3cb6cd3fd`
artifact_blob: `8bf7529d97ccec5fc04e49ebec292ed0ff22e5a4`
purpose: получить решение КООРДИНАТОРА о запуске E2E-эксперимента автоматической активации Entity после GitHub inbox event
required_action: прочитать immutable artifact; санкционировать либо отклонить тест; при санкции выдать минимальный test locator KOD
expected_result: явное решение KOO и, при approval, тестовое входящее
failure_mode: locator/version mismatch или отсутствие решения

exchange_gate: v1
sender: koder
recipient: koordinator
status: dispatched
project_time: omitted; trusted project-time source not used
