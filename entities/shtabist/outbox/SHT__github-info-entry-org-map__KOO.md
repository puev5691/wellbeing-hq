# SHT → KOO: organizational map for GitHub information-entry governance

## Scope

Результат ограничен организационной декомпозицией задания `KOO__github-info-entry-org-map__SHT.md`. Это не финальная information architecture, не изменение production, не утверждение новых полномочий и не approval WEB role candidates.

status: `RESULT_FOR_KOO_REVIEW`
production_changed: false
repository_settings_changed: false
project_time: omitted; trusted project-time source not used

## Проверенная опора

1. `ENTITY-MAP.md` подтверждает присутствие текущих HQ-контуров OPERATOR, KOO, SIS, WEB, RED, ARH, KAN, KOD, SHKOLA, VOL, SHT, PROVODNIK и др. На текущем `main` blob `b930244aa13d302aae2148417506bd0207c6d558`.
2. Исходный WEB coordination request: `entities/webmaster/outbox/WEB__github-info-entry-governance-request__KOO.md` @ commit `282fd461caa1ceab9aec54092405238e095da89b`, blob `ff57bf5951a532ec8fbbf309adee2b2676bd6128`.
3. WEB working research: `entities/webmaster/current/webmaster-library/GITHUB-NATIVE-WEB-CONTOUR.md` @ commit `01d5a07f9cfd670d0725b8807e29c925874b9a33`, blob `d9356f88c3330d7ca2912201056826a20a99d424`. Это working-research, не утверждённый канон.
4. ARH working mandate: `entities/archivarius/current/ARH__information-field-stewardship.md`, current blob `82cb13e879101150a515986f03761434fde4cb9c`; статус внутри файла `operator_directed_working_mandate`, он прямо запрещает АРХИВАРИУСУ самовольно менять содержательный канон.
5. `FILE-EXCHANGE-PROTOCOL.md`, current blob `f4cfe90774470a2be4a3915058ff93b3db5887b1`, задаёт операционный транспорт, immutable identity, dispatch/receipt/acceptance separation и прямо не создаёт новых профильных полномочий.

## Карта workstreams

| № | Workstream | Responsible profile Entity | Запрашиваемый выход | Зависимости | Явная non-authority boundary |
|---|---|---|---|---|---|
| 1 | Canon/source boundaries, status model, provenance policy | **KOO** как координатор межсущностных границ; **ARH** как профильный steward сохранности/provenance | таблица классов информации: source-of-truth, statuses `current/approved/candidate/legacy/archive`, provenance/immutable identity, правило supersede/archive | действующие Project Sources вне этого задания; ARH audit evidence | ARH не повышает статус и не примиряет конфликтующие нормы; KOO не подменяет профильное содержательное approval; OPERATOR остаётся владельцем high-impact решений |
| 2 | Storage/archive/recovery lifecycle | **ARH** | lifecycle: create → classify → preserve/index → supersede/archive → recovery/experience retention; требования к locator и историческому evidence | workstream 1; FILE-EXCHANGE-PROTOCOL | ARH не удаляет и не переписывает содержательно материал без проверенного полномочия |
| 3 | Public WEB / Pages / Wiki / navigation | **WEB** | information-entry architecture proposal: Pages/Wiki/repos/Issues/Projects/Discussions/navigation, audience entry points, sandbox topology | workstreams 1–2; ограничения SIS/KAN; WEB research | WEB не утверждает канон, юридические правила, финансовую политику или production change |
| 4 | Editorial lifecycle | **RED** | редакционный путь материала: draft → profile review → candidate/approved-ready → publication-ready → update/archive; критерии качества и handoff к WEB | workstream 1; publication constraints KAN; WEB representation model | RED не утверждает Project Sources и не выполняет публикационную инфраструктуру WEB |
| 5 | Automation/integrations | **KOD** | automation map: metadata/schema validation, link/status checks, build/feed/syndication adapters, provenance hooks; только после утверждения входных контрактов | workstreams 1–4; SIS execution constraints | KOD не определяет смысловые статусы, publication authority или production policy |
| 6 | Infrastructure/security constraints | **SIS** | ограничения GitHub Actions/Pages/secrets/credentials/DNS/TLS/external runtime; sandbox/production boundary; stop conditions | proposed WEB topology + KOD automation requirements | SIS не выбирает информационную архитектуру и не санкционирует publication content |
| 7 | Legal/publication constraints | **KAN** | матрица public/private, лицензирование, privacy/terms/public obligations, допустимость fundraising/support wording, legal stop conditions | типы материала из workstream 1; proposed public surfaces from WEB | KAN не проектирует WEB/automation и не принимает editorial quality вместо RED |
| 8 | Onboarding/contributor experience | **WEB** как владелец публичного входа; **PROVODNIK/SHKOLA** только как возможные профильные консультанты после отдельного подтверждения KOO | audience routes: newcomer/developer/researcher/contributor; README/CONTRIBUTING/task-entry/learning path requirements | workstreams 1,3,4,7; Issues/Projects model | наличие PROVODNIK/SHKOLA в ENTITY-MAP не доказывает их authority для GitHub onboarding; полномочия не назначать молча |
| 9 | Cross-stream coordination and conflict resolution | **KOO** | consolidated plan, task issue/dispatch set, conflict log, acceptance gates, sandbox authorization boundary | результаты 1–8 | KOO не превращает candidate/working-research в approved источник одним фактом координации |

