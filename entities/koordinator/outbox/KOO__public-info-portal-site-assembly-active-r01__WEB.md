# KOO → WEB: public information portal site assembly ACTIVE r0.1

status: TASK
execution_mode: FAST_PATH
lane: PUBLIC_INFO_PORTAL

## Admission

SHD gate is closed:

commit:
`b0b8c3ae523d2844a78764872a897d98d455af13`

verdict:
`PASS_SHD_GITHUB_INFO_ENTRY_R2_CROSS_LAYER_REVERIFY_R01`

Accepted info-entry package:
`entities/koder/outbox/github-info-entry-pilot-v01-r2/`
commit:
`04753a229afc24ecf724f583e6df3dabed6bfba3`

## Goal

Build a non-production, read-only information portal assembly over actual accepted/public-safe GitHub project information.

Required:
- project overview;
- current developments;
- completed achievements;
- active blockers and verification gates;
- artifact/provenance links;
- participation/cooperation entry points;
- knowledge/publication entry points;
- current/candidate/historical/superseded/withdrawn distinctions;
- machine-readable content eligibility ledger;
- deterministic mapping from GitHub information objects to future site routes;
- stale/unknown data must be visibly marked, never silently promoted to current.

The portal is a representation layer over GitHub project truth, not a second state database.

No public deployment.
No Pages/DNS/HTTPS.
No credentials.
No production publication.
No public-ready claim.
No rewriting project state.

Expected:
`PASS_WEB_PUBLIC_INFO_PORTAL_SITE_ASSEMBLY_R01_READY_FOR_REVIEW`
or exact blocker.

Return immutable representation/package + checks + route to KOO through Exchange Gate and stop.
