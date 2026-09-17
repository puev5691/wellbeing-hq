# KOO → KOD: emergency replacement initiation v0.4

status: `READY_FOR_FRESH_EMERGENCY_INITIATION_ATTEMPT`
THIS_IS_NOT_A_PROFILE_TASK
project_time: omitted; trusted project-time source not used

## Purpose

Run a NEW initiation attempt in this new KOD instance using the same canonical recovery and existing emergency failover authority. Do NOT continue another chat instance's failed initiation state.

## Transport source pack

Input archive supplied by OPERATOR:
`KOD_source_gate_pack_v01.tar.gz`

Expected archive SHA-256:
`72f005ff6e95a37ea72ff5ddedac8c3b39fa04cea7a92989afe340a999331b8a`

The archive contains exactly the five approved Project Sources required by the active source-loading policy plus `SHA256SUMS.txt` and README.

Required source verification:
1. verify archive checksum if transport preserves the exact bytes;
2. extract/read the package;
3. run or otherwise reproduce `sha256sum -c SHA256SUMS.txt`;
4. require exact 5/5 PASS before proceeding;
5. load the five source texts into active initiation context.

## Recovery canon status clarification

Exact clarification:
`entities/koordinator/outbox/KOO__recovery-canon-v14-status-clarification__OPERATOR.md`
commit `3c8996b071893b8222fb50c6233148731a764c64`.

For exact source:
`entity-state-preservation-and-recovery-canon-v1_4-approved.md`
SHA-256 `984871a22aab1910fc4ab3217c16488eac1e472734bdfd1948fd57c213566fda`

OPERATOR explicitly confirmed that the service-card status `approved_for_active_use / approved_by_operator / Effective: true` controls over the erroneous word `candidate` in the title. Do not alter the source bytes and do not generalize this clarification to any other draft/candidate file.

## Canonical recovery

`puev5691/wellbeing-entity-bootstrap@f134dac1a3c64523fe6e74a8c90bfc79bcc86078:entities/kod/recovery/current`

Independent ARH verification:
`entities/archivarius/outbox/ARH__KOD-emergency-recovery-verification__KOD.md`
commit `78a8f278e3a332bce05e28352e1316ea18f0a13c`
verdict `PASS_PUBLISHED_CANONICAL_RECOVERY`.

## Existing emergency failover authority

`entities/koordinator/outbox/KOO__KOD-emergency-failover-v03__OPERATOR.md`
commit `0ef6727698cdadbd6c5c2015fdf6e585a824b862`.

That authority already sets former writer v0.2 operational state for new KOD mutations to:
`RETIRED_BY_EXPLICIT_OPERATOR_EMERGENCY_FAILOVER_DECISION`.

Former writer artifact:
`entities/koder/current/KOD__replacement-current-writer-v02.md`
commit `56db550005d6ed6956ba1bf753f3cb24ca295cc3`
blob `23f20f04504c65497c154c099d8090cde11fba83`.

## Mandatory fresh attempt sequence

1. Load and verify all five approved Project Sources from the supplied source pack.
2. Read the canonical recovery package from its immutable locator.
3. Verify recovery composition and checksums/readback according to its manifest.
4. Set one exact initiation status:
   - `initiation_verified`, or
   - `initiation_loaded_external_unverified`, or
   - `initiation_failed`.
5. If not `initiation_verified`, stop and return exact blocker. Do not establish writer.
6. If `initiation_verified`, fresh-scan `puev5691/wellbeing-hq`.
7. Reconcile KOD delta since recovery publication, including the retired writer v0.2, accepted benchmark authority decision, and unfinished three-model evidence-tail.
8. Perform fresh competing-writer check. Historical v0.1/v0.2 markers do not count as competing active writers where superseded/retired by explicit immutable evidence. Any NEW KOD writer evidence newer than emergency authority must block establishment until reconciled.
9. If clean, establish exactly one new replacement current-writer v0.3/v0.4 for this instance using the existing OPERATOR emergency failover authority.
10. Stop immediately after writer establishment and return result to KOO. Do NOT resume profile work in the same initiation cycle.

## Unfinished profile work boundary

Exact unfinished task remains NOT PASS:
`entities/koordinator/outbox/KOO__openai-model-policy-extension-impl-r01__KOD.md`
commit `b98458343c6502c5fa6a3dec9dc9ca296c1cff2b`.

Evidence-tail:
- `7957b4d0211ed6cef96f54f2693c19b88e9f9d2e`
- `9824993082fccacfd09ac47ad465eb342803878e`
- `715eeb2357e23605d0570a15a900c5ceeced705c`
- `495053e79b37baec3b6239180becf214018f9b80`
- `f501869c31b8a5d383bd36095356c46726f170c6`

Classification:
`UNFINISHED_UNACCEPTED_EVIDENCE_TAIL`.

Do not run, modify, accept, discard or supersede this tail during initiation.

## Forbidden in this cycle

- profile implementation work;
- live provider calls;
- API keys/credentials;
- billing/account mutations;
- production deployment;
- TERA2/WBN execution;
- mutation of approved Project Sources.

## Expected terminal

`PASS_KOD_EMERGENCY_INITIATION_V04_WRITER_ESTABLISHED`

or exact `BLOCKED_* / FAIL_*`.

Return KOO through current Exchange Gate.
