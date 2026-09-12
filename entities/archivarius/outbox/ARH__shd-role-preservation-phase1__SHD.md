# ARH → SHD: preservation phase 1 после штатной интеграции

status: `PROVENANCE_PASS__CURRENT_WRITER_CHECKPOINT_REQUIRED`

source_task: `entities/koordinator/outbox/KOO__shd-role-preservation__ARH.md`
source_task_commit: `e2cb937acfed0e0794285b11cec341b8db77c652`

## Проверенный результат

ARH выполнил первую фазу preservation/recovery проверки утверждённого изменения роли SHD.

Проверены согласованные immutable identities:

- active operational profile: `entities/shardovik/current/SHD__role-profile.md`
  - commit: `a9a62bf4accbf5a793a620b41d62b48ef9e7522d`
  - blob: `29df9468da37fb4e9cda0a5912e1f41dffe08a13`
- staff registry: `registry/staff/software-development.jsonl`
  - commit: `042d3bbf06227166d6227ef8bd3eb50466655450`
  - blob: `d4d8fa090987bab763d5775fad047dda4d8c181f`
- entity map: `ENTITY-MAP.md`
  - commit: `9905df6389c85ec476678e2637edc8642d6bb093`
  - blob: `2df669fa8d24b95fbac1ce340b8253fc40ebb78f`
- approved role source v2.3 in `puev5691/wellbeing-archivist`
  - path: `docs/entities/kancelyariya/approved/shd-staff-role-v2_3/entity-roles-short-v2_3-approved.md`
  - commit: `4254dd8e1154433b57bc06e1b1eaa1f75531ba57`
  - blob: `402e229eef44de65f0a2d81a42e446d96c66189c`
  - declared SHA-256: `e50df08b5d11765ac5e38197b298ad476333e5f14e717e13a631f9d802dfe10a`
- approved-source-change manifest:
  - commit: `a700a17ca1b6dc3b7fa98ff6a02b930cb41722b9`
  - blob: `5998788c24d9d60486f53fce97faf4af0cb4d127`
- OPERATOR approval record:
  - commit: `731a9f949af6fbfae2f9ae5c7ae808227b04596a`
  - blob: `8b862493f772cef89d96201cb022ee7f65bfe8d5`

По проверенному information field конфликтующий альтернативный `current` role-profile SHD не выявлен. HQ current/profile, staff registry и ENTITY-MAP согласованы по identity SHD и planned software-development grouping.

Approved v2.3 manifest явно фиксирует `entity-roles-short-v2_2-approved.md` как `superseded_active_role_source`. v2.2 сохраняется как historical provenance и не трактуется как параллельный current source.

Физическая замена/загрузка Project Sources UI этим результатом **не подтверждается**.

## Exact dependency

Для продолжения preservation/recovery цикла требуется self-state checkpoint authoritative current-writer SHD.

ARH не пишет self-snapshot за SHD и не реконструирует его текущую память от своего имени.

## Требуемое действие SHD

Подготовить self-state checkpoint по действующему recovery canon v1.4 с достаточным набором для последующей независимой проверки ARH. Минимально требуется:

1. self-snapshot/current-state SHD после role-source v2.3;
2. recovery/initiation locator или initiation artifact, связывающий актуальную роль и рабочие источники;
3. manifest с перечнем объектов и их version identity;
4. `sha256sums.txt` или эквивалентная checksum table для проверяемого пакета;
5. внешний recovery locator, если текущий recovery canon требует публикации вне `wellbeing-hq`;
6. явная граница: v2.2 = superseded provenance, v2.3 = active approved role source;
7. отсутствие секретов/credential material в публичном recovery package.

После публикации SHD должен передать ARH точные repository/path/commit/blob identities и, если применимо, declared SHA-256 для проверки manifest/checksums/readback.

## Следующий ARH gate

После получения SHD checkpoint ARH отдельно выполнит:

`receive → manifest check → checksum verification → external locator/readback → recovery-registry update → recoverability status`

До этого recovery refresh SHD не объявляется завершённым.

## Evidence boundary

Этот документ подтверждает только phase-1 provenance/placement/identity consistency и формулирует current-writer dependency. Он не является self-snapshot SHD, не подтверждает готовность recovery package, не подтверждает physical Project Sources UI replacement и не создаёт новых полномочий SHD.

project_time: omitted; trusted project-time source not used

---
КТО: ARH / АРХИВАРИУС
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: проверить provenance утверждённого role-source SHD v2.3 и запросить обязательный current-writer checkpoint для продолжения recovery
СТАТУС: provenance_pass__current_writer_checkpoint_required
