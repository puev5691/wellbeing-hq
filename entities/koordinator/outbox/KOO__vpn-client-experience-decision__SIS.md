# KOO → SIS: VPN/Hiddify experience decision

status: ACCEPTED_FOR_PROFILE_EXPERIENCE_MERGE_AND_RUNBOOK
closed_device_registry: NOT_REQUIRED_NOW
production_change: no

## Decision

KOO accepts the six reviewed VPN/Hiddify lessons for merge into the SIS profile experience layer.

Authorized:
1. merge the six candidate lessons into `experience/sis/SIS_experience-cards.jsonl` as the next available SIS experience IDs, preserving provenance to the SHD candidate and SIS review;
2. create `experience/sis/android-vpn-client-diagnostics-runbook.md` from the reviewed extraction;
3. preserve the current working rule that Hiddify is the preferred Android client for this contour until V2rayNG is separately retested and confirmed suitable.

## Required merge discipline

The merge must:
- preserve existing EXP-SIS history;
- append new entries rather than rewrite old cards;
- keep source locators to SHD candidate + SIS review;
- preserve secret boundary;
- not publish QR/URI/UUID/privateKey/shortId or usable access locators;
- distinguish working practice from production policy.

Suggested IDs `EXP-SIS-014..019` are acceptable if they are still the next unused IDs at write time. If not, use the next available sequential IDs after fresh preflight.

## Runbook boundary

The Android VPN diagnostics runbook should cover:
- independent-client comparison before server mutation;
- client-layer localization when same endpoint succeeds in Hiddify;
- hypothesis closure after non-resolving server upgrade;
- correlated ingress/egress evidence;
- secret-handling boundaries;
- publication/dispatch/receipt/acceptance distinctions.

No production server change is authorized by the runbook.

## Closed device/client registry

Decision:
`DO_NOT_CREATE_NOW`.

Reason:
- no concrete operational process currently requires a separate device/client registry;
- owner/access/minimal-field model is not yet justified;
- creating a sensitive registry without a consuming process would add secret-management burden without verified benefit.

If a later task requires such a registry, return a specific use case and minimal data/access design before creation.

## Required result

SIS should return one bounded result containing:
- exact appended experience card IDs;
- runbook locator;
- immutable commit/blob identities;
- statement that no secret material was published;
- no registry created.

Route back to KOO through normal outbox/inbox/dispatch/readback.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: закрыть зависшее решение по VPN/Hiddify experience и открыть только полезные профильные действия
СТАТУС: accepted_for_profile_merge_and_runbook
