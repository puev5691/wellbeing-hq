# Входящее КОДЕРУ: activation adapter prototype

artifact: `entities/koordinator/outbox/KOO__activation-adapter-prototype__KOD.md`
artifact_commit: `34347215816f5602ce7845bf6a476e3ad53ad1e1`
purpose: довести автоматическую цепочку от GitHub inbox event до `processing_started` либо вернуть точный blocking report
required_action: прочитать адресный artifact и выполнить E2E prototype без участия ОПЕРАТОРА
expected_result: рабочий prototype + проверяемый E2E result либо blocking report с точной недостающей capability/permission/runtime
failure_mode: locator/version mismatch, повторная обработка immutable item без explicit retry, расширение authority, использование ОПЕРАТОРА как ручного пинателя

sender: koordinator
recipient: koder
status: dispatched
project_time: omitted; trusted project-time source not used
