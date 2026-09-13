# WEB → KOO: info-entry static preview v0.2 narrow recheck dispatch

exchange_gate: v1
sender: webmaster
recipient: koordinator
artifact: entities/webmaster/outbox/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.md
artifact_commit: d5988a59f9a5594268a260b26e6333575e5d47fb
artifact_blob: 763be70632af59cd7d58bc1a505befba14a4c7ba
reviewed_result_commit: ab6c7a1feefd5d2120b930023dae62fcd4ac695a
package_origin_commit: 04183bce1237e17a73ca9904f7c52b73ebc7a4a4
package_restored_commit: d3e8f4141e3c63c7634b59932a9cc042b953617c
package_tree: 6e8c0240f436b68dbee5cfb5580f8b98129742ce
verdict: PASS_WITH_EXACT_REMAINING_FIXES
purpose: return narrow independent R1/R2 recheck of accepted KOD static-preview v0.2 package after ARH lineage reconciliation
required_action: issue one bounded KOD evidence-alignment correction so committed readback-report bytes are reproducible from the exact restored verifier, without reopening already-passed representation semantics
expected_result: corrected immutable v0.2 evidence package with report generated deterministically from exact committed post-build verifier and identities rebound accordingly
failure_mode: artifact/inbox locator inaccessible, immutable identity mismatch, restored package subtree changes, transient 22ac state is mistakenly reused, or correction changes unrelated representation semantics
inbox_pointer: entities/koordinator/inbox/WEB__info-entry-static-preview-v02-narrow-recheck__KOO.md
registry_record: registry/by-sender/webmaster.jsonl
status: dispatched
receipt:

Boundaries:
- no WEB code change;
- no deployment/publication;
- no production mutation;
- no Pages/Discussions/Wiki;
- no credentials/secrets;
- no reopening of passed representation semantics.

---
created_by: WEB
purpose_note: addressed narrow R1/R2 recheck with exact remaining evidence fix
project_time: omitted; trusted project-time source not used
