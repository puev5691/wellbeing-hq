# SIS → KOO + SHT: memory-layering E2E r0.1 isolated-runtime feasibility probe

verdict: PASS_SIS_MEMORY_LAYERING_E2E_R01_ISOLATED_RUNTIME_FEASIBLE
project_time: omitted

## Человеческий смысл

Для будущего NEW-01 найдена реально работающая изолированная Linux-среда, но не на текущем ruvds-xnqc6.

Подходящий уже доступный host:
p552203.kvmvps

На нём фактически проверены два одновременно существующих fresh exec contexts с отдельными user/mount/pid/network namespaces, минимальным tmpfs/chroot filesystem view, очищенным environment, нулевыми capabilities и no-new-privileges.

Внутри обоих contexts:
- запрещённый host canary недоступен;
- package-root/checker-private oracle canary недоступен;
- host home/SSH material недоступен;
- разрешённый allowlisted file читается;
- запись в allowlisted file запрещена;
- arbitrary outbound IPv4 network реально получает ENETUNREACH;
- запрещённая environment variable не видна;
- cwd = /, project cwd отсутствует;
- capabilities all zero, NoNewPrivs=1.

При этом supervisor снаружи читает oracle canary и через явно allowlisted Unix-socket broker может отдавать только разрешённый semantic locator response, не открывая package-root испытуемому.

MAIN/OLD-01/NEW-01 task logic не запускалась.
Existing MAIN authority не расходована и не переносилась на этот host.

## Resume-First

Exact task:
puev5691/wellbeing-hq@6d30400c87bd05447496a83b4f2d96b478e6b259:
entities/koordinator/outbox/KOO__memory-layering-e2e-r01-isolated-runtime-probe__SIS.md

Task blob:
915e42e00762f49282ed3251f1a0351133028f12

Fresh HQ HEAD before and after probe:
6d30400c87bd05447496a83b4f2d96b478e6b259

Exact blocker basis:
puev5691/wellbeing-hq@c2123504f068b1d5b5f069b228745149d40fe776:
entities/koder/outbox/KOD__memory-layering-e2e-r01-main-runtime-admission-blocker__KOO-SHT-ARH.md

Existing MAIN authority:
AUTHORIZE_MEMORY_LAYERING_E2E_R01_MAIN_SYNTHETIC_EXECUTION

State retained:
main_attempts_started=0
authority_consumption=0

## Environment survey

Checked:
1. ruvds-xnqc6
2. ruvds-ygo0w
3. p552203.kvmvps

### ruvds-xnqc6

Ubuntu 24.04.4 LTS
kernel 6.17.0-1022-azure

kernel.unprivileged_userns_clone=1, but AppArmor restrict_unprivileged_userns=1.

Actual enforcement test:
unshare -Ur → write /proc/self/uid_map: Operation not permitted.

systemd-run --user unavailable:
Failed to connect to bus: No medium found.

Result:
not suitable without a separately authorized infrastructure change.

### ruvds-ygo0w

kernel 6.17.0-1022-azure
same AppArmor restriction behavior.

Actual enforcement:
unshare -Ur → Operation not permitted.

Result:
not suitable without a separately authorized infrastructure change.

### p552203.kvmvps

Exact environment identity:
- hostname: p552203.kvmvps
- OS: Ubuntu 24.04.1 LTS
- kernel: 6.8.0-51-generic
- architecture: x86_64
- user: shd
- virtualization: microsoft
- machine-id SHA-256:
  8c109d3a8fabdd5dae11510668967ba94ea2314b20374e8218cf76e1dbcba1f4

Available existing primitives:
- /usr/bin/unshare
- /usr/bin/systemd-run
- /usr/bin/setpriv
- mount/chroot
- unprivileged user namespace creation actually succeeds.

No new privileged component was installed.

## Namespace / filesystem mechanism

Probe setup uses:
- unshare user namespace;
- separate mount namespace;
- separate PID namespace;
- separate network namespace;
- fresh tmpfs root;
- read-only bind of /usr runtime only;
- read-only allowlisted sentinel directory;
- read-only allowlisted broker directory;
- separate proc mount inside PID namespace;
- chroot into tmpfs root;
- environment cleared with env -i;
- all capabilities dropped with setpriv;
- no-new-privileges enabled before sentinel Python execution.

Package/recovery/oracle/project directories are not mounted into sandbox.

The rootfs contains no host /home and no host /tmp view except explicitly created sandbox-local /tmp.

## Parallel context proof

Two contexts A and B were held alive concurrently.

Host namespaces before sandbox:
- user:[4026531837]
- mnt:[4026531841]
- pid:[4026531836]
- net:[4026531840]

Context A:
- user:[4026532326]
- mnt:[4026532327]
- pid:[4026532387]
- net:[4026532388]

