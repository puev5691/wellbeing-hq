# GWR-CONTOUR-RETIRE-R01

status: AUTHORIZED_DORMANT
decision: AUTHORIZE_GWR_CONTOUR_RETIRE_R01
project_time: omitted
host: p552203.kvmvps
legacy_contour: wellbeing-shard-gateway

Purpose:
finish retirement of the exact legacy wellbeing-shard-gateway contour without per-file OPERATOR decisions, while preserving fail-closed object admission and preservation requirements.

Mutation allowlist:
- /etc/systemd/system/wellbeing-shard-gateway-verify.service
- /opt/wb-shard-gateway
- /run/wb-shard-gateway
- /var/lib/wellbeing/shard-gateway
- /var/log/wb-shard-gateway

Required per-object chain:
INSPECT -> CLASSIFY -> PRESERVE -> ADMIT -> PRE-MUTATION REVERIFY -> RETIRE -> VERIFY

DURABLE_STATE_OR_DATA / AUDIT_EVIDENCE:
immutable byte-preservation + exact locator + immutable identity + integrity/readback + rollback/recoverability evidence are mandatory before mutation.

After preservation and admission, no separate OPERATOR decision is required for individual residual objects inside this contour.

Fail closed on:
ACTIVE_DEPENDENCY
SECRET_OR_SENSITIVE
UNKNOWN
OUT_OF_SCOPE
writer/host/task mismatch
symlink/mount/path escape
object identity change requiring reclassification
preservation/recoverability failure
need for mutation outside allowlist

Recursive/container retirement is permitted only when every removed descendant is inspected, classified, preserved where required, admitted, and not ACTIVE/UNKNOWN/SENSITIVE/OUT_OF_SCOPE.

No wildcard/recursive deletion over unclassified content.

After old unit removal, systemd daemon-reload is permitted if required.

Explicitly excluded:
- /data/wellbeing-lab mutation
- proof roots
- backend
- T01-T20
- CHECKPOINT_DURABLE
- memory-layering attempt 3
- Telegram/provider/credential contours
- Project Sources/canons
- other hosts/services
- reset/reimage

Completion:
if the whole legacy contour is verified retired:
RETIREMENT_COMPLETE_CONSUMED

After consumption this authority does not apply to future objects that later appear at the same paths.

This authority supersedes the need for the pending per-object audit.jsonl decision gate, but does not replay any consumed historical task.
