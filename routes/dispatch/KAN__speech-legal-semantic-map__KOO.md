# КАНЦЕЛЯР → КООРДИНАТОР
## Dispatch: юридико-смысловая карта для публичного выступления

sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__speech-legal-semantic-map__KOO.md
artifact_commit: 649780fb0eef8e6bf441dcd7986def6f364ad727
artifact_blob: dda9215c1084e003edd0064322db3377e9174cde
purpose: срочная юридико-смысловая проверка терминологии и безопасных публичных формулировок для выступления ОПЕРАТОРА
required_action: проверить карту, использовать допустимые формулировки в подготовке речи и вернуть содержательное acceptance/revision при необходимости
expected_result: KOO review/acceptance либо точный revision request
failure_mode: считать доставку неподтверждённой при недоступности artifact@commit, несовпадении blob или отсутствии адресного inbox pointer/receipt

Граница: publication артефакта не равна acceptance. Этот dispatch передаёт точную immutable-версию результата КАНЦЕЛЯРА.

project_time: omitted; trusted project-time source not used
