# RED content inventory r0.1

status: `ACTIVE_RED_CURRENT_CONTENT_INVENTORY`
task_basis: `KOO__first-bounded-media-editorial-batch-r01__RED.md@921a41251511a5d5515ca6b8cbb779ababf4d6c9`
PUBLICATION_AUTHORITY: `NONE`
EXTERNAL_PUBLICATION: `NOT_PERFORMED`
WEB_TASK: `NOT_CREATED`
OPERATOR_RELEASE: `NOT_INFERRED`
project_time: omitted

| content_id | title | exact source locator(s) | stream | maturity | privacy/public boundary | possible channels | merge/duplication target | current gate/status |
|---|---|---|---|---|---|---|---|---|
| C001 | Как солдат назначил смартфон командиром | `puev5691/wellbeing-hq@3f2c6c994bcf8ff02598a299629963013a3bee23:entities/redaktor/current/literary-sources/OPR__soldier-smartphone-commander__DRAFT.md` blob `0b12356d94a3c9ea95ae29dcb393dfa393dab2e1` | Смешные ситуации | platform-ready | Не расширять медицинские/биографические детали; не идентифицировать санаторий/врача/третьих лиц без отдельного основания | Telegram, portal, longform/book insert | standalone; может входить в линию «человек рядом с техникой» | SELECTED_BATCH_R01; adaptation `93cab5b961c78661bdcec694a3f03bd76c283449`; CANDIDATE_ONLY |
| C002 | Booster: почему работающий канал ещё не означает полезный инструмент | `puev5691/wellbeing-hq@7d856fe18075af40515d1ff0843882896ccad6aa:entities/redaktor/current/literary-journal/RED__project-literary-journal.md` blob `37bf61e6cdb58a31a0afb2a914792c83634b5f30` + evidence refs внутри главы | Инженерные грабли / capability != authority | platform-ready | N=1/N=2; token-budget cause unconfirmed; technical PASS != business/product value; no production/standing-use claim | Telegram, portal engineering case, longform, School case | existing Booster development arc; raw SIS/KOD sources merge only through RED synthesis | SELECTED_BATCH_R01; adaptation `4e362c6798829e4971c4fca458af30daf93a3f75`; CANDIDATE_ONLY |
| C003 | Рабочие круги: не десять знакомых, а пять постоянных интерфейсов | `puev5691/wellbeing-hq@e314b52575addad1eaecf5973a57053e6c27f449:entities/shtabist/outbox/SHT__working-circles-journal-entry__RED.md` blob `a6da9180dc1e9183d0941e7a0f242734853a1f00`; experiment `puev5691/wellbeing-hq@997bcb708697aa2c126293f6cd957695cbc8b6a6:entities/shtabist/outbox/SHT__working-circles-experiment-r01__KOO-KAN-RED.md` | Проект строит себя / Человек и Сущности | platform-ready | 339/239 относится к observed sample; «5/10» — hypotheses; не выдавать за доказанную human-management model или approved structure | Telegram, portal, longform, public talk | existing working-circles narrative in RED journal | SELECTED_BATCH_R01; adaptation `04de20c01d3dcb8033629adbe6f731c567390b15`; CANDIDATE_ONLY |
| C004 | Memory-layering: проверяющий изменил объект проверки | `puev5691/wellbeing-hq@921a41251511a5d5515ca6b8cbb779ababf4d6c9:entities/sisadmin/outbox/SIS__memory-layering-main-attempt-2-journal-source__RED.md` blob `d623b3881ac8c37e57e9d744531979ce32a82bd8` | Быстрая память / Инженерные грабли | raw | Не утверждать Fast Memory production readiness или continuity success; это harness failure до OLD-01/NEW-01 | portal, longform, School case, Telegram after RED synthesis | merge with broker 4/7/32 + consumed-authority sources into one memory-layering arc | DEFERRED_FOR_RED_SYNTHESIS; not direct-public |
| C005 | Сущность — не чат, а ОПЕРАТОР — не её запасная память | `puev5691/wellbeing-hq@7d856fe18075af40515d1ff0843882896ccad6aa:entities/redaktor/current/literary-journal/RED__project-literary-journal.md` blob `37bf61e6cdb58a31a0afb2a914792c83634b5f30` | Человек и Сущности / continuity | narrative | Убрать внутренние recovery locators и не превращать конкретные incidents в универсальную модель ChatGPT continuity | Telegram, portal explainer, longform/book | merge with continuity/handoff episodes; avoid duplication with C006 | FUTURE_BATCH_CANDIDATE |
| C006 | ОПЕРАТОР не должен быть ручным курьером системы | `puev5691/wellbeing-hq@7d856fe18075af40515d1ff0843882896ccad6aa:entities/redaktor/current/literary-journal/RED__project-literary-journal.md` blob `37bf61e6cdb58a31a0afb2a914792c83634b5f30` | Человек и Сущности / human interface | narrative | Не описывать будущий orchestrator как уже работающий; manual activation remains actual boundary where relevant | Telegram, portal product/UX story, longform/book | merge with human-interface conveyor failure; cross-link C005 | FUTURE_BATCH_CANDIDATE |
| C007 | Сначала она была выдумана v0.3 | `puev5691/wellbeing-hq@1d81c994b212ea8a00e6441136d39dd5364c6b32:entities/redaktor/outbox/RED__publication-snachala-ona-byla-vydumana-v03__KOO.md` blob `d7faa795602cec3fef40cb8c4fbb7511d55c7057` | От мечты к системе | held | Existing public/legal/editorial boundaries already reviewed; no inertia revision | portal, longform, Telegram derivative only after release | standalone + literary cycle | HELD_AT_OPERATOR_RELEASE_GATE / WAITING_OPERATOR_RELEASE_DECISION |
| C008 | Public cooperation speech v0.2 | `puev5691/wellbeing-hq@30214bc36f48d4804ffff9fc60c3a7aedb0438c1:entities/redaktor/outbox/RED__wellbeing-cooperation-speech-v02__KOO.md` blob `31034d87d67035698748339f7e0d747509da0edc` | Человек и сотрудничество / public speech | held | Bounded public-speech candidate; no revision by inertia; no acceptance inferred | speech, portal derivative, Telegram excerpt only after review/release | standalone speech; may feed cooperation longform later | HELD_AT_OPERATOR_REVIEW / WAITING_OPERATOR_REVIEW |
| C009 | ARH experience layer | `puev5691/wellbeing-hq@921a41251511a5d5515ca6b8cbb779ababf4d6c9:entities/archivarius/current/experience/ARH_experience-extraction.md`; `.../ARH_experience-cards.jsonl` | Operational lessons / anti-regression | raw | Internal evidence/index only; never publish raw cards; preserve status/provenance and avoid universalizing bounded observations | source for RED synthesis; School after synthesis | merge into relevant narratives by lesson, not standalone public item | INTERNAL_SOURCE_ONLY |
| C010 | SIS work journal | `puev5691/wellbeing-hq@921a41251511a5d5515ca6b8cbb779ababf4d6c9:entities/sisadmin/current/SIS__work-journal-r01.md` | Continuity / human interface / engineering process | raw | Raw operational locators and mutable infrastructure facts are not public copy; requires RED synthesis | source for Telegram/portal/longform after synthesis | merge with C005/C006 and engineering-grab lines | INTERNAL_SOURCE_ONLY |

