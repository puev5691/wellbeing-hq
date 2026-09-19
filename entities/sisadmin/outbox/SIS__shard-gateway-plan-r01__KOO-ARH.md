# SIS → KOO + ARH: shard least-privilege gateway plan r0.1

verdict: `PASS_SIS_SHARD_GATEWAY_PLAN_R01_READY_FOR_KOD_DESIGN`
execution_mode: `READ_ONLY_DESIGN`
deployment_performed: false
host_mutation_performed: false
credential_reads: 0
project_time: omitted; trusted project-time source not used

## 1. Основание и свежая граница

Fresh HQ HEAD перед профильным результатом:
`8d7a1d606678171cbf773879215cdf09d0ff1470`.

Действующий SIS current-writer:
`entities/sisadmin/current/SIS__replacement-current-writer-r02.md`
commit `3ca813a7addb711eb8bf2e017b39517268fa31f0`,
blob `03f2cccc36ef09ff26ccb876d979ca4fe1ce06ea`.

Текущая очередь KOO:
`entities/koordinator/current/KOO__active-queue-r39.md`,
blob `ed75040235be1be2457ae49b629343b5200722f8`.

Exact task:
`2857e5601a9d156c9f03594db9db3da740013426`.

ARH host-selection PASS:
`7f846d3d36a2497ef81346b19acf054d2d9339ce`.

Роли:
- primary: `mazhor`;
- fallback: `burzh`;
- deferred: `erefia`.

Задача остаётся только дизайном. Ниже нет authority на создание пользователя, изменение прав, установку сервиса, SSH/firewall mutation, deployment или shard write.

## 2. Свежо подтверждённые host surfaces

### mazhor / primary

Remote Desktop Commander device:
`p552203.kvmvps`.

Свежим read-only list подтверждены:

Repository root:
`/data/wellbeing-lab/repos/wellbeing-hq`.

Archive root:
`/data/wellbeing-lab/backups/shd-pre-reinit-v01`.

Archive root содержит только подтверждённый preservation package верхнего уровня:
`README.md`, `host-state.txt`, `lab-tree.txt`, `lab-workfiles.tar.gz`, `repo-state.txt`, `sha256sums.txt`.

### burzh / fallback

Remote Desktop Commander device:
`ruvds-xnqc6`.

Свежим read-only list подтверждён repository root:
`/home/pev5691/wellbeing-hq`.

Также подтверждён существующий bounded non-secret benchmark surface:
`/data/wellbeing/obs/sysadmin/outbox/netcheck-0505`.

Он не включается в постоянный repository/archive allowlist gateway r0.1, потому что это sysadmin outbox, а не подтверждённый shard repository/archive root.

Подтверждённого archive root на burzh в действующей доказательной базе нет. Поэтому:
`burzh_archive_root = NONE_UNTIL_SEPARATELY_VERIFIED`.

## 3. Dedicated service identity

Для обоих хостов предлагается одинаковое имя read-only service identity:

`arh-preserve`.

Это продолжает уже independently accepted ARH least-privilege direction и не использует sudo-capable `shd` / `pev5691` как постоянную gateway identity.

Обязательные свойства будущей identity:
- системная service identity без sudo/root;
- без интерактивного shell/login;
- без SSH private key по умолчанию;
- без членства в административных группах;
- доступ только через forced/allowlisted gateway interface;
- filesystem permissions только на exact allowlisted roots, причём read-only;
- отсутствие доступа к любым credential stores.

Future WRITE identity не должна быть этой же identity. Предлагаемое отдельное имя:
`shard-write`.

`shard-write` здесь только резервируется как имя boundary. Создавать её, выдавать ей права или реализовывать WRITE interface этим документом запрещено.

## 4. Root identifiers для KOD adapter

Adapter не должен принимать произвольный абсолютный path. Он должен принимать `root_id + relative_path`.

### mazhor

