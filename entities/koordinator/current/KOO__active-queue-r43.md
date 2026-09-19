# KOO current active queue r0.43

status: CURRENT_QUEUE
writer: `entities/koordinator/current/KOO__replacement-current-writer-v06.md`
writer_commit: `525e5b131472e61b1f55db5ef7307217aea4c4fc`
writer_gate_pass: `06dd7873b532c1fe86f4b382d40c26908a5a11b2`
project_time: omitted; trusted project-time source not used

## Fresh change

OPERATOR changed the conveyor transport assumption after r0.42:

PROMPT activation does not require physical transfer of referenced artifacts when the addressed Entity can read them from the project information field by exact locator and immutable identity.

Physical artifact transfer is fallback only for unavailable locator or an external file absent from the shared information field.

This is a new exact input to the existing source-rebuild r0.3 lineage.

## Attempt disposition

Previous open correction task:
`entities/koordinator/outbox/KOO__source-rebuild-r03-correction__KOO.md`
commit `b7831b95ffcdffe71c090c4b8fd77d620d004d46`
had `processing_started=no`.

Because authoritative inputs changed before processing started, that open attempt is now:

`SUPERSEDED_BY_OPERATOR_SCOPE_UPDATE`.

No replay of the old attempt is allowed.

## COMPLETED THIS CYCLE — SOURCE REBUILD R0.3 MATERIALIZATION

Integration result:
`entities/koordinator/outbox/KOO__source-rebuild-r03-integration-result__KOO.md`

commit:
`5488c79e626f9ab4085a14b864e4a5ed7e536eaf`

blob:
`a6269282611bd382e2977cd21174ee1f2d4204a8`

Exact local candidate package:
`project-sources-conveyor-v1-r03-candidate.zip`

SHA-256:
`2c0327f8fdeb5a1f47da2bf9cdb74892b19ebf1e2edfd0c899dd3af043003b4c`

Size:
`57473 bytes`

Composition:
7 files.

Local ZIP readback:
`7_OF_7_PASS`.

Integrated scope:
- SHT D1 replacement-PROMPT lifecycle;
- SHT D2 chat-specific conveyor / generic Entity instance boundary;
- SHT D3 deterministic source-set rollback;
- OPERATOR locator-first activation decision.

Project Sources activation:
NO.

Approval:
NO.

Open OPERATOR gates remain OPEN / UNRESOLVED:
- recovery v1.5 r0.4 gate `17190f729eef6537f0404af387253c9c11eb3a21`;
- source-loading-policy v2.1 gate `b15a9250e72e7bb5da4efabd027fa4e43386022e`.

## ACTIVE SLOT 1 — KOO / R0.3 INFOFIELD PUBLICATION

Exact task:
`entities/koordinator/outbox/KOO__source-rebuild-r03-infofield-publish__KOO.md`

commit:
`831ea8db8197f0f559244495ecd1881d2e9e8342`

blob:
`ab4f2bf015ad3789e6e2b1761028b9ab4d749bd5`

State:
`READY_FOR_EXACT_TASK`.

processing_started:
`no`.

Goal:
publish exact 7-file r0.3 candidate bytes into shared project information field, establish one immutable boundary, and read back 7/7.

This is required before the next SHT review so that OPERATOR will transfer only the activation PROMPT, not the referenced source package.

Expected:
`PASS_KOO_SOURCE_REBUILD_R03_INFOFIELD_PUBLISHED_READY_FOR_SHT_RECHECK`
or exact blocker/fail.

## PENDING NEXT — SHT R0.3 NARROW RECHECK

Do not activate before exact info-field publication + readback PASS.

After publication PASS, the SHT activation PROMPT will contain:
- exact info-field locator;
- boundary commit/tree;
- per-file blob/SHA identities;
- D1–D3 + locator-first decision review scope.

No physical package transfer is required if SHT can access the locator.

## PENDING PARALLEL — KOD SHARD GATEWAY ADAPTER INDEPENDENT VERIFY

KOD terminal PASS remains current:
`abe67edb9fbca9201d4a107761c835a696946591`.

Required reviewers:
SIS + ARH.

State:
`CURRENT_PENDING_NOT_ACTIVE`.

Fresh-reconcile before activation.

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: apply OPERATOR locator-first decision and move source rebuild to info-field publication
СТАТУС: CURRENT_QUEUE
