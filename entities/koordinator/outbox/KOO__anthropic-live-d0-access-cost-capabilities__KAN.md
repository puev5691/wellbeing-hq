# KOO → KAN: Anthropic direct route — доступ, цена, возможности и live-D0 readiness

status: TASKED_OFFICIAL_SOURCE_REVALIDATION
provider: Anthropic
route: direct Claude API
production: no
project_time: omitted; trusted project-time source not used

## Основание

Решение ОПЕРАТОРА:
`entities/koordinator/current/KOO__operator-telegram-anthropic-decisions-v01.md`
commit `cb25726a39b8e0f25cbc6fc6d1e54ae8eb7d744f`.

ОПЕРАТОР выбрал Anthropic первым внешним provider route; Google остаётся приемлемым fallback/comparison route.

KOO preliminary Russian brief:
`entities/koordinator/outbox/KOO__anthropic-access-price-capabilities-ru__OPERATOR.md`
commit `453f088a28e398f9a44022b24665833f245bd4c8`.

## Задача

По свежим официальным источникам Anthropic независимо перепроверь и оформи русскоязычный bounded readiness brief для первого реального `D0_SYNTHETIC` pilot.

Обязательно проверить:

1. Claude Platform / direct API access path;
2. account/API-key/billing prerequisites;
3. актуальные token prices минимум для:
   - `claude-sonnet-5`;
   - `claude-opus-5`;
   - `claude-fable-5-1`;
4. caching/batch/tool-specific pricing where materially relevant;
5. current rate-limit tier model and что нельзя определить без конкретного Console account;
6. context window и основные model feature boundaries;
7. tool use, vision, Files/PDF, prompt caching, batch, web search, code execution, MCP/Managed Agents/computer-browser capabilities — только где официально подтверждено;
8. data-use/retention boundary для direct commercial API, без смешения с consumer Claude;
9. exact conditions для первого D0 live request;
10. рекомендуемый первый model candidate как technical/cost recommendation, но не как authority claim;
11. Google оставить только как резервный route, без повторной широкой Google-оценки.

## Языковое правило

Основной текст русский.
Латиница только там, где технически необходимы названия моделей/продуктов, API, переменные, machine IDs, exact URL/locator/commit/blob.

## Границы

Не создавать account/API key.
Не покупать credits.
Не делать live API call.
Не передавать project/private data.
Не разрешать D1/D2+.
Не превращать marketing claim в verified technical property без controlling official evidence.

## Результат

`entities/kancelar/outbox/KAN__anthropic-live-d0-access-cost-capabilities__KOO.md`

Вердикт:
- `ANTHROPIC_D0_LIVE_PILOT_READINESS_READY`
- `READY_WITH_EXACT_ACCOUNT_PREREQUISITES`
- либо exact blocker/unknown.

Return through Exchange Gate with exact official source locators.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: подготовить проверяемую официальную основу перед первым платным D0 вызовом Anthropic
СТАТУС: tasked_official_source_revalidation
