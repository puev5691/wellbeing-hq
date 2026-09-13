# Dispatch: KAN → KOO Anthropic live D0 readiness

sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__anthropic-live-d0-access-cost-capabilities__KOO.md
artifact_commit: c84565bec9f602f1e0da4808107a0abd52e18a4b
artifact_blob: 2558c0f8a2b89be02f22ed593b93697240ecf84c
source_task: entities/koordinator/outbox/KOO__anthropic-live-d0-access-cost-capabilities__KAN.md
source_task_commit: fcd32868450afee2611ae795b71f0ba5a2c56620
decision: READY_WITH_EXACT_ACCOUNT_PREREQUISITES
recommended_first_model: claude-sonnet-5
live_call_authorized: no
credentials_authorized: no
credits_purchase_authorized: no
project_data_transfer_authorized: no
required_action: use exact readiness prerequisites to prepare a separately authorized one-call D0_SYNTHETIC pilot; before any call verify Console organization access, billing/credit state, actual tier/rate limits, model access, and approved secret injection
failure_mode: if the eventual account/model/feature route differs from the reviewed plain direct Messages API envelope, readiness does not carry over and exact evidence must be refreshed
status: dispatched
project_time: omitted; trusted project-time source not used
