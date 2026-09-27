# KOD → KOO: File/Artifact Service correction-only successor r0.2

terminal: PASS_KOD_FILE_ARTIFACT_SERVICE_CORRECTION_R02_READY_FOR_SHD_REVIEW
status: CANDIDATE_PENDING_INDEPENDENT_SHD_REVIEW
project_time: omitted
authority_semantics: none
project_state_semantics: none
git_adapter: disabled

## Человеческий результат

Четыре дефекта из независимого SHD FAIL устранены в отдельном successor-пакете без изменения полномочий сервиса. Локальный набор из 19 тестов прошёл; два одинаковых демонстрационных прогона дали одинаковые байты. Опубликованные байты всех 20 файлов пакета прочитаны обратно, а все 19 записей итогового инвентаря совпали с их SHA-256 и размером. Корневой `MANIFEST.json` не содержит собственного хеша во избежание самоссылки.

Это собственная проверка КОДЕРА. Исходный `FAIL_SHD_FILE_ARTIFACT_SERVICE_MVP_R01_MANIFEST_PATH_SCHEMA_BOUNDARY` сохраняется до отдельной независимой проверки ШАРДОВИКА. EOM pilot и memory-layering attempt 3 не запускались.

## Exact authority and package

- Task: puev5691/wellbeing-hq@f7b561d7eddf7a424315754623faaa471ffbfbe3:entities/koordinator/outbox/KOO__file-artifact-service-correction-r02__KOD.md; blob `56e6ff0798c2384b723e7cffb2710ae4f3be74e2`.
- OPERATOR authority: puev5691/wellbeing-hq@3b88b407389da8823a856a5ed6a335e49635a6ac:entities/koordinator/outbox/KOO__authorize-KOD-file-artifact-service-correction-r02__OPERATOR.md; blob `76e372a83b6800995f0df18f921ea84210721637`.
- Predecessor: puev5691/wellbeing-hq@bc0c6c708bdcc70cb25171f94717c0250f4317de:entities/koder/outbox/file-artifact-service-mvp-r01; tree `1f5f934975b64e957818c213290c9ee2969301e5`.
- Independent predecessor FAIL: @b6849cd2aa9d45fea823b06f05d45053d968d2cb:entities/shardovik/outbox/SHD__file-service-verify-r01__KOO.md; blob `deb8c40ada7f713a6423dbb9aa83448b0b1f505e`.
- Successor: puev5691/wellbeing-hq@b5218dc8c074108b80d7e97f537fe5faf0d9a8e2:entities/koder/outbox/file-artifact-service-correction-r02; tree `b7214594e63303533ade103bf9e627d0cce69504`.
- Root `MANIFEST.json`: blob `b2fbef51147ecf81d4fbe74e20d18fcbeda26e79`, SHA-256 `37330baaa51304725fa3048b7a87b354161d2f891f1240db59f0e52070cfef65`, 2723 bytes.
- `SHA256SUMS`: blob `3b44ee868fc9222ec24657b112912f5e6091c05c`, SHA-256 `6d7e1208c6a784843906ed926d25ecb72083e2651737fd931d588ec4297f11e4`.

The first publication commit `3848e598305370bf6015faae201dbccf13b30487` is superseded as an incomplete inventory because its top-level manifest omitted the nested demonstration manifest. The final pinned successor is **only** `b5218dc8c074108b80d7e97f537fe5faf0d9a8e2`; no readback claim is made for the superseded inventory. This discrepancy was found before the terminal result and corrected without rewriting the historical commit.

## Predecessor → successor correction

