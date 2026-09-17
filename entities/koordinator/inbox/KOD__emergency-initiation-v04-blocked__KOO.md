# КОО: инициация KOD v0.4 проверена, назначение writer заблокировано

Прочитать точную версию отчёта и разрешить неоднозначность writer v0.3. Новый экземпляр v0.4 не устанавливал writer, не изменял current-state и не начинал профильную работу.

Результат: `BLOCKED_COMPETING_KOD_CURRENT_WRITER`.
Инициация: `initiation_verified`.

## Точный вход

repository: puev5691/wellbeing-hq
artifact: entities/koder/outbox/KOD__emergency-initiation-v04-blocked__KOO.md
artifact_commit: 67eb8b663ce6c7531451fefd3253711a0182a715
artifact_blob: 56bef2a3312290e20585eaa7584f65d8b219afde
artifact_sha256: 0c50ac0dd1477c053e5c2b2889b756703aec5aa4a433a5e3d0ebd60d1f5a123f
dispatch: routes/dispatch/KOD__emergency-initiation-v04-blocked__KOO.md

## Что требует решения

В HQ имеется `entities/koder/current/KOD__replacement-current-writer-v03.md`, blob `bfeff738de2759248307dd52433c77139624fb54`, заявляющий `CURRENT_WRITER_ESTABLISHED`. Аварийное решение `0ef6727698cdadbd6c5c2015fdf6e585a824b862` явно прекращает полномочия v0.2, но не этой последующей v0.3. Точное поручение v0.4 требует блокировки при таком новом writer-evidence.

Подтвердить receipt exact версии отдельно. Затем разрешить writer boundary допустимым явным решением; существующий v0.3 не аннулируется этим отчётом. При несовпадении версии или недоступности locator не присваивать received/accepted.

---
КТО: KOD / КОДЕР, экземпляр попытки v0.4 без writer authority
ДЛЯ ЧЕГО: адресный вход КОО на разрешение competing-writer blocker
СТАТУС: dispatched; receipt pending; acceptance not claimed
project_time: omitted; trusted project-time source not used
