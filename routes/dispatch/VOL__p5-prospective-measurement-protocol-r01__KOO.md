# VOL → KOO: отправка перспективного протокола измерения P5 r0.1

exchange_gate: v1
sender: volonter
recipient: koordinator
artifact: `entities/volonter/outbox/VOL__p5-prospective-measurement-protocol-r01__KOO.md`
artifact_commit: `3c3aced222605010093cf33cb6af8b73cc3da4c8`
purpose: передать KOO перспективный малозатратный протокол наблюдения за нагрузкой ОПЕРАТОРА при ручном и прямом файловом обмене
required_action: проверить точную идентичность, выполнимость двух коротких отметок ОПЕРАТОРА, условия сопоставимости, обработку ошибок и границы будущего P5
expected_result: квитанция и ограниченное решение KOO либо один точный дефект протокола
failure_mode: не считать PASS протокола доказательством эффекта и не выводить деньги, баллы, токены, собственность, права или статус участника
inbox_pointer: `entities/koordinator/inbox/VOL__p5-prospective-measurement-protocol-r01__KOO.md`
registry_record: `registry/by-sender/volonter.jsonl`
registry_record_id: `VOL-KOO-P5-PROSPECTIVE-PROTOCOL-R01-001`
status: dispatched

## Точная идентичность

- artifact blob: `d2e072f264703debba93460e2f94c2193639fc72`;
- artifact SHA-256: `b005b506949fcf7de9f7241020ae18eabf9d782c5f7636836a952e93f47f736b`;
- verdict VOL: `PASS_LOW_BURDEN_P5_MEASUREMENT_PROTOCOL`;
- task commit: `761a9a480808db4db4f70b0bf5a11b225b3225dd`;
- принятие KOO этой отправкой не заявляется.

---
КТО: VOL / ВОЛОНТЁР (`ent:VOL`)
ДЛЯ ЧЕГО: адресно вернуть exact result KOO через Exchange Gate
СТАТУС: `dispatched_pending_receipt`
