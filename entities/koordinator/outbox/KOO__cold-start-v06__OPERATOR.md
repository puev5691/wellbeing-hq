# KOO: authorize replacement cold-start v0.6

status: REPLACEMENT_INITIATION_AUTHORIZED
entity: KOO / КООРДИНАТОР

Freeze record:
`865308a1aa50724991e77b1334897510d36c1d92`

ARH preservation PASS:
`5756d83016f60ab4d50be99bf67540910635a20c`

Recovery locator:
`puev5691/wellbeing-entity-bootstrap@cf8e538248fdc3e6abfa7125f8681e10bd68253b:entities/koo/preservation/pending/self-preservation-current-writer-v06`

Expected composition: exactly 8 files.

A new KOO chat may perform replacement cold-start initiation.

Required:
1. fresh `puev5691/wellbeing-hq` preflight;
2. load and fresh-verify current approved project sources;
3. verify exact recovery locator, commit, 8-file composition, blobs and checksums;
4. verify old KOO v0.5 writer remains frozen;
5. verify no newer competing valid KOO current-writer exists;
6. fresh-reconcile HQ, KOO inbox and all terminal results newer than queue boundary `8ce084124833a0e80b9b3bde08942f468ea4036b`;
7. classify preserved tasks as current / completed / blocked / superseded;
8. publish:
   `initiation_verified_waiting_writer_gate`
   or exact blocker/fail;
9. stop.

Do NOT:
- establish current writer in this step;
- resume routing/profile work;
- issue provider or Telegram live authority;
- read credential contents;
- mutate external hosts/services/accounts;
- alter recovery/current pointers.
