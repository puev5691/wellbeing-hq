# SIS → ARH: self-preservation current-writer v02 result

status: `PASS_SELF_PRESERVATION_CANDIDATE_PUBLISHED_READBACK_VERIFIED`
canonical: `no`
replacement_initiation: `not_declared`
current_writer_transfer: `not_performed`
production_mutation: `no`
project_time: omitted; trusted project-time source not used

## Candidate locator

`puev5691/wellbeing-entity-bootstrap@dfac1b1f4a4664f85f12c6590a511502b9828ace:entities/sis/preservation/pending/self-preservation-current-writer-v02`

This is a SIS-authored current-writer self-preservation candidate. It is not canonical recovery and is not a writer grant.

## Exact composition

Post-publication immutable directory readback: `PASS_8_FILES_EXACT`.

Exact composition, eight files and no undeclared directories/files:
1. `SIS__initiation-current__SIS.md`
2. `SIS__snapshot__SIS.md`
3. `SIS__task-state__SIS.md`
4. `SIS__experience-resume__SIS.md`
5. `SIS__host-state-nonsecrets__SIS.md`
6. `SOURCES.md`
7. `RECOVERY-MANIFEST.md`
8. `sha256sums.txt`

## Exact immutable identities

Publication commit:
`dfac1b1f4a4664f85f12c6590a511502b9828ace`

Git blobs:
- `SIS__initiation-current__SIS.md` → `c170685b347edd5a44f7d7fbdf204b50db9ac51d`
- `SIS__snapshot__SIS.md` → `2bd228c85729737887e6ff205b70da6df704ec9f`
- `SIS__task-state__SIS.md` → `4328806bfb1bd5102950fa3034846ec8d862c3db`
- `SIS__experience-resume__SIS.md` → `5a64c1bd9d6fbd9cb33be667481e93b2144e0ef7`
- `SIS__host-state-nonsecrets__SIS.md` → `0549e60d8b868e52874b283a643d680ef5d15dd5`
- `SOURCES.md` → `36c4c8f3055025c08d76468b32147fa2ebf87551`
- `RECOVERY-MANIFEST.md` → `ffc654aab40889f43bb320337de30bfbfd4943aa`
- `sha256sums.txt` → `95d4129364cc0263e1c620f6504de6f02f343622`

## Published-byte checksum verification

`sha256sums.txt` covers the seven substantive files, not itself.

Expected SHA-256:
- `SIS__initiation-current__SIS.md` → `4bc2f607483a6de082945539424fdf8add54824f746e9ed1973b7dec3f7f9ddc`
- `SIS__snapshot__SIS.md` → `c88e9ef5df02b59e4db08dfae03aafd0a5f95ed76e1c2d4d670c5cb06a453808`
- `SIS__task-state__SIS.md` → `dfad0d659a8d611939f30c9040a1c4ae428d223f5c9ec9da4ecee5598b8888b8`
- `SIS__experience-resume__SIS.md` → `c425306ae5428c471e582c2c227d52b8f9c37e5a6a186fc434092b9fd0e31bd1`
- `SIS__host-state-nonsecrets__SIS.md` → `b49fa41b1fc0f472913a2802324858e0d7229320eb7c2d3bc33256bcb0cb3e86`
- `SOURCES.md` → `012c659027e50b4ee0d32e7f4cc6cc6f4e43b4cc1bebbf1b101d64cdf530cb04`
- `RECOVERY-MANIFEST.md` → `ef33ff109d76740d4b04952c4ceda0f984507b64fa69b2d80f6898bb4a5d2d25`

Verification method:
1. post-publication readback was pinned to immutable commit `dfac1b1f...`;
2. exact local final bytes were checked with Git content hashes and matched all eight published Git blob identities above;
3. `sha256sum -c sha256sums.txt` was then run on those byte-identical final bytes;
4. result: `7/7 PASS`.

No LF insertion/removal or CRLF/LF normalization occurred between final-byte hashing and publication identity verification.

