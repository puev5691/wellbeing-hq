# KOO source rebuild r0.3 integration result

status: CANDIDATE_R03_MATERIALIZED_LOCAL_READBACK_PASS
project_sources_activation: no
approval: no
project_time: omitted; trusted project-time source not used

## Exact lineage

Previous open correction task:
`entities/koordinator/outbox/KOO__source-rebuild-r03-correction__KOO.md`
commit `b7831b95ffcdffe71c090c4b8fd77d620d004d46`
blob `98bdd0c56cf017f238aabf76be91070b757e3e6a`.

That attempt had:
`processing_started: no`.

OPERATOR then supplied a new exact input:
PROMPT activation no longer requires physical transfer of referenced artifacts when the addressed Entity can read them from project info field by exact locator and immutable identity.

Because authoritative inputs changed before processing_started, the prior open correction attempt is dispositioned:

`SUPERSEDED_BY_OPERATOR_SCOPE_UPDATE`.

No old attempt is replayed.

## Applied correction scope

r0.3 integrates:

1. SHT D1 — deterministic replacement PROMPT attempt lifecycle;
2. SHT D2 — chat-specific conveyor vs generic Entity instance boundary;
3. SHT D3 — deterministic source-set rollback;
4. OPERATOR locator-first activation decision:
   - PROMPT remains activation payload;
   - PROMPT may be direct text or file-form;
   - referenced artifacts are not physically transferred when exact locator + immutable identity are readable by recipient;
   - physical artifact transfer is fallback only for unavailable locator or external file absent from shared information field;
   - 40–50 character naming rule applies only to file-form PROMPT;
   - task authority, automation-authority, `activation != processing_started`, and delivery/receipt/acceptance boundaries remain unchanged.

## Exact r0.3 package identity

Local candidate package:
`project-sources-conveyor-v1-r03-candidate.zip`

SHA-256:
`2c0327f8fdeb5a1f47da2bf9cdb74892b19ebf1e2edfd0c899dd3af043003b4c`

Size:
`57473 bytes`

Composition:
exactly 7 files.

Local ZIP readback:
`7_OF_7_PASS`.

Exact file SHA-256:

- `SOURCE-REBUILD-MANIFEST.md`
  `ec02d7482f2a74fd0dff25e77e81941705bbe0a464d61b47962cb4859e47b888`
- `task-conveyor-canon-v1-candidate.md`
  `7be4a0d30d0e8ad1653f9d3aea50f92ff2ed20a8190b7f9f722ea2b4a83b7644`
- `project-instructions-core-v2_2-candidate.md`
  `8c3ed7faa58da334b5b8bc2cff2d2dcbac764c92e0ef7d22f664292e31b79fd2`
- `entity-roles-short-v2_4-candidate.md`
  `e9a150d897932e02b123b180bca1939649045538100f652f379d52fd1cd6dcdb`
- `file-work-canon-universal-v2_4-candidate.md`
  `04e670583b95880410ec70f42be1b705d3eb068e3fe4bddffeef27d4b5e95e10`
- `source-loading-policy-v2_2-candidate.md`
  `081d8737c8e24ef58d9e9e7d17fbfc341c4736a181c584b05e854d298fd3644a`
- `entity-state-preservation-and-recovery-canon-v1_6-candidate.md`
  `eead47bfd085e9473c729307c8d4aff06d3a8379283dc1cb91f803d2d592c673`

## Preserved gates

These remain OPEN / UNRESOLVED:

Recovery v1.5 r0.4 OPERATOR gate:
`17190f729eef6537f0404af387253c9c11eb3a21`.

Source-loading-policy v2.1 OPERATOR gate:
`b15a9250e72e7bb5da4efabd027fa4e43386022e`.

No candidate is approved, withdrawn or selected silently.

## Info-field publication boundary

The new operator decision removes the need to physically hand referenced package bytes to the reviewer **once those exact bytes are available in the project information field by verified locator**.

At this result boundary, r0.3 package bytes are materialized and locally read back, but a verified GitHub/info-field locator for the exact r0.3 bytes has not yet been established.

Therefore SHT re-review MUST NOT start from this result alone.

Next causal state:

`SOURCE_REBUILD_R03_READY_FOR_INFOFIELD_PUBLICATION`.

After exact info-field publication + readback, route a narrow SHT recheck using only:
- activation PROMPT;
- exact locator;
- commit/blob or equivalent immutable identity;
- package/file hashes.

No manual transfer of referenced source files will be required after that barrier passes.

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: integrate SHT D1-D3 + OPERATOR locator-first activation decision into candidate r0.3
СТАТУС: CANDIDATE_R03_MATERIALIZED_LOCAL_READBACK_PASS