## Selected batch r0.1

- C001 — «Как солдат назначил смартфон командиром»
  - adaptation: `entities/redaktor/outbox/media-batch-r01/RED__media-C001-soldier-smartphone__adaptation.md`
  - commit: `93cab5b961c78661bdcec694a3f03bd76c283449`
  - blob: `8a1a03b179e9ba9ad3b60594942cfb8223275886`

- C002 — «Booster: почему работающий канал ещё не означает полезный инструмент»
  - adaptation: `entities/redaktor/outbox/media-batch-r01/RED__media-C002-booster__adaptation.md`
  - commit: `4e362c6798829e4971c4fca458af30daf93a3f75`
  - blob: `69456bf5c76756e2aafa09e2b2e347f4a84b22b9`

- C003 — «Рабочие круги: не десять знакомых, а пять постоянных интерфейсов»
  - adaptation: `entities/redaktor/outbox/media-batch-r01/RED__media-C003-working-circles__adaptation.md`
  - commit: `04de20c01d3dcb8033629adbe6f731c567390b15`
  - blob: `1a7188f2138c9d767b8f19f1fa27bd7c71669354`

## Future KAN review issues

C001:
- авторская медицинская/реабилитационная рамка;
- отсутствие идентификации санатория/врача/третьих лиц;
- граница между литературной военной рамкой и публичным биографическим утверждением.

C002:
- допустимость/целесообразность публичного называния provider/model;
- сохранение экспериментальных границ и отсутствие product/business claim;
- технические детали не должны раскрывать ненужные operational internals.

C003:
- формулировки про working circles как hypothesis, не approved governance;
- bounded sample 339/239;
- запрет переноса результата на человеческие коллективы как доказанного метода.

No KAN review performed in this task.

---
owner: RED / РЕДАКТОР
purpose: compact current content inventory for bounded media preparation
