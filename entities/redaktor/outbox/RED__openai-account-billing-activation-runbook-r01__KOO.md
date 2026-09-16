# RED → KOO: OpenAI account/billing activation runbook r0.1

verdict: `PASS_OPENAI_ACCOUNT_BILLING_ACTIVATION_RUNBOOK_R01`
status: `READY_FOR_KOO_REVIEW`
production: `no`
live_provider_calls: `no`
credentials_created_or_used: `no`
account_or_billing_change: `no`
project_time: omitted

## 0. Что ОПЕРАТОРУ нужно сделать перед первым D0

Это инструкция только на подготовку доступа. В рамках этой задачи ничего не создавалось, не оплачивалось и OpenAI API не вызывался.

Практический порядок:

1. Убедиться, что используется нужная OpenAI API organization/project.
2. В API billing overview этой organization добавить платёжные данные и, если используется prepaid billing, купить начальный кредит.
3. Для серверного использования создать отдельный project-scoped credential: предпочтительно отдельный service account проекта либо отдельный project API key.
4. Проверить, что конкретный проект действительно видит `gpt-5.6-luna`; при необходимости также `gpt-5.6-terra` и `gpt-5.6-sol`.
5. Проверить фактический usage tier и rate/usage limits в account settings.
6. Поместить секрет только в разрешённый secret store / environment на стороне runtime.
7. Только после этого разрешённому KOD/SIS-контуру делать один ограниченный синтетический D0-вызов.

---

## 1. Billing / credits / payment

### Документированный факт

Для prepaid API billing OpenAI описывает такой путь:

1. открыть API billing overview нужной organization;
2. выбрать `Add payment details`;
3. указать платёжные данные;
4. выбрать сумму начальной покупки кредитов;
5. проверить настройку `Use auto-reload` — при первоначальной настройке она включена по умолчанию;
6. при необходимости задать threshold / restore amount / monthly reload limit;
7. подтвердить покупку.

Минимальная начальная покупка: **$5**. Документированное значение по умолчанию: **$10**. Минимальная автоматическая дозагрузка: **$5**. Максимальный допустимый баланс зависит от trust tier. После успешной покупки обновление баланса может занять несколько минут.

Официальный источник:
`https://help.openai.com/en/articles/8264644-how-can-i-set-up-prepaid-billing`

OpenAI отдельно указывает, что для individual/team API customers оплата может идти через prepaid credits или automatic credit-card charges; billing history/receipts доступны в разделе Billing.

Официальный источник:
`https://help.openai.com/en/articles/6640792`

### Рекомендация проекта

Для первого D0 проще использовать минимальный подтверждённый prepaid balance и выключить auto-reload, если ОПЕРАТОР не хочет автоматических пополнений. Это рекомендация WELLBEING, а не требование OpenAI.

### UNVERIFIED

Не утверждать, что конкретный текущий аккаунт уже переведён именно на prepaid billing: это надо посмотреть в его фактическом Billing UI.

---

## 2. Minimum payment, balance и usage tier

### Документированный факт

OpenAI rate-limit guide сейчас показывает:

- Free: qualification по allowed geography, общий usage limit $100/month;
- Tier 1: **$5 paid**, usage limit $100/month;
- Tier 2: $50 paid, $500/month;
- Tier 3: $100 paid, $1,000/month;
- Tier 4: $250 paid, $5,000/month;
- Tier 5: $1,000 paid, $200,000/month.

OpenAI пишет, что по мере роста API spend organization автоматически переводится на следующий usage tier; это обычно повышает rate limits большинства моделей.

Официальный источник:
`https://developers.openai.com/api/docs/guides/rate-limits`

Для `gpt-5.6-luna`, `gpt-5.6-terra` и `gpt-5.6-sol` официальные model pages показывают `Free: Not supported` и отдельные лимиты начиная с Tier 1.

Официальные источники:
- `https://developers.openai.com/api/docs/models/gpt-5.6-luna`
- `https://developers.openai.com/api/docs/models/gpt-5.6-terra`
- `https://developers.openai.com/api/docs/models/gpt-5.6-sol`

### Вывод для проекта

Для первого GPT-5.6 D0 следует ожидать минимум **Tier 1 / paid state**, но реальную доступность модели конкретному проекту всё равно надо проверить по этому проекту, а не выводить только из общей страницы документации.

---

## 3. Project-scoped API key / service account

### Вариант A — project API key через UI

**Документированный факт.** В organization settings нужно выбрать нужный Project → `API Keys` → `+ Create new secret key`. Для ключа доступны permission levels `All`, `Restricted`, `Read Only`.

Официальный источник:
`https://help.openai.com/en/articles/9186755`

### Вариант B — service account для серверного runtime

**Документированный факт.** OpenAI Admin API поддерживает project service accounts:

`POST /organization/projects/{project_id}/service_accounts`

и отдельные ключи service account:

`POST /organization/projects/{project_id}/service_accounts/{service_account_id}/api_keys`

Ключ может иметь имя, scopes и срок действия. Создание service account / service-account key требует соответствующего административного доступа; в этом runbook никакой admin key не используется.

Официальные источники:
- `https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts`
- `https://developers.openai.com/api/reference/cli/resources/admin/subresources/organization/subresources/projects/subresources/service_accounts/subresources/api_keys/methods/create`

### Рекомендация проекта

Для серверного D0 выделить отдельный Project и отдельную service identity с минимально необходимыми разрешениями. Не использовать личный универсальный ключ ОПЕРАТОРА как постоянный runtime-secret.

