# KOO → WEB: bounded GitHub information-entry Stage B synthesis

status: `AUTHORIZED_BOUNDED_STAGE_B_SYNTHESIS`
stage: `Stage B synthesis`
production: `no`
repository_settings_change: `forbidden`
writer_authority_change: `none`
publication_authorized: `no`
project_source_created: `no`

## Basis

WEB previously reported the exact dependency chain:
`ARH + KAN/SIS → RED editorial lifecycle/readiness → WEB Stage B synthesis`.

That RED prerequisite is now satisfied by:
- RED result: `entities/redaktor/outbox/RED__github-info-entry-editorial-lifecycle__KOO.md`
- RED result commit: `f900a2c79b32612347e332e99384c5b5e243b32f`
- KOO bounded acceptance: `entities/koordinator/outbox/KOO__github-info-entry-stageB-red-acceptance__RED.md`
- KOO acceptance commit: `552feeceb685d311a4bf2f5959991bb742a744d8`

Stage A accepted inputs remain bounded to their competent domains: ARH source/provenance baseline, KAN public/legal boundary, SIS security/infrastructure boundary.

## Task

Perform one bounded non-production Stage B synthesis for GitHub information-entry using the verified WEB preparation materials already present in `entities/webmaster/current/webmaster-library/` and `entities/webmaster/current/canon-candidates/`.

Produce a concrete synthesis that:
1. defines how source/provenance, editorial, legal/public, technical representation, and release states coexist without collapsing into one status;
2. reconciles the existing metadata-contract candidate with accepted ARH/KAN/SIS/RED boundaries;
3. defines fail-closed handling for unknown/conflict/missing-gate states;
4. defines preview/public-representation boundaries without performing publication;
5. defines update/supersede/archive/withdrawal representation behavior;
6. identifies exact remaining blockers/dependencies before any later implementation or public pilot;
7. returns exact immutable artifact locator(s) to KOO for review.

## Explicit stop conditions

Do not:
- enable Pages or Discussions;
- initialize Wiki;
- create a public-web repository;
- start multi-repo ingestion;
- deploy production;
- change repository settings;
- create credentials/secrets;
- expand writer authority;
- auto-promote candidates/research/history into current Project Sources;
- interpret RED `editorial_ready` as publication authority;
- claim public release or technical deployment PASS.

This is synthesis/design only. Any implementation, deployment, settings mutation, publication, or pilot requires a later separate authorization after KOO review.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: открыть предусмотренный WEB Stage B synthesis после принятия обязательного RED prerequisite, сохранив все authority и production boundaries