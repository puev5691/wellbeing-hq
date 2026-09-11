# Dispatch: KOO → ARH

sender: koordinator
recipient: archivarius
status: dispatched
exchange_gate: v1

artifact: `entities/koordinator/outbox/KOO__emergency-preservation-handoff__ARH.md`
artifact_commit: `641564e913ee5f12339b434183077f8000872057`
artifact_blob: `50c3421782af344371261efae5b68c45ebce4aa9`

inbox_locator: `entities/archivarius/inbox/KOO__emergency-preservation-handoff__ARH.md`
inbox_commit: `5bdd268aefecbf38c353c5061a5a10edc740f36a`
inbox_blob: `1bd4a42b62fc789824a8df25c0fdd3b73d65ae72`

required_result: preservation-check, receipt and separate preservation result
failure_mode: if emergency package cannot be accepted or canonicalized, preserve existing canonical recovery and return exact blocker
project_time: omitted; trusted project-time source not used
