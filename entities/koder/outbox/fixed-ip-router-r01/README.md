# Fixed-IP administration router r0.1 — review package

This is a **non-deployed implementation package** for independent SIS review. It does not create a project administration route, node control plane, operational admission, or automatic failover authority.

## Contents and scope

| File | Purpose |
| --- | --- |
| `router.py` | Strict profile parsing, digest/current-generation comparison, deterministic route state machine, closed audit output. |
| `node_probe.py` | Candidate node-local HTTPS HEAD probe; fixed numeric IPv4 destination, SNI/Host/certificate name `chatgpt.com`. It was **not run live**. |
| `offline_cli.py` | Offline fixture route plan and manual start-node interface; no live/network option. |
| `profile.schema.json` | Closed versioned candidate profile schema. Runtime parser also validates exact identity and fixed node order. |
| `profile.current.json` | Exact measured node/IP profile with `DOCUMENTED_CURRENT_MEASURED_SET`, which admission **rejects** as operational. |
| `fixtures/` | Synthetic admitted clone, digest comparison record and observations for offline demonstration; not real authority. |
| `test_router.py` | Synthetic unit tests, including a mocked probe preserving numeric destination, SNI/Host and certificate validation. |
| `MANIFEST.md`, `SHA256SUMS.txt` | Package inventory and byte checksums. |

## State machine and classification

After an independently verified profile/admission, inspect nodes in immutable priority order `burzh → mazhor → erefia`. Within a node, inspect `104.18.32.47` then `172.64.155.209`. No latency-only switch or DNS discovery changes this order.

| Observation | Action |
| --- | --- |
| `HEALTHY` or `HTTP_APPLICATION_RESPONSE` (including 403/429/5xx) | Select this node/IP; stop. HTTP status remains in closed audit. Application usability is a separate policy. |
| `TARGET_IP_FAILURE` | Try the other admitted IP on the same node. After both fail, try the next node. |
| `NODE_FAILURE` | Node/control path unavailable; skip its other IP, try the next node. This outcome must be supplied by a separately verified node adapter. |
| `TLS_CERTIFICATE_FAILURE` | Stop route with identity failure. Do not disable certificate checking or silently switch to another IP/node. |
| Missing observation | `MISSING_OBSERVATION` blocker; no optimistic success. |
| All admitted IPs/nodes fail | `FIXED_IP_SET_EXHAUSTED`; stop. No DNS fallback. |

Application redirects are reported as HTTP application responses; this package does not follow redirects. A TLS handshake failure other than certificate verification is a target-IP failure. The local adapter reads only a bounded status line and does not read a response body. It uses a bounded timeout; retries and fallback are absent. The local adapter never receives credentials.

## Offline reproducibility

From this directory, with Python 3.10+:

```sh
python -m unittest -v test_router.py
python offline_cli.py --profile fixtures/profile.synthetic-admitted.json --admission fixtures/admission.synthetic.json --observations fixtures/observations.synthetic.json
python offline_cli.py --profile fixtures/profile.synthetic-admitted.json --admission fixtures/admission.synthetic.json --observations fixtures/observations.synthetic.json --manual-node mazhor
sha256sum -c SHA256SUMS.txt
```

These commands use synthetic records only. The second command selects the other admitted IP on `burzh` after one synthetic failure and records HTTP 403 as an application response. The third command explicitly begins at `mazhor` and records the manual override. The `profile.current.json` is intentionally *not* usable with the synthetic admission: its status is documentary, not operational.

## Admission and successor profiles

The offline `admission.synthetic.json` is **not a trust source**. A future supervisor must independently verify exact immutable profile bytes/digest, approval/authority, current generation, supersession/revocation, node identity, executable identity, controlled observations and operation budget. It must pass independently verified claims to `admit` and prevent caller-forged observations. The pure planner does not verify signatures, reach other hosts, or confer permission. The node-local probe alone cannot attest its host or orchestrate remote execution. SIS must review and specify the authenticated node adapter/control path before deployment. No arbitrary SSH or node credential behavior is included.

A stale profile, unadmitted successor, mismatching digest or generation is rejected before route selection. Discovery and independent validation of new IPs remain separate work. A successor creates new immutable bytes and requires its own independent admission; the measured fixture is never edited in place. No automatic admission, DNS lookup, fallback to hostname transport, or profile refresh exists.

## Manual failover interface

`offline_cli.py --manual-node mazhor` (or `erefia`) skips earlier nodes only for that explicit offline plan; node order and profile bytes remain unchanged. The closed trace records the selected node/IP, observation class, HTTP status when present and profile digest. An actual manual switch in an operational service requires a separate authorized supervisor command, verified node identity and audit. This package does not make that switch.

## Later SIS review and rollout boundary

SIS should independently inspect code bytes, schema/fixture identities and tests, verify the node-local network/TLS behavior in an *independently authorized* bounded environment, and assess authenticated node execution, profile authority/currentness and audit containment. These are not proven by local mocks. Burzh and Mazhor medians were close in the historical 60-request measurement, so the priority is a current deterministic policy, not a permanent latency fact. The IP set can become stale.

Before any later installation, independently record exact existing per-node files, config, service, routing, active listeners, checksums and status as pre-state. A separately authorized deployment plan must stage exact reviewed bytes and profile, verify each node, and define rollback to that captured pre-state. On failure, stop newly introduced route/control path and restore only modified artifacts by exact identity; compare checksums and service/routing state against pre-state. No assumed rollback command is safe without knowing that state. This package did not collect host pre-state or touch a node.

No credentials, private request content, provider/API call, service mutation, deployment, DNS change, automation change, shard write, checkpoint durability or task-resume authority is contained or claimed. Memory-layering attempt 3 remains NOT_AUTHORIZED.
