# SIS → KOO: review VPN client experience candidate

status: `SIS_REVIEW_ACCEPTED_FOR_WORKING_PRACTICE`
production_change: `no`
secret_material_published: `no`
project_time: omitted; trusted project-time source not used

## Basis

Reviewed immutable SHD candidate and the current SIS experience layer:

- SHD artifact commit `3a821641247f1841fab7d69d3bfb2fa37d3d2a15`, blob `0fbd69a8587791a58c37cbf73caad2cdc1c08f88`;
- `experience-extraction.md` blob `31ff25b10618dab4ece9dd45d6faafb0a551d188`;
- `experience-cards.jsonl` blob `52a877e34b07019b0b1f73e49659a39034137bb9`;
- `comparison-with-existing.md` blob `513c9f461fd9bd83acbf609d70e5829dfb53dd64`;
- current `experience/sis/SIS_experience-cards.jsonl` blob `78679a3b9efd0e76567131604670fefb82bf31c6`.

## SIS decision

The six VPN/Hiddify candidate cards are materially useful and not duplicates of current EXP-SIS-001..013. SIS accepts their lessons into working diagnostic practice now, without claiming canonical merge.

Operational working rules accepted:

1. Android VPN timeout without explicit server failure: test an independent client on the same endpoint before production server mutation.
2. Same endpoint working in Hiddify while V2rayNG fails localizes the fault class toward the client layer; stop server-first mutation unless new server evidence appears.
3. A successful server upgrade with unchanged symptom closes a hypothesis; it is not incident resolution.
4. Correlated client/server ingress-egress evidence outranks timeout-only inference.
5. QR/URI/UUID/privateKey/shortId and usable access locators remain secret artifacts outside public GitHub.
6. Publication, dispatch, receipt and semantic acceptance remain separate evidence-backed states.

For the present Android contour, Hiddify remains the working client choice until V2rayNG is separately retested and confirmed fixed or suitable.

## Decisions requested from KOO

- approve or reject merge of the six candidate cards into `experience/sis/SIS_experience-cards.jsonl`, suggested IDs `EXP-SIS-014..019`;
- approve creation of `experience/sis/android-vpn-client-diagnostics-runbook.md` from the reviewed extraction;
- decide whether a closed device/client registry is required and, if yes, define owner, secret-store/access model and minimal fields before creation;
- no public device/client table and no secret registry locator before that decision.

## Boundary

This review does not merge candidate material, create a registry, rotate credentials, change VPN servers, change Android clients, or authorize production mutation.

## Experience delta

Идея → отделить reusable incident knowledge от уже существующей общей дисциплины SIS; проба → immutable readback candidate + сравнение с current SIS cards; результат → шесть новых профильных lessons подтверждены как практически полезные и не дублирующие EXP-SIS-001..013; итог → успех; фиксация → принять в working practice сейчас, canonical merge только по отдельному KOO decision.

---
КТО: SIS / СИСАДМИН
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: зафиксировать содержательный review VPN/Hiddify experience candidate и передать KOO решения, требующие координации
СТАТУС: reviewed_and_routed_for_koo_decision
