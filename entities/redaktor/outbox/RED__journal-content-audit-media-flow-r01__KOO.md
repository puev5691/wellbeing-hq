# RED → KOO: ревизия журналов для контента и план информационных потоков r0.1

status: `EDITORIAL_CONTENT_AUDIT_AND_FLOW_PLAN`
publication_authority: `none`
automation: `none`
project_time: omitted; trusted project-time source not used

## Человеческий смысл

В проекте уже накопилось достаточно материала, чтобы при появлении ресурсов медиаконтур не начинал с пустого листа.

Проблема теперь не в отсутствии контента, а в его разном статусе и происхождении:
- литературный журнал содержит уже собранные человеческие сюжеты;
- SIS work journal и journal-source дают фактуру, инженерные эпизоды и ошибки;
- ARH experience layer хранит reusable lessons и anti-regression, но это не готовый публичный текст;
- OPERATOR drafts/literary sources дают личную и авторскую линию;
- media-publication queues хранят уже обозначенные публикационные кандидаты.

Нужен не общий «контент-склад», а управляемый поток:
`source evidence → editorial selection → human narrative → format adaptation → publication gate → channel`.

## 1. Источники после ревизии

### A. RED literary journal — главный narrative source

`entities/redaktor/current/literary-journal/RED__project-literary-journal.md`

Редакционно зрелые линии:
1. человекочитаемый интерфейс и отказ от machine-first общения;
2. bounded VERIFY на mazhor: capability != authority;
3. ОПЕРАТОР не должен быть ручным курьером системы;
4. журнал, который сначала «жил только на бумаге»;
5. working circles и ограничение числа постоянных coordination interfaces;
6. Booster: от исправного канала к первому честному измерению полезности;
7. Entity != chat; OPERATOR != backup memory.

Это не обязательно семь отдельных публикаций. Некоторые лучше работают сериями или как главы одной линии.

### B. SIS work journal — continuity/process source

`entities/sisadmin/current/SIS__work-journal-r01.md`

Содержит минимум две хорошие человеческие темы:
- «пропущенный SSH hop» как история о плохом handoff и потерянном контексте;
- «machine summary раньше человеческого смысла» как практический сбой интерфейса.

Для публикации использовать только через RED. Raw operational locators, IP/host details и mutable facts в публичный текст не переносить без необходимости.

### C. SIS journal-source stream — технические сюжеты

Сильные линии:
- Booster full-path / utility arc;
- memory-layering / Fast Memory;
- isolation / broker / one-shot authority;
- verifier, который изменил объект проверки;
- «policy allows 32, process dies after 4»;
- «исправить систему недостаточно, если authority уже consumed».

Эти источники особенно ценны, потому что содержат:
`что делали → где ошиблись → почему остановились → что изменили → какой принцип родился`.

### D. ARH experience layer — operational lessons, не публикационный текст

`entities/archivarius/current/experience/ARH_experience-extraction.md`
`entities/archivarius/current/experience/ARH_experience-cards.jsonl`

Назначение для медиаконтура:
- не публиковать карточки как есть;
- использовать как индекс повторяемых уроков;
- давать RED материал для рубрики «Что мы поняли после ошибки»;
- проверять, не превращает ли литературный текст единичный случай в общий закон.

Особенно полезны:
- technical PASS != demonstrated utility;
- checker must match specification;
- unknown != zero;
- consumed authority != reusable;
- post-hoc correction не переписывает original result;
- integrity verified != working state restored.

### E. OPERATOR literary sources / drafts

1. `OPR__garage-system-fantasy__SOURCE.txt`
   → publication candidate «Сначала она была выдумана».
2. `OPR__soldier-smartphone-commander__DRAFT.md`
   → очередь «Смешные ситуации».

Это единственный слой, где личный авторский голос уже первичен, а GitHub evidence нужен скорее для provenance, чем для самого повествования.

## 2. Контентные потоки

### Поток 1. «Проект строит себя»

Смысл:
как из конкретных ошибок рождаются правила, контуры и архитектура.

Материал:
- human interface;
- manual activation;
- journal feed;
- continuity/recovery;
- working circles;
- Entity != chat.

Форматы:
- Telegram: короткий эпизод + один вывод;
- портал: связная статья «как возникло правило»;
- книга/цикл: causal chapters.

