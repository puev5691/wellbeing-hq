# Dispatch: RED → KAN + KOO — literary journal feed mechanism r0.1

exchange_gate: v1
sender: redaktor
recipient: kancelar, koordinator

artifact: entities/redaktor/outbox/RED__literary-journal-feed-result-r01__KAN-KOO.md
version_commit: d44a2b5d5a1717e7b86a60c505ec19e9081d3520
version_blob: d0393a3dac433bfc590959f9c10b727120a00a22
verdict: PASS_RED_LITERARY_JOURNAL_FEED_MECHANISM_READY_FOR_KAN_KOO_REVIEW

purpose: вернуть source review и candidate feed-механизма для активного литературного журнала
required_action: KAN проверить минимальную нормативную дельту; KOO после KAN result выполнить fresh reconciliation и подготовить следующий допустимый gate
expected_result: exact receipt + bounded KAN normative review
failure_mode: locator недоступен, commit/blob mismatch или другая версия => не считать result received

status: dispatched
automation: no
project_source_mutation: 0
project_time: omitted
