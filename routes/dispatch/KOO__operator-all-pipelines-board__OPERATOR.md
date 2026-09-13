# KOO → OPERATOR dispatch: all HQ pipelines board

artifact: `entities/koordinator/outbox/KOO__operator-all-pipelines-board__OPERATOR.md`
artifact_commit: `4a3a2f8fd61adfd70b6dff0354bc42ac51f35b19`
artifact_blob: `8d9b3b57d261cd2928f0e556446f81fb15b18b3a`
recipient: operator
purpose: operator-facing round-robin map of all currently verified HQ task pipelines, not only the five-phase polling chain
required_action: use as current dispatch board; each actual launch still starts with fresh GitHub-preflight/Resume-First
failure_mode: if repository state changes materially, board must be refreshed before relying on its current-owner fields
project_time: omitted; trusted project-time source not used
