# КООРДИНАТОР — рабочая очередь v0.10

Статус: `CURRENT_OPERATOR_QUEUE`
Режим: `WIP_LIMIT_2`
Проектное время не указывается.

## Смысл

Очередь v0.9 устарела по фактическому состоянию: KOD replacement current-writer установлен; Telegram Phase1B threading-fix r0.2 выполнен KOD и готов к независимой SIS-проверке; ARH и WEB preservation-кандидаты готовы; SHT завершил process design Chat→Work.

Новый принцип исполнения:

`не более двух активных профильных Сущностей одновременно`.

Новая работа не запускается, пока один из двух активных слотов не завершён, не заблокирован или явно не переведён в waiting.

## P0 — ACTIVE SLOT 1: SIS / Telegram Phase1B independent verification

Основание:
- KOD result: `entities/koder/outbox/KOD__telegram-phase1b-threading-fix-r02-result__KOO.md`;
- result commit: `446dfa2ea1ef55858e60ad0575e506f8b28842d8`;
- result blob: `d7fbc4e765bc6b2c29f1c8fbf842916df1c3d12c`;
- verdict: `PASS_KOD_THREADING_FIX_CANDIDATE_READY`;
- immutable package commit: `62f82c3322f28adc55b47b1a7064fccb23e4c351`;
- package tree: `2c8301c211315a695166188bd69ab4c91be95836`.

Следующее действие: KOO адресует SIS отдельную bounded non-production verification task.

Граница: никакого live Telegram, credentials, public webhook, production, sudo/privileged mutation или historical unchanged host-gate replay без отдельного последующего gate.

## P0 — ACTIVE SLOT 2: KOD / OpenAI Responses API D0 adapter

Цель: начать OpenAI API-интеграцию не с нуля, а поверх уже проверенной multi-model mechanics.

Проверенная база:
- `KOD__multi-model-gateway-mock-r01-result__KOO.md` → `PASS_LOCAL_SYNTHETIC_GATEWAY_MOCK`;
- `KOD__anthropic-direct-adapter-r01__KOO.md` → credential-free/network-disabled adapter ready;
- `KOD__anthropic-live-transport-r01__KOO.md` → live-capable transport prepared, live call not performed.

Следующее действие: KOO адресует KOD отдельную задачу на OpenAI Responses API adapter/transport candidate только для `D0_SYNTHETIC`, без API key и live provider call.

Первый target-model для технического pilot: `gpt-5.6-luna`, если fresh official OpenAI documentation не показывает конфликт. При provider-doc drift KOD обязан остановиться и вернуть exact blocker/correction, а не менять контракт молча.

## P1 — после освобождения P0 slots

### OpenAI live D0 gate

Только после PASS KOD adapter candidate:
1. ОПЕРАТОР включает API billing;
2. ОПЕРАТОР создаёт OpenAI API key;
3. секрет не попадает в GitHub/логи/chat artifacts;
4. SIS делает preflight одного выбранного Unix-host;
5. один D0 synthetic provider call;
6. фиксируются model, response/request identity, usage tokens, latency, retry/error state и immutable result;
7. никаких project-private данных на первом live gate.

### Anthropic live D0 gate

После первого OpenAI live PASS либо отдельного решения KOO/OPERATOR можно использовать уже подготовленный Anthropic transport для второго provider D0 call и сравнения provider-neutral gateway behavior.

## P2 — профильные проектные линии

### TERA2 / SHD

После освобождения KOD slot:
`entities/koordinator/outbox/KOO__tera2-root-profile-candidate-r01__KOD.md`
commit `9c6972681ae8b058cbe99c5ae4a3674a5cd1d3eb`.

SHD не будить до нового KOD root-profile result.

### Recovery canon v1.5 OPERATOR gate

Готов, но не блокирует P0/P1:
`entities/koordinator/outbox/KOO__entity-recovery-canon-v1_5-operator-gate__OPERATOR.md`
commit `17190f729eef6537f0404af387253c9c11eb3a21`.

Допустимые решения сохранены без изменения:
- `APPROVE_V1_5_WAKE_INITIATION_RESUME_AMENDMENT`;
- `RETURN_V1_5_FOR_FIXES: <точный дефект>`;
- `REJECT_V1_5`.

## P3 — PARKED / BACKGROUND

### Retired Entity lifecycle study

v0.1 выявил методические дефекты. Требуется v0.2 с `CAPTURE_FIRST` и external collector.
Исследование не блокирует основную работу. После выпуска v0.2 samples собираются фоном; первая агрегация не ранее появления примерно 10–20 пригодных samples.

### Chat → Work migration

SHT process design завершён. Массовую миграцию не начинать. Work остаётся optional execution surface; приоритет сейчас у API/entity-runner architecture.

### ARH / WEB replacement

Preservation candidates готовы. Replacement не выполнять без эксплуатационной необходимости или отдельного gate.

### VOL / RED / KAN

Не будить без материализованной зависимости или отдельного current task.

## Экономическая проверка Plus / Pro / API

Не менять подписку по предположению. До следующего решения собрать фактическую телеметрию API и оценить, какая доля рутинной Entity work реально ушла из ChatGPT в API.

Решение о Plus/Pro принимать перед следующим периодом оплаты по двум фактам:
1. реальная ценность/usage ChatGPT-интерфейса для ОПЕРАТОРА;
2. фактическая месячная стоимость API workloads по моделям и токенам.

API billing рассматривается отдельно от ChatGPT subscription.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: заменить устаревшую v0.9 фактической двухполосной очередью и не перегружать ОПЕРАТОРА параллельными хвостами
СТАТУС: `CURRENT_OPERATOR_QUEUE_V10`
