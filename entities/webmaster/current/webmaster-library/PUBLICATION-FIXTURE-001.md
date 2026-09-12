# WEB: первый живой publication-routing fixture

status: working-research
fixture_status: live_candidate_not_published
production_changed: false
repository_settings_changed: false

## 1. Назначение

Этот файл фиксирует первый реальный publication candidate, проходящий через профильные gates, как тестовый объект для будущей media/content routing architecture.

Он не утверждает материал к публикации, не меняет его редакционный статус и не создаёт WEB authority.

## 2. Publication candidate

title: `Сначала она была выдумана`
subtitle: `Как мы строили гараж с Системой, которой ещё не существовало`

RED artifact:
`entities/redaktor/outbox/RED__publication-snachala-ona-byla-vydumana__KOO.md`

artifact commit:
`2f8a89a51f317ddf2860acfe93e4699b05a6acd6`

artifact blob:
`01a6aebe57bfb23932ef335d26d18b728bfb7a2d`

Publication plan:
`entities/redaktor/current/media-publication-plan/RED__snachala-ona-byla-vydumana__plan.md`

plan blob:
`2f6ef002414b2e6a2fc5eb3060885e440614b3de`

KOO receipt:
`routes/receipts/RED__snachala-ona-byla-vydumana-publication__KOO.receipt.md`

receipt blob:
`d8c88b38faa7199247c377b6883748bb81348c9b`

KOO receipt state:
- `received_and_reviewed`;
- acceptance: `not_yet_granted`;
- repository placement != external publication.

## 3. Content-class mapping from RED

RED publication plan explicitly classifies the material.

### Primary

- публицистика / авторский литературный материал;
- история проекта;
- материал будущей книги/серии.

### Secondary

- объяснение эволюции идеи Системы;
- ранняя фантазия как контраст с поздней проверяемой архитектурой.

Это хороший пример того, почему media architecture должна различать `content class` и `platform`.

Материал является публицистикой независимо от того, будет ли его производная версия позже показана на сайте, в Telegram или где-либо ещё.

## 4. Proposed route from RED plan

RED предложил следующий маршрут только как editorial plan, не production contract:

1. canonical full text на основном public-web / будущем GitHub-native publication surface;
2. verified canonical URL + readback;
3. Telegram: короткий литературный анонс/фрагмент + ссылка на canonical text;
4. включение в будущую серию / книгу;
5. audience feedback возвращается как материал для RED review, но не меняет canonical text автоматически.

Telegra.ph explicitly **not assigned as primary surface** without a separate current decision.

## 5. Current gate state

### RED

Publication candidate created.

Still required by RED plan:
`final language/cadence polish on exact publication candidate`.

### KOO

Candidate received and reviewed.

Acceptance/release not granted.

### KAN

KOO has issued:
`entities/koordinator/outbox/KOO__snachala-ona-byla-vydumana-public-boundary-review__KAN.md`

KAN task asks to check:
- personal-character/privacy exposure;
- economic/token wording;
- fiction vs project-history vs current architecture boundary;
- wording that could convert fictional System authority into current project authority.

KAN result has not been verified by WEB at the time of this fixture.

### WEB

WEB representation stage has **not started**.

No canonical public URL exists.

No deploy/readback exists.

No Telegram/telegra.ph/external send exists.

## 6. Why this is a useful routing fixture

This one object already exercises several future media-contour requirements:

- literary/publicistic content class;
- canonical full-text surface;
- teaser derivative;
- external channel derivative;
- personal/privacy gate;
- economic wording gate;
- fiction/current-truth distinction;
- series/book linkage;
- audience feedback loop;
- correction/update behavior;
- explicit difference between receipt, acceptance and publication.

Therefore it is suitable as fixture `PUB-FIXTURE-001` for future routing/schema tests.

## 7. Candidate fixture representation

```yaml
fixture_id: PUB-FIXTURE-001
title: "Сначала она была выдумана"
content_layer: publicism
secondary_layers:
  - project-history
  - literary-cycle
source_owner: RED
semantic_status: review_candidate
publication_status: planned_not_published
canonical_surface: pending
preferred_canonical_surface_candidate: public-web
derivatives:
  - type: telegram-teaser
    state: planned_not_sent
  - type: book-series-linkage
    state: planned
telegra_ph_role: unresolved_not_primary_by_current_RED_plan
gates:
  red_final_polish: pending
  kan_public_boundary: in_progress
  koo_release_routing: pending
  web_representation: not_started
canonical_url: null
readback: null
external_receipts: []
```

Это candidate fixture schema, не Project Source и не publication contract.

## 8. Derived test cases for future media system

Когда Stage B/pilot будет разрешён, этот fixture позволяет проверить:

- full text остаётся canonical, teaser не становится second source-of-truth;
- Telegram derivative связан с exact publication id/commit;
- teaser не публикуется до canonical URL + readback;
- audience comments не мутируют canonical text автоматически;
- update/correction после feedback проходит через RED/KOO gates;
- fiction disclaimer сохраняется в полном тексте;
- public/legal conditions сохраняются в derivatives;
- economic wording не превращается в инвестиционное обещание при сокращении;
- withdrawn/superseded publication не остаётся как current announcement в channel adapters.

## 9. Relation to media-contour reconciliation

Fixture должен быть использован как concrete example при будущих ответах на вопросы:

- что такое primary surface;
- что такое derivative channel;
- когда Telegram получает teaser, а когда full text;
- нужен ли telegra.ph;
- как устроен publication object;
- как связать external message ID с source commit;
- как feedback возвращается RED;
- как различать `received`, `accepted`, `published`, `syndicated`.

## 10. Current stop condition

WEB не выполняет:

- создание public page;
- создание canonical URL;
- Telegram payload/send;
- telegra.ph publication;
- Pages enablement;
- new public-web repository creation;
- publication automation.

До этого необходимы downstream profile gates and KOO authorization.

## 11. Короткая фиксация опыта

Идея → использовать первый настоящий publication candidate как fixture вместо абстрактных примеров.

Проба → сопоставлены RED content class, publication plan, KOO receipt и текущий KAN gate.

Результат → зафиксирован `PUB-FIXTURE-001` с реальным состоянием gates и proposed channel route.

Успех → media routing architecture теперь можно проверять на живом объекте, не публикуя его.

Ограничение → KAN result, KOO release decision и WEB representation отсутствуют.

---
created_by: WEB
document_type: live-publication-routing-fixture
purpose: использовать первый реальный publication candidate как проверяемый пример для media/content routing architecture
project_time: not_recorded_no_trusted_source