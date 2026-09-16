# RED → KOO: Anthropic account/billing activation runbook r0.1

verdict: `PASS_ANTHROPIC_ACCOUNT_BILLING_RUNBOOK_R01`
status: `READY_FOR_KOO_REVIEW`
production: `no`
live_provider_calls: `no`
credentials_created_or_read: `no`
account_or_billing_change: `no`
project_time: omitted

## 0. Что ОПЕРАТОРУ нужно сделать перед первым D0

Это инструкция только на подготовку доступа. В рамках этой задачи аккаунты, workspace, service account, API keys и billing не создавались и не изменялись; вызовов Anthropic API не было.

Практический порядок:

1. Войти в нужную Claude Console organization и убедиться, что используется именно API/Console-контур, а не consumer subscription.
2. Для проекта создать/выбрать отдельный Workspace в `Settings > Workspaces`.
3. Для общего или unattended runtime создать отдельный service account в `Settings > Service accounts` и дать ему только нужный доступ к выбранному Workspace.
4. В `Settings > API keys` создать отдельный ключ, связанный с этим service account, и по возможности scope'ить его на нужный Workspace.
5. Активировать API billing: для большинства организаций Console использует prepaid usage credits; организации с отдельным invoicing arrangement оплачивают usage помесячно.
6. Проверить текущий usage/rate tier и фактические limits в Console.
7. С разрешённым credential проверить `GET /v1/models`; только модели, возвращённые Models API, считать подтверждённо доступными этому credential.
8. Только после этого разрешённому KOD/SIS-контуру делать один bounded synthetic D0 call.

---

## 1. Account / Organization / Workspace

### Документированный факт Anthropic

Anthropic API используется через Claude Console account. Console позволяет управлять API keys, участниками, billing и Workbench.

Для organization workspaces Anthropic документирует:
- у каждой organization есть Default Workspace;
- отдельные workspaces создаются через `Settings > Workspaces > Create workspace`;
- organization admins могут создавать workspaces;
- workspace roles разграничивают доступ к API keys, API и billing;
- service accounts можно добавлять в workspaces из `Settings > Service accounts` либо из вкладки Service accounts конкретного workspace.

Официальные источники:
- https://support.claude.com/en/articles/8114521-how-can-i-access-the-anthropic-api
- https://platform.claude.com/docs/en/manage-claude/workspaces

### Рекомендация WELLBEING

Для первого D0 использовать отдельный Workspace проекта, а не Default Workspace, чтобы отдельно ограничить доступ, spend/rate limits и аудит.

---

## 2. Service account и API key

### Документированный факт Anthropic

Anthropic Authentication guide различает personal key и service account key. Для shared/unattended workload Anthropic прямо рекомендует service account key вместо персонального ключа.

Console-путь создания ключа:
`Settings > API keys > Create key`.

При создании ключа можно:
- задать имя и expiration;
- выбрать `Linked account`: пользователь либо service account;
- scope'ить ключ на конкретный Workspace либо оставить organization scope в пределах прав linked account.

Service account создаётся в `Settings > Service accounts`; затем его можно добавить в нужный Workspace. Service account является отдельной workload identity.

Anthropic также поддерживает Workload Identity Federation для production cloud/CI workloads без долгоживущих статических секретов.

Официальные источники:
- https://platform.claude.com/docs/en/manage-claude/authentication
- https://platform.claude.com/docs/en/api/beta/organization/service_accounts/create
- https://platform.claude.com/docs/en/manage-claude/workspaces

### Рекомендация WELLBEING

Для первого bounded server D0:
- отдельный service account проекта;
- отдельный key;
- scope только на нужный Workspace;
- минимально разумный срок действия;
- production-переход позже рассмотреть через Workload Identity Federation.

Не использовать личный универсальный ключ ОПЕРАТОРА как постоянный runtime-secret.

---

## 3. Billing / prepaid credits / minimum

### Документированный факт Anthropic

Для Claude API через Console большинство организаций платит prepaid usage credits. До API usage credits должны быть куплены; если credits закончились, API и playground перестают работать до пополнения. Организации с invoicing arrangement оплачивают usage помесячно вместо prepaid.

Console-путь для prepaid:
`Settings > Billing > Buy credits`.

Purchased credits:
- доступны сразу после покупки;
- отображаются на Billing page;
- могут пополняться через auto-reload;
- истекают через один год;
- не возвращаются.

Официальные источники:
- https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage
- https://support.claude.com/en/articles/8114531-i-created-a-claude-console-organization-how-do-i-start-using-the-claude-api

### UNVERIFIED

В проверенных текущих официальных Anthropic источниках не найден фиксированный минимальный долларовый размер первой prepaid credit purchase. Не подставлять сумму по памяти, старым скриншотам или сторонним материалам; фактический minimum смотреть в текущем Billing UI перед оплатой.

### Рекомендация WELLBEING

Для D0 покупать только минимальный объём, который фактически допускает текущий Billing UI, и не включать auto-reload до отдельного решения ОПЕРАТОРА.

---

## 4. Usage / rate tiers и limits

### Документированный факт Anthropic

Текущая документация описывает standard usage tiers `Start`, `Build`, `Scale` и `Custom`; новые/малoиспользовавшиеся организации могут начинать в `Evaluation` tier с лимитами ниже standard. Tier определяется автоматически по usage history и account standing и может повышаться со временем.

Текущие monthly spend caps:
- Start: `$500/month`;
- Build: `$1,000/month`;
- Scale: `$200,000/month`;
- Custom: custom arrangement, без стандартного monthly cap.

Rate limits применяются по моделям и измеряются RPM, ITPM и OTPM. Фактические organization limits и tier нужно смотреть в Claude Console `Rate limits`; usage/headroom также видны на Usage page. Workspace limits могут быть ниже organization limits.

