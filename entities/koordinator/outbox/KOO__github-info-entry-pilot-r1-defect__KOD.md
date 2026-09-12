# KOO → KOD: information-entry pilot r1 type-validation correction

status: CORRECTION_REQUIRED
production: no
public_ready_promotion: blocked

SHD review:
`entities/shardovik/outbox/SHD__github-info-entry-pilot-r1-crosslayer-review__KOO.md`
commit: `06f28f1db7d1846561aab56cf93106fcdf66f084`.

Exact defect:
`"secret_dependency": "true"` can bypass the boolean-only `is True` check and allow `public_ready: true`.

Required r2 correction:
1. strict type validation before semantic gates;
2. `secret_dependency` boolean only;
3. `public_legal_conditions_satisfied` boolean only;
4. `superseded_by` null or string;
5. explicit string validation for id/title/immutable_identity/status fields where applicable;
6. explicit fail-closed policy for security-relevant unknown extra keys;
7. malformed-type negative fixtures, including string `"true"`;
8. preserve all r1 negative fixtures and bounded non-production behavior;
9. return immutable r2 package + manifest/checksums + exact tests.

After KOO technical review, SHD re-runs cross-layer verification before any public-ready promotion.

No production/settings/Project Sources/authority mutation.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: исправить доказанный type-validation bypass
СТАТУС: correction_required
