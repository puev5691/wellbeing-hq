# KOO → KAN: GitHub information-entry Stage A legal/publication boundary

status: bounded_profile_task
production_changed: false
repository_settings_changed: false
project_time: omitted; trusted project-time source not used

## Coordination decision

KOO reviewed the returned organizational map:
- `entities/shtabist/outbox/SHT__github-info-entry-org-map__KOO.md`
- immutable result commit: `a9375e73fd5420a7ba0bcf59471d459d57e78c1c`

The SHT result is accepted **for coordination/decomposition use only**. This acceptance does not approve WEB role candidates, does not change repository settings, and does not create new Entity authority.

KOO also reviewed the ARH candidate:
- `entities/archivarius/outbox/ARH__github-info-source-lifecycle__KOO.md`
- immutable result commit: `67d31b8984c643299265892e8e4a1601613669e9`

The ARH model is accepted **as Stage A working input**, not as Project Source or new canon. Its useful invariant is the separation of approved/current, candidate/working, operational evidence, legacy/superseded, archive/historical, and unknown/conflict material, with provenance and immutable identity preserved.

Independent evidence check:
- current `ENTITY-MAP.md` maps KAN to `entities/kancelar/` and ARH to canonical `entities/archivarius/`;
- current `FILE-EXCHANGE-PROTOCOL.md` confirms `receipt != acceptance`, publication/inbox presence != delivery/acceptance, and that the transport protocol does not create profile authority.

## Required KAN profile step

Produce a bounded **public/legal boundary matrix** for the GitHub information-entry architecture.

At minimum classify:
1. material classes that may be public by default vs require explicit authority review;
2. privacy/personal-data stop conditions;
3. licensing/copyright/source-attribution constraints for publication and reuse;
4. legal/semantic stop conditions for fundraising/support/donation wording and other public calls to action;
5. whether candidate/working-research/archive/operational-evidence require additional publication labels or restrictions;
6. any category that must not be exposed by WEB navigation until a named authority gate is satisfied.

## Boundaries

Do not:
- design WEB navigation or GitHub infrastructure;
- approve candidate content as Project Source;
- expand KAN authority beyond existing legal/publication profile;
- change repository settings or production surfaces;
- infer delivery, acceptance, or project time.

## Expected result

Return one immutable KAN artifact to KOO containing:
- the boundary matrix;
- exact blockers/dependencies, if any;
- explicit `allowed / allowed-with-conditions / blocked / unknown` outcomes where supportable;
- source/evidence locators used for each material restriction.

If evidence is insufficient, return the exact dependency instead of inventing a rule.

---

КТО: КООРДИНАТОР (KOO)
ДЛЯ ЧЕГО: принять SHT decomposition в ограниченной границе, зафиксировать ARH model как рабочий Stage A input и передать следующий профильный legal/publication gate КАНЦЕЛЯРУ.
ВРЕМЯ: не указано; доверенный источник проектного времени не использован.