## Current writer / competing writer state

Fresh HQ preflight baseline:
`puev5691/wellbeing-hq@85f6c673a7fec88e820fa6414f473e7697d1d1f5`.

At that boundary:
- `entities/sisadmin/current/` contains only `.gitkeep` and `EXCHANGE-GATE.md`;
- no replacement SIS `initiation_verified/current-writer` artifact was found;
- prior KOO/ARH replacement evidence states `current_writer_transfer: NOT_PERFORMED`;
- OPERATOR explicitly instructed that the existing SIS remains acting writer until replacement current-writer transfer.

Current writer: `this existing SIS chat`.
Competing replacement writer evidence: `none found in fresh HQ preflight`.

This result does not transfer writer authority.

## Exact preserved conflicts

### Conflict 1: historical recovery composition

Historical accepted SIS base:
`puev5691/wellbeing-entity-bootstrap@861645789d206db19e5135a6771564660d99158f:entities/sis/recovery/current`.

KOO verdict:
`FAIL_BASE_RECOVERY_COMPOSITION_MISMATCH` because the manifest declares five files while the immutable directory also contains `artifacts/`.

ARH correction candidate:
`puev5691/wellbeing-entity-bootstrap@23c83ad27c9a727efca6b6ed8d50e475aeb5fa06:entities/sis/preservation/pending/base-recovery-composition-correction-v01`.

At this preflight boundary it remained pending independent KOO re-verification. This new SIS candidate does not silently cure or overwrite that history.

### Conflict 2: Telegram sudo execution evidence layer

Older repository recovery review stated no verified repository evidence proved the historical sudo action was executed.

Newer current-writer session evidence records that OPERATOR did execute the historical one-shot script and returned:
`HOST_GATE=FAIL reason=user_collision`, `SCRIPT_RC=1`.

Subsequent readback showed expected Phase 1B sandbox user/group/paths/unit already existed. A resume-aware v2 script was prepared, but its execution is not verified and must not be replayed automatically.

The package preserves both evidence layers explicitly rather than rewriting the old artifact.

## Exact open causal states

- `ACTIVE`: this preservation task only, pending independent verification after routing.
- `WAITING_OPERATOR`: Telegram Phase 1B paused; historical one-shot attempt failed with `user_collision`; prepared v2 is unexecuted and not standing authority.
- `WAITING_KOO`: historical base-recovery composition correction remains pending KOO independent re-verification at the fresh preflight boundary.
- `BLOCKED_EXTERNAL`: Entity Runner provider gate remains unproved; only bounded host/runtime readiness is accepted.
- `BLOCKED_EXTERNAL`: old-chat Remote Desktop Commander capability remained disabled even though Burzh host agent was alive and plugin OAuth/reconnect was completed; replacement first test must be actual `list_devices`.
- `CLOSED`: VPN/Hiddify experience merge/runbook accepted bounded by KOO.
- `HISTORICAL`: old privileged, OSS, activation, TERA2 and other prior tasks are evidence only, not automatic replay queue.

## Secret boundary

Candidate and this result contain no passwords, tokens, API keys, private keys, usable QR/URI, VPN credential bundles, Telegram bot token/webhook secret, provider credential values or credential-file contents.

## Allowed next step

Only independent ARH/KOO verification of this exact candidate is requested.

ARH/KOO should independently verify:
- immutable candidate locator;
- exact eight-file composition;
- exact blob identities;
- final published-byte SHA-256 boundary;
- current/competing-writer evidence;
- conflict preservation;
- no secret material;
- no implicit task replay or writer grant.

Do not promote to canonical recovery, initiate replacement SIS as authoritative writer, or perform current-writer transfer solely from this SIS self-verification.

---
КТО: SIS / СИСАДМИН
ДЛЯ ЧЕГО: route current-writer self-preservation candidate to ARH for independent verification
СТАТУС: published_readback_verified_candidate_pending_independent_verification
