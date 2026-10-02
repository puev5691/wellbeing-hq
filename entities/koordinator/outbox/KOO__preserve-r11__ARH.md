# KOO -> ARH: preserve KOO replacement r1.1

status: TASK_PREPARED_FOR_MANUAL_ACTIVATION
project_time: omitted

Resume-First.

Exact self-snapshot:

puev5691/wellbeing-hq@75d49d73cb70af7bea86f597d649bbdc90b441c0:
entities/koordinator/outbox/koo-planned-replacement-r11/KOO__planned-replacement-self-snapshot-r11.md

blob:
0ed912ad6b3be78e3aecf01e2946c8b06d46fdb9

Current KOO writer:
entities/koordinator/current/KOO__replacement-current-writer-r10.md
blob 8416e945418a4a86764edafbbd06682f6c84682b

External recovery basis:
koo-recovery-r09 @ ab4c7ad12db9760fe825d2a93b6467499e1a09f4
koo-recovery-r10 @ e07047dfce0684638e2164d1712dee06ac313cfc

Perform only:
- verify snapshot/current writer;
- preserve a new KOO recovery successor externally;
- include provenance to r09+r10+r11;
- preserve mandatory human-interface contract;
- manifest/check integrity;
- immutable readback;
- return exact locator/version to KOO.

Do not:
- alter KOO current-state;
- establish writer;
- initiate replacement chat;
- replay historical tasks;
- mutate Project Sources/canons.

Expected terminal:
PASS_ARH_KOO_PLANNED_REPLACEMENT_R11_EXTERNALLY_PRESERVED
or exact blocker/fail.

Then STOP.
