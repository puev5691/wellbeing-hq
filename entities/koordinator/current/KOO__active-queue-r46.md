# KOO current active queue r0.46

status: CURRENT_QUEUE
writer: `entities/koordinator/current/KOO__replacement-current-writer-v06.md`
writer_commit: `525e5b131472e61b1f55db5ef7307217aea4c4fc`
writer_gate_pass: `06dd7873b532c1fe86f4b382d40c26908a5a11b2`
project_time: omitted; trusted project-time source not used

## Fresh reconciliation

Previous queue:
`entities/koordinator/current/KOO__active-queue-r45.md`
commit `908d08c9da258688aee720889b45db984c779c43`.

New SHT terminal result:
`entities/shtabist/outbox/SHT__source-rebuild-r03-narrow-recheck__KOO.md`
commit `8949ec92965d8b8ed3835007de04a104ee402262`
blob `cd64946979a22cd30f9523246cb2811ef1f64b82`
verdict `PASS_SHT_SOURCE_REBUILD_R03_READY_FOR_RECOVERY_REVIEW`.

KOO inbox:
`entities/koordinator/inbox/SHT__source-rebuild-r03-narrow-recheck__KOO.md`
is addressed_for_processing only.

Inbox placement != receipt != acceptance != recovery review != processing_started.

SHT PASS is current and no newer source-rebuild result supersedes it.

Historical task replay: none.

## ACTIVE SLOT 1 — ARH / SOURCE REBUILD R0.3 RECOVERY REVIEW

Owner:
ARH / АРХИВАРИУС.

Owner basis:
preservation/recovery process, provenance, source lifecycle and information-field stewardship.

Current ARH writer lineage:
`entities/archivarius/current/ARH__replacement-current-writer-r01.md`
establishment commit `a00b1644e840bed722e3712e78c8842959599797`
current blob `3d17b16c02e84e841d1266e3b0fcc083640b77d6`.

Exact task:
`entities/koordinator/outbox/KOO__source-rebuild-r03-recovery-review__ARH.md`
commit `8c90b29e89f888076bef7c22730d378d276cac9c`
blob `f6903919be48cbff958882c58af811f5636428a9`.

Dispatch:
`routes/dispatch/KOO__source-rebuild-r03-recovery-review__ARH.md`
commit `57f47c4c128cbf0c8f319b8bbf68ef61d628ed51`.

ARH inbox:
`entities/archivarius/inbox/KOO__source-rebuild-r03-recovery-review__ARH.md`
commit `25b0e54d8c1d7a077a145e97637d68ee0a3c5cfb`.

Sender registry:
`74b31c4ec6d73a6b3b3cad97cbcae1bcec5adba2`.

Automatic activation boundary:
`93e6e1ab8879945d9328ecab9ae3432ed2d14e91`.

Activation status:
`activation_failed`.

processing_started:
`no`.

operator_manual_ping_required:
`yes`.

State:
`AWAITING_OPERATOR_TRANSFER`.

## Exact immutable review input

Candidate locator:
`puev5691/wellbeing-hq@316fe7ac638b9ed7bc422f2cbf1a720ca6197b10:entities/koordinator/outbox/source-rebuild-r03`

Boundary commit:
`316fe7ac638b9ed7bc422f2cbf1a720ca6197b10`.

Boundary tree:
`e8cd47baec0be6accca0fa2968187aefa75b18ed`.

Composition:
exactly 7 files.

SHT PASS:
`8949ec92965d8b8ed3835007de04a104ee402262`.

ARH must read exact candidate bytes from the shared info field. No physical candidate-artifact transfer by OPERATOR is required.

## OPEN GATES — unchanged

Recovery v1.5 r0.4 OPERATOR gate:
`17190f729eef6537f0404af387253c9c11eb3a21`.

Source-loading-policy v2.1 OPERATOR gate:
`b15a9250e72e7bb5da4efabd027fa4e43386022e`.

Both remain OPEN / UNRESOLVED.

Project Sources approval:
`NO`.

Project Sources activation:
`NO`.

## PENDING PARALLEL — KOD SHARD GATEWAY ADAPTER INDEPENDENT VERIFY

KOD terminal PASS:
`abe67edb9fbca9201d4a107761c835a696946591`.

Required reviewers:
SIS + ARH.

State:
`CURRENT_PENDING_NOT_ACTIVE`.

Do not mix this technical review with the source-rebuild recovery review.

## EXACT NEXT CAUSAL STATE

`ARH_SOURCE_REBUILD_R03_RECOVERY_REVIEW_AWAITING_OPERATOR_ACTIVATION`

Required OPERATOR action:
transfer the prepared activation PROMPT to the ARH chat only.

No candidate ZIP/files need to be transferred.

After ARH terminal result:
fresh-reconcile before deciding any further source-review/approval step.

---
КТО: replacement KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: Resume-First routing after SHT r0.3 PASS
СТАТУС: CURRENT_QUEUE
