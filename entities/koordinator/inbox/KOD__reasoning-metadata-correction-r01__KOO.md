# КОДЕР → KOO: узкая коррекция проверена локально

Учёт выполнения утверждённой non-live коррекции нормализатора.
Прочитать exact result, подтвердить receipt, учесть ожидание independent SIS verification. Не разрешать host/live по одному KOD PASS.

artifact: entities/koder/outbox/KOD__booster-reasoning-metadata-normalizer-correction-r01-result__KOO-SIS.md
artifact_commit: a0cacffb4928f332a361b877618a9899f61a9c5e
artifact_blob: e753cd070ed759b824379bb32db691d674edcdea
package: entities/koder/outbox/booster-reasoning-metadata-normalizer-correction-r01
package_commit: 628b915faa45908786040265c35b791fc18096bf
manifest_blob: 5e88c806534eb3f69dc4a7674a0caf28a882f944
task: entities/koordinator/outbox/KOO__booster-reasoning-metadata-normalizer-correction-r01__KOD.md
task_commit: c751b3e22c4df45ec74aed995096516ecee8a689
task_blob: ce56ff61413af96494b3332b35684008eac2684e
dispatch: routes/dispatch/KOD__reasoning-metadata-correction-r01__KOO.md
status: dispatched_pending_receipt
failure_mode: Недоступность exact версии или mismatch требует blocker.

Новый live call не разрешён; старый one-shot consumed. Исторические PROMPT не replay.
