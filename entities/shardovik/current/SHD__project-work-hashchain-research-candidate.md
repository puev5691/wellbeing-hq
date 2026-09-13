# SHD / ШАРДОВИК: research candidate — blockchain hashchain для технической работы проекта

Кратко: ОПЕРАТОР предложил исследовать отдельный blockchain/hashchain-контур, который фиксирует не содержание технической работы проекта, а проверяемые хэши, locators и lineage артефактов. Идея рассматривается как research candidate для SHD/WBN/TERA2 экспериментов, не как утверждённая архитектура, production deployment или tokenomics decision.

## 1. Исходная идея ОПЕРАТОРА

Смысл вводной:

- GitHub information field уже хранит много технических артефактов, но нуждается в проверяемой immutable фиксации;
- блокчейн можно использовать как слой хэширования информации о технической работе проекта;
- корневой blockchain должен якорить основополагающую информацию проекта;
- корневой слой может быть медленным и устойчивым;
- быстрые шарды могут использоваться для рабочих потоков, мероприятий, сеансов связи, экспериментов и временных задач;
- TERA-derived подход и возможность шардов делают эту идею пригодной для лабораторной проверки;
- цель сейчас: поиграться с идеей и проверить, где она полезна, а где превращается в дорогой культ хэша.

## 2. Рабочее название

```text
Project Work Hashchain / PWH
```

Варианты русских названий:

```text
Цепь доказательств проекта
Журнал хэшей технической работы
Корневая цепь доверия ШТАБА
```

Рабочее короткое имя для эксперимента:

```text
pwh-root
```

## 3. Базовая архитектурная гипотеза

GitHub остаётся readable information field: там лежат Markdown, JSONL, scripts, manifests, reports, dispatch и receipts.

Blockchain/hashchain не хранит всё содержимое. Он хранит:

```text
artifact_id
repository/path/ref
commit_sha
blob_sha или content_sha256
source_hash
previous_hash / parent_hashes
event_type
sender
recipient
status_class
timestamp, если есть доверенный источник времени
signature/author marker, если появится утверждённый signing flow
```

То есть blockchain не заменяет GitHub. Он создаёт tamper-evident layer поверх GitHub-артефактов.

## 4. Root chain и shard model

### Root chain

Назначение root chain:

- anchor active Project Sources;
- anchor approved role sources;
- anchor recovery checkpoints;
- anchor official registry snapshots;
- anchor important route/receipt milestones;
- anchor summaries of shard sessions.

Root chain должен быть редким, медленным и строгим. Скорость не является целью root chain. Цель — устойчивость, простота проверки и минимальный canonical surface.

### Fast shards

Назначение быстрых шардов:

- session-scoped technical work;
- incident diagnostics;
- экспериментальные chains для WBN/TERA2;
- временные хэши больших рабочих потоков;
- event/meeting shards;
- high-frequency task/receipt streams.

Shard может жить коротко, затем завершаться root-anchor записью:

```text
shard_id
shard_genesis_hash
shard_final_hash
range_of_events
manifest_hash
root_anchor_hash
```

## 5. Первые use cases

### 5.1. Project Source anchoring

Каждая утверждённая версия Project Source получает запись:

```json
{
  "event_type": "project_source_anchor",
  "source_name": "entity-roles-short-v2_3-approved.md",
  "sha256": "...",
  "approved_by": "OPERATOR",
  "locator": "wellbeing-archivist:docs/...",
  "supersedes": "entity-roles-short-v2_2-approved.md"
}
```

### 5.2. Recovery checkpoint anchoring

Каждый recovery package фиксируется root/hashchain записью:

```json
{
  "event_type": "recovery_checkpoint_anchor",
  "entity": "SHD",
  "package_id": "SHD-role-v2_3-current-recovery",
  "manifest_hash": "...",
  "checksum_file_hash": "...",
  "external_locator": "wellbeing-entity-bootstrap:packages/...",
  "status": "published_for_ARH_verification"
}
```

### 5.3. Dispatch / receipt lineage

Каждая важная межсущностная передача может иметь event:

```json
{
  "event_type": "dispatch_anchor",
  "sender": "shardovik",
  "recipient": "archivarius",
  "artifact": "entities/shardovik/outbox/...md",
  "artifact_commit": "...",
  "dispatch": "routes/dispatch/...md",
  "status": "dispatched"
}
```

Receipt добавляется отдельным событием, а acceptance отдельным. Нельзя смешивать эти состояния, иначе получится blockchain, который неизменно доказывает путаницу. Печально, но типично.

## 6. Связь с COOP/WBN/TERA2 fit-gap