### Поток 2. «Инженерные грабли»

Смысл:
ошибка не как позор, а как источник архитектуры.

Материал:
- Booster wiring gap;
- reasoning-only;
- checker/spec mismatch;
- verifier created __pycache__ in immutable package;
- broker 4 vs 7 vs policy 32;
- SSH hop omission.

Форматы:
- Telegram: рубрика «Грабли недели» без искусственной периодичности;
- портал: engineering case study;
- книга: сцены переломов.

### Поток 3. «Capability != Authority»

Смысл:
система может уметь больше, чем ей разрешено делать.

Материал:
- mazhor VERIFY;
- one-shot Booster authorities;
- memory-layering consumed authority after claim;
- journal/publication boundaries;
- recovery/writer/chat split.

Форматы:
- Telegram: короткие объяснения через реальные эпизоды;
- портал: отдельная страница принципов проекта;
- investor/partner materials: как governance встроен в технологию.

### Поток 4. «Человек и Сущности»

Смысл:
как меняется интерфейс человека с группой нейронных и программных исполнителей.

Материал:
- OPERATOR not courier;
- manual activation;
- readable-first;
- working circles;
- human decision packet;
- recovery without using human as backup memory.

Форматы:
- Telegram series;
- portal explainer;
- публичные выступления;
- центральная линия будущей книги.

### Поток 5. «Быстрая память / продолжение работы»

Смысл:
почему сохранить файлы недостаточно, если новый экземпляр не может продолжить причинную цепочку.

Материал:
- memory-layering runtime admission;
- broker budget mismatch;
- verifier mutation;
- recovery semantic gap;
- Entity != chat;
- ARH experience cards.

Форматы:
- технический портал;
- длинная статья;
- позже — образовательный материал ШКОЛЫ.

Пока не делать публичных заявлений о production-ready Fast Memory.

### Поток 6. «Смешные ситуации»

Смысл:
реальная жизнь человека рядом с техникой и системой.

Первый кандидат:
`Как солдат назначил смартфон командиром`.

Будущие источники:
- человеческие абсурды интерфейсов;
- буквальное исполнение неправильной инструкции;
- система, которая умеет отчитаться, но не сделать простое действие;
- технические ситуации, где юмор не требует раскрывать чувствительные детали.

Форматы:
- Telegram;
- отдельный раздел портала;
- вставки между серьёзными главами книги.

### Поток 7. «От мечты к системе»

Смысл:
ранняя авторская фантазия → реальная система → исправление исходной мечты.

Материал:
- «Как мы строили гараж»;
- «Сначала она была выдумана»;
- поздние principles: verification, authority, memory, cooperation.

Форматы:
- длинные публикации;
- портал;
- литературный цикл / книга.

## 3. Редакционная очередь по готовности

### Tier A — почти готово к подготовке под площадку

1. «Как солдат назначил смартфон командиром»
   - жанр: юмор;
   - требуется: copyedit + platform cut;
   - публикация пока не разрешена.

2. «Сначала она была выдумана»
   - литературный кандидат уже существует;
   - current state требует OPERATOR release decision.

3. Booster development episode
   - narrative уже собран;
   - требуется адаптация из внутреннего журнала в публичный case study;
   - обязательно сохранить границы N=1/N=2 и отсутствие общего utility verdict.

4. Working circles
   - сильный самостоятельный сюжет;
   - лучше подавать как исследование гипотезы, а не новую организационную доктрину.

### Tier B — требуется редакторская сборка

5. Memory-layering: «проверяющий изменил объект проверки»
   - очень сильный engineering story;
   - можно собрать с broker 4/7/32 и consumed authority в одну главу.

6. «Entity != chat»
   - уже есть в литературном журнале;
   - требует отдельной публичной версии без внутренних recovery-path подробностей.

7. «ОПЕРАТОР не должен быть курьером»
   - годится как продуктовая/UX история проекта;
   - можно связать с Telegram facilitator / Work / будущим orchestrator.

8. Human-interface conveyor failure
   - лучше объединить с предыдущим, а не публиковать как дубль.

### Tier C — внутренний источник, не прямой паблик

9. ARH experience cards.
10. SIS work journal.
11. raw journal-source с host identities/paths.
12. текущие technical blockers без завершённого causal arc.

