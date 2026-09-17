# KOO → OPERATOR: KOD source-gate remediation v0.1

status: `SOURCE_GATE_BYTES_VERIFIED_5_OF_5`
production: `no`
live_provider_calls: `no`
credentials: `no`
project_time: omitted; trusted project-time source not used

## Основание

Новый экземпляр KOD остановил emergency initiation v0.3 с:
`BLOCKED_APPROVED_PROJECT_SOURCES_UNAVAILABLE`.

Его отчёт указал четыре недоступных approved-текста и ожидаемые SHA-256. В текущем Project context у КОО доступны полные байты всех пяти approved Project Sources.

## Bytewise verification

Локально вычисленные SHA-256:

- `project-instructions-core-v2_1-approved.md`
  `8a86945c28e361b5adf7ecc96326a1591a193118ce7be258a9c0a21ddd2ace26`
- `file-work-canon-universal-v2_3-approved.md`
  `5ec75e480c0b78a72bb2faa702a21064b32bd3b919b225b1ae25a30dd0a700e5`
- `source-loading-policy-v2-approved.md`
  `2661a3a266547a5e0f6b70c3dab8a02add2bb788b4a90b1136b7e9445b2d6061`
- `entity-state-preservation-and-recovery-canon-v1_4-approved.md`
  `984871a22aab1910fc4ab3217c16488eac1e472734bdfd1948fd57c213566fda`
- `entity-roles-short-v2_3-approved.md`
  `e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a`

Result: `5/5 PASS`.

These identities exactly match the expected identities recorded by the blocked KOD report.

## Delivery package

A standalone source-gate package was created for OPERATOR-mediated file transfer into the replacement KOD chat:

`KOD_source_gate_pack_v01.tar.gz`

Archive SHA-256:
`72f005ff6e95a37ea72ff5ddedac8c3b39fa04cea7a92989afe340a999331b8a`

Contents:
- five exact approved source files under canonical names;
- `SHA256SUMS.txt`;
- `README.md` with retry boundary.

The package is a transport/remediation package only. It does not create or amend canon.

## Required continuation

Replacement KOD should:
1. verify archive identity if available;
2. extract/read five approved source files;
3. run `sha256sum -c SHA256SUMS.txt` and require 5/5 PASS;
4. repeat source-loading gate;
5. continue the existing emergency initiation v0.3 from canonical recovery readback/checksums, fresh HQ reconciliation and competing-writer check;
6. establish replacement current-writer only after `initiation_verified` and existing emergency authority verification;
7. stop after writer establishment;
8. keep the incomplete three-model implementation as `UNFINISHED_UNACCEPTED_EVIDENCE_TAIL` for a later separate profile cycle.

No provider call, API key handling, billing mutation, production deployment or TERA2/WBN execution is authorized by this remediation.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: устранить транспортную недоступность approved Project Sources для emergency initiation KOD v0.3
СТАТУС: `SOURCE_GATE_REMEDIATION_READY_V01`
