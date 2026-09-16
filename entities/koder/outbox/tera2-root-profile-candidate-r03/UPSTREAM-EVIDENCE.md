# Upstream evidence retained for r0.3

Exact upstream repository: `https://gitlab.com/terafoundation/tera2.git`.
Exact pinned commit: `6cc2061c12986bbaea182786c42d89fd979eeb33`.

The r0.3 correction does not change the r0.2 tracked source patch. Source evidence remains:
- `Source/core/const-mode.js` for tracked root mode and common chain assignments;
- `Source/system/accounts.js` for WBN_ROOT genesis accounts 0..15;
- `Source/core/constant.js` for `TOTAL_SUPPLY_TERA=1e9` and 16 genesis-account range basis;
- `Source/system/smart.js` retained unchanged for built-in `GenesisSmartCreate()`;
- `Source/core/crypto-library.js` pinned as retained upstream evidence.

`SOURCE-IDENTITIES.json` records exact upstream blob/SHA-256 identities. `PATCHED-FILE-IDENTITIES.json` records exact post-patch identities for every touched source file. Verifier consumes both artifacts and requires the patch-touched file set to match the declared post-patch identity set exactly.
