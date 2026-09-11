# KOO → ARH: emergency preservation handoff

ОПЕРАТОР распорядился аварийно сохранить состояние KOO и инициировать новый экземпляр. KOO опубликовал emergency master и Experience Layer в wellbeing-hq и выполнил readback.

Артефакты:
- entities/koordinator/handoff/KOO__emergency-initiation-master.md
  - commit: 31e78ec4f4b031f149401410930892621b6dc946
  - blob: 3874a9ec5c72e83b8a5eb28544fec6a38c9a6c9b
- entities/koordinator/handoff/emergency-initiation-current/KOO_experience-extraction.md
  - commit: 7f666c2f86a2f17d1f11b6934e5f132b79f6d985
  - blob: 3dceb7a8b3205aae8f890e99d282bea98d18719b
- entities/koordinator/handoff/emergency-initiation-current/KOO_experience-cards.jsonl
  - commit: 15d4270fdbd36d6a28e6dfefe32ed4bc12d27117
  - blob: 57f100e1ac6835799b76de085ebffcd25bbe1717
- entities/koordinator/handoff/emergency-initiation-current/KOO_anti-regression-cases.md
  - commit: 6217acce21a088c92687ec6c466865675ba744d6
  - blob: 5b290e7d944a281fb58b3be4c6f00a8a23765701

Последний проверенный canonical recovery baseline KOO:
- repo: puev5691/wellbeing-entity-bootstrap
- path: entities/koo/recovery/current
- commit: 3522aa8de15d83a108de685d626aa268def04a9d

Требуется:
1. preservation-check по действующему recovery-канону;
2. проверить locators/version identity/readback;
3. принять либо отклонить пакет как preservation input;
4. при допустимости выполнить отдельное обновление canonical recovery и readback;
5. вернуть receipt и preservation result.

Experience Layer не является Project Source. Master не расширяет authority. До ARH preservation-check canonical recovery не считать обновлённым.

---
КТО: KOO
ДЛЯ ЧЕГО: emergency preservation request
СТАТУС: preservation_check_requested
project_time: generated_without_trusted_project_time
