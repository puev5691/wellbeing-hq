# ШТАБИСТ: учёт candidate-линии Entity Continuity / Memory Layering

## Назначение

Зафиксировать, как свежие адресные материалы KOD/KOO влияют на организационное проектирование ШТАБИСТА, не повышая их статус до действующих Project Sources или канона.

## Проверенные входы

1. KOD, `entity-continuity-task-persistence.md` @ commit `85663ac6f5c37ae052012d4a86c971b3f95780ce`, blob `cd9a0761969f0e41a7a6c7a19d4303c6198e2d99`.
   Статус источника: `active_concept`, не Project Source.

2. KOD, `KOD__entity-layered-memory-event-lineage__ALL.md` @ commit `166fd07a6d50bb4055b0d0ffa0d1de98452f252c`, blob `0ec0b1553c8bbe3fbaf6e2436213772670b53ea7`.
   Статус источника: `concept_candidate_for_review`, не Project Source.

3. KOO, `KOO__entity-continuity-data-requirements-headsup__SHT.md`.
   Статус: `heads_up_candidate_requirements`; действие от SHT не требуется, направление учитывать.

4. KOO, `KOO__memory-layering-log16-notice__SHT.md`.
   Статус: `architecture_notice_candidate`; active нормы не меняются.

## Что ШТАБИСТ учитывает как candidate

При дальнейшей разработке маршрутов и критериев состояния различать:

- Entity ID: долговечная роль/Сущность;
- Task ID: задача, которая может пережить смену instance;
- Instance ID: сменяемый исполнительный экземпляр.

Candidate-инварианты для будущей проверки:

- `FAILED INSTANCE != FAILED TASK`;
- BLOCKED сохраняет Task активной и должен иметь проверяемый маршрут снятия блокера;
- DONE требует проверяемого результата, проверки, адресной доставки и фиксации состояния;
- current-writer/ownership не должен наследоваться новому instance без проверки;
- recovery должен поднимать актуальное состояние и релевантный опыт, а не весь архив;
- память проектируется слоями: raw events, operational state, causal episodes, experience, durable procedures/concepts, compact log16/digest;
- promotion в durable memory требует provenance/status/freshness/applicability/conflict checks;
- нужны статусы retired/obsolete/superseded для сохранения старого evidence без управления текущей работой;
- автоматический контур должен стремиться к продолжению Task без ручного сообщения ОПЕРАТОРА.

## Что НЕ изменено

Эта фиксация не:

- вводит новый Project Source;
- утверждает Entity Continuity как действующий канон;
- объявляет существование полного runtime supervisor;
- меняет authority или writer grants;
- разрешает считать candidate знанием без проверки.

До отдельного approval и/или E2E-подтверждения эти положения остаются рабочими требованиями-кандидатами.

## Проверка обработки

- immutable KOD source read: PASS;
- layered-memory immutable artifact identity: PASS;
- matching receipt `routes/receipts/KOD__entity-layered-memory-event-lineage__SHT.receipt.md`: exists, status `received`, identity_check `PASS`;
- KOO notices read: PASS;
- status elevation performed: NO.

---
from_entity: SHT
document_type: current-candidate-impact-note
status: candidate_inputs_processed
project_time: omitted; trusted project-time source not used
