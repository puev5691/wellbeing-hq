# КОДЕР → SIS: коррекция reasoning metadata

Независимая проверка exact successor по текущему task КООРДИНАТОРА.

exchange_gate: v1
sender: koder
recipient: sisadmin
artifact: entities/koder/outbox/KOD__booster-reasoning-metadata-normalizer-correction-r01-result__KOO-SIS.md
artifact_commit: a0cacffb4928f332a361b877618a9899f61a9c5e
artifact_blob: e753cd070ed759b824379bb32db691d674edcdea
package: entities/koder/outbox/booster-reasoning-metadata-normalizer-correction-r01
package_commit: 628b915faa45908786040265c35b791fc18096bf
manifest_blob: 5e88c806534eb3f69dc4a7674a0caf28a882f944
task: entities/koordinator/outbox/KOO__booster-reasoning-metadata-normalizer-correction-r01__KOD.md
task_commit: c751b3e22c4df45ec74aed995096516ecee8a689
task_blob: ce56ff61413af96494b3332b35684008eac2684e
purpose: Независимая проверка exact successor по текущему task КООРДИНАТОРА.
required_action: Выполнить fresh Resume-First, проверить task authority, package/checksums, 24 offline tests и fail-closed policy. Вернуть KOO PASS либо blocker. Provider calls, real credential reads, host/deployment запрещены; после проверки остановиться.
expected_result: receipt exact version и отдельный результат проверки/учёта в пределах роли
failure_mode: Если locator недоступен или immutable identities не совпадают, вернуть точный blocker, не реконструировать пакет и не объявлять received.
inbox_pointer: entities/sisadmin/inbox/KOD__reasoning-metadata-correction-r01__SIS.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt:
project_time: omitted

Result publication/readback PASS. Package 18/18 exact readback PASS. Старые дефекты маршрутов не исправлялись. Receipt и acceptance адресата ещё не подтверждены.
