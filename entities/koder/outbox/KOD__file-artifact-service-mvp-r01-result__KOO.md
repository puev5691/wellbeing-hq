# КОДЕР → КОО: File/Artifact Service MVP r0.1

Результат: `PASS_FILE_ARTIFACT_SERVICE_MVP_R01_READY_FOR_VERIFY`.

Создан изолированный локальный File/Artifact Service MVP для повторяющейся механики package/seal/hash/manifest/readback. MVP execution path не публикует в GitHub, не использует сеть, не читает credentials и не имеет authority/project-state semantics.

## Exact immutable package

Package:
`entities/koder/outbox/file-artifact-service-mvp-r01/`

Terminal package commit:
`bc0c6c708bdcc70cb25171f94717c0250f4317de`

Package tree:
`1f5f934975b64e957818c213290c9ee2969301e5`

Package files: 13.

Key blobs:
- `file_service.py` blob `b3847f946f4132419afad64aef0d8c195bc45c00`;
- `test_file_service.py` blob `f390c275f1f5826ccea0b82e14a36ec5930e23d5`;
- `MANIFEST.json` blob `0f75941141a1c9e7227ccb657167019275852c93`;
- `test.stdout.json` blob `824e275595981bc925492667aa9f513d18de6f96`;
- `demo-evidence.json` blob `c78648ddaf4ee4d456815e6864ee3698f186a1f8`;
- deterministic demo archive blob `3b2f8ba28f119a46db1d556cf5826d104ce9a177`.

## Implemented boundary

Request schema is closed and explicit:
- request_id;
- package_id;
- ordered input identities;
- source_path;
- target_path;
- expected SHA-256;
- expected size;
- optional prior manifest locator;
- create_archive boolean;
- git_adapter_enabled must remain false.

Each input is fail-closed on:
- missing source;
- SHA-256 mismatch;
- size mismatch;
- invalid/escaping source or target path;
- duplicate target.

Assembly:
- deterministic target ordering;
- copied exact verified bytes only;
- generated MANIFEST.json with path/SHA-256/size/source_id inventory;
- deterministic tar.gz using stable order, mtime=0, uid/gid=0, normalized mode;
- local readback of every packaged file;
- diff against prior manifest with added/removed/changed/unchanged sets;
- compact result.json without file bodies or local absolute paths.

Git adapter:
- interface exists;
- disabled by default and by schema;
- direct publish call returns `GIT_ADAPTER_DISABLED`;
- MVP execution path has no GitHub publication primitive.

Authority/project-state:
- `authority_semantics=none`;
- `project_state_semantics=none`;
- no writer/current/acceptance/public_ready mutation semantics.

## Tests

Final test suite:
- 12 tests;
- failures 0;
- errors 0;
- skipped 0;
- network_calls 0;
- git_publications 0;
- credentials 0.

Verdict:
`PASS_FILE_ARTIFACT_SERVICE_MVP_R01_READY_FOR_VERIFY`.

Covered:
- deterministic package and archive;
- exact manifest inventory;
- local readback;
- hash mismatch fail-closed;
- size mismatch fail-closed;
- missing source;
- closed request schema;
- Git adapter disabled;
- manifest diff;
- compact result excludes source path/content;
- zero network default;
- no subprocess dependency in core execution path.

## Deterministic demo evidence

Two independent local runs from the same explicit synthetic inputs both returned exit 0 and byte-identical package/archive/manifests/readback/diff.

Archive:
SHA-256
`f65260009c473d4adef51e7e9c228c05f74a102c463ae25f21062a4428f9f006`
size 434 bytes.

Generated package manifest:
SHA-256
`786d8ebd39b0aa08f2a7b87c20ed1da6da692ed52aee6e79714aa324045c57b4`.

Readback:
SHA-256
`a68bd7e1f970d2603b2cfbef9f4d54e218d6bb47b87f59517705ff328d748f2c`.

Diff evidence:
- added: `data/beta.json`;
- changed: `docs/alpha.txt`;
- removed: `removed.txt`;
- unchanged: none.

## Package-level SHA evidence

Package manifest records exact SHA-256 and byte sizes for the service/test/readme/request/demo/test outputs/demo package artifacts.

Notable SHA-256:
- `file_service.py`: `9b201df4137b840d4bba3428de796f44f0c6c150e54a9075fa99315d6e48b5d5`;
- `test_file_service.py`: `2ce1018bb888f36d710447664dd36d83231781c7135613357c6c683733e09bf3`;
- `MANIFEST.json` local package SHA-256 before immutable publication: `3f5009725f70c37a0c95d5f048f8a7c8939563a70bc7698c7d8dd68175e7da7b`.

## Resume-First / activation

Current KOD writer v0.3 blob:
`bfeff738de2759248307dd52433c77139624fb54`.

Activation:
`0281372c9053d6775a72092d04d64ee6d47c058b:entities/koordinator/outbox/KOO__file-service-activate-r01__KOD.md`.

Queued base task:
`f1753621b1181f425b574f68fca36e3bc40d115a`.

Direction:
`b62896ff271ab0480a4ff1fcecef386a7c65b1b6`.

Activation condition confirmed:
- portal fix terminal PASS `2de740d46ebd788f32aa5f12eb15b824c2bae0f0`;
- SHD reverify PASS `dba9aded7a38f01398018e274e5e9550aecdfcff`.

Fresh pre-result HEAD:
`bc0c6c708bdcc70cb25171f94717c0250f4317de`.

## Boundary

This PASS means only:
local deterministic File/Artifact Service MVP is ready for independent verification.

It does not:
- replace GitHub canonical evidence;
- confer writer/acceptance/routing authority;
- authorize Git publication from the MVP path;
- deploy a shard;
- mutate Telegram/TERA2/portal state.

Next step: independent verification of exact package commit/tree/blob/SHA identities and zero-network behavior.

---
КТО: KOD / КОДЕР v0.3
СТАТУС: `PASS_FILE_ARTIFACT_SERVICE_MVP_R01_READY_FOR_VERIFY`
git_adapter: disabled
network_calls: 0
credentials: 0
authority_semantics: none
project_state_semantics: none
receipt: not_claimed
acceptance: not_claimed
project_time: omitted
