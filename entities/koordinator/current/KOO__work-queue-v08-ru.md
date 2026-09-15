# КООРДИНАТОР — рабочая очередь v0.8

Статус: актуальная операторская очередь после свежей сверки.  
Это рабочий документ KOO, не канон проекта.  
Проектное время не указывается: доверенный источник проектного времени в этой сверке не использовался.

## Как работать ОПЕРАТОРУ

Не открывать inbox-файлы и не пересказывать задачи. Работать оконно: максимум четыре активных интерактивных Entity-чата одновременно. Когда один возвращает проверяемый результат или упирается в gate, его слот освобождается и в окно входит следующий подготовленный lane.

Это не технический лимит ChatGPT. Это операторский лимит для снижения ручного переключения контекста и ошибок маршрутизации.

## Human gate вне окна — KOD / КОДЕР

Новый экземпляр KOD успешно прошёл replacement initiation:
`entities/koder/outbox/KOD__replacement-initiation-v02-result__KOO.md`
commit `14272b4067069cd044cf10e1affab66858a74b12`.

KOO acceptance:
`routes/receipts/KOD__replacement-initiation-v02-result__KOO.receipt.md`
commit `dd45fcd015d50b8eb9e0175f2879bef6667c9a87`.

State:
- `initiation_verified`;
- новый экземпляр не current-writer;
- прежний verified KOD writer всё ещё не имеет retirement/replacement boundary;
- профильная работа нового KOD не разрешена до отдельного writer decision.

ОПЕРАТОР должен отдельно решить один вопрос: сохраняется ли прежний verified KOD current-writer либо он выводится из дальнейшей профильной работы и новый initiated instance получает право пройти writer-transfer gate.

Это решение не заменяется wake-промптом.

## Волна A — открыть сейчас, максимум 4 чата

### A1. ARH / АРХИВАРИУС

Exact input:
`KOO__entity-wake-initiation-resume-r04-narrow-recheck__ARH.md`

Task commit:
`fe3c71347736858101eff0f1e3123ea88e953baf`.

Цель: только narrow recovery recheck candidate r0.4 после интеграции R1–R3. При PASS ветка v1.5 выходит к финальному KOO/OPERATOR gate.

Не брать параллельно sender-registry sanitation defect `94158f2...`; он следующий ARH lane.

### A2. SHD / ШАРДОВИК

Exact input:
`KOO__tera2-main-genesis-root-research-r01__SHD.md`

Task commit:
`31a283417df2d499882456771cf0f70b0427bb71`.

Цель: read-only исследование точного upstream-механизма main/root genesis TERA2 для нового основного кластера.

Не лечить старый WBN fork, не запускать новый genesis, не менять старые DATA/DB/runtime.

### A3. WEB / ВЕБМАСТЕР

Exact input:
`KOO__info-entry-static-preview-v03-narrow-recheck__WEB.md`

Task commit:
`2e2a747596169d1e7467ef6e85e54fa87be519f2`.

Цель: независимая узкая перепроверка закрытия Static Preview E1 в KOD v0.3.

### A4. SIS / СИСАДМИН

Exact input:
`KOO__telegram-phase1b-resume-after-erefia-r05__SIS.md`

Task commit:
`81e686eee63ddbcf45a527345f58cf942068cdae`.

Цель: fresh resume-gate Telegram Phase1B после закрытия эРэФии.

Запрещён replay старого sudo только по факту его существования; live Telegram/public webhook/credentials/production не разрешены.

## Волна B — готова, запускать после освобождения слотов

### B1. SHT / ШТАБИСТ

Exact input:
`KOO__recovery-record-lifecycle-convention-r01__SHT.md`

Task commit:
`39bf92e53749ed677616aec271ce04213038f69d`.

Цель: reusable process convention для completed recovery records, которые семантически завершены, но лежат под `recovery-pending/`. Только process design; никаких move/delete/canon changes.

### B2. VOL / ВОЛОНТЁР

Exact input:
`KOO__p5-prospective-measurement-protocol-r01__VOL.md`

Task commit:
`761a9a480808db4db4f70b0bf5a11b225b3225dd`.

Цель: low-burden prospective measurement protocol для будущего реального P5 эпизода. Никаких ретроспективно выдуманных эффектов, денег, баллов, токенов, ownership или governance.

## Следующие уже известные lanes после результатов

ARH после r0.4 recheck:
- если PASS: KOO final integration → OPERATOR approval/reject gate v1.5;
- затем отдельно exact repair proven sender-registry append-only defect `94158f2...`;
- lifecycle sanitation по `recovery-pending` только после SHT convention/решения KOO.

KOD после writer decision/establishment:
1. activation-lineage schema F1/F2 correction;
2. sender-registry sanitation;
строго последовательно одним KOD current-writer.

WEB после narrow E1 recheck:
- PASS закрывает этот verification lane;
- FAIL возвращается KOD только exact defect, без общего redesign.

SHD после main/root genesis research:
- только после research PASS materialize deployment/design lane;
- runtime/new genesis запуск требует отдельного проверяемого task/authority.

SIS после Phase1B r0.5:
- если нужен human/sudo gate, вернуть один Termux block и остановиться;
- live Telegram остаётся отдельным gate.

## Спящие, которых сейчас не будить

RED / РЕДАКТОР: текущий speech working draft существует; следующая полезная редакция зависит от нового factual material и не требует wake ради занятости.

KAN / КАНЦЕЛЯРИЯ: authority review r0.2 завершён; новый authority lane появится только при материальном изменении после r0.4/OPERATOR gate.

KOD / КОДЕР: не спит в обычном смысле, а стоит на writer decision.

## Правило параллельности

Параллельно допускаются lanes разных Entity/current-writer domains без общей mutable target и без неразрешённой причинной зависимости.

Операторское окно: 4 активных интерактивных Entity-чата. Пятый и последующие не запрещены платформой, но переводятся в READY-резерв до освобождения слота, если нет особой срочности.

После каждого возвращённого результата KOO выполняет fresh GitHub-preflight и пересобирает окно. Inbox/dispatch/activation не означают RUNNING.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: организовать следующий проход как управляемое окно параллельных конвейеров без перегрузки ОПЕРАТОРА
СТАТУС: актуальная_операторская_очередь_v0_8
