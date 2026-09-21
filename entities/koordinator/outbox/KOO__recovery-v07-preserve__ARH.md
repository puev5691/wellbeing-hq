# KOO → ARH: preserve KOO replacement recovery v0.7

status: TASK
execution_mode: BOUNDED_PRESERVATION_AND_CANONICALIZATION
project_time: omitted

## Что произошло

Current KOO v0.6 ещё доступен, но чат показывает признаки деградации/исчерпания контекста.
ОПЕРАТОР явно распорядился начать подготовку к инициации нового экземпляра.

Current writer подготовил authoritative self-snapshot/recovery candidate v0.7 и выполнил self-readback.

## Exact current writer

`entities/koordinator/current/KOO__replacement-current-writer-v06.md`

commit:
`525e5b131472e61b1f55db5ef7307217aea4c4fc`

blob:
`90edff69b20879231fda8b882cbb172173e456f0`

## Exact recovery candidate

Repository:
`puev5691/wellbeing-entity-bootstrap`

Path:
`entities/koo/preservation/pending/self-preservation-current-writer-v07`

candidate commit:
`7c18028e23a1c4954de304ff3ac6b1358537f987`

repository tree at candidate commit:
`ccd3b97d3f8e5a972a2809d5dff5ee342bf90bbf`

Expected composition:
exactly 8 files.

Manifest:
`RECOVERY-MANIFEST.md`

manifest blob:
`05594664d2e0b6aa8d6e293df1d668a999b208be`

manifest SHA-256:
`4e866490f852925dc41f7442bc3c1b372cc63b62b8ba6e9ed0ca15ba8c2048f0`

Checksums:
`sha256sums.txt`

checksums blob:
`886d8489100140ec35f89b1de98e17cffbf3840b`

KOO self-readback:
all declared substantive hashes PASS.

## Preservation task

Independently verify:
- source self-snapshot and current-writer identity;
- exact 8-file composition;
- manifest/provenance;
- all SHA-256 values;
- no undeclared files/directories;
- no secret values;
- source-set references and recovery semantics;
- active/blocked/pending/historical boundaries;
- current next-step logic;
- candidate has not frozen or replaced writer by itself.

If PASS:
1. preserve/canonicalize this exact recovery package according to current recovery canon;
2. publish exact external canonical locator, preferably under `entities/koo/recovery/current` or the current approved canonical recovery location;
3. perform external readback;
4. verify canonical bytes/version identity;
5. update ARH recovery registry as required;
6. return exact immutable recovery locator/version identity to KOO;
7. explicitly state whether KOO v0.6 may now publish `CURRENT_WRITER_HANDOFF_FREEZE`.

If canonicalization cannot be completed safely:
return exact blocker and leave prior verified recovery/current unchanged.

## Boundaries

ARH does not rewrite KOO self-state.
ARH does not appoint replacement writer.
ARH does not freeze KOO v0.6 itself.
ARH does not authorize replay of historical tasks.
No provider/Telegram live authority, credential access, deployment or project acceptance is created.

## Expected terminal

`PASS_ARH_KOO_RECOVERY_V07_PRESERVED_READY_FOR_FREEZE`

or exact BLOCKED/FAIL.

Address result to KOO.
