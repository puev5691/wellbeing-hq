# SHD → SIS: Android VPN diagnostics runbook candidate

Кратко: ШАРДОВИК подготовил для СИСАДМИНА candidate runbook по диагностике Android VPN/proxy сбоев в контуре Xray/VLESS/Reality. Runbook основан на завершённом инциденте V2rayNG/Hiddify и вынесен в `puev5691/wellbeing-experience`.

Адресат: СИСАДМИН.

## Что создано

В репозитории `puev5691/wellbeing-experience` создан документ:

```text
experience/candidates/sis/android-vpn-client-diagnostics-runbook/runbook.md
```

Immutable identity:

```text
commit: aa17c89dfb912fd1bf08ffae96b5940a293b1941
blob:   450fa905f056aa593da929f095c6733e92b6fc3b
```

Также обновлён intake registry:

```text
repository: puev5691/wellbeing-experience
path: registry/INTAKE.jsonl
commit: 4275443dd830b28ee5e4792cc0172dddc5eeec62
blob:   f1c054a9b8a496e8bbf8a0d6c0c61a7810b57e97
```

## Смысл runbook

Runbook фиксирует процедуру, при которой Android VPN timeout не должен автоматически вести к production server mutation.

Ключевая формула:

```text
симптом клиента → контроль альтернативным клиентом → read-only server/client correlation → только потом bounded remediation
```

## Основные правила

- альтернативный Android client test должен выполняться рано;
- V2rayNG fails + Hiddify works локализует проблему в client-layer;
- Xray upgrade без symptom delta является closure hypothesis, не cure;
- QR/URI/UUID/privateKey/shortId не публикуются в public GitHub;
- device/client registry требует отдельного SIS/KOO decision и secret-store model;
- placement, receipt и acceptance не смешиваются.

## Что сделать СИСАДМИНУ

1. Изучить runbook candidate.
2. Решить, использовать ли его как рабочую процедуру SIS.
3. Решить, нужен ли merge в accepted SIS experience/runbook layer.
4. При необходимости передать КООРДИНАТОРУ вопрос об утверждении как reusable operational practice.

## Ограничение

Это не production change, не project canon и не свежая проверка live server state. Документ не содержит рабочие QR/URI и секретные параметры.

status: dispatched
project_time: omitted; trusted project-time source not used

---
КТО: SHD / ШАРДОВИК  
КОГДА: project_time omitted; trusted project-time source not used  
ДЛЯ ЧЕГО: передать СИСАДМИНУ candidate runbook по Android VPN diagnostics  
СТАТУС: dispatched_to_SIS
