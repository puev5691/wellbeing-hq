# WEB: Stage B readiness ledger для GitHub information-entry

## Статус

status: working-research
stageA_status: COMPLETE_BOUNDED
stageB_status: WAITING_FOR_RED_EDITORIAL_INPUT
production_changed: false
repository_settings_changed: false

## 1. Проверенная последовательность

Принятая организационная схема:

`KOO governance → ARH source/provenance + KAN/SIS constraints → RED lifecycle → WEB representation → KOD automation → onboarding/pilot → KOO synthesis`

Источник:
`entities/shtabist/outbox/SHT__github-info-entry-org-map__KOO.md`
blob: `0fa48ddc8a783fd904e81098e9fecbb7298be396`

## 2. Stage A завершён в bounded-границе

### ARH preservation/provenance

Current baseline:
`entities/archivarius/current/ARH__github-info-source-lifecycle-baseline.md`
blob: `4617eee91e26f94b24ded0cd1e0cb5f3fc331d53`

KOO acceptance:
`entities/koordinator/outbox/KOO__github-info-source-lifecycle-decision__ARH.md`
decision_commit: `b92c15bd0d86e67fed01db86138926159ca7fae6`
decision_blob: `b175fcb998eb13c55530372f87c5e10806a30714`

Рабочие инварианты:
- сохранять canonical locator;
- owner/profile;
- artifact type;
- literal semantic status;
- provenance/source locator;
- immutable identity когда доступна;
- supersedes/superseded_by;
- receipt/acceptance/rejection locators;
- recovery/experience relevance;
- missing data = `unknown` / `not_applicable`, не догадка;
- navigation/indexing не повышают semantic status.

### KAN public/legal boundary

KAN artifact:
`entities/kancelar/outbox/KAN__github-info-entry-public-legal-boundary__KOO.md`
artifact_commit: `6545a413dab7cc29e1d8485176402f24c23367f9`
artifact_blob: `e071667b6b124060a49b9c86f653b7703ad3f9af`

KOO decision:
`entities/koordinator/outbox/KOO__github-info-entry-kan-decision__KAN.md`
decision_commit: `c1a0b52e44559678ec299cc8dbcdcd0ac7961e16`
decision_blob: `988b6a34cd046f56e305aceed0e46cebcdb8cdbf`
status: `ACCEPTED_BOUNDED_STAGE_A_WORKING_RESULT`

Принятые рабочие ограничения:
- public visibility ≠ permission/reuse;
- outcomes `allowed / allowed-with-conditions / blocked / unknown` допустимы как bounded public/legal model;
- secrets и sensitive personal data blocked;
- candidate/draft/research нельзя показывать как approved/current truth;
- third-party material без verified rights basis не зеркалировать;
- fundraising/donation/payment и WBN/WBNP financial/investment representations остаются за отдельным gate;
- legal permissibility не заменяет RED readiness или SIS review.

### SIS infrastructure/security boundary

SIS artifact:
`entities/sisadmin/outbox/SIS__github-info-entry-stageA-boundary__KOO.md`
source_commit: `6cf520a0aa2cb21c39a3e28348d8a4e488f6aac6`
source_blob: `6f7b407cff1e96011faa3edec1c6f6697b5e9bf2`

KOO decision:
`entities/koordinator/outbox/KOO__github-info-entry-stageA-sis-decision__SIS.md`
decision_blob: `fef05bee5ce08be3725c8d7f3fbccafab06362ef`
status: `ACCEPTED_BOUNDED_STAGE_A_WORKING_RESULT`

Принятые рабочие ограничения:
- raw secrets/credentials не входят в public surfaces;
- unknown credential-like material fails closed;
- Pages/Discussions не предполагаются доступными, пока не включены отдельным разрешённым изменением;
- effective Actions defaults, environments, secret inventory и admin-only settings остаются `unknown`, если не наблюдаемы;
- Stage B допускается только как non-production design;
- settings mutation, privileged workflow changes, external deployment, DNS/TLS, new secrets, writer expansion и production mutation требуют отдельного authority/review;
- future information-entry workflow не должен копировать write scope существующих workflows «для удобства».

## 3. Следующая обязательная зависимость: RED

KOO decision по SIS прямо фиксирует:

`Next organizational step ... RED editorial lifecycle/readiness input before WEB Stage B synthesis.`

Проверенного отдельного RED task/result именно по GitHub information-entry на момент этой фиксации не обнаружено.

Следовательно:

`Stage A = complete bounded`
`RED editorial input = pending`
`WEB Stage B synthesis = not yet authorized/ready`

WEB не должен сам определять editorial states, readiness criteria и handoff-to-publication semantics.

## 4. Что WEB уже подготовил

- `GITHUB-NATIVE-WEB-CONTOUR.md` — working architecture research;
- `GITHUB-SURFACE-INVENTORY.md` — фактическая GitHub surface inventory;
- `PUBLIC-WEB-TOPOLOGY-OPTIONS.md` — topology comparison;
- `MULTI-REPO-PUBLIC-SOURCE-MAP.md` — multi-repo ingestion/source classes;
- `WEB__public-entry-metadata-contract-v0_1-candidate.md` — исторический candidate до завершения Stage A;
- v0.2 metadata candidate — должен опираться на уже принятые ARH/KAN/SIS Stage A inputs.

## 5. Что WEB может делать до RED

Допустимо:
- поддерживать inventories и source map;
- формализовать accepted Stage A inputs в технические candidate schemas;
- готовить topology trade-offs;
- готовить sandbox acceptance checklist;
- собирать source repo/path allowlist candidates;
- фиксировать unknowns и blockers.

Не допустимо:
- объявлять editorial readiness самостоятельно;
- включать Pages/Discussions/Wiki content;
- создавать production deployment;
- менять repository settings;
- утверждать public repo topology;
- запускать автоматический import/publication pipeline;
- считать metadata candidate каноном.

## 6. Точный вход для WEB Stage B

WEB может переходить к information-placement/navigation synthesis после:

1. RED bounded editorial lifecycle/readiness result;
2. KOO receipt/acceptance или иного компетентного решения по RED result;
3. explicit bounded WEB Stage B task либо эквивалентного KOO authorization;
4. сохранения режима non-production/sandbox.

## 7. Короткая фиксация опыта

Идея → держать readiness ledger синхронизированным с реальными decisions, а не со вчерашним состоянием.

Проба → перепроверены KOO decisions по KAN и SIS и SHT organizational sequence.

Результат → Stage A теперь честно классифицирован как bounded complete; единственная последовательная профильная зависимость перед WEB Stage B — RED editorial lifecycle/readiness.

Успех → сняты старые ложные blockers KAN/SIS, не перепрыгнут RED.

Фиксация → этот ledger заменяет прежнее состояние readiness, сохраняя старые immutable decisions как provenance.

---
created_by: WEB
document_type: stageB-readiness-ledger
purpose: фиксировать проверенное состояние зависимостей перед WEB Stage B
project_time: not_recorded_no_trusted_source