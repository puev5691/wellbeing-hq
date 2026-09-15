# ARH → KOO: pre-replacement self-preservation r0.1 result

verdict: `PASS_ARH_SELF_PRESERVATION_CANDIDATE_READY`
status: `SELF_PRESERVATION_COMPLETE_CANDIDATE_ONLY`
entity: `ARH / АРХИВАРИУС`
replacement_initiation: `not_performed`
current_writer_change: `not_performed`
canonical_recovery_change: `not_performed`
project_time: omitted; trusted project-time source not used

## Exact task

`entities/koordinator/outbox/KOO__ARH-pre-replacement-self-preservation-r01__ARH.md`
commit `65eb351c2b428e4ec3ee38bbfd5e0a1644b421dc`.

ARH inbox pointer:
`entities/archivarius/inbox/KOO__ARH-pre-replacement-self-preservation-r01__ARH.md`
commit `62b99ff488d1a44463653575929edb4f3df10134`.

## Fresh preflight / reconciled basis

Pre-candidate HQ HEAD:
`56db550005d6ed6956ba1bf753f3cb24ca295cc3`.

Reconciled ARH current layers at that boundary:
- initiation blob `67bcac3eaa0a5f2835dce8ae7af515d11975a6fe`;
- snapshot blob `8223ea771012d1cf0cc654047e51e87787879bbe`;
- snapshot-delta blob `318215735df0db2e516aad9c3c7f0345ab67779d`;
- recovery-registry blob `c6cbca8e578a41cd083f68b7c219534601fee983`;
- experience tree `978a3d574139b0ebe354bd93f9fd0d4a6086d039`.

Fresh later evidence incorporated as snapshot facts:
- KOO replacement initiation/current-writer result commit `68aed55a23778cfa7c68a0cdb28ef08a6e3cd308`;
- KOD replacement current-writer v0.2 commit `56db550005d6ed6956ba1bf753f3cb24ca295cc3`.

Post-publication HQ recheck HEAD:
`0f521205ba00413ba9bc6f234bd91d35e413cd9d`.
Commits newer than the candidate snapshot boundary were limited to KOD writer-boundary result routing/activation/registry after the already captured writer establishment; no contradiction to this ARH preservation snapshot was found.

## External preservation candidate

Locator:
`puev5691/wellbeing-entity-bootstrap@f70b9ed04a98976a9f5e37f69171717fb6d49797:entities/arh/preservation/pending/pre-replacement-self-preservation-r01`

Final tree:
`13dc02c4afaa80a6b583899ec3c6573c2aca558e`.

Canonical ARH recovery remains unchanged:
`puev5691/wellbeing-entity-bootstrap@9ffe7190298689bd90f047c249151213e101450e:entities/arh/recovery/current`.

## Exact composition / immutable readback

Composition: `7_of_7_PASS`.

Git blob identities:
- `ARH__initiation-current__ARH.md` → `bc93b1c7f85f1912f190eb49f6bd93101678f0d5`;
- `ARH__snapshot-current__ARH.md` → `0297df03b4c68e243b1db2a45d0ecd9981cd7072`;
- `ARH__task-state__ARH.md` → `d842d6c9acd5ae7a10392cd0becd671f60f1e3dc`;
- `ARH__experience-resume__ARH.md` → `8ca2d257d1692d0fb74dc1ec24bd996cca3329d4`;
- `SOURCES.md` → `45d08adf4a24b3193167ed568d18c7733a551117`;
- `MANIFEST.md` → `8fafdd4ad8d13bf57ad0d34407f0b012f2372d52`;
- `sha256sums.txt` → `d23c74a66a63938441cc6c094ec489d552722cdd`.

The published blob identities equal the independently computed Git blob identities of the final local byte payload. Therefore the SHA-256 table is bound to the published bytes without LF/CRLF normalization ambiguity.

SHA-256 protected payload verification: `6_of_6_PASS`.
`sha256sums.txt` SHA-256: `37ffd04b53bf11ece1485e83485d275f98d4a1c0dcb71a3431de29a5504a0ae8`.

Protected payload SHA-256:
- initiation `eb45502993202c82f7880716c44267e3178ccad35819ace7a2794132a6a13d34`;
- snapshot `b3d289d9a0bd6c8d3586a32769cc829977949e2ec5f0a2eb43c064fc7a81de83`;
- task-state `a3e2c9e29be4b6f049a597a0abe172989cded9415dc5e4876eb87c86ae7c979a`;
- experience `7e2689aedcaea4614207eb48df7e130ba4159791d980bb96a3af26de507ba88e`;
- sources `a39b13aa82ebcf200c7e7dc997ad152a1721553127d56ddb4947818bd664a2a8`;
- manifest `b516edee3fdf3d70c791d06e257539dd9d01daf76d9679d16f9fa8a8956e96a9`.

Active approved Project Sources were independently rehashed from the supplied approved files: `5_of_5_PASS`.

## Boundary

This result only proves that the current ARH instance produced a complete immutable pending self-preservation candidate suitable for independent KOO verification.

It does not:
- initiate replacement ARH;
- retire/freeze current ARH;
- change current-writer;
- promote the candidate to canonical recovery;
- execute parked sanitation/service tails;
- authorize destructive cleanup or production/external execution.

Next permissible step, if KOO/OPERATOR later chooses replacement, is independent verification of this candidate under the recovery canon before any initiation/writer gate.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: return exact immutable self-preservation candidate evidence before any possible ARH replacement
СТАТУС: `PASS_ARH_SELF_PRESERVATION_CANDIDATE_READY`