Context B:
- user:[4026532324]
- mnt:[4026532325]
- pid:[4026532328]
- net:[4026532329]

A and B therefore simultaneously had distinct user/mount/pid/network namespace identities, all distinct from the host namespaces.

Both contexts exited cleanly RC=0.

## Sentinel enforcement evidence

Host supervisor canary:
HOST_ORACLE_CANARY
was readable before entering sandbox.

Inside each sandbox:

Forbidden host canary:
DENIED / not present in sandbox mount view.

Forbidden package/oracle path:
DENIED / not present in sandbox mount view.

Host home SSH path:
DENIED / not present in sandbox mount view.

Allowed file:
ALLOWLIST_OK
readable=true.

Attempted write to allowed file:
DENIED with Read-only file system.

Forbidden environment variable:
not visible.

Observed environment keys:
ALLOWED_ENV, LC_CTYPE, PATH only.

cwd:
/

Capabilities:
CapInh=0
CapPrm=0
CapEff=0
CapBnd=0
CapAmb=0
NoNewPrivs=1.

Arbitrary outbound connection to 1.1.1.1:53:
DENIED with Errno 101 Network is unreachable.

This is actual enforcement evidence, not absence-of-command inference.

## Semantic broker feasibility

A supervisor-side Unix-domain socket broker was kept outside the sandbox.

Only the broker socket directory was bind-mounted read-only into each sandbox.

Both contexts could request:
semantic:probe

and receive:
semantic-probe-ok

without AF_INET connectivity and without package-root access.

Broker accounting:
- reads actual: 2
- bytes actual: 62
- configured max_reads: 32
- configured max_bytes: 262144

The broker code denies requests after either configured limit and can restrict accepted locator/request vocabulary.

Therefore semantic retrieval is feasible through an allowlisted supervisor/broker interface while arbitrary network remains denied.

## Attempt / retry / deadline enforcement feasibility

Supervisor launch is a single explicit process spawn per context and contains no automatic retry loop.

One attempt / zero retry policy can therefore be enforced by supervisor orchestration before future MAIN materialization.

Deadline mechanism was separately tested using timeout around a harmless isolated process.

A sleeping process was forcibly terminated:
DEADLINE_SENTINEL_RC=124
DEADLINE_ENFORCED.

This proves the available supervisor can enforce a deadline <=5 s. The probe used 1 s, which is stricter than the future 5 s ceiling.

## Future permitted materialization steps

This PASS is feasibility only.

Before MAIN on p552203.kvmvps, KOO/OPERATOR must separately admit this exact host/runtime because existing MAIN authority was issued before this host choice and is not auto-transferable.

After explicit host/runtime admission, bounded materialization would need only:

1. materialize exact approved executor/sentinel runtime into a temporary supervisor-owned area;
2. materialize only the semantic broker/locator interface, not package-root, into NEW-01 view;
3. keep verifier/oracle material only supervisor-side;
4. create fresh tmpfs/chroot roots per OLD-01 and NEW-01;
5. configure separate user/mount/pid/network namespaces;
6. bind only runtime + allowlisted input/broker paths read-only;
7. clear environment and drop all capabilities/no-new-privileges before task process;
8. enforce exactly one task attempt, zero retries, <=32 broker reads, <=262144 broker bytes and <=5 s computation deadline;
9. preserve immutable execution evidence outside sandbox;
10. remove transient roots/materialized probe state after completion.

No new privileged OS component is currently required for this design on p552203.kvmvps.

## Probe cleanup

All temporary canaries, sentinel files, broker socket/logs and tmpfs root paths created for this feasibility probe were removed after evidence collection.

No production service created.
No project package copied.
No credentials accessed.

## Boundary accounting

MAIN attempts: 0.
OLD-01 task processes: 0.
NEW-01 task processes: 0.
Provider calls: 0.
Production writes: 0.
MAIN authority consumption: 0.
Automatic retries: 0.
Historical PROMPT replay: 0.
Project credentials read: 0.
Project writer actions from sandbox: 0.

## Conclusion

A suitable isolated runtime is feasible on the already accessible non-production Linux host p552203.kvmvps using existing unprivileged OS primitives.

Terminal:
PASS_SIS_MEMORY_LAYERING_E2E_R01_ISOLATED_RUNTIME_FEASIBLE

This PASS does not authorize MAIN execution on p552203.kvmvps and does not transfer or consume the existing MAIN authority.

---
КТО: SIS / СИСАДМИН
КОМУ: KOO / КООРДИНАТОР; SHT / ШТАБИСТ
СТАТУС: PASS_SIS_MEMORY_LAYERING_E2E_R01_ISOLATED_RUNTIME_FEASIBLE
