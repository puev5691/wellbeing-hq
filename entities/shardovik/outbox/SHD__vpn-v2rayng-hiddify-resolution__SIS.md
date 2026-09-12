# Отчёт для СИСАДМИНА: сбой V2rayNG и переход на Hiddify

Кратко: смартфонный VPN-контур проекта восстановлен не серверной правкой и не сменой параметров VLESS/Reality, а переходом Android-клиентов с V2rayNG на Hiddify. Серверная часть проверена, обновлена до Xray `26.6.1` и оставлена рабочей. Полные QR, URI, UUID и ключевые параметры доступа в этот отчёт не включены.

Адресат: СИСАДМИН.

Что требуется от СИСАДМИНА: принять результат как рабочую техническую фиксацию по Android VPN-клиентам, учитывать Hiddify как текущий основной Android-клиент для данного VLESS/Reality контура, не возвращать смартфоны на V2rayNG без нового доказательного теста.

## 1. Ситуация

На смартфонах через V2rayNG перестали нормально работать Telegram и YouTube на сотовых операторах и сети Волна.

Наблюдавшееся поведение:

- Telegram открывался, но зависал в состоянии соединения;
- YouTube открывал оболочку интерфейса, но не догружал видео, изображения и текст;
- проверка соединения V2rayNG возвращала `context deadline exceeded`;
- после отключения IPv6 поведение не изменилось;
- после обновления серверного Xray поведение V2rayNG не изменилось;
- тот же контур в Hiddify заработал нормально;
- после переноса старых QR/URI в Hiddify пользователь подтвердил: всё работает.

## 2. Проверенная серверная часть

Проверялись серверы:

- `wbnetrus.ru` как основной Reality/VLESS entrypoint на `443`;
- `uk.wbnetrus.ru` как внешний выход;
- Xray service на обоих серверах;
- SSH SOCKS tunnel `127.0.0.1:1081` на `wbnetrus.ru`;
- server-side target probes;
- correlated capture во время смартфонных тестов.

Подтверждённый результат:

- `wbnetrus.ru` видел входящий поток на `443` во время тестов;
- `127.0.0.1:1081` на `wbnetrus.ru` активно использовался;
- UK-side показывал активность;
- Xray и SOCKS unit не были причиной полного отказа;
- полная недоступность `wbnetrus.ru:443` со смартфона не подтверждена.

## 3. Upgrade Xray

Перед обновлением был выполнен preflight:

- оба сервера были на Xray `26.5.3`;
- бинарник находился в `/usr/local/bin/xray`;
- конфигурация находилась в `/usr/local/etc/xray/config.json`;
- layout был не apt/snap, а `/usr/local`;
- `xray -test -config` проходил успешно.

Затем выполнен controlled upgrade до Xray `26.6.1` на обоих серверах.

Итог:

- `uk.wbnetrus.ru`: `26.5.3 -> 26.6.1`, config-test OK, service active/running;
- `wbnetrus.ru`: `26.5.3 -> 26.6.1`, config-test OK, service active/running;
- rollback не срабатывал;
- после upgrade поведение V2rayNG не изменилось.

Вывод: гипотеза «серверный Xray слишком старый для V2rayNG 2.2.4» проверена и закрыта как не подтвердившаяся. Откат на `26.5.3` не требуется, если не появятся отдельные побочные симптомы.

## 4. Клиентские логи V2rayNG

Логи смартфона показывали:

- Xray-core внутри V2rayNG стартует;
- трафик приложений попадает внутрь V2rayNG;
- в одном логе маршруты шли через `socks >> proxy`, в другом через `tun >> proxy`;
- DNS и Telegram/Google targets уходили через proxy;
- повторялись ошибки `context deadline exceeded` для `google.com/generate_204` и `gstatic.com/generate_204`;
- явной ошибки Reality handshake, fingerprint, allowInsecure или pinnedPeerCertSha256 не было.

Вывод: проблема не выглядела как простая ошибка сертификата, Reality-параметров или полной сетевой недоступности сервера.

## 5. Новый client / QR

Для исключения старого кривого импорта был создан новый VLESS/Reality client на `wbnetrus.ru` и сгенерирован новый QR/URI.

Результат:

- новый профиль в V2rayNG дал прежнее плохое поведение;
- тот же профиль в Hiddify заработал нормально.

