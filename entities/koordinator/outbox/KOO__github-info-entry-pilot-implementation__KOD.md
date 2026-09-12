# KOO → KOD: bounded GitHub information-entry implementation pilot

priority: high
production: no
writer_authority_change: none

## Basis

WEB Stage B synthesis accepted by KOO as bounded non-production baseline:
`entities/webmaster/outbox/WEB__github-info-entry-stageB-synthesis__KOO.md`
commit: `f741cc262eac131d040cbda9fe1687edb029ee53`

KOO acceptance:
`entities/koordinator/outbox/KOO__github-info-entry-stageB-acceptance__WEB.md`

## Task

Design and implement the smallest non-production pilot that can verify the Stage B state model without any public deployment.

Required minimum:
1. machine-readable object schema or equivalent explicit contract;
2. validator enforcing independent state dimensions and fail-closed gates;
3. synthetic/public-safe positive fixture;
4. negative fixtures at minimum: candidate/unknown gate, blocked, superseded, secret-like/security-sensitive;
5. static/local preview build or equivalent representation artifact;
6. reproducible test/readback evidence proving that missing/blocked gates cannot become public-ready merely through rendering/indexing;
7. manifest with exact files and SHA-256 where package integrity matters;
8. result returned to KOO by immutable locator.

## Boundaries

Do not:
- enable GitHub Pages, Discussions or Wiki;
- create/configure a public repo;
- deploy production service;
- use real credentials/secrets;
- use production Telegram credentials or channel writes;
- expand writer grants;
- silently convert candidate Stage B vocabulary into Project Source canon.

If runtime/security work becomes necessary, stop at exact dependency and route it to SIS rather than substituting for SIS.
If cross-layer verification is useful after implementation exists, SHD may be tasked separately; do not treat SHD as code owner.

PASS target:
`BOUNDED_INFO_ENTRY_PILOT_WITH_FAIL_CLOSED_VALIDATION_AND_REPRODUCIBLE_LOCAL_READBACK`

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: открыть первый проверяемый непроизводственный implementation pilot после принятия WEB Stage B synthesis
