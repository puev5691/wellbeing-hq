# Exact Handoff to Future KOD Implementation

No code is authorized by this pack itself.

## Input schema

KOD must preserve every metadata field present in fixtures across identity/provenance, semantic/profile, editorial, public/legal, security, representation, release, distribution and fixture-control dimensions.

## Validator

- reject missing required dimensions;
- fail closed on blocked/unknown applicable gates;
- reject status promotion by renderer config;
- require real Git immutable identity when available;
- allow Git `not_applicable` only for synthetic or justified non-Git input;
- validate supersede lineage;
- validate derivative parent identity;
- validate forbidden-field suppression;
- distinguish preview-ready, release-authorized and readback-confirmed.

## Static preview

Deterministic local/static artifact; no network dependency needed; no deployment; visible non-production banner; separate buckets; internal-only blocked/quarantine view; forbidden fields absent from public-safe output.

## KOD evidence expected later

implementation commit; schema version; validator test report; generated static artifact; fixture-by-fixture assertion report; negative-test failures; no-deployment statement; immutable manifest/checksums.

PASS requires all assertions in `06-READBACK-ASSERTIONS.md` and fixture-local assertions. Producing HTML alone is not PASS.

---
created_by: WEB
purpose: exact future implementation handoff
project_time: omitted; trusted project-time source not used
