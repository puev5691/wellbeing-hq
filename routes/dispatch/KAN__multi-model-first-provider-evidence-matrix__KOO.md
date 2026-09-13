# Dispatch: KAN → KOO first-provider D0/D1 evidence matrix

sender: kancelar
recipient: koordinator
artifact: entities/kancelar/outbox/KAN__multi-model-first-provider-evidence-matrix__KOO.md
artifact_commit: 4ef395dfbdc2dee4dbb0e5f2472d5e5acf597ddf
artifact_blob: e548140d171b0e21d5a11038263085fb752f764d
source_task: entities/koordinator/outbox/KOO__multi-model-first-provider-evidence-matrix__KAN.md
source_task_commit: 0318580018815b86248394bec7f46194e1ea6330
classification_anthropic_direct: ELIGIBLE_D1
classification_google_vertex_gemini_direct: ELIGIBLE_D1
classification_openrouter_d0: ELIGIBLE_D0_WITH_EXACT_CONTROLS
classification_openrouter_d1: CONDITIONAL
provider_connection_authorized: no
credentials_authorized: no
external_project_data_transfer_authorized: no
purchase_authorized: no
required_action: use exact source locators and route envelopes for later pilot-route selection; OpenRouter D1 requires pinned-upstream official policy evidence plus deterministic no-fallback verification
failure_mode: if product/API/model/endpoint/router configuration differs from the reviewed route envelope, classification does not carry over and reverts to UNKNOWN_PENDING_EVIDENCE until refreshed
status: dispatched
project_time: omitted; trusted project-time source not used
