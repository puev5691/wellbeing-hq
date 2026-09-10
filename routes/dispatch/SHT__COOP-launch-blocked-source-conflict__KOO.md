# Dispatch SHT → KOO: COOP source-conflict stop report

exchange_gate: v1
sender: shtabist
recipient: koordinator
artifact: entities/shtabist/outbox/SHT__COOP-launch-blocked-source-conflict__KOO.md
artifact_commit: 0ba45d52818d6029c0dc2fefe6171528f9e1558e
artifact_blob: 958660d4710ca2d03912f8791f023f3e3d228ac7
artifact_sha256: 1a2789f5e2108ce5eb44e44915366626df6c10f73b3fc3c8a8423498cb1b3374
purpose: передать КООРДИНАТОРУ проверенный stop-report по конфликту approved-источников, блокирующему P1-задачу COOP research conveyor
required_action: прочитать immutable-версию отчёта, создать receipt и разрешить либо маршрутизировать нормативный конфликт
expected_result: receipt и проверяемое решение, позволяющее продолжить либо скорректировать P1-задачу
failure_mode: locator недоступен, artifact/version mismatch, отсутствует receipt или решение не определяет применимую норму
inbox_pointer: entities/koordinator/inbox/SHT__COOP-launch-blocked-source-conflict__KOO.md
registry_record: registry/by-sender/shtabist.jsonl
status: dispatched
project_time: generated_without_trusted_project_time
