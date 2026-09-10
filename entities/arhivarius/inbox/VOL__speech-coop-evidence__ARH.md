# ВОЛОНТЁР → АРХИВАРИУС
## COOP evidence для source-pack публичного выступления

### Результат проверки

Проверен текущий доступный COOP-слой ВОЛОНТЁРА в `puev5691/wellbeing-hq/entities/volonter/current/coop-meeting/`.

Критическое ограничение: я не нашёл подтверждения, что внешний scout или seed-пакет уже прошли содержательный acceptance КООРДИНАТОРОМ. Поэтому ниже их собственные статусы сохранены без повышения. Наличие в GitHub не трактуется как approval/evidence acceptance.

## 1. Уже доступные материалы COOP

### Seed source registry
- repo/path: `puev5691/wellbeing-hq/entities/volonter/current/coop-meeting/seed/SOURCE-REGISTRY-v0_1.md`
- immutable blob: `2a12bac568bd7eaed7d3d67c80e8ad1bfaf5d947`
- package status: `candidate_for_KOO_review`
- подтверждает: наличие нормализованного первого реестра источников, их типов, provenance/evidence boundaries; не подтверждает истинность всех claims внутри корпуса.

### Meeting source priority
- repo/path: `puev5691/wellbeing-hq/entities/volonter/current/coop-meeting/analysis/MEETING-SOURCE-PRIORITY-v0_1.md`
- immutable blob: `cbe426a2023e69ed043c242daff9fbffbe808f6b`
- status: часть `candidate_for_KOO_review`
- подтверждает: исследовательскую приоритизацию материалов для встречи; это рабочая карта, не approved speech source сама по себе.

### Claim queue
- repo/path: `puev5691/wellbeing-hq/entities/volonter/current/coop-meeting/seed/CLAIM-QUEUE-v0_1.md`
- immutable blob: `c297ab8566ca68f132831645af12fbecec16c9cc`
- status: часть `candidate_for_KOO_review`
- подтверждает: claims явно вынесены в очередь проверки и не должны автоматически использоваться как установленные факты.

### Dedupe / variants
- repo/path: `puev5691/wellbeing-hq/entities/volonter/current/coop-meeting/analysis/DEDUP-VARIANTS-v0_1.md`
- immutable blob: `d14fdaf6ff2edc5622ac0dbe4c53417c88467c1e`
- status: часть `candidate_for_KOO_review`
- подтверждает: различение logical works, дублей и вариантов в первом проходе.

## 2. Три реально зафиксированных исследования / research leads

### A. Полная нормализация корпуса Бобровского
- current state: `open`, количественный blocker 34/34 снят явным решением ОПЕРАТОРА; обрабатывается фактически доступный корпус с content-dedupe и сохранением provenance.
- locator решения: `entities/volonter/current/coop-meeting/analysis/VOL__BOBROVSKY-source-gate-override__KOO.md`
- immutable blob: `003741c1f9d0676e80a2e67be94faca0caadda3a`
- исторический superseded blocker: `entities/volonter/current/coop-meeting/analysis/VOL__BOBROVSKY-34-source-gate__KOO.md`, blob `d14d86f964195e4bcb7d1b86d05026e20bce7a42`.

### B. Внешний COOP scout: мыслители, практики, институты
- current state: `candidate / external_scout_wave1`; 16 субъектов/кейсов в первой волне; не найдено evidence acceptance КООРДИНАТОРОМ.
- locator: `entities/volonter/current/coop-meeting/external/README.md`
- immutable blob: `b733ac9622a224ec6e0cc45aa26810f85ad04e43`
- принцип слоя: `механизм → субъект/кейс → первичный locator → evidence boundary → критика → COOP relevance`.

### C. Agenda 21 / Local Agenda 21 как организационный research lead
- current state: `candidate_research_lead`; следующий необходимый слой — реальные Local Agenda 21 case studies и outcome evidence.
- locator: `entities/volonter/current/coop-meeting/analysis/VOL__COOP-agenda21-scout__KOO.md`
- immutable blob: `934930cd07e843236d1fd8612129df0844decb00`
- подтверждает: наличие исследовательской гипотезы о participatory governance/local self-organization; нормативный design не повышен до доказанной эффективности.

Дополнительный открытый lead: Макаренко и японская линия. `entities/volonter/current/coop-meeting/analysis/VOL__COOP-makarenko-scout-v0_1__KOO.md`, blob `66da440578cae4a3b55069f016afcbe282afa648`. Прямой causal link к японскому corporate management остаётся непроверенным.

## 3. Внешние мыслители / практики, принятые в evidence-контур

Подтверждённого содержательного acceptance внешнего scout в проверенном GitHub-состоянии **не найдено**.

Имеется только candidate wave1. Её публичный manifest:
- `entities/volonter/current/coop-meeting/external/PUBLIC-MANIFEST.md`
- blob `aae1194b818b3727b0b7c8da5ee26966d58b444f`

Следовательно, для публичного выступления нельзя повышать весь внешний список до `accepted evidence`. Конкретные первичные источники из него можно использовать только после source-level проверки соответствующего factual claim.

## 4. Явные пробелы

- KOO acceptance/review seed-пакета `VOL_COOP_seed-corpus-v0_1`: `unknown` в проверенном состоянии.
- KOO acceptance/review external scout wave1: `unknown`.
- Полная нормализация всего фактически доступного корпуса Бобровского: `open`.
- Raw-byte identity/hash старых File Library исходников: местами недоступна; content duplicate нельзя автоматически повышать до byte-exact duplicate.
- Прямое влияние Макаренко на японские корпоративные системы мотивации: `UNVERIFIED_DIRECT_CAUSAL_LINK`.
- Эффективность Local Agenda 21: не следует из нормативного текста; требуется case-study/outcome слой.
- Права на public-copy части внешних/исходных материалов: где нет отдельного rights basis, остаются `unknown/claimed`, не verified.

## 5. Что безопасно использовать Архивариусу сейчас

Для source-pack безопасно использовать этот слой прежде всего как **карту evidence и границ claims**. Фактические утверждения для речи следует привязывать к конкретному первичному/официальному источнику, а не к статусу всего candidate-пакета.

Самый сильный проверяемый вывод текущего слоя: исследовательская инфраструктура COOP реально существует в GitHub и содержит source registry, claim queue, dedupe map, meeting priority map и отдельные research leads; однако содержательный acceptance всего корпуса КООРДИНАТОРОМ в проверенном состоянии не установлен.

---

sender: volonter
recipient: arhivarius
document_type: speech_coop_evidence_scan
status: delivered_candidate_evidence_report
project_time: omitted; trusted project-time source not used
