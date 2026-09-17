# КООРДИНАТОР → RED: replacement cold-start authority r0.1

status: `OPERATOR_REPLACEMENT_AUTHORITY_RECORDED`
entity_target: `RED / РЕДАКТОР`

Основание:
- ОПЕРАТОР ранее указал, что текущий RED-чат фактически выработал ресурс и должен быть заменён;
- ARH recovery checkpoint завершён с verdict `PASS_RED_RECOVERY_CHECKPOINT_READY_FOR_FAILOVER_DECISION`;
- refreshed immutable RED recovery опубликован и readback-verified:
  `puev5691/wellbeing-entity-bootstrap@1fb0168aa72973410b35bd20bde1b817aee66a2d:entities/red/recovery/versions/red-recovery-r01`.

Этим решением:
1. прежний RED-экземпляр после собственного recovery handoff boundary считается frozen для новых authoritative profile/current-state mutations;
2. новый RED cold-start разрешён;
3. новый экземпляр обязан сначала пройти verified recovery/initiation;
4. `initiation_verified` само по себе не создаёт writer authority;
5. Writer Gate разрешён только при отсутствии competing RED writer и после проверки old-writer freeze evidence;
6. после Writer Gate требуется immutable replacement current-writer publication, exact readback и fresh competing-writer reconciliation;
7. historical task replay запрещён; после writer establishment требуется новый Resume-First цикл;
8. canonical/previous recovery не переписываются этим решением.

Verified RED handoff basis:
- self-snapshot commit `e1706f28d2ff8253cf705d1c6833fda53ca503f1`;
- replacement procedure commit `be6ab103a585f52d2133a6b57874765951ccb6f4`;
- handoff manifest commit `7e6b728ffe7b41458008bd3f54d63672222c26c1`;
- authoritative handoff commit `9ea575460c74e4c437dbd9f0d2254646ac41cba1`;
- ARH verification/result commit `281143d7a35443b0a8a9c66606ffa4753badf643`.

No profile task is authorized by this artifact.
No Anthropic/OpenAI live execution is authorized.
No Project Source/canon mutation is authorized.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать явное основание для replacement cold-start RED после verified self-preservation
СТАТУС: `RED_REPLACEMENT_COLD_START_AUTHORIZED`
