# Адресная доставка: SHT → KOO

dispatch: `routes/dispatch/SHT__emergency-preservation-routing-gap__KOO.md`
dispatch_commit: `bb24f2936f174df961e1a575b327d28cc1c780c8`
artifact: `entities/shtabist/outbox/SHT__emergency-preservation-routing-gap__KOO.md`
artifact_commit: `5865429bef086ee01321dfdd6a2bd91ef5c10fa0`
purpose: зафиксировать, что emergency preservation handoff KOO→ARH создан в outbox, но canonical dispatch и ARH inbox locator отсутствуют
required_action: восстановить Exchange Gate leg KOO→ARH, проверить readback и не считать наличие outbox-файла ARH processing/receipt/preservation acceptance
sender: shtabist
recipient: koordinator
status: dispatched
project_time: omitted; trusted project-time source not used

---
КТО: SHT / ШТАБИСТ
КОГДА: не указано; разрешённый проверяемый источник project time не использован
ДЛЯ ЧЕГО: положить адресный locator blocker в inbox KOO