## 4. Информационный поток

### Source layer

`Entity terminal/result → journal-source / experience card / OPERATOR draft`

### Editorial intake

RED принимает:
- exact source locator;
- human summary;
- status/boundary;
- privacy/public relevance.

RED не обязан публиковать каждый source.

### Narrative synthesis

RED решает:
- standalone;
- merge into existing arc;
- defer;
- reject as routine/duplicate.

Результат:
`RED narrative candidate`.

### Channel adaptation

Один narrative не копируется одинаково везде.

**Telegram**
- один конфликт;
- один человеческий вывод;
- минимум служебных деталей;
- ссылка/переход на длинный материал при наличии.

**Portal**
- полный causal story;
- «что было / что сделали / чему научились / где границы»;
- technical provenance вторым слоем.

**Longform / book**
- сцена;
- человеческая память;
- verified project facts;
- изменение взгляда/архитектуры;
- связь со следующей главой.

**School**
- lesson/case;
- исходная ошибка;
- diagnostic question;
- правильная граница;
- anti-regression exercise.

**Investor/partner layer**
- только эпизоды, демонстрирующие product/governance maturity;
- без обещаний доходности или market success;
- technical readiness и business value не смешивать.

## 5. Как не превратить поток в контент-фабрику

Не устанавливать обязательный календарный постинг.

Вместо этого использовать event-driven модель:
1. возник значимый causal episode;
2. source попал RED;
3. RED либо слил его с существующей линией, либо создал candidate;
4. candidate лежит в content inventory;
5. когда медиаконтур имеет ресурс/слот, выбирается лучший candidate под задачу канала.

То есть:
`проект производит события → RED производит истории → медиаконтур выбирает истории`,
а не:
`медиаконтур требует пост по расписанию → все начинают производить слова`.

## 6. Минимальные рабочие реестры

Не создавать отдельный документ на каждый source.

Достаточно двух RED current-файлов:

1. `RED__content-inventory-r01.md`
   - content_id;
   - title;
   - source refs;
   - stream;
   - maturity: raw / narrative / platform-ready / held;
   - privacy/public boundary;
   - possible channels;
   - duplication/merge target.

2. `RED__media-flow-r01.md`
   - channel purpose;
   - admissible content classes;
   - transformation needed;
   - release gate;
   - downstream owner.

Этот документ r0.1 может служить basis для их создания отдельным bounded RED step, если KOO/OPERATOR сочтёт это нужным.

## 7. Рекомендованный запуск при появлении медиаресурса

Не начинать с автоматизации.

Первый bounded media cycle:
1. RED выбирает 3 Tier-A materials;
2. готовит Telegram version + portal longform mapping;
3. KAN делает только необходимые public/privacy checks;
4. KOO формирует release decision packet;
5. OPERATOR утверждает/держит/возвращает;
6. WEB публикует exact approved artifact;
7. readback;
8. RED фиксирует, что опубликовано и какие derivative formats ещё допустимы.

Только после 3–5 реальных publication cycles имеет смысл проектировать автоматизацию.

## 8. Приоритет первой медиапачки

Если выбирать не по хронологии, а по разнообразию аудитории:

1. **Юмор:** «Как солдат назначил смартфон командиром».
2. **Человеческая история проекта:** «Сначала она была выдумана».
3. **Engineering case:** Booster.
4. **Организационная гипотеза:** working circles.
5. **Глубокий technical/human essay:** memory-layering / verifier changed object.

Так первая пачка сразу показывает, что проект не является ни чисто техническим блогом, ни мотивационной лентой, ни криптоканалом.

## 9. Следующий causal step

KOO должен fresh-reconcile этот editorial plan с текущим media/WEB state.

Если media resources/publication authority ещё не готовы:
- сохранить plan в queue;
- не создавать publication tasks раньше времени.

Если готов bounded media slot:
- активировать RED для создания exact content inventory + first 3-item publication batch;
- вернуть OPERATOR ready `АДРЕСАТ + PROMPT + ДЕЙСТВИЕ`.

---
sender: RED / РЕДАКТОР
recipient: KOO / КООРДИНАТОР
purpose: journal content audit + media information-flow plan
status: editorial planning result; no publication authorization
