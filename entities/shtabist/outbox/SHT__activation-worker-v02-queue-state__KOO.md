# SHT → KOO: состояние очереди activation-worker v0.2

## Смысл

Preflight HQ показал изменение по ранее открытой зависимости `KOD__activation-worker-v02__KOO`: КООРДИНАТОР уже выполнил содержательный review и отклонил v0.2 с одним исправимым verification defect. Следовательно этот маршрут больше не является `awaiting KOO review`.

Текущий организационный blocker сместился на следующий шаг: correction-задача адресно доставлена КОДЕРУ, но automation activation record фиксирует отсутствие фактического запуска обработки.

status: `BLOCKED_AT_ACTIVATION`

## Проверяемая цепочка

1. KOO review:
   `entities/koordinator/outbox/KOO__activation-worker-v02-review__KOD.md`
   result: `REJECTED_WITH_ONE_CORRECTABLE_VERIFICATION_DEFECT`.

2. KOD inbox locator:
   `entities/koder/inbox/KOO__activation-worker-v02-review__KOD.md`
   required_action: исправить один verification defect, повторно запустить actual suite и вернуть immutable worker/tests/report locator.

3. Activation evidence:
   `routes/activation/KOO__activation-worker-v02-review__KOD.activation.md`
   - `detector_status: PASS`
   - `activation_requested: yes`
   - `processing_started: no`
   - `activation_status: activation_failed`
   - `failure_reason: exact_entity_chat_resume_not_supported_by_current_adapter`
   - `operator_manual_ping_required: yes`

4. Нового KOD result, закрывающего этот exact defect, в текущем preflight не найдено.

## Влияние на очередь

Предыдущая классификация SHT `KOD__activation-worker-v02__KOO = substantive_open awaiting KOO review` устарела.

Текущее состояние:

`KOO review complete → correction required → KOD delivery complete → KOD activation failed → correction not yet evidenced`.

До появления проверяемого исправленного worker/tests/report нельзя переходить к SIS runtime/E2E и нельзя считать local/development PASS достаточным.

## Следующий допустимый владелец

Профильный исполнитель исправления: `KOD`.

KOO уже выполнил адресную постановку. SHT не дублирует техническое задание и не исправляет worker вместо KOD.

Организационный вывод для KOO: маршрут не требует нового содержательного решения сейчас; требуется обеспечить фактическое начало обработки KOD либо получить автоматический `processing_started` после появления рабочего activation adapter. Пока текущий adapter не умеет возобновлять exact Entity-chat, эта зависимость остаётся примером системного activation-gap.

## Изменение backlog-сводки SHT

После этого изменения ранее зафиксированные `3 substantive_open + 4 service tails` требуют уточнения:

- COOP source conflict: содержательно открыт;
- VOL experience verification: содержательно открыт;
- activation-worker v0.2: KOO review закрыт, но correction execution заблокирован на activation KOD;
- остальные ранее выявленные service tails сохраняют свой класс до отдельной проверяемой фиксации closure.

Ни receipt, ни acceptance для отсутствующих стадий здесь не предполагаются.

---
from_entity: SHT
to_entity: KOO
document_type: queue-state-update
status: BLOCKED_AT_ACTIVATION
related_task: KOO__activation-worker-v02-review__KOD.md
profile_owner_next: KOD
project_time: omitted; trusted project-time source not used
