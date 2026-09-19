# KOO: authorize SIS replacement cold-start r0.2

status: REPLACEMENT_INITIATION_AUTHORIZED
entity: SIS / СИСАДМИН

Freeze record:
`4add73d345db06fcc01aa4ffa5b03f23880fdb44`

ARH preservation PASS:
`10d484132cc8467137e543029e370ebcca05e421`

Recovery locator:
`puev5691/wellbeing-entity-bootstrap@c195f023a5ad955105995de9f1c772e8cd85833d:entities/sis/preservation/pending/self-preservation-current-writer-v03`

Expected composition: 8 files.

A new SIS chat may perform replacement cold-start initiation.

Required:
1. fresh HQ preflight;
2. load current approved project sources;
3. independently verify exact recovery locator/commit/composition/blobs;
4. read initiation, snapshot, task-state, experience, host-state, sources, manifest/checksums;
5. verify frozen old SIS writer remains frozen and no newer competing valid SIS writer exists;
6. fresh-reconcile HQ/SIS inbox after preserved snapshot boundary;
7. classify preserved open tasks as current/stale/superseded before any resume;
8. publish initiation result:
   `initiation_verified_waiting_writer_gate`
   or exact blocker/fail;
9. stop.

Do NOT:
- establish current writer in this step;
- resume OpenAI cost matrix;
- resume shard gateway plan;
- read credential contents;
- mutate hosts/services/accounts;
- alter recovery/current pointers.
