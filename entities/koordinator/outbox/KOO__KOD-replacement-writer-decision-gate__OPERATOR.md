# KOO → OPERATOR: решение по replacement current-writer KOD

status: `WAITING_OPERATOR_WRITER_DECISION`
entity: `KOD / КОДЕР`

## Проверенное состояние

Новый KOD instance успешно завершил replacement initiation:
`entities/koder/outbox/KOD__replacement-initiation-v02-result__KOO.md`
commit `14272b4067069cd044cf10e1affab66858a74b12`.

Результат: `initiation_verified`, но `writer_transfer_performed: no`.

На fresh boundary существующий writer marker остаётся:
`entities/koder/current/KOD__initiation-verified-current-writer-v01.md`
commit создания `b7cdd1cbb28c9f144ca26d23823ba4b42973fd5f`.

Отдельной retirement/replacement boundary прежнего writer не найдено.

## Требуемое решение ОПЕРАТОРА

Если прежний KOD instance больше не должен выполнять профильную работу, ОПЕРАТОР может дать новому инициированному экземпляру ровно это основание:

> Предыдущий verified KOD current-writer прекращает дальнейшую профильную работу и считается retired для новых KOD mutations. Новому `initiation_verified` KOD instance разрешаю выполнить fresh competing-writer check и, если нового конфликта нет, установить replacement current-writer с immutable publication/readback и post-publication reconciliation. После writer establishment остановись и верни KOO результат; профильные задачи автоматически не начинай.

Эта карточка сама authority не создаёт. Authority появляется только из явного решения ОПЕРАТОРА.

---
КТО: KOO
ДЛЯ ЧЕГО: дать ОПЕРАТОРУ точный writer-gate без пересказа recovery истории
СТАТУС: waiting_operator_writer_decision