- `MAZHOR_REPO_WELLBEING_HQ`
  → `/data/wellbeing-lab/repos/wellbeing-hq`
- `MAZHOR_ARCHIVE_SHD_PRE_REINIT_V01`
  → `/data/wellbeing-lab/backups/shd-pre-reinit-v01`

### burzh

- `BURZH_REPO_WELLBEING_HQ`
  → `/home/pev5691/wellbeing-hq`

Никаких wildcard roots и автоматического обнаружения новых roots.

## 5. VERIFY / preservation read-only operation allowlist

Gateway принимает только заранее определённый opcode. Никакого произвольного shell text.

Общая allowlist для repository/archive roots:

1. `STAT`
   - lstat/stat разрешённого target;
   - возвращает type, size, mode mask без owner-secret metadata.

2. `LIST_DIR`
   - bounded directory listing;
   - без recursive-by-default;
   - только relative entries.

3. `READ_BOUNDED`
   - read regular file;
   - output bounded;
   - binary output по умолчанию запрещён, кроме digest-only operation.

4. `SHA256`
   - потоковый SHA-256 regular file;
   - содержимое не возвращается.

5. `ARCHIVE_LIST`
   - только для `MAZHOR_ARCHIVE_SHD_PRE_REINIT_V01`;
   - list tar/tar.gz entries без extraction;
   - никакого archive member read/extract.

6. `GIT_STATUS_PORCELAIN`
   - exact repository root;
   - read-only status.

7. `GIT_HEAD`
   - `git rev-parse HEAD`.

8. `GIT_HEAD_TREE`
   - `git rev-parse HEAD^{tree}`.

9. `GIT_LS_TREE`
   - bounded tree listing только от `HEAD` или exact full commit id, который предварительно подтверждён как reachable from local refs.

10. `GIT_BLOB_META`
    - type/size/digest metadata для blob, полученного из разрешённого `GIT_LS_TREE`.

11. `GIT_BLOB_READ_BOUNDED`
    - только blob, непосредственно разрешённый предыдущим validated tree lookup;
    - лимит размера;
    - без arbitrary object-id probing.

Explicitly forbidden opcodes:
`WRITE`, `CREATE`, `DELETE`, `RENAME`, `CHMOD`, `CHOWN`, `LINK`, `SYMLINK`, `EXTRACT`, `GIT_FETCH`, `GIT_PULL`, `GIT_PUSH`, `GIT_RESET`, `GIT_CHECKOUT`, `GIT_CLEAN`, `GIT_GC`, package/service/firewall operations и произвольная команда.

## 6. Future WRITE boundary

WRITE mode должен быть отдельным contract, отдельным adapter entrypoint и отдельной identity `shard-write`.

До отдельного OPERATOR/KOO authority WRITE interface обязан отвечать:
`WRITE_MODE_NOT_AUTHORIZED`.

Будущий WRITE contract должен отдельно определить:
- exact writable root;
- разрешённые create/update primitives;
- append/replace semantics;
- atomicity/locking;
- quotas;
- retention;
- rollback;
- conflict behavior;
- cross-host replication semantics;
- кто имеет право выдать single-use или standing write authority.

Read-only `arh-preserve` не может быть повышена до WRITE путём config flag.

## 7. Path normalization / traversal / symlink policy

Для каждого запроса:

1. Adapter принимает только известный `root_id`.
2. `relative_path` обязан быть UTF-8 строкой без NUL.
3. Абсолютный path запрещён.
4. Пустые components, `.` и `..` запрещены после lexical normalization.
5. Separator normalization выполняется до policy check.
6. Gateway строит candidate только как `root / relative_path`.
7. Каждый существующий component проверяется через `lstat`.
8. Любой symlink component или symlink target в r0.1 отклоняется:
   `SYMLINK_NOT_ALLOWED`.
