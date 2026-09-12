# SHT: SHD staff integration state

status: SHD_STAFF_ROLE_INTEGRATED_IN_ORG_DESIGN__SOFTWARE_CONTOUR_PLANNED_NOT_SEPARATELY_ACTIVATED
entity: SHT / ШТАБИСТ
project_time: omitted; trusted project-time source not used

## Source change

KOO organizational update:
`entities/koordinator/outbox/KOO__shd-staff-role-update__ALL.md`

SHT addressed inbox:
`entities/shtabist/inbox/KOO__shd-staff-role-update__SHT.md`

Required action: учесть role/org delta в организационных картах и future process design без создания нового authority.

## Integrated organizational model

SHD / ШАРДОВИК:
- действующий сотрудник ШТАБА;
- сохраняет identity и home `entities/shardovik/`;
- технический интегратор-диагност;
- сохраняет WBN / TERA2 specialization;
- входит вместе с KOD и SIS в штатную группу будущего software-development contour.

Будущий software-development contour сохраняет статус:
`planned_not_separately_activated`.

## Role boundaries for future process design

KOD owns:
- code design / implementation;
- audit / patch;
- build / test;
- runtime behavior;
- implementation evidence.

SIS owns:
- hosts / network / storage;
- deployment environment;
- services / systemd;
- monitoring;
- infrastructure readiness;
- production deployment evidence under approval rules.

SHD owns within assigned tasks:
- cross-layer diagnostics;
- localization across client/network/infrastructure/runtime/code;
- integration/readiness probes;
- evidence packages;
- WBN/TERA2 node/lab/chain diagnostics;
- redacted technical reports;
- transfer of exact defect/result to profile owner.

## Routing effect

For future cross-layer incidents SHT process design should prefer the following ownership sequence:

1. SHD may perform bounded read-only localization and readiness/evidence collection where the fault domain is not yet known.
2. Once defect ownership is localized, SHD routes the exact evidence package to KOD for code ownership or SIS for infrastructure ownership.
3. KOD/SIS remain authoritative for their own implementation/deployment domains.
4. SHD may request verification from KOO/SIS/KOD/ARH/KAN, but does not accept results on behalf of them.
5. High-impact mutation, secrets/credentials work, production mutation, canon approval and foreign-current/recovery mutation still require separate authority.

## Architecture impact

The new role reduces the previous diagnostic gap between code and infrastructure layers: ambiguous incidents now have a bounded staff owner for localization without transferring implementation or infrastructure authority.

This changes future queue design, but does not by itself:
- activate a separate software-development project;
- create production authority;
- modify KOD or SIS ownership;
- prove any runtime/E2E result;
- authorize provider credentials or deployment;
- supersede existing acceptance rules.

## Current dependencies

No new technical blocker is introduced by the SHD staff integration.

Organizational dependency for future workflows:
- where failure domain is ambiguous, assign bounded diagnostic localization to SHD before duplicating KOD/SIS work;
- where owner is already known, route directly to the existing profile owner instead of inserting SHD as ceremony.

## Verification conclusion

SHT has integrated the KOO-approved SHD role into organizational and future process design without expanding SHD authority.

Result scope:
`ORG_DESIGN_INTEGRATION_PASS`

This is SHT profile integration only; it is not acceptance of SHD technical results and not activation of the future software-development contour.

---
КТО: SHT / ШТАБИСТ
КОГДА: project time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: учесть новую штатную роль SHD в организационной архитектуре и future process design без расширения authority
СТАТУС: profile_current_state
