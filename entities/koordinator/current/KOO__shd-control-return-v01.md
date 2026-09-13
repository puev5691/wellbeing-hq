# KOO — возврат SHD / ШАРДОВИКА под координацию KOO

status: KOO_CONTROL_RESTORED_WAITING_OPERATOR_SETUP_HANDOFF
canon: no
production_mutation: no
automation_change: no
project_time: omitted; trusted project-time source not used

## Решение ОПЕРАТОРА

ОПЕРАТОР явно снял временное исключение SHD из управления KOO и разрешил КООРДИНАТОРУ снова управлять ШАРДОВИКОМ.

При этом ОПЕРАТОР отдельно сообщил, что:
- сначала завершит текущую настройку SHD;
- после настройки у SHD будет конкретное направление по запуску криптоплатформы.

## Текущая operational state

entity: `SHD`
control_owner: `KOO`
queue_participation: `adaptive`
scheduler_eligible: `false`
state: `WAITING_OPERATOR`
waiting_reason: `operator_finishes_current_setup_and_returns_exact_crypto-platform_direction`

Это ожидание не является возвратом SHD под прямое управление ОПЕРАТОРА. Управление уже возвращено KOO; заблокирован только следующий профильный запуск, потому что его exact input ещё формируется ОПЕРАТОРОМ.

## Текущая подтверждённая база SHD

Существующие current-материалы остаются входной базой, но не считаются новой задачей сами по себе:

- `entities/shardovik/current/SHD__lab-01-mazhor-host-candidate.md` — Мажор как кандидат `lab-01`, с требованием свежей server-side проверки перед техническими утверждениями;
- `entities/shardovik/current/SHD__hosting-experiment-platform-plan.md` — план экспериментального контура GitHub / ChatGPT Pro / remote host / sandbox;
- существующие SHD-tail по WBN/WBNP/TERA2 и COOP не считаются автоматически активированными только из-за возврата управления.

## Следующий переход

После явного сообщения ОПЕРАТОРА, что настройка закончена и exact направление по запуску криптоплатформы готово:

1. KOO делает fresh GitHub-preflight;
2. проверяет current SHD/recovery/current-writer state;
3. reconciles направление ОПЕРАТОРА с существующими WBN/WBNP/TERA2 задачами;
4. создаёт один exact SHD task;
5. только после этого SHD становится `READY_PARALLEL` или `RUNNING` при наличии реального processing evidence.

## Границы

До этого события KOO не должен:
- будить SHD на старые хвосты ради занятости;
- запускать WBN/TERA2 node по старым материалам без нового exact direction;
- считать МАЖОР готовым runtime только по старому screenshot/current plan;
- менять production или security-sensitive контуры;
- дублировать настройку, которую прямо сейчас заканчивает ОПЕРАТОР.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: зафиксировать возврат SHD под управление KOO без конфликта с текущей ручной настройкой ОПЕРАТОРА
СТАТУС: koo_control_restored_waiting_operator_setup_handoff
