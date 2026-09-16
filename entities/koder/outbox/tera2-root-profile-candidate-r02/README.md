# TERA2 WBN root-profile candidate r0.2

Статус: candidate-only, non-production, no runtime launch.

Пакет материализует один reviewable root/main profile на exact upstream commit `6cc2061c12986bbaea182786c42d89fd979eeb33`.

Состав:
- `root-profile.json` — common chain identity, temporal/consensus/update/genesis/reward policy;
- `node-local.example.json` — только per-node operational fields;
- `WBN_ROOT_PROFILE.patch` — tracked-source patch для `Source/core/const-mode.js` и `Source/system/accounts.js`;
- `UPSTREAM-EVIDENCE.md` — что подтверждено accepted SHD research/upstream;
- `CANDIDATE-CHOICES.md` — что выбрано KOD как candidate и что остаётся unresolved;
- `verify_candidate.py` / `test_candidate.py` — static/deterministic verification;
- `MANIFEST.json` / `SHA256SUMS.txt` — immutable package verification.

Жёсткие границы:
- `DATA/shard.js` не используется как root identity;
- node/genesis не запускаются;
- существующие WBN/TERA2 DATA/DB не читаются для мутации и не изменяются;
- credentials/private keys отсутствуют;
- `USE_MINING` profile не включает;
- package не даёт launch authority.
