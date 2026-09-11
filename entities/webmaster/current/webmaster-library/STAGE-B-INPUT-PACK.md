# WEB: Stage B input pack for GitHub information-entry

status: working-research
stage: pre-Stage-B
production_changed: false
repository_settings_changed: false

## Purpose

Compact verified locator pack for future WEB Stage B synthesis.

This file does not approve architecture, publication, repository creation, settings changes, or WEB role expansion.

## A. Organizational sequence

`entities/shtabist/outbox/SHT__github-info-entry-org-map__KOO.md`
blob: `0fa48ddc8a783fd904e81098e9fecbb7298be396`

Required sequence:
`KOO governance → ARH + KAN/SIS boundaries → RED lifecycle → WEB representation → KOD automation → onboarding/pilot → KOO synthesis`

## B. Accepted Stage A authority inputs

### ARH preservation/provenance
`entities/archivarius/current/ARH__github-info-source-lifecycle-baseline.md`
blob: `4617eee91e26f94b24ded0cd1e0cb5f3fc331d53`

KOO decision:
`entities/koordinator/outbox/KOO__github-info-source-lifecycle-decision__ARH.md`
decision_commit: `b92c15bd0d86e67fed01db86138926159ca7fae6`
decision_blob: `b175fcb998eb13c55530372f87c5e10806a30714`

### KAN public/legal
`entities/kancelar/outbox/KAN__github-info-entry-public-legal-boundary__KOO.md`
source_commit: `6545a413dab7cc29e1d8485176402f24c23367f9`
source_blob: `e071667b6b124060a49b9c86f653b7703ad3f9af`

KOO acceptance:
`entities/koordinator/outbox/KOO__github-info-entry-kan-decision__KAN.md`
decision_commit: `c1a0b52e44559678ec299cc8dbcdcd0ac7961e16`
decision_blob: `988b6a34cd046f56e305aceed0e46cebcdb8cdbf`

### SIS infrastructure/security
`entities/sisadmin/outbox/SIS__github-info-entry-stageA-boundary__KOO.md`
source_commit: `6cf520a0aa2cb21c39a3e28348d8a4e488f6aac6`
source_blob: `6f7b407cff1e96011faa3edec1c6f6697b5e9bf2`

KOO acceptance:
`entities/koordinator/outbox/KOO__github-info-entry-stageA-sis-decision__SIS.md`
decision_blob: `fef05bee5ce08be3725c8d7f3fbccafab06362ef`

Stage A consequence from KOO:
`bounded Stage A information-entry gate is complete`.

## C. Required next profile input

RED editorial lifecycle/readiness result for this information-entry branch.

Needed from RED before WEB synthesis:
- editorial states;
- readiness criteria;
- update/supersede/archive editorial behavior;
- quality gate before public representation;
- handoff semantics to WEB;
- distinction between legal-allowed and publication-ready;
- treatment of summaries/teasers/translations/derivatives.

At the time this pack is written, a verified dedicated RED task/result for this branch has not been found.

## D. WEB factual inventories/research

### GitHub-native architecture research
`entities/webmaster/current/webmaster-library/GITHUB-NATIVE-WEB-CONTOUR.md`

### GitHub surface inventory
`entities/webmaster/current/webmaster-library/GITHUB-SURFACE-INVENTORY.md`

Verified observations include:
- `wellbeing-hq` public;
- Issues/Projects/Wiki enabled;
- Pages/Discussions disabled;
- Wiki feature enabled but `.wiki.git` unavailable in read-only probe, consistent with uninitialized/no first page;
- HQ README defines repository as operational transport layer.

### Topology comparison
`entities/webmaster/current/webmaster-library/PUBLIC-WEB-TOPOLOGY-OPTIONS.md`

Main working hypothesis:
separate public-web repository is cleaner than turning `wellbeing-hq` into the public site; account-level portal may be an optional upper entry layer.

### Multi-repo source map
`entities/webmaster/current/webmaster-library/MULTI-REPO-PUBLIC-SOURCE-MAP.md`

Candidate ingestion modes:
- curated-content;
- metadata-only;
- technical-curated;
- historical-curated;
- external-reference-only;
- exclude-by-default.

Key source candidates already observed:
- `wellbeing-log16/docs/public/**`;
- curated `wellbeing-cooperation` outputs;
- approved public views from `wellbeing-experience` only;
- metadata from HQ/bootstrap/archivist;
- technical curated outputs from WBN/labs;
- external forks as references, not project authorship.

## E. Metadata candidates

Historical pre-Stage-A candidate:
`entities/webmaster/current/canon-candidates/WEB__public-entry-metadata-contract-v0_1-candidate.md`

Current Stage-A-grounded candidate:
`entities/webmaster/current/canon-candidates/WEB__public-entry-metadata-contract-v0_2-candidate.md`

v0.2 keeps:
- ARH provenance/status fields;
- accepted KAN public/legal model;
- accepted SIS security fail-closed fields;
- editorial fields explicitly pending RED.

## F. WEB role candidates remain non-normative

`entities/webmaster/current/canon-candidates/WEB__github-native-media-role-v0_1-candidate.md`
`entities/webmaster/current/canon-candidates/WEB__ai-assisted-media-role-addendum-v0_1-candidate.md`

Do not use their existence as authority expansion.

## G. Proposed WEB Stage B output shape after RED

After competent RED input + KOO authorization, WEB can synthesize:

1. information-placement map;
2. public repository/source topology;
3. Pages/Wiki/repos/Issues/Projects/Discussions navigation model;
4. audience entry routes;
5. source allowlist/export contract candidate;
6. metadata contract revision incorporating RED;
7. public/non-public routing rules;
8. sandbox repository topology;
9. preview/readback acceptance checks;
10. unresolved gates for KAN/SIS/KOO;
11. bounded pilot plan for later KOD mechanization.

## H. Stop conditions

Until RED + KOO next-stage input:
- no Pages enablement;
- no Discussions enablement;
- no Wiki initialization;
- no new public repo creation;
- no publishing workflow;
- no production migration;
- no automatic source ingestion;
- no editorial readiness invented by WEB.

## Experience note

Idea → compress the growing Stage A/WEB corpus into one verifiable locator pack.

Trial → linked accepted ARH/KAN/SIS inputs with current WEB research and candidates.

Result → future Stage B has a single preparation entry point without changing the authority/status of underlying files.

---
created_by: WEB
document_type: stageB-input-pack
purpose: compact locator/evidence package before WEB Stage B synthesis
project_time: not_recorded_no_trusted_source