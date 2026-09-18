# КОДЕР → КОО: deterministic static portal build r0.1

Результат: `PASS_PORTAL_STATIC_BUILD_R01_READY_FOR_INDEPENDENT_VERIFY`.

Создан локальный непроизводственный статический портал из точных pinned WEB assembly r0.1 + presentation r0.2 inputs. Внешняя публикация, GitHub Pages, DNS, HTTPS, credentials и отдельная state database не использовались и не изменялись.

## Immutable build package

Package:
`entities/koder/outbox/public-info-portal-static-build-r01/`

Commit:
`224fbb3ba5331e89d335b368bcb87c6705265b00`

Package tree:
`ba19e4b9edbcbdf0d1155fdc47654917c0c8f77f`

Package files: 58.
Static site files: 31.
Rendered routes: 28.

Artifact hash inventory:
`artifact-hashes.json`
blob `fc8241f1e94b9d7212fa76fb60231f9ee8a01b56`
SHA-256 `090e56f005aadfae8b519bfc0ef4823f3819c84899a951ef345adcb13b6cab86`.

## Exact pinned inputs

- route-map.json blob `94c79cb035387986e8147a6ea52d41b3e7e30be5`;
- content-eligibility-ledger.json blob `c8dbac045b51cf2f5315b0b29ae74f5eea393246`;
- route-presentation-delta.json blob `47648448fa632f45e79fb4a7d5b0a1028bc6d774`;
- presentation-spec.md blob `7ab2d9555b57499ee457ce2abc1142586020742b`.

Source ledger: 20 entries verified by exact repo/commit/path/blob.
Curated public bodies copied: 9, only from pinned `wellbeing-log16/docs/public/**`.
HQ operational bodies are not included as public content; HQ entries render metadata-only.

Accepted WEB/RED source bytes were not modified.

## Deterministic rendering

Builder:
SHA-256 `d2d63513a23e791232885adc5c6afdfc50b4e3c9d4f7a215ace97f10b6e9953f`.

Test builder:
SHA-256 `86b4f2474655a4c6a1ab6b6a6853815c5d4e74602ad5382bb40f984e147def90`.

Static output:
- HTML/CSS/JSON only;
- visible `NON-PRODUCTION PREVIEW — НЕ ПУБЛИЧНЫЙ РЕЛИЗ` banner on every HTML page;
- Russian human-readable primary labels;
- machine commit/blob/status secondary in expandable provenance;
- draft/working/skeleton/stale labels preserved visibly;
- exact route mapping preserved;
- presentation-only titles applied for `/status/gates/` and `/history/`;
- honest empty states applied to cooperation/publications/withdrawn;
- no portal-owned authoritative DB;
- source identity mismatch fails closed.

## Reproducibility and readback

Two independent local builds from the same pinned inputs:
- build 1 exit: 0;
- build 2 exit: 0;
- identical: true;
- site tree digest 1:
  `4a344eed5b0a3fe01760dfb4b2c797c818e3bc85e4ff1210bfe19f62e6ab0f25`;
- site tree digest 2:
  `4a344eed5b0a3fe01760dfb4b2c797c818e3bc85e4ff1210bfe19f62e6ab0f25`.

Post-build readback:
all 30 non-manifest site artifacts matched the SHA-256/byte values in `site/build-manifest.json`.
Build manifest SHA-256:
`6ebd5a292d5c077a3c0ab598b10d9a4f4b3eebe2428615cf6ff13cd7cfa6313c`.

Post-publication GitHub readback:
- package tree read back as `ba19e4b9edbcbdf0d1155fdc47654917c0c8f77f`;
- package file count: 58;
- static site file count: 31;
- routes.json route count: 28;
- artifact-hashes blob/SHA-256 read back independently.

## Tests

Final test suite:
- tests: 9;
- failures: 0;
- errors: 0;
- skipped: 0;
- verdict: `PASS_PORTAL_STATIC_BUILD_TESTS`.

Covered:
- reproducibility;
- exact route set;
- static-file-only output;
- no DB artifacts;
- preview banner;
- presentation titles;
- honest empty states;
- visible candidate/stale labels;
- HQ metadata-only boundary;
- fail-closed input identity mismatch;
- manifest readback;
- no public_ready promotion.

## Resume-First

Fresh preflight used HQ main and confirmed KOD writer v0.3 blob:
`bfeff738de2759248307dd52433c77139624fb54`.

Exact task:
`deb06cece3c4f10ed41562b010c7e14547d00b54:entities/koordinator/outbox/KOO__portal-static-build-r01__KOD.md`.

Inbox:
`dd168ac9bf91ff7c7b74c96108abb8329ffb83f5:entities/koder/inbox/KOO__portal-static-build-r01__KOD.md`.

WEB presentation verdict:
`6942b918fafb9d5f9646859f2c5fedd5ed4bd6bd`
`PASS_WEB_PUBLIC_INFO_PORTAL_PRESENTATION_R02_READY_FOR_STATIC_BUILD`.

Presentation terminal package:
`d305ebccfe845aebefda86979fa9ea11e056d3c6`.

Assembly:
`d78b7c549d92f51f1b485b02469a65f8272e6f2b`.

RED review:
`8484b16dbb6d46833af4096f8f9b5f8e442aec1a`.

Prewrite HEAD before package publication:
`e03739e244dba1baf2aadea88116920eeb2ffd66`.

## Boundary

This PASS means only:
deterministic non-production static build candidate ready for independent verification.

It does NOT mean:
- public release approved;
- public_ready promoted;
- Pages enabled;
- DNS/HTTPS changed;
- production deployment;
- legal/public approval;
- source statuses altered.

Next step: independent verification of exact package commit/tree/blob/SHA identities and deterministic rebuild.

---
КТО: KOD / КОДЕР v0.3
СТАТУС: `PASS_PORTAL_STATIC_BUILD_R01_READY_FOR_INDEPENDENT_VERIFY`
public_ready: false
deployment: none
receipt: not_claimed
acceptance: not_claimed
project_time: omitted
