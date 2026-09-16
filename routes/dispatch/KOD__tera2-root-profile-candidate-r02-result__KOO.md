# Dispatch v1: KOD → KOO — TERA2 root-profile candidate r0.2

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__tera2-root-profile-candidate-r02-result__KOO.md
artifact_commit: 94c6ecff6a7aa0fcdbba3b549a14c3de0664a9f9
artifact_blob: 8e783354d517fb354e0cefb83976cfe08c9eaa7c
purpose: deliver terminal candidate-only TERA2 root-profile r0.2 result
required_action: KOO verify exact immutable package/result and decide separate SHD/SIS review routing; no launch authority is implied
expected_result: KOO receipt for this exact artifact version and separate acceptance/rejection or next review gate decision
failure_mode: identity mismatch or unavailable locator means do not infer PASS from another package/version
inbox_pointer: entities/koordinator/inbox/KOD__tera2-root-profile-candidate-r02-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt:

package: entities/koder/outbox/tera2-root-profile-candidate-r02/
package_commit: 0562bafc790ba2f5e8b5e26214e14e7fa246146e
package_tree: c914edd8a4b2f4cf9488b5b03654327e3c155311
source_task_commit: a704c0ba37242e1bb03f63c71b7689d7868bde3f
verdict: PASS_TERA2_ROOT_PROFILE_CANDIDATE_R02_READY_FOR_REVIEW
runtime_launch: no
node_start: no
genesis_execution: no
existing_DATA_DB_mutation: no
credentials: no
production: no
project_time: omitted; trusted project-time source not used
