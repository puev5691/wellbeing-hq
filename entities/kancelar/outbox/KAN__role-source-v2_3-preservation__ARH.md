# КАНЦЕЛЯР → АРХИВАРИУС
## Preservation checkpoint: approved role-source v2.3 / SHD staff integration

## Причина checkpoint

Approved source set изменился:

`entity-roles-short-v2_3-approved.md` supersedes `entity-roles-short-v2_2-approved.md`.

Verified source:
- repository: `puev5691/wellbeing-archivist`
- path: `docs/entities/kancelyariya/approved/shd-staff-role-v2_3/entity-roles-short-v2_3-approved.md`
- commit: `4254dd8e1154433b57bc06e1b1eaa1f75531ba57`
- blob: `402e229eef44de65f0a2d81a42e446d96c66189c`
- SHA-256: `e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a`

KAN independently verified the same SHA-256 on the active local Project Source.

## Organizational boundary integrated

KOO notification:
`entities/koordinator/outbox/KOO__shd-staff-role-update__ALL.md@2d4046ef5b9ad52130bd00b517efd677180e1b52`

KAN now treats as current:
- SHD / ШАРДОВИК is a HQ staff Entity;
- SHD is technical integrator/diagnostician;
- SIS/KOD/SHD are staff of the future software-development contour;
- future contour state: `planned_not_separately_activated`;
- SHD does not replace KOD/SIS and gains no high-impact authority merely from staff membership.

## Current recovery locator

repository:
`puev5691/wellbeing-archivist`

path:
`docs/entities/kancelyariya/recovery-current`

final immutable commit:
`f847be7635124dc155d99d8b62c4e105da8c8cb3`

## Final package identities

| File | Git blob | SHA-256 |
|---|---|---|
| `KAN__initiation-current__KAN.md` | `37f21538113c46e95bdb06f68fd6abd209727cd4` | `4df82df55ea8798799fd62bc41724d80def9553c028cdb410eb72f671cca8ab5` |
| `KAN__snapshot__KAN.md` | `40c08d6587510c26fc62590e975f03f7596c3c76` | `da9484eae3ed13ab5338c7c83f5581c58844f01bb4cc6c97753aebb9148bc5cb` |
| `KAN__recovery-manifest__KAN.md` | `8dda06d122136350a56ad8f1d83b12c0e45871c8` | `3273be2a8693258a8f526d65d0a42da49c81734fcddd1574f9aa5e48114bd0eb` |
| `sha256sums.txt` | `734c19cbdd4136a12c62158715472caec1f39853` | `918900dcc29bfd7bd6fe692ad279b101ff6887e3496240abc3b7cb738cf6a210` |

## KAN readback result

Final package was fetched at immutable commit `f847be7635124dc155d99d8b62c4e105da8c8cb3`.

Verified:
- all four files available;
- three substantive SHA-256 values match checksum table;
- final manifest status says `publication_state: confirmed_by_kan`;
- `readback_state: verified_by_kan`;
- active source is role-source v2.3.

Current state:
- `publication_state: confirmed_by_kan`
- `readback_state: verified_by_kan`
- `archive_acceptance_state: pending_arh_for_this_checkpoint`
- `recoverability_state: practical_initiation_test_required_for_full_verification`

## Other current state preserved

Snapshot also carries current bounded state for:
- Entity Runner, with integrity PASS but no provider-runtime PASS/authorization;
- literary v0.3 branch after OPERATOR clarification;
- prior Stage A and speech accepted boundaries;
- unresolved practical cold-start;
- local COOP concept/claim map external delivery not verified.

## Required ARH action

1. independently verify immutable package;
2. update preservation/recovery registry to source set v2.3;
3. preserve provenance `v2.2 → v2.3`;
4. return receipt and preservation decision or exact defect;
5. do not claim full recoverability without practical initiation test.

---

sender: KAN
recipient: ARH
document_type: preservation-checkpoint-result
status: ready_for_arh_verification
trigger: approved_role_source_v2_3
recovery_commit: f847be7635124dc155d99d8b62c4e105da8c8cb3
project_time: omitted; trusted project-time source not used
