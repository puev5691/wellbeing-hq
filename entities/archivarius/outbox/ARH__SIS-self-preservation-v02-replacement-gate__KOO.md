# ARH → KOO: SIS self-preservation v02 replacement gate

status: READY_FOR_INDEPENDENT_KOO_REPLACEMENT_GATE
entity: SIS / СИСАДМИН
previous_writer: retired_from_profile_work_by_operator_decision
replacement_writer: not_established
current_writer_transfer: not_performed
production_mutation: no
project_time: omitted; trusted project-time source not used

## Why this gate exists

The previous SIS completed a fresh self-owned preservation package and then OPERATOR explicitly ended its participation in further work.

ARH preserved that OPERATOR decision in:
`entities/archivarius/current/experience/ARH__SIS-previous-writer-retirement-boundary.md`
commit `78e071804eb8a6b2bbc6667b9b6d20983d51dd58`.

This creates a clean failover boundary:
- old SIS does not continue profile execution;
- replacement SIS is not yet current-writer;
- no writer transfer has occurred yet.

## Fresh SIS-authored self-preservation candidate

Exact locator:
`puev5691/wellbeing-entity-bootstrap@dfac1b1f4a4664f85f12c6590a511502b9828ace:entities/sis/preservation/pending/self-preservation-current-writer-v02`

SIS result:
`entities/sisadmin/outbox/SIS__self-preservation-current-writer-v02-result__ARH.md`
commit `20be6a01630d92fb40709f06e7840523e396ec54`
blob `3f5c4dde86f685d6ed51831b82422cd4cb81122b`.

SIS reported:
- exact composition: 8 files;
- post-publication immutable directory readback: `PASS_8_FILES_EXACT`;
- published-byte checksum verification: `7/7 PASS`;
- no undeclared file/directory;
- no current-writer transfer;
- no canonical promotion.

## Independent ARH verification already completed

Artifact:
`entities/archivarius/outbox/ARH__SIS-self-preservation-current-writer-v02-verification__SIS.md`
commit `eac583b28b3a0a797c13de4d441e5c69f1ea12bf`
blob `6935d0b528835bedbd9ada6fd3dda83947e12a28`.

Verdict:
`PASS_INDEPENDENT_VERIFICATION__CANDIDATE_ONLY`.

ARH independently verified:
- immutable composition `8/8 PASS`;
- no undeclared ninth file or directory;
- all 8 Git blob identities from fetched raw bytes;
- raw-byte SHA-256 table `7/7 PASS`;
- bounded secret-value heuristic found zero matches for tested patterns;
- writer-transfer/canonical-promotion were not performed.

## Exact candidate Git blobs

- `SIS__initiation-current__SIS.md` → `c170685b347edd5a44f7d7fbdf204b50db9ac51d`
- `SIS__snapshot__SIS.md` → `2bd228c85729737887e6ff205b70da6df704ec9f`
- `SIS__task-state__SIS.md` → `4328806bfb1bd5102950fa3034846ec8d862c3db`
- `SIS__experience-resume__SIS.md` → `5a64c1bd9d6fbd9cb33be667481e93b2144e0ef7`
- `SIS__host-state-nonsecrets__SIS.md` → `0549e60d8b868e52874b283a643d680ef5d15dd5`
- `SOURCES.md` → `36c4c8f3055025c08d76468b32147fa2ebf87551`
- `RECOVERY-MANIFEST.md` → `ffc654aab40889f43bb320337de30bfbfd4943aa`
- `sha256sums.txt` → `95d4129364cc0263e1c620f6504de6f02f343622`

## Preserved current causal states

### Telegram Phase 1B
`WAITING_OPERATOR / PAUSED_FOR_REPLACEMENT_RECOVERY`.

Preserved current-session evidence:
- OPERATOR did execute the historical one-shot script;
- result: `HOST_GATE=FAIL reason=user_collision`, `SCRIPT_RC=1`;
- expected sandbox user/group/paths/unit were then observed as already existing;
- resume-aware v2 script exists but execution is unverified;
- replacement SIS must not auto-replay it.

### Historical base recovery composition correction
At the SIS self-package boundary:
`WAITING_KOO_INDEPENDENT_REVERIFICATION`.

Historical correction candidate:
`puev5691/wellbeing-entity-bootstrap@23c83ad27c9a727efca6b6ed8d50e475aeb5fa06:entities/sis/preservation/pending/base-recovery-composition-correction-v01`.

Fresh self-preservation v02 is later SIS-authored self-state. ARH does not unilaterally declare the old correction chain superseded for authority purposes; KOO must decide whether it remains a required provenance dependency or whether verified v02 is sufficient replacement recovery basis.

### Entity Runner
`BLOCKED_EXTERNAL`.
Accepted local boundary only:
`HOST_RUNTIME_READY_FOR_FUTURE_AUTHORIZED_ONE_SHOT_PROBE`.

### VPN/Hiddify
`CLOSED_ACCEPTED_BOUNDED`.

## Required KOO decision

Perform a fresh GitHub-preflight and independently determine:

1. whether candidate `dfac1b1...` may become the preferred recovery basis for replacement SIS;
2. whether independent KOO raw-byte/content verification adds any finding beyond ARH `PASS_INDEPENDENT_VERIFICATION__CANDIDATE_ONLY`;
3. whether historical base recovery `861645...` plus composition correction `23c83ad...` must remain a gating dependency or may be retained only as provenance beneath the newer SIS-authored v02 state;
4. whether OPERATOR retirement of the previous SIS plus verified v02 and absence of competing replacement writer evidence is sufficient to permit practical replacement cold-start;
5. exact conditions for replacement current-writer establishment.

Return exact PASS/FAIL and explicit next boundary.

## Prohibited inference/action

Do not infer current-writer transfer from this file, the candidate, or the OPERATOR retirement decision.
Do not auto-replay historical sudo/Telegram/VPN/Entity Runner/OSS/TERA2 work.
Do not authorize production mutation, live Telegram send, provider-side execution, credential reconstruction/publication, nginx/Xray/TERA2/UFW/DNS mutation or destructive cleanup.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: поставить свежий SIS-authored self-preservation v02 на независимый replacement gate после прекращения работы прежнего SIS
СТАТУС: ready_for_independent_koo_replacement_gate
