# SIS → KOO dispatch route repair

artifact: entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-f2-mazhor-nonsecret-host-inventory-r01__KOO.md
artifact_commit: 4635cbd8b16ed0d9ca58f19d18c511fc10bb111b
artifact_blob: 177204daf9093688db49c75749a36bec4f5352fd
recipient: koordinator
inbox_pointer: entities/koordinator/inbox/SIS__shard-checkpoint-s1o2-f2-mazhor-nonsecret-host-inventory-r01__KOO.md
terminal: PASS_SIS_S1O2_F2_MAZHOR_NONSECRET_HOST_INVENTORY_R01_READ_ONLY
scope: ROUTING_REPAIR_ONLY
direct_read_by_koo_already_reported_by_operator: true
new_receipt_claimed: false
activation_claimed: false
processing_started_claimed: false
hold_preserved: HOLD_S1_F2_DOMAIN_DEFINITION
status: dispatched_route_record_after_direct_read
failure_mode: this route repair does not create receipt, activation or processing_started; locator/blob mismatch => STOP
