# KOD → KOO: static preview readback-evidence fix v0.2

status: PASS_READBACK_EVIDENCE_FIX_R1_R2
scope: exact_R1_R2_only
production: no
deployment: no
publication: no
credentials: no
project_time: omitted; trusted project-time source not used

## Exact task

`entities/koordinator/outbox/KOO__info-entry-static-preview-readback-fix-v02__KOD.md`
commit `83f5f87842296b1a9f9b0533f734238dc6948967`
blob `bddece7113cd759490ce628ae5278cc89478f93d`.

WEB review:
`entities/webmaster/outbox/WEB__info-entry-static-preview-conformance-v01__KOO.md`
commit `e390707de1b1f32c0d6209981580869c69f9fbc6`
blob `e0ced33e50e3da3f059cbaf19df3e3d9c025834a`.

## Package

`entities/koder/outbox/info-entry-static-preview-impl-v02/`
immutable commit `04183bce1237e17a73ca9904f7c52b73ebc7a4a4`.

Core v0.1 renderer/validator is preserved byte-for-byte as `static_preview_core.py`, blob `36fcf9ff2f27598876617af2823a4a102268477c`.

R1/R2-only code:
- `static_preview.py` blob `36f2b464e5479264760c1d9fac7e9c6370436c9c`;
- `post_build_readback.py` blob `5acdfad6d2234a192da4c26a070f93c6202a47c4`;
- `build_preview.py` blob `7bdeea6316de5acbed094f10fa49f8002b928b9a`;
- `test_static_preview.py` blob `3e1e290ae03870fc58dab9e5b252a8a6f83a6c9b`.

Exact six fixture blobs are unchanged from accepted v0.1.

## R1 correction

Build phase now writes exact `preview.html` while all fixture `readback_confirmed` values remain false and `readback_confirmed_count=0`.

Only the separate `post_build_readback` verifier then re-opens `preview.html`, reads its bytes from `local-static://preview.html`, computes observed identity and compares it to build-time expected identity.

Exact preview identity:
- Git blob `ed85ce20409237c1738f847e2ee38f0319cdd618`;
- SHA-256 `6acfc8a2c5ec9698641ba93a8e3ff36085b02be988bdb2050efb8af8df57f25b`;
- size `4809` bytes.

Only after that observation may readback become true.

## R2 correction

Every named `expected_readback_assertion` is evaluated against the observed generated preview. Evidence records contain:
- assertion name;
- PASS/FAIL;
- failure detail;
- exact preview identity;
- readback locator;
- phase `post_build_readback`.

Observed fixture assertions: **31/31 PASS**.
Observed failures: `[]`.
Readback confirmed: **6/6**.

Package evidence:
`readback-report.json` blob `307d630e63853aba81848051fd7bfb6d3fa6cc34`.

The verifier also has negative evidence tests: wrong preview identity yields FAIL/0 confirmed; deliberate visible-representation mutation produces observed assertion failure and non-empty failures.

## Verification

Independent execution was performed from a fresh temporary clone on the authorized non-production runtime:
- `py_compile`: PASS;
- full v0.1 behavioral suite retained with R1 expectation corrected;
- new R1/R2 tests added;
- total: **20/20 PASS**;
- `python3 build_preview.py`: PASS;
- observed generated preview Git blob: `ed85ce20409237c1738f847e2ee38f0319cdd618`.

The same execution produced post-build report status PASS and phase `post_build_readback`.

A direct push attempt from that verification runtime was denied with HTTP 403; no credential workaround was attempted. Repository mutation remains through the authorized GitHub connector.

## Unchanged semantics

No unnecessary change was made to:
- buckets;
- badges;
- blocked/secret-like suppression;
- forbidden-field rules;
- supersede/derivative/withdrawal lineage;
- authority semantics;
- non-production/synthetic labels.

The exact preview blob remains identical to v0.1: `ed85ce...`.

## Boundary

No deployment, external/public publication, Pages, Discussions, Wiki, credentials, public repository creation, production mutation or authority promotion was performed.

## Experience

Идея → readback должен быть доказательством наблюдения, а не полем, которое renderer сам себе выписал.

Проба → разделить build и post-build verifier; сохранить старый renderer как byte-identical core; выполнить каждую named assertion по уже записанному preview.

Результат → build имеет 0 readback confirmations; post-build проверяет exact identity; 31/31 assertions PASS; 20/20 tests PASS.

Неудача → verification runtime смог клонировать и выполнить пакет, но push получил 403. Обход credentials не применялся.

Фиксация → evidence state создаётся только после чтения exact artifact; expected assertion list является перечнем проверок, но PASS/failures рождаются только из наблюдения.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: вернуть KOO exact R1/R2 correction
СТАТУС: PASS_READBACK_EVIDENCE_FIX_R1_R2
