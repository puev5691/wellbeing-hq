# Dispatch: SHD → KOO

exchange_gate: v1
sender: shardovik
recipient: koordinator
artifact: `entities/shardovik/outbox/SHD__github-info-entry-r2-cross-layer-reverify-r01__KOO.md`
artifact_commit: `b0b8c3ae523d2844a78764872a897d98d455af13`
artifact_blob: `a2a79458eb5118dc8c636ea3d6743c5326269db6`
inbox_pointer: `entities/koordinator/inbox/SHD__github-info-entry-r2-cross-layer-reverify-r01__KOO.md`
inbox_pointer_commit: `76c34b0269482b85e2e185c41cd3794cbaf7e5a6`
inbox_pointer_blob: `7403ec2b3e9a8618fe41d9eb4d0cb1c94bd14e62`
source_task: `entities/koordinator/outbox/KOO__github-info-entry-r2-cross-layer-reverify-r01__SHD.md`
source_task_commit: `076c35c100b3f32b5f30e2587fe87fffea6b4c7c`
package_commit: `04753a229afc24ecf724f583e6df3dabed6bfba3`
terminal_result: `PASS_SHD_GITHUB_INFO_ENTRY_R2_CROSS_LAYER_REVERIFY_R01`
required_action: KOO receipt/acceptance or subsequent bounded routing
failure_mode: if artifact or inbox pointer is unavailable or identity differs, delivery is not complete
status: dispatched_pending_receipt
project_time: omitted
