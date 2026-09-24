# PROMPT — KOO v0.8 materialize initiation result

Текущий физический replacement KOO уже завершил cold-start и сообщил:

`initiation_verified_waiting_writer_gate`

Но fresh GitHub-preflight ARH показал, что immutable initiation-result для v0.8 ещё не опубликован в `puev5691/wellbeing-hq`.

Не повторяй cold-start и не выполняй Writer Gate.

Сделай только фиксацию уже полученного initiation outcome как отдельного immutable artifact.

Обязательная база:

Predecessor writer:
`entities/koordinator/current/KOO__replacement-current-writer-v06.md`
blob:
`90edff69b20879231fda8b882cbb172173e456f0`
establishment commit:
`525e5b131472e61b1f55db5ef7307217aea4c4fc`

Handoff/freeze authority:
`entities/archivarius/outbox/ARH__KOO-v06-handoff-freeze-authority-v08__OPERATOR-KOO.md`
commit:
`41020449328bc65de00bfa3ee83cee21761bce46`
blob:
`4b07e9815eaae17f79e15d02f2007c2cb708025f`

Immutable recovery:
`puev5691/wellbeing-entity-bootstrap@ef8e2c887fe95b69a99b0a0252027d9ee267ea2b:entities/koo/recovery/versions/koo-recovery-v08`

ARH preservation terminal:
`PASS_ARH_KOO_RECOVERY_V08_PRESERVED_READY_FOR_HANDOFF`
result commit:
`d46c77a7f5a685943b0aec732d75cf42c95eed9b`

Required action:

1. fresh-preflight `puev5691/wellbeing-hq`;
2. verify no later competing KOO writer/handoff evidence;
3. publish one initiation-result artifact under `entities/koordinator/outbox/`;
4. artifact must state:
   - status `initiation_verified_waiting_writer_gate`;
   - exact recovery locator;
   - verified composition/readback result;
   - predecessor writer identity;
   - freeze authority identity;
   - fresh HQ HEAD used for verification;
   - historical PROMPT replay: none;
   - memory-layering attempt 3: NOT_AUTHORIZED;
   - Writer Gate: NOT_PERFORMED;
   - profile work: NOT_STARTED;
5. immutable readback published file and return exact:
   - path;
   - commit;
   - blob;
   - status.

Do not:
- rerun or reinterpret the cold-start;
- perform Writer Gate;
- create a new current-writer;
- execute profile/routing work;
- authorize attempt 3;
- mutate external systems.

STOP after immutable initiation-result readback.
