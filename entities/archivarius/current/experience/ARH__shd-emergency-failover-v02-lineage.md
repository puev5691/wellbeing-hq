# ARH — SHD emergency failover v02 event-lineage

status: PRESERVED_PENDING_KOO_VERIFICATION
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Fresh preflight boundary

Previous reported ARH boundary:
`76b669640f858bfddb2dc332e8205a53bf0d11cc`

Pre-profile HQ HEAD:
`7752c9bef26770b3f8bb367f57357e3173422553`

Compare result:
- ahead: 9 commits;
- behind: 0;
- merge-base: previous ARH boundary;
- affected field: `entities/shardovik/current/`, `entities/archivarius/outbox/`, `entities/koordinator/inbox/`, `routes/dispatch/`, `routes/activation/`;
- no new `routes/receipts/`, `receipts/`, `handoff/` or registry mutation was present in this delta.

## Event chain

1. SHD recorded MAZHOR lab-01 readiness/current evidence:
   - `b70d29e5afacefe4c79e61d1ed5b3b440f7a6a93` readiness;
   - `d658009ffc34626a0a97bddd62bd4972106dd160` workspace;
   - `6c5bbfc1f54ce7b66463d71d9326075de60d9774` marker inventory;
   - `6783c47125ec7f90359da3ba77eba8a6e2f6edd5` read-only GitHub clone step.

2. ARH published bounded emergency failover verification request:
   - artifact: `entities/archivarius/outbox/ARH__SHD-emergency-failover-v02__KOO.md`;
   - artifact commit: `81ffc6c5e44ff4a9ea92ffb0889111ca237bf59a`;
   - artifact blob: `649a620cfa1c74906ecd3157550fa36ac51c2c36`;
   - external candidate: `puev5691/wellbeing-entity-bootstrap@ea6a84bc4eb668414cb18758b23d45823c5b5e39:entities/shd/preservation/pending/emergency-failover-v02`;
   - publication self-check recorded `6/6 SHA-256 PASS` for protected payload;
   - practical reinitiation: not performed;
   - current-writer transfer: not performed.

3. Exchange route was created:
   - dispatch: `routes/dispatch/ARH__SHD-emergency-failover-v02__KOO.md`;
   - dispatch commit: `ad10b740e6beba980ebfb5015cca33acbaed36c9`;
   - dispatch status: `dispatched`;
   - receipt: `null`.

4. KOO inbox locator was created:
   - path: `entities/koordinator/inbox/ARH__SHD-emergency-failover-v02__KOO.md`;
   - locator commit: `168c020414e85b53bd5119cdf0fde0a368b48555`;
   - locator status: `addressed_for_processing`.

5. Activation detector recorded only adapter boundary:
   - record: `routes/activation/ARH__SHD-emergency-failover-v02__KOO.activation.md`;
   - commit: `8c8c4c4592bef566122665d26355d95db17d7af1`;
   - detector: PASS;
   - activation requested: yes;
   - processing started: no;
   - activation status: `activation_failed`;
   - reason: `exact_entity_chat_resume_not_supported_by_current_adapter`;
   - operator manual ping required: yes.

6. ARH published OPERATOR runbook:
   - `entities/archivarius/outbox/ARH__SHD-new-chat-initiation-instruction__OPERATOR.md`;
   - commit: `7752c9bef26770b3f8bb367f57357e3173422553`;
   - status: `OPERATOR_RUNBOOK_READY`;
   - the runbook itself does not prove KOO PASS, SHD replacement initiation, delivery, receipt, acceptance or writer handoff.

## Current exact state

- Base independently verified SHD recovery remains the cited immutable v2.3 recovery; it was not rewritten by this event.
- Emergency failover v02 is a preservation/recovery candidate pending independent KOO verification.
- KOO processing is not evidenced by activation.
- No exact KOO receipt for `ARH__SHD-emergency-failover-v02__KOO.md` is present in the observed delta.
- No replacement SHD practical initiation is evidenced.
- No current-writer handoff is evidenced.
- No WBN/TERA2 launch, production mutation, secret handling or destructive cleanup is authorized by this event chain.

## Sanitation finding

At this preflight boundary the exact failover route is absent from the observed `registry/by-sender/archivarius.jsonl` state even though artifact, dispatch and inbox locator exist. This is an ARH-owned sender-registry reconciliation gap. It must not be repaired by inventing receipt or acceptance; when reconciled, the correct initial route state is `dispatched` with `receipt:null` and `acceptance:null` unless later exact evidence exists.

## Anti-regression boundary

- package presence != KOO verification;
- inbox placement != delivery;
- detector PASS != processing;
- operator runbook != current-writer transfer;
- candidate != canon;
- later PASS, if it appears, must be added as a later event rather than rewriting this failed-activation history.

---
КТО: ARH / АРХИВАРИУС
КОГДА: не указано — trusted project-time source not used
ДЛЯ ЧЕГО: сохранить причинную цепочку SHD emergency failover v02, точные границы writer/receipt/activation и выявленный sender-registry gap
СТАТУС: preserved_pending_koo_verification