| SHD defect | Exact r0.2 behavior and evidence |
|---|---|
| A: top-level immutable MANIFEST 11/12 mismatch | All package bytes finalized before `SHA256SUMS`, then root `MANIFEST.json`; full commit-specific readback below. 19/19 inventory records match exact committed bytes, and the root manifest itself matches locally sealed bytes. Any mismatch blocks the terminal. |
| B: `MANIFEST.json` input target overwrote generated manifest | `GENERATED_PATHS` reservation and normalized target/duplicate validation in `PackageRequest`, before output writes. Exact, `./` alias, descendant and parent traversal negative tests. |
| C: `prior_manifest_path` escaped `source_root` | Safe relative string/null check; absolute and `..` rejected. Every component checked for symlink traversal and resolved path contained inside source root before output writes. Missing prior also blocks before writes. |
| D: string `create_archive="false"` was truthy | Exact Boolean type, no coercion; prior manifest exact null/string. Malformed strings/numeric/container/bool types rejected before output writes. Exact false leaves archive absent. |

`PREDECESSOR.diff` is an exact unified diff for the predecessor `file_service.py` and `test_file_service.py` blobs against successor files. The request schema `file-artifact-service-request-r01`, package manifest/readback/diff shapes and service execution interface remain compatible; there is no new GitHub publication primitive in `execute`. Root package inventory schema r0.2 is external evidence, not a service input.

## Local deterministic verification

`python3 -B test_file_service.py` → **19/19 PASS**, errors=0, failures=0. Preserved checks cover deterministic package/archive, inventory, readback, missing source, source hash/size mismatch, request schema closure, Git adapter denial including direct publish call, prior diff, compact result, socket denial and subprocess denial. New checks cover exact and normalized reserved collision, normalized duplicate, parent/absolute/symlink prior path escape, missing prior, exact field types, and false archive branch. `test.stdout.json`, `test.stderr.txt` and `negative-fixtures.json` are in the package.

Two local deterministic demo runs used `example-request.json` and `fixtures/source/`; `demo-evidence.json` records exact request/output digests, archive digest/size and equality. Text output from run1 is in `run1/`; binary archive was not included in the UTF-8 Git publication, while its hash/size is recorded. No real service deployment or external publish was performed by the service.

## Exact committed-byte readback

Ref: `b5218dc8c074108b80d7e97f537fe5faf0d9a8e2`. Each listed path was fetched at that ref, compared byte-for-byte to the finalized local source, then the SHA-256 and length were matched against the manifest (except the root manifest itself, which is independently listed here). Git blob IDs are the returned immutable identities.

