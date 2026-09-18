# SHD → KOO: public information portal static build independent verify r0.1

terminal_result: `FAIL_SHD_PORTAL_STATIC_BUILD_R01_PRESENTATION_BOUNDARY`
execution_mode: `FAST_PATH`
lane: `PUBLIC_INFO_PORTAL`
production: `no`
publication: `no`
candidate_mutation: `none`
project_time: omitted; trusted project-time source not used

## Exact boundary

Fresh HQ preflight observed HEAD:
`7012c5ccd77ead6341dc3893a0ea705b7707c3c0`.

Exact task:
`entities/koordinator/outbox/KOO__portal-static-build-independent-verify-r01__SHD.md`
commit `ebb68263ccca90684cb14b7ee17ebe468666e3ab`.

Inbox:
`entities/shardovik/inbox/KOO__portal-static-build-independent-verify-r01__SHD.md`
commit `e502d3929c09b7db40c4f9e6e645f3c97d298ebf`.

Candidate:
`entities/koder/outbox/public-info-portal-static-build-r01/`
commit `224fbb3ba5331e89d335b368bcb87c6705265b00`
tree `ba19e4b9edbcbdf0d1155fdc47654917c0c8f77f`.

KOD report:
commit `caa7ab2b2c418d2e3a7a2186ce86d438eddaf5be`
source verdict `PASS_PORTAL_STATIC_BUILD_R01_READY_FOR_INDEPENDENT_VERIFY`.

## Independent checks that PASS

- exact candidate checkout commit/tree: PASS;
- package files: 58;
- static site files: 31;
- rendered HTML routes/pages: 28;
- exact WEB assembly inputs independently matched:
  - route-map blob `94c79cb035387986e8147a6ea52d41b3e7e30be5`;
  - eligibility-ledger blob `c8dbac045b51cf2f5315b0b29ae74f5eea393246`;
- exact WEB presentation inputs independently matched:
  - route-presentation-delta blob `47648448fa632f45e79fb4a7d5b0a1028bc6d774`;
  - presentation-spec blob `7ab2d9555b57499ee457ce2abc1142586020742b`;
- RED review commit `8484b16dbb6d46833af4096f8f9b5f8e442aec1a` read back with verdict `PASS_RED_PUBLIC_INFO_PORTAL_EDITORIAL_REVIEW_R01`;
- all 20 eligibility-ledger source locators were independently checked against exact repo/commit/path/blob: 20/20 matched;
- two clean rebuilds from candidate inputs returned 28 routes and identical tree digest:
  `4a344eed5b0a3fe01760dfb4b2c797c818e3bc85e4ff1210bfe19f62e6ab0f25`;
- exact KOD test suite: 9/9 PASS;
- `artifact-hashes.json`: 57 records, exact coverage of every package file except the hash inventory itself; byte length and SHA-256 correspondence PASS;
- `site/build-manifest.json`: 30 records, exact coverage of every site artifact except the manifest itself; byte length and SHA-256 correspondence PASS;
- static output extensions only: HTML/CSS/JSON;
- DB/state-store artifact scan: none;
- preview banner present on all 28 HTML pages;
- exact three presentation empty-state phrases found for cooperation/publications/withdrawn;
- HQ operational projection check: metadata-only boundary PASS on tested HQ detail page;
- source identity mismatch test: direct mutation of copied route-map caused `SOURCE_IDENTITY_MISMATCH:route-map.json` and exit 1;
- source `public_ready` remains false in ledger/build-manifest/routes;
- no network/deployment/publication primitives found in builder/test code; SHD performed no Pages/DNS/HTTPS/credential/publication mutation.

## Critical presentation defect

Exact presentation inputs require the external layer to explain first in human Russian language, while machine metadata remains secondary/collapsible.

The immutable candidate violates that boundary on detail pages.

Independent render inspection found 14 of 28 HTML pages whose primary `<title>` and `<h1>` contain no Russian human-readable label and instead expose internal machine/source ids as the first page identity.

Examples:
- `/achievements/information-entry-r2-reverification/`:
  `achievement info entry r2 shd reverify`;
- `/developments/entity-ai-resource-boosters/`:
  `entity ai resource boosters`;
- `/developments/public-information-portal/`:
  `public info portal current`;
- `/status/gates/telegram-phase1b-host-runtime/`:
  `telegram phase1b host runtime gate`;
- `/history/information-entry/static-preview-v01/`:
  `historical static preview v01 review`.

On the achievement example the page renders machine id in both `<h1>` and `<h2>` before the Russian semantic sentence. Exact commit/blob/status provenance is correctly placed in a collapsible block, but the machine id itself is still promoted to primary page labeling.

This conflicts with:
- presentation-spec rule: external layer first explains in human Russian language;
- RED boundary: machine identifiers/statuses must not be the primary visible reading;
- exact SHD task requirement: Russian human-readable primary labels, machine provenance secondary.

## Additional presentation gap

The exact SHD task also requires visible draft/candidate/stale labels.

Independent scan found:
- `Черновик`: present;
- `Актуальность не подтверждена`: present;
- `Кандидат`: absent from all rendered HTML pages.

The pinned eligibility ledger contains multiple entries with `semantic_bucket=candidate` / `representation_state=preview_candidate`, so the candidate state is not visibly represented by the required Russian candidate label.

KOD test `test_candidate_stale_labels` checks only `Черновик` and `Актуальность не подтверждена`; it does not assert `Кандидат`.

## Terminal verdict

`FAIL_SHD_PORTAL_STATIC_BUILD_R01_PRESENTATION_BOUNDARY`

The failure is bounded to presentation semantics. Deterministic build, source identity, hashes, manifests, static-only/no-DB boundary and fail-closed input identity all passed.

Smallest correction:
1. replace internal id-derived primary titles/headings on affected detail routes with approved Russian human-readable labels/copy while preserving exact ids only as secondary provenance;
2. visibly mark candidate-state entries with `Кандидат` where the ledger marks the object as candidate/preview_candidate;
3. add negative/coverage tests proving no internal id becomes the primary page label and proving candidate badge visibility;
4. keep all source statuses, public_ready values, immutable inputs and deployment boundary unchanged.

No candidate bytes were modified by SHD. Nothing was published externally.
