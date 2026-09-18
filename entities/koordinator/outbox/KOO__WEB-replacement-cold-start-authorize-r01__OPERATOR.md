# KOO → OPERATOR: WEB replacement cold-start authorization r0.1

status: READY_FOR_OPERATOR_ACTIVATION
entity: WEB / ВЕБМАСТЕР

## Recovery gate

ARH result:
`e1be53b46ffd298c2b2f30fbeb5ff3e174b860b0`

verdict:
`PASS_ARH_WEB_RECOVERY_PACKAGE_READY_FOR_REPLACEMENT_INITIATION_R01`

Exact external locator:
`puev5691/wellbeing-entity-bootstrap@70fa5df171903e5ec914cfd93b0cf60ec79c7664:entities/web/preservation/pending/emergency-replacement-r01`

Readback:
`4/4 PASS`

Exact blobs:
- writer failure state: `d07c6945776c91890206bce1f7fa17ee7bfdbbeb`
- evidence snapshot: `721ef4c1d0d2fbe434ee67763e1eab31c5817b94`
- replacement initiation: `d8c057acae849399d9932091bdca8bdb06a8cb61`
- manifest: `4e37a73f61fad4292d54dc607ff14a9c19168188`

## Cold-start rule

A new WEB chat may now initiate only from the exact external locator above and current approved project/recovery/file canons.

The old WEB instance remains frozen.

Presentation r0.2 remains:
`PENDING_OR_UNKNOWN_NO_VERIFIED_TERMINAL_RESULT`

Task:
`37f051ac7fc01ecb0a96b8d15891aa549e22764e`

No replacement instance may claim r0.2 completion without verified GitHub terminal evidence.

## Required replacement sequence

1. read exact external recovery package;
2. verify commit/path/composition/blobs;
3. load current mandatory project sources;
4. perform cold-start checks;
5. publish initiation report;
6. only after `initiation_verified`, perform separate writer-gate/failover;
7. reconcile portal r0.2 state;
8. if no terminal result exists, resume exact r0.2 task from preserved boundary.

This authorization does not itself transfer current-writer.
