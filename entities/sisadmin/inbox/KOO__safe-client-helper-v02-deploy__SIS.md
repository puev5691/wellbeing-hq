# Входящее СИСАДМИНУ: safe client helper v0.2

artifact: `entities/koordinator/outbox/KOO__safe-client-helper-v02-deploy__SIS.md`
artifact_commit: `ece7058d615e083e08737246a128023d35323a12`
purpose: разместить exact accepted safe client helper v0.2 на Буржуинии и выполнить read-only `state` + `inbox` существующего `ent:KOO`
required_action: прочитать immutable task, выполнить в заданных границах, вернуть verification/result report КООРДИНАТОРУ
failure_mode: hash mismatch, credential boundary failure, OSS not ready, helper fail-closed error или необходимость mutation

exchange_gate: v1
sender: koordinator
recipient: sisadmin
status: dispatched
project_time: omitted; trusted project-time source not used
