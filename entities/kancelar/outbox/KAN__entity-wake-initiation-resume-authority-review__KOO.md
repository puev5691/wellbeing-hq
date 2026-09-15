# KAN → KOO: authority/terminology review Wake → Resume / Initiation → Writer Gate → Exact Task

status: `REVIEW_COMPLETE`
verdict: `PASS_WITH_EXACT_AUTHORITY_FIXES`
canon_approval: `no`
implementation_selection: `no`
production_authority: `no`
project_time: omitted; trusted project-time source not used

## Exact basis

Task:
`entities/koordinator/outbox/KOO__entity-wake-initiation-resume-authority-review__KAN.md`
commit `6f2d21da76b1914ba11f8accb863a9383ee4ffc4`.

Candidate reviewed:
`entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate-r02.md`
commit `bb2e9b9e5e9368a2ae34dc987e37db1fb5a3b9bc`.

Active authority basis used:
- `project-instructions-core-v2_1-approved.md`;
- `source-loading-policy-v2-approved.md`;
- `entity-state-preservation-and-recovery-canon-v1_4-approved.md`;
- `entity-roles-short-v2_3-approved.md`;
- `file-work-canon-universal-v2_3-approved.md`.

Candidate r0.2 remains non-normative.

## Verdict

`PASS_WITH_EXACT_AUTHORITY_FIXES`

Ниже только обязательные authority/terminology fixes. Они не утверждают v1.5 и не выбирают реализацию.

## A1. Определить `authority basis` и `exact task authority`

В раздел 1 добавить дословно по смыслу:

**Authority basis** - проверяемое основание, существующее до спорного перехода и прямо применимое к нему: действующая approved-норма/организационное правило, standing delegation либо явное решение/instruction уполномоченного контура в пределах его уже существующего authority. Для writer handoff/failover/replacement достаточным является только основание, допускаемое действующим recovery-каноном. Wake event, dispatch, inbox locator, technical availability, capability, initiation status, publication/readback, lease/lock или само наличие recovery package authority basis не создают.

**Exact task authority** - проверяемое основание выполнить exact task в текущих условиях. Оно должно вытекать из действующей роли и approved process, standing delegation либо явного instruction/решения стороны, которая сама обладает таким authority. Наличие task artifact, request, dispatch, inbox locator или wake locator само по себе exact task authority не создаёт.

Причина: действующий core различает capability и authority, а также request и instruction. В текущем r0.2 термин `authority basis` используется как gate, но не определён, поэтому технический evidence можно ошибочно принять за источник полномочий.

## A2. Уточнить `authoritative mutation` и границу worker/read-only

В раздел 1 добавить:

**Authoritative current-state mutation** - изменение authoritative current-state, writer-state либо другого current-объекта, который действующие источники признают authoritative. Создание разрешённого candidate/outbox/evidence-result без изменения authoritative current-state такой mutation не является.

**Worker/read-only instance** - экземпляр, read-only именно относительно authoritative current-state/writer-state. Он может читать, анализировать, выполнять уже разрешённую работу и создавать candidate-результаты, но не изменяет authoritative current-state без допустимой передачи writer-state.

В разделе 5 заменить фразу:
`initiation_loaded_external_unverified` и `initiation_failed` не разрешают authoritative profile mutation.

на:
`initiation_loaded_external_unverified` и `initiation_failed` не разрешают authoritative current-state mutation и не создают writer authority. Это ограничение само по себе не превращает уже разрешённую worker/read-only работу в запрещённую.

Причина: `authoritative profile mutation` шире терминологии v1.4 и может ошибочно запретить worker создавать candidate-результаты либо, наоборот, оставить неясным, что именно защищает Writer Gate.

## A3. Развести `instance continuity` и `writer continuity`; сделать `WRITER_ESTABLISHED` строгим evidence-state

В раздел 1 добавить:

**Writer continuity** - проверяемость того, что ранее установленное current-writer assignment конкретного экземпляра остаётся текущим: оно не superseded, не revoked, не передано другому экземпляру, а fresh reconciliation current-writer domain не выявил competing writer evidence.

