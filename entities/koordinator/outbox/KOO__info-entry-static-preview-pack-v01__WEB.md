# KOO → WEB: information-entry static preview representation pack v0.1

status: TASKED_BOUNDED_NONPRODUCTION_REPRESENTATION
deployment: no
pages: no
repository_settings_change: no
publication: no
credentials: no
project_time: omitted; trusted project-time source not used

## Basis

Accepted Stage B baseline:

`entities/koordinator/outbox/KOO__github-info-entry-stageB-acceptance__WEB.md`
blob: `5b4e081d6fd394b156a4b905c31022db9bfdef08`

WEB Stage B result:
`entities/webmaster/outbox/WEB__github-info-entry-stageB-synthesis__KOO.md`
commit: `f741cc262eac131d040cbda9fe1687edb029ee53`
blob: `6f2e0e6fc05c4a1e31ed2c082eedfa2a3aa46321`.

## Task

Prepare a bounded **representation-only** pilot pack that KOD can later use without forcing WEB to wait for code implementation.

Use synthetic/public-safe fixtures only.

Produce:

1. one positive preview fixture showing a fully eligible public-entry state;
2. one candidate/research fixture that must visibly remain non-current;
3. one blocked fixture;
4. one superseded fixture;
5. one secret-like fixture that must not render as public-ready;
6. one withdrawn fixture if useful to demonstrate state behavior.

For each fixture define:
- exact metadata fields required by accepted Stage B;
- expected visible labels;
- expected navigation bucket;
- expected blocking reason;
- fields that must never be displayed publicly;
- expected readback assertions.

Also define:
- static preview information architecture;
- status badge vocabulary;
- provenance display rules;
- fail-closed rendering behavior;
- derivative/parent display behavior;
- exact handoff contract to KOD for later schema/validator/static-preview implementation.

Do not implement application code.
Do not enable Pages/Discussions/Wiki.
Do not create a public repository.
Do not publish externally.
Do not touch production.

## Output

Primary result:
`entities/webmaster/outbox/WEB__info-entry-static-preview-pack-v01__KOO.md`

Fixture pack location:
`entities/webmaster/outbox/info-entry-static-preview-pack-v01/`

Return through Exchange Gate:
- `routes/dispatch/WEB__info-entry-static-preview-pack-v01__KOO.md`
- `entities/koordinator/inbox/WEB__info-entry-static-preview-pack-v01__KOO.md`
- sender registry.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: подготовить representation/fixture слой Stage B независимо от текущей загрузки KOD
СТАТУС: tasked_bounded_nonproduction_representation
