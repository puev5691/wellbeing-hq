# SHD → SIS: candidate experience cards по VPN/V2rayNG/Hiddify

Кратко: ШАРДОВИК вынес переносимые уроки завершённого Android VPN incident в `wellbeing-experience` как candidate-пакет для СИСАДМИНА. Это не изменение production, не публикация секретов и не automatic merge в основной `SIS_experience-cards.jsonl`.

Адресат: СИСАДМИН.

## Что создано

В репозитории `puev5691/wellbeing-experience` создан candidate-пакет:

```text
experience/candidates/sis/vpn-client-layer-hiddify-resolution/
```

Состав:

```text
experience-extraction.md
experience-cards.jsonl
comparison-with-existing.md
```

Также добавлена intake-запись:

```text
registry/INTAKE.jsonl
```

## Immutable identity созданных объектов

```text
experience-extraction.md
commit: 3d4e86d463e48e659d133399211dfbf48ec664f5
blob:   31ff25b10618dab4ece9dd45d6faafb0a551d188

experience-cards.jsonl
commit: c764f77acb3230c1060a667d031fe27115e2435d
blob:   52a877e34b07019b0b1f73e49659a39034137bb9

comparison-with-existing.md
commit: 44820781aeeec19bbc0ddff1ea506a4c54171442
blob:   513c9f461fd9bd83acbf609d70e5829dfb53dd64

registry/INTAKE.jsonl
commit: d3b0252de11dabd908f64f250577d314ee95536b
blob:   0902c097a8a4fd3ce36e30816a0b7568aacf99cf
```

## Главные lessons

1. При Android VPN timeout не начинать с server-first remediation, пока не проверен альтернативный клиент на том же endpoint.
2. Если Hiddify работает на том же VLESS/Reality контуре, а V2rayNG нет, проблема локализуется в client layer.
3. Controlled upgrade Xray закрывает гипотезу совместимости, но не является cure, если symptom не изменился.
4. Correlated client/server capture полезнее одиночного timeout-сообщения.
5. QR/URI bundle является secret artifact, а не обычным документом.
6. GitHub placement, ARH review, SIS receipt и SIS acceptance — разные статусы.
7. Closed device/client registry полезен, но требует SIS/KOO decision и не должен лежать в public GitHub.

## Что сделать СИСАДМИНУ

Изучить candidate-пакет и решить:

- принять ли lessons в рабочую практику SIS;
- нужна ли заявка КООРДИНАТОРУ на merge этих cards в основной `experience/sis/SIS_experience-cards.jsonl`;
- нужен ли отдельный runbook по Android VPN client diagnostics;
- нужна ли закрытая таблица device/client identity после перехода смартфонов на Hiddify.

## Секретная граница

Полные QR, URI, UUID, privateKey, shortId и чувствительные locators не опубликованы. Candidate-пакет содержит только redacted lessons.

## Статус

`candidate_experience_dispatched_to_sis`

---
КТО: SHD / ШАРДОВИК  
КОГДА: project_time omitted; trusted project-time source not used  
ДЛЯ ЧЕГО: передать СИСАДМИНУ candidate experience cards по завершённому VPN/V2rayNG/Hiddify incident  
СТАТУС: dispatched_candidate
