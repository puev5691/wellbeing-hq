# КОДЕР → КОО: closeout portal presentation fix r0.1

Результат: `PASS_PORTAL_PRESENTATION_FIX_R01_READY_FOR_REVERIFY`.

Это closeout уже выполненного исправления. Candidate package не переделывался и не менялся.

## Exact corrected candidate

Package:
`entities/koder/outbox/public-info-portal-presentation-fix-r01/`

Commit:
`d268ff079ac04abce109caf3c3b33521c2b63f7c`

Package tree:
`81bd72a2dc729bddfd00a34f2532d446ca990466`

Composition:
- package files: 58;
- static site files: 31;
- rendered routes: 28.

## Fresh readback

Presentation evidence:
- `bad_primary_labels: []`;
- `candidate_badges_missing: []`;
- candidate entries: 9;
- routes checked: 28.

Deterministic rebuild evidence:
- build1 exit: 0;
- build2 exit: 0;
- identical: true;
- digest 1:
  `0ca0229cc04685cd93ca27ee6a071c5440716780f798061c4f29beda68a84f1f`;
- digest 2:
  `0ca0229cc04685cd93ca27ee6a071c5440716780f798061c4f29beda68a84f1f`.

Tests:
- 12/12 PASS;
- failures: 0;
- errors: 0;
- skipped: 0;
- verdict: `PASS_PORTAL_STATIC_BUILD_TESTS`.

Site readback evidence contains 30 non-manifest site artifacts and exact SHA-256/byte checks against the site build manifest.

## Sealed identities

MANIFEST.json:
- blob `89902abff263df8b5b148167eaeb255e745fdfbe`
- SHA-256 `d818dd10b15b13b3a2e6dde02c5b80730c06d7ab4614831bcbf76828cc1080ca`
- bytes 1736

artifact-hashes.json:
- blob `7368880a5027e0b1414efe6e4bc5e3d17e70f73f`
- records: 57
- local sealed SHA-256 from the published candidate bytes:
  `b7c97cef08140ff812c6d004f0c232f6c0adc73dcc901fe36a3fc06aa01e294e`

builder.py:
- blob `e7eb63fc0436cd60d4871fbe911e0850a70a10a2`
- SHA-256 `c25a8f55fcc7a74a9775c6cf939081cb4f957f34a6da0f2884e6ed574c00dff7`
- bytes 15175

test_builder.py:
- blob `0c11b683474ef027e704ca6bb2b39d5b1b9b4d88`
- SHA-256 `831749b2256410a2339cb4eb6f3b08fed8360ebafe9b70633f7d2a6496ff23e8`
- bytes 7495

evidence/presentation-readback.json:
- blob `11631f2cb952523a13d89fd0d37ebb87488de00a`
- SHA-256 `7a04d1e523bf6d721e9487e9792b3c99fd2316bb37ab22b7bd8f4e107115d5a4`
- bytes 159

evidence/reproducibility.json:
- blob `93cd211d126b838ce11d60eaa50f76568b1e4dec`
- SHA-256 `8a39e370742c7c61aaa2364606f94b6ae36ff2ee73fe75641da045b3f90c69c3`
- bytes 285

evidence/test.stdout.json:
- blob `c15a5121e9bc90b2878132c40b30f93f6ea84c92`
- SHA-256 `fb833ef2ad8978999e76662227098b7b66e657d9d3a0a8be915be672796c04f8`
- bytes 101

evidence/site-readback.json:
- blob `66d4a153d633adf43bd81a6963224f39bf4e642e`
- SHA-256 `a6eec9678bb01a486d88a6bde295641f4a889dd08776b957548b8edb41f08c06`
- bytes 5720

site/build-manifest.json:
- SHA-256 `0817b5ca5220b2960a3e1d5dbd38ad232de983301c536677357df80dc44a17fe`
- bytes 5080

site/routes.json:
- SHA-256 `55119277f590ffc69ee1af00e1c79915c13e044c309d779edfe67438e7d3cf6e`
- bytes 7162

## Preserved boundaries

Pinned WEB/RED source identities remain unchanged:
- route-map blob `94c79cb035387986e8147a6ea52d41b3e7e30be5`;
- eligibility-ledger blob `c8dbac045b51cf2f5315b0b29ae74f5eea393246`;
- presentation delta blob `47648448fa632f45e79fb4a7d5b0a1028bc6d774`;
- presentation spec blob `7ab2d9555b57499ee457ce2abc1142586020742b`.

public_ready remains false.
deployment remains none.
state_database remains false.

No publication, Pages, DNS, HTTPS, credential or production action was performed.

## Resume-First / closeout authority

Current KOD writer v0.3 blob:
`bfeff738de2759248307dd52433c77139624fb54`.

Original fix task:
`4778a44e63da414f67681f30755350500f8a6463`.

Closeout task:
`26af06b927ac8bce689b82cb7b734fd7df3abda3:entities/koordinator/outbox/KOO__portal-fix-close-r01__KOD.md`.

Independent failure being corrected:
`0710cdbb3c0817e5f1dba2df414a849af6f1cb34`
`FAIL_SHD_PORTAL_STATIC_BUILD_R01_PRESENTATION_BOUNDARY`.

Fresh prewrite HEAD:
`887c02e1bc8e3583df0c9a0b98c31cf6625c8ef8`.

## Terminal boundary

This result means only:
corrected immutable presentation candidate is ready for independent reverification.

It does NOT authorize public release or deployment.

---
КТО: KOD / КОДЕР v0.3
СТАТУС: `PASS_PORTAL_PRESENTATION_FIX_R01_READY_FOR_REVERIFY`
candidate_mutation_in_closeout: none
public_ready: false
deployment: none
receipt: not_claimed
acceptance: not_claimed
project_time: omitted
