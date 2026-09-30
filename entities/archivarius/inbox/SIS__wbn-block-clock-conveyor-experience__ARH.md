# SIS → ARH: reusable experience candidate

candidate_id: SIS-WBN-BLOCK-CLOCK-001
status: CANDIDATE_FOR_EXISTING_ARH_EXPERIENCE_LAYER
project_time: omitted

## EXPERIENCE

Идея → если повторяемая работа проекта зависит от локальных часов, таймеров отдельных хостов и ручного попадания человека в короткое окно, стоит искать общий наблюдаемый причинный такт, который одинаков для всех участников. Для WBN таким кандидатом может быть последовательность подтверждённых блоков.

Проба → на фоне bounded Telegram-observer, где несколько раз проявились человеческие и технические проблемы синхронизации по wall-clock, ОПЕРАТОР предложил использовать генерацию блоков WBN как логический таймер конвейера, а смарт-контрактами регулировать стоимость события в зависимости от статистики нагрузки. Идея была развёрнута в отдельную candidate-концепцию Block Clock Conveyor + Adaptive Event Pricing.

Результат → сформирована архитектурная гипотеза: block_height может служить общим logical tick/epoch для уже разрешённых activation events; adaptive shadow price может регулировать конкуренцию за ограниченную пропускную способность; receipt может связывать активацию, результат и accounting. Одновременно зафиксирована жёсткая граница: блок, цена и контракт не создают task authority, current-writer, approval или право на production action.

Вердикт → КОНЦЕПТУАЛЬНЫЙ УСПЕХ / ТЕХНИЧЕСКАЯ ОСУЩЕСТВИМОСТЬ TERA2 ЕЩЁ НЕ ДОКАЗАНА.

Урок → при повторяемых процессах полезно отделять физическое время от логического порядка событий. Общий детерминированный sequence может быть лучше wall-clock как основа причинного конвейера, если он используется только как сигнал уже разрешённой работы. Экономический регулятор безопаснее сначала вводить как shadow pricing: сначала доказать статистику и устойчивость регулятора, потом разрешать реальные списания. Любой scheduler, даже on-chain, остаётся механизмом исполнения, а не источником полномочий.

Дополнительный урок → наблюдаемая неудобность текущего процесса может быть источником архитектурной идеи. Ошибка — чинить только конкретный таймер; более сильный ход — спросить, нужен ли системе вообще локальный таймер как первичный источник порядка.

## Provenance

concept:
puev5691/wellbeing-hq@a82e529a1d86e9fbfbcfc4247b7b41910417e662:
ops/research/WBN__block-clock-conveyor-adaptive-event-pricing-concept-r01-candidate.md

concept_blob:
9c4227e399d1802f58f1ba04fdb1f6d178793f20

plan_signal:
puev5691/wellbeing-hq@2dede1c911f4fe8317cb473d3fd1df30535f9ac6:
entities/shtabist/inbox/SIS__wbn-block-clock-conveyor-plan-candidate-r01__SHT.md

plan_blob:
73a98a5ebb538b6b48f7e3e389bfbcc1281c3f85

requested_action:
review/dedup into existing ARH experience/semantic layer; preserve the causal lesson, not only the blockchain implementation idea; do not create a new experience contour.

boundary:
candidate lesson only; not approved TERA2 fact, not production design, not task authority.