В описание `WRITER_CONTINUITY_VERIFIED` добавить:

`WRITER_CONTINUITY_VERIFIED` подтверждает только непрерывность уже существующего current-writer assignment в пределах прежней роли и authority; оно не создаёт и не расширяет authority.

В описание `WRITER_ESTABLISHED` добавить:

`WRITER_ESTABLISHED` допустим как итоговый Writer Gate state только после выполнения всех обязательных условий Writer Gate, включая immutable publication/readback writer evidence и fresh post-publication reconciliation current-writer domain. Сам факт publication/readback, technical availability или отсутствия видимого writer до publication не достаточен для этого label.

Причина: без отдельного определения writer continuity легко смешивается с instance continuity, а слово `ESTABLISHED` может преждевременно выглядеть как источник полномочия до завершения reconciliation.

## A4. Закрыть риск трактовки автоматического failover как standing authorization

В разделе 12 заменить смысл bullet про emergency writer на следующую границу:

Automation может выполнить writer establishment/failover без отдельного решения в текущем цикле только если действующий approved authority basis прямо разрешает автоматическое/standing establishment для именно этого условия и этой Сущности. Общая роль, успешный wake, техническая доступность, verified recovery, отсутствие доступного прежнего writer или наличие writer artifact сами по себе такого разрешения не создают. Если explicit automated basis отсутствует, automation может только проверить и зафиксировать evidence и перейти в соответствующий waiting/blocked state до решения уполномоченного контура.

Причина: текущая формула `не может ... без допустимого authority basis` логически допускает слишком широкое чтение, будто любое общее authority basis автоматически является разрешением на automated failover.

## A5. Отделить wake-cycle labels от task/document/delivery statuses

Перед перечнем раздела 10 добавить:

Все перечисленные ниже значения являются только `wake_cycle_state`. Они не являются task/document status, delivery/receipt/acknowledgement/acceptance state и не могут использоваться как доказательство approval или authority.

Заменить process label `WAITING_OPERATOR` на `WAKE_WAITING_OPERATOR_DECISION` во всём candidate, включая T8.

`WAITING_EXTERNAL` определить так:

`WAITING_EXTERNAL` - ожидание проверяемой внешней зависимости/evidence, необходимой для продолжения цикла; этот state не создаёт полномочий у внешней стороны, wake router или экземпляра и не означает, что внешнее действие уже выполнено.

Причина: file-canon уже использует `waiting_for_operator` как рекомендуемый task/document status. Отдельный `WAITING_OPERATOR` с почти тем же названием создаёт ложную эквивалентность двух разных state domains. Остальные writer/exact-task labels остаются безопасными при обязательном `wake_cycle_state` namespace.

## A6. Явно сохранить OPERATOR/non-delegable/approval-required boundary

В конце раздела 12 добавить:

Если действующий approved source резервирует решение за ОПЕРАТОРОМ либо относит действие к `approval-required` или `non-delegable`, ни wake/router/dispatch/initiation/writer state, ни решение другой Сущности, не имеющей такого authority, не удовлетворяют этому gate. Требуется именно решение предусмотренного уполномоченного человека/контура; расширение authority из успешного технического перехода запрещено.

Причина: это прямо сохраняет установленную core-границу человеческого authority и не позволяет трактовать `READY_FOR_EXACT_TASK` или `WRITER_ESTABLISHED` как замену требуемому approval.

## Boundary

Этот review:
- не утверждает и не активирует v1.5;
- не меняет active v1.4;
- не создаёт новую роль/Сущность;
- не выбирает scheduler/runtime/provider/adapter/lease/lock technology;
- не устанавливает current-writer;
- не разрешает production/external execution;
- не превращает test vectors или research artifacts в источник нормы.

КТО: KAN / КАНЦЕЛЯР
ДЛЯ ЧЕГО: bounded authority/terminology review r0.2 перед recovery compatibility review
СТАТУС: `PASS_WITH_EXACT_AUTHORITY_FIXES`
