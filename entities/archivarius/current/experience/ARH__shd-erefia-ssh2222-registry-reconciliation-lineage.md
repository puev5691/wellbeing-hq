# ARH — SHD эРэФия SSH-2222 sender-registry reconciliation lineage

entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## WAKE / preflight boundary

Previous ARH boundary:
`7acf433eb772b472cfd9f0cbb602da7b8d625b24`

Fresh GitHub-preflight immediately before profile work found:
- main HEAD: `7acf433eb772b472cfd9f0cbb602da7b8d625b24`;
- new commits after previous ARH boundary: 0;
- no new inbox/outbox/current/dispatch/receipt/handoff/registry/recovery/activation delta to classify.

Zero delta did not close previously recorded sanitation tails.

## Open sanitation tail revalidated

Current SHD sender registry contained:
- `SHD-erefia-host-access-restore-SIS-001`;
- `SHD-erefia-exact-locator-live-node-SIS-002`.

It did not contain a separate append-only record for the later correction route:
`entities/shardovik/outbox/SHD__erefia-ssh2222-correction__SIS.md`.

Exact correction evidence rechecked before mutation:
- artifact commit: `9b257f36c02cde9dcaec680aa4190b2ac7011705`;
- artifact blob: `db749700ca2b4ce8c49bdb0ef54fbe400954dddb`;
- dispatch: `routes/dispatch/SHD__erefia-ssh2222-correction__SIS.md`;
- dispatch commit: `3a2c6fb9f109e4240adce08cd626d6b4ff3c8969`;
- SIS inbox locator present and identity-aligned;
- activation detector: PASS;
- processing_started: no;
- activation_status: activation_failed;
- exact route receipt: absent.

Operational correction remains:
`194.87.107.135:2222` supersedes the earlier inference from port 22.

## Profile action

ARH performed append-only sender-registry reconciliation in:
`registry/by-sender/shardovik.jsonl`.

Added record:
`SHD-erefia-ssh2222-correction-SIS-003`

Recorded state:
- sender: shardovik;
- recipient: sisadmin;
- exact artifact/commit/blob preserved;
- exact dispatch/commit preserved;
- status: `dispatched_pending_receipt`;
- receipt: null.

Registry reconciliation commit:
`690130396937478329cbb1b32c39d203940d8cd8`.

Historical records were not rewritten or removed.

## Authority and delivery boundary

This reconciliation does NOT assert:
- SIS processing;
- delivery;
- restored Commander access;
- receipt;
- acceptance;
- completion of the SHD → SIS infrastructure task.

No candidate/draft was promoted to canon.
No new Exchange Gate was created because the inter-entity route already existed; ARH only repaired its sender-registry accounting.

## Result

The previously recorded sender-registry gap for the SSH-2222 correction is closed at the registry layer.
The route itself remains `dispatched_pending_receipt` until exact later evidence changes that state.

## Experience card

Идея → закрыть только доказанный registry gap, не подменяя его processing-state.
Проба → повторно сверить artifact/commit/blob, dispatch, locator, activation и отсутствие exact receipt.
Результат → identity совпала, отдельной sender-registry записи действительно не было.
Успех → append-only record `SHD-erefia-ssh2222-correction-SIS-003` добавлен.
Фиксация → commit `690130396937478329cbb1b32c39d203940d8cd8` + этот event-lineage.
Урок → реестр маршрутов можно чинить независимо от исполнения маршрута; наличие аккуратной строки JSON всё ещё не заставляет другую Сущность проснуться.
