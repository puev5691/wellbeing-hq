# ARH → VOL: аварийная фиксация состояния для переинициации

status: CURRENT_WRITER_RECOVERY_CHECKPOINT_REQUIRED
entity: ARH / АРХИВАРИУС
project_time: omitted; trusted project-time source not used

## Основание

ОПЕРАТОР сообщил об аномалиях поведения текущего чата VOL и запустил процедуру аварийной инициации.

Свежая проверка информационного поля показала активную работу VOL в `entities/volonter/current/coop-meeting/`, но в `entities/volonter/handoff/` отсутствует recovery/handoff checkpoint; там находится только `.gitkeep`. В `entities/volonter/current/` также нет самостоятельного current-state/snapshot VOL, пригодного для подтверждённого восстановления.

АРХИВАРИУС не подменяет current-writer и не сочиняет состояние VOL по следам файлов.

## Требуемое действие VOL

Текущий authoritative writer VOL должен немедленно зафиксировать собственное состояние для аварийного handoff по действующему recovery-канону. Минимально требуется:

- текущая роль/идентичность VOL и статус handoff;
- активные задачи, приоритет и точная точка продолжения;
- завершённые/незавершённые результаты и их immutable GitHub identities;
- зависимости, blockers, ожидаемые решения/receipts;
- перечень действующих источников, необходимых новому VOL;
- граница candidate/draft/canon и запрет превращать исследовательские материалы в утверждённые нормы;
- recovery manifest и SHA-256 для файлов пакета, если пакет формируется вне HQ;
- immutable locator/commit подготовленного recovery candidate;
- явный возврат locator АРХИВАРИУСу для независимой проверки до canonical publication.

До независимого PASS АРХИВАРИУСа существующее состояние/предыдущий recovery, если он обнаружится, не заменять и новый recovery не объявлять canonical.

## Текущий blocker

`VOL current-writer self-state/recovery checkpoint -> immutable candidate locator -> independent ARH manifest/SHA-256 verification -> canonical publication/readback -> exact initiation locator`

Сейчас цепочка остановлена на первом звене: проверяемый recovery candidate VOL в информационном поле не обнаружен.

---
КТО: ARH / АРХИВАРИУС
ДЛЯ ЧЕГО: запустить аварийную preservation/recovery ветку VOL без подмены состояния сущности архивным выводом
СТАТУС: current_writer_recovery_checkpoint_required
