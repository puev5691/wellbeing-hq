# KOO → OPERATOR: p552203 preservation destination decision r0.1

status: WAITING_OPERATOR_DECISION
project_time: omitted

Current approved preservation set:
- /data/wellbeing-lab/backups/shd-pre-reinit-v01
- /data/wellbeing-lab/reports
- /opt/wb-shard-gateway

Exact disposition approval:
puev5691/wellbeing-hq@9388ef9ceee58a3837f48ac6e69e2c197a86dade:
entities/koordinator/outbox/KOO__STP-C-p552203-preservation-disposition-approved-r01__OPERATOR.md

No copy is authorized yet.

Select one destination class.

## P1 — immutable non-secret GitHub preservation package

Token:
SELECT_P552203_PRESERVATION_DESTINATION_P1_GITHUB_NONSECRET_PACKAGE

Meaning:
- SIS/KOD may later prepare an exact preservation package from only the approved non-secret preservation set;
- before publication, package must be scanned/verified for absence of secret material;
- publication target must be an exact project-controlled GitHub locator chosen in the subsequent bounded copy task;
- checksum manifest + immutable commit + exact readback required;
- if any secret-bearing content is discovered, STOP.

Pros:
- independently survives p552203 reset;
- exact immutable identity/readback is easy to prove.

Boundary:
does not yet choose exact repository/path or authorize copy/publication.

## P3 — separate OPERATOR-controlled host/device/archive

Token:
SELECT_P552203_PRESERVATION_DESTINATION_P3_EXTERNAL_ARCHIVE

Meaning:
- preserve the approved set to a separately identified host/device/archive outside p552203;
- exact target locator/device identity must be supplied/verified before copy;
- checksum manifest + exact readback required;
- secret-bearing material still fails closed.

Boundary:
does not yet identify or authorize a specific target.

## Defer

Token:
DEFER_P552203_PRESERVATION_DESTINATION_DECISION

No mutation follows from any token by itself.
A separate PRESERVATION_COPY_R01 authority is required after the destination is pinned.