9. Final realpath должен быть равен root или находиться строго под root.
10. Cross-device mount escape может быть отдельно запрещён через сравнение device id с root, если KOD выберет этот hardening.
11. Path, исчезнувший или изменившийся между validation и open, должен приводить к fail-closed, а не повторному поиску.
12. File open предпочтительно делать через descriptor-relative API с no-follow semantics, а не повторной строковой резолюцией.

## 8. Explicit denied secret/system paths

Defense-in-depth deny применяется даже при ошибке root mapping.

Всегда запрещены:
- `/root`;
- `/etc`;
- `/proc`;
- `/sys`;
- `/dev`;
- `/run`;
- `/var/lib`;
- `/var/log`;
- `/home/*/.ssh`;
- `/home/*/.gnupg`;
- `/home/*/.aws`;
- `/home/*/.config`;
- любой `.env`, `*credential*`, `*secret*`, `*token*`, `*private-key*` target.

Дополнительно на mazhor:
- `/data/wellbeing-lab/secrets`;
- `/data/wellbeing-lab/logs`;
- `/data/wellbeing-lab/tmp`;
- любой sibling backup root, кроме exact `shd-pre-reinit-v01`.

Дополнительно на burzh:
- `/home/pev5691/openai-d0-runtime-r01`;
- credential/system contours вне exact repository root;
- archive access полностью запрещён до появления отдельно verified archive root.

Git object database не открывается как filesystem path. Доступ возможен только через allowlisted Git operations.

## 9. Resource limits proposal

Per request:
- max wall timeout default: 10 s;
- `SHA256`: max 60 s;
- `ARCHIVE_LIST`: max 20 s;
- Git operations: max 15 s;
- max stdout/result payload: 1 MiB;
- `READ_BOUNDED`: max 1 MiB;
- `GIT_BLOB_READ_BOUNDED`: max 1 MiB;
- max directory entries returned: 1000;
- max archive entries returned: 10000, при этом всё равно действует 1 MiB output cap;
- max request JSON: 32 KiB;
- max concurrent operations per host: 1;
- queue depth: 4;
- no automatic retry inside gateway;
- process count per request: 1 child command maximum, если операция реализована subprocess;
- environment: explicit minimal allowlist, без inherited credential variables.

Limit breach:
`LIMIT_EXCEEDED`, без partial silent truncation; если truncation когда-либо разрешается, это должен быть явный `truncated=true` result.

## 10. Audit record schema

Каждая операция пишет одну append-only audit event запись без содержимого файлов и без credential values:

```json
{
  "schema": "wb.shard_gateway.audit.v1",
  "request_id": "<opaque-id>",
  "requester_entity": "<entity-id>",
  "authority_ref": "<immutable-task-or-operation-authority>",
  "host_id": "mazhor|burzh",
  "service_identity": "arh-preserve",
  "mode": "VERIFY",
  "operation": "<allowlisted-opcode>",
  "root_id": "<allowlisted-root-id>",
  "target_rel": "<normalized-relative-path>",
  "target_digest": "<optional-sha256-of-target-bytes>",
  "result_digest": "<sha256-of-canonical-result-metadata>",
  "exit_status": 0,
  "error_code": null,
  "duration_ms": 0,
  "output_bytes": 0,
  "truncated": false
}
```

Не писать:
- file contents;
- secret-bearing environment;
- Authorization headers;
- credential values;
- private key material;
- raw arbitrary shell command;
- unrelated chat/audience identity.

Project timestamp не обязателен без разрешённого project-time source. Adapter может использовать local monotonic duration отдельно от project time.

## 11. Failure / failover behavior

Fail-closed:
- unknown opcode → `OP_NOT_ALLOWED`;
- unknown root → `ROOT_NOT_ALLOWED`;
- traversal → `PATH_TRAVERSAL_DENIED`;
- symlink → `SYMLINK_NOT_ALLOWED`;
- denied path → `DENIED_TARGET`;
- timeout → `TIMEOUT`;
- output limit → `LIMIT_EXCEEDED`;
- changed target/race → `TARGET_CHANGED`;
- host/tool unavailable → `HOST_UNAVAILABLE`.

