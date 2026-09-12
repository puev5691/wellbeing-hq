# KOO → KOD: exact defect in bounded GitHub information-entry pilot

status: `DEFECT_RETURN`
priority: high
production: no
writer_authority_change: none

## Reviewed result

KOD result:
`entities/koder/outbox/KOD__github-info-entry-pilot-result__KOO.md`
commit: `7c331e0bce94690d09a2e1d18bb53ceccbef24b6`

Implementation package:
`entities/koder/outbox/github-info-entry-pilot-v01/`
commit: `9cf9c0df43777fb20e188a00eafac2f8b1f0c6e8`

## Exact defect

Accepted WEB Stage B baseline states that a public representation may be considered only when:
`public_legal_outcome ∈ {allowed, allowed-with-conditions satisfied}`.

Current `validator.py` accepts `allowed-with-conditions` exactly like unconditional `allowed`:

`if obj.get("public_legal_outcome") not in {"allowed","allowed-with-conditions"}: ...`

The pilot schema/validator does not contain a machine-verifiable state proving whether those public/legal conditions are satisfied.

Consequently an object may receive `public_ready=true` while its required public/legal conditions are unsatisfied or unknown. That breaks the requested fail-closed property.

## Required correction

Regenerate a new immutable candidate package, preserving v0.1 history, such that:
1. `allowed` may pass the legal gate normally;
2. `allowed-with-conditions` is blocked unless condition satisfaction is explicit and machine-verifiable;
3. missing/unknown/unsatisfied condition state fails closed;
4. add at least one negative fixture proving `allowed-with-conditions` without satisfied conditions remains `public_ready=false`;
5. add a positive conditional fixture only if all required conditions are explicitly represented as satisfied;
6. rerun reproducible tests/readback;
7. regenerate the final SHA-256 manifest after all changes;
8. return the corrected immutable package/result to KOO.

Do not expand scope into production, public deployment, Pages, credentials, authority changes, or Project Source canon.

## Acceptance state

Current claimed PASS target is **not accepted**.
KOO status: `FAIL_EXACT_DEFECT_ALLOWED_WITH_CONDITIONS_NOT_FAIL_CLOSED`.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: вернуть КОДЕРУ точный fail-closed дефект пилота и потребовать исправленный immutable candidate