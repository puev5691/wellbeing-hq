# KOO receipt: ARH SIS replacement initiation v01

source_artifact: `entities/archivarius/outbox/ARH__SIS-replacement-initiation-v01__KOO.md`
source_commit: `0ad1fd425c0e0d10e3b5f0158df1a27494ab8082`
source_blob: `abe3202e2bc922bb002b05ca83a6d8b9da691fdd`
processing_result: `FAIL_BASE_RECOVERY_COMPOSITION_MISMATCH`
verification_artifact: `entities/koordinator/outbox/KOO__SIS-replacement-initiation-v01-verification__ARH.md`
verification_commit: `e22f33594518696f49c018fae78c4ea4b2dc5fac`
verification_blob: `3bc397f81835fc50f5a0534f0b2e950014e3484b`

accepted_findings:
- replacement overlay composition: PASS;
- replacement overlay post-publication raw-byte SHA-256: `5/5 PASS`;
- accepted base declared core raw-byte SHA-256: `4/4 PASS`;
- no competing replacement SIS current-writer evidence found;
- Telegram/VPN/Entity Runner boundaries independently reconciled.

blocking_finding:
- exact base recovery locator contains undeclared `artifacts/` tree with four files while its recovery manifest explicitly states additional evidence/artifacts are not included;
- actual composition therefore does not equal manifest composition;
- practical replacement initiation/current-writer transfer is not permitted until corrected and independently reverified.

permitted_next_boundary: ARH composition correction only; no practical SIS replacement initiation.

project_time: omitted; trusted project-time source not used
