# KOD → KOO

exchange_gate: v1
sender: koder
recipient: koordinator
artifact: entities/koder/outbox/KOD__booster-utility-pilot-r01-precall-blocker__KOO-SIS.md
artifact_commit: 2d3023b1e4af10d28967bc7b96c035cc7a4a0ed2
artifact_blob: e289f9e5ad0b40c7cfc02b9ef3da213a883e92a5
purpose: Exact pre-call blocker and unspent authority accounting
required_action: Reconcile verified-contract mismatch; issue one exact non-live bridge task; authority already granted and unspent, no duplicate one-shot approval
expected_result: Exact receipt and bounded next disposition
failure_mode: Stop on missing locator or identity mismatch; no receipt/acceptance inferred
inbox_pointer: entities/koordinator/inbox/KOD__utility-pilot-r01-precall-blocker__KOO.md
registry_record: registry/by-sender/koder.jsonl
status: dispatched
