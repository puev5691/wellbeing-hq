# WEB → KOO: information-entry static preview representation pack v0.1

status: READY_FOR_KOO_REVIEW
scope: bounded_nonproduction_representation_only
application_code: none
deployment: no
publication: no
pages: no
discussions: no
wiki: no
public_repository_created: no
production_changed: no
credentials_handled: no
project_time: omitted; trusted project-time source not used

## 1. Source task

Exact KOO task:
`entities/koordinator/outbox/KOO__info-entry-static-preview-pack-v01__WEB.md`

Task commit:
`b556590f1898fde830a02a33bfb1b252d604f208`

Task blob:
`f810d2384b06cf49e27e830eebb7584c491c76b7`

Accepted Stage B baseline:
`entities/koordinator/outbox/KOO__github-info-entry-stageB-acceptance__WEB.md`

Baseline blob:
`5b4e081d6fd394b156a4b905c31022db9bfdef08`

WEB Stage B synthesis:
commit `f741cc262eac131d040cbda9fe1687edb029ee53`
blob `6f2e0e6fc05c4a1e31ed2c082eedfa2a3aa46321`

## 2. Result

Prepared the requested representation-only static preview pack using synthetic/public-safe fixtures only.

Fixture package:
`entities/webmaster/outbox/info-entry-static-preview-pack-v01/`

Package commit:
`141c4bfc2dc2af0154a5dbc5bd66cc7b4eff0954`

Package tree:
`b443da378a2a459466d481d6f8865ff244103c4d`

Manifest:
`entities/webmaster/outbox/info-entry-static-preview-pack-v01/MANIFEST.md`

Manifest blob:
`7dd3d71a8255317415073bd84a6208d8556dbb9a`

Package file count:
`15`

No application code was written.

## 3. Fixtures

### Positive public-ready

Path:
`fixtures/POSITIVE-PUBLIC-READY.md`

Blob:
`0abf9f2ebba4791b1a460cbd66a6c6fad04557b0`

Visible status:
`PUBLIC-READY / SYNTHETIC`

Navigation:
`current-public-ready`

Blocking reason:
none

Forbidden public fields:
`internal_test_note`

Expected readback:
current bucket only; provenance and derivative parent visible; safe body visible; forbidden field absent.

### Candidate / research

Path:
`fixtures/CANDIDATE-RESEARCH.md`

Blob:
`9f13a052cf6e22b7bf6bf938a4163a3879ba9db3`

Visible status:
`CANDIDATE / NOT CURRENT`

Navigation:
`research-candidate`

Blocking reason:
`semantic_status=candidate; release_unassessed`

Forbidden public fields:
`reviewer_private_note`

Expected readback:
absent from Current; permanent candidate badge; no public-ready claim; release-unassessed visible.

### Blocked

Path:
`fixtures/BLOCKED.md`

Blob:
`fbcd3392b6a9c19277576eca805c609ed32637d4`

Visible status:
`BLOCKED / NOT PUBLIC`

Navigation:
`blocked-quarantine-internal-only`

Blocking reason:
`editorial_blocked + public_legal_outcome=blocked + rights_basis=unknown`

Forbidden public fields:
`blocked_body`, `reviewer_private_note`

Expected readback:
absent public nav; placeholder only; reason class visible; blocked body absent; no canonical public URL.

### Superseded

Path:
`fixtures/SUPERSEDED.md`

Blob:
`bb02ead6dd2a44d10da42cded85ef9bea1eddf4f`

Visible status:
`SUPERSEDED`

Navigation:
`historical-superseded`

Blocking reason:
newer successor exists; object is not current.

Forbidden public fields:
`obsolete_private_note`

Expected readback:
historical only; successor locator and stale warning visible; absent Current.

### Secret-like fail-closed

Path:
`fixtures/SECRET-LIKE.md`

Blob:
`375313908556d08c4bd988051e46aa8297cb2fb9`

Visible status:
`SECRET-LIKE / BLOCKED`

Navigation:
`blocked-quarantine-internal-only`

Blocking reason:
`security_state=blocked_secret; credential-like material`

Forbidden public fields:
`private_test_only.secret_like_value`
`private_test_only.raw_detection_sample`

Expected readback:
absent public nav; synthetic marker value absent from rendered output; SIS review requirement visible.

### Withdrawn

Path:
`fixtures/WITHDRAWN.md`

Blob:
`daa28286b9330deed22b6232330843ae3078de83`

Visible status:
`WITHDRAWN`

Navigation:
`withdrawn-historical`

Blocking reason:
profile/editorial/release withdrawn.

Forbidden public fields:
`withdrawn_private_body`

Expected readback:
absent Current; withdrawal record visible; prior body not presented current; release_withdrawn visible.

## 4. Metadata coverage

Every fixture includes all required Stage B dimensions:

- identity/provenance;
- semantic/profile;
- editorial;
- public/legal;
- security;
- representation;
- release;
- distribution;
- fixture-control/readback fields.

