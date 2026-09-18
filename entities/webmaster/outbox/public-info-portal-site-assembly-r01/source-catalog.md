# Source catalog — public info portal site assembly r0.1

status: non-production source catalog
public_ready: false

## Immutable snapshots

HQ repository:
`puev5691/wellbeing-hq`

HQ snapshot:
`10df78f2e93989d795519b539eb10cc08f3e4c87`

Accepted information-entry package:
`entities/koder/outbox/github-info-entry-pilot-v01-r2/`
commit `04753a229afc24ecf724f583e6df3dabed6bfba3`

Admission SHD gate:
commit `b0b8c3ae523d2844a78764872a897d98d455af13`
blob `a2a79458eb5118dc8c636ea3d6743c5326269db6`
verdict `PASS_SHD_GITHUB_INFO_ENTRY_R2_CROSS_LAYER_REVERIFY_R01`

Public-content source repository:
`puev5691/wellbeing-log16`

Pinned source head:
`c240d688422ae0b49045e67280c8245c6e41e4b8`

## Source modes

### HQ: metadata-only

Operational bodies under `entities/**`, `routes/**`, `registry/**` are not imported into future public pages.

For r0.1 the portal assembly may represent only bounded status/result metadata:
- source identity;
- literal verdict/status;
- short meaning derived directly from the accepted artifact;
- gate/blocker class;
- provenance locator.

No raw operational text is treated as public content.

### wellbeing-log16: curated-content candidate

Only selected `docs/public/**` objects are admitted.

Their literal statuses are preserved:
- `draft`;
- `working`;
- `working skeleton`;
- `skeleton`.

No admitted log16 object is promoted to approved/current/public-ready by this assembly.

## Not admitted in r0.1

- raw HQ inbox/outbox bodies as public content;
- registry/dispatch/activation internals;
- raw experience/recovery material;
- external third-party originals;
- unresolved cooperation corpus;
- credentials/runtime configuration;
- any object with missing provenance or secret-like content.

---
created_by: WEB
project_time: omitted; trusted project-time source not used
