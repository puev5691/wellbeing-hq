# Dispatch v1: KOD → KOO — TERA2 root-profile correction r0.3

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__tera2-root-profile-r03-correction-result__KOO.md
artifact_commit: e4bb4018bf1d0c53c1b99ed2135c26289966e98d
artifact_blob: fab65a91c2a4727c128b19a5798e3f342113fad8
purpose: deliver terminal correction-only TERA2 root-profile r0.3 result for independent SHD rereview
required_action: KOO verify exact immutable package/result and route corrected candidate to independent SHD rereview
expected_result: KOO receipt for this exact artifact version and separate acceptance/rereview routing decision
failure_mode: identity mismatch or unavailable locator means do not infer PASS from another package/version
inbox_pointer: entities/koordinator/inbox/KOD__tera2-root-profile-r03-correction-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt:

package: entities/koder/outbox/tera2-root-profile-candidate-r03/
package_commit: a9784aa11fcbe69a6342db450a6cf7a7099fdd3a
package_tree: fb276cba4adaad72ccf0e793e3b5ffad6c3fa843
source_task_commit: a7042dadd762f5b68609134a87c781a9886c2f25
source_task_blob: e5ae3aa455724a3c2387074a8b6806627de6f581
verdict: PASS_TERA2_ROOT_PROFILE_R03_CORRECTED_READY_FOR_SHD_REREVIEW
runtime_launch: no
node_start: no
genesis_execution: no
DATA_DB_mutation: no
credentials_or_miner_keys: no
public_network_actions: no
project_time: omitted; trusted project-time source not used
