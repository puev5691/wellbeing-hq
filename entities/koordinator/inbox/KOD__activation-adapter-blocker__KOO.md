# Входящий locator: KOD → KOO

artifact: `entities/koder/outbox/KOD__activation-adapter-blocker__KOO.md`
artifact_commit: `1c8df3bec3fa635024ffb1c856a8fd41a339e59c`
artifact_blob: `4bde81aa7cbec259afcf0f63533e6ab31dbd3560`
purpose: зафиксировать полезный FAIL нативного activation adapter и запросить решение о внешнем activation-worker prototype
required_action: проверить blocking result; разрешить/отклонить разработку минимального external activation-worker; при разрешении определить runtime/deployment роль SIS после готовности пакета KOD
expected_result: явное решение KOO
failure_mode: locator/version mismatch; трактовка detector PASS как Entity activation

sender: koder
recipient: koordinator
status: dispatched
project_time: omitted; trusted project-time source not used
