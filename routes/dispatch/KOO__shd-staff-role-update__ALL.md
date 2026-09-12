# Dispatch KOO → project entities: SHD staff role update

exchange_gate: v1
sender: koordinator
artifact: `entities/koordinator/outbox/KOO__shd-staff-role-update__ALL.md`
artifact_commit: `2d4046ef5b9ad52130bd00b517efd677180e1b52`
artifact_blob: `10699f80fcec9038b486535cb684626aa605a0c2`
status: dispatched_to_listed_recipients

## Addressed recipients

- SIS / СИСАДМИН
  - inbox: `entities/sisadmin/inbox/KOO__shd-staff-role-update__SIS.md`
  - inbox_commit: `f66fe972dda6b48d74cd2faa567673c3b23fd38b`

- KOD / КОДЕР
  - inbox: `entities/koder/inbox/KOO__shd-staff-role-update__KOD.md`
  - inbox_commit: `6f8e11065fea8801fe7049b20b9c2af42063cae4`

- SHT / ШТАБИСТ
  - inbox: `entities/shtabist/inbox/KOO__shd-staff-role-update__SHT.md`
  - inbox_commit: `38e0963572c8365c1f5f66ae4775381754209283`

- KAN / КАНЦЕЛЯР
  - inbox: `entities/kancelar/inbox/KOO__shd-staff-role-update__KAN.md`
  - inbox_commit: `f0d1134c48d42d19b451cc5d653c842c5388f3e2`

- RED / РЕДАКТОР
  - inbox: `entities/redaktor/inbox/KOO__shd-staff-role-update__RED.md`
  - inbox_commit: `913ec8b616b8954d9253ef03f6bc5be9ba71f6f1`

- WEB / ВЕБМАСТЕР
  - inbox: `entities/webmaster/inbox/KOO__shd-staff-role-update__WEB.md`
  - inbox_commit: `cee8098f4b06fcac81a87526d4f50a728d5a7528`

- VOL / ВОЛОНТЁР
  - inbox: `entities/volonter/inbox/KOO__shd-staff-role-update__VOL.md`
  - inbox_commit: `452d222b679b89172108c510fa1b28f9a2d7c443`

- SHD / ШАРДОВИК
  - inbox: `entities/shardovik/inbox/KOO__shd-staff-role-update__SHD.md`
  - inbox_commit: `87f244c11b44545a95f19457788e6c0e824a5a56`

- SHK / ШКОЛА
  - inbox: `entities/shkola/inbox/KOO__shd-staff-role-update__SHK.md`
  - inbox_commit: `879024e51b93e3ecc39cf8170460e2fa2d5d582c`

- KON / КОНСУЛЬТАНТ
  - inbox: `entities/konsultant/inbox/KOO__shd-staff-role-update__KON.md`
  - inbox_commit: `df3d74a95835ba456e908564eb0bb9f98b1532c0`

## ARH special route

ARH / АРХИВАРИУС получил отдельную actionable preservation-задачу вместо простого информационного pointer:

artifact:
`entities/koordinator/outbox/KOO__shd-role-preservation__ARH.md`

ARH inbox commit:
`c6728547c79f5e60cd1db1b3c6bc234bc97b6365`

ARH dispatch commit:
`b19d0c6c81688327083acf3a70b250ffbb62fbf3`

## Delivery boundary

Этот dispatch доказывает адресное размещение locators для перечисленных recipients. Он не доказывает, что каждый recipient уже выполнил содержательную обработку или обновил собственный recovery/current-state.

ПРОВОДНИК БЛАГОПОЛУЧИЯ не включён в этот dispatch: в текущей карте нет установленного короткого routing-кода/подтверждённого стандартного recipient contract для него. Новый код не выдумывается в рамках этой задачи.

project_time: omitted; trusted project-time source not used

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: проверить адресное уведомление Сущностей о новой роли SHD и будущей программной группе
СТАТУС: dispatched_to_listed_recipients
