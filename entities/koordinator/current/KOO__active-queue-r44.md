# KOO current active queue r0.44

status: CURRENT_QUEUE
writer: `entities/koordinator/current/KOO__replacement-current-writer-v06.md`
writer_commit: `525e5b131472e61b1f55db5ef7307217aea4c4fc`
writer_gate_pass: `06dd7873b532c1fe86f4b382d40c26908a5a11b2`
project_time: omitted; trusted project-time source not used

## Source rebuild r0.3 state

Previous queue:
`entities/koordinator/current/KOO__active-queue-r43.md`
commit `7d80feb3c7c8f80c5848e86ddd8f1b0063d2cab4`.

OPERATOR locator-first decision is integrated into candidate r0.3.

Integration result:
`entities/koordinator/outbox/KOO__source-rebuild-r03-integration-result__KOO.md`
commit `5488c79e626f9ab4085a14b864e4a5ed7e536eaf`
blob `a6269282611bd382e2977cd21174ee1f2d4204a8`.

Exact local package:
`project-sources-conveyor-v1-r03-candidate.zip`
SHA-256 `2c0327f8fdeb5a1f47da2bf9cdb74892b19ebf1e2edfd0c899dd3af043003b4c`
composition 7 files;
local readback 7/7 PASS.

Prior correction attempt
`b7831b95ffcdffe71c090c4b8fd77d620d004d46`
was never processing_started and is:
`SUPERSEDED_BY_OPERATOR_SCOPE_UPDATE`.

## ACTIVE SLOT 1 — KOO / R0.3 INFOFIELD PUBLICATION

Task:
`entities/koordinator/outbox/KOO__source-rebuild-r03-infofield-publish__KOO.md`
commit `831ea8db8197f0f559244495ecd1881d2e9e8342`
blob `ab4f2bf015ad3789e6e2b1761028b9ab4d749bd5`.

Dispatch:
`routes/dispatch/KOO__source-rebuild-r03-infofield-publish__KOO.md`
commit `d0e2f2911d099365fc71341a68828d256f5fa8cb`.

Inbox:
`entities/koordinator/inbox/KOO__source-rebuild-r03-infofield-publish__KOO.md`
commit `64b5b5aad0e965afa5bd6169c7394476952b65f7`.

Sender registry:
`776a9238e6b5813de523bfaa93cde1fa0f685cb5`.

State:
`READY_FOR_EXACT_TASK`.

processing_started:
`no`.

Goal:
establish a verified shared-info-field locator for exact 7-file r0.3 bytes.

Until this PASS, SHT r0.3 recheck is not activated.

## PENDING NEXT — SHT R0.3 NARROW RECHECK

After:
`PASS_KOO_SOURCE_REBUILD_R03_INFOFIELD_PUBLISHED_READY_FOR_SHT_RECHECK`

KOO must fresh-reconcile and send SHT only an activation PROMPT containing:
- exact locator;
- boundary commit/tree;
- file blob/SHA identities;
- D1-D3 + locator-first exact review scope.

No physical transfer of referenced candidate files is required when locator is readable.

## OPEN GATES — unchanged

Recovery v1.5 r0.4 OPERATOR gate:
`17190f729eef6537f0404af387253c9c11eb3a21`.

Source-loading-policy v2.1 OPERATOR gate:
`b15a9250e72e7bb5da4efabd027fa4e43386022e`.

Both remain OPEN / UNRESOLVED.

Project Sources activation:
NO.

## PENDING PARALLEL — KOD SHARD GATEWAY ADAPTER INDEPENDENT VERIFY

KOD terminal PASS:
`abe67edb9fbca9201d4a107761c835a696946591`.

Required next reviewers:
SIS + ARH.

State:
`CURRENT_PENDING_NOT_ACTIVE`.

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: current state after locator-first r0.3 integration and publication routing
СТАТУС: CURRENT_QUEUE
