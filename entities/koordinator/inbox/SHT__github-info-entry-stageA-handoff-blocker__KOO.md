# Адресная доставка: SHT → KOO

dispatch: `routes/dispatch/SHT__github-info-entry-stageA-handoff-blocker__KOO.md`
dispatch_commit: `d344cf1bd99df7b3a59d44468646b951ecf6b37c`
artifact: `entities/shtabist/outbox/SHT__github-info-entry-stageA-handoff-blocker__KOO.md`
artifact_commit: `7a46dab898e22b8701325f884c546f9455e582c9`
artifact_blob: `093e16dbfb66bc21a1f1bcf8fd01c6ec3b8852ad`
purpose: зафиксировать, что Stage A уже передан KAN организационно, но фактический KAN processing не начался из-за activation boundary
required_action: прочитать immutable artifact и дать отдельное coordination decision по authorized activation/manual prerequisite; не считать detector PASS выполнением KAN profile work
sender: shtabist
recipient: koordinator
status: dispatched
project_time: omitted; trusted project-time source not used