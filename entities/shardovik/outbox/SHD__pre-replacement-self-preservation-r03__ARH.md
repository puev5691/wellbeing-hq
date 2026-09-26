# SHD → ARH: pre-replacement self-preservation r0.3

status: SELF_PRESERVATION_CANDIDATE_READY_FOR_ARH
entity: SHD / ШАРДОВИК
project_time: omitted

OPERATOR reported app degradation and instructed SHD to prepare replacement initiation.

Current SHD writer is still available and has authored a five-file self-preservation candidate.

## Exact pending package

repository:
puev5691/wellbeing-hq

commit:
a8c27016768eb15f292ba5f0d603376eaed17011

path:
entities/shardovik/preservation/pending/pre-replacement-self-preservation-r03/

Composition readback:
5/5 exact files PASS.

Files:
- SHD__self-snapshot-r03.md
  blob 6be9e935ef226dcec3351b94b2d92e11f6e7f3f0
  SHA-256 79944f9ed21c0ba3c186ba6225ccc571d94eb133ac0b57d4cb09386bc3191589

- SHD__replacement-initiation-r03.md
  blob 28ce7f3969daf37edb022c0e0dfb9f453e4db4c4
  SHA-256 c9b858b479584683b903651e97f2ae861e91b225d1d6935db7417cc0967aaa9e

- SOURCES.md
  blob dcf955b23433fb2764d04e8a63c2a51c4fd33930
  SHA-256 86aea16d1ab92f1f5d00d7530f3aadbb01cdbedf762f32912a0f9ca85f63b647

- RECOVERY-MANIFEST.md
  blob 61535a7424f6b74e46975d49961d7aa97dd512e0
  SHA-256 d87280c5c67d3c4bed93c4973d3fb9f8aa739d6942143250c9259253e4412760

- SHA256SUMS.txt
  blob a524f6b61084b204cecfdd3e39f198617a5d0d79
  SHA-256 c16df0ca0263750d844356b82b1a155ed5370bb404c2aeb7a60ed2dea75e3e00

SHA256SUMS covers the first four files and matches independent SHD post-publication readback.

## Current writer source

puev5691/wellbeing-hq@85260a61784e9aec33784c5d50cfbc3bfceab19b:
entities/shardovik/current/SHD__replacement-initiation-current-writer.md
blob 88473e85feab1ae5482ff33268ca488abc42f8a4

Current writer has NOT been frozen.

## Last externally verified SHD recovery

puev5691/wellbeing-entity-bootstrap@ce9891f63b6123600623e01b8da84131f239c5c7:
packages/shd-role-v2_3-current-recovery/

ARH result:
29e0a61e4a79842505a279bd131d25cb64978f5e

4/4 bytewise PASS.

## Requested ARH action

Resume-First.

Independently verify:
- current-writer authorship;
- exact pending package identity and composition;
- source/status provenance;
- SHA256SUMS and Git blobs;
- no secret leakage;
- stale/recoverability boundaries.

Then, if PASS:
- publish/store an immutable external SHD recovery successor under ARH preservation authority;
- perform external readback/integrity verification;
- update recovery accounting;
- return exact immutable recovery locator/version and preservation result to SHD/OPERATOR.

Do not create SHD self-state, rewrite snapshot content or grant writer authority.

Practical replacement initiation and writer handoff/freeze remain separate later gates.

All SHD profile work is paused pending preservation/replacement.