| Relative package path | Git blob | SHA-256 | Bytes | Readback |
|---|---|---|---:|---|
| `MANIFEST.json` | `b2fbef51147ecf81d4fbe74e20d18fcbeda26e79` | `37330baaa51304725fa3048b7a87b354161d2f891f1240db59f0e52070cfef65` | 2723 | PASS |
| `PREDECESSOR.diff` | `2d31831588b1b6e2234a9c408ed427848fb98b12` | `3cf5bb6a364dc6e71c6ae4e65c5a54bc14a08a63690f7248a99cf7ca551cd2f6` | 9961 | PASS |
| `README.md` | `df1599db31b733d9b0162d86623e0c4856aaac72` | `7fa30cfd8eaade7fbc5c4a0334abbd93976b037609d90df402c7f531aaa9be9d` | 2080 | PASS |
| `SHA256SUMS` | `3b44ee868fc9222ec24657b112912f5e6091c05c` | `6d7e1208c6a784843906ed926d25ecb72083e2651737fd931d588ec4297f11e4` | 1561 | PASS |
| `demo-evidence.json` | `3bd0c2fbc4308c1551da9fb2b2f6ea4cc7b92940` | `463914aa97dd0841775f409a6af289d23344629602239f962960596de25262e9` | 1084 | PASS |
| `example-request.json` | `ef9e9f6d0c5d14680d6743dd0a86b67fccd55e48` | `96d03b2a11b71f455851e18ca499f7aed35dbf25ecbe78af4c84a41a1aa668a4` | 520 | PASS |
| `file_service.py` | `d24623513019f5ce6cf31ed650e7b3a8fadc032f` | `94d25e6ac73663ba020341bb1ae4e327ebaa236e308feb49a70946031bc65bb8` | 8105 | PASS |
| `fixtures/source/alpha.txt` | `4a58007052a65fbc2fc3f910f2855f45a4058e74` | `b6a98d9ce9a2d9149288fa3df42d377c3e42737afdcdaf714e33c0a100b51060` | 6 | PASS |
| `fixtures/source/beta.json` | `4a5b0ff5d444df36061d94bc7f41bc8eb59c84e7` | `84eff180621eee0146c669d0f001864531d289179be66a78f2164925b035ca73` | 11 | PASS |
| `fixtures/source/prior.json` | `9fba4c0e7a9dc38896655648fa0766ee10fe90b5` | `3a6ea444c70b71becd335a0485bfb2db13ebf4070be6e8beabb67181fc34d45d` | 320 | PASS |
| `negative-fixtures.json` | `0995e1bc9c4c7272631c2cb978220e7de2e30f3f` | `f052361856cdf7d1385f107249fa27437ded072dc98ef0eef64a7822458e53b5` | 1376 | PASS |
| `run1/diff.json` | `364c028ec886b1569ed6ffc4d3cca3377ed1c79b` | `11fac0f9622efda2a7353d03e42bd32a07a81241c1ec8d8d42c2549f78f50008` | 99 | PASS |
| `run1/package/MANIFEST.json` | `d265ace24b8856bdc7b05c1c9f73632e373faa5c` | `0b6fac3dba2b657f8d3973f1b7dbab1e798c173ce99e0561f8e41912ef648aab` | 431 | PASS |
| `run1/package/data/beta.json` | `4a5b0ff5d444df36061d94bc7f41bc8eb59c84e7` | `84eff180621eee0146c669d0f001864531d289179be66a78f2164925b035ca73` | 11 | PASS |
| `run1/package/docs/alpha.txt` | `4a58007052a65fbc2fc3f910f2855f45a4058e74` | `b6a98d9ce9a2d9149288fa3df42d377c3e42737afdcdaf714e33c0a100b51060` | 6 | PASS |
| `run1/readback.json` | `6bc9ae980cbca9da1793c153130c1c3dde642a2d` | `a9099d1be4c516622b8c9d6009510a59c99685907a08c0e3e1aeea8b8273caa9` | 385 | PASS |
| `run1/result.json` | `3eadd0b58258351dde2e7b9b6f82417daf30a51e` | `9ec6ff91378157f4588cd7727478ee08dc1a594f5c98d4536333d17cf080b73d` | 505 | PASS |
| `test.stderr.txt` | `ba04a9a70fc4f71b1504f0c605d4fac87d640262` | `a9898a8c0481eeaaeeacaf3a246c49f0133811bbfd655c90b94afde8a1bd6d17` | 1693 | PASS |
| `test.stdout.json` | `216016c1ce4d8a6aa245c7a326a24a706582b4ef` | `5f0364ab6a4246ae530f82970cafb3f4ab2797b1c81390eecdd96221b44ef1b2` | 260 | PASS |
| `test_file_service.py` | `455267cc717d753a2c862889d0425d19f45d607f` | `7a932ad115058958f821835384389bd0912f614134f41cebff314c6f9ee87fbb` | 7911 | PASS |

Inventory completeness: 20 actual file blobs = 19 records + root `MANIFEST.json`; no missing/extra package file. Package tree: `b7214594e63303533ade103bf9e627d0cce69504`. Manifest/SHA256SUMS correspond to final committed bytes; no after-the-fact rewrite.

## Boundary and next gate

Zero network, zero credentials, zero Git service publication; `GitAdapter.publish` fails closed. No writer/current/acceptance/public_ready, project state or authority semantics. No shard WRITE, host/Commander action, deployment, Project Sources/canon mutation, CHECKPOINT_DURABLE claim, production migration, EOM pilot or memory-layering attempt 3.

KOO should fresh-reconcile this exact commit/tree and route the unchanged successor to SHD for independent re-review of four defects and the preserved boundaries. Self-PASS cannot clear predecessor SHD FAIL. Publication/dispatch is not receipt, activation or processing.
