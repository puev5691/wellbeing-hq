# Commands actually used

project_time:
omitted

## Acquisition

```bash
git clone --no-checkout https://github.com/puev5691/wellbeing-hq.git "$W/repo"
git -C "$W/repo" rev-parse "$C^{commit}"
git -C "$W/repo" rev-parse "$C:$P"
git -C "$W/repo" ls-tree -r "$C" "$P" > "$W/evidence/candidate-ls-tree.txt"
git -C "$W/repo" archive "$C" "$P" | tar -x -C "$W/materialized"
git hash-object <each materialized file>
sha256sum <all materialized files>
```

Expected candidate tree:
`65c8e7c9061bd81f6a0d2e9722d2fa60281c0ade`.

The verification loop compared all 58 materialized files against the immutable `git ls-tree` blob identities and stopped on mismatch.

## Safety

```bash
chmod -R a-w "$W/materialized"
export HOME="$W/runtime-home"
export TMPDIR="$W/runtime-tmp"
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONPATH="$W/guard:$ROOT"
```

An external `sitecustomize.py` audit hook blocked:
- socket connect/bind/getaddrinfo;
- subprocess/process spawning;
- filesystem mutation outside `$TMPDIR`.

The guard was self-tested before candidate execution.

## Test execution

```bash
python3 -B <in-memory compile of seven exact Python sources>
timeout 120 python3 -B "$ROOT/run_sandbox_adapter_tests.py"
timeout 120 python3 -B "$ROOT/run_runtime_integration_tests.py"
timeout 180 python3 -B "$ROOT/run_all_offline_tests.py"
timeout 120 python3 -B "$W/evidence/combined_r04_r02_probe.py"
```

## Post-execution verification

```bash
git -C "$W/repo" rev-parse "$C:$P"
git hash-object <each of 58 materialized files>
grep -h 'OFFLINE_GUARD_BLOCK' <actual test logs>
sha256sum <raw evidence files>
```

The initial final SHA collection line had a shell quoting error after tests were complete. Hash collection alone was corrected in a separate command.
