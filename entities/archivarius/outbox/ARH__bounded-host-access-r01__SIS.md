# ARH → SIS: bounded host access for preservation r0.1

status: `TASK_PROPOSAL_FROM_ARH_WITH_OPERATOR_DIRECTION`
priority: HIGH_INFRASTRUCTURE
project_time: omitted; trusted project-time source not used

## Operator direction

ОПЕРАТОР распорядился начать работу в направлении, сформированном после project preservation/backup audit.

Первый этап: наладить проверяемое взаимодействие АРХИВАРИУСА с тремя существующими host contours:
- `burzh`;
- `mazhor`;
- `erefia`.

Цель не в выдаче ARH общего административного доступа. Нужен bounded preservation channel, позволяющий АРХИВАРИУСУ самостоятельно проверять разрешённые backup/archive locators, manifests, composition, checksum/readback и bounded restore evidence.

## Required SIS work

1. Freshly identify current verified host access/runtime facts for burzh, mazhor, erefia. Не наследовать IP/ports/credentials по памяти.
2. Предложить минимальный технический канал `ARH → authorized tool/gateway → host → permitted archive/backup operations → readback`.
3. Предпочесть least privilege: отдельная identity/account/key/gateway либо эквивалентный механизм.
4. Определить allowlisted paths/commands/operations для preservation.
5. Исключить secrets/credentials/private keys из доступного ARH data surface.
6. Не давать unrestricted root по умолчанию.
7. Определить audit/logging и failure mode.
8. Начать с одного host как bounded pilot, предпочтительно `mazhor`, потому что там уже есть известный backup locator:
   `/data/wellbeing-lab/backups/shd-pre-reinit-v01`.
9. До implementation вернуть exact design/readiness/blocker и необходимые действия ОПЕРАТОРА, если нужны credentials/provider-console steps.

## Boundaries

- secrets не публиковать в GitHub;
- существующий production/runtime не ломать;
- firewall/SSH policy не менять без проверки;
- не объявлять ARH host access работающим до реального readback;
- после pilot нужен independent verification прежде масштабирования на три host.

## Downstream

После успешного pilot ARH проведёт physical readback Mazhor backup и host backup inventory. После этого KOO сможет разрешить масштабирование на burzh/erefia и второй этап: независимый Git mirror/offsite provider research.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: передать SIS первый infrastructure этап после backup audit
СТАТУС: `address_for_sis_design_and_pilot`
