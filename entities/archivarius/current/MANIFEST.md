# ARH emergency recovery manifest

entity: ARH / АРХИВАРИУС
status: emergency-recovery
project_time: omitted; trusted project-time source not used

## Recovery files

- `entities/archivarius/current/ARH__initiation-current.md`
  - created in commit `a0596982f6457b579458e8f08a359a3440890d2d`
  - purpose: self-contained cold-start initiation for replacement chat

- `entities/archivarius/current/ARH__snapshot.md`
  - created in commit `7fb43759d39685cf8b95c4764eb2832a5630e005`
  - purpose: emergency snapshot of verified state and open work

- `entities/archivarius/current/ARH__snapshot-delta-current.md`
  - introduced in commit `96566c269b0451795bb38b4eebc7a8d84b65f458`
  - purpose: supplemental non-canon current-state delta after the large emergency snapshot; preserves later bounded recovery/routing dependencies without silently rewriting the base snapshot

## Baseline

Repository baseline before emergency preservation writes:
`477c7a328aa5990d782330f9c6cc29c455cfc763`

## Start rule

Replacement ARH chat reads `ARH__initiation-current.md` first, verifies repository changes after the latest preservation commit, then reads `ARH__snapshot.md` and `ARH__snapshot-delta-current.md` as layered recovery state before doing a fresh GitHub-preflight. Active Project Sources outrank this emergency package if a conflict is found. The supplement does not create canon, approval, writer authority, delivery or processing state.