Эта идея пересекается с KOD handoff по COOP rights/state-transition fit-gap:

- нельзя выводить governance rights из account/pubkey ownership;
- технический hash/locator не равен праву, компетенции или полномочию;
- текущие TERA-derived structures, по handoff KOD, не подтверждают полный COOP transition model;
- WBN network/shard identity может быть technical object locator;
- exact WBNP on-chain/token/smart identity пока UNKNOWN;
- runtime/source parity с upstream TERA2 требует отдельной проверки.

Вывод: PWH может быть техническим evidence layer, но не governance system сам по себе.

## 7. Главная опасность идеи

Хэш доказывает только, что конкретные bytes/structure существовали в конкретной версии и не изменились без следа.

Хэш не доказывает:

- истинность содержимого;
- качество решения;
- правомерность действия;
- receipt;
- acceptance;
- полномочия автора;
- причинность между событиями, если она не смоделирована явно;
- что GitHub locator был доступен адресату;
- что runtime реально соответствовал source.

Поэтому PWH должен быть ledger of evidence, не оракул истины. Люди и так любят молиться на числа, не надо им ещё блокчейн-икону подсовывать.

## 8. Минимальный эксперимент на lab-01

Первый эксперимент не должен требовать production blockchain.

Stage 0:

```text
create local append-only JSONL hashchain
source: selected GitHub artifacts
fields: event_id, event_type, locator, commit, blob, sha256, prev_hash, event_hash
verify: recompute chain and detect tampering
```

Stage 1:

```text
anchor SHD recovery checkpoint
anchor KOD handoff receipt
anchor one dispatch/receipt pair
produce verification report
```

Stage 2:

```text
simulate root + shard:
root.jsonl
shards/<session-id>.jsonl
close shard by writing final shard hash into root
```

Stage 3:

```text
compare with TERA/WBN feasibility:
can TERA-derived shard/account/smart model store these anchors cleanly?
what must be sidecar/off-chain?
what remains UNKNOWN?
```

## 9. Candidate data model

```json
{
  "pwh_version": "0.1-candidate",
  "event_id": "PWH-SHD-0001",
  "event_type": "artifact_anchor",
  "scope": "root|shard",
  "shard_id": null,
  "subject_entity": "SHD",
  "artifact_locator": "puev5691/wellbeing-hq:entities/shardovik/current/SHD__recovery-checkpoint-current.md",
  "artifact_commit": "dafaa2e...",
  "artifact_blob": "849b7f...",
  "artifact_sha256": null,
  "parent_event_hashes": [],
  "prev_event_hash": "...",
  "event_payload_hash": "...",
  "event_hash": "...",
  "status_semantics": "dispatched|received|accepted|candidate|verified|blocked",
  "authority_boundary": "technical_evidence_only",
  "secret_boundary": "no_secrets_in_payload"
}
```

## 10. Вопросы для проверки

1. Что должно попадать в root chain, а что только в shard?
2. Должен ли root chain быть настоящим TERA/WBN chain или сначала хватит local hashchain?
3. Как фиксировать Project Source supersession без превращения старых версий в current truth?
4. Как хранить event_time, если проектный источник времени недоступен?
5. Кто имеет право писать root anchors: KOO, ARH, SIS, SHD, automated runner?
6. Нужна ли подпись автора события, и каким ключом?
7. Как не раскрывать secret locators, но доказать, что secret bundle существовал?
8. Как связать GitHub commit/blob SHA и content SHA-256 без ложного ощущения acceptance?
9. Какой минимальный proof нужен для cold-start нового чата?
10. Может ли TERA shard быть disposable session ledger, или проще начать с JSONL и только потом переносить в chain?

## 11. Рекомендация SHD

Начать не с TERA blockchain, а с local PWH prototype на `Мажор / lab-01`:

```text
phase A: JSONL hashchain over GitHub artifacts
phase B: root + ephemeral shard simulation
phase C: verification report
phase D: fit-gap against TERA/WBN implementation
phase E: decision whether to implement as real WBN/TERA shard
```

Так мы проверим смысл без запуска религиозного обряда вокруг ноды. Если JSONL-модель не дисциплинирует данные, blockchain тем более не спасёт.

## 12. Boundary

- This is a research candidate.
- No production node is touched.
- No tokenomics is introduced.
- No governance authority is inferred from hashes.
- No secrets are published.
- No TERA/WBN implementation claim is made before source/runtime parity and lab verification.

---
КТО: SHD / ШАРДОВИК
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: зафиксировать research candidate идеи project-work hashchain/root+shards для будущей проверки на lab-01
СТАТУС: research_candidate