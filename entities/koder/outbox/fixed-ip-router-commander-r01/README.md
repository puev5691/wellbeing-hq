# Fixed-IP router → Remote Desktop Commander selection r0.1

This is a **non-deployed, operator-assisted integration candidate**. It turns independently verified fixed-IP route evidence into one exact Commander device selection descriptor. It does not call Commander, acquire credentials or execute a host command. Any administrative action still needs its own exact authority and explicit operator invocation.

## Evidence and exact mapping

| Logical node | Host name | Commander device ID | Project evidence |
| --- | --- | --- | --- |
| burzh | `ruvds-xnqc6` | `dd09a197-f716-4dd6-80bb-7f8e5d8260ff` | SIS Telegram direct-message diagnostic, blob `734146576f35942c6b584b898c83129521a7bc2a` |
| mazhor | `p552203.kvmvps` | `830038a0-232b-4d83-b52d-0e9973126165` | SIS mazhor host access pilot, blob `c895f72b6cb6cd99d4d7abe93f49201f965f56ec` |
| erefia | `ruvds-ygo0w` | `c55d5659-f2c8-416d-8b40-9bac8c80c30d` | SIS Erefia access readiness, blob `424bfba42d385e056552ef3528205d61cb9c3447` |

The IDs are historical independently documented identities. This package does not claim a fresh Commander inventory or current availability. `mapping.current.json` therefore says `IDENTITY_FROM_PUBLISHED_EVIDENCE_CURRENT_AVAILABILITY_UNKNOWN`. An independently verified current inventory of the **selected** device is a required input before readiness. No substitution by hostname or guessed ID.

Existing router package tree: `fc1bb2751cc5d662037a037fdecf3ece69f07adb`; measured profile SHA-256: `b459ea79e31ddba2d36b96872c64a201c001ed6ba4bac8f4f05dd019d7df17ac`. Current KOO policy: `OPERATOR_ASSISTED_ACTIVE_NO_AUTO_FAILOVER`. This package only reads route evidence; it does not activate its own router or alter an IP/profile.

## Three independent gates

1. **Route selection evidence.** Supervisor supplies a verified observation from the exact router package/profile and an explicit manual node choice. For a second IP, the trace must first contain `TARGET_IP_FAILURE` for the first. `TLS_CERTIFICATE_FAILURE` and transport failure do not establish readiness. `HTTP_APPLICATION_RESPONSE`, including 403/429/5xx, establishes transport/TLS reachability only, not application authorization.
2. **Commander selection.** Exact mapping bytes/digest and current independently verified Commander inventory must agree on selected device ID and host. An unavailable device produces `COMMANDER_DEVICE_UNAVAILABLE`; it never causes selection of a different device. The output contains the exact device ID for an operator to select, not a host command.
3. **Task authority.** A different supervisor must verify authority for the exact action ID, node, device and scope, then obtain explicit operator confirmation. Merely producing `CONTROL_PATH_READY` at selection gate is not permission to mutate a host. `gate_action` returns only a descriptor, never an execution request with command payload. A future Commander invocation needs its own per-task admission and is outside this package.

The local `verified_by_supervisor` fixture boolean is an **interface placeholder**, not a trust root. A caller-controlled JSON claim can be forged. SIS must define and independently verify the actual authority/currentness source and inventory provenance before integration can be relied upon in an operational control path. The CLI below is deliberately offline and may be used only with synthetic fixtures.

## State machine

| State | Meaning / action |
| --- | --- |
| `ROUTE_NOT_HEALTHY` | Missing, stale/mismatched or unhealthy exact router evidence; stop. Certificate failure always stops. |
| `COMMANDER_DEVICE_UNKNOWN` | Unknown node or mismatched/missing device ID, host or inventory evidence; stop. |
| `COMMANDER_DEVICE_UNAVAILABLE` | Exact selected device is unavailable; stop. No automatic next device. |
| `TASK_AUTHORITY_MISSING` | Selection may be ready, but no verified authority for the requested administrative action. No execution. |
| `CONTROL_PATH_READY` | Exact node/device selection prepared, or separate action gate claims authority plus manual confirmation. Still no host execution in this package. |
| `CONTROL_PATH_EXECUTION_BLOCKED` | Missing manual marker/confirmation, mismatched authority/action, or attempt to execute from a failed selection; stop. |

The audit envelope contains only selected logical node, exact device ID, selected IP, 40-hex health evidence reference, explicit `OPERATOR_SELECTED:<node>` marker, requested action identifier and outcome. No credentials, URL, command body, private request or host output. Evidence references are opaque exact identities; their independent provenance remains an external verification duty.

## Offline verification

With Python 3.10+ from this directory:

```sh
python -m unittest -v test_integration.py
python offline_cli.py --mapping mapping.current.json --mapping-sha256 3a48b6224e074b657a94907c276605fb34db369d1ac3ca762773970b44916e7c --fixture fixtures/operator-selection.synthetic.json
sha256sum -c SHA256SUMS.txt
```

The CLI fixture is synthetic and deliberately has no task authority. Expected outcome is `TASK_AUTHORITY_MISSING` even though its mocked route result is HTTP 403 and the synthetic Commander device is marked available. An operator must not paste fixture output into a live Commander invocation.

Tests cover three mappings, unknown node and ID, route failure, TLS failure, HTTP 403/429/5xx, first-IP failure requirement for second IP, missing/mismatched task authority, explicit manual selection, unavailable device without fallback, mapping/profile mismatch, closed audit and mocks proving no socket/subprocess use by planner. No provider/API/DNS/Commander calls occurred.

## Future SIS review and runbook boundary

SIS independently checks exact package bytes, published evidence for all three device IDs, mapping hash, external route/inventory provenance, authority verifier, audit controls and negative cases. A separately authorized bounded integration may use the **exact selected device ID** in the existing Commander operator interface, after fresh inventory and action authority. Neither task-level host mutation nor a generic Commander command executor is granted by this package.

Before later integration, record current Commander inventory, permissions, control interface, router package state and per-node host/service state as exact pre-state. A separately approved rollout must define immutable installed bytes and rollback that removes only the new integration while preserving the operator-assisted router and other Commander configuration. No pre-state was collected here; no rollback action was executed.

No automatic failover, autonomous node switching, IP discovery/admission, DNS fallback, credential use, provider/API call, shard WRITE, automation or Project Sources/canon change, CHECKPOINT_DURABLE claim, resume authority or memory-layering attempt 3.
