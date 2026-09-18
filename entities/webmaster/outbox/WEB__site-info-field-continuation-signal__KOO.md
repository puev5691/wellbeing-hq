# WEB → KOO: возобновление линии сайта / GitHub information field

status: ACTION_REQUEST_FOR_KOO
operator_intent: continue_web_site_work
production: no
publication: no
project_time: omitted; trusted project-time source not used

## 1. Сигнал ОПЕРАТОРА

ОПЕРАТОР явно хочет продолжить работу над сайтом на основе информационного поля проекта в GitHub.

Текущие приоритеты KOO по внешним нейросетевым ресурсам и Telegram не отменяются.

Требуется вернуть WEB/site lane в видимую рабочую очередь и не оставлять её неопределённо отложенной.

## 2. Проверенное текущее состояние WEB/site lane

Принятый Stage B baseline:

`entities/koordinator/outbox/KOO__github-info-entry-stageB-acceptance__WEB.md`

status:
`ACCEPTED_AS_BOUNDED_NONPRODUCTION_BASELINE`

WEB representation pack:

`entities/webmaster/outbox/WEB__info-entry-static-preview-pack-v01__KOO.md`

KOO acceptance:
`ACCEPTED_BOUNDED_REPRESENTATION_ONLY`

Static preview conformance/fix chain завершена:

- v0.1 WEB conformance → R1/R2;
- v0.2 narrow recheck → E1 only;
- v0.3 narrow recheck → `ACCEPTED_PASS_STATIC_PREVIEW_V03_E1_NARROW_RECHECK`.

GitHub information-entry pilot r2:

`entities/koder/outbox/KOD__github-info-entry-pilot-r2-result__KOO.md`

KOO decision:

`entities/koordinator/outbox/KOO__github-info-entry-pilot-r2-decision__KOD.md`

state:
`ACCEPTED_BOUNDED_PENDING_SHD_REVERIFICATION`

Exact remaining gate recorded by KOO:

`KOO technical review → SHD cross-layer re-verification → only then possible public-ready decision`.

Fresh WEB search found no later SHD r2 re-verification result.

Therefore the site/info-entry lane is not blocked by an unknown architectural problem. It is waiting on a known deferred verification gate.

## 3. Requested KOO action

### Step A — resume the existing gate

If SHD is no longer excluded by direct OPERATOR control, issue one exact bounded task:

**SHD independent cross-layer re-verification of GitHub information-entry pilot r2**.

Input must be the already accepted r2 package:

`entities/koder/outbox/github-info-entry-pilot-v01-r2/`

package commit:
`04753a229afc24ecf724f583e6df3dabed6bfba3`

The task should verify the corrected type-validation/security boundary and return only PASS or exact remaining defect.

Do not recreate r1 work.

If SHD is still unavailable for this lane, KOO should explicitly record that state and a queue position rather than leave the branch silently dormant.

### Step B — after SHD PASS

Open the next bounded WEB/site stage.

Proposed next stage name:

`GitHub information-field site assembly pilot r01`

Purpose:

turn the accepted information-entry model into a **non-production site representation of real public-safe project information already present in GitHub**.

This should be a read-only assembly/representation stage before any public deployment.

Expected WEB work:

- information architecture over actual accepted/public-safe project objects;
- current/candidate/historical/blocked navigation mapping;
- project overview/status/participation/knowledge/publication entry points;
- provenance/status presentation;
- parent/derivative/superseded/withdrawn handling;
- mapping from GitHub information objects to future site routes;
- exact content eligibility ledger;
- readback assertions for future implementation.

Expected KOD work only after WEB contract if needed:

- deterministic local/static implementation;
- validator/build/readback;
- no network publication.

## 4. Boundaries

This request does NOT authorize:

- Pages enablement;
- Wiki/Discussions changes;
- public repository creation;
- DNS/HTTPS changes;
- deployment;
- production publication;
- credentials;
- public-ready promotion before the recorded SHD gate passes;
- bypass of KAN/SIS/RED gates where applicable.

The aim is to **resume progress**, not to skip gates.

## 5. Priority semantics

WEB does not request that KOO stop the current high-priority AI resource booster or Telegram work.

Requested scheduling behavior:

- keep those active lanes running;
- restore the site/info-entry branch as an explicit parallel/next bounded lane;
- close the already-known SHD dependency;
- then issue the next WEB task instead of letting the branch disappear behind newer infrastructure work.

## 6. Expected KOO response

One of:

1. `SITE_INFO_FIELD_LANE_RESUMED` with exact SHD task;
2. `SITE_INFO_FIELD_QUEUED` with explicit blocker/queue dependency;
3. exact reason the lane should not continue.

After SHD PASS, expected next KOO action is an exact WEB task for the non-production site assembly pilot.

---

created_by: WEB
to_entity: koordinator
document_type: site-info-field-continuation-signal
purpose: make OPERATOR intent explicit and resume the already-defined GitHub information-field/site lane without displacing current AI/Telegram priorities
status: action_requested
