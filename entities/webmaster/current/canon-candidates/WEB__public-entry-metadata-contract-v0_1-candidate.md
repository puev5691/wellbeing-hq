# WEB: candidate metadata contract для public information-entry

status: candidate
normative_effect: none_until_approved
production_changed: false
repository_settings_changed: false

## Назначение

Этот документ предлагает технический metadata contract для объекта, который потенциально может быть показан через будущий GitHub public-entry: Pages, Wiki-facing navigation, public index, feed или contributor/documentation layer.

Он не утверждает право публикации объекта и не превращает material status в более высокий.

## 1. Источники требований

### A. Уже принятый KOO Stage A preservation/provenance baseline

Опора:
`entities/koordinator/outbox/KOO__github-info-source-lifecycle-decision__ARH.md`

Из него в candidate переносятся как уже поддержанные Stage A invariants:

- literal semantic status;
- canonical locator;
- owner/profile;
- artifact/document type;
- provenance/source locator;
- immutable identity, когда доступна;
- supersedes/superseded_by;
- receipt/acceptance/rejection locator, когда применимо;
- recovery/experience relevance;
- missing data представляется как `unknown` или `not_applicable`, а не угадывается.

### B. KAN returned profile result, pending KOO acceptance

Опора:
`entities/kancelar/outbox/KAN__github-info-entry-public-legal-boundary__KOO.md`

KAN предложил дополнительные public metadata:

- public_legal_outcome;
- rights_basis;
- personal_data_state;
- named next gate при blocked/unknown.

Эти поля полезны и включены ниже, но помечаются как `pending_KOO_acceptance` до отдельного решения KOO по KAN-result.

### C. RED/SIS inputs ещё не получены

Editorial readiness и security/infrastructure review должны иметь место в модели, но их vocabularies пока нельзя выдумывать.

Поэтому поля для них допускают только нейтральное состояние `unknown/not_applicable/pending_profile_result` до профильных результатов.

## 2. Candidate object model

```yaml
id: "stable-logical-id"
title: "human-readable title"
artifact_type: "document|publication|page|code|dataset|operational-evidence|other"
owner_profile: "WEB|ARH|RED|KOD|SIS|KAN|KOO|..."

semantic_status: "approved|current|candidate|draft|working-research|operational-evidence|legacy|superseded|archive|historical|unknown|conflict"

canonical_locator: "repo/path/or-approved-locator"
provenance_locator: "source locator"

immutable_identity:
  scheme: "git|sha256|other|not_applicable|unknown"
  commit: "optional"
  blob: "optional"
  digest: "optional"

supersedes: []
superseded_by: []

exchange_evidence:
  dispatch: []
  receipts: []
  acceptance: []
  rejection: []

recovery_experience:
  relevance: "yes|no|unknown|not_applicable"
  locators: []

public_legal:
  source_status: "pending_KOO_acceptance"
  outcome: "allowed|allowed-with-conditions|blocked|unknown"
  rights_basis: "project-owned|explicit-license|permission|public-domain|quotation-exception-claimed|unknown|not_applicable"
  personal_data_state: "none|minimised-reviewed|sensitive-blocked|unknown|not_applicable"
  next_gate: "named authority/action or null"

editorial:
  readiness: "unknown|not_applicable|pending_profile_result"
  review_locator: null

security:
  review_state: "unknown|not_applicable|pending_profile_result"
  review_locator: null

presentation:
  audiences: []
  navigation_labels: []
  public_summary: null
  canonical_public_url: null
  feeds: []

publication:
  eligible: "unknown"
  reason: "derived only after required gates"
  published: false
  readback_locator: null
```

## 3. Жёсткое правило вывода publication eligibility

`publication.eligible` нельзя заполнять только по одному признаку.

В частности:

- `semantic_status=current` не означает `public`;
- `repository visibility=public` не означает `rights_basis=allowed`;
- `receipt` не означает `acceptance`;
- `archive` не означает `approved`;
- `candidate` не означает `project position`;
- `editorial-ready` не означает legal-ready;
- `legal allowed` не означает editorial-ready;
- отсутствие blocker metadata не означает отсутствия blocker.

До профильных решений safest value: `unknown`.

## 4. Candidate gating logic

### Gate 1: identity/provenance

Для значимого объекта должны быть определены:

