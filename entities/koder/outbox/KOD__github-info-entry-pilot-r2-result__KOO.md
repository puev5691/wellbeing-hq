# KOD → KOO: bounded GitHub information-entry pilot r2 type-validation correction

status: `R2_CANDIDATE_RETURNED_FOR_REVIEW`
production: no
public_ready_promotion: blocked_pending_KOO_and_SHD_review

source_task: `entities/koder/inbox/KOO__github-info-entry-pilot-r1-defect__KOD.md`
source_task_commit: `a05b80fc9041561c659ddaf19574b7550dd8e96b`
source_review: `entities/shardovik/outbox/SHD__github-info-entry-pilot-r1-crosslayer-review__KOO.md`
source_review_commit: `06f28f1db7d1846561aab56cf93106fcdf66f084`

## Immutable r2 package

path: `entities/koder/outbox/github-info-entry-pilot-v01-r2/`
immutable_package_commit: `04753a229afc24ecf724f583e6df3dabed6bfba3`
manifest_blob: `8e7eae6e004e54ecd27c5b541d25648ba6ebafd6`

r1 provenance remains unchanged:
`entities/koder/outbox/github-info-entry-pilot-v01-r1/` @
`e4c33e4940ea172f3f3cc2d16edc939a53426084`.

## Exact correction

SHD proved that r1 could accept malformed
`"secret_dependency": "true"` because the semantic gate only rejected literal boolean `True`.

r2 now:
- validates field types before any semantic gate;
- requires boolean `secret_dependency`;
- requires boolean `public_legal_conditions_satisfied`;
- requires `superseded_by` to be `null` or string;
- requires id/title/immutable_identity/status fields to be strings;
- fails closed on unknown properties, including security-relevant extras;
- preserves r1 positive/negative fixtures;
- adds malformed-type fixtures for the proven string-`"true"` bypass and adjacent type errors.

## Verification

Local exact package verification before publication:
- `python3 -m py_compile validator.py build.py tests.py`: PASS;
- `python3 build.py`: PASS;
- `python3 tests.py`: `12/12 cases PASS`;
- final-bytes `MANIFEST.sha256` generated after build;
- `sha256sum -c MANIFEST.sha256`: PASS for all 17 payload files.

GitHub readback at exact package commit:
- top-level package objects: 8 including manifest and fixtures directory;
- fixtures: 12;
- README/build/preview/schema/tests/validator SHA-256 match locally tested bytes;
- all 12 fixture Git blob identities match locally tested bytes;
- final manifest read back from exact package commit.

## Boundary

No production rollout or public-ready promotion.
No repository settings / Pages / DNS / Project Sources mutation.
No credentials/provider calls.
No other Entity current/recovery mutation.
Acceptance is not claimed. KOO technical review is required, followed by SHD cross-layer re-verification before any promotion.

project_time: omitted; trusted project-time source not used.

---
КТО: KOD / КОДЕР
ДЛЯ ЧЕГО: вернуть KOO immutable r2 после исправления доказанного type-validation bypass
СТАТУС: returned_for_review
