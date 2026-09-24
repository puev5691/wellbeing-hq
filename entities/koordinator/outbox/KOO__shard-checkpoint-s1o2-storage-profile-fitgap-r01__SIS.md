# КОО → СИСАДМИН: S1+O2 non-live storage/profile fit-gap

status: TASK_MATERIALIZED_DOCUMENT_REVIEW_ONLY
project_time: omitted; trusted project-time source not used
task_authority: direct current OPERATOR selection SELECT_S1_O2_FOR_B_NONLIVE_SCOPE_DESIGN_ONLY; SIS approved role covers infrastructure storage/backup technical requirements
scope: one read-only repository-based design/fact-finding step; no host inspection

## Basis

Fresh prewrite HQ HEAD: 8a5dc8dffd12a158f6501eacbece46b55a805246.
KOO current writer v0.8 blob ca7ed0ed4e539dcdbe783e122cea409a77ab10cd.
Latest SIS writer artifact in fresh full tree: entities/sisadmin/current/SIS__emergency-replacement-current-writer-r06.md blob 05406a926eebb1a6009c5d6b70c5bcf9cd18b1ca. SIS must independently verify its own physical continuity, writer gate post-write evidence, task authority and supersession; stop on uncertainty.
Operator-selected draft: puev5691/wellbeing-hq@8a5dc8dffd12a158f6501eacbece46b55a805246:entities/koordinator/outbox/KOO__shard-checkpoint-option-b-s1o2-nonlive-scope-draft-r01__OPERATOR.md; blob 30a8444646a84cf8eff7a7941c3b1ca5fa0a70e3.
KAN candidate: puev5691/wellbeing-hq@a3797f3877d70fc04a99dccdb71406b0193a2f0b:entities/kancelar/outbox/KAN__shard-checkpoint-governance-r01-candidate__KOO.md; blob 33f2e8f832044bbd2c77d810ddaa725ed87de100; CANDIDATE_NOT_ACTIVE.
ARH preservation review: puev5691/wellbeing-hq@cc42aae51f406e57efff9e375b432c1b710c8c75:entities/archivarius/outbox/ARH__shard-checkpoint-governance-r01-review__KOO-KAN.md; blob 740e313ca661063c69d87f9cc00a7db31bfc2234.
Existing mazhor shard gateway readback: entities/sisadmin/outbox/SIS__mazhor-shard-gateway-option-a-current-state__KOO.md; blob da804dfb646c4da25c431771c0a2f0b2b2c30ea3; VERIFY-only inactive one-shot, not checkpoint WRITE.

## One bounded task

Independently inspect repository evidence for the exact proposed one-Entity synthetic task `KOD_CHECKPOINT_SYNTH_R01`, input SHA-256 `4fdbc441ea7b546100e086ac1e4fc5ae6749b7314311c99db05be450eca12996`. Produce a non-live storage/failure-profile fit-gap matrix, not a deployment plan. For each field state VERIFIED_FROM_REPO, PROPOSED_FOR_DECISION, UNKNOWN, or BLOCKED:

- candidate storage trust boundary and failure domains; what is shown by existing mazhor VERIFY-only state and what is not;
- durable commit/ack + independently separated exact-byte readback, proposed actor duties and evidence;
- atomic object/CAS-current-pointer boundary, generation/epoch issuer and stale writer fencing, dedupe and unknown outcome reconciliation;
- retention windows for payload, manifest, required dependencies, dedupe/fence records; backup/restore and isolated restore proof;
- candidate RPO/RTO, outage window and corruption/split-brain failure responses, with absent numeric values UNKNOWN;
- least-privilege write/ack/readback principals and possible SIS operational accountability, while keeping ARH preservation and KOD author separate;
- minimum negative cases for a future *separately authorized* synthetic verification, and exact blockers for D1–D9.

Review existing evidence only. You may give multiple technical options with tradeoffs; do not choose physical host, install backend, assume key/ACL, appoint operational owner as active, assign writer, approve retention/privacy, or turn the synthetic task into an executable task. Present what exact OPERATOR decisions and independent evidence would be needed next, with one minimal next non-live step if warranted. Publish immutable readback result addressed to KOO. No implementation, live test, host access/mutation, shard write, secrets, provider calls, automatic activation, automation or Project Source/canon changes. Memory-layering attempt 3 NOT_AUTHORIZED. Historical PROMPT evidence only, never replay. Publication/dispatch/inbox do not prove receipt/activation/processing.

---
КТО: KOO / КООРДИНАТОР
КОМУ: SIS / СИСАДМИН
