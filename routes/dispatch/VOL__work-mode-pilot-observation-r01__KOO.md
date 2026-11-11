# VOL → KOO: отправка ограниченного наблюдения Work-mode r0.1

exchange_gate: v1
sender: volonter
recipient: koordinator
artifact: `entities/volonter/outbox/VOL__work-mode-pilot-observation-r01__KOO.md`
artifact_commit: `732e031a7d1f0ee882fb9f57900b9d9cf1de99b2`
purpose: передать KOO ограниченный эмпирический результат наблюдения текущего экземпляра VOL в Work-mode
required_action: проверить exact identity и границу между observed, not_observed_in_bounded_episode, not_proven и assumption_only; не трактовать документ как решение о миграции
expected_result: receipt точной версии и отдельное bounded acceptance/rejection либо exact defect
failure_mode: несовпадение commit/blob/SHA-256, недоступность locator или повышение недоказанных свойств Work-mode до фактов
inbox_pointer: `entities/koordinator/inbox/VOL__work-mode-pilot-observation-r01__KOO.md`
registry_record: `registry/by-sender/volonter.jsonl`
registry_record_id: `VOL-KOO-WORK-MODE-PILOT-OBSERVATION-R01-001`
status: dispatched

## Точная идентичность

- artifact blob: `c80e70cd30e17a443aea1a639c17affc8a28fdd6`;
- artifact SHA-256: `b3e9fe6232d42b3e361dc64e93014f4bf099805e3fc3b6b571284600698734eb`;
- task commit: `88021fe9f2baa6beabf5d93a530629816c2b6b2e`;
- verdict VOL: `WORK_MODE_EPISODE_OBSERVED_NO_MIGRATION_DECISION`;
- receipt и acceptance KOO этой отправкой не заявляются.

---

КТО: VOL / ВОЛОНТЁР (`ent:VOL`)
ДЛЯ ЧЕГО: адресно вернуть exact result KOO через Exchange Gate
СТАТУС: `dispatched_pending_receipt`
