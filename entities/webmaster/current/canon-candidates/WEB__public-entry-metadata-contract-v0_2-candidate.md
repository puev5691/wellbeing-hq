# WEB: public-entry metadata contract v0.2 candidate

status: candidate
normative_effect: none_until_approved
stageA_basis: accepted_bounded_working_results
production_changed: false
repository_settings_changed: false

## Назначение

Технический candidate metadata contract для будущего GitHub public-entry после завершения bounded Stage A.

Он опирается на принятые рабочие результаты ARH + KAN + SIS, но не заменяет RED editorial lifecycle и не является каноном.

## 1. Accepted Stage A basis

### ARH
`canonical_locator`, `owner/profile`, `artifact_type`, literal `semantic_status`, provenance, immutable identity, supersession и exchange evidence.

### KAN
`public_legal_outcome` со значениями:
- `allowed`;
- `allowed-with-conditions`;
- `blocked`;
- `unknown`.

Также:
- `rights_basis`;
- `personal_data_state`;
- named next gate для blocked/unknown.

### SIS
Security/publication contract должен fail closed для secrets/credential-like data и не предполагать Pages, Discussions, workflow write rights, environments, secrets или deployment settings без отдельной проверки.

## 2. Candidate object model

```yaml
id: "stable-logical-id"
title: "human-readable-title"
artifact_type: "document|publication|page|code|dataset|operational-evidence|other"
owner_profile: "profile-or-entity"

semantic_status: "approved|current|candidate|draft|working-research|operational-evidence|legacy|superseded|archive|historical|unknown|conflict"

canonical_locator: "repo/path/or-approved-locator"
provenance_locator: "source-locator"

immutable_identity:
  scheme: "git|sha256|other|not_applicable|unknown"
  commit: null
  blob: null
  digest: null

supersedes: []
superseded_by: []

exchange_evidence:
  dispatch: []
  receipts: []
  acceptance: []
  rejection: []

public_legal:
  authority_state: "accepted_bounded_stageA_model"
  outcome: "allowed|allowed-with-conditions|blocked|unknown"
  rights_basis: "project-owned|explicit-license|permission|public-domain|quotation-exception-claimed|unknown|not_applicable"
  personal_data_state: "none|minimised-reviewed|sensitive-blocked|unknown|not_applicable"
  conditions: []
  next_gate: null

security:
  authority_state: "accepted_bounded_stageA_model"
  sensitivity: "public-safe|requires-SIS-review|blocked-secret|unknown|not_applicable"
  review_locator: null
  requires_privileged_setting: false

editorial:
  authority_state: "pending_RED_profile_result"
  readiness: "unknown|not_applicable|pending_profile_result"
  review_locator: null

presentation:
  audiences: []
  navigation_labels: []
  public_summary: null
  canonical_public_url: null
  feeds: []

publication:
  eligible: "unknown"
  reason: "requires all applicable authority gates"
  published: false
  readback_locator: null
```

## 3. Fail-closed rules

`publication.eligible` не выводится из одного поля.

Запрещённые сокращения логики:
- `current` ≠ `public`;
- public repository ≠ reuse permission;
- `receipt` ≠ `acceptance`;
- `archive` ≠ `approved`;
- `candidate` ≠ project position;
- legal `allowed` ≠ editorial-ready;
- editorial-ready ≠ infrastructure-safe;
- отсутствие найденного секрета ≠ доказанное отсутствие секрета;
- `has_pages=false` нельзя обходить предположением, что deploy surface уже существует.

## 4. Public/legal gate

На базе принятого KAN Stage A:

- `blocked` → public navigation/build запрещён;
- `unknown` → fail closed для default-current public exposure;
- `allowed-with-conditions` → каждая condition должна иметь evidence;
- `allowed` → разрешает только переход к следующим gates.

## 5. Security gate

На базе принятого SIS Stage A:

- reusable credential/secret → `blocked-secret`;
- credential-like unknown → `unknown` + SIS review;
- security-sensitive operational evidence → `requires-SIS-review`;
- settings/workflow/deployment dependency отмечается отдельно;
- public-web design не предполагает existing Pages/Discussions/write permissions.

## 6. Editorial gate

RED vocabulary пока не получена.

До RED result:
`editorial.authority_state = pending_RED_profile_result`
`editorial.readiness = pending_profile_result`

WEB не должен придумывать промежуточные editorial states от себя.

## 7. Multi-repo source extension

Для импортируемого материала добавить:

```yaml
source_repository:
  repo: "owner/name"
  path: "path"
  source_commit: "sha"
  source_blob: "sha"
  ingestion_mode: "curated-content|metadata-only|technical-curated|historical-curated|external-reference-only|exclude-by-default"
  allowlist_rule: "rule-id"
```

Импорт без `source_commit/source_blob` для значимого Git-объекта должен считаться неполным, если immutable identity доступна.

## 8. Future schema path

После RED result и KOO Stage B authorization этот candidate можно преобразовать в:
- JSON Schema;
- Markdown/frontmatter schema;
- import manifest schema;
- fixtures positive/negative;
- GitHub Action validator;
- exporter/importer contract;
- publication/readback manifest.

## 9. Источники authority

ARH baseline:
`entities/archivarius/current/ARH__github-info-source-lifecycle-baseline.md`

KAN acceptance:
`entities/koordinator/outbox/KOO__github-info-entry-kan-decision__KAN.md`
decision_commit: `c1a0b52e44559678ec299cc8dbcdcd0ac7961e16`

SIS acceptance:
`entities/koordinator/outbox/KOO__github-info-entry-stageA-sis-decision__SIS.md`
source SIS commit: `6cf520a0aa2cb21c39a3e28348d8a4e488f6aac6`

## 10. Короткая фиксация опыта

Идея → не редактировать старый candidate так, будто KAN/SIS всегда были accepted.

Проба → создана новая v0.2 на основании реально принятых bounded Stage A decisions.

Результат → legal/security поля теперь имеют проверенную Stage A authority basis, а editorial часть честно остаётся pending RED.

Успех → история v0.1 сохраняет прежнюю фазу, v0.2 отражает новую.

---
created_by: WEB
document_type: public-entry-metadata-contract-candidate
purpose: technical metadata candidate after bounded Stage A completion
project_time: not_recorded_no_trusted_source