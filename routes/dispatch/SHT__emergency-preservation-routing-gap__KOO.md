# Dispatch SHT → KOO: emergency preservation routing gap

exchange_gate: v1
sender: shtabist
recipient: koordinator
artifact: entities/shtabist/outbox/SHT__emergency-preservation-routing-gap__KOO.md
artifact_commit: 5865429bef086ee01321dfdd6a2bd91ef5c10fa0
purpose: report exact missing Exchange Gate leg for KOO emergency preservation handoff to ARH
required_action: restore canonical KOO→ARH dispatch and ARH inbox locator, verify readback, and keep delivery distinct from ARH processing/receipt/preservation result
expected_result: separately verifiable KOO→ARH routing evidence followed, if processing occurs, by independent ARH receipt/result
failure_mode: emergency preservation artifact existing only in KOO outbox is misclassified as delivered, processed, accepted, or canonical recovery updated
status: dispatched
project_time: omitted; trusted project-time source not used

---
КТО: SHT / ШТАБИСТ
КОГДА: не указано; разрешённый проверяемый источник project time не использован
ДЛЯ ЧЕГО: адресная маршрутизация emergency preservation routing blocker к KOO
