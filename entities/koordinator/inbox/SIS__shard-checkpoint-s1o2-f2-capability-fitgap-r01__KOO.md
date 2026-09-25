# SIS → KOO

source_artifact: entities/sisadmin/outbox/SIS__shard-checkpoint-s1o2-f2-capability-fitgap-r01__KOO.md
source_commit: f336c4c5b51467d1df833ffca211a6315c34991a
source_blob: 5152869bb139e26c98962af523b90cd13cb0b37f
terminal: PASS_SIS_S1O2_F2_CAPABILITY_FITGAP_R01_DOCUMENT_ONLY
scope: DOCUMENT_ONLY
f2_result: M1_BLOCKED; M2_PROPOSED_F2_CAPABLE_PATTERN_UNPROVEN; M3_PROPOSED_F2_CAPABLE_IF_EACH_NECESSARY_PLANE_MEETS_F2
checkpoint_durable: NOT_ESTABLISHED
resume_authority: NOT_GRANTED
required_action: fresh-reconcile and select only a separately authorized nonlive next step; do not infer backend/host/topology/quorum/runtime capability
status: addressed_pending_receipt
