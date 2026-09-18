# WEB → SIS: Telegram experimental target verification r0.1

status: TASK
execution_mode: BOUNDED_NONPRODUCTION

## Verified operator facts

Channel key: `wbnp_pev5691_15042026`
Bot: `@WBNP_Media_Bot`

ОПЕРАТОР подтвердил:
- бот создан через BotFather;
- ранее показанный credential был заменён;
- актуальный credential WEB не получал;
- бот добавлен администратором канала;
- оставлено минимальное право отправки публикаций;
- остальные показанные admin-права выключены.

Existing WEB mapping:
`entities/webmaster/outbox/WEB__telegram-experimental-surface-mapping-r01__KOO.md`
commit `faa09e7409672007948d36b5dca3a576b1b8ad88`.

## Required SIS verification

В контролируемом SIS окружении:
1. verify exact bot identity;
2. resolve exact numeric chat id for channel key `wbnp_pev5691_15042026`;
3. verify bot membership/admin state;
4. verify effective publishing rights;
5. determine whether a discussion group is linked using authorized evidence;
6. if linked, resolve exact discussion identity/chat id;
7. confirm non-public credential storage location without returning credential values;
8. define exact first bounded send + readback method, but do not send in this task.

Do not publish credentials, perform Telegram send, alter channel rights, create/change webhook, moderate users, or deploy production service.

If credential provisioning into SIS-controlled storage requires OPERATOR action, return one minimal provisioning step that keeps the credential outside project artifacts.

Expected:
`PASS_SIS_TELEGRAM_EXPERIMENTAL_TARGET_API_MAPPING_R01`
or exact blocker/fail.

Return immutable result to WEB and KOO.

---
КТО: WEB / ВЕБМАСТЕР
СТАТУС: TASK_READY_FOR_SIS
