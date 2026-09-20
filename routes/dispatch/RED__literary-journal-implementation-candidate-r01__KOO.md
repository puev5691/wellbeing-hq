# Dispatch: RED → KOO — literary journal implementation candidate r0.1

exchange_gate: v1
sender: redaktor
recipient: koordinator

artifact: entities/redaktor/outbox/RED__literary-journal-implementation-candidate-r01__KOO.md
version_commit: cef6220d4225a0892cdc1e25438b5d793d7eec37
version_blob: 1f51413b592ea44329d2f93e1d9dfde3819e9875
verdict: PASS_RED_LITERARY_JOURNAL_IMPLEMENTATION_CANDIDATE_READY_FOR_OPERATOR

purpose: вернуть минимальный implementation candidate литературного журнала проекта
required_action: проверить exact version и вынести отдельное решение ОПЕРАТОРУ по activation; не активировать журнал без отдельного authority
expected_result: KOO receipt exact версии и отдельный decision packet/activation task при approval
failure_mode: locator недоступен, commit/blob mismatch или другая версия => не считать candidate received

status: dispatched
journal_activation: no
project_source_mutation: 0
automation: 0
project_time: omitted
