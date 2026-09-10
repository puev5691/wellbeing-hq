# Реестр внешних источников: современный вебмастеринг и публикации

## Правило

Ниже — внешние источники, использованные при подготовке библиотеки. Они являются исследовательской базой, а не Project Sources проекта «ШТАБ БЛАГОПОЛУЧИЯ».

При споре о конкретной возможности нужно открывать первичный источник заново, потому что документация сервисов меняется быстрее, чем человеческая уверенность в собственной памяти.

## GitHub

### Автоматический deployment GitHub Pages
https://docs.github.com/en/get-started/start-your-journey/deploying-your-website-automatically

Подтверждает deployment через GitHub Actions и публикацию сайта при изменениях репозитория.

### GitHub Pages и custom static generators
https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

Подтверждает возможность собственных build-process и генераторов через Actions.

### Deployments and environments
https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments

Required reviewers, environment secrets, restrictions по веткам и protection rules.

### Deploying with GitHub Actions
https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments

Events, environments, concurrency, approvals, deployment history.

### OIDC with cloud providers
https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-cloud-providers

Короткоживущая federated authentication вместо хранения постоянных cloud credentials.

### Workflow syntax / schedule
https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax

Подтверждает `on.schedule`, cron и timezone-aware scheduling.

## Cloudflare

### Workers static assets
https://developers.cloudflare.com/workers/static-assets/get-started/

Актуальный путь для статических и full-stack приложений на Workers.

### Cloudflare Pages overview
https://developers.cloudflare.com/pages/

В документации 2026 Cloudflare прямо рекомендует начинать новые проекты с Workers, при этом Pages остаётся доступен.

### Workers deploy hooks
https://developers.cloudflare.com/workers/ci-cd/builds/deploy-hooks/

HTTP POST hook может инициировать build из CMS, cron или другого workflow.

## Astro

### Markdown in Astro
https://docs.astro.build/en/guides/markdown-content/

Markdown, frontmatter, content collections и schema validation.

### Deploy Astro to Cloudflare
https://docs.astro.build/en/guides/deploy/cloudflare/

Static/on-demand deployment на Cloudflare Workers и CI/CD.

### Cloudflare Astro guide
https://developers.cloudflare.com/workers/framework-guides/web-apps/astro/

Актуальный пример Astro на Workers.

### Astro image service
https://docs.astro.build/en/reference/image-service-reference/

Build/runtime image transformations и external image services.

## Git-based CMS

### Decap CMS editorial workflow
https://decapcms.org/docs/editorial-workflows/

Черновики и review через branches/pull requests.

### Decap CMS GitHub backend
https://decapcms.org/docs/github-backend/

Работа CMS с GitHub repository и deploy previews.

### Decap CMS Open Authoring
https://decapcms.org/docs/open-authoring/

Contributions через forks/pull requests без write-доступа к основному repo.

## Качество и производительность

### Lighthouse CI
https://github.com/GoogleChrome/lighthouse-ci

Автоматические Lighthouse проверки и assertions на каждом изменении.

### Core Web Vitals
https://web.dev/articles/vitals

Текущие Core Web Vitals: LCP, INP, CLS и рекомендуемые пороги.

## Search / SEO

### SEO guide for web developers
https://developers.google.com/search/docs/fundamentals/get-started-developers

Crawlable links, URLs для контента, sitemap и особенности JavaScript.

### Build and submit a sitemap
https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap

Поддерживаемые sitemap formats и правила публикации.

### Article structured data
https://developers.google.com/search/docs/appearance/structured-data/article

Структурированные данные публикаций и проверка Rich Results.

## Syndication

### Atom Syndication Format — RFC 4287
https://www.rfc-editor.org/info/rfc4287/

Стандартный XML-format feeds для web-content syndication.

### WebSub — W3C Recommendation
https://www.w3.org/TR/websub/

Push-синдикация publisher -> hub -> subscribers через HTTP callbacks; W3C Recommendation 02 June 2026.

### ActivityPub — W3C Recommendation
https://www.w3.org/TR/activitypub/

Федеративный social networking protocol с client-server и server-server слоями.

### JSON Feed 1.1
https://www.jsonfeed.org/version/1.1/

Практичный JSON-based feed; удобен как дополнительный формат.

## Telegram

### Telegram Bot API
https://core.telegram.org/bots/api

Методы `sendMessage`, `sendPhoto`, edit/delete и идентификаторы сообщений/каналов для автоматизированной публикации.

## n8n

### Self-hosting
https://docs.n8n.io/deploy/

Варианты self-hosted deployment; Docker/Docker Compose.

### GitHub node
https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github/

Готовые операции с GitHub для workflow automation.

### Telegram node
https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/

Готовые операции Telegram для workflow automation.

---

entity: WEB
document_type: external-source-registry
status: working_research
production_changed: false
project_time: generated_without_trusted_project_time
