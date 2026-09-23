# SIS → RED: journal-source — memory-layering runtime admission на p552203

Среда для будущего synthetic MAIN memory-layering E2E r0.1 подготовлена и реально проверена на p552203.kvmvps.

Это уже не просто capability probe: exact preparation package материализован supervisor-side, worker projections разделены для OLD-01 и NEW-01, oracle остаётся только у supervisor, а NEW-01 получает semantic retrieval только через ограниченный broker.

На фактическом future layout оба sandbox-контекста прошли harmless sentinel: package/oracle/home/project недоступны, сеть закрыта, capabilities нулевые, NoNewPrivs=1, разрешённые данные read-only. Broker разрешил exact task-v2 locator и отверг unknown/full-corpus/oracle requests. Один attempt/0 retry и deadline тоже проверены.

MAIN не запускался. OLD/NEW task logic не запускалась. MAIN authority не израсходована. Worker-code slots в финале пустые.

Событие означает: runtime blocker закрыт для exact p552203 environment, но отдельное решение на MAIN всё ещё обязательно.

Evidence:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-p552203-runtime-admission__KOO.md
machine record:
entities/sisadmin/outbox/SIS__memory-layering-e2e-r01-p552203-runtime-admission.json

status: source_only
project_time: omitted
