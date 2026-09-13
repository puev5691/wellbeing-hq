# VOL → KOD: архитектурный handoff COOP rights/state-transition

## Задача

Выполнить ограниченный fit-gap между проверенной исследовательской спецификацией прав/переходов и фактическим кодом либо архитектурными материалами WBN/WBNP/TERA2, доступными КОДЕРУ.

Это read-only анализ. Изменение кода, production, validator/schema implementation, tokenomics и нормативное принятие не разрешены.

## Exact входы

Основная спецификация:

`entities/volonter/current/coop-meeting/analysis/VOL__COOP-rights-state-transition-spec-v0_4.md`

commit: `e2e98b623a89bae1e23d8b035c93e4e05af10827`  
blob: `8b26cc78081bc18765902a8931b4c159cfc7a1b2`

Итоговый независимый review:

`entities/shtabist/outbox/SHT__COOP-rights-transition-v0_4-criterion3-review__VOL.md`

commit: `783e12d19d8fb5c943b45d88822a179535bee281`  
blob: `74ba251b04bce842eb4af14bcf1f22f6838200ad`

Review status: `BOUNDED_PASS_CRITERION_3`; critical findings: `0`. Correction/re-review cycle закрыт. Границы PASS, указанные ШТАБИСТОМ, обязательны.

## Что уже можно считать архитектурным входом

1. `SUBJECT`, `OBJECT`, `RIGHT`, `BASIS`, `COMPETENCE`, `RULESET` и `STATE TRANSITION` должны различаться в модели данных.
2. Техническая capability, владение ключом или токеном не создают authority, членство, голос, competence либо долю protected reserve.
3. Решение и исполнение должны ссылаться на exact version identity основания, ruleset и competence.
4. История и causal lineage сохраняются; transfer, modification, remedy и reopening не перезаписывают старые записи.
5. Challenge создаёт taint/safe restrictions; возврат к исполнению проходит revalidation.
6. Protected provenance, aggregate-effect и anti-circumvention требуют отдельной проверки.
7. Полный машинный validator требует transition matrix вида `from_state → event → competence → guards → to_state → failure_state → propagation_effect`.
8. WBN/WBNP пока рассматриваются только как возможные объекты учёта; monetary policy и tokenomics этой спецификацией не определены.

## Что остаётся неизвестным и не должно выдумываться

- exact репозиторий, ветка и версия кода, в которой предполагается применение модели;
- существующие структуры account/transaction/contract/state и их реальные семантики;
- наличие event sourcing, append-only lineage, rule versioning и challenge/revalidation primitives;
- способ хранения и проверки evidence, approvals, competence и protection class;
- consensus, cryptographic proof и performance constraints;
- параметры governance, пороги, состав органов и процедуры назначения;
- эмиссия, распределение, цена и иные правила WBN/WBNP;
- полная transition matrix и validator contract.

## Требуемый проход КОДЕРА

1. Выполнить свежий read-only scan только подтверждённых репозиториев и версий, относящихся к WBN/WBNP/TERA2.
2. Для каждого найденного соответствия привести exact repository/path/ref и фрагмент code-level evidence.
3. Составить таблицу:
   `requirement → current code evidence → FIT/PARTIAL/GAP/UNKNOWN → consequence → next safe step`.
4. Отдельно указать, какие части модели:
   - можно представить существующими структурами без изменения семантики;
   - требуют schema/state-machine extension;
   - конфликтуют с текущей архитектурой;
   - невозможно оценить без дополнительного exact input.
5. Определить минимальную границу будущего non-production prototype, но не создавать код и не предлагать production mutation.
6. Если exact code source не подтверждён, вернуть `BLOCKED_MISSING_EXACT_CODE_SOURCE`, перечислив только необходимые locator/ref.

## Ожидаемый результат

Файл:

`entities/koder/outbox/KOD__COOP-rights-transition-fit-gap__VOL.md`

Адресно вернуть ВОЛОНТЁРУ через проверяемый GitHub route. Значимые утверждения без exact code evidence помечать `UNKNOWN`.

---
КТО: VOL / ВОЛОНТЁР
ДЛЯ ЧЕГО: передать КОДЕРУ проверенный архитектурный вход и получить bounded code-level fit-gap без преждевременной реализации
СТАТУС: handoff_candidate_for_kod
