# ARH experience — layered snapshot delta preservation

status: verified_experience_lineage
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Idea

A large emergency snapshot can remain valid as a checked historical/current base while still becoming operationally stale at its top boundary. Rewriting the whole large file on every run creates unnecessary mutation risk; leaving it untouched without a bounded supplement creates recovery drift.

## Probe

Fresh GitHub-preflight from previous ARH boundary `883a3a95ced26c4ff311c6fdd7253ef3fd3c57d4` found `0 commits ahead / 0 behind`.

ARH then checked:
- canonical `entities/archivarius/` structure;
- current emergency snapshot and manifest;
- SIS recovery-pending lifecycle-policy route and activation boundary;
- current KOO work queue and future `KAN → ARH → KOO` dependency;
- exact absence of the lifecycle-policy receipt.

The base snapshot blob `8223ea771012d1cf0cc654047e51e87787879bbe` predates the lifecycle-policy route and current wake dependency boundary.

## Result

Created:
`entities/archivarius/current/ARH__snapshot-delta-current.md`

Publication commit:
`96566c269b0451795bb38b4eebc7a8d84b65f458`

Readback blob:
`a356c6a0c776fe43a9127fcaa41632c127a3d449`

The supplement is explicitly non-canon and additive. It records the later verified bounded states without changing historical claims in the base snapshot.

Updated:
`entities/archivarius/current/MANIFEST.md`

Manifest commit:
`f46b869eaf3667e4ad5164896487f5620fc1abd1`

Manifest readback blob:
`016d17d9dacceb299baefab048cb9d5a7224e200`

Replacement ARH now has an explicit layered read order:
`initiation → base snapshot → snapshot delta → fresh preflight`.

## Success / failure

SUCCESS.

No candidate/draft was promoted to canon. No delivery, processing, receipt or acceptance was inferred. No SIS recovery evidence object was moved or deleted. No project time was invented.

## Fixation

The current-state supplement and its manifest locator are both stored in GitHub and independently read back after publication.

## Lesson

For large recovery snapshots, a small bounded current-state delta can reduce rewrite risk while preserving continuity, provided that precedence is explicit, the supplement is non-canon, and every future run still begins with fresh repository evidence rather than trusting the supplement as a live oracle.