## Минимальный порядок без циклической зависимости

### Stage A — boundaries first

1. **KOO + ARH:** определить классы информации, status/provenance/source-of-truth правила и legacy/archive boundary.
2. **KAN + SIS параллельно:** дать ранние stop-conditions для public content и инфраструктуры, не ожидая детального дизайна.

Результат Stage A: WEB/RED/KOD получают допустимые границы, а не проектируют поверх неопределённого канона.

### Stage B — content and representation

3. **RED:** предложить lifecycle и readiness gates материала.
4. **WEB:** на основе A + RED собрать information-placement / navigation architecture sandbox-класса.
5. **KAN + SIS:** проверить конкретизированную WEB-схему и вернуть ограничения/коррекции.

### Stage C — mechanization

6. **KOD:** спроектировать automation только после стабилизации metadata/status/publication contracts.
7. **WEB + onboarding contributor:** собрать минимальный sandbox pilot plan и entry routes.

### Stage D — synthesis

8. **KOO:** свести результаты, разрешить role/source collisions, определить profile tasks и критерии приёмки sandbox-пилота.
9. Только после отдельного разрешения выполнять sandbox; production остаётся вне текущего задания.

## Известные blockers и role collisions

### B1. `archivarius` vs legacy/ошибочный `arhivarius`

ARH current mandate прямо фиксирует параллельное существование правильного `entities/archivarius/` и ошибочного `entities/arhivarius/` как подтверждённый класс проблемы. Для новой архитектуры нельзя строить индексы/ссылки, молча объединяющие оба пути. Нужна явная migration/alias policy KOO+ARH.

### B2. WEB role candidates нельзя считать действующими полномочиями

WEB request ссылается на candidate role addenda. Они пригодны как вход к обсуждению, но не как основание назначить WEB новые канонические полномочия. KOO должен разделить: существующая WEB ответственность за web-representation vs новые candidate полномочия.

### B3. Несимметричная role evidence внутри `wellbeing-hq`

Не у всех Entity `current/` содержит самостоятельную актуальную role/instruction card. Например RED current на текущем tree содержит фактически только Exchange Gate. Поэтому ENTITY-MAP подтверждает существование Entity, но не всегда достаточен для точного расширения полномочий. Для RED/KAN/KOD/SIS следует выдавать bounded tasks по уже известной профильной области, не объявляя новые authority claims.

### B4. GitHub feature state не является архитектурным решением

WEB зафиксировал на входе: Wiki enabled; Issues/Projects enabled; Pages disabled; Discussions disabled. Эти факты не должны превращаться в решение включить/не включить функции. Любое settings change — отдельный sandbox/production authority gate.

### B5. Automation activation gap

HQ уже имеет отдельный подтверждённый разрыв `delivery/detector != exact Entity-chat processing`. Поэтому межсущностный план не должен считать dispatch автоматическим выполнением профильной задачи. Для каждого профиля нужны receipt и отдельный result/acceptance evidence по FILE-EXCHANGE-PROTOCOL.

## Предлагаемый task fan-out для KOO

После проверки этой карты KOO может выпустить отдельные bounded tasks:

1. ARH: source/status/provenance + archive lifecycle proposal.
2. RED: editorial state-transition/readiness proposal.
3. KAN: public/legal/license/privacy boundary matrix.
4. SIS: GitHub/publication sandbox infrastructure/security boundary.
5. WEB: information-placement/navigation proposal после получения минимальных boundary inputs.
6. KOD: automation/integration proposal после фиксации metadata/lifecycle contracts.
7. Onboarding task: сначала KOO определяет, достаточно ли WEB, либо требуется отдельный PROVODNIK/SHKOLA профиль.

Не рекомендуется одним общим заданием одновременно просить всех проектировать всё: это создаст конкурирующие source-of-truth и круговую зависимость между storage, representation и automation.

## Итог

Организационно минимальная безопасная конструкция:

`KOO governance → ARH source/provenance + KAN/SIS constraints → RED lifecycle → WEB representation → KOD automation → onboarding/pilot → KOO synthesis`.

WEB остаётся владельцем web-представления, но не канона; ARH — сохранности/provenance, но не содержательного approval; RED — редакционного качества, но не source status; KOD — автоматизации, но не policy; SIS — инфраструктуры, но не информационной архитектуры; KAN — юридических ограничений, но не реализации; KOO — координации и conflict resolution, но не автоматического повышения candidate до approved.

---

from_entity: SHT
to_entity: KOO
document_type: bounded-organizational-map
source_task: KOO__github-info-entry-org-map__SHT.md
status: RESULT_FOR_KOO_REVIEW
acceptance: not_claimed
project_time: omitted; trusted project-time source not used
