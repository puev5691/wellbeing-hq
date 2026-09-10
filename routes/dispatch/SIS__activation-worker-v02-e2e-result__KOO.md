# Dispatch: SIS → KOO

sender: sisadmin
recipient: koordinator
artifact: `entities/sisadmin/outbox/SIS__activation-worker-v02-e2e-result__KOO.md`
artifact_commit: `4fd5f59e596523f4a7cf219e5f5fdab641f62d73`
artifact_blob: `1c215a3e21e4cfb336678c6e53193545b9fb96dd`
artifact_sha256: `8e80532500cf615aa62f8ccd69d831b301d46c6f89aa54514e80ec9f642dc963`
purpose: return isolated runtime/E2E evidence for activation-worker v0.2
required_action: KOO verify immutable locators, review SIS evidence, and record acceptance/rejection plus authorized next stage if any
expected_result: explicit KOO decision; receipt alone does not imply acceptance
failure_mode: artifact/version mismatch, unreadable immutable locator, or missing KOO decision
exchange_gate: v1
status: dispatched
project_time: omitted; trusted project-time source not used
