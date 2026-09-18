# КОДЕР → КОО: live-worker immutable hash metadata fix r0.1

Результат: PASS_LIVEWORKER_HASH_METADATA_FIX_R01_READY_FOR_REVERIFY.

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__liveworker-hash-metadata-fix-r01-result__KOO.md
artifact_commit: fe38612cc1d1355404b8863c30a17a538602c219
artifact_blob: 65e4b5f5b14d3e3cd559647d03e8ce9ecc534f88
artifact_sha256: ea7991a8a8c4367a8a9f10c2c1c078384d9f35e0e84b55d12969f317d79ac6f3
package: entities/koder/outbox/entity-resource-gateway-live-worker-hash-metadata-fix-r01/
package_commit: 716637bb0e18319fa8f3151253ed5c71b8c1aad7
package_tree: 2737ae65789e6608ad71631e074cc67602a182ab
purpose: вернуть metadata-only live-worker hash reconciliation package на независимую повторную проверку
required_action: проверить exact Git blob bytes и прямые SHA-256; подтвердить receipt; назначить SIS independent reverification metadata-only package
expected_result: receipt точных версий и SIS verdict по immutable hash consistency без live provider calls
failure_mode: при несовпадении commit/tree/blob/SHA-256 не подтверждать received; повторить чтение exact blob API bytes
inbox_pointer: entities/koordinator/inbox/KOD__liveworker-hash-metadata-fix-r01-result__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
receipt: null
acceptance_status: not_claimed

Code/test blobs unchanged from behavior-verified race-fix. Correct direct SHA-256:
live_worker.py 175e95b1cde6fb72d9c473b34e796a93d4c243936ded9f397032a8254ae113a3
test_live_worker.py 3eb5f2ff7c664f8a03cd3978636537aa8ab5c776dc44803c56799d779f0c5ad0

Post-publication rerun: 31/31 PASS. Real provider calls/credentials: 0.
