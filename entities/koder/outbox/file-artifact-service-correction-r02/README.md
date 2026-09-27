# File/Artifact Service correction-only successor r0.2

This is a local deterministic packaging service, not an authority, publication or deployment mechanism. It retains the r0.1 JSON request schema, package manifest, deterministic optional tar.gz, readback, diff and compact result. `GitAdapter.publish()` always fails with `GIT_ADAPTER_DISABLED`; the execution path needs no network, credentials or subprocess.

Correction of independent SHD r0.1 FAIL:

1. The successor inventory is sealed after every inventoried byte is final. `SHA256SUMS` is generated from those bytes; top-level `MANIFEST.json` is generated last and records the checksum file. Neither metadata file claims a self hash. External publication is followed by exact Git committed-blob readback and independent SHA-256/size comparison, reported separately.
2. Input target `MANIFEST.json`, normalized aliases and descendants are rejected before any output write. Generated path reservations are explicit in `GENERATED_PATHS`.
3. `prior_manifest_path` accepts null or a safe relative string only; absolute/parent paths and symlink traversal fail before package writes. Source-root containment is checked on the resolved path.
4. `create_archive` is exact Boolean. No truthiness coercion. `prior_manifest_path` is exact null/string.

Run offline: `python3 -B test_file_service.py`. The 19 tests include preserved r0.1 positive/negative boundaries and new regressions. `negative-fixtures.json` lists explicit malformed requests as deltas to `example-request.json`. `demo-evidence.json` and `run1` record two deterministic executions with equal output hashes. `PREDECESSOR.diff` shows source and test changes against the exact r0.1 Git blobs.

Operational boundaries: `authority_semantics=none`, `project_state_semantics=none`, no writer/current/acceptance/public_ready claim. GitHub package publication and committed-byte verification occur outside the service. The independent SHD re-review is still required. No production use, shard WRITE, checkpoint durability or EOM/memory-layering MAIN attempt is inferred.
