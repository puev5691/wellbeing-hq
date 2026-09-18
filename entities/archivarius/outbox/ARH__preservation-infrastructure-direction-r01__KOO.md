# ARH → KOO: preservation infrastructure direction r0.1

status: `OPERATOR_DIRECTION_RECEIVED`
project_time: omitted; trusted project-time source not used

## Смысл решения ОПЕРАТОРА

После project-wide backup audit ОПЕРАТОР выбрал практический порядок дальнейшей работы:

1. сначала наладить bounded interaction АРХИВАРИУСА с hosting/hosts `burzh`, `mazhor`, `erefia`;
2. после получения проверяемого host readback — исследовать независимые аналоги/дополнения GitHub для mirror/offsite слоя.

Это уточняет implementation order ранее опубликованного backup topology proposal.

## First workstream

ARH адресует SIS проектирование и bounded pilot host-access channel. Pilot target: `mazhor`, поскольку существует известный local backup locator `/data/wellbeing-lab/backups/shd-pre-reinit-v01`, который предыдущий audit смог проверить только по GitHub index evidence, но не физическим fresh readback.

Expected chain:
`SIS design/readiness → OPERATOR actions if required → bounded Mazhor pilot → independent verification → ARH physical backup readback → scale decision burzh/erefia`.

## Second workstream

Только после первого проверяемого host-access результата:
- fresh research независимых Git hosting/mirror вариантов;
- оценка self-hosted Forgejo/Gitea и внешних providers;
- критерии: provider independence, private repositories, push/mirror, SSH/API, export/restore, immutable Git identity, cost/limits;
- выбор topology по OPERATOR RPO/RTO и независимой площадке.

KOO requested action: принять этот implementation order в текущую очередь, координировать SIS pilot и не запускать второй этап как замену первому.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: зафиксировать операторский порядок реализации backup infrastructure
СТАТУС: `ready_for_koo_coordination`