Вывод: проблема находится в связке V2rayNG 2.2.4 / Android TUN / обработка профиля / маршрутизация клиента, а не в самом серверном VLESS/Reality контуре.

## 6. Экспорт существующих клиентов

С `wbnetrus.ru` был выполнен read-only export существующих VLESS/Reality clients.

Redacted-сводка:

- domain: `wbnetrus.ru`;
- port: `443`;
- security: `reality`;
- type: `tcp`;
- flow: `xtls-rprx-vision`;
- sni: `www.cloudflare.com`;
- fingerprint: `chrome`;
- clients: 4.

В отчёт не включены полные VLESS URI, QR, UUID, shortId, publicKey или privateKey. Полный QR/URI bundle является секретным рабочим комплектом.

## 7. Рабочее решение

Подтверждённое решение:

- Android-смартфоны переводить на Hiddify;
- существующие VLESS/Reality QR/URI импортировать в Hiddify;
- V2rayNG не использовать как основной Android-клиент для текущего контура, пока отдельный тест не докажет обратное;
- старые профили V2rayNG удалить или пометить как «не использовать», чтобы не создавать ложную диагностику.

## 8. Операционные правила для СИСАДМИНА

При новых жалобах на смартфонный VPN:

1. Сначала уточнить клиент: Hiddify или V2rayNG.
2. Если это V2rayNG, не начинать серверную диагностику без повторной проверки на Hiddify.
3. Если Hiddify работает, считать проблему клиентской, а не серверной.
4. Если Hiddify тоже не работает, собирать Hiddify log/export и server-side correlated capture.
5. Проверять `xray.service`, `wb-errefiya-to-burzhuiniya-socks.service`, listener `:443`, listener `127.0.0.1:1081`.
6. Не публиковать полный QR/URI bundle в открытый GitHub, общие чаты или документы.
7. При выдаче доступа участнику передавать только его client QR/URI, а не общий bundle всех клиентов.
8. Вести карту соответствия: устройство -> client email -> где установлен -> дата/этап проверки -> результат.

## 9. Что не делать

- Не откатывать Xray на `26.5.3` без отдельного подтверждённого основания.
- Не считать `context deadline exceeded` в V2rayNG доказательством падения сервера.
- Не создавать новый серверный endpoint до проверки альтернативного клиента.
- Не использовать один общий client UUID на все смартфоны, если есть возможность развести устройства по отдельным client email.
- Не хранить полный QR/URI bundle в публичной части репозитория.

## 10. Открытые вопросы

- Нужно ли удалить временный client `phone-qr-20260621-224507`, созданный для проверки, если он больше не используется.
- Нужно ли оформить отдельный закрытый реестр соответствия «устройство -> client email» вне публичного GitHub.
- Нужно ли перенести lesson в `wellbeing-experience` отдельными experience cards.
- Нужно ли АРХИВАРИУСУ создать архивную карточку события и указать место долговременного хранения redacted-отчёта.

## 11. Статус

Статус: resolved_by_client_replacement.

Практический результат подтверждён пользователем: после переноса профилей в Hiddify всё работает.

Серверная часть оставлена на Xray `26.6.1`.

## Служебная карточка документа

- document_type: technical-incident-resolution-report
- status: working-confirmed-by-operator
- graph_role: sisadmin-actionable-report
- entity_author: SHD / ШАРДОВИК
- human_responsible: OPR / ОПЕРАТОР
- intended_recipients: SIS / СИСАДМИН; ARH / АРХИВАРИУС для архивной проверки
- created_for: фиксация результата диагностики VPN/Xray/V2rayNG/Hiddify и передача рабочего вывода СИСАДМИНУ
- source_artifacts: `SHD__vpn-v2rayng-hiddify-resolution-report__OPR.tar.gz`; `SHD__vless-reality-existing-clients-qr-export-report__OPR.tar.gz`; smartphone V2rayNG logcat files; correlated capture reports; upgrade reports
- secret_material_excluded: full VLESS URI; QR images; UUID; privateKey; shortId; publicKey; passwords; tokens
- project_time: omitted; trusted project-time source not used

КТО: ШАРДОВИК / ChatGPT
КОГДА: project_time omitted; trusted project-time source not used
ДЛЯ ЧЕГО: передать СИСАДМИНУ проверенный вывод по Android VPN-клиенту и зафиксировать переход V2rayNG -> Hiddify
СТАТУС: working-confirmed-by-operator