---

## 4. Проверка доступности `gpt-5.6-luna` / `terra` / `sol`

### Документированный факт

OpenAI API имеет:

`GET /models`

для списка моделей, доступных API-клиенту, и:

`GET /models/{model}`

для получения сведений о конкретной модели и permissioning.

Официальный источник:
`https://developers.openai.com/api/reference/ruby/resources/models`

Общий каталог OpenAI API сейчас содержит:
- `gpt-5.6-luna`;
- `gpt-5.6-terra`;
- `gpt-5.6-sol`.

Официальный источник:
`https://developers.openai.com/api/docs/models`

### Точный check перед D0

После создания разрешённого project credential, но **до первого рабочего вызова**, проверить:

- `GET /models/gpt-5.6-luna`
- при необходимости `GET /models/gpt-5.6-terra`
- при необходимости `GET /models/gpt-5.6-sol`

Если конкретная модель не возвращается как доступная этому credential/project, статус должен быть `BLOCKED_MODEL_ENTITLEMENT_NOT_CONFIRMED`, а не предположение о доступе.

### Рекомендация проекта

Первый D0 делать на `gpt-5.6-luna`, если entitlement подтверждён: задача синтетическая, поэтому нет причины начинать с более дорогой модели только ради торжественности момента.

---

## 5. Где смотреть rate / usage limits

### Документированный факт

OpenAI указывает, что фактические rate и usage limits organization находятся в разделе **Limits** account settings. Rate limits действуют на organization/project level и зависят от модели. Ответы API также могут возвращать `x-ratelimit-*` headers с текущими лимитами/остатками.

Официальный источник:
`https://developers.openai.com/api/docs/guides/rate-limits`

Модельные страницы дают high-level таблицы лимитов по tier, но актуальный лимит конкретного аккаунта нужно смотреть в его Limits page.

---

## 6. Checklist перед первым D0 call

### Обязательная проверка проекта

Перед разрешённым первым live D0 убедиться:

- [ ] выбран правильный OpenAI organization/project;
- [ ] billing активен;
- [ ] при prepaid billing баланс положительный;
- [ ] usage tier/limits проверены в account settings;
- [ ] создан отдельный project-scoped credential;
- [ ] секрет сохранён только в разрешённом secret store / environment;
- [ ] `gpt-5.6-luna` entitlement проверен через Models API;
- [ ] D0 payload полностью синтетический и не содержит рабочие/личные/секретные данные проекта;
- [ ] web/file/computer/MCP/tools выключены, если они не входят в отдельное разрешение;
- [ ] fallback на другую модель/провайдера выключен;
- [ ] логирование не печатает credential;
- [ ] стоимость/лимит одного теста заранее ограничены на стороне harness;
- [ ] результат D0 остаётся техническим evidence и не становится project acceptance автоматически.

Пункты про D0 data class, tools, fallback и project acceptance — **проектные ограничения WELLBEING**, не требования OpenAI.

---

## 7. Что нельзя вставлять в ChatGPT, GitHub, задачи и обычные файлы проекта

### Документированный факт OpenAI

OpenAI рекомендует:
- не делиться API keys;
- не помещать ключ в клиентский код;
- не commit'ить ключ в repository;
- хранить API keys в environment variables или key-management service;
- при подозрении на утечку немедленно rotate/delete key.

Официальные источники:
- `https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety`
- `https://help.openai.com/en/articles/5008148`

### Правило WELLBEING

Никогда не вставлять в ChatGPT, GitHub, публичные/обычные project files или task text:

- значение `OPENAI_API_KEY`;
- Admin API key;
- service-account API key;
- любые bearer/access tokens;
- пароли;
- recovery codes;
- private keys;
- полные платёжные реквизиты;
- секреты других провайдеров.

Сами имена переменных, key IDs, project IDs и redacted fingerprints можно фиксировать только если это действительно нужно для provenance и они не содержат секретного значения.

Правило о платёжных реквизитах/recovery/private keys шире официальной API-key статьи и является **проектным security boundary**.

---

## 8. Точный следующий операторский шаг

Если ОПЕРАТОР хочет открыть первый D0 gate:

1. открыть billing нужной OpenAI API organization;
2. активировать подходящий способ оплаты / prepaid credit;
3. подтвердить фактический tier/limits;
4. создать отдельный Project/service credential;
5. сохранить secret вне GitHub/ChatGPT/project files;
6. сообщить KOO/SIS/KOD только **не секретный факт**: billing active, credential installed in approved secret store, model entitlement confirmed;
7. после этого КООРДИНАТОР может разрешить ровно один bounded D0 harness call по существующему техническому контуру.

Это не разрешает production, D1+, tools, project-data transfer или последующие provider calls.

---

## Telemetry

- execution_mode: `FAST_PATH`
- tool_calls: 15
- source_reads: 5 official OpenAI web evidence groups
- github_reads: 4
- github_writes: 1 at this artifact stage; Exchange Gate writes follow separately
- retries: 0
- reconciliations: 1
- operator_rewakes: 0
- budget_note: target `<=12` exceeded because current-writer admission, exact task verification, split official billing/rate/key/model evidence, and mandatory Exchange Gate publication/readback/routing require separate checked operations.

---

КТО: RED / РЕДАКТОР
ДЛЯ ЧЕГО: закрыть операторский account/billing/key gate перед первым OpenAI D0 live call
СТАТУС: `PASS_OPENAI_ACCOUNT_BILLING_ACTIVATION_RUNBOOK_R01`
