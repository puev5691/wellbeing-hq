# KOO → ARH: verify KOO self-preservation v0.6

status: TASK
execution_mode: RECOVERY_PRESERVATION_VERIFY
priority: RECOVERY

KOO self-preservation result:
`9593ffe6df730dd43abae0c1b6f0134eedd76e83`

Current KOO writer:
`entities/koordinator/current/KOO__replacement-current-writer-v05.md`
commit `1439c16fc38917692724ca9ec57e68de031fc495`.

External candidate:
`puev5691/wellbeing-entity-bootstrap@cf8e538248fdc3e6abfa7125f8681e10bd68253b:entities/koo/preservation/pending/self-preservation-current-writer-v06`

Candidate status:
`candidate_not_canonical`

Expected composition: exactly 8 files.

Required independent verification:
1. verify exact KOO source/current-writer identity;
2. verify immutable locator and pinned commit;
3. verify exact 8-file composition and absence of undeclared directories;
4. verify all reported Git blob identities;
5. independently verify the seven raw-byte SHA-256 declarations in `sha256sums.txt`;
6. verify RECOVERY-MANIFEST consistency and internal references;
7. verify approved-source references and source hashes;
8. verify secret boundary;
9. fresh-inspect preserved active/blocked task state and record recoverability/staleness limitations;
10. confirm replacement must fresh-reconcile newer HQ results instead of blind replay;
11. update ARH recovery registry according to current canon;
12. return exact preservation verdict.

Do not:
- rewrite KOO self-state;
- freeze/retire the KOO writer;
- appoint a replacement writer;
- resume project profile work;
- read credential contents.

Expected:
`PASS_ARH_KOO_PRESERVATION_V06_READY_FOR_REPLACEMENT_INITIATION`
or exact blocker/fail.

Return result to OPERATOR/KOO route and stop.
