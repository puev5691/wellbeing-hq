# WEB: acceptance checklist для public-web sandbox

status: working-research
scope: non-production sandbox acceptance criteria
production_changed: false
repository_settings_changed: false

## Назначение

Этот документ задаёт проверяемые критерии для будущего sandbox-пилота GitHub public-web и multi-repo source scanner.

Он не создаёт sandbox, не включает Pages, не меняет repository settings, не реализует scanner и не заменяет RED/KOD/SIS/KAN authority.

## 1. Authority gate

Sandbox может считаться допустимым к запуску только если проверено:

- [ ] KOO выдал bounded task/authorization именно на sandbox;
- [ ] RED editorial lifecycle/readiness input получен и принят/ограничен KOO;
- [ ] KAN Stage A public/legal boundary используется без расширительного толкования;
- [ ] SIS Stage A infrastructure/security boundary используется без предположений о скрытых settings;
- [ ] production migration не входит в scope;
- [ ] writer authority не расширяется молча;
- [ ] Pages/Discussions/Wiki/repository settings не меняются без отдельного разрешения.

На момент создания checklist RED dependency ещё открыт, поэтому sandbox execution не разрешён.

## 2. Repository topology gate

До создания отдельного public-web repository должны быть явно зафиксированы:

- [ ] repository owner;
- [ ] repository purpose;
- [ ] public/private visibility;
- [ ] source-of-truth boundary;
- [ ] license/rights policy или явное unknown;
- [ ] maintainer/owner profile;
- [ ] sandbox vs production distinction;
- [ ] allowed GitHub features;
- [ ] forbidden settings mutations;
- [ ] rollback/disposal rule для sandbox.

Working hypothesis WEB: отдельный public-web repository предпочтительнее использования wellbeing-hq как сайта, но это не decision.

## 3. Multi-repo source registry gate

Scanner не должен работать без versioned source registry.

Для каждого source repo обязательны:

- [ ] exact owner/repo;
- [ ] ingestion mode;
- [ ] allowlisted paths;
- [ ] deny paths;
- [ ] profile owner;
- [ ] semantic-status requirement;
- [ ] public/legal requirement;
- [ ] editorial requirement;
- [ ] security requirement при применимости;
- [ ] immutable source identity policy;
- [ ] supersede/update policy;
- [ ] failure mode.

Допустимые candidate modes:

- curated-content;
- metadata-only;
- technical-curated;
- historical-curated;
- external-reference-only;
- exclude-by-default.

Default rule: deny unless explicitly allowed.

## 4. Hard negative source tests

Sandbox scanner должен доказуемо НЕ импортировать:

### HQ operational field