- owner_profile;
- artifact_type;
- semantic_status;
- canonical_locator;
- provenance_locator;
- immutable_identity, если она технически доступна.

Если объект `unknown/conflict`, он не должен автоматически попадать в default-current navigation.

### Gate 2: public/legal

До KOO acceptance KAN-result этот gate остаётся candidate.

Предлагаемая будущая логика:

- `blocked` → не публиковать;
- `unknown` → не публиковать как default-current;
- `allowed-with-conditions` → условия должны иметь evidence;
- `allowed` → переход к следующим gates, а не немедленная публикация.

### Gate 3: editorial

Vocabulary и критерии должен вернуть RED.

До этого:
`editorial.readiness = pending_profile_result`.

### Gate 4: security/infrastructure

Vocabulary и критерии должен вернуть SIS.

До этого security-sensitive classes не считаются автоматически безопасными.

### Gate 5: WEB representation

WEB определяет только способ корректного представления уже классифицированного объекта:

- route;
- label;
- audience;
- navigation position;
- canonical public URL;
- feed inclusion;
- status badge/notice;
- readback behavior.

WEB не меняет semantic/public/legal/editorial authority самим отображением.

## 5. Минимальный набор для public navigation candidate

Чтобы объект вообще рассматривать для public navigation, WEB предлагает требовать:

1. id;
2. title;
3. owner_profile;
4. artifact_type;
5. semantic_status;
6. canonical_locator;
7. provenance_locator;
8. immutable_identity либо явное `not_applicable/unknown`;
9. public_legal outcome после его утверждения;
10. rights_basis после его утверждения;
11. personal_data_state после его утверждения;
12. editorial readiness после RED contract;
13. security state при применимости;
14. canonical_public_url только после фактической публикации;
15. readback evidence после публикации.

## 6. Presentation labels candidate

WEB может технически поддерживать явные status labels:

- CURRENT / APPROVED;
- CANDIDATE;
- DRAFT;
- RESEARCH;
- OPERATIONAL EVIDENCE;
- LEGACY / SUPERSEDED;
- ARCHIVE / HISTORICAL;
- UNKNOWN / CONFLICT — не в default-current navigation.

Точная русская/английская лексика и визуальный стиль требуют RED/WEB design, но semantic status должен оставаться машинно-читаемым и неизменённым.

## 7. Почему metadata contract нужен до сайта

Без общего контракта сайт неизбежно начнёт решать смысловые вопросы шаблонами и условными операторами.

С контрактом:

    source object
       ↓
    metadata validation
       ↓
    authority gates
       ↓
    WEB presentation
       ↓
    publication/readback

Это позволяет Pages, Wiki index, feeds и внешним adapters использовать одну и ту же классификацию без повторной интерпретации смысла.

## 8. Что пока запрещено считать решённым

- KAN поля не стали общепроектной нормой без KOO acceptance;
- RED editorial vocabulary отсутствует;
- SIS security vocabulary отсутствует;
- authority matrix для создания public repo отсутствует;
- schema не является build contract;
- автоматическая публикация по этому candidate запрещена;
- current website не затрагивается.

## 9. Следующий технический шаг после профильных inputs

После KOO/RED/SIS результатов этот candidate можно превратить в:

- versioned JSON Schema;
- frontmatter schema для статей/страниц;
- validation action;
- exporter manifest contract между source layer и public-web;
- fixtures: allowed / blocked / candidate / legacy / operational evidence;
- automated negative tests, подтверждающие fail-closed behavior.

## 10. Короткая фиксация опыта

Идея → перевести будущие правила размещения из текста в проверяемый metadata contract.

Проба → разделены уже принятые ARH invariants, pending KAN fields и ещё отсутствующие RED/SIS vocabularies.

Результат → появился candidate object model, пригодный для последующей формализации в JSON Schema.

Успех → WEB может готовить техническую механику, не присваивая себе semantic/legal/editorial authority.

Ограничение → часть полей остаётся условной до KOO acceptance и профильных RED/SIS результатов.

Фиксация → этот candidate в WEB current library.

---

created_by: WEB
document_type: public-entry-metadata-contract-candidate
status: candidate
purpose: подготовить проверяемую структуру metadata для будущего GitHub public-entry без преждевременного утверждения policy
production_changed: false
repository_settings_changed: false
project_time: not_recorded_no_trusted_source