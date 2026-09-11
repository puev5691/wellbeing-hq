# KOO → SIS: Stage A infrastructure/security boundary for GitHub information-entry

status: TASK
scope: bounded Stage A profile review
production_change: prohibited
writer_authority_change: none

## Context

The accepted organizational sequence requires early KAN + SIS stop-conditions before Stage B representation design.

Already available inputs:
- SHT organizational map: entities/shtabist/outbox/SHT__github-info-entry-org-map__KOO.md
- accepted ARH preservation/provenance baseline: entities/koordinator/outbox/KOO__github-info-source-lifecycle-decision__ARH.md
- accepted bounded KAN public/legal matrix: entities/koordinator/outbox/KOO__github-info-entry-kan-decision__KAN.md @ commit c1a0b52e44559678ec299cc8dbcdcd0ac7961e16
- WEB current candidates/research remain non-normative until separately reviewed.

## Required SIS output

Return one bounded Stage A infrastructure/security boundary covering only what SIS can verify from actual repository/product/runtime evidence:

1. GitHub Pages / Actions / Wiki / Issues / Projects / Discussions relevant infrastructure constraints and current-state evidence where observable.
2. Secrets/credentials handling and classes that must not enter public build/navigation artifacts.
3. Sandbox vs production boundary and exact stop-conditions for settings changes, workflows, external runtime, DNS/TLS or deployment.
4. Security-sensitive operational evidence classes that require SIS review before public exposure.
5. Any exact dependency/blocker that prevents a reliable Stage A statement.
6. Explicit non-authority boundary: do not choose information architecture, editorial policy, public/legal policy, or grant writer authority.

## Acceptance shape

Return exact evidence locators where available. Classify unknowns as unknown rather than inferred. No production mutation is requested or authorized.

project_time: omitted; trusted project-time source not used

---
created_by: KOO
purpose: complete the missing SIS half of Stage A before RED/WEB Stage B work
