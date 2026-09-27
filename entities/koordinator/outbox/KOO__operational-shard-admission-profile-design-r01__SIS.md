# KOO → SIS: operational shard admission profile design r0.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
recipient: SIS / СИСАДМИН r0.6
scope: DOCUMENT_ONLY_ADMISSION_PROFILE_DESIGN
project_time: omitted

Exact authority:
puev5691/wellbeing-hq@bb79c50ed20b789e620eb4acfdcee6f62c25409e:
entities/koordinator/outbox/KOO__authorize-SIS-operational-shard-admission-profile-design-r01__OPERATOR.md

Exact reviewed offline candidate:
puev5691/wellbeing-hq@9faa1ede62460fdcc073e48fd13b10f93027e957:
entities/koder/outbox/operational-shard-store-offline-r02
tree 8c5cb47ce3267dac4b1810e93cf993a35a3a0492

Independent review basis:
SIS:
puev5691/wellbeing-hq@92038724366a4fb7e54c2e3014b70445bf28ae16
terminal PASS_SIS_OPERATIONAL_SHARD_STORE_OFFLINE_R02_REREVIEW

SHD:
puev5691/wellbeing-hq@a76dfcea52627cbe73fe8b29abc152c3b3f25404
terminal PASS_SHD_OPERATIONAL_SHARD_STORE_OFFLINE_R02_REREVIEW

SHT:
puev5691/wellbeing-hq@79a351255020a4a94b007117abefbb087bb59880
terminal PASS_SHT_OPERATIONAL_SHARD_STORE_OFFLINE_R02_BOUNDARY_REVIEW

Design one concrete admission-profile candidate only.

## Required sections

1. SupervisorTrustProfile
- possible owner/issuer models;
- authentication root options;
- scope/version/revocation semantics;
- which facts remain UNKNOWN.

2. WriterFenceAttestation / epoch authority
- attestor candidates;
- monotonic epoch issuance;
- freeze/replacement interaction;
- revocation channel;
- replay/staleness handling.

3. Currentness / freshness
- what must be checked before mutation;
- candidate freshness model;
- failure behavior when canonical authority is unavailable;
- no fail-open cache.

4. Backend candidates
- suitable backend classes only;
- transaction/CAS/WAL/fsync requirements;
- fault-domain implications;
- what evidence would be needed before selecting one.

5. Store owner/operator
- role boundary;
- process identity;
- separation from requester/verifier/publisher;
- credential/secret custody boundary.

6. Isolation
- requester;
- attestor;
- mutation service;
- read-only verifier;
- File/Artifact Service;
- GitHub publisher;
- prohibited capability sharing.

7. Retention / GC
- required policy fields;
- holds;
- unresolved CAS evidence;
- orphan objects;
- canonical anchors;
- deletion preconditions;
- explicitly UNKNOWN numerical durations unless sourced/approved.

8. Canonical-unavailable behavior
- exact fail-closed states;
- what provisional work may or may not continue;
- what can never be claimed.

9. Future live-admission prerequisites
List exact evidence/decisions that would be required before KOO could even open a bounded live-admission decision.

10. Decision table for OPERATOR
For each unresolved governance choice:
- option;
- consequence;
- evidence needed;
- decision owner;
- current status UNKNOWN/CANDIDATE.

## Hard boundaries

Do not:
- appoint trust root;
- select backend as active;
- appoint operator/service account;
- create credentials;
- deploy;
- mutate host;
- enable live WRITE/CAS;
- claim production durability;
- claim CHECKPOINT_DURABLE;
- run EOM pilot;
- run memory-layering attempt 3;
- activate Project Source/canon.

Return one standalone immutable design candidate to KOO with exact readback.

Expected terminal:

PASS_SIS_OPERATIONAL_SHARD_ADMISSION_PROFILE_DESIGN_R01_READY_FOR_REVIEW

or exact BLOCKED_* / FAIL_*.

After immutable result + exact readback + return KOO, STOP.
