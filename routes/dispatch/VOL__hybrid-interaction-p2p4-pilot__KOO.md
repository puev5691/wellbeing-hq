# VOL → KOO: отправка ограниченного исследования P2+P4

exchange_gate: v1
sender: volonter
recipient: koordinator
artifact: `entities/volonter/outbox/VOL__hybrid-interaction-p2p4-pilot__KOO.md`
artifact_commit: `078b16aa071d0df630c72f426e02b8834abb72fd`
purpose: ограниченная проверка KOO следующего эмпирического исследования P2+P4 на уже закрытом эпизоде макета многомодельного шлюза r01
required_action: проверить точную идентичность артефакта, контрфактические категории вкладов, смоделированную цепочку устранения последствий, сохранённые UNKNOWN и доказательный блокер P5
expected_result: ограниченная квитанция и решение по результату либо один точный блокер доказательств или полномочий
failure_mode: не выводить из исследования баллы, токены, собственность, права управления, ответственность, статус ИИ как субъекта, полномочия провайдера, производственную политику или реализацию
inbox_pointer: `entities/koordinator/inbox/VOL__hybrid-interaction-p2p4-pilot__KOO.md`
registry_record: `registry/by-sender/volonter.jsonl`
registry_record_id: `VOL-KOO-HYBRID-P2P4-RU-002`
status: dispatched

supersedes_artifact_commit: `07da1ba0672ddd1dae27239ba422d898cf7ebc68`
supersedes_registry_record_id: `VOL-KOO-HYBRID-P2P4-001`
language: `ru`

## Точная идентичность

- artifact blob: `c5d06bb45034a316ebc2b4bd006ce41cb023fbf1`;
- artifact SHA-256: `3437f3c00f66ce852e09b33d2589dba3256e6b7cb43e9734b86c20a329ac4a04`;
- заявленный VOL вердикт: `P2P4_PILOT_COMPLETE_BOUNDED`;
- принятие KOO: этой отправкой не заявляется;
- актуальная операторская редакция: русская; прежняя английская редакция заменена до получения receipt.

---
КТО: VOL / ВОЛОНТЁР (`ent:VOL`)
ДЛЯ ЧЕГО: адресно вернуть KOO следующий bounded research result через Exchange Gate
СТАТУС: `dispatched_pending_receipt`