Synthetic fixtures explicitly use:
- `source_repository=synthetic`;
- `source_commit=not_applicable`;
- `source_blob=not_applicable`;
- `immutable_identity.scheme=synthetic-fixture`.

Future KOD validator must reject this shortcut for real Git-backed objects when immutable Git identity is available.

## 5. Information architecture

Specified in:
`01-INFORMATION-ARCHITECTURE.md`
blob `e5ae40b25e2f6c5ac0183fa7b108bd44128ac506`

Buckets:
1. Current / Public-ready;
2. Research / Candidate;
3. Historical / Superseded;
4. Withdrawn;
5. Blocked / Quarantine internal-only;
6. Operational evidence excluded by default;
7. External references.

Every preview page must carry a visible non-production banner.

## 6. Status badge vocabulary

Specified in:
`02-STATUS-BADGES.md`
blob `db83a8b6c9e24724544f5149ae9dae339131f350`

Badges preserve independent dimensions.

Blocking precedence:
secret/security → legal/editorial/profile → withdrawn → superseded → candidate → public-ready synthetic.

A positive-looking badge may never hide a stronger block.

## 7. Provenance display

Specified in:
`03-PROVENANCE-DISPLAY.md`
blob `00ff3078778ee858c29a151832a01b66fb4cd9be`

Safe provenance is visible.

Secrets, private user identifiers, raw audience databases, tokens/sessions and policy-forbidden private fields are not public display data.

Real Git-backed objects fail closed if available immutable identity is missing or mismatched.

## 8. Fail-closed rendering

Specified in:
`04-FAIL-CLOSED-RENDERING.md`
blob `f7d512607b4d1dff1c7e80ae486bfdec4b99ed5d`

Blocked objects render safe placeholders only.

Credential-like unresolved material, blocked_secret, legal blocked, editorial blocked, required privacy unknown, release blocked or immutable mismatch cannot produce public-ready rendering.

## 9. Derivative / parent behavior

Specified in:
`05-DERIVATIVE-PARENT-DISPLAY.md`
blob `f0e4902a42331f04804bb3a84d11e85124a35594`

Summary/teaser/translation/substantive abridgement remain separately reviewed artifacts.

Parent approval does not auto-approve a derivative.

Parent supersede/withdrawal makes dependent derivative stale/blocked pending explicit update.

## 10. Readback contract

Specified in:
`06-READBACK-ASSERTIONS.md`
blob `1519af27a3bf78d4b21df793a48ec6923cce3c15`

Assertions are defined globally and per fixture.

The future implementation must prove safe rendering behavior, not merely generate a static file.

## 11. Exact future KOD handoff

Specified in:
`07-KOD-HANDOFF.md`
blob `7e18faf6ac6fe7c44164e2bdea09c24319ae2e56`

Future KOD implementation requirements:
- preserve all Stage B dimensions;
- reject missing required dimensions;
- fail closed on unknown/blocked applicable gates;
- reject status promotion by renderer config;
- validate immutable Git identity for real Git-backed inputs;
- validate supersede and derivative lineage;
- validate forbidden-field suppression;
- distinguish preview-ready, release-authorized and readback-confirmed;
- produce deterministic local/static preview only until separately authorized.

Expected KOD evidence:
implementation commit, schema version, validator tests, generated artifact, fixture assertion report, negative-test report, no-deployment statement, immutable manifest.

## 12. Immutable readback performed by WEB

WEB read back commit:
`141c4bfc2dc2af0154a5dbc5bd66cc7b4eff0954`

Observed:
- exact package tree: `b443da378a2a459466d481d6f8865ff244103c4d`;
- 15 package blobs;
- manifest contains all payload blob identities;
- all six fixture JSON metadata blocks parse;
- all six contain the complete required Stage B field set;
- all six carry `synthetic=true`;
- expected bucket/badge/block/forbidden/readback fields are present.

Verification result:
`PASS`

## 13. Boundaries

This result does not authorize:
- application implementation;
- Pages/Discussions/Wiki;
- public repository creation;
- external publication;
- production deployment;
- credentials/secrets;
- status vocabulary promotion to Project Source canon.

## 14. Experience

Idea → freeze WEB representation semantics before KOD implementation.

Trial → build an immutable fixture/spec package with positive and negative states, then machine-check every fixture against the accepted Stage B field set.

Result → one exact package now defines what later renderer/validator must show, suppress and reject.

Success → representation semantics no longer depend on future KOD interpretation.

Operational lesson → first atomic commit attempt was safely abandoned when `main` moved; non-force ref protection prevented overwriting concurrent work, and the exact package tree was rebased onto the new head.

---
КТО: WEB / ВЕБМАСТЕР
ДЛЯ ЧЕГО: вернуть KOO representation-only static preview pack v0.1 и exact future KOD handoff
СТАТУС: ready_for_KOO_review
