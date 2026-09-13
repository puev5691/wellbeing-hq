# ОПЕРАТОР — текущие человеческие действия

status: ACTIONS_REQUIRED
project_time: omitted; trusted project-time source not used

## 1. Telegram Phase 1B — одно действие на `ruvds-xnqc6`

SIS подготовил и проверил одноразовый bounded script.

На сервере `ruvds-xnqc6` выполнить ровно:

`sudo /home/pev5691/sis-phase1b-tooling/phase1b-host-gate-once.sh`

Script SHA-256:
`47f1a2011dfa46759a2f111696f982dc17a2483149249a72aa47fdd84398ded3`

Если terminal попросит текущий sudo password — вводить только в terminal. Не отправлять пароль в ChatGPT/GitHub.

После завершения не интерпретировать вывод вручную. Сообщить, что команда выполнена, и снова запустить SIS. SIS сам прочитает:
`/home/pev5691/sis-phase1b-tooling/host-gate-evidence.txt`

Источник:
https://github.com/puev5691/wellbeing-hq/blob/main/entities/sisadmin/outbox/SIS__telegram-phase1b-authorized-tooling-path-result__KOO.md

## 2. Anthropic — подготовить account-side prerequisites

До первого live D0 запроса нужны факты конкретного Claude Console account:

1. доступна Claude Console organization;
2. billing активен: prepaid credits > 0 либо invoicing arrangement;
3. создан отдельный API key для пилота или иной approved auth path;
4. видны текущие tier/rate/spend limits;
5. доступна модель `claude-sonnet-5`.

Рекомендуемый первый путь:
- отдельный experimental workspace, если Console позволяет;
- workspace-scoped API key;
- разумный короткий срок действия;
- key хранить только как secret, не в GitHub и не в чате.

KOD параллельно готовит credential-free adapter, поэтому account/key можно готовить независимо.

KAN readiness:
https://github.com/puev5691/wellbeing-hq/blob/main/entities/kancelar/outbox/KAN__anthropic-live-d0-access-cost-capabilities__KOO.md

После подготовки сообщить KOO только не-секретные факты:
- organization/workspace ready: yes/no;
- billing/credits ready: yes/no;
- API key created: yes/no, без значения ключа;
- model access `claude-sonnet-5`: yes/no;
- tier/rate/spend limits: значения/скриншот без секретов.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: вынести два текущих human-only действия из технических отчётов в одну понятную карточку
СТАТУС: actions_required
