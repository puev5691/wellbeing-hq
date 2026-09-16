# TERA2 root-profile candidate r0.3

Status: correction-only, review-only, non-production.

Basis:
- r0.2 package commit `0562bafc790ba2f5e8b5e26214e14e7fa246146e`;
- SHD blocker review commit `bcdbe6dfc744ee1ff581ca78bd1f3eeaf001323c`;
- exact upstream TERA2 `6cc2061c12986bbaea182786c42d89fd979eeb33`.

Only two corrections are in scope:
1. `MODE_RUN=WBN_ROOT` is common immutable selector, not freely node-local.
2. machine-readable profile ↔ tracked patch proof is complete and fail-closed.

The tracked source patch is byte-identical to r0.2. Naming, supply allocation, reward policy, built-in `GenesisSmartCreate()` retention and fixed start-date policy are unchanged.

Verification uses `POLICY-MAP.json`, pinned source/post-patch identities and deterministic negative fixtures. No Node process, genesis execution, DATA/DB write, credentials/miner keys or public-network action belongs to this package.
