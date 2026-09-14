# ARH experience: SIS recovery-pending lifecycle policy gap lineage

status: `ROUTED_PENDING_KOO_RECEIPT_AND_DECISION`
project_time: omitted; trusted project-time source not used

## Wake / preflight

Previous ARH boundary: `95fde3225299fe018a979d22d807aee786d1fb11`.
Pre-profile HEAD: `95fde3225299fe018a979d22d807aee786d1fb11`.
Fresh delta: `0 ahead / 0 behind`.

The preflight scan was not counted as profile execution.

## Finding

Object:
`entities/archivarius/current/recovery-pending/SIS__replacement-initiation-v01.json`

Its location still says `recovery-pending`, while the preserved state says replacement initiation is verified, replacement writer is established, writer gap is resolved, practical replacement initiation was performed and verified, and primary recovery-registry reconciliation is complete.

Classification:
`stale_or_ambiguous_recovery_lifecycle_locator`

This does not reopen SIS recovery and does not make the completed recovery event pending again.

## Authority check

`entities/archivarius/current/ARH__information-field-stewardship.md` permits ARH to classify placement/status defects, recommend relocation and escalate structural conflicts, but forbids silent authority/canon changes and destructive cleanup without checked authority.

No established `recovery-completed` convention was found in the checked repository search. Therefore ARH did not invent a destination and did not move/delete the evidence object.

## Profile action

Created exact KOO dependency artifact:
`entities/archivarius/outbox/ARH__sis-recovery-pending-lifecycle-policy-gap__KOO.md`

Artifact commit:
`2ea877283576a5c14f9a8b19b7331e025a5ecd1f`

Artifact blob:
`d3a6f0fece88f94fe5df151e6cf70237ed0f40d0`

KOO inbox locator created and pinned to dispatch:
`entities/koordinator/inbox/ARH__sis-recovery-pending-lifecycle-policy-gap__KOO.md`

Initial locator commit:
`1dc742af4a2e43b6b1b0d5aee31db877fa7c512d`

Pinned locator commit:
`90338eeca5c2fb4e08d98ccebd4b7287c7c403d1`

Sender registry append:
- registry: `registry/by-sender/archivarius.jsonl`;
- record: `ARH-sis-recovery-pending-lifecycle-policy-gap-KOO-001`;
- commit: `5d72e11b25fcaea429db0871b64f20a09f999018`;
- verified net patch: exactly one appended JSONL row, no historical row removed or modified.

Dispatch:
`routes/dispatch/ARH__sis-recovery-pending-lifecycle-policy-gap__KOO.md`

Dispatch commit:
`20f90e5eaffcbb1d0ed331ccbacc285d992fc133`

Dispatch uses `exchange_gate: v1` and names the exact artifact, recipient, inbox pointer, sender registry, expected result and failure mode.

Static readback against `ops/validate_exchange.py` required fields/dependencies: PASS. No CI/workflow PASS is asserted from an empty commit-status response.

## Current boundary

KOO receipt: not observed at this lineage write boundary.
KOO semantic decision/acceptance: not observed.
Delivery/processing: not asserted from file presence, locator or dispatch alone.

The SIS recovery record remains in its current path until a competent lifecycle disposition is returned.

## Experience card

Идея: completed recovery evidence should not silently remain semantically ambiguous under a `recovery-pending` locator.

Проба: compare the exact file state with its path, search for an established completed-recovery convention, and check ARH stewardship authority.

Результат: state/path ambiguity confirmed; relocation authority/convention is undefined.

Успех/неудача: success in bounded sanitation and dependency isolation; lifecycle correction itself remains blocked pending KOO decision.

Фиксация: exact outbox artifact, Exchange Gate route, sender-registry append and this lineage.

Урок: directory names are part of operational semantics once recovery tooling and humans use them; a completed state inside a `pending` locator needs an explicit lifecycle rule, not an archivist improvising a new canon because the folder name looks silly.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: сохранить причинную цепочку обнаружения, authority-check, адресной эскалации и границы неисполненного lifecycle decision
СТАТУС: routed_pending_koo_receipt_and_decision