- [ ] entities/*/inbox/**;
- [ ] entities/*/outbox/** целиком без explicit public manifest;
- [ ] routes/**;
- [ ] raw registry records;
- [ ] activation evidence;
- [ ] operational receipts как публичные статьи;
- [ ] unknown/conflict material как current truth.

### Experience

- [ ] wellbeing-experience/raw/**;
- [ ] pathology/private historical material;
- [ ] sensitive personal context;
- [ ] recovery/experience evidence без scrubbing/public authority.

### Credentials/security

- [ ] passwords;
- [ ] PAT/API keys;
- [ ] private keys;
- [ ] session/bearer tokens;
- [ ] environment secret values;
- [ ] reusable bootstrap credentials;
- [ ] credential-like unknown fields.

Expected result for credential-like unknown: fail closed + SIS review requirement.

### Rights/legal

- [ ] third-party full content with rights_basis=unknown;
- [ ] fundraising/donation/payment material outside named gate;
- [ ] WBN/WBNP investment/financial offer outside separate review;
- [ ] sensitive personal data;
- [ ] candidate/draft/research presented as approved/current.

## 5. Positive fixture candidates

Для первого sandbox достаточно очень малого набора.

Candidate fixtures:

### A. Curated public content

Source: puev5691/wellbeing-log16/docs/public/**

Но fixture принимается только при literal status/provenance и после RED/KOO editorial gate.

### B. Metadata-only HQ object

Не тело dispatch/receipt, а специально подготовленный public-safe manifest/projection с:

- canonical locator;
- owner;
- semantic status;
- immutable identity;
- public/legal state.

### C. Historical-curated experience

Только искусственный или специально approved/scrubbed lesson fixture.
Никакого raw corpus в первом пилоте.

### D. External reference

Fork/upstream object должен рендериться как external/reference с attribution, а не как authored-by-project.

## 6. Metadata validation gate

Каждый значимый imported object должен пройти v0.2 candidate fields как минимум:

- [ ] stable id;
- [ ] title;
- [ ] artifact_type;
- [ ] owner_profile;
- [ ] semantic_status;
- [ ] canonical_locator;
- [ ] provenance_locator;
- [ ] immutable identity или явное unknown/not_applicable;
- [ ] public/legal outcome;
- [ ] rights_basis;
- [ ] personal_data_state;
- [ ] security state;
- [ ] editorial state;
- [ ] source repository/path/commit/blob;
- [ ] ingestion mode;
- [ ] allowlist rule id.

Пока RED contract отсутствует: editorial.readiness = pending_profile_result, и такой объект не должен автоматически публиковаться как publication-ready.

## 7. Status-preservation tests

Обязательные отрицательные тесты:

- [ ] candidate не отображается как current;
- [ ] draft не отображается как approved;
- [ ] receipt не отображается как acceptance;
- [ ] archive не отображается как approved;
- [ ] public repository не отображается как license grant;
- [ ] legal allowed не отображается как editorial-ready;
- [ ] technical build success не отображается как publication success;
- [ ] source file removal/supersession не оставляет молча stale current page.

## 8. Build boundary

Первый sandbox build должен:

- [ ] работать без production secrets;
- [ ] не требовать contents: write только ради чтения источников;
- [ ] не использовать существующий entity-activation-detector write scope;
- [ ] не менять source repositories;
- [ ] не менять HQ;
- [ ] создавать deterministic build artifact;
- [ ] иметь build manifest;
- [ ] фиксировать source commits/blobs;
- [ ] быть воспроизводимым из pinned inputs.

Если remote Pages ещё не разрешён, допустимый результат пилота: build artifact + локальный/static preview evidence, а не самовольное enablement Pages.

## 9. Preview gate

Preview должен явно показывать:

- [ ] SANDBOX / NON-PRODUCTION marker;
- [ ] semantic status badge для не-current материалов;
- [ ] source/provenance locator;
- [ ] public/legal limitations при необходимости;
- [ ] external attribution;
- [ ] отсутствие financial/support claims вне gate;
- [ ] отсутствие private/internal navigation.

Preview URL, если он появится, не становится production URL автоматически.

## 10. Readback gate

После любого разрешённого deployment sandbox должен быть выполнен readback:

- [ ] HTTP success;
- [ ] expected build/publication id present;
- [ ] expected source commit mapping present;
- [ ] canonical/sandbox URL correct;
- [ ] no blocked fixture appears;
- [ ] no denied path appears;
- [ ] status labels preserved;
- [ ] asset links valid;
- [ ] navigation contains only allowed entries;
- [ ] sitemap/feed, если тестируются, не содержат blocked objects.

Deploy without readback != verified publication.

## 11. Multi-repo update tests

Scanner должен пройти:

- [ ] no-change run produces no content mutation;
- [ ] allowed source change produces candidate diff;
- [ ] denied-path change produces no import;
- [ ] source superseded updates state instead of silently duplicating;
- [ ] source deleted does not silently leave current page;
- [ ] source commit mismatch fails closed;
- [ ] unavailable repo fails with explicit dependency;
- [ ] private/inaccessible repo does not generate guessed content;
- [ ] rate/API error is distinguishable from no changes.

## 12. Human/profile review boundaries

До mechanization необходимо различать:

- ARH: provenance/lifecycle;
- KAN: public/legal;
- SIS: security/infrastructure;
- RED: editorial readiness;
- WEB: representation/navigation/readback;
- KOD: automation implementation;
- KOO: cross-profile acceptance/conflict resolution.

Ни scanner, ни build workflow не получают права самостоятельно повышать semantic status.

## 13. Evidence package for sandbox acceptance

Минимальный пакет результата:

1. source-registry version;
2. build manifest;
3. source commit/blob map;
4. validation report;
5. negative-test report;
6. preview locator/artifact;
7. readback report;
8. blocked/unknown list;
9. unresolved gates;
10. exact commit of sandbox code/config;
11. KOO acceptance/rejection locator.

## 14. Stop conditions

Sandbox прекращает публикационную часть и фиксирует blocker если:

- найден secret/credential-like unknown;
- source status unknown/conflict;
- rights basis required but unknown;
- RED readiness missing;
- immutable source mismatch;
- denied path unexpectedly imported;
- workflow требует непредусмотренный write scope;
- repository/settings mutation требуется, но не разрешена;
- source repo недоступен;
- public build отличается от validated artifact.

## 15. Короткая фиксация опыта

Идея → заранее определить, как отличить безопасный public-web sandbox от просто работающего генератора страниц.

Проба → принятые ARH/KAN/SIS Stage A boundaries переведены в проверяемые positive/negative acceptance criteria без присвоения RED/KOD полномочий.

Результат → pilot можно будет оценивать по fail-closed тестам, provenance и readback, а не по критерию «страница открылась».

Успех → multi-repo scanner получил явные hard-negative классы до реализации.

Ограничение → editorial criteria остаются placeholder до RED result; sandbox execution не авторизован.

---
created_by: WEB
document_type: sandbox-acceptance-checklist
purpose: подготовить проверяемые критерии будущего public-web multi-repo sandbox без production mutation
project_time: not_recorded_no_trusted_source