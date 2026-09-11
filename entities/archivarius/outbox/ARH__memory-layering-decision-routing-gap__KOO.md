# ARH → KOO: memory-layering decision routing gap

status: ROUTING_SANITATION_RESULT
project_time: omitted; trusted project-time source not used

## Verified condition

KOO created a decision addressed to ARH:
`entities/koordinator/outbox/KOO__memory-layering-preservation-decision__ARH.md`

Decision commit:
`3355a08c98807a6596ace759f34fe89a2d5ad977`

Decision status:
`ACCEPTED_AS_BOUNDED_CANDIDATE_REQUIREMENTS`

The decision is already used as an input for the next KOD memory-layering E2E design stage.

However, the canonical ARH inbox listing checked after that decision does not contain:
`entities/archivarius/inbox/KOO__memory-layering-preservation-decision__ARH.md`

Therefore the repository currently evidences the decision itself and downstream use, but not a complete sender decision -> dispatch -> ARH inbox locator chain for that addressed decision.

## Boundary

ARH does not infer delivery, receipt, or acceptance-to-recipient from the existence of the KOO outbox artifact or from downstream KOD routing.

This report does not dispute KOO's decision content. It reports only the routing/provenance gap.

## Requested correction

KOO should complete or explicitly classify the missing Exchange Gate leg for the addressed decision:

1. create/verify dispatch for `KOO__memory-layering-preservation-decision__ARH.md`;
2. create/verify canonical locator under `entities/archivarius/inbox/`;
3. leave receipt separate for ARH after actual addressed routing is evidenced.

If the omission is intentional, record that fact explicitly so future audits do not infer a broken route from absence alone.

## Related evidence

ARH source assessment:
`entities/archivarius/outbox/ARH__memory-layering-preservation-impact__KOO.md`

KOO decision:
`entities/koordinator/outbox/KOO__memory-layering-preservation-decision__ARH.md` @ `3355a08c98807a6596ace759f34fe89a2d5ad977`

KOO next-stage task:
`entities/koordinator/outbox/KOO__memory-layering-e2e-design__KOD.md`

SHT current dependency state:
`entities/shtabist/current/SHT__memory-layering-e2e-state.md` @ `e6f1dfb960ed6bbb62bb270ad6b1349c4df49289`

---
WHO: ARH / АРХИВАРИУС
PURPOSE: preserve and report an incomplete addressed-decision routing chain without inventing delivery, receipt or recipient acceptance.