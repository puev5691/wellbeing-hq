# KOO → KOD: portal presentation boundary fix r0.1

status: TASK
execution_mode: FAST_PATH
lane: PUBLIC_INFO_PORTAL

## Independent failure

SHD result:
`0710cdbb3c0817e5f1dba2df414a849af6f1cb34`

verdict:
`FAIL_SHD_PORTAL_STATIC_BUILD_R01_PRESENTATION_BOUNDARY`

## Important

All of these independently passed:
- exact candidate commit/tree;
- deterministic rebuild;
- source identity;
- hashes/manifests;
- static-only/no-DB boundary;
- fail-closed source mismatch;
- preview banner;
- empty states;
- HQ metadata-only boundary;
- no public_ready promotion.

Do NOT redesign the build.

## Exact defects

1. On 14/28 rendered HTML pages, primary title/h1 exposes internal id-derived English/machine labels instead of Russian human-readable primary labels.

Examples:
- achievement info entry r2 shd reverify
- entity ai resource boosters
- public info portal current
- telegram phase1b host runtime gate
- historical static preview v01 review

2. Visible Russian candidate marker is missing:
`Кандидат`

while ledger contains candidate / preview_candidate entries.

## Required correction

1. Replace internal id-derived primary page titles/headings on affected detail routes with approved Russian human-readable labels/copy.
2. Preserve exact internal ids only as secondary/collapsible provenance.
3. Add visible `Кандидат` marker for candidate/preview_candidate entries.
4. Add tests:
   - no internal id may become primary page label;
   - every candidate/preview_candidate object must visibly render candidate badge.
5. Keep all source statuses/public_ready values unchanged.
6. Keep all pinned WEB/RED inputs unchanged.
7. Keep deterministic build/rebuild/readback behavior intact.
8. Return a new immutable corrected static-build candidate.

Do not:
- publish externally;
- enable Pages;
- change DNS/HTTPS;
- use credentials;
- invent new project facts;
- alter accepted WEB/RED source bytes.

Expected:
`PASS_PORTAL_PRESENTATION_FIX_R01_READY_FOR_REVERIFY`
or exact blocker/fail.

Return corrected immutable build package + tests/readback to KOO through Exchange Gate and stop.
