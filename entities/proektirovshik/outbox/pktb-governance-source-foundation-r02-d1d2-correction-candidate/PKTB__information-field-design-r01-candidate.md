# ПКТБ Information Field Design r0.1 candidate

status: CANDIDATE_ONLY_NOT_ACTIVE
project_time: omitted

Compatible with inherited global File Work / Recovery / Task Conveyor canons; no shadow copies.

## Minimal target layout
- current/profile layer: active PKTB local profiles and Entity current-state only after exact activation/writer gates.
- task inputs: exact addressed tasks/authority/immutable dependencies, preferably by locator rather than copies.
- internal results/outbox: bounded specialist results and PRO integrated results.
- engineering artifacts: standalone calculation/CAD/drawing/BOM/test/diagnostic/prototype/manufacturing-preparation packages only when practically needed.
- source/evidence references: provenance links/identities; task-specific sources are referenced, not promoted.
- migration/linkage index: links existing PRO/HQ artifacts preserving original provenance/status; no reconstruction.
- recovery dependency: Entity continuity stays under global recovery canon/external recovery contour.
- operational shard linkage: only after common mechanism is admitted/authorized; no local fallback.

## Information semantics
Significant completed engineering result must be immutable-published and exact-readback. Chat-only finished result is insufficient.
created != published != readback != dispatched != received != accepted.

Do not create registries/manifests/route notes merely for form. Manifest only for packages where composition/integrity must be verified.

## Working-flow boundary
Until operational shard admission exists, this design does not claim continuous shard capture. Missing shard runtime is explicit UNKNOWN/NOT_ESTABLISHED, not silently replaced by chat memory or an invented local journal.