Официальный источник:
- https://platform.claude.com/docs/en/api/rate-limits

### UNVERIFIED

Anthropic в проверенной текущей документации не публикует простой фиксированный `$X paid → Tier Y` переход, аналогичный некоторым другим провайдерам. Не выводить tier только из суммы первой покупки.

---

## 5. Model access / entitlement check

### Документированный факт Anthropic

`GET /v1/models` возвращает список моделей, доступных для использования в API конкретным credential. Anthropic прямо указывает, что Models API response можно использовать для определения доступных моделей.

Официальный источник:
- https://platform.claude.com/docs/en/api/models/list

На момент проверки официальная model-deprecation page помечает как Active, среди прочих:
- `claude-haiku-4-5-20251001`;
- `claude-sonnet-5`;
- `claude-opus-5`.

Официальный источник:
- https://platform.claude.com/docs/en/about-claude/model-deprecations

### Рекомендация WELLBEING для первого entitlement check

Для трёх внутренних ролей проекта проверить наличие в `GET /v1/models`:
- routine: `claude-haiku-4-5-20251001`;
- main: `claude-sonnet-5`;
- complex: `claude-opus-5`.

Это mapping WELLBEING, а не классификация Anthropic и не гарантия entitlement.

Если конкретная модель не возвращается Models API для выбранного key/workspace, статус должен быть `BLOCKED_MODEL_ENTITLEMENT_NOT_CONFIRMED`, а не предположение о доступе.

---

## 6. Secret handling

### Документированный факт Anthropic

Anthropic рекомендует:
- не делиться API keys;
- не хранить plaintext keys в public repositories, исходниках или config files;
- передавать secrets через environment variables / secrets manager;
- `.env` исключать из source control;
- периодически rotate keys;
- disable/delete key при подозрении на утечку;
- для shared workload использовать service account key; для production cloud/CI рассматривать Workload Identity Federation.

Официальные источники:
- https://support.claude.com/en/articles/9767949-api-key-best-practices-keeping-your-keys-safe-and-secure
- https://platform.claude.com/docs/en/manage-claude/authentication

### Правило WELLBEING

Никогда не вставлять в ChatGPT, GitHub, task text, обычные project files или журналы:
- значение `ANTHROPIC_API_KEY`;
- Admin API keys;
- service-account keys;
- OAuth/bearer tokens;
- пароли, recovery codes и private keys;
- полные платёжные реквизиты.

Допустимо фиксировать только несекретный факт установки credential, redacted fingerprint/key ID при практической необходимости и workspace/service-account IDs, если они не являются секретами.

---

## 7. Exact checklist перед первым bounded synthetic D0

Перед первым разрешённым live D0 проверить:

- [ ] выбран правильный Claude Console organization;
- [ ] выбран отдельный Workspace проекта;
- [ ] service account создан и добавлен только в нужный Workspace;
- [ ] отдельный service account key создан и установлен в approved secret store/environment;
- [ ] ключ не опубликован в GitHub/ChatGPT/project files/logs;
- [ ] billing active;
- [ ] при prepaid billing положительный credit balance;
- [ ] фактический usage tier, monthly spend cap и current rate limits проверены в Console;
- [ ] project/workspace spend limit установлен достаточно низко для bounded test;
- [ ] `GET /v1/models` подтверждает нужный model ID;
- [ ] D0 payload полностью синтетический и не содержит project/private/secret data;
- [ ] tools, web, files, MCP, computer use, server-side fallback и иные внешние действия выключены, если не разрешены отдельным решением;
- [ ] один model ID выбран явно; автоматический fallback выключен;
- [ ] `max_tokens`/test harness ограничивают объём и стоимость одного вызова;
- [ ] логи не печатают credential или полный sensitive payload;
- [ ] результат D0 остаётся техническим evidence и не означает project acceptance/production approval.

Пункты о data class, tools, fallback, spend bound и acceptance — проектные ограничения WELLBEING, а не требования Anthropic.

---

## 8. Точный следующий операторский шаг

Чтобы открыть первый Anthropic D0 gate, ОПЕРАТОРУ нужно только подготовить внешний доступ:

1. подтвердить нужную Claude Console organization;
2. создать/выбрать отдельный Workspace;
3. активировать billing / prepaid balance по фактическому Billing UI;
4. проверить текущий tier и limits;
5. создать отдельный service account и service account key;
6. сохранить key только в approved secret store/runtime environment;
7. проверить доступные модели через `GET /v1/models`;
8. сообщить KOO/SIS/KOD только несекретный факт: billing active, credential installed, workspace selected, model entitlement confirmed.

После этого КООРДИНАТОР может отдельно разрешить ровно один bounded synthetic Anthropic D0 call.

Это не разрешает production, реальные project data, tools, D1+, последующие provider calls или auto-reload.

---

## Prewrite reconciliation

Fresh RED current-state read показал активный RED writer без competing current-writer marker. Exact KOO task прочитан по commit `dee656bf4640aff508d83e8c1e4dfbdcf586c98f`; задача `READY_FOR_RED_EXECUTION`. Конфликта с текущим editorial state не обнаружено: это новая адресная bounded task.

---

## Telemetry

- execution_mode: `FAST_PATH`
- source policy: current official Anthropic/Claude Platform sources only
- account creation: `0`
- purchase: `0`
- keys created/read: `0`
- provider calls: `0`
- TERA2/WBN: `not_touched`
- project_time: omitted

---

КТО: RED / РЕДАКТОР
ДЛЯ ЧЕГО: закрыть операторский Anthropic account/billing/service-account/key gate перед первым bounded synthetic D0
СТАТУС: `PASS_ANTHROPIC_ACCOUNT_BILLING_RUNBOOK_R01`
