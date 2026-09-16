# KOO → OPERATOR: FAST_PATH execution contract r0.1

status: `CANDIDATE_FOR_IMMEDIATE_QUEUE_USE`
project_time: omitted; trusted project-time source not used

## Purpose

Сократить wall-time обычных Entity execution cycles без потери проверяемости и authority boundaries.

## 1. Default mode

Для обычных профильных задач использовать:
`EXECUTION_MODE: FAST_PATH`
`RECOMMENDED_REASONING: MEDIUM`

`HIGH` только если задача содержит архитектурный конфликт, тяжёлый debugging, reconciliation нескольких противоречивых evidence или высокий риск необратимого решения.

## 2. Admission once

Instance admission + fresh HQ preflight выполняются один раз в начале задачи.
Повторный полный preflight внутри того же execution-cycle запрещён, если нет наблюдаемого drift/conflict перед записью.
Перед final write достаточно bounded prewrite HEAD reconciliation.

## 3. Evidence budget

Читать только exact task, current-writer boundary и минимальный набор артефактов, без которых нельзя выполнить scope.
Не сканировать весь inbox/current/archive "для уверенности".
Не повторять уже подтверждённые immutable readback без причины.

## 4. Tool budget

Для штатной FAST_PATH задачи целевой budget:
- до 12 внешних tool calls до terminal result;
- до 8 GitHub reads/searches;
- до 4 GitHub writes, если пакет не требует большего.

Это target, не hard safety limit. Превышение допустимо только с короткой причиной в telemetry.

## 5. Early terminal

При первом достаточном доказательстве:
- PASS → завершить;
- exact blocker → завершить `BLOCKED_*`;
- wrong instance → завершить `WRONG_INSTANCE_OR_WRONG_CHAT`.

Не исследовать соседние проблемы после достижения terminal condition.
Не исправлять unrelated defects.

## 6. Artifact economy

Для одного bounded результата по умолчанию создавать:
1. один terminal result artifact;
2. необходимые route/registry records.

Не создавать manifest/checksums/package/readme/test-report как отдельные сущности, если task не требует immutable package или эти файлы не дают самостоятельной проверочной ценности.

## 7. Compact routing

Результат в чате/dispatch должен содержать только:
- terminal verdict;
- exact artifact locator;
- commit/blob;
- blocker/next dependency, если есть.

Подробное evidence хранится в result artifact, не дублируется в чат.

## 8. Latency telemetry

Фиксировать только реально доступные lifecycle events:
- dispatch/activation;
- first profile work;
- terminal result;
- routing complete.

Также:
- tool_calls;
- github_reads;
- github_writes;
- retries;
- reconciliations;
- operator_rewake_count.

Если абсолютные event timestamps доступны из GitHub evidence, допустимо вычислить queue/execution/routing/wall latency и явно обозначить источник как GitHub event timestamps.
Не выдумывать отсутствующие значения.

## 9. Escalation

FAST_PATH → DEEP_PATH только если:
- обнаружен material conflict;
- задача требует архитектурного решения;
- verifier/test failed и причина не локальна;
- security/recovery/authority boundary неоднозначен.

При escalation зафиксировать одну строку:
`ESCALATED_TO_DEEP_PATH: <reason>`.

## 10. Current priority

FAST_PATH применяется прежде всего к текущей OpenAI-first coordination infrastructure и будущим provider-adapter/entity-runner задачам.
TERA2/WBN остаётся PARKED_BACKGROUND и не занимает профильные слоты без отдельного решения ОПЕРАТОРА.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: уменьшить wall-time execution cycles и убрать лишний ceremonial overhead
СТАТУС: `candidate_fast_path_execution_contract_r01`
