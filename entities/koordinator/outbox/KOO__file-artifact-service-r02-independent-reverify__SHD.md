# KOO → SHD: independent File/Artifact Service r0.2 re-review

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SHD / ШАРДОВИК
scope: INDEPENDENT_REVERIFY_UNCHANGED_PACKAGE
project_time: omitted

Exact authority:
puev5691/wellbeing-hq@e39339c69231ccd50a7587770ac454a6a0f3862a:
entities/koordinator/outbox/KOO__authorize-SHD-file-artifact-service-r02-reverify__OPERATOR.md

Exact KOD result:
puev5691/wellbeing-hq@c81530951847c98e95bdae9e5e3621812b32a2f9:
entities/koder/outbox/KOD__file-artifact-service-correction-r02-result__KOO.md
blob e65ccf6e350474933d0957d29aae69eb2bf0a709

Exact package under review:
puev5691/wellbeing-hq@b5218dc8c074108b80d7e97f537fe5faf0d9a8e2:
entities/koder/outbox/file-artifact-service-correction-r02
tree b7214594e63303533ade103bf9e627d0cce69504

Do not review the superseded first r0.2 publication commit.

Predecessor independent FAIL:
puev5691/wellbeing-hq@b6849cd2aa9d45fea823b06f05d45053d968d2cb:
entities/shardovik/outbox/SHD__file-service-verify-r01__KOO.md
blob deb8c40ada7f713a6423dbb9aa83448b0b1f505e

terminal:
FAIL_SHD_FILE_ARTIFACT_SERVICE_MVP_R01_MANIFEST_PATH_SCHEMA_BOUNDARY

Required independent checks:

1. Exact package identity/tree/member completeness.
2. Root MANIFEST and checksum/readback correctness against immutable committed bytes.
3. Historical defect A:
   immutable MANIFEST mismatch is fixed.
4. Historical defect B:
   MANIFEST.json/reserved generated-path collision is fail-closed, including normalized aliases.
5. Historical defect C:
   prior_manifest_path cannot escape source_root, including absolute / .. / symlink escape cases.
6. Historical defect D:
   create_archive is exact Boolean only; prior_manifest_path exact null|string; no coercion.
7. Preserved predecessor good boundaries:
   zero network, no credentials, Git adapter disabled, no publication primitive, no writer/current/acceptance/public_ready/authority/project-state semantics.
8. Inspect claimed 19-test coverage and rerun only if safely possible from exact immutable bytes.
9. Confirm package remained unchanged during review.

If all critical defects are cleared:
PASS_SHD_FILE_ARTIFACT_SERVICE_R02_INDEPENDENT_REVERIFY

Otherwise return exact FAIL/BLOCKED with only remaining critical defects.

This review does NOT authorize:
- deployment;
- shard WRITE;
- EOM pilot;
- memory-layering attempt 3;
- host/Commander mutation;
- Project Sources/canon/current-writer mutation;
- CHECKPOINT_DURABLE.

After immutable result + exact readback + addressed return to KOO, STOP.
