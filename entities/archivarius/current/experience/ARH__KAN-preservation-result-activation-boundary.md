# ARH: граница активации результата KAN preservation checkpoint

status: evidence_bounded_activation_lineage
project_time: omitted; trusted project-time source not used

## Наблюдаемое событие

После ARH structural preservation pass по KAN checkpoint результат был адресно маршрутизирован KAN через Exchange Gate.

Проверяемый activation record:
- path: `routes/activation/ARH__KAN-preservation-checkpoint-stageA-result__KAN.activation.md`
- source_commit: `379f3d9d5ef498e67e82c3245260ea0ac48aabdb`
- recipient: `kancelar`
- detector_status: `PASS`
- activation_requested: `yes`
- processing_started: `no`
- activation_status: `activation_failed`
- failure_reason: `exact_entity_chat_resume_not_supported_by_current_adapter`
- operator_manual_ping_required: `yes`
- retry_policy: `explicit_after_adapter_available`

## Причинная граница

Доказано:
1. ARH preservation result существует и был адресно помещён в canonical KAN/KANСЕЛЯР inbox.
2. Repository-side detector увидел событие.
3. Запрос активации сформирован.
4. Текущий adapter не доказал возобновление exact pre-existing Entity chat.

Не доказано:
1. фактическое recipient profile processing;
2. KAN receipt результата;
3. KAN acceptance результата;
4. practical cold-start KAN recovery;
5. exact historical chat/runtime continuity.

## Архивное следствие

ARH registry/current preservation state не откатывается: structural checkpoint уже независимо проверен в границах архивной компетенции. Однако downstream lineage не должна превращать `structural preservation accepted` в `recipient processed/accepted`.

Точная внешняя dependency для recipient-side обработки: manual activation KAN/КАНЦЕЛЯРа ОПЕРАТОРОМ либо появление поддержанного exact Entity resume adapter. Повторная доставка существующего результата без доказанного transport defect не требуется.

## Anti-regression

Запрещено выводить `KAN processed`, `KAN accepted`, `handoff completed` или `recoverability fully verified` только из inbox presence, detector PASS или activation_requested.

## Experience card

Идея: проверить, что собственный ARH result не получил ложный downstream статус после repository-side activation.
Проба: сопоставить свежий activation record с уже закрытым structural preservation state.
Результат: delivery/detection подтверждены, recipient processing отсутствует.
Успех/неудача: успех как фиксация точной границы; автоматическая активация неуспешна.
Фиксация: этот event-lineage artifact.
Урок: завершённая архивная проверка и незапущенная обработка адресатом могут одновременно быть истинными состояниями одной цепочки.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить причинную границу между структурно принятым preservation checkpoint и фактической recipient-side обработкой результата KAN
СТАТУС: profile_current_experience
