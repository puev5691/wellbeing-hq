# SECE runtime-integration grounding correction R03

status: OFFLINE_RUNTIME_INTEGRATION_IMPLEMENTATION_CANDIDATE_NOT_ACTIVATED
attempt: KOD_SECE_R01_RUNTIME_INTEGRATION_GROUNDING_CORRECTION_R03_A1

Predecessor:
puev5691/wellbeing-hq@ca7de24d7a03e0ce45859511eeb4ed4d73a98f3b:
entities/koder/outbox/sece-r01-runtime-integration-offline-implementation-static-correction-r02/
tree 4f473559512c1a0c16561e414d870190f1bed3b6

R03 corrects only SHD C1-R and C3-R.

C1-R:
authoritative TrustPolicy evidence dependency now travels through resolution, Effective Context/contract, intent, admission and invocation frontier with exact identity/version/currentness/conflict binding.

C3-R:
ACTOR_EXECUTION_BINDING is derived from exact verified/current evidence, not directly normalized from caller state. Supporting evidence identities/versions are part of binding identity and invocation frontier.

C2 remains preserved; only dependency plumbing was added to its accepted invocation verifier.

Reviewed baseline core is unchanged.
Candidate remains NOT_ACTIVATED.
