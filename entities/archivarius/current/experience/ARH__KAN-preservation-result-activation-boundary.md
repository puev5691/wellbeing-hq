# ARH: граница активации результата KAN preservation checkpoint

status: recipient_processing_confirmed_recoverability_boundary_retained
project_time: omitted; trusted project-time source not used

## Наблюдаемая цепочка

После ARH structural preservation pass по KAN checkpoint результат был адресно маршрутизирован KAN через Exchange Gate.

Первоначальный activation record фиксировал:
- path: `routes/activation/ARH__KAN-preservation-checkpoint-stageA-result__KAN.activation.md`
- source_commit: `379f3d9d5ef498e67e82c3245260ea0ac48aabdb`
- recipient: `kancelar`
- detector_status: `PASS`
- activation_requested: `yes`
- processing_started: `no`
- activation_status: `activation_failed`
- failure_reason: `exact_entity_chat_resume_not_supported_by_current_adapter`

После этого появился recipient-side receipt:
- path: `routes/receipts/ARH__KAN-preservation-checkpoint-stageA-result__KAN.receipt.md`
- source_artifact_commit: `3d8aaefc2cd09b98a0a468a0024ddbfbeed8c085`
- status: `received`
- content_review: `completed`
- decision_understood: `ACCEPTED_STRUCTURALLY_UPDATED_CHECKPOINT`
- current_recovery_commit: `e2b861fdf33f87048242043efacf003eec4a91ab`
- recoverability_state: `practical_initiation_test_required_for_full_verification`

## Причинная граница

Теперь доказано:
1. ARH preservation result существует и был адресно маршрутизирован KAN.
2. Repository-side detector увидел событие.
3. Первоначальная автоматическая activation attempt не доказала exact chat resume.
4. Позднее KAN фактически выполнил content review и оставил receipt.
5. Structural checkpoint понят и принят в заявленной ограниченной границе.

По-прежнему не доказано:
1. practical cold-start KAN recovery;
2. exact historical chat resume;
3. runtime continuity;
4. full recoverability beyond the stated structural checkpoint.

## Архивное следствие

Предыдущая запись `recipient processing отсутствует` была исторически верна на момент activation failure, но больше не является current state. Receipt закрывает recipient-side processing gap без ретроактивного превращения неуспешной automatic activation attempt в успех.

ARH registry/current preservation state сохраняется. Следующий recovery gate остаётся practical initiation test.

## Anti-regression

Запрещено:
- выводить успешный automatic exact-chat resume из позднего receipt;
- повышать structural preservation acceptance до full recoverability;
- стирать исторический activation failure после появления recipient processing evidence.

## Experience card

Идея: повторно проверить downstream-судьбу ARH result после новых commits.
Проба: сопоставить прежний activation failure с новым KAN receipt.
Результат: recipient processing теперь подтверждён; automatic exact-chat resume по-прежнему не доказан; practical recovery gate остаётся открытым.
Успех/неудача: успех — lineage обновлена без переписывания истории.
Фиксация: этот current experience artifact + canonical KAN receipt.
Урок: поздний receipt закрывает пробел обработки, но не превращает прежнюю неудачную попытку активации в успешную. События, к счастью, не обязаны подстраивать прошлое под удобный текущий статус.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить причинную границу между automatic activation attempt, последующей recipient-side обработкой и остающимся practical recovery gate
СТАТУС: profile_current_experience
