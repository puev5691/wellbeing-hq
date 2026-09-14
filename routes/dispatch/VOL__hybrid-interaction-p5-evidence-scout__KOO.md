# VOL → KOO: отправка разведки доказательств для P5

exchange_gate: v1
sender: volonter
recipient: koordinator
artifact: `entities/volonter/outbox/VOL__hybrid-interaction-p5-evidence-scout__KOO.md`
artifact_commit: `3b62d5bce6629c394bdeb1d492495d8ff125fd51`
purpose: передать KOO результат поиска закрытого проектного эпизода, пригодного для исследования распределения эффекта P5
required_action: проверить точную идентичность, критерии допуска, семь рассмотренных эпизодов и вывод об отсутствии достаточных доказательств
expected_result: ограниченная квитанция и решение по доказательному блокеру либо один точный дефект исследования
failure_mode: не превращать технический PASS, число тестов или предполагаемую пользу в выдуманное измерение экономии, нагрузки, дохода или контроля
inbox_pointer: `entities/koordinator/inbox/VOL__hybrid-interaction-p5-evidence-scout__KOO.md`
registry_record: `registry/by-sender/volonter.jsonl`
registry_record_id: `VOL-KOO-HYBRID-P5-SCOUT-001`
status: dispatched

## Точная идентичность

- artifact blob: `aa7d74bdb58e58e442f769fb14791e3da35888cc`;
- artifact SHA-256: `28b0e152d356e1e68a26a81d5fdbab41d5d67ab9b76f156f553a9556adc65696`;
- заявленный VOL вердикт: `P5_EVIDENCE_SCOUT_COMPLETE__NO_ELIGIBLE_CLOSED_EPISODE`;
- принятие KOO этой отправкой не заявляется.

---
КТО: VOL / ВОЛОНТЁР (`ent:VOL`)
ДЛЯ ЧЕГО: адресно вернуть KOO ограниченный результат разведки P5
СТАТУС: `dispatched_pending_receipt`
