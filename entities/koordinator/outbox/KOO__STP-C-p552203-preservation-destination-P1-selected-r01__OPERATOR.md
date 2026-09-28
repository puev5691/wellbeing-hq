# KOO record: OPERATOR selects P1 GitHub non-secret preservation destination

status: OPERATOR_PRESERVATION_DESTINATION_P1_SELECTED
project_time: omitted

Exact OPERATOR token:

SELECT_P552203_PRESERVATION_DESTINATION_P1_GITHUB_NONSECRET_PACKAGE

Exact disposition approval:
puev5691/wellbeing-hq@9388ef9ceee58a3837f48ac6e69e2c197a86dade:
entities/koordinator/outbox/KOO__STP-C-p552203-preservation-disposition-approved-r01__OPERATOR.md

Meaning:
- preserve the approved non-secret preservation set into an immutable project-controlled GitHub package;
- checksum manifest + immutable commit + exact readback required;
- secret-bearing or ambiguous content fails closed and must not be published;
- preservation destination must survive p552203 reset.

Selected exact project package root for the bounded preservation task:
entities/sisadmin/outbox/p552203-stpc-preservation-r01/

This selection does NOT authorize:
- deleting/moving source data;
- resetting/reimaging p552203;
- proof-root creation;
- service retirement/removal;
- backend install/run;
- T01-T20 execution.