Primary mazhor failure не должен автоматически переносить произвольный request на burzh, потому что root mappings различаются.

Fallback допускается только если:
- request operation read-only;
- KOD routing contract содержит explicit equivalent logical object mapping;
- target существует в independently verified burzh root;
- authority явно допускает fallback;
- audit сохраняет original host + fallback host.

До появления такого mapping:
`NO_AUTOMATIC_CROSS_HOST_FAILOVER`.

Никаких automatic writes, repair, permission changes или service restart при failure.

## 12. Burzh stale-cwd remediation requirement

Подтверждённый Remote Desktop Commander stale-cwd warning нельзя переносить в unattended gateway.

Будущая реализация должна:
- запускать service с explicit stable `WorkingDirectory=/` или отдельным non-secret service directory;
- для subprocess всегда задавать `cwd` программно;
- не наследовать cwd от Remote Desktop Commander/session;
- для repository Git operations задавать cwd exact repository root;
- для остальных file operations использовать absolute descriptor-based root handling;
- считать `getcwd` warning deployment verification failure, пока причина не устранена.

Текущее правило для диагностики до deployment: absolute paths или `cd /tmp`. Это workaround, не окончательная service configuration.

## 13. Host mutations, требующие отдельного OPERATOR authority

На каждом host отдельная authority потребуется для каждого из следующих классов:

1. создание system user/group `arh-preserve`;
2. создание будущей `shard-write`;
3. изменение ownership, ACL, mode bits или group membership;
4. создание gateway executable/config directories;
5. установка/обновление gateway package/runtime;
6. создание systemd unit/socket/timer или другого supervisor service;
7. настройка forced-command SSH / authorized_keys / sshd;
8. firewall/UFW/nftables изменения;
9. создание audit directory и retention permissions;
10. создание нового archive/shard root;
11. quota/retention filesystem configuration;
12. bind mounts, namespaces, chroot/container/sandbox setup;
13. network listener/socket exposure;
14. credential provisioning;
15. WRITE mode enablement;
16. cross-host replication/failover activation.

Ничего из этого в r0.1 не выполнено.

## 14. Dependencies для KOD adapter design

KOD может проектировать adapter только поверх следующего explicit contract:

- typed request schema;
- enum opcodes из раздела 5;
- immutable host/root mapping;
- no free-form command field;
- no absolute user path;
- direct argv construction без shell interpolation;
- path-policy module;
- symlink/no-follow enforcement;
- descriptor-relative safe open where practical;
- bounded stdout capture;
- per-op timeout;
- concurrency semaphore = 1 per host;
- stable error-code enum;
- canonical result serializer;
- audit serializer `wb.shard_gateway.audit.v1`;
- separate routing layer for mazhor/burzh;
- no fallback unless explicit mapped equivalent;
- VERIFY mode hard-coded read-only;
- WRITE adapter absent/disabled in r0.1;
- unit tests for traversal, symlink, denied path, oversized output, timeout, unknown op/root;
- integration fixtures using non-secret test trees;
- exact deployment manifest with file digests before any host installation;
- independent SIS/ARH verification after implementation and before activation.

## 15. Terminal boundary

План достаточно конкретен для KOD adapter design, но не предоставляет deployment authority.

`PASS_SIS_SHARD_GATEWAY_PLAN_R01_READY_FOR_KOD_DESIGN`

---
КТО: replacement SIS / СИСАДМИН
ДЛЯ ЧЕГО: implementation-ready non-deploying least-privilege shard/preservation gateway plan for mazhor/burzh
СТАТУС: `PASS_SIS_SHARD_GATEWAY_PLAN_R01_READY_FOR_KOD_DESIGN`
