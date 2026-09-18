# Future KOD handoff — public info portal assembly r0.1

status: implementation contract candidate
implementation_authority: not_granted_by_this_file
public_deployment_authority: none

## Input

- `portal-assembly.md`
- `content-eligibility-ledger.json`
- `route-map.json`
- `source-catalog.md`

## Required future behavior

1. read pinned source identities;
2. validate ledger schema;
3. reject duplicate routes/source ids;
4. fail closed when source identity is missing/mismatched;
5. never ingest raw HQ operational bodies into public output;
6. render HQ items as metadata projections only;
7. preserve literal draft/working/skeleton labels from log16;
8. render blocked/unknown routes as explicit placeholders;
9. keep historical/superseded outside current navigation;
10. never derive public-ready from repository visibility;
11. produce deterministic static local preview;
12. produce post-build readback bound to exact artifact identity.

## No independent state database

Implementation may cache build inputs, but must not create a portal-owned authoritative status database.

Source truth remains GitHub source objects and their accepted decisions.

## Expected evidence if KOD is later tasked

- immutable implementation package;
- schema/validator;
- deterministic build;
- route-by-route readback;
- forbidden-source checks;
- provenance links;
- no-network/no-deployment statement;
- exact preview identity.

---
created_by: WEB
project_time: omitted; trusted project-time source not used
