# SIS-GWR-MAINT-R01 — reusable bounded authority candidate for p552203 gateway residue maintenance

status: CANDIDATE_NOT_ACTIVE
entity_scope: SIS / СИСАДМИН current-writer only
host_scope: p552203.kvmvps only
project_time: omitted

## Human meaning

This candidate replaces repeated one-file-at-a-time authority requests for residual objects belonging to the retired wellbeing-shard-gateway contour on p552203.

It proposes one reusable bounded maintenance authority for current SIS to run the same standard fail-closed chain:

inspect -> classify -> retire -> verify

only inside a closed allowlist of gateway paths.

It does not authorize unrelated maintenance, proof execution, backend work or any other project contour.

## Exact motivation / current blocker

Fresh current blocker:

puev5691/wellbeing-hq@1cbbb48c6eb1cbef9f39e7d4dff963d773a53e26

terminal:
BLOCKED_SIS_P552203_REQUEST_JSON_AND_GATEWAY_RETIREMENT_R02_LOG_DIR_NONEMPTY

Current observed next residue scope includes non-empty:
/var/log/wb-shard-gateway

No mutation occurred in that blocked attempt.

## Proposed reusable authority ID

SIS-GWR-MAINT-R01

Meaning:
SIS Gateway Residue Maintenance r0.1

## Closed host scope

Only exact host:
p552203.kvmvps

SIS must fresh-verify host identity before every maintenance cycle.

Host mismatch:
STOP.

## Closed path allowlist

Only these exact paths and descendants where explicitly applicable:

1. /etc/systemd/system/wellbeing-shard-gateway-verify.service
2. /opt/wb-shard-gateway
3. /var/lib/wellbeing/shard-gateway
4. /run/wb-shard-gateway
5. /var/log/wb-shard-gateway

No path outside this allowlist may be inspected beyond minimal dependency tracing, and no path outside this allowlist may be mutated.

Symlink/path escape outside allowlist:
STOP.

## Standard cycle

Each cycle must be:

1. INSPECT
2. CLASSIFY
3. RETIRE only if exact classification permits
4. VERIFY
5. immutable result/readback

No cycle may skip directly to RETIRE.

## Stable helper contract: SIS-GWR-INSPECT

Purpose:
bounded read-only evidence collection inside the closed allowlist.

May collect only what is necessary to classify residue:
- exact entries;
- file type;
- size;
- owner/group;
- mode;
- inode/link metadata;
- filesystem timestamps as metadata only;
- open-file references;
- socket references;
- process references;
- systemd references;
- safe content inspection only when needed and non-secret;
- symlink target/path containment check.

Classification values:

ACTIVE_DEPENDENCY
STALE_RETIRABLE_CANDIDATE
SECRET_OR_SENSITIVE
UNKNOWN
OUT_OF_SCOPE

Rules:
- SECRET_OR_SENSITIVE => STOP, no raw secret disclosure, no retire.
- UNKNOWN => STOP, no retire.
- ACTIVE_DEPENDENCY => STOP, no retire.
- OUT_OF_SCOPE => STOP.
- only STALE_RETIRABLE_CANDIDATE may proceed to SIS-GWR-RETIRE.

SIS-GWR-INSPECT performs zero mutation.

## Stable helper contract: SIS-GWR-RETIRE

Purpose:
remove only objects already classified STALE_RETIRABLE_CANDIDATE inside the closed allowlist.

Before mutation, repeat critical freshness checks:
- current SIS writer;
- exact host identity;
- service/dependency state;
- object identity/path still matches inspected candidate;
- no new process/open-file/socket/systemd consumer;
- no new symlink/path escape;
- no newer superseding result/authority;
- exact object remains within closed allowlist.

If any freshness check fails or becomes UNKNOWN:
STOP before mutation.

Permitted actions, only within allowlist:
- remove exact stale file(s)/directory entries classified by current cycle;
- remove exact old unit file if classified stale and dependency-free;
- remove exact /opt/wb-shard-gateway tree only if every contained object is classified within current or prior still-fresh bounded evidence and no active dependency exists;
- remove runtime/log/data directories only when their remaining contents are all classified stale-retirable and no active dependency exists;
- run systemd daemon-reload only if unit removal requires it.

No wildcard deletion across unknown contents.
No recursive deletion before classification of contained objects.

## Mandatory fail-closed STOP conditions

STOP entire cycle on any:

- current SIS writer mismatch/freeze/replacement;
- host mismatch;
- path outside allowlist;
- symlink escape;
- active process/open-file/socket/systemd dependency;
- SECRET_OR_SENSITIVE;
- UNKNOWN object or unknown ownership/use relevant to safe retirement;
- object changed after inspection;
- unexpected object appears before retire;
- required evidence unavailable;
- helper output malformed/incomplete;
- superseding authority/result/task;
- need to touch unrelated path;
- ambiguity whether object belongs to old gateway contour.

STOP means:
no further mutation in that cycle.

## Reusability boundary

If OPERATOR later activates SIS-GWR-MAINT-R01, current SIS may repeat the standard cycle on newly discovered residue within the same closed allowlist without requesting a new authority for each individual residual file.

Each cycle still requires:
- fresh Resume-First;
- current-writer verification;
- host verification;
- helper-based inspect/classify/retire/verify;
- immutable result/readback.

Reusable authority does NOT mean unattended execution or automatic activation.

## Operator-assisted privileged path

Where SIS tooling cannot perform required root-level inspect/retire directly, SIS may provide OPERATOR one exact self-contained privileged block implementing the helper contract for that cycle.

OPERATOR execution is transport/execution assistance only.
It does not expand scope.

## Explicitly excluded

SIS-GWR-MAINT-R01 grants no authority for:

- /data/wellbeing-lab mutation;
- proof roots;
- backend selection/install/run;
- T01-T20;
- CHECKPOINT_DURABLE;
- memory-layering attempt 3;
- Telegram;
- provider credentials/API;
- Project Sources/canons;
- other services/hosts;
- reset/reimage;
- arbitrary system cleanup.

## Helper stability

Stable helper names:

SIS-GWR-INSPECT
SIS-GWR-RETIRE

Future helper implementation may change internally only under its own reviewed/versioned implementation authority.

The names here define contract roles, not executable code identities.

No helper implementation is authorized by this candidate.

## Result classes

Each maintenance cycle returns one:

PASS_SIS_GWR_MAINT_CYCLE_COMPLETE

BLOCKED_SIS_GWR_MAINT_<reason>

FAIL_SIS_GWR_MAINT_<reason>

Result must include:
- inspected scope;
- classifications;
- mutations actually performed;
- verification;
- remaining residue;
- whether another cycle is needed.

## Effectivity boundary

This file is only a candidate.

It does NOT:
- activate SIS-GWR-MAINT-R01;
- authorize helper implementation;
- authorize automation;
- create background maintenance authority;
- change Project Sources/canons.

Separate OPERATOR decision is required for activation.

## Proposed OPERATOR decision

AUTHORIZE_SIS_GWR_MAINT_R01_REUSABLE_BOUNDED_AUTHORITY_P552203

Meaning:
activate exactly this reusable bounded authority for current SIS on p552203 under the closed path allowlist and fail-closed rules above.

Alternative:
HOLD_SIS_GWR_MAINT_R01

## Terminal

CANDIDATE_SIS_GWR_MAINT_R01_READY_FOR_OPERATOR_DECISION
